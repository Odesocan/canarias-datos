# ============================================================
# 4_carga/carga.R — Exporta la tabla canónica y carga en Supabase.
# Patrón alineado con Salud mental:
#  - Export local CSV/XLSX (ced_presupuestos.csv|xlsx)
#  - Carga opcional vía REST API (PostgREST) si SUPABASE_URL+KEY
#  - Carga vía PG directo si no hay API y SUPABASE_HOST está definido
# ============================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr","glue","readr","writexl","purrr"))
  library(dplyr)
  library(glue)
})

write_exports <- function(cfg, data) {
  readr::write_csv2(data, file.path(cfg$load_dir, "ced_presupuestos.csv"))
  writexl::write_xlsx(data, file.path(cfg$load_dir, "ced_presupuestos.xlsx"))
}

# ----------------------------------------------------------------------------
# Capa Hacienda — integra el dump SGCIEF (4_carga/hacienda_capa_*.csv)
# como filas adicionales con capa='hacienda' y imp_total agregado por
# CCAA-año. Es independiente del modelado autonómico: cuando un CCAA-año
# tiene también capa autonómica, conviven con la clave única
# (ccaa, periodo, genero, origen, capa).
# ----------------------------------------------------------------------------

load_hacienda_layer <- function(cfg) {
  patrones <- list.files(cfg$load_dir, pattern = "^hacienda_capa.*\\.csv$",
                          full.names = TRUE, ignore.case = TRUE)
  if (length(patrones) == 0) {
    log_event("INFO", "Capa Hacienda: sin CSV en 4_carga/ (saltando)")
    return(tibble::tibble())
  }
  dfs <- purrr::map(patrones, function(p) {
    tryCatch(readr::read_csv(p, show_col_types = FALSE,
                              col_types = readr::cols(.default = readr::col_character(),
                                                       importe_eur = readr::col_double(),
                                                       anio = readr::col_integer())),
              error = function(e) {
                log_event("WARN", sprintf("Capa Hacienda: error leyendo %s: %s",
                                           basename(p), conditionMessage(e)))
                NULL
              })
  })
  dfs <- dfs[!vapply(dfs, is.null, logical(1))]
  if (length(dfs) == 0) return(tibble::tibble())

  raw <- dplyr::bind_rows(dfs)
  required <- c("ccaa_id3","anio","importe_eur")
  if (!all(required %in% names(raw))) {
    log_event("WARN", sprintf("Capa Hacienda: CSV sin columnas %s",
                               paste(setdiff(required, names(raw)), collapse = ", ")))
    return(tibble::tibble())
  }

  agg <- raw |>
    dplyr::filter(!is.na(.data$ccaa_id3), !is.na(.data$anio),
                  is.finite(.data$importe_eur)) |>
    dplyr::group_by(.data$ccaa_id3, .data$anio) |>
    dplyr::summarise(imp_total = sum(.data$importe_eur, na.rm = TRUE),
                     .groups = "drop")

  agg$ccaa <- ced_id3_to_ccaa(agg$ccaa_id3)
  agg <- agg |> dplyr::filter(!is.na(.data$ccaa))

  if (nrow(agg) == 0) {
    log_event("WARN", "Capa Hacienda: ninguna fila tras mapear id3 a CCAA canónico")
    return(tibble::tibble())
  }

  out <- tibble::tibble(
    ccaa        = agg$ccaa,
    periodo     = as.integer(agg$anio),
    genero      = "total",
    origen      = "real",
    capa        = "hacienda",
    es_prorroga = FALSE,
    estimado    = FALSE,
    imp_total   = agg$imp_total
  )
  log_event("OK", sprintf("Capa Hacienda: %d filas CCAA-año (años=%s-%s, CCAA=%d)",
                           nrow(out), min(out$periodo), max(out$periodo),
                           dplyr::n_distinct(out$ccaa)))
  out
}

connect_supabase <- function(cfg) {
  db <- cfg$db
  missing <- names(db)[vapply(db[c("host","user","password")],
                              function(x) identical(x, "") || is.na(x), logical(1))]
  if (length(missing) > 0) {
    stop(sprintf("Faltan variables Supabase: %s", paste(missing, collapse = ", ")), call. = FALSE)
  }
  require_packages(c("DBI","RPostgres"))
  DBI::dbConnect(RPostgres::Postgres(), host = db$host, port = db$port,
                  dbname = db$name, user = db$user, password = db$password)
}

ensure_supabase_table <- function(cfg, columnas_extra) {
  con <- connect_supabase(cfg); on.exit(DBI::dbDisconnect(con), add = TRUE)
  schema <- cfg$db$schema; target <- "ced_presupuestos"

  base_cols <- "
      ccaa text NOT NULL,
      periodo integer NOT NULL,
      genero text NOT NULL DEFAULT 'total',
      origen text NOT NULL DEFAULT 'real',
      capa text NOT NULL DEFAULT 'autonomica',
      es_prorroga boolean NOT NULL DEFAULT false,
      estimado boolean NOT NULL DEFAULT false,
      pib_origen text"

  DBI::dbExecute(con, sprintf('CREATE SCHEMA IF NOT EXISTS "%s"', schema))
  DBI::dbExecute(con, sprintf('CREATE TABLE IF NOT EXISTS "%s"."%s" (%s)',
                              schema, target, base_cols))

  # Columnas de TEXTO añadidas fuera del set base (para tablas preexistentes):
  # pib_origen marca si el PIB regional del año es real o proyección bootstrap.
  cols_texto <- c("pib_origen")
  for (col in intersect(columnas_extra, cols_texto)) {
    DBI::dbExecute(con, sprintf(
      'ALTER TABLE "%s"."%s" ADD COLUMN IF NOT EXISTS "%s" text',
      schema, target, col))
  }

  # El resto de columnas dinámicas (imp_*, pib_*, pibreg_*, pc_*, var_*,
  # pib_regional_eur) son numéricas.
  for (col in setdiff(columnas_extra, cols_texto)) {
    DBI::dbExecute(con, sprintf(
      'ALTER TABLE "%s"."%s" ADD COLUMN IF NOT EXISTS "%s" double precision',
      schema, target, col))
  }

  DBI::dbExecute(con, sprintf(
    'CREATE UNIQUE INDEX IF NOT EXISTS "ced_presupuestos_key_idx"
       ON "%s"."%s" (ccaa, periodo, genero, origen, capa)',
    schema, target))
}

write_supabase_pg <- function(cfg, data) {
  ensure_supabase_table(cfg, setdiff(names(data),
                                      c("ccaa","periodo","genero","origen","capa",
                                        "es_prorroga","estimado")))
  con <- connect_supabase(cfg); on.exit(DBI::dbDisconnect(con), add = TRUE)
  schema <- cfg$db$schema; target <- "ced_presupuestos"

  DBI::dbWithTransaction(con, {
    DBI::dbExecute(con, sprintf('DELETE FROM "%s"."%s"', schema, target))
    DBI::dbAppendTable(con, DBI::Id(schema = schema, table = target), data)
  })
}

supabase_api_available <- function(cfg) {
  nzchar(cfg$db$api_url) && nzchar(cfg$db$api_key)
}

supabase_request <- function(cfg, path, method = "GET", body = NULL, prefer = NULL, query = NULL) {
  require_packages("httr2")
  req <- httr2::request(paste0(cfg$db$api_url, "/rest/v1/", path)) |>
    httr2::req_method(method) |>
    httr2::req_headers(
      apikey = cfg$db$api_key,
      Authorization = paste("Bearer", cfg$db$api_key),
      `Accept-Profile` = cfg$db$schema,
      `Content-Profile` = cfg$db$schema,
      `Content-Type` = "application/json"
    ) |>
    httr2::req_timeout(120)
  if (!is.null(prefer)) req <- httr2::req_headers(req, Prefer = prefer)
  if (!is.null(query))  req <- httr2::req_url_query(req, !!!query)
  if (!is.null(body))   req <- httr2::req_body_raw(req, body, type = "application/json")
  httr2::req_perform(req)
}

write_supabase_via_api <- function(cfg, data, batch_size = 500) {
  require_packages(c("httr2","jsonlite"))
  target <- "ced_presupuestos"
  log_event("DB", glue("Vaciando {cfg$db$schema}.{target} vía REST"))
  supabase_request(cfg, target, method = "DELETE",
                    query = list(periodo = "gte.0"), prefer = "return=minimal")
  records <- purrr::transpose(data)
  n <- length(records)
  log_event("DB", glue("Insertando {n} filas en lotes de {batch_size}"))
  inserted <- 0L
  for (i in seq(1L, n, by = batch_size)) {
    chunk <- records[i:min(i + batch_size - 1L, n)]
    body <- jsonlite::toJSON(chunk, auto_unbox = TRUE, na = "null", dataframe = "rows")
    resp <- supabase_request(cfg, target, method = "POST", body = body, prefer = "return=minimal")
    st <- httr2::resp_status(resp)
    if (st >= 300) stop(sprintf("Supabase API error %s: %s", st, httr2::resp_body_string(resp)),
                        call. = FALSE)
    inserted <- inserted + length(chunk)
  }
  log_event("DB", glue("Carga REST completada: {inserted} filas"))
}

run_carga <- function(cfg) {
  log_event("INFO", "Iniciando carga")

  modeled <- load_named_rds(cfg$model_dir, c("ced_presupuestos"))
  ced <- modeled$ced_presupuestos

  if (nrow(ced) == 0) {
    log_event("WARN", "ced_presupuestos vacío — escribiendo CSV/XLSX vacíos")
    write_exports(cfg, ced)
    return(invisible(list(ced_presupuestos = ced)))
  }

  ced <- ced |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels()) |>
    dplyr::mutate(periodo = as.integer(.data$periodo))

  # Capa Hacienda — append filas con capa='hacienda' e imp_total
  # agregado por CCAA-año desde el dump SGCIEF en 4_carga/hacienda_capa*.csv
  hacienda <- load_hacienda_layer(cfg)
  if (nrow(hacienda) > 0) {
    hacienda <- hacienda |>
      dplyr::filter(.data$ccaa %in% official_ccaa_levels(),
                    !is.na(.data$periodo))
    if (nrow(hacienda) > 0 && any(ced$capa == "hacienda", na.rm = TRUE)) {
      key_cols <- c("ccaa","periodo","genero","origen","capa")
      hacienda_original <- nrow(hacienda)
      hacienda <- hacienda |>
        dplyr::anti_join(
          ced |> dplyr::filter(.data$capa == "hacienda") |>
            dplyr::select(dplyr::all_of(key_cols)),
          by = key_cols
        )
      omitidas <- hacienda_original - nrow(hacienda)
      if (omitidas > 0) {
        log_event("WARN", sprintf(
          "Capa Hacienda: omitidas %d filas ya presentes en el modelado para evitar duplicados",
          omitidas
        ))
      }
    }
    # Asegura columnas comunes: si el ced trae imp_* columnas, las añadimos
    # como NA en hacienda (y viceversa) para que bind_rows respete schema.
    if (nrow(hacienda) > 0) {
      ced <- dplyr::bind_rows(ced, hacienda)
    }
  }

  assert_required_columns(ced, c("ccaa","periodo","genero","origen","capa"), "ced_presupuestos carga")
  assert_unique_keys(ced, c("ccaa","periodo","genero","origen","capa"), "ced_presupuestos carga")

  log_series_coverage(ced, "ced_presupuestos carga")
  log_table_quality(ced, "ced_presupuestos carga", c("periodo"))

  write_exports(cfg, ced)
  log_event("OK", sprintf("Exportados ced_presupuestos.csv/xlsx (%d filas)", nrow(ced)))

  if (isTRUE(cfg$with_db)) {
    if (supabase_api_available(cfg)) {
      log_event("DB", "Usando REST API (SUPABASE_URL detectada)")
      write_supabase_via_api(cfg, ced)
    } else {
      log_event("DB", "Usando conexión PostgreSQL")
      write_supabase_pg(cfg, ced)
    }
    log_event("DB", "Carga en Supabase completada")
  } else {
    log_event("INFO", "Carga a Supabase omitida (--with-db=false)")
  }

  log_event("OK", "Carga completada")
  invisible(list(ced_presupuestos = ced))
}
