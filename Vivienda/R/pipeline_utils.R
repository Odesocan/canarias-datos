`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0) {
    return(y)
  }

  if (is.character(x) && identical(trimws(x), "")) {
    return(y)
  }

  x
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
  allowed <- c("scraping", "extraccion", "transformacion", "modelado", "carga")
  items <- strsplit(value %||% paste(allowed, collapse = ","), ",", fixed = TRUE)[[1]]
  items <- tolower(trimws(items))
  items <- items[nzchar(items)]

  invalid <- setdiff(items, allowed)
  if (length(invalid) > 0) {
    stop(sprintf("Pasos no soportados: %s", paste(invalid, collapse = ", ")))
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

parse_month_label_es <- function(x) {
  value <- tolower(trimws(as.character(x)))
  value[!nzchar(value)] <- NA_character_

  month_map <- c(
    "enero" = "01",
    "febrero" = "02",
    "marzo" = "03",
    "abril" = "04",
    "mayo" = "05",
    "junio" = "06",
    "julio" = "07",
    "agosto" = "08",
    "septiembre" = "09",
    "setiembre" = "09",
    "octubre" = "10",
    "noviembre" = "11",
    "diciembre" = "12"
  )

  parsed <- vapply(value, function(item) {
    if (is.na(item)) {
      return(NA_character_)
    }

      if (grepl("^\\d{4}-\\d{2}-\\d{2}$", item)) {
        return(item)
      }
      if (grepl("^\\d{4}-\\d{2}$", item)) {
        return(paste0(item, "-01"))
      }
      if (grepl("^\\d{1,2}/\\d{1,2}/\\d{4}$", item)) {
        parts <- strsplit(item, "/", fixed = TRUE)[[1]]
        return(sprintf("%s-%02d-%02d", parts[[3]], as.integer(parts[[2]]), as.integer(parts[[1]])))
      }

    year_only <- regmatches(item, regexpr("\\d{4}", item))
    month_only <- regmatches(item, regexpr("enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre", item))

    if (length(year_only) == 0 || identical(year_only, character(0)) || length(month_only) == 0 || identical(month_only, character(0))) {
      return(NA_character_)
    }

    month_number <- month_map[[month_only]]
    if (is.null(month_number)) {
      return(NA_character_)
    }

    sprintf("%s-%s-01", year_only, month_number)
  }, character(1))

  as.Date(parsed)
}

normalize_key <- function(x) {
  value <- trimws(as.character(x))
  value <- iconv(value, from = "", to = "ASCII//TRANSLIT")
  value <- tolower(value)
  value <- gsub("[^a-z0-9]+", " ", value)
  trimws(value)
}

official_ccaa_levels <- function() {
  ced_official_ccaa_levels()
}

normalize_ccaa_name <- function(x) {
  lookup <- ced_ccaa_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("^\\d{1,2}\\s*", "", raw)
  key <- normalize_key(raw)
  idx <- match(key, lookup$key)
  normalized <- lookup$ccaa[idx]
  normalized[is.na(normalized)] <- raw[is.na(normalized)]

  normalized
}

province_lookup_table <- function() {
  tibble::tribble(
    ~provincia_key, ~provincia, ~ccaa,
    "alava", "Álava", "País Vasco",
    "araba alava", "Álava", "País Vasco",
    "albacete", "Albacete", "Castilla-La Mancha",
    "alicante", "Alicante", "Comunidad Valenciana",
    "alicante alacant", "Alicante", "Comunidad Valenciana",
    "almeria", "Almería", "Andalucía",
    "asturias", "Asturias", "Principado de Asturias",
    "avila", "Ávila", "Castilla y León",
    "badajoz", "Badajoz", "Extremadura",
    "barcelona", "Barcelona", "Cataluña",
    "burgos", "Burgos", "Castilla y León",
    "caceres", "Cáceres", "Extremadura",
    "cadiz", "Cádiz", "Andalucía",
    "cantabria", "Cantabria", "Cantabria",
    "castellon", "Castellón", "Comunidad Valenciana",
    "castellon castello", "Castellón", "Comunidad Valenciana",
    "ceuta", "Ceuta", "Ceuta",
    "ciudad real", "Ciudad Real", "Castilla-La Mancha",
    "cordoba", "Córdoba", "Andalucía",
    "cuenca", "Cuenca", "Castilla-La Mancha",
    "girona", "Girona", "Cataluña",
    "gerona", "Girona", "Cataluña",
    "granada", "Granada", "Andalucía",
    "guadalajara", "Guadalajara", "Castilla-La Mancha",
    "gipuzkoa", "Gipuzkoa", "País Vasco",
    "guipuzcoa", "Gipuzkoa", "País Vasco",
    "huelva", "Huelva", "Andalucía",
    "huesca", "Huesca", "Aragón",
    "illes balears", "Illes Balears", "Islas Baleares",
    "islas baleares", "Illes Balears", "Islas Baleares",
    "jaen", "Jaén", "Andalucía",
    "a coruna", "A Coruña", "Galicia",
    "la coruna", "A Coruña", "Galicia",
    "la rioja", "La Rioja", "La Rioja",
    "las palmas", "Las Palmas", "Canarias",
    "leon", "León", "Castilla y León",
    "lleida", "Lleida", "Cataluña",
    "lerida", "Lleida", "Cataluña",
    "lugo", "Lugo", "Galicia",
    "madrid", "Madrid", "Comunidad de Madrid",
    "malaga", "Málaga", "Andalucía",
    "melilla", "Melilla", "Melilla",
    "murcia", "Murcia", "Región de Murcia",
    "navarra", "Navarra", "Comunidad Foral de Navarra",
    "ourense", "Ourense", "Galicia",
    "orense", "Ourense", "Galicia",
    "palencia", "Palencia", "Castilla y León",
    "pontevedra", "Pontevedra", "Galicia",
    "salamanca", "Salamanca", "Castilla y León",
    "segovia", "Segovia", "Castilla y León",
    "sevilla", "Sevilla", "Andalucía",
    "soria", "Soria", "Castilla y León",
    "tarragona", "Tarragona", "Cataluña",
    "santa cruz de tenerife", "Santa Cruz de Tenerife", "Canarias",
    "teruel", "Teruel", "Aragón",
    "toledo", "Toledo", "Castilla-La Mancha",
    "valencia", "Valencia", "Comunidad Valenciana",
    "valencia valencia", "Valencia", "Comunidad Valenciana",
    "valladolid", "Valladolid", "Castilla y León",
    "bizkaia", "Bizkaia", "País Vasco",
    "vizcaya", "Bizkaia", "País Vasco",
    "zamora", "Zamora", "Castilla y León",
    "zaragoza", "Zaragoza", "Aragón"
  )
}

normalize_provincia_name <- function(x) {
  lookup <- province_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("\\s+[Pp]rovincia$", "", raw)
  raw <- gsub("^\\d{1,2}\\s*", "", raw)
  key <- normalize_key(raw)
  matched <- lookup$provincia[match(key, lookup$provincia_key)]
  matched[is.na(matched)] <- raw[is.na(matched)]
  matched
}

province_to_ccaa <- function(provincia) {
  lookup <- province_lookup_table()
  key <- normalize_key(provincia)
  matched <- lookup$ccaa[match(key, lookup$provincia_key)]
  matched
}

sanitize_year_headers <- function(names_vector) {
  names_vector[is.na(names_vector) | !nzchar(names_vector)] <- "dimension"

  names_vector |>
    gsub("^X", "", x = _) |>
    gsub("\\.0+$", "", x = _)
}

prepare_ine_table <- function(raw) {
  cleaned <- raw[-1, , drop = FALSE]
  cleaned <- janitor::row_to_names(cleaned, 1)
  names(cleaned) <- sanitize_year_headers(names(cleaned))
  cleaned
}

transform_ine_geo_table <- function(raw, value_name) {
  table <- prepare_ine_table(raw)
  names(table)[[1]] <- "ccaa"

  table |>
    dplyr::mutate(ccaa = as.character(.data$ccaa)) |>
    dplyr::filter(!is.na(.data$ccaa), !stringr::str_detect(.data$ccaa, "^Fuente"), .data$ccaa != "Total") |>
    tidyr::pivot_longer(
      cols = tidyselect::matches("^20\\d{2}$"),
      names_to = "periodo",
      values_to = value_name
    ) |>
    dplyr::mutate(
      periodo = as.integer(.data$periodo),
      value = parse_number_es(.data[[value_name]]),
      ccaa = normalize_ccaa_name(.data$ccaa)
    ) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels(), !is.na(.data$value)) |>
    dplyr::group_by(.data$ccaa, .data$periodo) |>
    dplyr::slice_head(n = 1) |>
    dplyr::ungroup() |>
    dplyr::select("ccaa", "periodo", "value") |>
    dplyr::rename(!!value_name := .data$value)
}

transform_ine_gender_table <- function(raw, value_name) {
  table <- prepare_ine_table(raw)
  names(table)[[1]] <- "genero"

  table |>
    dplyr::mutate(genero = tolower(trimws(as.character(.data$genero)))) |>
    dplyr::filter(.data$genero %in% c("total", "hombres", "mujeres")) |>
    tidyr::pivot_longer(
      cols = tidyselect::matches("^20\\d{2}$"),
      names_to = "periodo",
      values_to = value_name
    ) |>
    dplyr::mutate(
      periodo = as.integer(.data$periodo),
      value = parse_number_es(.data[[value_name]])
    ) |>
    dplyr::filter(!is.na(.data$value)) |>
    dplyr::group_by(.data$genero, .data$periodo) |>
    dplyr::slice_head(n = 1) |>
    dplyr::ungroup() |>
    dplyr::select("genero", "periodo", "value") |>
    dplyr::rename(!!value_name := .data$value)
}

impute_gender_series <- function(geo_df, gender_df, total_col, output_col) {
  gaps <- gender_df |>
    dplyr::select("periodo", "genero", value = dplyr::all_of(total_col)) |>
    tidyr::pivot_wider(names_from = .data$genero, values_from = .data$value) |>
    dplyr::mutate(gap = .data$hombres - .data$mujeres) |>
    dplyr::select("periodo", "gap")

  geo_df |>
    tidyr::crossing(genero = c("hombres", "mujeres", "total")) |>
    dplyr::left_join(gaps, by = "periodo") |>
    dplyr::mutate(
      value = dplyr::case_when(
        .data$genero == "hombres" ~ .data[[total_col]] + (.data$gap / 2),
        .data$genero == "mujeres" ~ .data[[total_col]] - (.data$gap / 2),
        TRUE ~ .data[[total_col]]
      )
    ) |>
    dplyr::select("ccaa", "periodo", "genero", "value") |>
    dplyr::rename(!!output_col := .data$value)
}

transform_hogares_mono <- function(raw) {
  raw |>
    dplyr::rename_with(tolower) |>
    dplyr::rename(
      ccaa = `comunidades y ciudades autónomas`,
      genero = sexo,
      hogares_mono = total
    ) |>
    dplyr::filter(
      !is.na(.data$ccaa),
      stringr::str_detect(.data$edad, regex("total", ignore_case = TRUE)),
      stringr::str_detect(.data$`estado civil`, regex("total", ignore_case = TRUE))
    ) |>
    dplyr::mutate(
      ccaa = normalize_ccaa_name(.data$ccaa),
      genero = dplyr::recode(
        .data$genero,
        "Ambos sexos" = "total",
        "Hombre" = "hombres",
        "Mujer" = "mujeres"
      ),
      periodo = as.integer(.data$periodo),
      hogares_mono = parse_number_es(.data$hogares_mono)
    ) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels(), !is.na(.data$hogares_mono)) |>
    dplyr::select("ccaa", "periodo", "genero", "hogares_mono")
}

transform_salario_mediano <- function(raw) {
  parts <- stringr::str_split(raw$Nombre, stringr::fixed("."))

  tibble::tibble(
    genero = trimws(purrr::map_chr(parts, ~ .x[[1]] %||% NA_character_)),
    ccaa = trimws(purrr::map_chr(parts, ~ .x[[2]] %||% NA_character_)),
    variable = trimws(purrr::map_chr(parts, ~ .x[[4]] %||% NA_character_)),
    periodo = as.integer(raw$Anyo),
    salario_mediano = as.numeric(raw$Valor)
  ) |>
    dplyr::mutate(
      ccaa = normalize_ccaa_name(.data$ccaa),
      genero = dplyr::recode(
        tolower(.data$genero),
        "total" = "total",
        "hombres" = "hombres",
        "mujeres" = "mujeres"
      )
    ) |>
    dplyr::filter(
      .data$variable == "50",
      .data$ccaa %in% official_ccaa_levels(),
      .data$genero %in% c("hombres", "mujeres", "total"),
      !is.na(.data$salario_mediano)
    ) |>
    dplyr::select("ccaa", "periodo", "genero", "salario_mediano")
}

prepare_price_locations <- function(raw) {
  if ("ccaa" %in% names(raw)) {
    return(
      raw |>
        dplyr::mutate(ccaa = normalize_ccaa_name(.data$ccaa))
    )
  }

  if ("comunidad" %in% names(raw)) {
    return(
      raw |>
        dplyr::mutate(ccaa = normalize_ccaa_name(.data$comunidad))
    )
  }

  raw |>
    dplyr::mutate(
      provincia = normalize_provincia_name(.data$provincia),
      ccaa = province_to_ccaa(.data$provincia)
    )
}

prepare_price_historic <- function(raw, value_col) {
  period_col <- if ("anio" %in% names(raw)) "anio" else "periodo"

  prepare_price_locations(raw) |>
    dplyr::mutate(
      periodo = as.integer(.data[[period_col]]),
      value = as.numeric(.data[[value_col]])
    ) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels(), !is.na(.data$periodo), !is.na(.data$value)) |>
    aggregate_price_to_ccaa(strategy = "simple_mean") |>
    dplyr::mutate(periodo_label = as.character(.data$periodo))
}

prepare_price_monthly_proxy <- function(raw, value_col) {
  located <- prepare_price_locations(raw)
  period_source <- if ("periodo_label" %in% names(located)) located$periodo_label else located$periodo

  located |>
    dplyr::mutate(
      periodo_date = parse_month_label_es(period_source),
      value = as.numeric(.data[[value_col]])
    ) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels(), !is.na(.data$periodo_date), !is.na(.data$value)) |>
    dplyr::mutate(
      periodo = lubridate::year(.data$periodo_date),
      periodo_label = format(.data$periodo_date, "%Y-%m")
    ) |>
    dplyr::filter(.data$periodo == max(.data$periodo, na.rm = TRUE)) |>
    dplyr::group_by(.data$ccaa) |>
    dplyr::filter(.data$periodo_date == max(.data$periodo_date, na.rm = TRUE)) |>
    dplyr::ungroup() |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$periodo_label) |>
    dplyr::summarise(value = mean(.data$value), .groups = "drop") |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$periodo_label) |>
    dplyr::summarise(value = mean(.data$value, na.rm = TRUE), .groups = "drop")
}

aggregate_price_to_ccaa <- function(data, strategy = "simple_mean") {
  if (!identical(strategy, "simple_mean")) {
    stop(sprintf("Estrategia de agregación no soportada: %s", strategy), call. = FALSE)
  }

  data |>
    dplyr::group_by(.data$ccaa, .data$periodo) |>
    dplyr::summarise(value = mean(.data$value, na.rm = TRUE), .groups = "drop")
}

extract_year_from_period <- function(x) {
  value <- trimws(as.character(x))
  matched <- ifelse(
    grepl("\\d{4}", value),
    sub(".*?(\\d{4}).*", "\\1", value),
    NA_character_
  )
  suppressWarnings(as.integer(matched))
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
    year_ccaa <- sort(unique(data$ccaa[data$periodo == year]))
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
  steps <- cfg$steps

  requirements <- list(
    transformacion = list(
      needed = c(
        "gasto_elevado",
        "gasto_elevado_gen",
        "dif_finmes",
        "dif_finmes_gen",
        "espacio_insuf",
        "espacio_insuf_gen",
        "retrasos_pagos",
        "retrasos_pagos_gen",
        "hogares_mono",
        "salario_mediano",
        "precio_venta_historico",
        "precio_venta_mensual",
        "precio_alquiler_historico",
        "precio_alquiler_mensual"
      ),
      dir_path = cfg$extraction_dir,
      generated_by = "extraccion"
    ),
    modelado = list(
      needed = c(
        "dif_finmes",
        "espacio_insuf",
        "gasto_elevado",
        "hogares_mono",
        "precio_alquiler",
        "precio_venta",
        "retrasos_pagos",
        "salario_mediano"
      ),
      dir_path = cfg$transform_dir,
      generated_by = "transformacion"
    ),
    carga = list(
      needed = c(
        "dif_finmes",
        "espacio_insuf",
        "gasto_elevado",
        "hogares_mono",
        "precio_alquiler",
        "precio_venta",
        "retrasos_pagos",
        "salario_destinado"
      ),
      dir_path = cfg$model_dir,
      generated_by = "modelado"
    )
  )

  for (step in names(requirements)) {
    if (!(step %in% steps) || requirements[[step]]$generated_by %in% steps) {
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

validate_raw_dataset <- function(path, spec) {
  data <- utils::read.csv(path, stringsAsFactors = FALSE, check.names = FALSE)
  assert_required_columns(data, spec$required_columns, basename(path))

  location_col <- dplyr::case_when(
    "ccaa" %in% names(data) ~ "ccaa",
    "comunidad" %in% names(data) ~ "comunidad",
    "provincia" %in% names(data) ~ "provincia",
    TRUE ~ NA_character_
  )
  if (is.na(location_col)) {
    stop(sprintf("%s no contiene columna de territorio: ccaa, comunidad o provincia", basename(path)), call. = FALSE)
  }

  duplicated_rows <- duplicated(data[c(location_col, "periodo")])
  if (any(duplicated_rows)) {
    stop(sprintf("%s contiene claves duplicadas de %s + periodo", basename(path), location_col), call. = FALSE)
  }

  years <- extract_year_from_period(data$periodo)
  valid_years <- stats::na.omit(years)
  if (length(valid_years) == 0) {
    stop(sprintf("%s no contiene periodos parseables", basename(path)), call. = FALSE)
  }

  if (length(unique(valid_years)) < spec$min_distinct_years) {
    stop(
      sprintf(
        "%s no cumple el mínimo de años distintos (%s)",
        basename(path),
        spec$min_distinct_years
      ),
      call. = FALSE
    )
  }

  latest_year <- max(valid_years)
  if (latest_year < spec$min_recent_year) {
    stop(
      sprintf(
        "%s no alcanza la frescura mínima esperada. Último año=%s, esperado>=%s",
        basename(path),
        latest_year,
        spec$min_recent_year
      ),
      call. = FALSE
    )
  }

  recent_rows <- data[years == latest_year, , drop = FALSE]
  recent_locations <- if (identical(location_col, "provincia")) {
    unique(recent_rows[[location_col]])
  } else {
    unique(normalize_ccaa_name(recent_rows[[location_col]]))
  }
  missing_locations <- setdiff(spec$recent_locations, recent_locations)
  if (length(missing_locations) > 0) {
    stop(
      sprintf(
        "%s no contiene territorios clave para %s: %s",
        basename(path),
        latest_year,
        paste(missing_locations, collapse = ", ")
      ),
      call. = FALSE
    )
  }

  log_event(
    "INFO",
    sprintf(
      "Raw validado %s: filas=%s | años=%s-%s",
      basename(path),
      nrow(data),
      min(valid_years),
      latest_year
    )
  )

  invisible(data)
}

raw_validation_specs <- function(current_year = as.integer(format(Sys.Date(), "%Y"))) {
  common_recent_locations <- c("Canarias", "Comunidad de Madrid", "Cataluña")
  list(
    venta_historico = list(
      required_columns = c("ccaa", "periodo", "periodo_label", "precio_venta_m2", "fuente_url", "fetched_at"),
      min_distinct_years = 3L,
      min_recent_year = current_year - 2L,
      recent_locations = common_recent_locations
    ),
    venta_mensual = list(
      required_columns = c("ccaa", "periodo", "periodo_label", "precio_venta_m2", "fuente_url", "fetched_at"),
      min_distinct_years = 2L,
      min_recent_year = current_year - 1L,
      recent_locations = common_recent_locations
    ),
    alquiler_historico = list(
      required_columns = c("ccaa", "periodo", "periodo_label", "precio_alquiler_m2", "fuente_url", "fetched_at"),
      min_distinct_years = 3L,
      min_recent_year = current_year - 2L,
      recent_locations = common_recent_locations
    ),
    alquiler_mensual = list(
      required_columns = c("ccaa", "periodo", "periodo_label", "precio_alquiler_m2", "fuente_url", "fetched_at"),
      min_distinct_years = 2L,
      min_recent_year = current_year - 1L,
      recent_locations = common_recent_locations
    )
  )
}

combine_price_series <- function(historic_df, monthly_proxy_df, output_col) {
  period_label_col <- paste0(output_col, "_periodo_label")

  dplyr::bind_rows(
    dplyr::mutate(historic_df, source_rank = 0L),
    dplyr::mutate(monthly_proxy_df, source_rank = 1L)
  ) |>
    dplyr::group_by(.data$ccaa, .data$periodo) |>
    dplyr::slice_max(.data$source_rank, n = 1, with_ties = FALSE) |>
    dplyr::ungroup() |>
    dplyr::select("ccaa", "periodo", "periodo_label", "value") |>
    dplyr::rename(
      !!output_col := value,
      !!period_label_col := periodo_label
    )
}

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

build_pipeline_config <- function(base_path, cli_args = list()) {
  raw_dir <- file.path(base_path, "fuentes", "raw", "idealista")
  scraping_dir <- file.path(base_path, "fuentes", "scrapings", "alquiler_historico_ccaa")

  config <- list(
    base_path = normalizePath(base_path, winslash = "/", mustWork = TRUE),
    extraction_dir = file.path(base_path, "1_extraccion"),
    transform_dir = file.path(base_path, "2_transformacion"),
    model_dir = file.path(base_path, "3_modelado"),
    load_dir = file.path(base_path, "4_carga"),
    raw_dir = raw_dir,
    scraping_dir = scraping_dir,
    scraper_script = file.path(scraping_dir, "main.py"),
    scraper_python = Sys.getenv("CED_PYTHON_BIN", "python3"),
    price_aggregation_strategy = "simple_mean",
    raw_files = list(
      alquiler_historico = file.path(raw_dir, "alquiler_historico.csv"),
      alquiler_mensual = file.path(raw_dir, "alquiler_mensual.csv")
    ),
    raw_specs = raw_validation_specs(),
    steps = normalize_steps(cli_value(cli_args, c("steps"), paste(c("scraping", "extraccion", "transformacion", "modelado", "carga"), collapse = ","))),
    run_scraping = parse_bool(cli_value(cli_args, c("run-scraping", "run_scraping"), FALSE)),
    with_db = parse_bool(cli_value(cli_args, c("with-db", "with_db"), FALSE)),
    projection_target_year = as.integer(Sys.getenv("CED_PROJECTION_TARGET_YEAR", "2026")),
    model_validation_years = as.integer(Sys.getenv("CED_MODEL_VALIDATION_YEARS", "3")),
    db = list(
      name = Sys.getenv("CED_DB_NAME", ""),
      host = Sys.getenv("CED_DB_HOST", "localhost"),
      port = as.integer(Sys.getenv("CED_DB_PORT", "5432")),
      user = Sys.getenv("CED_DB_USER", ""),
      password = Sys.getenv("CED_DB_PASSWORD", ""),
      schema = Sys.getenv("CED_DB_SCHEMA", "canendatos")
    )
  )

  ensure_dir(config$extraction_dir)
  ensure_dir(config$transform_dir)
  ensure_dir(config$model_dir)
  ensure_dir(config$load_dir)
  ensure_dir(config$raw_dir)
  assert_step_prerequisites(config)

  config
}

assert_raw_inputs <- function(cfg) {
  purrr::iwalk(cfg$raw_files, function(path, name) {
    assert_file_exists(path, sprintf("raw %s", name))
    validate_raw_dataset(path, cfg$raw_specs[[name]])
  })
}
