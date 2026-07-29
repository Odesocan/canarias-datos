# ===========================================================================
# setup-packages.R -- Instala los paquetes R requeridos por el pipeline
# ===========================================================================
# Cuaderno metodologico v2: dependencias del pipeline ETL + modelado
# multi-algoritmo (extraccion, transformacion, modelado, carga).
#
# Uso (desde el directorio Dependencia/):
#   Rscript setup-packages.R           # instala lo que falte
#   Rscript setup-packages.R --check   # solo lista lo que falta
# ===========================================================================

CRAN_REPO <- "https://cloud.r-project.org"

PIPELINE_PACKAGES <- list(
  base = c(
    "dplyr", "purrr", "stringr", "stringi", "stringdist",
    "tibble", "tidyr", "lubridate", "readr", "glue", "fs", "digest"
  ),
  extraccion = c(
    "readxl", "rvest", "httr2", "xml2", "janitor"
  ),
  modelado = c(
    "forecast",   # ARIMA, ETS
    "prophet",    # Prophet (per-serie)
    "ranger",     # Random Forest (modelo global)
    "xgboost"     # XGBoost (modelo global)
  ),
  carga = c(
    "DBI", "RPostgres", "writexl"
  )
)

all_pkgs <- unique(unlist(PIPELINE_PACKAGES, use.names = FALSE))

is_installed <- function(p) requireNamespace(p, quietly = TRUE)
missing_pkgs <- function() Filter(Negate(is_installed), all_pkgs)

args <- commandArgs(trailingOnly = TRUE)

if ("--check" %in% args) {
  miss <- missing_pkgs()
  if (length(miss) == 0) {
    cat("OK: todos los paquetes (", length(all_pkgs), ") estan instalados\n", sep = "")
    quit(status = 0)
  }
  cat("Faltan", length(miss), "paquetes:\n")
  cat(paste("  -", miss, collapse = "\n"), "\n")
  quit(status = 1)
}

# Instalar lo que falte en la libreria global
miss <- missing_pkgs()
if (length(miss) == 0) {
  cat("OK: todos los paquetes (", length(all_pkgs), ") ya estan instalados\n", sep = "")
  quit(status = 0)
}

cat("Instalando", length(miss), "paquetes:", paste(miss, collapse = ", "), "\n")
install.packages(miss, repos = CRAN_REPO)

still_missing <- missing_pkgs()
if (length(still_missing) > 0) {
  cat("ERROR: estos paquetes no se pudieron instalar:\n")
  cat(paste("  -", still_missing, collapse = "\n"), "\n")
  quit(status = 1)
}

cat("OK: ", length(all_pkgs), " paquetes disponibles\n", sep = "")
