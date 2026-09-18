# =============================================================================
# Sanidad · Canarias en Datos — utilidades compartidas del pipeline
# Cliente API INCLASNS (Ministerio de Sanidad), normalización, validación,
# configuración de indicadores núcleo y construcción del índice de mortalidad
# evitable (portado del proyecto Prevención de ODESOCAN).
# =============================================================================

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0) return(y)
  if (is.character(x) && identical(trimws(x), "")) return(y)
  x
}

parse_bool <- function(x, default = FALSE) {
  if (is.null(x) || length(x) == 0) return(default)
  v <- tolower(trimws(as.character(x[[1]])))
  if (v %in% c("true", "1", "yes", "y", "si", "sí")) return(TRUE)
  if (v %in% c("false", "0", "no", "n")) return(FALSE)
  default
}

# Código ISO/INE de 2 dígitos de la CCAA canónica (para la columna ccaa_cod).
ccaa_to_cod <- function(x) {
  lookup <- ced_ccaa_lookup_table()
  map <- setNames(lookup$ccaa_code, lookup$ccaa)
  unname(map[x])
}

require_packages <- function(packages) {
  missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly = TRUE)]
  if (length(missing) > 0) {
    stop(sprintf("Faltan paquetes de R requeridos: %s", paste(missing, collapse = ", ")), call. = FALSE)
  }
  invisible(packages)
}

log_event <- function(level, message) {
  cat(sprintf("[%s] [%-7s] %s\n", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), level, message))
}

ensure_dir <- function(path) {
  dir.create(path, recursive = TRUE, showWarnings = FALSE)
  invisible(path)
}

# Ejecuta una expresión; ante error, loguea WARN y devuelve `default` sin abortar.
safe_step <- function(expr, label = "paso", default = NULL) {
  tryCatch(
    force(expr),
    error = function(e) {
      log_event("WARN", sprintf("%s falló: %s", label, conditionMessage(e)))
      default
    }
  )
}

save_named_rds <- function(objects, dir_path) {
  ensure_dir(dir_path)
  purrr::iwalk(objects, function(value, name) {
    if (!is.null(value)) saveRDS(value, file.path(dir_path, paste0(name, ".rds")))
  })
  invisible(objects)
}

assert_required_columns <- function(data, required, label = deparse(substitute(data))) {
  missing <- setdiff(required, names(data))
  if (length(missing) > 0) {
    stop(sprintf("%s no contiene columnas requeridas: %s", label, paste(missing, collapse = ", ")), call. = FALSE)
  }
}

# ----------------------------------------------------------------------------
# Normalización territorial y de género (delegan en R/ccaa_dictionary.R)
# ----------------------------------------------------------------------------
normalize_ccaa_name <- function(x) {
  if (!exists("ced_ccaa_lookup_table")) {
    stop("ced_ccaa_lookup_table no cargado. Haz source() de R/ccaa_dictionary.R", call. = FALSE)
  }
  lookup <- ced_ccaa_lookup_table()
  raw <- trimws(as.character(x))
  raw <- gsub("\\s*\\([^)]*\\)$", "", raw)
  key <- ced_normalize_text_key(raw)
  normalized <- lookup$ccaa[match(key, lookup$key)]
  normalized[is.na(normalized)] <- raw[is.na(normalized)]
  normalized
}

# Sanidad conserva las ciudades autónomas (Ceuta y Melilla) además de las 17 CCAA.
official_ccaa_levels <- function(include_national = FALSE) {
  ced_official_ccaa_levels(
    include_state = isTRUE(include_national),
    include_autonomous_cities = TRUE
  )
}

# Unifica los literales de sexo de la API a tres categorías canónicas.
normalize_genero <- function(x) {
  v <- tolower(trimws(as.character(x)))
  dplyr::case_when(
    v %in% c("total", "ambos sexos", "ambos") ~ "total",
    v %in% c("hombres", "hombre", "varones", "varón") ~ "hombres",
    v %in% c("mujeres", "mujer") ~ "mujeres",
    TRUE ~ NA_character_
  )
}

# ----------------------------------------------------------------------------
# API INCLASNS — Indicadores Clave del SNS (Ministerio de Sanidad)
# ----------------------------------------------------------------------------
sns_api_base <- function() Sys.getenv("SNS_API_BASE", "https://inclasns.sanidad.gob.es")

sns_api_token <- function() {
  token <- Sys.getenv("SNS_API_TOKEN", "")
  if (!nzchar(token)) stop("Falta la variable de entorno SNS_API_TOKEN. Revisa .Renviron.", call. = FALSE)
  token
}

#' Descarga datos de un indicador del API INCLASNS.
#' Llama a /api/v2/datos?indicador=CODE&ccaa=&anio=&API_KEY=TOKEN.
#' `sexo` NULL = agregado Total; "hombre"/"mujer" = esa categoría. NUNCA sexo="".
#' Devuelve: indicador_codigo | indicador_nombre | ccaa_raw | anio | sexo | valor
sns_get_indicador <- function(codigo, sexo = NULL, retries = 3L, timeout_secs = 60L) {
  require_packages(c("httr", "jsonlite"))
  url <- sprintf("%s/api/v2/datos", sns_api_base())
  query <- list(indicador = codigo, ccaa = "", anio = "", API_KEY = sns_api_token())
  if (!is.null(sexo) && nzchar(sexo)) query$sexo <- sexo

  attempt <- 1L
  repeat {
    resp <- tryCatch(httr::GET(url, query = query, httr::timeout(timeout_secs)), error = function(e) e)
    if (!inherits(resp, "error") && httr::status_code(resp) == 200) {
      raw_text <- httr::content(resp, as = "text", encoding = "UTF-8")
      parsed <- tryCatch(jsonlite::fromJSON(raw_text, simplifyVector = FALSE), error = function(e) e)
      if (!inherits(parsed, "error") && length(parsed) > 0) {
        block <- parsed[[1]]
        if (is.character(block) || is.character(parsed[[1]])) {
          stop(sprintf("INCLASNS API error (indicador=%s, sexo=%s): %s",
                       codigo, sexo %||% "(none)", as.character(parsed[[1]])), call. = FALSE)
        }
        rows <- block$datos %||% list()
        if (length(rows) == 0) {
          return(data.frame(indicador_codigo = character(0), indicador_nombre = character(0),
                            ccaa_raw = character(0), anio = integer(0), sexo = character(0),
                            valor = numeric(0), stringsAsFactors = FALSE))
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
      msg <- if (inherits(resp, "error")) conditionMessage(resp) else sprintf("HTTP %s", httr::status_code(resp))
      stop(sprintf("INCLASNS indicador=%s: fallo tras %s intentos (%s)", codigo, retries, msg), call. = FALSE)
    }
    attempt <- attempt + 1L
    Sys.sleep(2 * attempt)
  }
}

# ----------------------------------------------------------------------------
# Tidy multi-componente (formato largo -> wide por componente)
# Portado de Prevención::tidy_sns_group. Entrada con columna `componente`.
# Salida: ccaa | periodo | genero | <comp1> | <comp2> | ...
# ----------------------------------------------------------------------------
tidy_sns_group <- function(raw) {
  if (is.null(raw) || nrow(raw) == 0L) return(NULL)
  if (!"componente" %in% names(raw)) {
    log_event("WARN", "tidy_sns_group: sin columna 'componente'")
    return(NULL)
  }
  raw |>
    dplyr::mutate(
      ccaa    = normalize_ccaa_name(.data$ccaa_raw),
      genero  = normalize_genero(.data$sexo),
      periodo = suppressWarnings(as.integer(.data$anio)),
      valor   = suppressWarnings(as.numeric(.data$valor))
    ) |>
    dplyr::filter(
      !is.na(.data$genero), !is.na(.data$periodo), !is.na(.data$valor),
      .data$ccaa %in% official_ccaa_levels(include_national = TRUE)
    ) |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$genero, .data$componente) |>
    dplyr::summarise(valor = mean(.data$valor, na.rm = TRUE), .groups = "drop") |>
    tidyr::pivot_wider(names_from = "componente", values_from = "valor")
}

# ----------------------------------------------------------------------------
# Índice compuesto de mortalidad evitable
# Portado de Prevención::build_mort_evitable_idx (2_transformacion/transformacion.R).
# Método: cada componente de mortalidad prematura (cáncer 1240, cardiopatía 1250,
# diabetes 1260, ictus 1270, EPOC 1280) se normaliza dividiéndolo por su media
# histórica nacional; el índice es el promedio simple de los componentes
# normalizados. Valor > 1 = mortalidad prematura por encima de la media histórica.
# ----------------------------------------------------------------------------
build_mort_evitable_idx <- function(mort_wide,
                                    components = c("mort_cancer", "mort_cardio",
                                                   "mort_diabetes", "mort_ictus", "mort_epoc")) {
  if (is.null(mort_wide) || nrow(mort_wide) == 0L) return(NULL)
  present <- intersect(components, names(mort_wide))
  if (length(present) == 0L) {
    log_event("WARN", "mort_evitable_idx: ningún componente disponible")
    return(NULL)
  }
  if (length(present) < length(components)) {
    log_event("WARN", sprintf("mort_evitable_idx: solo %d/%d componentes (%s)",
                              length(present), length(components), paste(present, collapse = ", ")))
  }
  normalizers <- vapply(present, function(c) mean(mort_wide[[c]], na.rm = TRUE), numeric(1))
  normalizers[normalizers == 0 | !is.finite(normalizers)] <- NA_real_

  scaled <- mort_wide
  for (c in present) scaled[[c]] <- mort_wide[[c]] / normalizers[[c]]

  scaled$mort_evitable_idx <- rowMeans(as.matrix(scaled[, present, drop = FALSE]), na.rm = TRUE)
  scaled$mort_evitable_idx[!is.finite(scaled$mort_evitable_idx)] <- NA_real_
  scaled
}

# Reescalado 0-100 (min-max) del índice para difusión pública en Sanidad.
# Conserva orden y distancias relativas; mayor valor = mayor mortalidad evitable.
rescale_0_100 <- function(x) {
  rng <- range(x, na.rm = TRUE)
  if (!all(is.finite(rng)) || diff(rng) == 0) return(rep(NA_real_, length(x)))
  100 * (x - rng[1]) / (rng[2] - rng[1])
}

# ----------------------------------------------------------------------------
# Configuración del pipeline de Sanidad — selección núcleo definitiva (Tabla 2)
# ----------------------------------------------------------------------------
GEN_TOTAL   <- c("total")
GEN_COMPLET <- c("total", "hombre", "mujer")

# Localiza el fichero más reciente que casa con un patrón glob (por nombre).
find_latest_file <- function(dir_path, pattern) {
  files <- list.files(dir_path, pattern = pattern, full.names = TRUE)
  if (length(files) == 0) return(NA_character_)
  files[order(basename(files), decreasing = TRUE)][1]
}

build_sanidad_config <- function(base_path) {
  base_path <- normalizePath(base_path, winslash = "/", mustWork = TRUE)
  config <- list(
    base_path      = base_path,
    extraction_dir = file.path(base_path, "1_extraccion"),
    transform_dir  = file.path(base_path, "2_transformacion"),
    model_dir      = file.path(base_path, "3_modelado"),
    load_dir       = file.path(base_path, "4_carga"),
    # Fuente externa: área de Presupuestos (gasto sanitario autonómico sobre PIB)
    presupuestos_dir = file.path(dirname(base_path), "Presupuestos", "outputs"),
    # Carga a Supabase (schema canendatos). --with-db / CED_WITH_DB la activan.
    with_db = parse_bool(Sys.getenv("CED_WITH_DB", "false")),
    db = list(
      host     = Sys.getenv("SUPABASE_HOST", ""),
      port     = as.integer(Sys.getenv("SUPABASE_PORT", "5432")),
      name     = Sys.getenv("SUPABASE_DBNAME", "postgres"),
      user     = Sys.getenv("SUPABASE_USER", ""),
      password = Sys.getenv("SUPABASE_PASS", ""),
      schema   = Sys.getenv("SUPABASE_SCHEMA", "canendatos"),
      api_url  = sub("/$", "", Sys.getenv("SUPABASE_URL", "")),
      api_key  = trimws(Sys.getenv("SUPABASE_SERVICE_KEY", ""))
    ),
    # Componentes del índice de mortalidad evitable (orden estable)
    mort_evitable_keys = c("mort_cancer", "mort_cardio", "mort_diabetes", "mort_ictus", "mort_epoc"),
    # Modelado (bagged ETS bootstrap): variables proyectables y años a imputar.
    # Se proyecta el índice de mortalidad evitable (no sus componentes) y el
    # resto de indicadores anuales; las series que ya cubren un año objetivo se
    # saltan solas ("ya cubierto por la serie observada").
    # El horizonte llega a 2026, como el resto de áreas del hub. La población
    # entra también: es el peso de la media estatal, y sin ella 2026 sería el
    # único año con media simple.
    imputar_target_years = c(2024L, 2025L, 2026L),
    imputar_variables = c("avs_65", "mort_evitable_idx",
                          "med_ae", "med_ap", "enf_ae", "enf_ap", "camas",
                          "gasto_farmacia_pct", "pct_pib_sanidad",
                          "espera_quir", "espera_ae", "reingresos_psiq",
                          "poblacion_total"),
    sns_indicators = list(
      # --- Estado de salud ---
      avs_65         = list(codigo = "1050", label = "Años de vida saludable a los 65 años", grupo = "estado_salud", generos = GEN_COMPLET),
      # --- Mortalidad prematura: componentes del índice (desagregado por género) ---
      mort_cancer    = list(codigo = "1240", label = "Mortalidad prematura por cáncer", grupo = "mort_evitable", generos = GEN_COMPLET),
      mort_cardio    = list(codigo = "1250", label = "Mortalidad prematura por cardiopatía isquémica", grupo = "mort_evitable", generos = GEN_COMPLET),
      mort_diabetes  = list(codigo = "1260", label = "Mortalidad prematura por diabetes mellitus", grupo = "mort_evitable", generos = GEN_COMPLET),
      mort_ictus     = list(codigo = "1270", label = "Mortalidad prematura por enfermedad vascular cerebral", grupo = "mort_evitable", generos = GEN_COMPLET),
      mort_epoc      = list(codigo = "1280", label = "Mortalidad prematura por EPOC", grupo = "mort_evitable", generos = GEN_COMPLET),
      # --- Recursos (nivel sistema: solo total) ---
      med_ae         = list(codigo = "4050", label = "Personal médico en atención especializada", grupo = "recursos", generos = GEN_TOTAL),
      med_ap         = list(codigo = "4060", label = "Personal médico en atención primaria", grupo = "recursos", generos = GEN_TOTAL),
      enf_ae         = list(codigo = "4070", label = "Personal de enfermería en atención especializada", grupo = "recursos", generos = GEN_TOTAL),
      enf_ap         = list(codigo = "4080", label = "Personal de enfermería en atención primaria", grupo = "recursos", generos = GEN_TOTAL),
      camas          = list(codigo = "4090", label = "Camas hospitalarias en funcionamiento", grupo = "recursos", generos = GEN_TOTAL),
      # --- Gasto (nivel sistema: solo total) ---
      # NOTA: 6020 (gasto público per cápita) se descartó: la API solo lo expone
      # a nivel nacional (sin desglose CCAA). El esfuerzo de gasto por CCAA se
      # cubre con la variable gasto_pib_sanidad importada del área de Presupuestos
      # (ver fetch_presupuestos_pib en 1_extraccion/extraccion.R).
      gasto_farmacia_pct = list(codigo = "6060", label = "Porcentaje del gasto en farmacia", grupo = "gasto", generos = GEN_TOTAL),
      # --- Accesibilidad (nivel sistema: solo total) ---
      espera_quir    = list(codigo = "8200", label = "Tiempo medio de espera para intervención quirúrgica no urgente", grupo = "accesibilidad", generos = GEN_TOTAL),
      espera_ae      = list(codigo = "8290", label = "Tiempo medio de espera para 1ª consulta en atención especializada", grupo = "accesibilidad", generos = GEN_TOTAL),
      # --- Resultados (desagregado por género) ---
      reingresos_psiq = list(codigo = "7140", label = "Reingresos urgentes psiquiátricos", grupo = "resultados", generos = GEN_COMPLET),
      # --- Denominadores (desagregado por género) ---
      poblacion_total = list(codigo = "9000", label = "Población total", grupo = "poblacion", generos = GEN_COMPLET)
    )
  )
  ensure_dir(config$extraction_dir)
  config
}
