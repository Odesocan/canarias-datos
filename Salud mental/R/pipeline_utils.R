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
        "Los pasos deben seguir el orden canónico: %s",
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

normalize_key <- function(x) {
  value <- trimws(as.character(x))
  value <- chartr(
    "áéíóúüñÁÉÍÓÚÜÑ",
    "aeiouunAEIOUUN",
    value
  )
  value <- tolower(value)
  value <- gsub("[^a-z0-9]+", " ", value)
  trimws(value)
}

# ----------------------------------------------------------------------------
# Normalización CCAA — delega al diccionario en R/ccaa_dictionary.R
# ----------------------------------------------------------------------------

normalize_ccaa_name <- function(x) {
  if (!exists("ced_ccaa_lookup_table")) {
    stop("ced_ccaa_lookup_table no está cargado. Asegúrate de hacer source() de R/ccaa_dictionary.R", call. = FALSE)
  }
  lookup <- ced_ccaa_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("\\s*\\([^)]*\\)$", "", raw)
  key <- ced_normalize_text_key(raw)
  normalized <- lookup$ccaa[match(key, lookup$key)]
  normalized[is.na(normalized)] <- raw[is.na(normalized)]
  normalized
}

official_ccaa_levels <- function(include_national = FALSE) {
  if (!exists("ced_official_ccaa_levels")) {
    stop("ced_official_ccaa_levels no está cargado. Asegúrate de hacer source() de R/ccaa_dictionary.R", call. = FALSE)
  }
  ced_official_ccaa_levels(
    include_state = isTRUE(include_national),
    include_autonomous_cities = FALSE
  )
}

# ----------------------------------------------------------------------------
# API INCLASNS (Ministerio de Sanidad) — Indicadores Clave del SNS
# ----------------------------------------------------------------------------

sns_api_base <- function() {
  Sys.getenv("SNS_API_BASE", "https://inclasns.sanidad.gob.es")
}

sns_api_token <- function() {
  token <- Sys.getenv("SNS_API_TOKEN", "")
  if (!nzchar(token)) {
    stop("Falta variable de entorno SNS_API_TOKEN. Revisa .Renviron.", call. = FALSE)
  }
  token
}

#' Descarga datos de un indicador del API INCLASNS
#'
#' Llama a /api/v2/datos?indicador=CODE&ccaa=&anio=&API_KEY=TOKEN.
#' Si `sexo` es NULL, NO se pasa el parámetro (la API devuelve el agregado Total).
#' Si `sexo` es "hombres" o "mujeres" se pasa explícito y devuelve esa categoría.
#'
#' Importante: pasar `sexo=""` (vacío) hace que la API devuelva NaN en todos los
#' valores. No usar nunca esa forma.
#'
#' Devuelve un data.frame plano con columnas:
#'   indicador_codigo, indicador_nombre, ccaa_raw, anio, sexo, valor
sns_get_indicador <- function(codigo, sexo = NULL, retries = 3L, timeout_secs = 60L) {
  require_packages(c("httr", "jsonlite"))
  url <- sprintf("%s/api/v2/datos", sns_api_base())
  query <- list(
    indicador = codigo,
    ccaa = "",
    anio = "",
    API_KEY = sns_api_token()
  )
  if (!is.null(sexo) && nzchar(sexo)) {
    query$sexo <- sexo
  }

  attempt <- 1L
  repeat {
    resp <- tryCatch(
      httr::GET(url, query = query, httr::timeout(timeout_secs)),
      error = function(e) e
    )

    if (!inherits(resp, "error") && httr::status_code(resp) == 200) {
      raw_text <- httr::content(resp, as = "text", encoding = "UTF-8")
      parsed <- tryCatch(jsonlite::fromJSON(raw_text, simplifyVector = FALSE), error = function(e) e)
      if (!inherits(parsed, "error") && length(parsed) > 0) {
        block <- parsed[[1]]
        # Mensajes de error de la API vienen como string envuelto en JSON
        if (is.character(block) || is.character(parsed[[1]])) {
          stop(sprintf("INCLASNS API error (indicador=%s, sexo=%s): %s",
                       codigo, sexo %||% "(none)", as.character(parsed[[1]])),
               call. = FALSE)
        }
        rows <- block$datos %||% list()
        if (length(rows) == 0) {
          return(
            data.frame(
              indicador_codigo = character(0),
              indicador_nombre = character(0),
              ccaa_raw = character(0),
              anio = integer(0),
              sexo = character(0),
              valor = numeric(0),
              stringsAsFactors = FALSE
            )
          )
        }
        df <- do.call(rbind, lapply(rows, function(r) {
          val <- r$valor
          if (is.character(val) && tolower(val) %in% c("nan", "")) val <- NA_real_
          data.frame(
            indicador_codigo = as.character(block$codigo),
            indicador_nombre = as.character(block$nombre),
            ccaa_raw = as.character(r$ccaa %||% NA_character_),
            anio = suppressWarnings(as.integer(r$anio %||% NA)),
            sexo = as.character(r$sexo %||% NA_character_),
            valor = suppressWarnings(as.numeric(val)),
            stringsAsFactors = FALSE
          )
        }))
        return(df)
      }
    }

    if (attempt >= retries) {
      msg <- if (inherits(resp, "error")) {
        conditionMessage(resp)
      } else {
        sprintf("HTTP %s", httr::status_code(resp))
      }
      stop(sprintf("INCLASNS indicador=%s: fallo tras %s intentos (%s)", codigo, retries, msg), call. = FALSE)
    }
    attempt <- attempt + 1L
    Sys.sleep(2 * attempt)
  }
}

# ----------------------------------------------------------------------------
# Censo INE 56940 — trimestral × edad × género → anual × CCAA
# ----------------------------------------------------------------------------

#' Calcula el censo anual por CCAA × género a partir del raw INE 56940.
#'
#' Lógica:
#'  - Filtra la dimensión "Edad" a "Todas las edades" (suma ya hecha por INE).
#'    Si esa categoría no existe, suma todas las edades disponibles.
#'  - Promedia los valores trimestrales del año (4 puntos por año en general).
#'  - Mantiene Total / Hombres / Mujeres (renombrado a "genero").
#'
#' Devuelve un data.frame con columnas: ccaa, periodo, genero, censo
compute_annual_census <- function(raw_censo) {
  require_packages(c("dplyr", "stringr", "tidyr"))
  data <- raw_censo

  if (!"Nombre" %in% names(data)) {
    stop("compute_annual_census requiere columna 'Nombre' (dataset INE 56940).", call. = FALSE)
  }
  if (!"Anyo" %in% names(data) || !"Valor" %in% names(data)) {
    stop("compute_annual_census requiere columnas 'Anyo' y 'Valor'.", call. = FALSE)
  }

  # En INE 56940 la columna Nombre tiene dos órdenes posibles:
  #   "Total Nacional. Edad. Género. Población. Número."
  #   "Género. Edad. CCAA. Población. Número."
  # Detectamos cuál es cuál mirando si el primer componente es un género.
  gender_tokens <- c("total", "hombres", "mujeres", "ambos sexos")

  parts_split <- stringr::str_split(data$Nombre, "\\s*\\.\\s*")
  first  <- vapply(parts_split, function(p) if (length(p) >= 1) p[[1]] else NA_character_, character(1))
  second <- vapply(parts_split, function(p) if (length(p) >= 2) p[[2]] else NA_character_, character(1))
  third  <- vapply(parts_split, function(p) if (length(p) >= 3) p[[3]] else NA_character_, character(1))

  first_is_gender <- tolower(trimws(first)) %in% gender_tokens

  ccaa_raw <- ifelse(first_is_gender, third, first)
  edad_raw <- second
  sexo_raw <- ifelse(first_is_gender, first, third)

  parsed <- data |>
    dplyr::mutate(
      ccaa_raw = .env$ccaa_raw,
      edad_raw = .env$edad_raw,
      sexo_raw = .env$sexo_raw,
      periodo = suppressWarnings(as.integer(.data$Anyo)),
      valor = suppressWarnings(as.numeric(.data$Valor))
    ) |>
    dplyr::filter(!is.na(.data$periodo), !is.na(.data$valor)) |>
    dplyr::mutate(
      ccaa = normalize_ccaa_name(.data$ccaa_raw),
      genero_norm = dplyr::case_when(
        tolower(trimws(.data$sexo_raw)) %in% c("total", "ambos sexos") ~ "total",
        tolower(trimws(.data$sexo_raw)) %in% c("hombres", "hombre", "varones") ~ "hombres",
        tolower(trimws(.data$sexo_raw)) %in% c("mujeres", "mujer") ~ "mujeres",
        TRUE ~ NA_character_
      )
    ) |>
    dplyr::filter(
      !is.na(.data$genero_norm),
      .data$ccaa %in% official_ccaa_levels(include_national = TRUE)
    )

  has_total_edad <- any(tolower(trimws(parsed$edad_raw)) == "todas las edades", na.rm = TRUE)

  if (has_total_edad) {
    parsed <- dplyr::filter(parsed, tolower(trimws(.data$edad_raw)) == "todas las edades")
  } else {
    parsed <- parsed |>
      dplyr::group_by(.data$ccaa, .data$periodo, .data$genero_norm, .data$Fecha) |>
      dplyr::summarise(valor = sum(.data$valor, na.rm = TRUE), .groups = "drop")
  }

  parsed |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$genero_norm) |>
    dplyr::summarise(censo = mean(.data$valor, na.rm = TRUE), .groups = "drop") |>
    dplyr::rename(genero = "genero_norm") |>
    dplyr::mutate(censo = round(.data$censo, 0))
}

# ----------------------------------------------------------------------------
# Validación de datasets raw
# ----------------------------------------------------------------------------

raw_validation_specs <- function() {
  list(
    sns_t_mental = list(
      label = "INCLASNS 1365 — trastornos mentales",
      required_cols = c("indicador_codigo", "indicador_nombre", "ccaa_raw", "anio", "sexo", "valor"),
      min_rows = 50
    ),
    sns_antidep = list(
      label = "INCLASNS 5930 — DHD antidepresivos",
      required_cols = c("indicador_codigo", "indicador_nombre", "ccaa_raw", "anio", "sexo", "valor"),
      min_rows = 50
    ),
    sns_hipno = list(
      label = "INCLASNS 5920 — DHD hipnosedantes",
      required_cols = c("indicador_codigo", "indicador_nombre", "ccaa_raw", "anio", "sexo", "valor"),
      min_rows = 50
    ),
    suicidios = list(
      label = "INE 46688 — suicidios",
      required_cols = c("Nombre", "NombrePeriodo", "Valor"),
      min_rows = 50
    ),
    censo = list(
      label = "INE 56940 — censo trimestral",
      required_cols = c("Nombre", "Anyo", "Valor"),
      min_rows = 100
    )
  )
}

validate_raw_dataset <- function(name, data) {
  specs <- raw_validation_specs()
  spec <- specs[[name]]
  if (is.null(spec)) {
    return(invisible(NULL))
  }

  assert_required_columns(data, spec$required_cols, spec$label)

  if (!is.null(spec$min_rows) && nrow(data) < spec$min_rows) {
    stop(
      sprintf("%s tiene solo %s filas (mínimo esperado: %s)", spec$label, nrow(data), spec$min_rows),
      call. = FALSE
    )
  }

  log_event("INFO", sprintf("Raw %s ok: %s filas", spec$label, nrow(data)))
}

# ----------------------------------------------------------------------------
# Merge / cobertura / calidad
# ----------------------------------------------------------------------------

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
  if (!all(c("ccaa", "periodo") %in% names(data))) {
    return(invisible(NULL))
  }

  periods <- sort(unique(stats::na.omit(as.integer(data$periodo))))
  ccaa_count <- dplyr::n_distinct(stats::na.omit(data$ccaa))

  if (length(periods) == 0) {
    log_event("WARN", sprintf("%s: sin periodos válidos", label))
    return(invisible(NULL))
  }

  log_event(
    "INFO",
    sprintf(
      "%s: filas=%s | ccaa=%s | periodo=%s-%s",
      label,
      nrow(data),
      ccaa_count,
      min(periods),
      max(periods)
    )
  )

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
    log_event("INFO", sprintf("%s: sin métricas numéricas para evaluar", label))
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
      "%s: NA%% por métrica -> %s",
      label,
      paste(sprintf("%s=%s%%", names(na_share), na_share), collapse = " | ")
    )
  )
}

required_rds_paths <- function(dir_path, names) {
  file.path(dir_path, paste0(names, ".rds"))
}

assert_step_prerequisites <- function(cfg) {
  raw_extracted <- c("sns_t_mental", "sns_antidep", "sns_hipno", "suicidios", "censo")

  requirements <- list(
    transformacion = list(
      needed = raw_extracted,
      dir_path = cfg$extraction_dir,
      generated_by = "extraccion"
    ),
    modelado = list(
      needed = c("ced_saludmental"),
      dir_path = cfg$transform_dir,
      generated_by = "transformacion"
    ),
    carga = list(
      needed = c("ced_saludmental"),
      dir_path = cfg$model_dir,
      generated_by = "modelado"
    )
  )

  for (step in names(requirements)) {
    if (!(step %in% cfg$steps) || requirements[[step]]$generated_by %in% cfg$steps) {
      next
    }

    needed_paths <- required_rds_paths(requirements[[step]]$dir_path, requirements[[step]]$needed)
    missing <- needed_paths[!file.exists(needed_paths)]
    if (length(missing) > 0) {
      stop(
        sprintf(
          "No se puede ejecutar '%s' sin '%s' o sin artefactos previos. Faltan: %s",
          step,
          requirements[[step]]$generated_by,
          paste(basename(missing), collapse = ", ")
        ),
        call. = FALSE
      )
    }
  }
}

build_pipeline_config <- function(base_path, cli_args = list()) {
  load_dir <- file.path(base_path, "4_carga")
  fuentes_dir <- file.path(base_path, "fuentes")

  config <- list(
    base_path = normalizePath(base_path, winslash = "/", mustWork = TRUE),
    extraction_dir = file.path(base_path, "1_extraccion"),
    transform_dir = file.path(base_path, "2_transformacion"),
    model_dir = file.path(base_path, "3_modelado"),
    load_dir = load_dir,
    fuentes_dir = fuentes_dir,
    raw_dir = file.path(fuentes_dir, "raw"),
    sanidad_xls_legacy = file.path(fuentes_dir, "raw", "sanidad", "datos.xls"),
    sns_indicators = list(
      sns_t_mental = list(codigo = "1365", label = "Prevalencia trastornos mentales"),
      sns_antidep  = list(codigo = "5930", label = "DHD antidepresivos"),
      sns_hipno    = list(codigo = "5920", label = "DHD hipnosedantes")
    ),
    ine_tables = list(
      suicidios = list(id = 46688L, label = "Tasa mortalidad por suicidio"),
      censo     = list(id = 56940L, label = "Censo de población (trimestral)")
    ),
    steps = normalize_steps(cli_value(cli_args, c("steps"), paste(c("extraccion", "transformacion", "modelado", "carga"), collapse = ","))),
    with_db = parse_bool(cli_value(cli_args, c("with-db", "with_db"), Sys.getenv("CED_WITH_DB", "false"))),
    horizon_year = max(2026L, as.integer(cli_value(cli_args, c("horizon-year", "horizon_year"), Sys.getenv("CED_HORIZON_YEAR", "2026")))),
    cv_folds = max(2L, as.integer(cli_value(cli_args, c("cv-folds", "cv_folds"), Sys.getenv("CED_CV_FOLDS", "3")))),
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
  ensure_dir(file.path(config$raw_dir, "sanidad"))
  ensure_dir(file.path(config$raw_dir, "ine"))
  assert_step_prerequisites(config)

  config
}
