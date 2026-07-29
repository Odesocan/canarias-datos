# =============================================================================
# Sanidad · Canarias en Datos — ETAPA 3: MODELADO
# Proyección/imputación de las series recientes mediante BAGGED ETS (bootstrap),
# emulando el método del proyecto Prevención. Para cada serie anual continua
# (ccaa × genero × variable) con ≥10 observaciones, imputa los años objetivo,
# persistiendo la predicción central (con IC 95%) y las B=100 simulaciones.
# Construye el ced_sanidad modelado con la bandera origen (real/proyección).
# Entrada: 2_transformacion/ced_sanidad.rds. Salida: 3_modelado/*.
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "tidyr", "purrr", "glue"))
  library(dplyr); library(tidyr); library(glue); library(purrr)
})

KEYS <- c("ccaa", "periodo", "genero")

run_modelado <- function(cfg) {
  log_event("INFO", "Iniciando modelado (bagged ETS bootstrap)")
  ensure_dir(cfg$model_dir)

  # Carga bajo demanda del motor de bootstrap (requiere forecast/tibble)
  boot_path <- file.path(cfg$base_path, "R", "imputacion_bootstrap.R")
  if (!file.exists(boot_path)) stop("Falta R/imputacion_bootstrap.R", call. = FALSE)
  source(boot_path, local = FALSE)

  ced <- readRDS(file.path(cfg$transform_dir, "ced_sanidad.rds"))
  vars <- intersect(cfg$imputar_variables, names(ced))

  # Panel largo de entrada: series observadas de las variables proyectables
  panel_largo <- ced |>
    dplyr::select(dplyr::all_of(c(KEYS, vars))) |>
    tidyr::pivot_longer(dplyr::all_of(vars), names_to = "variable", values_to = "valor") |>
    dplyr::filter(!is.na(.data$valor))

  log_event("INFO", glue("Bagged ETS: {length(vars)} variables · {dplyr::n_distinct(panel_largo$ccaa)} CCAA · ",
                         "objetivos {paste(cfg$imputar_target_years, collapse=', ')} · B=100"))

  # Itera los años objetivo; las series que ya cubren el año fallan blando ("ya cubierto")
  partes <- purrr::map(cfg$imputar_target_years, function(ty)
    imputar_panel_multi(panel_largo, variables = vars, target_year = ty, n_bootstrap = 100L))

  central   <- purrr::map_dfr(partes, "central")
  bootstrap <- purrr::map_dfr(partes, "simulaciones")
  fallos    <- purrr::map_dfr(partes, "fallos")
  fallos_reales <- dplyr::filter(fallos, !grepl("ya cubierto", .data$motivo))

  saveRDS(central,   file.path(cfg$model_dir, "imputaciones_centrales.rds"))
  saveRDS(bootstrap, file.path(cfg$model_dir, "imputaciones_bootstrap.rds"))
  if (nrow(fallos_reales) > 0) saveRDS(fallos_reales, file.path(cfg$model_dir, "imputaciones_fallos.rds"))
  log_event("INFO", glue("Imputadas {nrow(central)} celdas centrales · {nrow(bootstrap)} simulaciones · ",
                         "{nrow(fallos_reales)} fallos reales (excl. {nrow(fallos)-nrow(fallos_reales)} 'ya cubierto')"))

  # --- Construye ced_sanidad modelado: rellena centrales donde había NA --------
  ced_mod <- ced
  for (v in vars) {
    cen_v <- central |> dplyr::filter(.data$variable == v) |>
      dplyr::select("ccaa", "genero", "periodo", valor_imp = "valor")
    if (nrow(cen_v) == 0L) next
    ced_mod <- dplyr::left_join(ced_mod, cen_v, by = c("ccaa", "genero", "periodo"))
    fill <- is.na(ced_mod[[v]]) & !is.na(ced_mod$valor_imp)
    ced_mod[[v]][fill] <- ced_mod$valor_imp[fill]
    ced_mod$valor_imp <- NULL
  }
  # Recalcula el reescalado 0-100 del índice con los valores completados
  if ("mort_evitable_idx" %in% names(ced_mod))
    ced_mod$mort_evitable_idx_0_100 <- rescale_0_100(ced_mod$mort_evitable_idx)

  # --- Tabla larga con bandera origen (real/proyección) por celda --------------
  ind_cols <- setdiff(names(ced_mod), c(KEYS, "origen_pib"))
  imp_key <- with(central, paste(ccaa, genero, periodo, variable))
  ced_largo <- ced_mod |>
    tidyr::pivot_longer(dplyr::all_of(ind_cols), names_to = "variable", values_to = "valor") |>
    dplyr::filter(!is.na(.data$valor)) |>
    dplyr::mutate(origen = ifelse(paste(.data$ccaa, .data$genero, .data$periodo, .data$variable) %in% imp_key,
                                  "proyeccion", "real"))

  saveRDS(ced_mod, file.path(cfg$model_dir, "ced_sanidad.rds"))
  saveRDS(ced_largo, file.path(cfg$model_dir, "ced_sanidad_largo.rds"))
  utils::write.csv(ced_mod, file.path(cfg$model_dir, "ced_sanidad.csv"), row.names = FALSE, fileEncoding = "UTF-8")

  n_proy <- sum(ced_largo$origen == "proyeccion")
  log_event("OK", glue("ced_sanidad modelado: {nrow(ced_mod)} filas · {n_proy} celdas proyectadas · ",
                       "{nrow(ced_largo)} celdas totales ({round(100*n_proy/nrow(ced_largo),1)}% proyección)"))
  invisible(list(ced = ced_mod, central = central, bootstrap = bootstrap, largo = ced_largo, fallos = fallos_reales))
}
