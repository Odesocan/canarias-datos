# ============================================================
# R/pipeline_utils.R — Utilidades comunes del pipeline Presupuestos.
# Alineado con Vivienda / Salud mental / Dependencia.
# ============================================================

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0) return(y)
  if (is.character(x) && identical(trimws(x), "")) return(y)
  x
}

require_packages <- function(packages) {
  missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly = TRUE)]
  if (length(missing) > 0) {
    stop(sprintf("Faltan paquetes de R requeridos: %s", paste(missing, collapse = ", ")), call. = FALSE)
  }
  invisible(packages)
}

log_event <- function(level, message) {
  timestamp <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
  cat(sprintf("[%s] [%-7s] %s\n", timestamp, level, message))
}

parse_bool <- function(x, default = FALSE) {
  if (is.null(x) || length(x) == 0) return(default)
  value <- tolower(trimws(as.character(x[[1]])))
  if (value %in% c("true", "1", "yes", "y", "si", "sí")) return(TRUE)
  if (value %in% c("false", "0", "no", "n")) return(FALSE)
  default
}

parse_cli_args <- function(args) {
  parsed <- list()
  index <- 1L
  while (index <= length(args)) {
    arg <- args[[index]]
    if (!startsWith(arg, "--")) { index <- index + 1L; next }
    item <- sub("^--", "", arg)
    if (grepl("=", item, fixed = TRUE)) {
      parts <- strsplit(item, "=", fixed = TRUE)[[1]]
      key <- parts[[1]]; value <- paste(parts[-1], collapse = "=")
    } else if (index < length(args) && !startsWith(args[[index + 1L]], "--")) {
      key <- item; value <- args[[index + 1L]]; index <- index + 1L
    } else {
      key <- item; value <- "true"
    }
    parsed[[key]] <- value
    index <- index + 1L
  }
  parsed
}

cli_value <- function(args, keys, default = NULL) {
  for (key in keys) if (!is.null(args[[key]])) return(args[[key]])
  default
}

normalize_steps <- function(value) {
  allowed <- c("extraccion", "transformacion", "modelado", "carga")
  items <- strsplit(value %||% paste(allowed, collapse = ","), ",", fixed = TRUE)[[1]]
  items <- tolower(trimws(items)); items <- items[nzchar(items)]
  invalid <- setdiff(items, allowed)
  if (length(invalid) > 0) stop(sprintf("Pasos no soportados: %s", paste(invalid, collapse = ", ")), call. = FALSE)
  items <- unique(items)
  canonical_subset <- allowed[allowed %in% items]
  if (!identical(items, canonical_subset)) {
    stop(sprintf("Los pasos deben seguir el orden canónico: %s", paste(allowed, collapse = " -> ")), call. = FALSE)
  }
  items
}

ensure_dir <- function(path) {
  dir.create(path, recursive = TRUE, showWarnings = FALSE)
  invisible(path)
}

assert_file_exists <- function(path, label = NULL) {
  if (!file.exists(path)) stop(sprintf("Falta %s: %s", label %||% "archivo", path), call. = FALSE)
}

assert_required_columns <- function(data, required, label = deparse(substitute(data))) {
  missing <- setdiff(required, names(data))
  if (length(missing) > 0) {
    stop(sprintf("%s no contiene columnas requeridas: %s", label, paste(missing, collapse = ", ")), call. = FALSE)
  }
}

assert_unique_keys <- function(data, keys, label = deparse(substitute(data))) {
  if (nrow(data) == 0) return(invisible(NULL))
  dup <- dplyr::count(data, dplyr::across(dplyr::all_of(keys)), name = "n") |>
    dplyr::filter(.data$n > 1)
  if (nrow(dup) > 0) {
    stop(sprintf("%s contiene claves duplicadas para: %s", label, paste(keys, collapse = ", ")), call. = FALSE)
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
    purrr::map(function(name) readRDS(file.path(dir_path, paste0(name, ".rds"))))
}

# ----------------------------------------------------------------------------
# CCAA — delega en R/ccaa_dictionary.R
# ----------------------------------------------------------------------------

normalize_ccaa_name <- function(x) {
  if (!exists("ced_ccaa_lookup_table")) {
    stop("ced_ccaa_lookup_table no está cargado.", call. = FALSE)
  }
  lookup <- ced_ccaa_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("\\s*\\([^)]*\\)$", "", raw)
  key <- ced_normalize_text_key(raw)
  normalized <- lookup$ccaa[match(key, lookup$key)]
  normalized[is.na(normalized)] <- raw[is.na(normalized)]
  normalized
}

official_ccaa_levels <- function(include_national = FALSE, include_autonomous_cities = FALSE) {
  ced_official_ccaa_levels(include_state = isTRUE(include_national),
                           include_autonomous_cities = isTRUE(include_autonomous_cities))
}

# ----------------------------------------------------------------------------
# Importes: número en formato es-ES (1.234,56) → numérico.
# Tolerante con formato anglosajón sencillo (1234.56) si no hay miles.
# ----------------------------------------------------------------------------

parse_number_es <- function(x) {
  if (is.numeric(x)) return(as.numeric(x))
  value <- trimws(as.character(x))
  value[value %in% c("", "NA", "N/A", "n.d.", "-", "NULL")] <- NA_character_
  has_comma <- grepl(",", value, fixed = TRUE)
  out <- value
  out[has_comma] <- gsub("\\.", "", out[has_comma])
  out[has_comma] <- gsub(",", ".", out[has_comma], fixed = TRUE)
  suppressWarnings(as.numeric(out))
}

parse_eur <- parse_number_es  # alias retro-compatible con la antigua API

# ----------------------------------------------------------------------------
# Hashing
# ----------------------------------------------------------------------------

sha256_file <- function(path) {
  digest::digest(path, algo = "sha256", file = TRUE)
}

# ----------------------------------------------------------------------------
# Validaciones de calidad: conciliación, outliers (z-score), Benford
# ----------------------------------------------------------------------------

conciliar_total <- function(df, total_externo, tol = 0.005, group_cols = NULL) {
  if (is.null(group_cols)) {
    s <- sum(df$importe_eur, na.rm = TRUE)
    if (!is.finite(total_externo) || total_externo == 0) {
      return(list(ok = NA, suma = s, total = total_externo, dif_rel = NA_real_))
    }
    dif <- abs(s - total_externo) / total_externo
    return(list(ok = dif <= tol, suma = s, total = total_externo, dif_rel = dif))
  }
  df |>
    dplyr::group_by(dplyr::across(dplyr::all_of(group_cols))) |>
    dplyr::summarise(suma = sum(.data$importe_eur, na.rm = TRUE), .groups = "drop")
}

detectar_outliers <- function(df, z_thr = 3) {
  df |>
    dplyr::group_by(.data$ccaa, .data$concepto) |>
    dplyr::mutate(
      n = dplyr::n(),
      media = mean(.data$importe_eur, na.rm = TRUE),
      desv = stats::sd(.data$importe_eur, na.rm = TRUE),
      z = ifelse(.data$n >= 3 & !is.na(.data$desv) & .data$desv > 0,
                 abs(.data$importe_eur - .data$media) / .data$desv, NA_real_),
      es_outlier = !is.na(.data$z) & .data$z > z_thr
    ) |>
    dplyr::ungroup() |>
    dplyr::select(-"n", -"media", -"desv")
}

chequeo_benford <- function(importes) {
  importes <- importes[is.finite(importes) & importes > 0]
  if (length(importes) < 30) {
    return(list(chi = NA_real_, p_value = NA_real_, ok = NA, n = length(importes)))
  }
  d <- as.integer(substr(formatC(importes, format = "f", digits = 0, big.mark = ""), 1, 1))
  d <- d[d %in% 1:9]
  observado <- as.integer(table(factor(d, levels = 1:9)))
  esperado <- log10(1 + 1 / (1:9)) * length(d)
  chi <- sum((observado - esperado)^2 / esperado)
  pval <- stats::pchisq(chi, df = 8, lower.tail = FALSE)
  list(chi = chi, p_value = pval, ok = pval > 0.01, n = length(d))
}

# ----------------------------------------------------------------------------
# Cobertura y calidad — copiados del patrón Vivienda/Salud mental
# ----------------------------------------------------------------------------

log_series_coverage <- function(data, label) {
  if (!all(c("ccaa", "periodo") %in% names(data))) return(invisible(NULL))
  periods <- sort(unique(stats::na.omit(as.integer(data$periodo))))
  ccaa_count <- dplyr::n_distinct(stats::na.omit(data$ccaa))
  if (length(periods) == 0) { log_event("WARN", sprintf("%s: sin periodos válidos", label)); return(invisible(NULL)) }
  log_event("INFO", sprintf("%s: filas=%s | ccaa=%s | periodo=%s-%s",
                            label, nrow(data), ccaa_count, min(periods), max(periods)))
  recent_years <- tail(periods, min(2, length(periods)))
  expected <- official_ccaa_levels()
  for (year in recent_years) {
    year_ccaa <- sort(unique(data$ccaa[data$periodo == year & data$ccaa %in% expected]))
    missing <- setdiff(expected, year_ccaa)
    if (length(missing) > 0) {
      log_event("WARN", sprintf("%s: faltan CCAA en %s: %s", label, year, paste(missing, collapse = ", ")))
    } else {
      log_event("INFO", sprintf("%s: cobertura completa en %s", label, year))
    }
  }
}

log_table_quality <- function(data, label, key_cols) {
  numeric_cols <- setdiff(names(data)[vapply(data, is.numeric, logical(1))], key_cols)
  if (length(numeric_cols) == 0) {
    log_event("INFO", sprintf("%s: sin métricas numéricas para evaluar", label)); return(invisible(NULL))
  }
  na_share <- vapply(numeric_cols, function(col) round(mean(is.na(data[[col]])) * 100, 1), numeric(1))
  log_event("INFO", sprintf("%s: NA%% por métrica -> %s",
                            label, paste(sprintf("%s=%s%%", names(na_share), na_share), collapse = " | ")))
}

# ----------------------------------------------------------------------------
# Merge multi-tabla
# ----------------------------------------------------------------------------

merge_metric_tables <- function(tables, keys) {
  standardized <- purrr::map(tables, function(df) {
    missing_keys <- setdiff(keys, names(df))
    for (key in missing_keys) df[[key]] <- NA
    dplyr::select(df, dplyr::all_of(c(keys, setdiff(names(df), keys))))
  })
  purrr::reduce(standardized, function(left, right) dplyr::full_join(left, right, by = keys)) |>
    dplyr::arrange(dplyr::across(dplyr::all_of(keys)))
}

# ----------------------------------------------------------------------------
# Prerrequisitos entre fases
# ----------------------------------------------------------------------------

required_rds_paths <- function(dir_path, names) {
  file.path(dir_path, paste0(names, ".rds"))
}

assert_step_prerequisites <- function(cfg) {
  raw_extracted <- c("manifest", "staging_gasto")

  requirements <- list(
    transformacion = list(
      needed = raw_extracted,
      dir_path = cfg$extraction_dir,
      generated_by = "extraccion"
    ),
    modelado = list(
      needed = c("gasto_normalizado"),
      dir_path = cfg$transform_dir,
      generated_by = "transformacion"
    ),
    carga = list(
      needed = c("ced_presupuestos"),
      dir_path = cfg$model_dir,
      generated_by = "modelado"
    )
  )

  for (step in names(requirements)) {
    if (!(step %in% cfg$steps) || requirements[[step]]$generated_by %in% cfg$steps) next
    needed_paths <- required_rds_paths(requirements[[step]]$dir_path, requirements[[step]]$needed)
    missing <- needed_paths[!file.exists(needed_paths)]
    if (length(missing) > 0) {
      stop(sprintf("No se puede ejecutar '%s' sin '%s' o sin artefactos previos. Faltan: %s",
                   step, requirements[[step]]$generated_by, paste(basename(missing), collapse = ", ")),
           call. = FALSE)
    }
  }
}

# ----------------------------------------------------------------------------
# Lectura de externos (PIB nacional, población CCAA × año)
# ----------------------------------------------------------------------------

load_externos <- function(cfg) {
  pib_path <- file.path(cfg$externos_dir, "pib_nacional.csv")
  pob_path <- file.path(cfg$externos_dir, "poblacion_ccaa.csv")

  pib <- if (file.exists(pib_path)) {
    df <- utils::read.csv(pib_path, stringsAsFactors = FALSE)
    df$anio <- as.integer(df$anio); df$pib_nominal_eur <- as.numeric(df$pib_nominal_eur)
    df
  } else {
    log_event("WARN", sprintf("Falta %s — pct_pib_nacional será NA", basename(pib_path)))
    data.frame(anio = integer(0), pib_nominal_eur = numeric(0))
  }

  pob <- if (file.exists(pob_path)) {
    df <- utils::read.csv(pob_path, stringsAsFactors = FALSE)
    df$anio <- as.integer(df$anio); df$poblacion <- as.numeric(df$poblacion)
    df$ccaa <- normalize_ccaa_name(df$ccaa)
    df
  } else {
    log_event("WARN", sprintf("Falta %s — eur_per_capita será NA", basename(pob_path)))
    data.frame(ccaa = character(0), anio = integer(0), poblacion = numeric(0))
  }

  # PIB REGIONAL por CCAA (INE Contabilidad Regional, op. 30679). Denominador
  # del indicador comparable pct_pib_regional. Serie real 2015-2024; los años
  # posteriores se completan por bootstrap en el modelado (ver modelado.R).
  pibreg_path <- file.path(cfg$externos_dir, "pib_regional_ccaa.csv")
  pib_regional <- if (file.exists(pibreg_path)) {
    df <- utils::read.csv(pibreg_path, stringsAsFactors = FALSE)
    df$anio <- as.integer(df$anio)
    df$pib_regional_eur <- as.numeric(df$pib_regional_eur)
    df[c("ccaa_id3", "anio", "pib_regional_eur")]
  } else {
    log_event("WARN", sprintf("Falta %s — pct_pib_regional será NA", basename(pibreg_path)))
    data.frame(ccaa_id3 = character(0), anio = integer(0),
               pib_regional_eur = numeric(0))
  }

  list(pib = pib, poblacion = pob, pib_regional = pib_regional)
}

# ----------------------------------------------------------------------------
# Configuración del pipeline
# ----------------------------------------------------------------------------

build_pipeline_config <- function(base_path, cli_args = list()) {
  config <- list(
    base_path       = normalizePath(base_path, winslash = "/", mustWork = TRUE),
    extraction_dir  = file.path(base_path, "1_extraccion"),
    transform_dir   = file.path(base_path, "2_transformacion"),
    model_dir       = file.path(base_path, "3_modelado"),
    load_dir        = file.path(base_path, "4_carga"),
    fuentes_dir     = file.path(base_path, "fuentes"),
    raw_dir         = file.path(base_path, "fuentes", "raw"),
    externos_dir    = file.path(base_path, "fuentes", "externos"),
    logs_dir        = file.path(base_path, "logs"),
    fuentes_yml     = file.path(base_path, "fuentes.yml"),
    correspondencias_yml = file.path(base_path, "correspondencias.yml"),
    extract_pdf_py  = file.path(base_path, "1_extraccion", "extract_pdf.py"),
    python_bin      = Sys.getenv("CED_PYTHON_BIN", "python3"),
    steps           = normalize_steps(cli_value(cli_args, c("steps"),
                          paste(c("extraccion","transformacion","modelado","carga"), collapse=","))),
    with_db         = parse_bool(cli_value(cli_args, c("with-db","with_db"),
                          Sys.getenv("CED_WITH_DB", "false"))),
    run_scraping    = parse_bool(cli_value(cli_args, c("run-scraping","run_scraping"), FALSE)),
    dry_run         = parse_bool(cli_value(cli_args, c("dry-run","dry_run"), FALSE)),
    ccaa_filter     = cli_value(cli_args, c("ccaa"), NULL),
    year_filter     = {
      raw <- cli_value(cli_args, c("year","anio"), NULL)
      if (is.null(raw)) NULL else as.integer(raw)
    },
    horizon_year    = as.integer(cli_value(cli_args, c("horizon-year","horizon_year"),
                          Sys.getenv("CED_HORIZON_YEAR", "2026"))),
    fuzzy_threshold = as.numeric(cli_value(cli_args, c("fuzzy-threshold"),
                          Sys.getenv("CED_FUZZY_THRESHOLD", "0.92"))),
    enable_projection = parse_bool(cli_value(cli_args, c("enable-projection","enable_projection"),
                          Sys.getenv("CED_ENABLE_PROJECTION", "false"))),
    # Bootstrap del PIB regional (completa los años sin dato del INE, p.ej.
    # 2025-2026). Es un relleno del denominador, NO depende de enable_projection.
    pib_boot_n    = as.integer(cli_value(cli_args, c("pib-boot-n","pib_boot_n"),
                          Sys.getenv("CED_PIB_BOOT_N", "5000"))),
    pib_boot_seed = as.integer(cli_value(cli_args, c("pib-boot-seed","pib_boot_seed"),
                          Sys.getenv("CED_PIB_BOOT_SEED", "20260716"))),
    db = list(
      host = Sys.getenv("SUPABASE_HOST", ""),
      port = as.integer(Sys.getenv("SUPABASE_PORT", "5432")),
      name = Sys.getenv("SUPABASE_DBNAME", "postgres"),
      user = Sys.getenv("SUPABASE_USER", ""),
      password = Sys.getenv("SUPABASE_PASS", ""),
      schema = Sys.getenv("SUPABASE_SCHEMA", "canendatos"),
      api_url = sub("/$", "", Sys.getenv("SUPABASE_URL", "")),
      api_key = trimws(Sys.getenv("SUPABASE_SERVICE_KEY", ""))
    )
  )

  ensure_dir(config$extraction_dir)
  ensure_dir(config$transform_dir)
  ensure_dir(config$model_dir)
  ensure_dir(config$load_dir)
  ensure_dir(config$raw_dir)
  ensure_dir(config$externos_dir)
  ensure_dir(config$logs_dir)
  assert_step_prerequisites(config)

  config
}
