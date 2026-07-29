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

find_project_root <- function(start_dir) {
  current <- normalizePath(start_dir, winslash = "/", mustWork = TRUE)

  repeat {
    expected_files <- c(
      file.path(current, "R", "ccaa_dictionary.R"),
      file.path(current, "R", "pipeline_utils.R"),
      file.path(current, "1_extraccion", "extraccion.R")
    )

    if (all(file.exists(expected_files))) {
      return(current)
    }

    parent <- dirname(current)
    if (identical(parent, current)) {
      stop(
        sprintf("No se pudo localizar la carpeta raíz de Salud mental desde: %s", start_dir),
        call. = FALSE
      )
    }

    current <- parent
  }
}

project_root <- find_project_root(resolve_script_dir())

# Carga .Renviron del proyecto si existe (sobrescribe el global solo para este proceso)
local_renv <- file.path(project_root, ".Renviron")
if (file.exists(local_renv)) {
  readRenviron(local_renv)
}

source(file.path(project_root, "R", "ccaa_dictionary.R"))
source(file.path(project_root, "R", "pipeline_utils.R"))
source(file.path(project_root, "1_extraccion", "extraccion.R"))
source(file.path(project_root, "2_transformacion", "transformacion.R"))
source(file.path(project_root, "3_modelado", "modelado.R"))
source(file.path(project_root, "4_carga", "carga.R"))

main <- function() {
  cli_args <- parse_cli_args(commandArgs(trailingOnly = TRUE))
  cfg <- build_pipeline_config(project_root, cli_args)

  log_event("INFO", glue("Proyecto: {cfg$base_path}"))
  log_event("INFO", glue("Pasos: {paste(cfg$steps, collapse = ' -> ')}"))
  log_event("INFO", glue("with-db={cfg$with_db} | horizonte={cfg$horizon_year} | cv_folds={cfg$cv_folds}"))

  step_runners <- list(
    extraccion = run_extraccion,
    transformacion = run_transformacion,
    modelado = run_modelado,
    carga = run_carga
  )

  started_at <- Sys.time()

  for (step in cfg$steps) {
    log_event("STEP", paste("Inicio", step))
    step_runners[[step]](cfg)
    log_event("STEP", paste("Fin", step))
  }

  if ("carga" %in% cfg$steps) {
    outputs <- c(
      file.path(cfg$load_dir, "ced_saludmental.csv"),
      file.path(cfg$load_dir, "ced_saludmental.xlsx")
    )
    purrr::walk(outputs, assert_file_exists)
  }

  duration_min <- round(as.numeric(difftime(Sys.time(), started_at, units = "mins")), 2)
  log_event("DONE", glue("Pipeline completado en {duration_min} minutos"))
}

main()
