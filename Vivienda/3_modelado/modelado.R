suppressPackageStartupMessages({
  library(dplyr)
  library(glue)
  library(prophet)
  library(purrr)
  library(tidyr)
})

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
    }, error = function(error) NULL)

    if (is.null(model)) {
      return(rep(NA_real_, h))
    }

    return(tryCatch(
      as.numeric(forecast::forecast(model, h = h)$mean),
      error = function(error) rep(NA_real_, h)
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
    }, error = function(error) NULL)

    if (is.null(model)) {
      return(rep(NA_real_, h))
    }

    forecast <- tryCatch({
      future <- prophet::make_future_dataframe(model, periods = h, freq = "year")
      stats::predict(model, future)
    }, error = function(error) NULL)

    return(if (is.null(forecast)) rep(NA_real_, h) else as.numeric(tail(forecast$yhat, h)))
  }

  stop(sprintf("Algoritmo no soportado: %s", algorithm), call. = FALSE)
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

fit_global_algorithm <- function(train_df, algorithm) {
  if (nrow(train_df) < 10) {
    return(NULL)
  }

  if (identical(algorithm, "RF")) {
    return(tryCatch(
      ranger::ranger(
        value ~ periodo + lag_1 + lag_2 + media_hist + entity_id,
        data = train_df,
        num.trees = 500,
        seed = 42
      ),
      error = function(error) NULL
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
      error = function(error) NULL
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
      error = function(error) rep(NA_real_, nrow(newdata))
    ))
  }

  if (identical(algorithm, "XGBoost")) {
    return(tryCatch(
      as.numeric(stats::predict(model, xgboost::xgb.DMatrix(xgb_matrix(newdata)))),
      error = function(error) rep(NA_real_, nrow(newdata))
    ))
  }

  stop(sprintf("Algoritmo global no soportado: %s", algorithm), call. = FALSE)
}

validation_keys <- function(prepared, group_cols, validation_years, min_points) {
  prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (dplyr::n_distinct(group_df$periodo) < min_points) {
        return(tibble::tibble())
      }
      periods <- sort(unique(group_df$periodo))
      h <- min(validation_years, length(periods) - min_points + 1L)
      if (h <= 0) {
        return(tibble::tibble())
      }
      result <- tibble::tibble(periodo = tail(periods, h))
      for (group_col in group_cols) {
        result[[group_col]] <- group_df[[group_col]][[1]]
      }
      result |>
        dplyr::select(dplyr::all_of(group_cols), "periodo")
    })
}

validate_global_algorithm <- function(prepared, value_col, algorithm, validation_years = 3L, min_points = 5L) {
  group_cols <- intersect(c("ccaa", "genero"), names(prepared))
  keys <- validation_keys(prepared, group_cols, validation_years, min_points)
  if (nrow(keys) == 0) {
    return(tibble::tibble())
  }

  features <- build_global_features(prepared, group_cols)
  if (nrow(features) == 0) {
    return(tibble::tibble())
  }

  by_cols <- c(group_cols, "periodo")
  test <- dplyr::semi_join(features, keys, by = by_cols)
  train <- dplyr::anti_join(features, keys, by = by_cols)

  if (nrow(test) == 0) {
    return(tibble::tibble())
  }

  model <- fit_global_algorithm(train, algorithm)
  preds <- predict_global_algorithm(model, test, algorithm)

  test |>
    dplyr::mutate(variable = value_col, algoritmo = algorithm, predicho = preds) |>
    dplyr::transmute(
      dplyr::across(dplyr::all_of(group_cols)),
      variable = .data$variable,
      algoritmo = .data$algoritmo,
      periodo = .data$periodo,
      observado = .data$value,
      predicho = .data$predicho
    )
}

validate_projection_algorithm <- function(df, value_col, algorithm, validation_years = 3L, min_points = 5L) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  prepared <- prepare_model_input(df, value_col)
  if (nrow(prepared) == 0) {
    return(tibble::tibble())
  }

  if (algorithm %in% c("RF", "XGBoost")) {
    return(validate_global_algorithm(prepared, value_col, algorithm, validation_years, min_points))
  }

  prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (dplyr::n_distinct(group_df$periodo) < min_points) {
        return(tibble::tibble())
      }

      periods <- sort(unique(group_df$periodo))
      h <- min(validation_years, length(periods) - min_points + 1L)
      if (h <= 0) {
        return(tibble::tibble())
      }

      validation_periods <- tail(periods, h)
      train_df <- dplyr::filter(group_df, !.data$periodo %in% validation_periods)
      test_df <- dplyr::filter(group_df, .data$periodo %in% validation_periods)
      preds <- fit_predict_algorithm(train_df, algorithm, length(validation_periods))

      result <- tibble::tibble(
        variable = value_col,
        algoritmo = algorithm,
        periodo = validation_periods,
        observado = test_df$value[match(validation_periods, test_df$periodo)],
        predicho = preds
      )

      for (group_col in group_cols) {
        result[[group_col]] <- group_df[[group_col]][[1]]
      }

      result |>
        dplyr::select(dplyr::all_of(group_cols), "variable", "algoritmo", "periodo", "observado", "predicho")
    })
}

evaluate_projection_algorithms <- function(tables, value_cols, validation_years = 3L) {
  algorithms <- projection_algorithms()

  predictions <- purrr::imap_dfr(
    tables,
    function(df, value_col) {
      purrr::map_dfr(
        algorithms,
        function(algorithm) validate_projection_algorithm(df, value_col, algorithm, validation_years = validation_years)
      )
    }
  )

  if (nrow(predictions) == 0) {
    fallback <- if ("ETS" %in% algorithms) "ETS" else algorithms[[1]]
    log_event("WARN", glue("No se pudieron validar algoritmos; se usará {fallback}"))
    return(list(
      selected_algorithm = fallback,
      metrics = tibble::tibble(),
      predictions = predictions
    ))
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

  if (any(global_metrics$candidato_global)) {
    selected <- global_metrics |>
      dplyr::filter(.data$candidato_global) |>
      dplyr::slice_min(.data$error_global, n = 1, with_ties = FALSE) |>
      dplyr::pull(.data$algoritmo)
  } else {
    selected <- global_metrics |>
      dplyr::arrange(dplyr::desc(.data$variables_validas), .data$error_global) |>
      dplyr::slice(1) |>
      dplyr::pull(.data$algoritmo)
    log_event("WARN", glue("Ningún algoritmo superó la cobertura mínima en todas las variables; se usará {selected} por mejor cobertura/error."))
  }

  log_event("INFO", "Evaluación de algoritmos de proyección por error normalizado global")
  print(global_metrics)
  log_event("OK", glue("Algoritmo global seleccionado para variables modeladas: {selected}"))

  list(
    selected_algorithm = selected,
    metrics = global_metrics,
    variable_metrics = variable_metrics,
    predictions = predictions
  )
}

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
      if (is.null(model) || dplyr::n_distinct(group_df$periodo) < min_points) {
        return(tibble::tibble())
      }

      group_df <- dplyr::arrange(group_df, .data$periodo)
      last_period <- max(group_df$periodo, na.rm = TRUE)
      if (last_period >= target_year) {
        return(tibble::tibble())
      }

      entity <- entity_key(group_df[1, group_cols, drop = FALSE], group_cols)[[1]]
      entity_int <- match(entity, entity_levels)
      if (is.na(entity_int)) {
        return(tibble::tibble())
      }

      vals_hist <- group_df$value
      future_periods <- seq.int(last_period + 1L, target_year)
      rows <- list()

      for (period in future_periods) {
        n <- length(vals_hist)
        if (n < 2) {
          next
        }

        newdata <- tibble::tibble(
          periodo = period,
          lag_1 = vals_hist[[n]],
          lag_2 = vals_hist[[n - 1L]],
          media_hist = mean(vals_hist, na.rm = TRUE),
          entity_id = factor(entity, levels = entity_levels),
          entity_id_int = entity_int
        )

        pred <- predict_global_algorithm(model, newdata, algorithm)[[1]]
        if (is.na(pred)) {
          next
        }

        row <- tibble::tibble(periodo = period, origen = "proyeccion", value = pred)
        for (group_col in group_cols) {
          row[[group_col]] <- group_df[[group_col]][[1]]
        }
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
  prepared <- prepare_model_input(df, value_col)

  if (algorithm %in% c("RF", "XGBoost")) {
    return(project_global_series(df, value_col, target_year, algorithm, min_points))
  }

  actual <- prepared |>
    dplyr::mutate(origen = "real") |>
    dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")

  projected <- prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (dplyr::n_distinct(group_df$periodo) < min_points) {
        return(tibble::tibble())
      }

      last_period <- max(group_df$periodo, na.rm = TRUE)
      if (last_period >= target_year) {
        return(tibble::tibble())
      }

      future_periods <- seq.int(last_period + 1L, target_year)
      preds <- fit_predict_algorithm(group_df, algorithm, length(future_periods))

      future_rows <- tibble::tibble(
        periodo = future_periods,
        origen = "proyeccion",
        value = as.numeric(preds)
      ) |>
        dplyr::filter(!is.na(.data$value))

      for (group_col in group_cols) {
        future_rows[[group_col]] <- group_df[[group_col]][[1]]
      }

      future_rows |>
        dplyr::select(dplyr::all_of(group_cols), "periodo", "origen", "value")
    })

  dplyr::bind_rows(actual, projected) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$periodo, .data$origen) |>
    dplyr::rename(!!value_col := value)
}

run_modelado <- function(cfg) {
  log_event("INFO", "Iniciando modelado")

  transformed <- load_named_rds(
    cfg$transform_dir,
    c(
      "dif_finmes",
      "espacio_insuf",
      "gasto_elevado",
      "hogares_mono",
      "precio_alquiler",
      "precio_venta",
      "retrasos_pagos",
      "salario_mediano"
    )
  )

  modelable <- transformed[c("dif_finmes", "espacio_insuf", "gasto_elevado", "hogares_mono", "retrasos_pagos", "salario_mediano")]
  selection <- evaluate_projection_algorithms(modelable, names(modelable), validation_years = cfg$model_validation_years)
  selected_algorithm <- selection$selected_algorithm
  target_year <- cfg$projection_target_year

  modeled <- list(
    dif_finmes = project_series(transformed$dif_finmes, "dif_finmes", target_year, selected_algorithm),
    espacio_insuf = project_series(transformed$espacio_insuf, "espacio_insuf", target_year, selected_algorithm),
    gasto_elevado = project_series(transformed$gasto_elevado, "gasto_elevado", target_year, selected_algorithm),
    hogares_mono = project_series(transformed$hogares_mono, "hogares_mono", target_year, selected_algorithm),
    precio_alquiler = dplyr::mutate(transformed$precio_alquiler, origen = "real"),
    precio_venta = dplyr::mutate(transformed$precio_venta, origen = "real"),
    retrasos_pagos = project_series(transformed$retrasos_pagos, "retrasos_pagos", target_year, selected_algorithm),
    salario_mediano = project_series(transformed$salario_mediano, "salario_mediano", target_year, selected_algorithm)
  )

  salario_destinado <- modeled$salario_mediano |>
    dplyr::left_join(
      dplyr::rename(modeled$precio_alquiler, origen_precio = origen),
      by = c("ccaa", "periodo")
    ) |>
    dplyr::mutate(
      origen = dplyr::case_when(
        is.na(.data$precio_alquiler) | is.na(.data$salario_mediano) ~ .data$origen,
        .data$origen == "real" & .data$origen_precio == "real" ~ "real",
        TRUE ~ "proyeccion"
      ),
      salario_destinado = (.data$precio_alquiler / (.data$salario_mediano / 12)) * 100
    ) |>
    dplyr::filter(!is.na(.data$salario_destinado)) |>
    dplyr::select("ccaa", "periodo", "genero", "origen", "salario_destinado")

  outputs <- c(
    modeled[c("dif_finmes", "espacio_insuf", "gasto_elevado", "hogares_mono", "precio_alquiler", "precio_venta", "retrasos_pagos")],
    list(salario_destinado = salario_destinado)
  )

  save_named_rds(outputs, cfg$model_dir)
  saveRDS(selection, file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion.rds"))
  utils::write.csv2(selection$metrics, file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_global.csv"), row.names = FALSE)
  utils::write.csv2(selection$variable_metrics, file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_variables.csv"), row.names = FALSE)
  log_event("OK", glue("Modelado completado: {length(outputs)} datasets | algoritmo={selected_algorithm} | proyección hasta {target_year}"))

  invisible(outputs)
}
