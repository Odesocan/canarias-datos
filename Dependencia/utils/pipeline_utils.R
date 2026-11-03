# ===========================================================================
# pipeline_utils.R -- Utilidades compartidas del pipeline Dependencia (SAAD)
# ===========================================================================

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0) {
    return(y)
  }

  if (is.character(x) && identical(trimws(x), "")) {
    return(y)
  }

  x
}

require_packages <- function(packages) {
  missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly = TRUE)]
  if (length(missing) > 0) {
    stop(
      sprintf(
        "Faltan paquetes de R requeridos: %s",
        paste(missing, collapse = ", ")
      ),
      call. = FALSE
    )
  }

  invisible(packages)
}

log_event <- function(level, message) {
  timestamp <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
  cat(sprintf("[%s] [%-7s] %s\n", timestamp, level, message))
}

parse_bool <- function(x, default = FALSE) {
  if (is.null(x) || length(x) == 0) {
    return(default)
  }

  value <- tolower(trimws(as.character(x[[1]])))
  if (value %in% c("true", "1", "yes", "y", "si", "sí")) {
    return(TRUE)
  }
  if (value %in% c("false", "0", "no", "n")) {
    return(FALSE)
  }

  default
}

parse_cli_args <- function(args) {
  parsed <- list()
  index <- 1L

  while (index <= length(args)) {
    arg <- args[[index]]

    if (!startsWith(arg, "--")) {
      index <- index + 1L
      next
    }

    item <- sub("^--", "", arg)

    if (grepl("=", item, fixed = TRUE)) {
      parts <- strsplit(item, "=", fixed = TRUE)[[1]]
      key <- parts[[1]]
      value <- paste(parts[-1], collapse = "=")
    } else if (index < length(args) && !startsWith(args[[index + 1L]], "--")) {
      key <- item
      value <- args[[index + 1L]]
      index <- index + 1L
    } else {
      key <- item
      value <- "true"
    }

    parsed[[key]] <- value
    index <- index + 1L
  }

  parsed
}

cli_value <- function(args, keys, default = NULL) {
  for (key in keys) {
    if (!is.null(args[[key]])) {
      return(args[[key]])
    }
  }

  default
}

normalize_steps <- function(value) {
  allowed <- c("extraccion", "transformacion", "modelado", "carga")
  items <- strsplit(value %||% paste(allowed, collapse = ","), ",", fixed = TRUE)[[1]]
  items <- tolower(trimws(items))
  items <- items[nzchar(items)]

  invalid <- setdiff(items, allowed)
  if (length(invalid) > 0) {
    stop(sprintf("Pasos no soportados: %s", paste(invalid, collapse = ", ")), call. = FALSE)
  }

  items <- unique(items)
  canonical_subset <- allowed[allowed %in% items]
  if (!identical(items, canonical_subset)) {
    stop(
      sprintf(
        "Los pasos deben seguir el orden canonico: %s",
        paste(allowed, collapse = " -> ")
      ),
      call. = FALSE
    )
  }

  items
}

ensure_dir <- function(path) {
  dir.create(path, recursive = TRUE, showWarnings = FALSE)
  invisible(path)
}

assert_file_exists <- function(path, label = NULL) {
  if (!file.exists(path)) {
    stop(sprintf("Falta %s: %s", label %||% "archivo", path), call. = FALSE)
  }
}

any_file_exists <- function(paths) {
  any(file.exists(paths))
}

assert_required_columns <- function(data, required, label = deparse(substitute(data))) {
  missing <- setdiff(required, names(data))
  if (length(missing) > 0) {
    stop(
      sprintf(
        "%s no contiene columnas requeridas: %s",
        label,
        paste(missing, collapse = ", ")
      ),
      call. = FALSE
    )
  }
}

assert_unique_keys <- function(data, keys, label = deparse(substitute(data))) {
  duplicated_rows <- dplyr::count(data, dplyr::across(dplyr::all_of(keys)), name = "n") |>
    dplyr::filter(.data$n > 1)

  if (nrow(duplicated_rows) > 0) {
    stop(
      sprintf("%s contiene claves duplicadas para: %s", label, paste(keys, collapse = ", ")),
      call. = FALSE
    )
  }
}

save_named_rds <- function(objects, dir_path) {
  ensure_dir(dir_path)

  purrr::iwalk(objects, function(value, name) {
    saveRDS(value, file.path(dir_path, paste0(name, ".rds")))
  })

  invisible(objects)
}

load_named_rds <- function(dir_path, names) {
  purrr::set_names(names) |>
    purrr::map(function(name) {
      readRDS(file.path(dir_path, paste0(name, ".rds")))
    })
}

# ===========================================================================
# Normalizacion de texto y CCAA
# ===========================================================================

normalize_key <- function(x) {
  value <- trimws(as.character(x))
  value <- iconv(value, from = "", to = "ASCII//TRANSLIT")
  value <- tolower(value)
  value <- gsub("[^a-z0-9]+", " ", value)
  trimws(value)
}

normalize_ccaa_name <- function(x) {
  lookup <- ced_ccaa_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("^\\d{1,2}\\s*", "", raw)
  raw <- gsub("\\*", "", raw)
  key <- normalize_key(raw)
  idx <- match(key, lookup$key)
  normalized <- lookup$ccaa[idx]
  normalized[is.na(normalized)] <- raw[is.na(normalized)]
  normalized
}

official_ccaa_levels <- function(include_ceuta_melilla = TRUE) {
  ced_official_ccaa_levels(
    include_state = FALSE,
    include_autonomous_cities = FALSE,
    include_ceuta_melilla_combined = include_ceuta_melilla
  )
}

# ===========================================================================
# Parsing numeros y fechas (locale espanol)
# ===========================================================================

parse_number_es <- function(x) {
  if (is.numeric(x)) {
    return(as.numeric(x))
  }

  value <- trimws(as.character(x))
  value[value %in% c("", "NA", "N/A", "n.d.", "-", "NULL")] <- NA_character_
  value <- gsub("\\.", "", value)
  value <- gsub(",", ".", value, fixed = TRUE)
  suppressWarnings(as.numeric(value))
}

periodo_from_name <- function(nm) {
  m <- stringr::str_match(nm, "(\\d{1,2})\\s*[/\\-]\\s*(\\d{4})")
  if (is.na(m[1, 1])) NA_character_ else sprintf("%s-%02d", m[3], as.integer(m[2]))
}

norm_txt <- function(x) {
  x |>
    as.character() |>
    enc2utf8() |>
    gsub("\\*", "", x = _) |>
    gsub("\u00AD|\u200B", "", x = _, useBytes = TRUE) |>
    stringi::stri_replace_all_regex("[\\u00A0\\u202F\\t]", " ") |>
    stringr::str_trim() |>
    stringr::str_replace_all("\\s+", " ")
}

# Mes (YYYY-MM-01) a partir de la fecha del nombre de fichero IMSERSO.
# estsisaad_20260930.xlsx -> 2026-09-01. Es la fecha autoritativa: la cabecera
# de los informes puede arrastrar la de un mes anterior (incidencia 2026-10).
fecha_mes_from_filename <- function(file_name) {
  m <- stringr::str_match(basename(file_name), "(20\\d{2})(\\d{2})(\\d{2})")
  out <- rep(as.Date(NA), length(file_name))
  ok <- !is.na(m[, 1])
  out[ok] <- as.Date(sprintf("%s-%s-01", m[ok, 2], m[ok, 3]))
  out
}

meses_es <- c(
  enero = 1, febrero = 2, marzo = 3, abril = 4, mayo = 5, junio = 6, julio = 7,
  agosto = 8, septiembre = 9, setiembre = 9, octubre = 10, noviembre = 11, diciembre = 12
)

# Primer "a DD de <mes> de YYYY" o "DD/MM/YYYY" de un texto -> YYYY-MM-01.
fecha_mes_from_text <- function(txt) {
  txt <- tolower(stringi::stri_trans_general(paste(txt[!is.na(txt)], collapse = " "), "Latin-ASCII"))
  m <- stringr::str_match(txt, "\\b\\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre) de (20\\d{2})")
  if (!is.na(m[1, 1])) {
    return(as.Date(sprintf("%s-%02d-01", m[1, 3], meses_es[[m[1, 2]]])))
  }
  m <- stringr::str_match(txt, "\\b\\d{1,2}/(\\d{1,2})/(20\\d{2})\\b")
  if (!is.na(m[1, 1])) {
    return(as.Date(sprintf("%s-%02d-01", m[1, 3], as.integer(m[1, 2]))))
  }
  as.Date(NA)
}

# ---------------------------------------------------------------------------
# Validacion de descargas (incidencia 2026-10)
# ---------------------------------------------------------------------------
# imserso.es devuelve una pagina HTML de ~35 KB (403) en lugar del fichero
# cuando la peticion no lleva cabeceras de navegador. Si esa pagina se guarda
# con extension .xlsx queda en cache para siempre y readxl falla en silencio
# (la hoja se lee como error y el mes desaparece). Antes de parsear se
# comprueba la firma binaria y un tamano minimo.

download_min_bytes <- 100 * 1024

validate_download <- function(path, min_bytes = download_min_bytes) {
  if (!file.exists(path)) return(list(ok = FALSE, motivo = "no existe"))
  size <- file.info(path)$size
  ext <- tolower(tools::file_ext(path))
  con <- file(path, "rb")
  magic <- readBin(con, "raw", n = 8)
  close(con)
  if (length(magic) < 4) return(list(ok = FALSE, motivo = "fichero vacio"))
  # Primer byte que no es espacio/BOM: '<' delata una pagina HTML
  primer <- magic[!magic %in% as.raw(c(0x20, 0x09, 0x0a, 0x0d, 0xef, 0xbb, 0xbf))][1]

  firma_ok <- switch(
    ext,
    xlsx = , xlsm = , docx = identical(magic[1:4], as.raw(c(0x50, 0x4b, 0x03, 0x04))),
    xls = , xlsb = identical(magic[1:4], as.raw(c(0xd0, 0xcf, 0x11, 0xe0))) ||
      identical(magic[1:4], as.raw(c(0x50, 0x4b, 0x03, 0x04))),
    pdf = identical(rawToChar(magic[1:4]), "%PDF"),
    FALSE
  )

  if (!is.na(primer) && primer == as.raw(0x3c)) {
    return(list(ok = FALSE, motivo = sprintf("es HTML (%d bytes), no %s", as.integer(size), ext)))
  }
  if (!firma_ok) {
    return(list(ok = FALSE, motivo = sprintf("firma binaria no corresponde a %s", ext)))
  }
  if (size < min_bytes) {
    return(list(ok = FALSE, motivo = sprintf("demasiado pequeno (%d bytes)", as.integer(size))))
  }
  list(ok = TRUE, motivo = "ok")
}

# ---------------------------------------------------------------------------
# Antiguedad del ultimo dato real (incidencia 2026-10)
# ---------------------------------------------------------------------------
# El IMSERSO publica con 6-8 semanas de retraso: el dia 5 de cada mes lo normal
# es tener el mes M-2. Mas de dos meses de distancia indica que la extraccion
# o la carga se han parado.

max_meses_sin_dato_real <- 2L

meses_de_antiguedad <- function(ultimo_mes, hoy = Sys.Date()) {
  ultimo_mes <- as.Date(ultimo_mes)
  hoy_mes <- as.Date(format(hoy, "%Y-%m-01"))
  (as.integer(format(hoy_mes, "%Y")) - as.integer(format(ultimo_mes, "%Y"))) * 12L +
    as.integer(format(hoy_mes, "%m")) - as.integer(format(ultimo_mes, "%m"))
}

# Emite un aviso (y anotacion de GitHub Actions) si el ultimo mes real es
# demasiado antiguo. Devuelve los meses de antiguedad de forma invisible.
check_freshness <- function(ultimo_mes, contexto, max_meses = max_meses_sin_dato_real) {
  if (length(ultimo_mes) == 0 || is.na(ultimo_mes)) {
    log_event("WARN", sprintf("%s: no hay ningun mes con dato real", contexto))
    return(invisible(NA_integer_))
  }
  meses <- meses_de_antiguedad(ultimo_mes)
  msg <- sprintf("%s: ultimo mes real %s (%d meses de antiguedad)",
                 contexto, format(as.Date(ultimo_mes), "%Y-%m"), meses)
  if (meses > max_meses) {
    log_event("WARN", paste0(msg, sprintf(" > %d: revisar extraccion o carga", max_meses)))
    if (nzchar(Sys.getenv("GITHUB_ACTIONS"))) {
      cat(sprintf("::warning title=Dependencia desactualizada::%s\n", msg))
    }
  } else {
    log_event("OK", msg)
  }
  invisible(meses)
}

first_numeric_in_row <- function(row_vec) {
  nums <- suppressWarnings(
    readr::parse_number(
      as.character(row_vec),
      locale = readr::locale(decimal_mark = ",", grouping_mark = ".")
    )
  )
  out <- nums[which(!is.na(nums))][1]
  if (length(out) == 0) NA_real_ else out
}

# ===========================================================================
# Extraccion de hojas por patron (reemplaza 4 copias de get_list)
# ===========================================================================

extract_sheet_by_pattern <- function(raw_data, pattern, year_pattern_fn = NULL) {
  out <- list()

  for (yr_name in names(raw_data)) {
    year_list <- raw_data[[yr_name]]
    if (is.null(year_list) || !length(year_list)) next

    pat <- if (!is.null(year_pattern_fn)) {
      year_pattern_fn(as.integer(yr_name))
    } else {
      pattern
    }

    for (mo_name in names(year_list)) {
      mo_list <- year_list[[mo_name]]
      if (is.null(mo_list) || !length(mo_list)) next

      found_tbl <- NULL
      for (file_obj in mo_list) {
        if (!is.list(file_obj) || is.null(names(file_obj))) next
        sheet_names <- names(file_obj)
        hit_idx <- which(grepl(pat, sheet_names, ignore.case = TRUE))
        if (length(hit_idx)) {
          found_tbl <- file_obj[[hit_idx[1]]]
          break
        }
      }

      if (!is.null(found_tbl)) {
        mm <- suppressWarnings(as.integer(mo_name))
        if (!is.na(mm) && mm >= 1 && mm <= 12) {
          label <- sprintf("%02d/%s", mm, yr_name)
          out[[label]] <- tibble::as_tibble(found_tbl, .name_repair = "unique")
        }
      }
    }
  }

  out
}

# ===========================================================================
# Conexion Supabase (compartida entre transformacion y carga)
# ===========================================================================

connect_supabase <- function(cfg) {
  db_cfg <- cfg$db
  missing <- c("host", "user", "password")[vapply(
    db_cfg[c("host", "user", "password")],
    function(x) identical(x, "") || is.na(x),
    logical(1)
  )]
  if (length(missing) > 0) {
    stop(
      sprintf("Faltan variables de entorno de Supabase: %s", paste(missing, collapse = ", ")),
      call. = FALSE
    )
  }

  DBI::dbConnect(
    RPostgres::Postgres(),
    host = db_cfg$host,
    port = db_cfg$port,
    dbname = db_cfg$name,
    user = db_cfg$user,
    password = db_cfg$password,
    sslmode = "require"
  )
}

# ===========================================================================
# Calidad de datos y cobertura
# ===========================================================================

merge_metric_tables <- function(tables, keys) {
  standardized <- purrr::map(
    tables,
    function(df) {
      missing_keys <- setdiff(keys, names(df))
      for (key in missing_keys) {
        df[[key]] <- NA
      }
      dplyr::select(df, dplyr::all_of(c(keys, setdiff(names(df), keys))))
    }
  )

  purrr::reduce(
    standardized,
    function(left, right) {
      dplyr::full_join(left, right, by = keys)
    }
  ) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(keys)))
}

log_series_coverage <- function(data, label) {
  period_col <- if ("fecha" %in% names(data)) "fecha" else if ("periodo" %in% names(data)) "periodo" else NULL
  if (is.null(period_col) || !"ccaa" %in% names(data)) {
    return(invisible(NULL))
  }

  periods <- sort(unique(stats::na.omit(as.character(data[[period_col]]))))
  ccaa_count <- dplyr::n_distinct(stats::na.omit(data$ccaa))

  if (length(periods) == 0) {
    log_event("WARN", sprintf("%s: sin periodos validos", label))
    return(invisible(NULL))
  }

  log_event(
    "INFO",
    sprintf(
      "%s: filas=%s | ccaa=%s | periodo=%s a %s",
      label,
      nrow(data),
      ccaa_count,
      min(periods),
      max(periods)
    )
  )
}

log_table_quality <- function(data, label, key_cols) {
  numeric_cols <- setdiff(names(data)[vapply(data, is.numeric, logical(1))], key_cols)
  if (length(numeric_cols) == 0) {
    log_event("INFO", sprintf("%s: sin metricas numericas para evaluar", label))
    return(invisible(NULL))
  }

  na_share <- vapply(
    numeric_cols,
    function(col) round(mean(is.na(data[[col]])) * 100, 1),
    numeric(1)
  )

  log_event(
    "INFO",
    sprintf(
      "%s: NA%% por metrica -> %s",
      label,
      paste(sprintf("%s=%s%%", names(na_share), na_share), collapse = " | ")
    )
  )
}

# ===========================================================================
# Prereqs y configuracion del pipeline
# ===========================================================================

required_rds_paths <- function(dir_path, names) {
  file.path(dir_path, paste0(names, ".rds"))
}

assert_step_prerequisites <- function(cfg) {
  requirements <- list(
    transformacion = list(
      needed = list(
        "solsaad", "perfsaad", "dictsaad", "benpresaad",
        "pendsaad", "tiempo_espera", "perfcuidador_ccaa"
      ),
      dir_path = cfg$extraction_dir,
      generated_by = "extraccion"
    ),
    modelado = list(
      needed = list(
        "dashboard_indicators",
        "solsaad_all", "benpresaad_all", "dictsaad_all"
      ),
      dir_path = cfg$transform_dir,
      generated_by = "transformacion"
    ),
    carga = list(
      needed = list(
        "dashboard_indicators",
        "solsaad_all", "benpresaad_all", "dictsaad_all",
        "perf_ccaa_genero"
      ),
      dir_path = cfg$model_dir,
      generated_by = "modelado"
    )
  )

  for (step in names(requirements)) {
    if (!(step %in% cfg$steps) || requirements[[step]]$generated_by %in% cfg$steps) {
      next
    }

    needed_groups <- lapply(requirements[[step]]$needed, function(x) required_rds_paths(requirements[[step]]$dir_path, x))
    missing <- needed_groups[!vapply(needed_groups, any_file_exists, logical(1))]
    if (length(missing) > 0) {
      stop(
        sprintf(
          "No se puede ejecutar '%s' sin '%s' o sin artefactos previos. Faltan: %s",
          step,
          requirements[[step]]$generated_by,
          paste(vapply(missing, function(x) paste(basename(x), collapse = " o "), character(1)), collapse = ", ")
        ),
        call. = FALSE
      )
    }
  }
}

dashboard_indicator_names <- function() {
  # Convencion: los indicadores relativizados a Poblacion Potencialmente
  # Dependiente terminan en *_pct_ppd y se almacenan ya como porcentaje (x100).
  # Los tres limbos se ordenan cronologicamente segun el flujo administrativo
  # del SAAD: grado -> PIA -> prestacion efectiva.
  c(
    "cobertura_pct_ppd",
    "solicitudes_pct_ppd",
    "pct_mujeres_benef",
    "limbo_grado_pct_ppd",
    "limbo_pia_pct_ppd",
    "limbo_prestaciones_pct_ppd",
    "tiempo_espera_total_dias",
    "pct_pecef",
    "pct_atencion_residencial",
    "ratio_prest_x_benef",
    "pct_grado3"
  )
}

build_pipeline_config <- function(base_path, cli_args = list()) {
  # Horizonte de proyeccion = ultimo mes observado + 6 meses.
  # Decision metodologica: con series mensuales cortas (~36 meses observados
  # desde 2023) y modelos univariantes ETS/ARIMA, las proyecciones a 12+ meses
  # tienden a una linealizacion poco informativa. Limitar a 6 meses produce
  # proyecciones mas defendibles y comunica honestamente el alcance temporal.
  forecast_default <- format(
    as.Date(format(Sys.Date(), "%Y-%m-01")) +
      as.difftime(184, units = "days"),
    "%Y-%m-01"
  )

  config <- list(
    base_path = normalizePath(base_path, winslash = "/", mustWork = TRUE),
    extraction_dir = file.path(base_path, "1_extraccion"),
    transform_dir  = file.path(base_path, "2_transformacion"),
    model_dir      = file.path(base_path, "3_modelado"),
    load_dir       = file.path(base_path, "4_carga"),
    legacy_dir     = file.path(base_path, "_legacy"),
    xls_dir        = file.path(base_path, "1_extraccion", "imserso_xls_multi"),
    pipeline_start_year = 2023L,
    saad_years     = 2023L:as.integer(format(Sys.Date(), "%Y")),
    base_url       = "https://imserso.es",
    ppd_schema     = "general",
    ppd_table      = "censo_ppd",
    dashboard_indicators = dashboard_indicator_names(),
    vars_to_model  = dashboard_indicator_names(),
    forecast_horizon_months = 6L,
    cv_folds       = 3L,
    min_points_cv  = 12L,
    include_prophet = parse_bool(cli_value(cli_args, c("include-prophet", "include_prophet"), FALSE)),
    steps = normalize_steps(
      cli_value(cli_args, c("steps"), "extraccion,transformacion,modelado,carga")
    ),
    with_db  = parse_bool(cli_value(cli_args, c("with-db", "with_db"), FALSE)),
    # Destino de la carga con --with-db=true (incidencia 2026-10):
    #   staging    -> copia de las tablas publicadas en el esquema ced_staging,
    #                 con el mismo upsert que produccion, para revisar antes.
    #   produccion -> upsert directo sobre las tablas que consume la web.
    # Por defecto staging: escribir en produccion tiene que pedirse.
    db_target = match.arg(
      tolower(cli_value(cli_args, c("db-target", "db_target"), "staging")),
      c("staging", "produccion")
    ),
    # Tablas intermedias (solsaad_all, benpresaad_all...) al esquema de
    # trabajo 'saad'. Se reemplazan enteras (DROP + RENAME), por eso son
    # opcionales y nunca se escriben en modo staging.
    aux_tables = parse_bool(cli_value(cli_args, c("aux-tables", "aux_tables"), TRUE)),
    force_download = parse_bool(cli_value(cli_args, c("force-download", "force_download"), FALSE)),
    forecast_horizon_end = as.Date(
      cli_value(cli_args, c("horizon-end", "horizon_end"), forecast_default)
    ),
    db = list(
      host     = Sys.getenv("SUPABASE_HOST", ""),
      port     = as.integer(Sys.getenv("SUPABASE_PORT", "5432")),
      name     = Sys.getenv("SUPABASE_DBNAME", "postgres"),
      user     = Sys.getenv("SUPABASE_USER", ""),
      password = Sys.getenv("SUPABASE_PASS", ""),
      schema   = Sys.getenv("SUPABASE_SCHEMA", "saad"),
      # Las tablas hub que lee la web (ced_dependencia_global/_gen) viven en la
      # capa de publicacion 'canendatos', no en la de trabajo 'saad'. Antes se
      # escribian todas en 'saad', donde la web no las lee (incidencia 2026-10).
      publish_schema = Sys.getenv("SUPABASE_PUBLISH_SCHEMA", "canendatos"),
      staging_schema = "ced_staging"
    )
  )

  if (!is.null(cli_args[["with-ppd"]]) || !is.null(cli_args[["with_ppd"]])) {
    log_event(
      "WARN",
      "--with-ppd es obsoleto: la PPD es obligatoria con fallback XLS desde la v2 del cuaderno"
    )
  }

  ensure_dir(config$extraction_dir)
  ensure_dir(config$transform_dir)
  ensure_dir(config$model_dir)
  ensure_dir(config$load_dir)
  ensure_dir(config$legacy_dir)
  ensure_dir(config$xls_dir)
  assert_step_prerequisites(config)

  config
}
