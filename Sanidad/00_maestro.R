# =============================================================================
# Sanidad · Canarias en Datos — MAESTRO
# Orquesta las etapas del pipeline. En fase fundacional está operativa la
# extracción; transformación, modelado y carga se añadirán a continuación.
# Uso:  Rscript 00_maestro.R [--steps=extraccion]
# =============================================================================

suppressPackageStartupMessages(library(glue))

resolve_script_dir <- function() {
  file_arg <- grep("^--file=", commandArgs(), value = TRUE)
  if (length(file_arg) == 0) return(normalizePath(getwd(), winslash = "/", mustWork = TRUE))
  script_path <- sub("^--file=", "", file_arg[[1]])
  script_path <- gsub("~\\+~", " ", script_path)
  dirname(normalizePath(script_path, winslash = "/", mustWork = TRUE))
}

find_project_root <- function(start_dir) {
  current <- normalizePath(start_dir, winslash = "/", mustWork = TRUE)
  repeat {
    markers <- c(
      file.path(current, "R", "ccaa_dictionary.R"),
      file.path(current, "R", "pipeline_utils.R"),
      file.path(current, "1_extraccion", "extraccion.R")
    )
    if (all(file.exists(markers))) return(current)
    parent <- dirname(current)
    if (identical(parent, current)) {
      stop("No se pudo localizar la raíz del proyecto Sanidad.", call. = FALSE)
    }
    current <- parent
  }
}

project_root <- find_project_root(resolve_script_dir())

# Carga .Renviron local si existe (credenciales INCLASNS / Supabase)
local_renv <- file.path(project_root, ".Renviron")
if (file.exists(local_renv)) readRenviron(local_renv)

source(file.path(project_root, "R", "ccaa_dictionary.R"))
source(file.path(project_root, "R", "pipeline_utils.R"))
source(file.path(project_root, "1_extraccion", "extraccion.R"))
source(file.path(project_root, "2_transformacion", "transformacion.R"))
source(file.path(project_root, "3_modelado", "modelado.R"))
source(file.path(project_root, "4_carga", "carga.R"))

main <- function() {
  args <- commandArgs(trailingOnly = TRUE)
  steps_arg <- sub("^--steps=", "", grep("^--steps=", args, value = TRUE))
  steps <- if (length(steps_arg)) strsplit(steps_arg[[1]], ",")[[1]]
           else c("extraccion", "transformacion", "modelado", "carga")

  cfg <- build_sanidad_config(project_root)
  if (any(grepl("^--with-db", args))) cfg$with_db <- TRUE   # fuerza la carga a Supabase

  started_at <- Sys.time()
  runners <- list(extraccion = run_extraccion, transformacion = run_transformacion,
                  modelado = run_modelado, carga = run_carga)
  for (step in steps) {
    if (is.null(runners[[step]])) { log_event("WARN", glue("Paso no soportado: {step}")); next }
    log_event("STEP", paste("Inicio", step))
    runners[[step]](cfg)
    log_event("STEP", paste("Fin", step))
  }
  dur <- round(as.numeric(difftime(Sys.time(), started_at, units = "mins")), 2)
  log_event("DONE", glue("Pipeline [{paste(steps, collapse=', ')}] completado en {dur} minutos"))
}

if (identical(environment(), globalenv()) && !interactive()) {
  main()
}
