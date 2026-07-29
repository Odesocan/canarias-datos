# =============================================================================
# Sanidad · Canarias en Datos — ETAPA 1: EXTRACCIÓN
# Descarga la selección núcleo definitiva de indicadores del INCLASNS
# (Ministerio de Sanidad) y persiste un RDS por grupo temático en 1_extraccion.
# Fuente troncal: API INCLASNS /api/v2/datos.
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("glue", "purrr", "httr", "jsonlite", "dplyr", "tidyr"))
  library(glue)
  library(purrr)
})

# Traduce el literal de género de la config al parámetro que espera la API
# ("total" -> NULL; "hombre"/"mujer" tal cual). NUNCA se pasa sexo = "".
.genero_to_api <- function(g) if (identical(g, "total")) NULL else g

#' Descarga un indicador para su lista de géneros y lo devuelve en formato largo,
#' etiquetado con su clave semántica (`componente`) y grupo temático.
fetch_sns_indicator <- function(spec, key) {
  purrr::map_dfr(spec$generos, function(g) {
    api_sexo <- .genero_to_api(g)
    log_event("API", glue("INCLASNS ind={spec$codigo} ({key}) sexo={g}"))
    df <- safe_step(sns_get_indicador(spec$codigo, sexo = api_sexo),
                    label = glue("INCLASNS {key} ({spec$codigo}) sexo={g}"),
                    default = NULL)
    if (is.null(df) || nrow(df) == 0L) return(NULL)
    df$componente <- key
    df$grupo <- spec$grupo
    df
  })
}

# -----------------------------------------------------------------------------
# Fuente externa: área de Presupuestos — gasto sanitario autonómico sobre PIB.
# Lee el fichero integrado más reciente (presupuestos_pib_integrado_*.csv) del
# área de Presupuestos y devuelve la variable pct_pib_sanidad (% del PIB regional
# destinado a la función Sanidad en el presupuesto de cada CCAA), junto con el
# importe y el PIB regional. Es gasto PRESUPUESTADO (esfuerzo), no liquidado.
# Salida (formato tidy): ccaa | periodo | genero | pct_pib_sanidad |
#                        imp_sanidad_eur | pib_regional_eur | origen_pib
# -----------------------------------------------------------------------------
fetch_presupuestos_pib <- function(cfg) {
  path <- find_latest_file(cfg$presupuestos_dir, "^presupuestos_pib_integrado_\\d{4}-\\d{2}-\\d{2}\\.csv$")
  if (is.na(path) || !file.exists(path)) {
    log_event("WARN", glue("No se encontró presupuestos_pib_integrado_*.csv en {cfg$presupuestos_dir}"))
    return(NULL)
  }
  log_event("API", glue("Presupuestos: leyendo {basename(path)}"))
  raw <- utils::read.csv(path, stringsAsFactors = FALSE, encoding = "UTF-8")

  needed <- c("ccaa", "anio", "pct_pib_sanidad", "imp_sanidad", "pib_regional_eur", "origen_pib")
  assert_required_columns(raw, needed, "presupuestos_pib_integrado")

  # Dos abreviaturas no las cubre el diccionario territorial; se pre-normalizan.
  fix <- c("Cast. y León" = "Castilla y León", "Cast.-La Mancha" = "Castilla-La Mancha")
  ccaa_full <- ifelse(raw$ccaa %in% names(fix), fix[raw$ccaa], raw$ccaa)

  out <- data.frame(
    ccaa            = normalize_ccaa_name(ccaa_full),
    periodo         = suppressWarnings(as.integer(raw$anio)),
    genero          = "total",
    pct_pib_sanidad = suppressWarnings(as.numeric(raw$pct_pib_sanidad)),
    imp_sanidad_eur = suppressWarnings(as.numeric(raw$imp_sanidad)),
    pib_regional_eur = suppressWarnings(as.numeric(raw$pib_regional_eur)),
    origen_pib      = as.character(raw$origen_pib),
    stringsAsFactors = FALSE
  )
  out <- out[!is.na(out$periodo) & !is.na(out$pct_pib_sanidad) &
               out$ccaa %in% official_ccaa_levels(include_national = TRUE), , drop = FALSE]
  log_event("OK", glue("Presupuestos gasto_pib_sanidad: {nrow(out)} filas, {length(unique(out$ccaa))} CCAA, {min(out$periodo)}-{max(out$periodo)}"))
  out
}

run_extraccion <- function(cfg) {
  log_event("INFO", "Iniciando extracción (INCLASNS — selección núcleo Sanidad)")

  # Descarga indicador a indicador según la config
  raw_all <- purrr::imap_dfr(cfg$sns_indicators, function(spec, key) {
    df <- fetch_sns_indicator(spec, key)
    if (is.null(df) || nrow(df) == 0L) {
      log_event("WARN", glue("Sin datos para {key} ({spec$codigo})"))
      return(NULL)
    }
    df
  })

  if (is.null(raw_all) || nrow(raw_all) == 0L) {
    stop("La extracción no devolvió datos. Revisa credenciales y conectividad.", call. = FALSE)
  }
  assert_required_columns(
    raw_all,
    c("indicador_codigo", "indicador_nombre", "ccaa_raw", "anio", "sexo", "valor", "componente", "grupo"),
    "raw_all"
  )

  # Parte por grupo temático y persiste un RDS por grupo (formato largo)
  grupos <- split(raw_all, raw_all$grupo)
  save_named_rds(grupos, cfg$extraction_dir)
  # Además, un RDS consolidado con todo el crudo
  saveRDS(raw_all, file.path(cfg$extraction_dir, "raw_sanidad.rds"))

  # Fuente externa: gasto sanitario sobre PIB (área de Presupuestos)
  gasto_pib <- safe_step(fetch_presupuestos_pib(cfg), label = "Presupuestos gasto_pib_sanidad", default = NULL)
  if (!is.null(gasto_pib) && nrow(gasto_pib) > 0) {
    saveRDS(gasto_pib, file.path(cfg$extraction_dir, "gasto_pib.rds"))
  }

  # Resumen de extracción
  resumen <- raw_all |>
    dplyr::group_by(.data$grupo, .data$componente, .data$indicador_codigo) |>
    dplyr::summarise(
      filas = dplyr::n(),
      con_valor = sum(!is.na(.data$valor)),
      generos = paste(sort(unique(.data$sexo)), collapse = "/"),
      anio_min = suppressWarnings(min(.data$anio[!is.na(.data$valor)], na.rm = TRUE)),
      anio_max = suppressWarnings(max(.data$anio[!is.na(.data$valor)], na.rm = TRUE)),
      .groups = "drop"
    )
  print(as.data.frame(resumen))

  log_event("OK", glue("Extracción completada: {nrow(raw_all)} filas, {length(grupos)} grupos, {dplyr::n_distinct(raw_all$componente)} indicadores"))
  invisible(list(raw_all = raw_all, grupos = grupos, resumen = resumen))
}
