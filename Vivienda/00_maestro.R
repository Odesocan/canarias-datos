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
        sprintf("No se pudo localizar la carpeta raíz de Vivienda desde: %s", start_dir),
        call. = FALSE
      )
    }

    current <- parent
  }
}

project_root <- find_project_root(resolve_script_dir())

source(file.path(project_root, "R", "ccaa_dictionary.R"))
source(file.path(project_root, "R", "pipeline_utils.R"))
source(file.path(project_root, "1_extraccion", "extraccion.R"))
source(file.path(project_root, "2_transformacion", "transformacion.R"))
source(file.path(project_root, "3_modelado", "modelado.R"))
source(file.path(project_root, "4_carga", "carga.R"))

missing_raw_inputs <- function(cfg) {
  raw_paths <- unlist(cfg$raw_files, use.names = TRUE)
  names(raw_paths)[!file.exists(raw_paths)]
}

latest_scraped_alquiler_file <- function(cfg) {
  processed_dir <- file.path(cfg$scraping_dir, "data", "processed")
  files <- list.files(
    processed_dir,
    pattern = "^alquiler_historico_ccaa_.*\\.csv$",
    full.names = TRUE
  )

  if (length(files) == 0) {
    stop(sprintf("No se encontró CSV procesado del scraper en: %s", processed_dir), call. = FALSE)
  }

  files[order(file.info(files)$mtime, decreasing = TRUE)][[1]]
}

normalize_scraped_alquiler_raw <- function(cfg) {
  month_names <- c(
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
  )
  input_path <- latest_scraped_alquiler_file(cfg)
  raw <- utils::read.csv(input_path, stringsAsFactors = FALSE, check.names = FALSE, fileEncoding = "UTF-8-BOM")
  names(raw) <- sub("^\ufeff", "", names(raw))

  required <- c("comunidad", "codigo_ccaa", "mes", "periodo", "precio_m2", "fecha_extraccion")
  missing <- setdiff(required, names(raw))
  if (length(missing) > 0) {
    stop(sprintf("El CSV del scraper no contiene columnas requeridas: %s", paste(missing, collapse = ", ")), call. = FALSE)
  }

  raw$mes <- suppressWarnings(as.integer(raw$mes))
  raw$periodo <- suppressWarnings(as.integer(raw$periodo))
  raw$precio_m2 <- suppressWarnings(as.numeric(raw$precio_m2))
  raw <- raw[!is.na(raw$mes) & !is.na(raw$periodo) & !is.na(raw$precio_m2), , drop = FALSE]

  codigo_ccaa_fmt <- sprintf("%02d", suppressWarnings(as.integer(raw$codigo_ccaa)))

  monthly <- data.frame(
    ccaa = raw$comunidad,
    codigo_ccaa = codigo_ccaa_fmt,
    periodo = sprintf("%04d-%02d-01", raw$periodo, raw$mes),
    periodo_label = paste(month_names[raw$mes], "de", raw$periodo),
    precio_alquiler_m2 = raw$precio_m2,
    fuente_url = "idealista_historico_ccaa",
    fetched_at = raw$fecha_extraccion,
    stringsAsFactors = FALSE
  )

  # Histórico anual: media aritmética de los meses disponibles para cada
  # (CCAA, año). Para años incompletos (p.ej. 2026 con Ene–Mar) se calcula
  # sobre los meses disponibles.
  annual_key <- data.frame(
    ccaa = raw$comunidad,
    codigo_ccaa = codigo_ccaa_fmt,
    anio = raw$periodo,
    precio_alquiler_m2 = raw$precio_m2,
    fecha_extraccion = raw$fecha_extraccion,
    stringsAsFactors = FALSE
  )

  annual_price <- aggregate(
    precio_alquiler_m2 ~ ccaa + codigo_ccaa + anio,
    data = annual_key,
    FUN = function(x) round(mean(x, na.rm = TRUE), 2)
  )

  annual_fetched <- aggregate(
    fecha_extraccion ~ ccaa + anio,
    data = annual_key,
    FUN = max
  )

  historic <- merge(annual_price, annual_fetched, by = c("ccaa", "anio"))
  historic$periodo <- as.character(historic$anio)
  historic$periodo_label <- as.character(historic$anio)
  historic$fuente_url <- "idealista_historico_ccaa"
  historic$fetched_at <- historic$fecha_extraccion
  historic <- historic[, c("ccaa", "codigo_ccaa", "periodo", "periodo_label",
                           "precio_alquiler_m2", "fuente_url", "fetched_at")]
  historic <- historic[order(historic$ccaa, historic$periodo), , drop = FALSE]

  dir.create(cfg$raw_dir, recursive = TRUE, showWarnings = FALSE)
  utils::write.csv(historic, cfg$raw_files$alquiler_historico, row.names = FALSE, fileEncoding = "UTF-8")
  utils::write.csv(monthly, cfg$raw_files$alquiler_mensual, row.names = FALSE, fileEncoding = "UTF-8")
  log_event("OK", glue("Raw de alquiler Idealista normalizado desde {basename(input_path)} (histórico = media anual)"))
}

run_scraping_step <- function(cfg) {
  if (isTRUE(cfg$run_scraping)) {
    args <- c(
      shQuote(cfg$scraper_script),
      "--no-supabase"
    )

    log_event("SCRAPE", glue("Ejecutando scraper: {cfg$scraper_python} {basename(cfg$scraper_script)}"))
    status <- system2(cfg$scraper_python, args = args, wait = TRUE)
    if (!identical(status, 0L)) {
      stop(sprintf("El scraper devolvió código %s", status), call. = FALSE)
    }
    normalize_scraped_alquiler_raw(cfg)
  } else {
    missing <- missing_raw_inputs(cfg)
    if (length(missing) > 0) {
      stop(
        glue(
          "Faltan raw de Idealista en {cfg$raw_dir}: {paste(missing, collapse = ', ')}.\n",
          "Ejecuta el pipeline con scraping: Rscript \"{file.path(cfg$base_path, '00_maestro.R')}\" ",
          "--steps=scraping,extraccion,transformacion,modelado,carga --run-scraping=true --with-db=false\n",
          "Si ya ejecutaste el scraper, revisa que los CSV estén en fuentes/raw/idealista."
        ),
        call. = FALSE
      )
    }
  }

  assert_raw_inputs(cfg)
  log_event("OK", "Raw de Idealista verificados")
}

main <- function() {
  cli_args <- parse_cli_args(commandArgs(trailingOnly = TRUE))
  cfg <- build_pipeline_config(project_root, cli_args)

  log_event("INFO", glue("Proyecto: {cfg$base_path}"))
  log_event("INFO", glue("Pasos: {paste(cfg$steps, collapse = ' -> ')}"))
  log_event("INFO", glue("run-scraping={cfg$run_scraping} | with-db={cfg$with_db}"))

  step_runners <- list(
    scraping = run_scraping_step,
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

  outputs <- c(
    file.path(cfg$load_dir, "ced_vivienda_global.csv"),
    file.path(cfg$load_dir, "ced_vivienda_global.xlsx"),
    file.path(cfg$load_dir, "ced_vivienda_gen.csv"),
    file.path(cfg$load_dir, "ced_vivienda_gen.xlsx")
  )

  if ("carga" %in% cfg$steps) {
    purrr::walk(outputs, assert_file_exists)
  }

  duration_min <- round(as.numeric(difftime(Sys.time(), started_at, units = "mins")), 2)
  log_event("DONE", glue("Pipeline completado en {duration_min} minutos"))
}

main()
