# =============================================================================
# Sanidad · Canarias en Datos — QA de la etapa de MODELADO (bagged ETS)
# Valida la imputación: celdas proyectadas, nº de simulaciones, amplitud del
# IC 95%, fallos, distribución origen (real/proyección) y plausibilidad de los
# valores imputados frente al histórico observado.
# Salida: 3_modelado/qa/*.csv + informe por consola.
# =============================================================================

suppressPackageStartupMessages({ require_packages(c("dplyr","glue")); library(dplyr); library(glue) })

qa_modelado <- function(cfg) {
  qa_dir <- file.path(cfg$model_dir, "qa"); ensure_dir(qa_dir)
  central   <- readRDS(file.path(cfg$model_dir, "imputaciones_centrales.rds"))
  bootstrap <- readRDS(file.path(cfg$model_dir, "imputaciones_bootstrap.rds"))
  largo     <- readRDS(file.path(cfg$model_dir, "ced_sanidad_largo.rds"))
  ced_obs   <- readRDS(file.path(cfg$transform_dir, "ced_sanidad.rds"))
  fpath <- file.path(cfg$model_dir, "imputaciones_fallos.rds")
  fallos <- if (file.exists(fpath)) readRDS(fpath) else NULL

  # Resumen por variable: celdas imputadas, años, sims, amplitud IC, plausibilidad
  resumen <- central |>
    dplyr::mutate(ic_rel = ifelse(valor != 0, (ls_95 - li_95) / abs(valor), NA_real_)) |>
    dplyr::group_by(variable) |>
    dplyr::summarise(
      celdas_imp = dplyr::n(),
      anios = paste(sort(unique(periodo)), collapse = ","),
      generos = paste(sort(unique(genero)), collapse = "/"),
      ic_rel_medio = round(mean(ic_rel, na.rm = TRUE), 3),
      val_min = round(min(valor), 2), val_max = round(max(valor), 2),
      .groups = "drop"
    )
  # sims por celda
  sims_por_celda <- bootstrap |>
    dplyr::count(ccaa, genero, variable, periodo, name = "n_sims")
  resumen <- resumen |>
    dplyr::left_join(
      sims_por_celda |> dplyr::group_by(variable) |>
        dplyr::summarise(sims_min = min(n_sims), sims_med = round(median(n_sims)), .groups = "drop"),
      by = "variable")

  # Plausibilidad: imputado dentro del rango observado ampliado (±20%)
  rangos_obs <- purrr::map_dfr(unique(central$variable), function(v) {
    ob <- ced_obs[[v]]
    tibble::tibble(variable = v, obs_min = min(ob, na.rm = TRUE), obs_max = max(ob, na.rm = TRUE))
  })
  chk <- central |> dplyr::left_join(rangos_obs, by = "variable") |>
    dplyr::mutate(fuera_rango = valor < obs_min * 0.8 | valor > obs_max * 1.2)
  fuera <- dplyr::filter(chk, fuera_rango)

  write.csv(resumen, file.path(qa_dir, "qa_modelado_resumen.csv"), row.names = FALSE)
  write.csv(central, file.path(qa_dir, "qa_imputaciones_centrales.csv"), row.names = FALSE)
  if (nrow(fuera) > 0) write.csv(fuera, file.path(qa_dir, "qa_imputaciones_fuera_rango.csv"), row.names = FALSE)

  origen_tab <- largo |> dplyr::count(origen) |> dplyr::mutate(pct = round(100 * n / sum(n), 1))

  cat("\n=================== QA MODELADO — bagged ETS bootstrap ===================\n")
  cat(sprintf("Celdas imputadas: %d | Simulaciones: %d | Fallos reales: %d\n",
              nrow(central), nrow(bootstrap), if (is.null(fallos)) 0 else nrow(fallos)))
  cat(sprintf("Origen (panel largo): %s\n",
              paste(sprintf("%s=%d (%.1f%%)", origen_tab$origen, origen_tab$n, origen_tab$pct), collapse = " | ")))
  cat(sprintf("Plausibilidad: %d celdas fuera del rango observado ±20%% %s\n",
              nrow(fuera), ifelse(nrow(fuera) == 0, "✓", "(ver qa_imputaciones_fuera_rango.csv)")))
  cat("\n--- Resumen por variable ---\n")
  print(as.data.frame(resumen), row.names = FALSE)
  if (!is.null(fallos) && nrow(fallos) > 0) {
    cat("\n--- Fallos reales (series no imputables) ---\n")
    print(as.data.frame(fallos |> dplyr::count(variable, motivo)), row.names = FALSE)
  }
  cat("\n--- Canarias: valores imputados ---\n")
  print(as.data.frame(central |> dplyr::filter(ccaa == "Canarias", genero == "total") |>
                        dplyr::select(variable, periodo, valor, li_95, ls_95) |>
                        dplyr::mutate(across(c(valor, li_95, ls_95), \(x) round(x, 2)))), row.names = FALSE)
  cat("\n=========================================================================\n")
  invisible(resumen)
}
