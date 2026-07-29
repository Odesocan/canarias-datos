
# ===========================================================================
# 00_maestro.R -- Script maestro del pipeline Dependencia (SAAD)
# ===========================================================================
#
# Ejecuta las 4 etapas del pipeline en secuencia:
#   extraccion -> transformacion -> modelado -> carga
#
# Uso desde terminal:
#   Rscript "Dependencia/00_maestro.R" --steps=extraccion,transformacion,modelado,carga --with-db=true
#
# Opciones CLI:
#   --steps=extraccion,transformacion,modelado,carga  (cuales ejecutar)
#   --with-db=true/false                              (cargar a Supabase y leer PPD)
#   --horizon-end=YYYY-MM-01                          (fecha fin forecast; default = hoy + 6 meses)
#   --force-download=true/false                       (ignorar cache XLS)
#   --include-prophet=true/false                      (incluir Prophet en CV; default false porque
#                                                      con series mensuales cortas <= 40 puntos
#                                                      tiene NMAE 4x peor que ETS/ARIMA y es lento)
#
# Cuaderno metodologico v2 (2026-04-29):
#   * Corte 2023 como anio base (saad_years = 2023:actual)
#   * PPD obligatoria desde general.censo_ppd con fallback XLS
#   * Matriz de 10 indicadores en transformacion (ver dashboard_indicators)
#   * Salida principal: ced_dependencia_global + ced_dependencia_gen
#
# Variables de entorno requeridas para --with-db=true:
#   SUPABASE_HOST, SUPABASE_PORT, SUPABASE_USER, SUPABASE_PASS,
#   SUPABASE_DBNAME, SUPABASE_SCHEMA
#
# ===========================================================================

suppressPackageStartupMessages({
  library(glue)
})

resolve_script_dir <- function() {
  file_arg <- grep("^--file=", commandArgs(), value = TRUE)
  if (length(file_arg) == 0) {
    return(normalizePath(getwd(), winslash = "/", mustWork = TRUE))
  }

  script_path <- sub("^--file=", "", file_arg[[1]])
  script_path <- gsub("~\\+~", " ", script_path)

  dirname(normalizePath(script_path, winslash = "/", mustWork = TRUE))
}

project_root <- resolve_script_dir()

source(file.path(project_root, "utils", "ccaa_dictionary.R"))
source(file.path(project_root, "utils", "pipeline_utils.R"))

main <- function() {
  cli_args <- parse_cli_args(commandArgs(trailingOnly = TRUE))
  cfg <- build_pipeline_config(project_root, cli_args)

  step_scripts <- list(
    extraccion     = file.path(project_root, "1_extraccion", "extraccion.R"),
    transformacion = file.path(project_root, "2_transformacion", "transformacion.R"),
    modelado       = file.path(project_root, "3_modelado", "modelado.R"),
    carga          = file.path(project_root, "4_carga", "carga.R")
  )

  purrr::walk(cfg$steps, function(step) source(step_scripts[[step]]))

  log_event("INFO", glue("Proyecto: {cfg$base_path}"))
  log_event("INFO", glue("Pasos: {paste(cfg$steps, collapse = ' -> ')}"))
  log_event("INFO", glue("with-db={cfg$with_db} | anios={min(cfg$saad_years)}-{max(cfg$saad_years)}"))
  log_event("INFO", glue("forecast horizon: {cfg$forecast_horizon_end}"))

  step_runners <- setNames(
    lapply(cfg$steps, function(step) get(paste0("run_", step), mode = "function")),
    cfg$steps
  )

  started_at <- Sys.time()

  for (step in cfg$steps) {
    log_event("STEP", paste("Inicio", step))
    step_runners[[step]](cfg)
    log_event("STEP", paste("Fin", step))
  }

  if ("carga" %in% cfg$steps) {
    assert_file_exists(file.path(cfg$load_dir, "ced_dependencia_global.csv"))
  }

  duration_min <- round(as.numeric(difftime(Sys.time(), started_at, units = "mins")), 2)
  log_event("DONE", glue("Pipeline completado en {duration_min} minutos"))
}

main()
