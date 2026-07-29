# ============================================================
# 2_transformacion/transformacion.R — Normaliza el staging:
#   1) Resuelve concepto con correspondencias.yml (overrides CCAA + globales + fuzzy)
#   2) Filtra Administración General / organismos / entes según `capa` (sec. 2.4)
#   3) Aplica reglas de unidad (eur vs miles), prórroga, consolidación
#   4) Agrega por (ccaa, anio, concepto, capa) preservando trazabilidad
# ============================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr","tidyr","tibble","purrr","stringi"))
  library(dplyr)
})

.aplicar_reglas_unidad <- function(df) {
  if (!"unidad_origen" %in% names(df)) df$unidad_origen <- "eur"
  miles <- !is.na(df$unidad_origen) & df$unidad_origen %in% c("miles","miles_eur","k","thousand")
  df$importe_eur[miles] <- df$importe_eur[miles] * 1000
  df$unidad_origen <- "eur"
  df
}

.filtrar_perimetro <- function(df) {
  if (!"denominacion" %in% names(df)) return(df)
  den_norm <- tolower(stringi::stri_trans_general(df$denominacion, "Latin-ASCII"))
  patrones_totales <- c("^total\\b", "^suma\\b", "^total general$",
                         "presupuesto total", "presupuesto consolidado")
  drop <- Reduce(`|`, lapply(patrones_totales, function(p) grepl(p, den_norm)))
  if (any(drop, na.rm = TRUE)) {
    log_event("INFO", sprintf("Filtradas %d filas de totales/sumas", sum(drop, na.rm = TRUE)))
  }
  df[!drop, , drop = FALSE]
}

.normalizar_concepto_python <- function(x) {
  if (is.null(x)) return(NA_character_)
  out <- trimws(as.character(x))
  out[out %in% c("", "NA", "NaN", "nan", "None", "none", "NULL", "null")] <- NA_character_
  out
}

.escribir_reporte_csv <- function(df, path) {
  tryCatch(
    utils::write.csv(df, path, row.names = FALSE, fileEncoding = "UTF-8"),
    error = function(e) log_event("WARN", sprintf("No se pudo escribir %s: %s",
                                                   basename(path), conditionMessage(e)))
  )
}

.reportar_discrepancias_concepto <- function(detalle, cfg) {
  if (!all(c("concepto_python","concepto") %in% names(detalle))) {
    return(tibble::tibble())
  }
  discrepancias <- detalle |>
    dplyr::filter(!is.na(.data$concepto_python),
                  !is.na(.data$concepto),
                  .data$concepto_python != .data$concepto) |>
    dplyr::transmute(
      ccaa = .data$ccaa,
      ccaa_id3 = .data$ccaa_id3,
      anio = .data$anio,
      capa = .data$capa,
      codigo = .data$codigo_origen,
      denominacion = .data$denominacion_origen,
      concepto_python = .data$concepto_python,
      concepto_final = .data$concepto,
      regla_final = .data$regla,
      fuente_url = .data$fuente_url
    )
  if (nrow(discrepancias) > 0) {
    resumen <- discrepancias |>
      dplyr::count(.data$ccaa_id3, .data$anio, .data$concepto_python,
                   .data$concepto_final, name = "n") |>
      dplyr::arrange(dplyr::desc(.data$n))
    log_event("WARN", sprintf("Concepto Python vs R: %d discrepancias en %d CCAA-año",
                              nrow(discrepancias),
                              dplyr::n_distinct(paste(discrepancias$ccaa_id3,
                                                       discrepancias$anio))))
    .escribir_reporte_csv(discrepancias,
                          file.path(cfg$transform_dir, "discrepancias_concepto.csv"))
    .escribir_reporte_csv(resumen,
                          file.path(cfg$transform_dir, "discrepancias_concepto_resumen.csv"))
  } else {
    log_event("INFO", "Concepto Python vs R: sin discrepancias")
    .escribir_reporte_csv(discrepancias,
                          file.path(cfg$transform_dir, "discrepancias_concepto.csv"))
    .escribir_reporte_csv(tibble::tibble(ccaa_id3 = character(), anio = integer(),
                                         concepto_python = character(),
                                         concepto_final = character(), n = integer()),
                          file.path(cfg$transform_dir, "discrepancias_concepto_resumen.csv"))
  }
  discrepancias
}

.chequeos_magnitud_minimos <- function(normalizado) {
  if (nrow(normalizado) == 0) return(tibble::tibble())

  alertas <- list()

  negativos <- normalizado |>
    dplyr::filter(is.finite(.data$importe_eur), .data$importe_eur < 0) |>
    dplyr::transmute(tipo = "importe_negativo", severidad = "WARN",
                     ccaa = .data$ccaa, ccaa_id3 = .data$ccaa_id3,
                     anio = .data$anio, capa = .data$capa,
                     concepto = .data$concepto, importe_eur = .data$importe_eur,
                     detalle = "Importe menor que cero")
  alertas[[length(alertas) + 1L]] <- negativos

  grandes_cero <- normalizado |>
    dplyr::filter(.data$concepto %in% c("sanidad","educacion","dependencia"),
                  is.finite(.data$importe_eur), .data$importe_eur <= 0) |>
    dplyr::transmute(tipo = "concepto_grande_cero", severidad = "WARN",
                     ccaa = .data$ccaa, ccaa_id3 = .data$ccaa_id3,
                     anio = .data$anio, capa = .data$capa,
                     concepto = .data$concepto, importe_eur = .data$importe_eur,
                     detalle = "Concepto estructural con importe cero o negativo")
  alertas[[length(alertas) + 1L]] <- grandes_cero

  sanidad_fuera_rango <- normalizado |>
    dplyr::filter(.data$concepto == "sanidad",
                  is.finite(.data$importe_eur),
                  (.data$importe_eur < 1e8 | .data$importe_eur > 4e10)) |>
    dplyr::transmute(tipo = "sanidad_fuera_rango", severidad = "WARN",
                     ccaa = .data$ccaa, ccaa_id3 = .data$ccaa_id3,
                     anio = .data$anio, capa = .data$capa,
                     concepto = .data$concepto, importe_eur = .data$importe_eur,
                     detalle = "Sanidad fuera de rango amplio 0.1B-40B")
  alertas[[length(alertas) + 1L]] <- sanidad_fuera_rango

  saltos <- normalizado |>
    dplyr::arrange(.data$ccaa, .data$capa, .data$concepto, .data$anio) |>
    dplyr::group_by(.data$ccaa, .data$capa, .data$concepto) |>
    dplyr::mutate(
      importe_prev = dplyr::lag(.data$importe_eur),
      rel = dplyr::if_else(is.finite(.data$importe_prev) & .data$importe_prev > 0,
                           (.data$importe_eur - .data$importe_prev) / .data$importe_prev,
                           NA_real_)
    ) |>
    dplyr::ungroup() |>
    dplyr::filter(is.finite(.data$rel), abs(.data$rel) > 0.75,
                  !(.data$concepto %in% c("total"))) |>
    dplyr::transmute(tipo = "salto_interanual", severidad = "WARN",
                     ccaa = .data$ccaa, ccaa_id3 = .data$ccaa_id3,
                     anio = .data$anio, capa = .data$capa,
                     concepto = .data$concepto, importe_eur = .data$importe_eur,
                     detalle = sprintf("Salto interanual %.1f%%", .data$rel * 100))
  alertas[[length(alertas) + 1L]] <- saltos

  prorrogas <- normalizado |>
    dplyr::arrange(.data$ccaa, .data$capa, .data$concepto, .data$anio) |>
    dplyr::group_by(.data$ccaa, .data$capa, .data$concepto) |>
    dplyr::mutate(
      importe_prev = dplyr::lag(.data$importe_eur),
      rel_abs = dplyr::if_else(is.finite(.data$importe_prev) & .data$importe_prev > 0,
                               abs(.data$importe_eur - .data$importe_prev) / .data$importe_prev,
                               NA_real_)
    ) |>
    dplyr::ungroup() |>
    dplyr::filter(.data$es_prorroga, is.finite(.data$rel_abs), .data$rel_abs > 0.01) |>
    dplyr::transmute(tipo = "prorroga_no_identica", severidad = "WARN",
                     ccaa = .data$ccaa, ccaa_id3 = .data$ccaa_id3,
                     anio = .data$anio, capa = .data$capa,
                     concepto = .data$concepto, importe_eur = .data$importe_eur,
                     detalle = sprintf("Prórroga difiere %.1f%% del año anterior",
                                       .data$rel_abs * 100))
  alertas[[length(alertas) + 1L]] <- prorrogas

  dplyr::bind_rows(alertas)
}

run_transformacion <- function(cfg) {
  log_event("INFO", "Iniciando transformación")

  artefactos <- load_named_rds(cfg$extraction_dir, c("manifest","staging_gasto"))
  staging <- as.data.frame(artefactos$staging_gasto)

  if (nrow(staging) == 0) {
    log_event("WARN", "Staging vacío — generando outputs vacíos")
    save_named_rds(list(
      gasto_normalizado = tibble::tibble(),
      gasto_detalle = tibble::tibble(),
      pendientes_revision = tibble::tibble()
    ), cfg$transform_dir)
    return(invisible(NULL))
  }

  assert_required_columns(staging,
    c("codigo","denominacion","importe_eur","ccaa","anio","capa","es_prorroga"),
    "staging_gasto")

  staging <- .aplicar_reglas_unidad(staging)
  staging <- .filtrar_perimetro(staging)
  staging$ccaa <- normalize_ccaa_name(staging$ccaa)
  if (!"concepto" %in% names(staging)) staging$concepto <- NA_character_
  staging$concepto_python <- .normalizar_concepto_python(staging$concepto)

  corr <- cargar_correspondencias(cfg$correspondencias_yml)

  ccaa_grupos <- split(seq_len(nrow(staging)), staging$ccaa)
  asignaciones <- vector("list", length(ccaa_grupos))
  for (i in seq_along(ccaa_grupos)) {
    idx <- ccaa_grupos[[i]]
    ccaa_nombre <- names(ccaa_grupos)[i]
    sub <- staging[idx, , drop = FALSE]
    asig <- asignar_concepto(sub$codigo, sub$denominacion,
                              ccaa = ccaa_nombre, corr = corr,
                              concepto_python = sub$concepto_python,
                              fuzzy_threshold = cfg$fuzzy_threshold)
    asig$row_index <- idx
    asignaciones[[i]] <- asig
  }
  asig_all <- dplyr::bind_rows(asignaciones) |> dplyr::arrange(.data$row_index)

  detalle <- staging |>
    dplyr::mutate(
      concepto_python = .data$concepto_python,
      concepto = asig_all$concepto,
      score = asig_all$score,
      regla = asig_all$regla,
      denominacion_origen = .data$denominacion,
      codigo_origen = .data$codigo
    )

  # Fallback sistémico (2026-07-01): cuando R no logra mapear el código
  # (concepto NA) pero el extractor Python SÍ asignó concepto vía la
  # correspondencia LOCAL de la CCAA, se adopta el de Python. Corrige el desfase
  # estructural raíz↔local del correspondencias.yml (p.ej. Cataluña 2015 códigos
  # 415/419 ausentes del bloque raíz; La Rioja con códigos punteados 3.1.1.1 que
  # el matcher R no reconoce). Sólo rellena huecos: NO pisa las filas donde R sí
  # decide (esas siguen su curso y su discrepancia se reporta igual). Se excluye
  # la capa Hacienda, que tiene su propia lógica de concepto=total más abajo.
  usar_py <- is.na(detalle$concepto) & !is.na(detalle$concepto_python) &
             detalle$capa != "hacienda"
  if (any(usar_py)) {
    detalle$concepto[usar_py] <- detalle$concepto_python[usar_py]
    detalle$score[usar_py]    <- 0.9
    detalle$regla[usar_py]    <- "python_local_fallback"
    log_event("INFO", sprintf("Fallback concepto Python (R=NA): %d filas rescatadas en %d CCAA-año",
                              sum(usar_py),
                              dplyr::n_distinct(paste(detalle$ccaa[usar_py], detalle$anio[usar_py]))))
  }

  # Capa Hacienda: las filas con capítulo económico (01..09) no encajan en
  # los conceptos funcionales del cuaderno (sec. 1.4 y §"Variable final"),
  # pero forman un "total gasto" útil para comparar CCAA → concepto = "total".
  hac_idx <- which(detalle$capa == "hacienda" & is.na(detalle$concepto) &
                    grepl("^0?[1-9]$", detalle$codigo))
  if (length(hac_idx) > 0) {
    detalle$concepto[hac_idx] <- "total"
    detalle$score[hac_idx]    <- 1
    detalle$regla[hac_idx]    <- "hacienda_capitulo"
    log_event("INFO", sprintf("Etiquetadas %d filas Hacienda como concepto=total", length(hac_idx)))
  }

  # NOTA (2026-07-03): la prioridad del concepto_python local sobre las reglas
  # globales toscas ahora la resuelve el propio motor `asignar_concepto` por score
  # de especificidad (python_local=78 > global_codigo=74/66). El bloque de override
  # posterior que había aquí quedó redundante y se retiró.
  discrepancias_concepto <- .reportar_discrepancias_concepto(detalle, cfg)

  pendientes <- detalle |> dplyr::filter(is.na(.data$concepto))
  asignadas  <- detalle |> dplyr::filter(!is.na(.data$concepto))

  conceptos_estimables <- c("salud_mental","diversidad","igualdad")
  asignadas <- asignadas |>
    dplyr::mutate(
      estimado = !is.na(.data$score) & .data$score < 0.95 & .data$concepto %in% conceptos_estimables
    )

  normalizado <- asignadas |>
    dplyr::group_by(.data$ccaa, .data$ccaa_id3, .data$anio, .data$concepto, .data$capa,
                    .data$consolidacion) |>
    dplyr::summarise(
      importe_eur = sum(.data$importe_eur, na.rm = TRUE),
      es_prorroga = any(.data$es_prorroga),
      estimado    = any(.data$estimado, na.rm = TRUE),
      n_partidas  = dplyr::n(),
      score_medio = mean(.data$score, na.rm = TRUE),
      fuente_url  = dplyr::first(.data$fuente_url),
      fuente_sha256 = dplyr::first(.data$fuente_sha256),
      .groups = "drop"
    )

  log_event("INFO", sprintf("Transformación: asignadas=%d, pendientes=%d, agregadas=%d",
                              nrow(asignadas), nrow(pendientes), nrow(normalizado)))

  alertas_magnitud <- .chequeos_magnitud_minimos(normalizado)
  if (nrow(alertas_magnitud) > 0) {
    log_event("WARN", sprintf("Chequeos de magnitud: %d alertas básicas", nrow(alertas_magnitud)))
  } else {
    log_event("INFO", "Chequeos de magnitud: sin alertas básicas")
  }
  .escribir_reporte_csv(alertas_magnitud,
                        file.path(cfg$transform_dir, "alertas_magnitud.csv"))

  log_series_coverage(normalizado |> dplyr::rename(periodo = "anio") |>
                                       dplyr::select("ccaa","periodo"),
                       "gasto_normalizado")

  save_named_rds(list(
    gasto_normalizado = normalizado,
    gasto_detalle = detalle,
    pendientes_revision = pendientes,
    discrepancias_concepto = discrepancias_concepto,
    alertas_magnitud = alertas_magnitud
  ), cfg$transform_dir)

  invisible(list(gasto_normalizado = normalizado,
                 pendientes_revision = pendientes))
}
