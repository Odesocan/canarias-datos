# =============================================================================
# Sanidad · Canarias en Datos — QA de la etapa de EXTRACCIÓN
# Controles de calidad sobre los datos crudos del INCLASNS:
#   cobertura territorial y temporal, continuidad 2015→último, género,
#   plausibilidad de valores, indicadores no desagregados por CCAA, y
#   validación del índice de mortalidad evitable (construcción portada).
# Salidas: 1_extraccion/qa/*.csv  + informe por consola.
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "tidyr", "purrr", "glue"))
  library(dplyr); library(glue)
})

qa_extraccion <- function(cfg) {
  qa_dir <- file.path(cfg$extraction_dir, "qa"); ensure_dir(qa_dir)
  raw <- readRDS(file.path(cfg$extraction_dir, "raw_sanidad.rds"))

  expected_ccaa <- official_ccaa_levels(include_national = TRUE)   # 17 CCAA + Ceuta + Melilla + Media Estatal
  log_event("QA", glue("Niveles territoriales esperados: {length(expected_ccaa)}"))

  # Normaliza territorio/género/periodo para todo el crudo
  norm <- raw |>
    mutate(
      ccaa    = normalize_ccaa_name(ccaa_raw),
      genero  = normalize_genero(sexo),
      periodo = suppressWarnings(as.integer(anio)),
      valor   = suppressWarnings(as.numeric(valor))
    )

  # --- CCAA sin mapear (literal crudo que no cae en el catálogo oficial) ------
  unmapped <- norm |>
    filter(!ccaa %in% expected_ccaa) |>
    distinct(componente, ccaa_raw, ccaa)
  if (nrow(unmapped) > 0) {
    log_event("WARN", glue("Literales de CCAA sin mapear: {nrow(unmapped)} (ver qa_ccaa_sin_mapear.csv)"))
    write.csv(unmapped, file.path(qa_dir, "qa_ccaa_sin_mapear.csv"), row.names = FALSE)
  } else {
    log_event("OK", "Todos los literales de CCAA se mapean al catálogo oficial")
  }

  # --- Continuidad 2015→último (serie nacional Media Estatal, género total) ---
  cont_flag <- function(years) {
    years <- sort(unique(years[!is.na(years)]))
    if (!length(years)) return(NA)
    ymax <- max(years)
    if (ymax < 2015) return(FALSE)
    all(2015:ymax %in% years)
  }

  # --- Resumen por indicador --------------------------------------------------
  resumen <- norm |>
    group_by(grupo, componente, indicador_codigo, indicador_nombre) |>
    summarise(
      filas       = dplyr::n(),
      con_valor   = sum(!is.na(valor)),
      na_pct      = round(100 * mean(is.na(valor)), 1),
      generos     = paste(sort(unique(genero[!is.na(genero)])), collapse = "/"),
      n_ccaa      = dplyr::n_distinct(ccaa[ccaa %in% expected_ccaa]),
      solo_nacional = all(ccaa[!is.na(valor)] %in% c("Media Estatal")),
      anio_min    = suppressWarnings(min(periodo[!is.na(valor)])),
      anio_max    = suppressWarnings(max(periodo[!is.na(valor)])),
      continua_2015 = cont_flag(periodo[ccaa == "Media Estatal" & genero == "total" & !is.na(valor)]),
      canarias_ok = any(ccaa == "Canarias" & !is.na(valor)),
      canarias_cont2015 = cont_flag(periodo[ccaa == "Canarias" & genero == "total" & !is.na(valor)]),
      val_min     = round(suppressWarnings(min(valor, na.rm = TRUE)), 2),
      val_med     = round(suppressWarnings(median(valor, na.rm = TRUE)), 2),
      val_max     = round(suppressWarnings(max(valor, na.rm = TRUE)), 2),
      .groups = "drop"
    ) |>
    mutate(ccaa_faltantes = purrr::map_chr(componente, function(k) {
      pres <- norm |> filter(componente == k, ccaa %in% expected_ccaa, !is.na(valor)) |> pull(ccaa) |> unique()
      falt <- setdiff(setdiff(expected_ccaa, "Media Estatal"), pres)
      if (length(falt) == 0) "-" else paste(falt, collapse = ", ")
    })) |>
    arrange(grupo, componente)

  write.csv(resumen, file.path(qa_dir, "qa_resumen_indicadores.csv"), row.names = FALSE)

  # --- Índice de mortalidad evitable: construcción y validación ---------------
  mort_raw <- readRDS(file.path(cfg$extraction_dir, "mort_evitable.rds"))
  mort_wide <- tidy_sns_group(mort_raw)
  idx <- build_mort_evitable_idx(mort_wide, components = cfg$mort_evitable_keys)
  idx$mort_evitable_idx_0_100 <- rescale_0_100(idx$mort_evitable_idx)
  write.csv(idx, file.path(qa_dir, "qa_mort_evitable_idx.csv"), row.names = FALSE)

  # Chequeos del índice
  comp_means <- vapply(cfg$mort_evitable_keys, function(c) mean(mort_wide[[c]], na.rm = TRUE), numeric(1))
  idx_nac <- idx |> filter(ccaa == "Media Estatal", genero == "total") |> arrange(periodo)
  idx_can <- idx |> filter(ccaa == "Canarias", genero == "total") |> arrange(periodo)

  # --- Informe por consola ----------------------------------------------------
  cat("\n=================== QA EXTRACCIÓN — SANIDAD ===================\n")
  cat(sprintf("Indicadores: %d | Filas crudas: %d | Niveles CCAA esperados: %d\n",
              nrow(resumen), nrow(raw), length(expected_ccaa)))
  cat("\n--- Resumen por indicador ---\n")
  print(as.data.frame(resumen[, c("grupo","componente","indicador_codigo","generos","n_ccaa",
                                  "solo_nacional","anio_min","anio_max","continua_2015",
                                  "canarias_cont2015","val_min","val_med","val_max")]),
        row.names = FALSE)

  cat("\n--- Avisos de cobertura ---\n")
  sn <- resumen |> filter(solo_nacional)
  if (nrow(sn)) cat(sprintf("  · Indicadores SOLO nacionales (sin desglose CCAA): %s\n",
                            paste(sprintf("%s (%s)", sn$componente, sn$indicador_codigo), collapse = ", ")))
  nc <- resumen |> filter(!continua_2015 %in% TRUE)
  if (nrow(nc)) cat(sprintf("  · Serie nacional NO continua 2015→último: %s\n",
                            paste(sprintf("%s", nc$componente), collapse = ", ")))
  ncan <- resumen |> filter(!canarias_cont2015 %in% TRUE)
  if (nrow(ncan)) cat(sprintf("  · Canarias NO continua 2015→último: %s\n",
                              paste(sprintf("%s", ncan$componente), collapse = ", ")))
  falt <- resumen |> filter(ccaa_faltantes != "-")
  if (nrow(falt)) { cat("  · CCAA faltantes por indicador:\n"); for (i in seq_len(nrow(falt)))
    cat(sprintf("      %s: %s\n", falt$componente[i], falt$ccaa_faltantes[i])) }

  cat("\n--- Índice de mortalidad evitable ---\n")
  cat(sprintf("  Componentes (media histórica nacional usada como normalizador):\n"))
  for (c in names(comp_means)) cat(sprintf("      %s = %.2f por 100.000\n", c, comp_means[c]))
  cat(sprintf("  Filas del índice: %d | NA: %d\n", nrow(idx), sum(is.na(idx$mort_evitable_idx))))
  cat(sprintf("  Índice (ratio) — rango: %.3f a %.3f | mediana: %.3f\n",
              min(idx$mort_evitable_idx, na.rm=TRUE), max(idx$mort_evitable_idx, na.rm=TRUE),
              median(idx$mort_evitable_idx, na.rm=TRUE)))
  cat(sprintf("  Reescalado 0-100 — rango: %.1f a %.1f\n",
              min(idx$mort_evitable_idx_0_100, na.rm=TRUE), max(idx$mort_evitable_idx_0_100, na.rm=TRUE)))
  cat("  Serie nacional (Media Estatal, total) últimos años:\n")
  tail_nac <- tail(idx_nac[, c("periodo","mort_evitable_idx","mort_evitable_idx_0_100")], 5)
  print(as.data.frame(round_df <- data.frame(periodo=tail_nac$periodo,
        idx=round(tail_nac$mort_evitable_idx,3), idx_0_100=round(tail_nac$mort_evitable_idx_0_100,1))),
        row.names = FALSE)
  cat("  Canarias vs Media Estatal (total, último año común):\n")
  yr <- max(intersect(idx_nac$periodo, idx_can$periodo))
  vn <- idx_nac$mort_evitable_idx[idx_nac$periodo==yr]; vc <- idx_can$mort_evitable_idx[idx_can$periodo==yr]
  cat(sprintf("      %d — Canarias=%.3f  Media Estatal=%.3f  (%.0f%% vs media)\n",
              yr, vc, vn, 100*vc/vn))

  # --- Gasto sanitario sobre PIB (fuente externa: Presupuestos) ---------------
  gpib_path <- file.path(cfg$extraction_dir, "gasto_pib.rds")
  cat("\n--- Gasto sanitario sobre PIB (área de Presupuestos) ---\n")
  if (file.exists(gpib_path)) {
    gpib <- readRDS(gpib_path)
    exp_ccaa17 <- setdiff(official_ccaa_levels(include_national = TRUE), c("Media Estatal", "Ceuta", "Melilla"))
    gcan <- gpib[gpib$ccaa == "Canarias", ]
    falt17 <- setdiff(exp_ccaa17, unique(gpib$ccaa))
    cat(sprintf("  Filas: %d | CCAA: %d | Años: %d-%d\n",
                nrow(gpib), dplyr::n_distinct(gpib$ccaa), min(gpib$periodo), max(gpib$periodo)))
    cat(sprintf("  pct_pib_sanidad — rango: %.2f%% a %.2f%% | mediana: %.2f%%\n",
                min(gpib$pct_pib_sanidad), max(gpib$pct_pib_sanidad), median(gpib$pct_pib_sanidad)))
    cat(sprintf("  origen_pib: %s\n",
                paste(names(table(gpib$origen_pib)), table(gpib$origen_pib), sep = "=", collapse = " | ")))
    cat(sprintf("  CCAA sin dato (de 17 esperadas): %s\n", if (length(falt17)) paste(falt17, collapse = ", ") else "-"))
    cat(sprintf("  Canarias continua 2015->: %s | rango Canarias: %.2f%%-%.2f%%\n",
                cont_flag(gcan$periodo), min(gcan$pct_pib_sanidad), max(gcan$pct_pib_sanidad)))
    yr2 <- suppressWarnings(max(gpib$periodo[gpib$origen_pib == "real"]))
    med2 <- median(gpib$pct_pib_sanidad[gpib$periodo == yr2])
    vc2  <- gpib$pct_pib_sanidad[gpib$ccaa == "Canarias" & gpib$periodo == yr2]
    cat(sprintf("  %d (último con PIB real) — Canarias=%.2f%%  mediana CCAA=%.2f%%\n", yr2, vc2, med2))
    write.csv(gpib, file.path(qa_dir, "qa_gasto_pib.csv"), row.names = FALSE)
  } else {
    cat("  NO disponible (falta gasto_pib.rds).\n")
  }
  cat("\n==============================================================\n")

  invisible(list(resumen = resumen, idx = idx, comp_means = comp_means))
}
# Ejecución: source(este archivo) tras cargar R/pipeline_utils.R y luego qa_extraccion(cfg).
