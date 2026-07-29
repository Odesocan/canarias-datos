# =============================================================================
# Sanidad · Canarias en Datos — ETAPA 2: TRANSFORMACIÓN
# Materializa ced_sanidad: panel longitudinal por (ccaa, periodo, genero) con
# una columna por indicador de la selección núcleo. Construye el ÚNICO índice
# sintético del área —mortalidad evitable— y deja el resto como indicadores
# sueltos. Une la variable externa de gasto sobre PIB (área de Presupuestos).
# Entrada: RDS de 1_extraccion. Salida: 2_transformacion/ced_sanidad.rds (+csv).
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "tidyr", "purrr", "glue"))
  library(dplyr); library(glue)
})

KEYS <- c("ccaa", "periodo", "genero")

run_transformacion <- function(cfg) {
  log_event("INFO", "Iniciando transformación (ced_sanidad)")
  ensure_dir(cfg$transform_dir)

  raw_all <- readRDS(file.path(cfg$extraction_dir, "raw_sanidad.rds"))

  # 1) Tabla ancha: un indicador por columna, por (ccaa, periodo, genero).
  #    Los indicadores de sistema (recursos, gasto, accesibilidad) solo traen
  #    genero='total', por lo que sus columnas quedan NA en las filas de
  #    hombres/mujeres (no tienen desglose por género en el INCLASNS).
  wide <- tidy_sns_group(raw_all)
  log_event("INFO", glue("Tabla ancha: {nrow(wide)} filas × {ncol(wide)} columnas"))

  # 2) Índice de mortalidad evitable (único índice sintético del área).
  #    Se calcula sobre una copia para NO alterar los valores crudos de los
  #    componentes (build_mort_evitable_idx normaliza in situ sus columnas).
  mort_cols <- intersect(cfg$mort_evitable_keys, names(wide))
  idx <- build_mort_evitable_idx(wide[, c(KEYS, mort_cols)], components = cfg$mort_evitable_keys)
  idx$mort_evitable_idx_0_100 <- rescale_0_100(idx$mort_evitable_idx)
  idx_slim <- idx[, c(KEYS, "mort_evitable_idx", "mort_evitable_idx_0_100")]

  ced <- dplyr::left_join(wide, idx_slim, by = KEYS)

  # 3) Fuente externa: gasto sanitario sobre PIB (Presupuestos), solo 'total'.
  gpib_path <- file.path(cfg$extraction_dir, "gasto_pib.rds")
  if (file.exists(gpib_path)) {
    gpib <- readRDS(gpib_path)
    ced <- dplyr::left_join(ced, gpib, by = KEYS)
    log_event("INFO", glue("Unido gasto/PIB (Presupuestos): {sum(!is.na(ced$pct_pib_sanidad))} filas con dato"))
  } else {
    log_event("WARN", "No se encontró gasto_pib.rds; ced_sanidad sin gasto/PIB")
  }

  # 4) Orden de columnas: claves + estado de salud + componentes mortalidad +
  #    índice + recursos + gasto + accesibilidad + resultados + denominador.
  orden <- c(
    KEYS,
    "avs_65",
    "mort_cancer", "mort_cardio", "mort_diabetes", "mort_ictus", "mort_epoc",
    "mort_evitable_idx", "mort_evitable_idx_0_100",
    "med_ae", "med_ap", "enf_ae", "enf_ap", "camas",
    "gasto_farmacia_pct", "pct_pib_sanidad", "imp_sanidad_eur", "pib_regional_eur", "origen_pib",
    "espera_quir", "espera_ae",
    "reingresos_psiq",
    "poblacion_total"
  )
  orden <- intersect(orden, names(ced))
  ced <- ced[, c(orden, setdiff(names(ced), orden))] |>
    dplyr::arrange(.data$ccaa, .data$periodo, match(.data$genero, c("total", "hombres", "mujeres")))

  # 5) Validación de unicidad de claves
  dup <- ced |> dplyr::count(dplyr::across(dplyr::all_of(KEYS))) |> dplyr::filter(.data$n > 1)
  if (nrow(dup) > 0) stop(glue("ced_sanidad: {nrow(dup)} claves duplicadas (ccaa,periodo,genero)"), call. = FALSE)

  saveRDS(ced, file.path(cfg$transform_dir, "ced_sanidad.rds"))
  utils::write.csv(ced, file.path(cfg$transform_dir, "ced_sanidad.csv"), row.names = FALSE, fileEncoding = "UTF-8")

  log_event("OK", glue("ced_sanidad: {nrow(ced)} filas × {ncol(ced)} columnas | {dplyr::n_distinct(ced$ccaa)} CCAA | periodo {min(ced$periodo)}-{max(ced$periodo)}"))
  invisible(ced)
}
