# =============================================================================
# imputacion_bootstrap.R — Sanidad · ODESOCAN
# Imputación/proyección mediante BAGGED ETS (bootstrap por bloques + ETS),
# portado del proyecto Prevención (Bergmeir-Hyndman-Benítez, IJF 2016).
#
# Método:
#   1. Bootstrap por bloques de la serie (bld.mbb.bootstrap): descompone STL,
#      hace moving-block bootstrap sobre los residuos y reconstruye B series.
#   2. Ajuste de un ETS automático a cada réplica bootstrap.
#   3. Promedio de las B previsiones puntuales como predicción central; se
#      persisten además las B simulaciones individuales y el IC 95%.
#
# Adaptación Sanidad: el panel es CCAA × periodo × GÉNERO, por lo que la
# imputación se aplica a cada serie (ccaa × genero × variable) por separado.
#
# Reglas:
#   - Solo series ANUALES CONTINUAS con ≥ .MIN_OBS_BAGGING observaciones
#     consecutivas terminadas en max(periodo).
#   - Semilla set.seed(42) por llamada para reproducibilidad estricta.
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("forecast", "dplyr", "tibble", "purrr", "glue"))
  library(forecast); library(dplyr); library(glue)
})

.MIN_OBS_BAGGING   <- 10L
.DEFAULT_BOOTSTRAPS <- 100L
.SEED              <- 42L

#' Filtra una serie anual a su tramo continuo más largo terminado en max(periodo).
.tail_continuous <- function(serie) {
  serie <- serie %>%
    dplyr::filter(!is.na(.data$periodo), !is.na(.data$valor)) %>%
    dplyr::arrange(.data$periodo)
  if (nrow(serie) == 0L) return(serie)
  diffs <- diff(serie$periodo)
  if (any(diffs > 1L)) {
    last_gap <- max(which(diffs > 1L))
    serie <- serie[(last_gap + 1L):nrow(serie), , drop = FALSE]
  }
  serie
}

#' Proyecta un año (target_year) para una sola serie (periodo, valor) con bagged ETS.
#' Devuelve list(central, simulaciones, ok, motivo).
proyectar_serie <- function(serie, target_year, n_bootstrap = .DEFAULT_BOOTSTRAPS) {
  require_packages("forecast")
  serie <- .tail_continuous(serie)
  if (nrow(serie) < .MIN_OBS_BAGGING) {
    return(list(ok = FALSE, motivo = sprintf("serie corta tras tramo continuo (%d < %d)",
                                             nrow(serie), .MIN_OBS_BAGGING)))
  }
  if (target_year <= max(serie$periodo)) {
    return(list(ok = FALSE, motivo = "target_year ya cubierto por la serie observada"))
  }
  horizon <- target_year - max(serie$periodo)
  if (horizon > 5L) {
    return(list(ok = FALSE, motivo = sprintf("horizonte excesivo: %d años", horizon)))
  }

  ts_serie <- stats::ts(serie$valor, start = min(serie$periodo), frequency = 1L)
  set.seed(.SEED)
  tryCatch({
    bootstrapped <- forecast::bld.mbb.bootstrap(ts_serie, num = n_bootstrap)
    modelo <- forecast::baggedModel(ts_serie, bootstrapped_series = bootstrapped, fn = forecast::ets)
    pred <- forecast::forecast(modelo, h = horizon, level = 95)

    sims <- unlist(lapply(modelo$models, function(m) {
      tryCatch(as.numeric(forecast::forecast(m, h = horizon, level = 95)$mean)[horizon],
               error = function(e) NA_real_)
    }))
    sims <- sims[!is.na(sims)]
    if (length(sims) < max(10L, floor(n_bootstrap / 4L))) {
      return(list(ok = FALSE, motivo = sprintf("solo %d simulaciones válidas de %d", length(sims), n_bootstrap)))
    }
    li_vec <- as.numeric(pred$lower); ls_vec <- as.numeric(pred$upper)
    list(
      central = tibble::tibble(periodo = target_year, valor = as.numeric(pred$mean)[horizon],
                               li_95 = li_vec[horizon], ls_95 = ls_vec[horizon]),
      simulaciones = tibble::tibble(sim_id = seq_along(sims), valor = sims),
      ok = TRUE
    )
  }, error = function(e) list(ok = FALSE, motivo = sprintf("baggedModel falló: %s", conditionMessage(e))))
}

#' Imputa una variable en el panel CCAA × GÉNERO. panel: (ccaa, genero, periodo, valor).
#' Devuelve list(central, simulaciones, fallos) con etiqueta de variable.
imputar_panel_variable <- function(panel, variable, target_year,
                                   n_bootstrap = .DEFAULT_BOOTSTRAPS) {
  assert_required_columns(panel, c("ccaa", "genero", "periodo", "valor"),
                          glue("imputar_panel_variable[{variable}]"))
  grupos <- panel %>% dplyr::distinct(.data$ccaa, .data$genero) %>% dplyr::arrange(.data$ccaa, .data$genero)

  resultados <- purrr::pmap(grupos, function(ccaa, genero) {
    serie <- panel %>%
      dplyr::filter(.data$ccaa == !!ccaa, .data$genero == !!genero) %>%
      dplyr::select("periodo", "valor")
    res <- proyectar_serie(serie, target_year = target_year, n_bootstrap = n_bootstrap)
    res$ccaa <- ccaa; res$genero <- genero
    res
  })

  ok   <- purrr::keep(resultados, ~ isTRUE(.x$ok))
  fail <- purrr::keep(resultados, ~ !isTRUE(.x$ok))

  central <- if (length(ok)) purrr::map_dfr(ok, function(r)
    r$central %>% dplyr::mutate(ccaa = r$ccaa, genero = r$genero, variable = variable, imputado = TRUE) %>%
      dplyr::select(ccaa, genero, variable, periodo, valor, li_95, ls_95, imputado)
  ) else tibble::tibble(ccaa = character(), genero = character(), variable = character(),
                        periodo = integer(), valor = numeric(), li_95 = numeric(),
                        ls_95 = numeric(), imputado = logical())

  simulaciones <- if (length(ok)) purrr::map_dfr(ok, function(r)
    r$simulaciones %>% dplyr::mutate(ccaa = r$ccaa, genero = r$genero, variable = variable,
                                     periodo = r$central$periodo) %>%
      dplyr::select(ccaa, genero, variable, periodo, sim_id, valor)
  ) else tibble::tibble(ccaa = character(), genero = character(), variable = character(),
                        periodo = integer(), sim_id = integer(), valor = numeric())

  fallos <- if (length(fail)) tibble::tibble(
    ccaa = vapply(fail, function(r) r$ccaa, character(1)),
    genero = vapply(fail, function(r) r$genero, character(1)),
    variable = variable,
    motivo = vapply(fail, function(r) r$motivo, character(1))
  ) else tibble::tibble(ccaa = character(), genero = character(), variable = character(), motivo = character())

  list(central = central, simulaciones = simulaciones, fallos = fallos)
}

#' Imputa múltiples variables. panel_largo: (ccaa, genero, periodo, variable, valor).
imputar_panel_multi <- function(panel_largo, variables = NULL, target_year,
                                n_bootstrap = .DEFAULT_BOOTSTRAPS) {
  assert_required_columns(panel_largo, c("ccaa", "genero", "periodo", "variable", "valor"), "imputar_panel_multi")
  variables <- variables %||% sort(unique(panel_largo$variable))
  resultados <- purrr::map(variables, function(v) {
    sub <- panel_largo %>% dplyr::filter(.data$variable == v) %>%
      dplyr::select("ccaa", "genero", "periodo", "valor")
    imputar_panel_variable(sub, variable = v, target_year = target_year, n_bootstrap = n_bootstrap)
  })
  list(
    central      = purrr::map_dfr(resultados, "central"),
    simulaciones = purrr::map_dfr(resultados, "simulaciones"),
    fallos       = purrr::map_dfr(resultados, "fallos")
  )
}
