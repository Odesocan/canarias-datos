# ============================================================
# 3_modelado/modelado.R — Indicadores derivados + proyección opcional.
#
# - pct_pib_nacional: importe_eur / PIB nominal nacional × 100 (denominador
#   COMÚN para comparar CCAA — sec. "Variable final" del cuaderno).
# - eur_per_capita:   importe_eur / poblacion(ccaa, anio).
# - var_nominal_pct:  (t - t-1) / t-1 × 100.
# - origen:           "real" | "proyeccion".
# - Proyección opcional con Prophet (cfg$enable_projection); fallback a
#   tendencia lineal cuando Prophet no está disponible. Series con <5
#   puntos no se proyectan.
#
# Salidas en 3_modelado/:
#   ced_presupuestos.rds   — tabla canónica (entra a la carga)
#   indicadores_pib.rds    — debug: indicadores intermedios
# ============================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr","tidyr","tibble","purrr"))
  library(dplyr)
})

.proyectar_serie <- function(df_serie, horizon_year, enable_projection) {
  if (!isTRUE(enable_projection)) return(df_serie)
  if (nrow(df_serie) < 5) return(df_serie)
  anio_max <- max(df_serie$anio, na.rm = TRUE)
  if (!is.finite(anio_max) || anio_max >= horizon_year) return(df_serie)

  if (requireNamespace("prophet", quietly = TRUE)) {
    fitting <- df_serie |> dplyr::transmute(
      ds = as.Date(paste0(.data$anio, "-01-01")),
      y  = .data$importe_eur
    )
    m <- tryCatch(
      prophet::prophet(fitting, yearly.seasonality = FALSE,
                        weekly.seasonality = FALSE, daily.seasonality = FALSE,
                        verbose = FALSE),
      error = function(e) NULL
    )
    if (is.null(m)) return(df_serie)
    periods <- horizon_year - anio_max
    fut <- prophet::make_future_dataframe(m, periods = periods, freq = "year")
    pred <- predict(m, fut)
    nuevos <- pred |>
      dplyr::mutate(anio = as.integer(format(.data$ds, "%Y"))) |>
      dplyr::filter(.data$anio > anio_max) |>
      dplyr::transmute(
        anio = .data$anio,
        importe_eur = .data$yhat,
        origen = "proyeccion"
      )
    df_serie <- df_serie |> dplyr::mutate(origen = "real")
    return(dplyr::bind_rows(df_serie, nuevos |>
                              dplyr::mutate(
                                ccaa = df_serie$ccaa[1],
                                ccaa_id3 = df_serie$ccaa_id3[1],
                                concepto = df_serie$concepto[1]
                              )))
  }

  # Fallback: regresión lineal sobre el año
  modelo <- tryCatch(stats::lm(importe_eur ~ anio, data = df_serie),
                     error = function(e) NULL)
  if (is.null(modelo)) return(df_serie)
  nuevos <- tibble::tibble(anio = seq.int(anio_max + 1L, horizon_year))
  nuevos$importe_eur <- as.numeric(stats::predict(modelo, newdata = nuevos))
  nuevos$origen <- "proyeccion"
  nuevos$ccaa     <- df_serie$ccaa[1]
  nuevos$ccaa_id3 <- df_serie$ccaa_id3[1]
  nuevos$concepto <- df_serie$concepto[1]
  df_serie <- df_serie |> dplyr::mutate(origen = "real")
  dplyr::bind_rows(df_serie, nuevos)
}

#' Completa el PIB regional de los años sin dato del INE (p.ej. 2025-2026)
#' mediante un BOOTSTRAP no paramétrico de las tasas de crecimiento nominal.
#'
#' Por CCAA (serie real 2015..t_max):
#'   1. g_t = log(PIB_t / PIB_{t-1})  — log-crecimientos (multiplicativos).
#'   2. Para cada réplica b=1..n_boot y cada año a proyectar, se muestrea con
#'      reemplazo una g del histórico y se encadena PIB*_{t+1}=PIB_t·exp(g*).
#'   3. Punto = MEDIANA de las réplicas (robusta al outlier COVID-2020, que se
#'      conserva en el pool para que la banda refleje el riesgo de recesión);
#'      banda = percentiles 5 y 95.
#'
#' Devuelve un data.frame (ccaa_id3, anio, pib_regional_eur, pib_lo, pib_hi,
#' pib_origen) con las filas REALES + las PROYECTADAS hasta `horizon_year`.
.bootstrap_pib_regional <- function(pib_real, horizon_year, n_boot = 5000L,
                                    seed = 20260716L) {
  if (is.null(pib_real) || nrow(pib_real) == 0) return(pib_real)
  set.seed(seed)
  reales <- pib_real
  reales$pib_lo <- NA_real_; reales$pib_hi <- NA_real_
  reales$pib_origen <- "real"

  proyecciones <- list()
  for (cc in unique(pib_real$ccaa_id3)) {
    serie <- pib_real[pib_real$ccaa_id3 == cc, ]
    serie <- serie[order(serie$anio), ]
    vals  <- serie$pib_regional_eur
    anios <- serie$anio
    t_max <- max(anios)
    if (t_max >= horizon_year || length(vals) < 4) next
    growths <- diff(log(vals))
    growths <- growths[is.finite(growths)]
    if (length(growths) < 3) next

    anios_proj <- seq.int(t_max + 1L, horizon_year)
    actual <- rep(vals[length(vals)], n_boot)         # PIB del último año real
    for (a in anios_proj) {
      g_star <- sample(growths, size = n_boot, replace = TRUE)
      actual <- actual * exp(g_star)
      proyecciones[[length(proyecciones) + 1L]] <- data.frame(
        ccaa_id3 = cc, anio = a,
        pib_regional_eur = stats::median(actual),
        pib_lo = stats::quantile(actual, 0.05, names = FALSE),
        pib_hi = stats::quantile(actual, 0.95, names = FALSE),
        pib_origen = "proyeccion",
        stringsAsFactors = FALSE
      )
    }
  }
  if (length(proyecciones) == 0) return(reales)
  rbind(reales, do.call(rbind, proyecciones))
}

run_modelado <- function(cfg) {
  log_event("INFO", "Iniciando modelado")
  artefactos <- load_named_rds(cfg$transform_dir, c("gasto_normalizado"))
  norm <- artefactos$gasto_normalizado

  if (nrow(norm) == 0) {
    log_event("WARN", "Gasto normalizado vacío — modelado generará tabla vacía")
    save_named_rds(list(ced_presupuestos = tibble::tibble()), cfg$model_dir)
    return(invisible(NULL))
  }

  # Capa preferente: si una CCAA tiene capa Hacienda + autonómica, la
  # comparable es la Hacienda; conservamos ambas con flag `capa`.
  ext <- load_externos(cfg)

  # Asegura el tipo entero para el join
  norm$anio <- as.integer(norm$anio)
  pib <- if (!is.null(ext$pib) && nrow(ext$pib) > 0) ext$pib else tibble::tibble()
  pob <- if (!is.null(ext$poblacion) && nrow(ext$poblacion) > 0) ext$poblacion else tibble::tibble()

  # Proyección por serie (ccaa, concepto, capa)
  if (isTRUE(cfg$enable_projection)) {
    norm <- norm |>
      dplyr::group_by(.data$ccaa, .data$ccaa_id3, .data$concepto, .data$capa) |>
      dplyr::group_modify(~ .proyectar_serie(.x, cfg$horizon_year, cfg$enable_projection)) |>
      dplyr::ungroup()
  }
  if (!"origen" %in% names(norm)) norm$origen <- "real"
  norm$origen <- ifelse(is.na(norm$origen), "real", norm$origen)

  # Indicadores derivados
  if (nrow(pib) > 0) {
    norm <- norm |> dplyr::left_join(pib, by = "anio")
  } else norm$pib_nominal_eur <- NA_real_

  if (nrow(pob) > 0) {
    norm <- norm |> dplyr::left_join(pob, by = c("ccaa","anio"))
  } else norm$poblacion <- NA_real_

  # PIB REGIONAL: se completan por bootstrap los años sin dato del INE (p.ej.
  # 2025-2026) hasta cubrir todos los ejercicios presentes en el gasto. Es un
  # relleno del denominador, independiente de enable_projection.
  pib_reg <- if (!is.null(ext$pib_regional)) ext$pib_regional else tibble::tibble()
  if (nrow(pib_reg) > 0) {
    hasta <- max(c(cfg$horizon_year, suppressWarnings(max(norm$anio, na.rm = TRUE))),
                 na.rm = TRUE)
    pib_reg_full <- .bootstrap_pib_regional(
      as.data.frame(pib_reg), horizon_year = hasta,
      n_boot = cfg$pib_boot_n %||% 5000L, seed = cfg$pib_boot_seed %||% 20260716L)
    n_proj <- sum(pib_reg_full$pib_origen == "proyeccion")
    log_event("INFO", sprintf(
      "PIB regional: %d filas reales + %d proyectadas (bootstrap n=%d) hasta %d",
      sum(pib_reg_full$pib_origen == "real"), n_proj,
      cfg$pib_boot_n %||% 5000L, hasta))
    norm <- norm |> dplyr::left_join(pib_reg_full, by = c("ccaa_id3", "anio"))
  } else {
    log_event("WARN", "Sin PIB regional — pct_pib_regional será NA")
    norm$pib_regional_eur <- NA_real_; norm$pib_origen <- NA_character_
    norm$pib_lo <- NA_real_; norm$pib_hi <- NA_real_
  }

  norm <- norm |>
    dplyr::mutate(
      pct_pib_nacional = ifelse(is.finite(.data$pib_nominal_eur) & .data$pib_nominal_eur > 0,
                                 .data$importe_eur / .data$pib_nominal_eur * 100, NA_real_),
      # INDICADOR OBJETIVO: % del PIB REGIONAL de la propia CCAA (comparable
      # entre territorios de tamaño distinto — mide prioridad, no volumen).
      pct_pib_regional = ifelse(is.finite(.data$pib_regional_eur) & .data$pib_regional_eur > 0,
                                 .data$importe_eur / .data$pib_regional_eur * 100, NA_real_),
      eur_per_capita   = ifelse(is.finite(.data$poblacion) & .data$poblacion > 0,
                                 .data$importe_eur / .data$poblacion, NA_real_)
    )

  # Variación interanual
  norm <- norm |>
    dplyr::arrange(.data$ccaa, .data$concepto, .data$capa, .data$anio) |>
    dplyr::group_by(.data$ccaa, .data$concepto, .data$capa) |>
    dplyr::mutate(
      importe_eur_prev = dplyr::lag(.data$importe_eur),
      var_nominal_pct  = ifelse(is.finite(.data$importe_eur_prev) & .data$importe_eur_prev != 0,
                                 (.data$importe_eur - .data$importe_eur_prev) /
                                 .data$importe_eur_prev * 100, NA_real_)
    ) |>
    dplyr::ungroup()

  # Tabla canónica con el shape esperado por la viz (mismo patrón que
  # ced_saludmental / ced_vivienda_global): genero=total (no se desagrega
  # por género en Presupuestos), origen, métricas pivotadas por concepto.
  canonico <- norm |>
    dplyr::transmute(
      ccaa = .data$ccaa,
      periodo = .data$anio,
      genero = "total",
      origen = .data$origen,
      concepto = .data$concepto,
      capa = .data$capa,
      importe_eur = round(.data$importe_eur, 2),
      pct_pib_nacional = round(.data$pct_pib_nacional, 4),
      pct_pib_regional = round(.data$pct_pib_regional, 4),
      eur_per_capita = round(.data$eur_per_capita, 2),
      var_nominal_pct = round(.data$var_nominal_pct, 2),
      pib_regional_eur = round(.data$pib_regional_eur, 2),
      pib_origen = .data$pib_origen,
      es_prorroga = .data$es_prorroga,
      estimado = .data$estimado
    )

  # Pivoteo: una columna por concepto × métrica.
  wide_importe <- canonico |>
    dplyr::select("ccaa","periodo","genero","origen","capa","concepto","importe_eur") |>
    tidyr::pivot_wider(names_from = "concepto", values_from = "importe_eur",
                        names_prefix = "imp_")

  wide_pct <- canonico |>
    dplyr::select("ccaa","periodo","genero","origen","capa","concepto","pct_pib_nacional") |>
    tidyr::pivot_wider(names_from = "concepto", values_from = "pct_pib_nacional",
                        names_prefix = "pib_")

  # Indicador objetivo: % del PIB REGIONAL por concepto (pibreg_<concepto>).
  wide_pibreg <- canonico |>
    dplyr::select("ccaa","periodo","genero","origen","capa","concepto","pct_pib_regional") |>
    tidyr::pivot_wider(names_from = "concepto", values_from = "pct_pib_regional",
                        names_prefix = "pibreg_")

  wide_pc <- canonico |>
    dplyr::select("ccaa","periodo","genero","origen","capa","concepto","eur_per_capita") |>
    tidyr::pivot_wider(names_from = "concepto", values_from = "eur_per_capita",
                        names_prefix = "pc_")

  wide_var <- canonico |>
    dplyr::select("ccaa","periodo","genero","origen","capa","concepto","var_nominal_pct") |>
    tidyr::pivot_wider(names_from = "concepto", values_from = "var_nominal_pct",
                        names_prefix = "var_")

  flags <- canonico |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$genero, .data$origen, .data$capa) |>
    dplyr::summarise(
      es_prorroga = any(.data$es_prorroga, na.rm = TRUE),
      estimado = any(.data$estimado, na.rm = TRUE),
      # PIB regional: constante por (ccaa, periodo); se resume una vez.
      pib_regional_eur = dplyr::first(.data$pib_regional_eur),
      pib_origen = dplyr::first(.data$pib_origen),
      .groups = "drop"
    )

  ced <- flags |>
    dplyr::left_join(wide_importe, by = c("ccaa","periodo","genero","origen","capa")) |>
    dplyr::left_join(wide_pct,     by = c("ccaa","periodo","genero","origen","capa")) |>
    dplyr::left_join(wide_pibreg,  by = c("ccaa","periodo","genero","origen","capa")) |>
    dplyr::left_join(wide_pc,      by = c("ccaa","periodo","genero","origen","capa")) |>
    dplyr::left_join(wide_var,     by = c("ccaa","periodo","genero","origen","capa")) |>
    dplyr::arrange(.data$ccaa, .data$periodo, .data$capa, .data$origen)

  log_series_coverage(ced, "ced_presupuestos modelado")
  log_table_quality(ced, "ced_presupuestos modelado", c("periodo"))

  # Chequeo Benford sobre importes reales (sec. 2.6)
  importes_reales <- norm$importe_eur[norm$origen == "real" & is.finite(norm$importe_eur)]
  bf <- chequeo_benford(importes_reales)
  if (is.na(bf$ok)) {
    log_event("INFO", sprintf("Benford: muestra insuficiente (n=%d)", bf$n))
  } else {
    log_event(if (isTRUE(bf$ok)) "INFO" else "WARN",
              sprintf("Benford: chi=%.2f p=%.4f ok=%s n=%d",
                      bf$chi, bf$p_value, bf$ok, bf$n))
  }

  save_named_rds(list(ced_presupuestos = ced,
                       indicadores_pib  = norm),
                  cfg$model_dir)

  invisible(list(ced_presupuestos = ced))
}
