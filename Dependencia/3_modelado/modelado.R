# ===========================================================================
# modelado.R -- Proyeccion mensual multi-algoritmo (cuaderno v2 §11.5)
# ===========================================================================
# Patron Salud Mental / Vivienda adaptado a granularidad mensual:
#   ARIMA, ETS, Prophet (per-serie) + RF, XGBoost (global con features de lag)
#   Seleccion automatica por CV temporal rolling-origin (3 folds, 1 mes ahead).
#   Proyeccion de los 10 indicadores del dashboard hasta horizonte (default
#   ultimo mes real + 12).
# ===========================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "purrr", "tibble", "tidyr", "lubridate", "glue"))
  library(dplyr); library(purrr); library(tibble)
  library(tidyr); library(lubridate); library(glue)
})

# ---------------------------------------------------------------------------
# Inventario de algoritmos disponibles
# ---------------------------------------------------------------------------

projection_algorithms <- function(include_prophet = FALSE) {
  algorithms <- character(0)
  if (requireNamespace("forecast", quietly = TRUE)) algorithms <- c(algorithms, "ARIMA", "ETS")
  if (isTRUE(include_prophet) && requireNamespace("prophet", quietly = TRUE)) {
    algorithms <- c(algorithms, "Prophet")
  }
  if (requireNamespace("ranger",   quietly = TRUE)) algorithms <- c(algorithms, "RF")
  if (requireNamespace("xgboost",  quietly = TRUE)) algorithms <- c(algorithms, "XGBoost")
  if (length(algorithms) == 0) {
    stop("No hay algoritmos disponibles. Instala forecast, ranger o xgboost.", call. = FALSE)
  }
  algorithms
}

# ---------------------------------------------------------------------------
# Preparacion de datos (granularidad mensual)
# ---------------------------------------------------------------------------

prepare_model_input <- function(df, value_col) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  df |>
    dplyr::mutate(
      fecha = as.Date(.data$fecha),
      value = as.numeric(.data[[value_col]])
    ) |>
    dplyr::filter(!is.na(.data$fecha), !is.na(.data$value)) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$fecha)
}

entity_key <- function(data, group_cols) {
  if (length(group_cols) == 0) return(rep("serie", nrow(data)))
  do.call(paste, c(data[group_cols], sep = " | "))
}

build_global_features <- function(prepared, group_cols) {
  prepared |>
    dplyr::mutate(
      .entity = entity_key(dplyr::pick(dplyr::all_of(group_cols)), group_cols),
      mes_num = lubridate::month(.data$fecha),
      anio = lubridate::year(.data$fecha),
      t_idx = (anio - min(anio, na.rm = TRUE)) * 12 + mes_num
    ) |>
    dplyr::group_by(.data$.entity) |>
    dplyr::arrange(.data$fecha, .by_group = TRUE) |>
    dplyr::mutate(
      lag_1  = dplyr::lag(.data$value, 1),
      lag_2  = dplyr::lag(.data$value, 2),
      lag_12 = dplyr::lag(.data$value, 12),
      media_hist = dplyr::lag(dplyr::cummean(.data$value)),
      entity_id = factor(.data$.entity, levels = sort(unique(.data$.entity))),
      entity_id_int = as.integer(.data$entity_id)
    ) |>
    dplyr::ungroup() |>
    dplyr::filter(!is.na(.data$lag_1), !is.na(.data$lag_2), !is.na(.data$media_hist)) |>
    dplyr::mutate(lag_12 = dplyr::coalesce(.data$lag_12, .data$media_hist))
}

xgb_matrix <- function(data) {
  cols <- c("t_idx", "mes_num", "lag_1", "lag_2", "lag_12", "media_hist", "entity_id_int")
  matrix(
    as.double(c(data$t_idx, data$mes_num, data$lag_1, data$lag_2,
                data$lag_12, data$media_hist, data$entity_id_int)),
    nrow = nrow(data), ncol = length(cols), byrow = FALSE,
    dimnames = list(NULL, cols)
  )
}

# ---------------------------------------------------------------------------
# Fit + prediccion por algoritmo
# ---------------------------------------------------------------------------

fit_predict_algorithm <- function(train_df, algorithm, h) {
  if (nrow(train_df) < 6 || h <= 0) return(rep(NA_real_, h))

  if (algorithm %in% c("ARIMA", "ETS")) {
    start_d <- min(train_df$fecha)
    ts_obj <- stats::ts(
      train_df$value,
      start = c(lubridate::year(start_d), lubridate::month(start_d)),
      frequency = 12
    )
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
    prophet_input <- tibble::tibble(ds = train_df$fecha, y = train_df$value)
    model <- tryCatch({
      suppressWarnings(suppressMessages(prophet::prophet(
        prophet_input,
        yearly.seasonality = TRUE,
        weekly.seasonality = FALSE,
        daily.seasonality  = FALSE,
        n.changepoints = max(0, min(15, nrow(prophet_input) - 2))
      )))
    }, error = function(e) NULL)
    if (is.null(model)) return(rep(NA_real_, h))
    fc <- tryCatch({
      future <- prophet::make_future_dataframe(model, periods = h, freq = "month")
      stats::predict(model, future)
    }, error = function(e) NULL)
    return(if (is.null(fc)) rep(NA_real_, h) else as.numeric(tail(fc$yhat, h)))
  }

  stop(sprintf("Algoritmo no soportado: %s", algorithm), call. = FALSE)
}

fit_global_algorithm <- function(train_df, algorithm) {
  if (nrow(train_df) < 12) return(NULL)

  if (identical(algorithm, "RF")) {
    return(tryCatch(
      ranger::ranger(
        value ~ t_idx + mes_num + lag_1 + lag_2 + lag_12 + media_hist + entity_id,
        data = train_df, num.trees = 500, seed = 42
      ),
      error = function(e) NULL
    ))
  }

  if (identical(algorithm, "XGBoost")) {
    return(tryCatch(
      xgboost::xgb.train(
        params = list(eta = 0.08, max_depth = 4, objective = "reg:squarederror"),
        data = xgboost::xgb.DMatrix(xgb_matrix(train_df), label = as.double(train_df$value)),
        nrounds = 200, verbose = 0
      ),
      error = function(e) NULL
    ))
  }

  stop(sprintf("Algoritmo global no soportado: %s", algorithm), call. = FALSE)
}

predict_global_algorithm <- function(model, newdata, algorithm) {
  if (is.null(model) || nrow(newdata) == 0) return(rep(NA_real_, nrow(newdata)))
  if (identical(algorithm, "RF")) {
    return(tryCatch(as.numeric(stats::predict(model, newdata)$predictions),
                    error = function(e) rep(NA_real_, nrow(newdata))))
  }
  if (identical(algorithm, "XGBoost")) {
    return(tryCatch(as.numeric(stats::predict(model, xgboost::xgb.DMatrix(xgb_matrix(newdata)))),
                    error = function(e) rep(NA_real_, nrow(newdata))))
  }
  stop(sprintf("Algoritmo global no soportado: %s", algorithm), call. = FALSE)
}

# ---------------------------------------------------------------------------
# CV temporal rolling-origin (3 folds, 1 mes ahead)
# ---------------------------------------------------------------------------

temporal_cv_per_series <- function(prepared, value_col, algorithm, cv_folds, min_points) {
  group_cols <- intersect(c("ccaa", "genero"), names(prepared))

  prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      fechas <- sort(unique(group_df$fecha))
      if (length(fechas) < min_points + cv_folds) return(tibble::tibble())

      results <- list()
      for (k in seq_len(cv_folds)) {
        target <- fechas[length(fechas) - cv_folds + k]
        train_df <- dplyr::filter(group_df, .data$fecha < target)
        test_df  <- dplyr::filter(group_df, .data$fecha == target)
        if (nrow(test_df) == 0 || nrow(train_df) < min_points) next
        pred <- fit_predict_algorithm(train_df, algorithm, h = 1L)[[1]]
        row <- tibble::tibble(
          variable = value_col, algoritmo = algorithm, fold = k,
          fecha = target, observado = test_df$value[[1]], predicho = pred
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

  fechas <- sort(unique(features$fecha))
  if (length(fechas) < min_points + cv_folds) return(tibble::tibble())

  results <- list()
  for (k in seq_len(cv_folds)) {
    target <- fechas[length(fechas) - cv_folds + k]
    train <- dplyr::filter(features, .data$fecha < target)
    test  <- dplyr::filter(features, .data$fecha == target)
    if (nrow(test) == 0 || nrow(train) < 12) next
    model <- fit_global_algorithm(train, algorithm)
    preds <- predict_global_algorithm(model, test, algorithm)
    row <- test |>
      dplyr::transmute(
        dplyr::across(dplyr::all_of(group_cols)),
        variable = value_col, algoritmo = algorithm, fold = k,
        fecha = .data$fecha, observado = .data$value, predicho = preds
      )
    results[[length(results) + 1L]] <- row
  }
  dplyr::bind_rows(results)
}

evaluate_with_temporal_cv <- function(tables, value_cols, cv_folds = 3L, min_points = 12L,
                                       include_prophet = FALSE) {
  algorithms <- projection_algorithms(include_prophet = include_prophet)
  log_event("INFO", glue("Algoritmos disponibles: {paste(algorithms, collapse=', ')}"))

  predictions <- purrr::imap_dfr(tables, function(df, value_col) {
    prepared <- prepare_model_input(df, value_col)
    if (nrow(prepared) == 0) return(tibble::tibble())
    purrr::map_dfr(algorithms, function(algorithm) {
      if (algorithm %in% c("RF", "XGBoost")) {
        temporal_cv_global(prepared, value_col, algorithm, cv_folds, min_points)
      } else {
        temporal_cv_per_series(prepared, value_col, algorithm, cv_folds, min_points)
      }
    })
  })

  if (nrow(predictions) == 0) {
    fallback <- if ("ETS" %in% algorithms) "ETS" else algorithms[[1]]
    log_event("WARN", glue("CV temporal sin datos suficientes; fallback={fallback}"))
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
      variables_validas   = sum(.data$candidato_variable, na.rm = TRUE),
      cobertura_media     = mean(.data$cobertura, na.rm = TRUE),
      error_global        = mean(.data$nmae[.data$candidato_variable], na.rm = TRUE),
      candidato_global    = .data$variables_validas == .data$variables_evaluadas & !is.na(.data$error_global),
      .groups = "drop"
    ) |> dplyr::arrange(.data$error_global)

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
    log_event("WARN", glue("Ningun algoritmo cubre todas las variables; se usa {selected} por mejor cobertura/error."))
  }

  log_event("INFO", glue("CV temporal: {cv_folds} folds | metrica = NMAE global"))
  print(global_metrics)
  log_event("OK", glue("Algoritmo seleccionado: {selected}"))

  list(
    selected_algorithm = selected,
    metrics = global_metrics,
    variable_metrics = variable_metrics,
    predictions = predictions
  )
}

# ---------------------------------------------------------------------------
# Proyeccion: real + proyeccion hasta horizon_end
# ---------------------------------------------------------------------------

month_seq <- function(from_date, to_date) {
  if (from_date > to_date) return(as.Date(character()))
  seq.Date(from_date, to_date, by = "month")
}

project_per_series <- function(df, value_col, horizon_end, algorithm, min_points = 12L) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  prepared <- prepare_model_input(df, value_col)

  actual <- prepared |>
    dplyr::mutate(origen = "real") |>
    dplyr::select(dplyr::all_of(group_cols), "fecha", "origen", "value")

  projected <- prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (dplyr::n_distinct(group_df$fecha) < min_points) return(tibble::tibble())
      last_date <- max(group_df$fecha, na.rm = TRUE)
      future_dates <- month_seq(last_date %m+% months(1), horizon_end)
      if (length(future_dates) == 0) return(tibble::tibble())
      preds <- fit_predict_algorithm(group_df, algorithm, length(future_dates))
      future_rows <- tibble::tibble(
        fecha = future_dates,
        origen = "proyeccion",
        value = as.numeric(preds)
      ) |> dplyr::filter(!is.na(.data$value))
      for (gc in group_cols) future_rows[[gc]] <- group_df[[gc]][[1]]
      future_rows |> dplyr::select(dplyr::all_of(group_cols), "fecha", "origen", "value")
    })

  dplyr::bind_rows(actual, projected) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$fecha, .data$origen) |>
    dplyr::rename(!!value_col := value)
}

project_global_series <- function(df, value_col, horizon_end, algorithm, min_points = 12L) {
  group_cols <- intersect(c("ccaa", "genero"), names(df))
  prepared <- prepare_model_input(df, value_col)

  actual <- prepared |>
    dplyr::mutate(origen = "real") |>
    dplyr::select(dplyr::all_of(group_cols), "fecha", "origen", "value")

  features <- build_global_features(prepared, group_cols)
  model <- fit_global_algorithm(features, algorithm)
  entity_levels <- if (nrow(features) > 0) levels(features$entity_id) else character(0)
  anio_min <- if (nrow(features) > 0) min(lubridate::year(features$fecha), na.rm = TRUE) else NA_integer_

  projected <- prepared |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::group_split() |>
    purrr::map_dfr(function(group_df) {
      if (is.null(model) || dplyr::n_distinct(group_df$fecha) < min_points) return(tibble::tibble())
      group_df <- dplyr::arrange(group_df, .data$fecha)
      last_date <- max(group_df$fecha, na.rm = TRUE)
      future_dates <- month_seq(last_date %m+% months(1), horizon_end)
      if (length(future_dates) == 0) return(tibble::tibble())

      entity <- entity_key(group_df[1, group_cols, drop = FALSE], group_cols)[[1]]
      entity_int <- match(entity, entity_levels)
      if (is.na(entity_int)) return(tibble::tibble())

      vals_hist <- group_df$value
      rows <- list()
      for (fd in future_dates) {
        fd <- as.Date(fd)
        n <- length(vals_hist)
        if (n < 2) next
        lag_12_v <- if (n >= 12) vals_hist[[n - 11]] else mean(vals_hist, na.rm = TRUE)
        newdata <- tibble::tibble(
          fecha = fd,
          t_idx = (lubridate::year(fd) - anio_min) * 12 + lubridate::month(fd),
          mes_num = lubridate::month(fd),
          lag_1 = vals_hist[[n]],
          lag_2 = vals_hist[[n - 1L]],
          lag_12 = lag_12_v,
          media_hist = mean(vals_hist, na.rm = TRUE),
          entity_id = factor(entity, levels = entity_levels),
          entity_id_int = entity_int
        )
        pred <- predict_global_algorithm(model, newdata, algorithm)[[1]]
        if (is.na(pred)) next
        row <- tibble::tibble(fecha = fd, origen = "proyeccion", value = pred)
        for (gc in group_cols) row[[gc]] <- group_df[[gc]][[1]]
        rows[[length(rows) + 1L]] <- row |>
          dplyr::select(dplyr::all_of(group_cols), "fecha", "origen", "value")
        vals_hist <- c(vals_hist, pred)
      }
      dplyr::bind_rows(rows)
    })

  dplyr::bind_rows(actual, projected) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(group_cols)), .data$fecha, .data$origen) |>
    dplyr::rename(!!value_col := value)
}

project_series <- function(df, value_col, horizon_end, algorithm, min_points = 12L) {
  if (algorithm %in% c("RF", "XGBoost")) {
    return(project_global_series(df, value_col, horizon_end, algorithm, min_points))
  }
  project_per_series(df, value_col, horizon_end, algorithm, min_points)
}

bound_dashboard_indicators <- function(df) {
  # Cotas razonables por indicador para acotar las proyecciones.
  # Los *_pct_ppd se acotan en [0, Inf): no tiene sentido un valor negativo,
  # pero pueden, en teoria, superar el 100% (p.ej. limbo de grado podria
  # exceder la PPD si el stock acumulado de pendientes es muy grande); por
  # eso no fijamos techo en 100.
  bounds <- list(
    cobertura_pct_ppd          = c(0, Inf),
    solicitudes_pct_ppd        = c(0, Inf),
    limbo_grado_pct_ppd        = c(0, Inf),
    limbo_pia_pct_ppd          = c(0, Inf),
    limbo_prestaciones_pct_ppd = c(0, Inf),
    tiempo_espera_total_dias   = c(0, Inf),
    ratio_prest_x_benef        = c(0, Inf),
    pct_mujeres_benef          = c(0, 100),
    pct_pecef                  = c(0, 100),
    pct_atencion_residencial   = c(0, 100),
    pct_grado3                 = c(0, 100)
  )

  for (nm in intersect(names(bounds), names(df))) {
    limits <- bounds[[nm]]
    df[[nm]] <- pmax(limits[[1]], df[[nm]])
    if (is.finite(limits[[2]])) df[[nm]] <- pmin(limits[[2]], df[[nm]])
  }
  df
}

# ---------------------------------------------------------------------------
# Pipeline principal: run_modelado
# ---------------------------------------------------------------------------

run_modelado <- function(cfg) {
  log_event("STEP", "Iniciando modelado (multi-algoritmo, granularidad mensual)")

  # 1. Cargar dashboard_indicators
  ind_path <- file.path(cfg$transform_dir, "dashboard_indicators.rds")
  if (!file.exists(ind_path)) {
    stop("Falta dashboard_indicators.rds: ejecuta 'transformacion' primero", call. = FALSE)
  }
  ced_real <- readRDS(ind_path)
  log_event("INFO", sprintf("dashboard_indicators: %d filas | %d CCAA",
                            nrow(ced_real), dplyr::n_distinct(ced_real$ccaa)))

  # 2. Variables a proyectar = los 10 indicadores del cuaderno §4
  vars <- intersect(cfg$vars_to_model %||% dashboard_indicator_names(), names(ced_real))
  if (length(vars) == 0) {
    log_event("WARN", "No hay indicadores en dashboard_indicators para modelar; salida = real")
    saveRDS(ced_real |> dplyr::mutate(origen = "real"),
            file.path(cfg$model_dir, "dashboard_indicators.rds"))
    return(invisible(NULL))
  }

  primary_tables <- purrr::set_names(vars) |>
    purrr::map(function(v) {
      ced_real |>
        dplyr::select(dplyr::all_of(c("ccaa", "fecha", v))) |>
        dplyr::filter(!is.na(.data[[v]]))
    })

  # 3. CV temporal rolling-origin
  cv_folds   <- as.integer(cfg$cv_folds %||% 3L)
  min_points <- as.integer(cfg$min_points_cv %||% 12L)
  selection  <- evaluate_with_temporal_cv(
    primary_tables, vars, cv_folds = cv_folds, min_points = min_points,
    include_prophet = isTRUE(cfg$include_prophet)
  )
  selected_algorithm <- selection$selected_algorithm

  # 4. Horizonte: ultimo mes real + N meses (default 12)
  last_real <- max(as.Date(ced_real$fecha), na.rm = TRUE)
  horizon_default <- last_real %m+% months(as.integer(cfg$forecast_horizon_months %||% 12L))
  horizon_end <- as.Date(cfg$forecast_horizon_end %||% horizon_default)
  if (horizon_end < horizon_default) horizon_end <- horizon_default

  log_event("INFO", glue("Proyeccion {format(last_real %m+% months(1), '%Y-%m')} -> {format(horizon_end, '%Y-%m')} con {selected_algorithm}"))

  # 5. Proyectar cada indicador
  projected <- purrr::imap(primary_tables, function(df, v) {
    out <- project_series(df, v, horizon_end, selected_algorithm, min_points = min_points)
    dplyr::rename(out, !!paste0(v, "_origen") := "origen")
  })

  # 6. Combinar por (ccaa, fecha)
  ced_modelado <- purrr::reduce(
    projected,
    function(left, right) dplyr::full_join(left, right, by = c("ccaa", "fecha"))
  )

  # 7. Origen global: "proyeccion" si alguna variable es proyectada, "real" si todas son reales
  origen_cols <- paste0(vars, "_origen")
  origen_present <- intersect(origen_cols, names(ced_modelado))
  ced_modelado$origen <- apply(
    ced_modelado[, origen_present, drop = FALSE], 1,
    function(row) {
      vals <- row[!is.na(row)]
      if (length(vals) == 0) NA_character_
      else if (any(vals == "proyeccion")) "proyeccion" else "real"
    }
  )
  ced_modelado <- ced_modelado |> dplyr::select(-dplyr::all_of(origen_present))

  ced_modelado <- ced_modelado |>
    bound_dashboard_indicators() |>
    dplyr::arrange(.data$ccaa, .data$fecha, .data$origen)

  # 8. Guardar dashboard_indicators con proyeccion + propagar tablas raw
  raw_keep <- list.files(cfg$transform_dir, pattern = "\\.rds$", full.names = TRUE)
  raw_keep <- raw_keep[basename(raw_keep) != "dashboard_indicators.rds"]
  for (p in raw_keep) {
    file.copy(p, file.path(cfg$model_dir, basename(p)), overwrite = TRUE)
  }

  saveRDS(ced_modelado, file.path(cfg$model_dir, "dashboard_indicators.rds"))
  saveRDS(selection, file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion.rds"))
  utils::write.csv2(
    selection$metrics,
    file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_global.csv"),
    row.names = FALSE
  )
  if (!is.null(selection$variable_metrics)) {
    utils::write.csv2(
      selection$variable_metrics,
      file.path(cfg$model_dir, "seleccion_algoritmo_proyeccion_variables.csv"),
      row.names = FALSE
    )
  }

  log_series_coverage(ced_modelado, "dashboard_indicators (real + proyeccion)")
  log_event("OK", glue("Modelado completado: algoritmo={selected_algorithm} | horizonte={format(horizon_end, '%Y-%m')}"))

  invisible(list(dashboard_indicators = ced_modelado, selection = selection))
}
