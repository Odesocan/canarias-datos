suppressPackageStartupMessages({
  require_packages(c("dplyr", "glue", "purrr", "tibble", "tidyr"))
  library(dplyr)
  library(glue)
  library(purrr)
  library(tibble)
  library(tidyr)
})

# ----------------------------------------------------------------------------
# Inventario de algoritmos disponibles
# ----------------------------------------------------------------------------

projection_algorithms <- function() {
  algorithms <- character(0)
  if (requireNamespace("forecast", quietly = TRUE)) {
    algorithms <- c(algorithms, "ARIMA", "ETS")
  }
  if (requireNamespace("prophet", quietly = TRUE)) {
    algorithms <- c(algorithms, "Prophet")
  }
  if (requireNamespace("ranger", quietly = TRUE)) {
    algorithms <- c(algorithms, "RF")
  }
  if (requireNamespace("xgboost", quietly = TRUE)) {
    algorithms <- c(algorithms, "XGBoost")
  }
  if (length(algorithms) == 0) {
    stop("No hay algoritmos de proyección disponibles. Instala forecast, prophet, ranger o xgboost.", call. = FALSE)
  }
  algorithms
}

# ----------------------------------------------------------------------------
# Preparación de datos
# ----------------------------------------------------------------------------

prepare_model_input <- function(df, value_col) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  df |>
    dplyr::mutate(
      periodo = as.integer(.data$periodo),
      value = as.numeric(.data[[value_col]])
    ) |>
    dplyr::filter(!is.na(.data$periodo), !is.na(.data$value)) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$periodo)
}

entity_key <- function(data, group_cols) {
  if (length(group_cols) == 0) {
    return(rep("serie", nrow(data)))
  }
  do.call(paste, c(data[group_cols], sep = " | "))
}

build_global_features <- function(prepared, group_cols) {
  prepared |>
    dplyr::mutate(.entity = entity_key(dplyr::pick(dplyr::all_of(group_cols)), group_cols)) |>
    dplyr::group_by(.data$.entity) |>
    dplyr::arrange(.data$periodo, .by_group = TRUE) |>
    dplyr::mutate(
      lag_1 = dplyr::lag(.data$value, 1),
      lag_2 = dplyr::lag(.data$value, 2),
      media_hist = dplyr::lag(dplyr::cummean(.data$value)),
      entity_id = factor(.data$.entity, levels = sort(unique(.data$.entity))),
      entity_id_int = as.integer(.data$entity_id)
    ) |>
    dplyr::ungroup() |>
    dplyr::filter(!is.na(.data$lag_1), !is.na(.data$lag_2), !is.na(.data$media_hist))
}

xgb_matrix <- function(data) {
  cols <- c("periodo", "lag_1", "lag_2", "media_hist", "entity_id_int")
  matrix(
    as.double(c(data$periodo, data$lag_1, data$lag_2, data$media_hist, data$entity_id_int)),
    nrow = nrow(data),
    ncol = length(cols),
    byrow = FALSE,
    dimnames = list(NULL, cols)
  )
}

# ----------------------------------------------------------------------------
# Fit + predicción por algoritmo
# ----------------------------------------------------------------------------

fit_predict_algorithm <- function(train_df, algorithm, h) {
  if (nrow(train_df) < 4 || h <= 0) {
    return(rep(NA_real_, h))
  }

  if (algorithm %in% c("ARIMA", "ETS")) {
    ts_obj <- stats::ts(train_df$value, start = min(train_df$periodo), frequency = 1)
    model <- tryCatch({
      if (identical(algorithm, "ARIMA")) {
        forecast::auto.arima(ts_obj, stepwise = TRUE, approximation = TRUE)
      } else {
        forecast::ets(ts_obj)
      }
    }, error = function(e) NULL)
    if (is.null(model)) return(rep(NA_real_, h))
    return(tryCatch(
      as.numeric(forecast::forecast(model, h = h)$mean),
      error = function(e) rep(NA_real_, h)
    ))
  }

  if (identical(algorithm, "Prophet")) {
    prophet_input <- tibble::tibble(
      ds = as.Date(sprintf("%d-01-01", train_df$periodo)),
      y = train_df$value
    )
    model <- tryCatch({
      suppressWarnings(suppressMessages(prophet::prophet(
        prophet_input,
        yearly.seasonality = FALSE,
        weekly.seasonality = FALSE,
        daily.seasonality = FALSE,
        n.changepoints = max(0, min(10, nrow(prophet_input) - 2))
      )))
    }, error = function(e) NULL)
    if (is.null(model)) return(rep(NA_real_, h))
    forecast <- tryCatch({
      future <- prophet::make_future_dataframe(model, periods = h, freq = "year")
      stats::predict(model, future)
    }, error = function(e) NULL)
    return(if (is.null(forecast)) rep(NA_real_, h) else as.numeric(tail(forecast$yhat, h)))
  }

  stop(sprintf("Algoritmo no soportado: %s", algorithm), call. = FALSE)
}

fit_global_algorithm <- function(train_df, algorithm) {
  if (nrow(train_df) < 10) return(NULL)

  if (identical(algorithm, "RF")) {
    return(tryCatch(
      ranger::ranger(
        value ~ periodo + lag_1 + lag_2 + media_hist + entity_id,
        data = train_df,
        num.trees = 500,
        seed = 42
      ),
      error = function(e) NULL
    ))
  }

  if (identical(algorithm, "XGBoost")) {
    return(tryCatch(
      xgboost::xgb.train(
        params = list(eta = 0.08, max_depth = 3, objective = "reg:squarederror"),
        data = xgboost::xgb.DMatrix(xgb_matrix(train_df), label = as.double(train_df$value)),
        nrounds = 120,
        verbose = 0
      ),
      error = function(e) NULL
    ))
  }

  stop(sprintf("Algoritmo global no soportado: %s", algorithm), call. = FALSE)
}

predict_global_algorithm <- function(model, newdata, algorithm) {
  if (is.null(model) || nrow(newdata) == 0) {
    return(rep(NA_real_, nrow(newdata)))
  }
  if (identical(algorithm, "RF")) {
    return(tryCatch(
      as.numeric(stats::predict(model, newdata)$predictions),
      error = function(e) rep(NA_real_, nrow(newdata))
    ))
  }
  if (identical(algorithm, "XGBoost")) {
    return(tryCatch(
      as.numeric(stats::predict(model, xgboost::xgb.DMatrix(xgb_matrix(newdata)))),
      error = function(e) rep(NA_real_, nrow(newdata))
    ))
  }
  stop(sprintf("Algoritmo global no soportado: %s", algorithm), call. = FALSE)
}

# ----------------------------------------------------------------------------
# Validación cruzada temporal (rolling origin) — más robusta que hold-out
# ----------------------------------------------------------------------------

# Para cada fold k = 1..K, entrenamos hasta T - K + (k-1) y validamos T - K + k.
# Devuelve una tibble con observado y predicho por (variable, algoritmo, fold,
# grupo, periodo).
temporal_cv_per_series <- function(prepared, value_col, algorithm, cv_folds, min_points) {
  group_cols <- intersect(c("ccaa", "genero"), names(prepared))

  prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      periods <- sort(unique(group_df$periodo))
      if (length(periods) < min_points + cv_folds) {
        return(tibble::tibble())
      }

      results <- list()
      for (k in seq_len(cv_folds)) {
        target <- periods[length(periods) - cv_folds + k]
        train_df <- dplyr::filter(group_df, .data$periodo < target)
        test_df  <- dplyr::filter(group_df, .data$periodo == target)
        if (nrow(test_df) == 0 || nrow(train_df) < min_points) next
        pred <- fit_predict_algorithm(train_df, algorithm, h = 1L)[[1]]
        row <- tibble::tibble(
          variable = value_col,
          algoritmo = algorithm,
          fold = k,
          periodo = target,
          observado = test_df$value[[1]],
          predicho = pred
        )
        for (gc in group_cols) row[[gc]] <- group_df[[gc]][[1]]
        results[[length(results) + 1L]] <- row
      }

      dplyr::bind_rows(results)
    })
}

temporal_cv_global <- function(prepared, value_col, algorithm, cv_folds, min_points) {
  group_cols <- intersect(c("ccaa", "genero"), names(prepared))
  features <- build_global_features(prepared, group_cols)
  if (nrow(features) == 0) return(tibble::tibble())

  all_periods <- sort(unique(features$periodo))
  if (length(all_periods) < min_points + cv_folds) return(tibble::tibble())

  results <- list()
  for (k in seq_len(cv_folds)) {
    target <- all_periods[length(all_periods) - cv_folds + k]
    train <- dplyr::filter(features, .data$periodo < target)
    test  <- dplyr::filter(features, .data$periodo == target)
    if (nrow(test) == 0 || nrow(train) < 10) next
    model <- fit_global_algorithm(train, algorithm)
    preds <- predict_global_algorithm(model, test, algorithm)
    row <- test |>
      dplyr::transmute(
        dplyr::across(dplyr::all_of(group_cols)),
        variable = value_col,
        algoritmo = algorithm,
        fold = k,
        periodo = .data$periodo,
        observado = .data$value,
        predicho = preds
      )
    results[[length(results) + 1L]] <- row
  }
  dplyr::bind_rows(results)
}

evaluate_with_temporal_cv <- function(tables, value_cols, cv_folds = 3L, min_points = 5L) {
  algorithms <- projection_algorithms()

  predictions <- purrr::imap_dfr(
    tables,
    function(df, value_col) {
      prepared <- prepare_model_input(df, value_col)
      if (nrow(prepared) == 0) return(tibble::tibble())
      purrr::map_dfr(algorithms, function(algorithm) {
        if (algorithm %in% c("RF", "XGBoost")) {
          temporal_cv_global(prepared, value_col, algorithm, cv_folds, min_points)
        } else {
          temporal_cv_per_series(prepared, value_col, algorithm, cv_folds, min_points)
        }
      })
    }
  )

  if (nrow(predictions) == 0) {
    fallback <- if ("ETS" %in% algorithms) "ETS" else algorithms[[1]]
    log_event("WARN", glue("No se pudieron validar algoritmos; se usará {fallback}"))
    return(list(selected_algorithm = fallback, metrics = tibble::tibble(), predictions = predictions))
  }

  variable_metrics <- predictions |>
    dplyr::filter(!is.na(.data$observado), !is.na(.data$predicho)) |>
    dplyr::group_by(.data$variable, .data$algoritmo) |>
    dplyr::summarise(
      n_valid = dplyr::n(),
      mae = mean(abs(.data$observado - .data$predicho), na.rm = TRUE),
      scale = mean(abs(.data$observado), na.rm = TRUE),
      nmae = dplyr::if_else(is.na(.data$scale) | .data$scale == 0, .data$mae, .data$mae / .data$scale),
      .groups = "drop"
    )

  expected <- predictions |>
    dplyr::filter(!is.na(.data$observado)) |>
    dplyr::group_by(.data$variable, .data$algoritmo) |>
    dplyr::summarise(n_expected = dplyr::n(), .groups = "drop")

  variable_metrics <- expected |>
    dplyr::left_join(variable_metrics, by = c("variable", "algoritmo")) |>
    dplyr::mutate(
      n_valid = tidyr::replace_na(.data$n_valid, 0L),
      cobertura = dplyr::if_else(.data$n_expected > 0, .data$n_valid / .data$n_expected, 0),
      candidato_variable = .data$cobertura >= 0.70 & !is.na(.data$nmae)
    )

  global_metrics <- variable_metrics |>
    dplyr::group_by(.data$algoritmo) |>
    dplyr::summarise(
      variables_evaluadas = dplyr::n_distinct(.data$variable),
      variables_validas = sum(.data$candidato_variable, na.rm = TRUE),
      cobertura_media = mean(.data$cobertura, na.rm = TRUE),
      error_global = mean(.data$nmae[.data$candidato_variable], na.rm = TRUE),
      candidato_global = .data$variables_validas == .data$variables_evaluadas & !is.na(.data$error_global),
      .groups = "drop"
    ) |>
    dplyr::arrange(.data$error_global)

  if (any(global_metrics$candidato_global, na.rm = TRUE)) {
    selected <- global_metrics |>
      dplyr::filter(.data$candidato_global) |>
      dplyr::slice_min(.data$error_global, n = 1, with_ties = FALSE) |>
      dplyr::pull(.data$algoritmo)
  } else {
    selected <- global_metrics |>
      dplyr::arrange(dplyr::desc(.data$variables_validas), .data$error_global) |>
      dplyr::slice(1) |>
      dplyr::pull(.data$algoritmo)
    log_event("WARN", glue("Ningún algoritmo cubrió todas las variables; se usa {selected} por mejor cobertura/error."))
  }

  log_event("INFO", glue("CV temporal: {cv_folds} folds, métrica = NMAE global"))
  print(global_metrics)
  log_event("OK", glue("Algoritmo seleccionado: {selected}"))

  list(
    selected_algorithm = selected,
    metrics = global_metrics,
    variable_metrics = variable_metrics,
    predictions = predictions
  )
}

# ----------------------------------------------------------------------------
# Proyección: real + proyectado hasta horizon_year
# ----------------------------------------------------------------------------

project_global_series <- function(df, value_col, target_year, algorithm, min_points = 5L) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  prepared <- prepare_model_input(df, value_col)

  actual <- prepared |>
    dplyr::mutate(origen = "real") |>
    dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")

  features <- build_global_features(prepared, group_cols)
  model <- fit_global_algorithm(features, algorithm)
  entity_levels <- if (nrow(features) > 0) levels(features$entity_id) else character(0)

  projected <- prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (is.null(model) || dplyr::n_distinct(group_df$periodo) < min_points) return(tibble::tibble())
      group_df <- dplyr::arrange(group_df, .data$periodo)
      last_period <- max(group_df$periodo, na.rm = TRUE)
      if (last_period >= target_year) return(tibble::tibble())

      entity <- entity_key(group_df[1, group_cols, drop = FALSE], group_cols)[[1]]
      entity_int <- match(entity, entity_levels)
      if (is.na(entity_int)) return(tibble::tibble())

      vals_hist <- group_df$value
      future_periods <- seq.int(last_period + 1L, target_year)
      rows <- list()
      for (period in future_periods) {
        n <- length(vals_hist)
        if (n < 2) next
        newdata <- tibble::tibble(
          periodo = period,
          lag_1 = vals_hist[[n]],
          lag_2 = vals_hist[[n - 1L]],
          media_hist = mean(vals_hist, na.rm = TRUE),
          entity_id = factor(entity, levels = entity_levels),
          entity_id_int = entity_int
        )
        pred <- predict_global_algorithm(model, newdata, algorithm)[[1]]
        if (is.na(pred)) next
        row <- tibble::tibble(periodo = period, origen = "proyeccion", value = pred)
        for (gc in group_cols) row[[gc]] <- group_df[[gc]][[1]]
        rows[[length(rows) + 1L]] <- row |>
          dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")
        vals_hist <- c(vals_hist, pred)
      }
      dplyr::bind_rows(rows)
    })

  dplyr::bind_rows(actual, projected) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$periodo, .data$origen) |>
    dplyr::rename(!!value_col := value)
}

project_series <- function(df, value_col, target_year, algorithm, min_points = 5L) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))

  if (algorithm %in% c("RF", "XGBoost")) {
    return(project_global_series(df, value_col, target_year, algorithm, min_points))
  }

  prepared <- prepare_model_input(df, value_col)

  actual <- prepared |>
    dplyr::mutate(origen = "real") |>
    dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")

  projected <- prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (dplyr::n_distinct(group_df$periodo) < min_points) return(tibble::tibble())
      last_period <- max(group_df$periodo, na.rm = TRUE)
      if (last_period >= target_year) return(tibble::tibble())
      future_periods <- seq.int(last_period + 1L, target_year)
      preds <- fit_predict_algorithm(group_df, algorithm, length(future_periods))
      future_rows <- tibble::tibble(
        periodo = future_periods,
        origen = "proyeccion",
        value = as.numeric(preds)
      ) |>
        dplyr::filter(!is.na(.data$value))
      for (gc in group_cols) future_rows[[gc]] <- group_df[[gc]][[1]]
      future_rows |>
        dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")
    })

  dplyr::bind_rows(actual, projected) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$periodo, .data$origen) |>
    dplyr::rename(!!value_col := value)
}

# ----------------------------------------------------------------------------
# Etiquetas (variables auxiliares para tooltip)
# ----------------------------------------------------------------------------

add_label_variables <- function(df) {
  df |>
    dplyr::mutate(
      n_personas_tm = dplyr::if_else(
        !is.na(.data$t_mental) & !is.na(.data$censo),
        round((.data$t_mental / 100) * .data$censo),
        NA_real_
      ),
      antidep_anual_total = dplyr::if_else(
        !is.na(.data$antidep_ajustado) & !is.na(.data$censo),
        round((.data$antidep_ajustado / 1000) * 365 * .data$censo),
        NA_real_
      ),
      hipno_anual_total = dplyr::if_else(
        !is.na(.data$hipno_ajustado) & !is.na(.data$censo),
        round((.data$hipno_ajustado / 1000) * 365 * .data$censo),
        NA_real_
      ),
      n_suicidios = dplyr::if_else(
        !is.na(.data$suicidios) & !is.na(.data$censo),
        round((.data$suicidios / 100000) * .data$censo),
        NA_real_
      )
    )
}

# ----------------------------------------------------------------------------
# Pipeline principal
# ----------------------------------------------------------------------------

run_modelado <- function(cfg) {
  log_event("INFO", "Iniciando modelado")

  ced_saludmental_real <- load_named_rds(cfg$transform_dir, c("ced_saludmental"))$ced_saludmental

  # Variables a proyectar (las primarias). brecha_rel se recalcula post-hoc.
  primary_vars <- c("t_mental", "antidep_ajustado", "hipno_ajustado", "suicidios", "censo")

  primary_tables <- purrr::set_names(primary_vars) |>
    purrr::map(function(v) {
      ced_saludmental_real |>
        dplyr::select(dplyr::all_of(c("ccaa", "periodo", "genero", v))) |>
        dplyr::filter(!is.na(.data[[v]]))
    })

  selection <- evaluate_with_temporal_cv(
    primary_tables,
    primary_vars,
    cv_folds = cfg$cv_folds,
    min_points = 5L
  )
  selected_algorithm <- selection$selected_algorithm
  target_year <- cfg$horizon_year

  projected <- purrr::imap(primary_tables, function(df, v) {
    out <- project_series(df, v, target_year, selected_algorithm)
    # Renombramos `origen` a `<v>_origen` para que cada variable conserve su
    # marca real/proyeccion sin colisionar al hacer full_join.
    dplyr::rename(out, !!paste0(v, "_origen") := "origen")
  })

  # Combinar por (ccaa, periodo, genero); origen global se deriva después.
  ced_modelado <- purrr::reduce(
    projected,
    function(left, right) {
      dplyr::full_join(left, right, by = c("ccaa", "periodo", "genero"))
    }
  )

  # `origen` global: "real" si todas las variables presentes son reales,
  # "proyeccion" si al menos una es proyectada.
  origen_cols <- paste0(primary_vars, "_origen")
  origen_present <- intersect(origen_cols, names(ced_modelado))

  ced_modelado$origen <- apply(
    ced_modelado[, origen_present, drop = FALSE],
    1,
    function(row) {
      vals <- row[!is.na(row)]
      if (length(vals) == 0) return(NA_character_)
      if (any(vals == "proyeccion")) return("proyeccion") else return("real")
    }
  )

  # Eliminamos las marcas por variable (auxiliares) del output final.
  ced_modelado <- ced_modelado |>
    dplyr::select(-dplyr::all_of(origen_present))

  # Recalcular brecha_rel desde t_mental hombres/mujeres (en real + proyectado)
  brecha <- ced_modelado |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    dplyr::select("ccaa", "periodo", "origen", "genero", "t_mental") |>
    tidyr::pivot_wider(names_from = "genero", values_from = "t_mental") |>
    dplyr::mutate(
      brecha_rel = dplyr::if_else(
        !is.na(.data$mujeres) & .data$mujeres != 0,
        ((.data$mujeres - .data$hombres) / .data$mujeres) * 100,
        NA_real_
      )
    ) |>
    dplyr::select("ccaa", "periodo", "origen", "brecha_rel")

  ced_modelado <- ced_modelado |>
    dplyr::left_join(brecha, by = c("ccaa", "periodo", "origen")) |>
    add_label_variables() |>
    dplyr::arrange(.data$ccaa, .data$periodo, .data$genero, .data$origen)

  assert_unique_keys(ced_modelado, c("ccaa", "periodo", "genero", "origen"), "ced_saludmental modelado")
  log_series_coverage(ced_modelado, "ced_saludmental modelado")

  save_named_rds(list(ced_saludmental = ced_modelado), cfg$model_dir)
  saveRDS(selection, file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion.rds"))
  utils::write.csv2(selection$metrics,
                    file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_global.csv"),
                    row.names = FALSE)
  utils::write.csv2(selection$variable_metrics,
                    file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_variables.csv"),
                    row.names = FALSE)
  log_event("OK", glue("Modelado completado: algoritmo={selected_algorithm} | proyección hasta {target_year}"))

  invisible(list(ced_saludmental = ced_modelado))
}
