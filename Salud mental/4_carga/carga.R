suppressPackageStartupMessages({
  require_packages(c("DBI", "RPostgres", "dplyr", "glue", "readr", "writexl", "httr2", "jsonlite", "purrr"))
  library(DBI)
  library(RPostgres)
  library(dplyr)
  library(glue)
  library(readr)
  library(writexl)
  library(httr2)
  library(jsonlite)
  library(purrr)
})

connect_supabase <- function(cfg) {
  db_cfg <- cfg$db
  missing <- names(db_cfg)[vapply(db_cfg[c("host", "user", "password")], function(x) identical(x, "") || is.na(x), logical(1))]
  if (length(missing) > 0) {
    stop(
      sprintf(
        "Faltan variables de entorno de Supabase: %s",
        paste(missing, collapse = ", ")
      ),
      call. = FALSE
    )
  }

  if (tolower(db_cfg$host) %in% c("localhost", "127.0.0.1")) {
    stop("SUPABASE_HOST no puede apuntar a localhost en este pipeline.", call. = FALSE)
  }

  DBI::dbConnect(
    RPostgres::Postgres(),
    host = db_cfg$host,
    port = db_cfg$port,
    dbname = db_cfg$name,
    user = db_cfg$user,
    password = db_cfg$password
  )
}

write_exports <- function(cfg, data) {
  readr::write_csv2(data, file.path(cfg$load_dir, "ced_saludmental.csv"))
  writexl::write_xlsx(data, file.path(cfg$load_dir, "ced_saludmental.xlsx"))
}

ensure_supabase_table <- function(cfg) {
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  schema <- cfg$db$schema
  target <- "ced_saludmental"

  DBI::dbExecute(con, sprintf('CREATE SCHEMA IF NOT EXISTS "%s"', schema))
  DBI::dbExecute(con, sprintf('DROP TABLE IF EXISTS "%s"."%s"', schema, target))
  DBI::dbExecute(con, sprintf('
    CREATE TABLE "%s"."%s" (
      ccaa text NOT NULL,
      periodo integer NOT NULL,
      genero text NOT NULL,
      origen text NOT NULL,
      t_mental double precision,
      brecha_rel double precision,
      antidep_ajustado double precision,
      hipno_ajustado double precision,
      suicidios double precision,
      censo double precision,
      n_personas_tm double precision,
      antidep_anual_total double precision,
      hipno_anual_total double precision,
      n_suicidios double precision
    )', schema, target))
  DBI::dbExecute(con, sprintf(
    'CREATE UNIQUE INDEX "ced_saludmental_key_idx" ON "%s"."%s" (ccaa, periodo, genero, origen)',
    schema, target
  ))
}

write_supabase_data <- function(cfg, data) {
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  schema <- cfg$db$schema
  target <- "ced_saludmental"

  DBI::dbAppendTable(con, DBI::Id(schema = schema, table = target), data)
}

# Row Level Security — se re-aplica tras cada carga.
# ensure_supabase_table() hace DROP + CREATE, asi que la tabla nueva nace sin
# RLS, sin politica y sin permisos: sin este paso, o la tabla queda invisible
# para la web (anon no puede leer) o, si alguien concede permisos a mano, queda
# abierta a escritura. Mismo patron que Dependencia/4_carga/carga.R.
# Solo aplica a la ruta PostgreSQL: la ruta REST (write_supabase_via_api) hace
# DELETE + INSERT sin recrear la tabla, asi que alli el RLS sobrevive.
apply_rls <- function(cfg, target = "ced_saludmental") {
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  schema <- cfg$db$schema
  policy <- paste0(target, "_select_anon")

  # Sin USAGE sobre el esquema, PostgREST responde 401 aunque la tabla tenga
  # GRANT SELECT y politica RLS.
  DBI::dbExecute(con, sprintf('GRANT USAGE ON SCHEMA "%s" TO anon, authenticated', schema))
  DBI::dbExecute(con, sprintf(
    'ALTER TABLE "%s"."%s" ENABLE ROW LEVEL SECURITY', schema, target
  ))
  DBI::dbExecute(con, sprintf(
    'DROP POLICY IF EXISTS %s ON "%s"."%s"', policy, schema, target
  ))
  DBI::dbExecute(con, sprintf(
    'CREATE POLICY %s ON "%s"."%s" FOR SELECT
       TO anon, authenticated USING (TRUE)', policy, schema, target
  ))
  DBI::dbExecute(con, sprintf(
    'GRANT SELECT ON "%s"."%s" TO anon, authenticated', schema, target
  ))
  log_event("DB", sprintf("RLS + politica de solo lectura aplicados a %s", target))
}

write_supabase_table <- function(cfg, data) {
  ensure_supabase_table(cfg)
  log_event("DB", "Tabla ced_saludmental creada en Supabase")
  write_supabase_data(cfg, data)
  apply_rls(cfg)
}

# -----------------------------------------------------------------------------
# REST API (PostgREST) — bypass del pooler PG. Requiere SUPABASE_URL +
# SUPABASE_SERVICE_KEY (service_role) en .Renviron. La tabla destino ya debe
# existir en el esquema (créala con el SQL en docs si es la primera vez).
# -----------------------------------------------------------------------------

supabase_api_available <- function(cfg) {
  nzchar(cfg$db$api_url) && nzchar(cfg$db$api_key)
}

supabase_request <- function(cfg, path, method = "GET", body = NULL, prefer = NULL, query = NULL) {
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

write_supabase_via_api <- function(cfg, data, table = "ced_saludmental", batch_size = 500) {
  if (!supabase_api_available(cfg)) {
    stop("REST API no configurada: faltan SUPABASE_URL o SUPABASE_SERVICE_KEY", call. = FALSE)
  }

  log_event("DB", glue::glue("Vaciando {cfg$db$schema}.{table} vía REST API"))
  supabase_request(
    cfg, table, method = "DELETE",
    query = list(periodo = "gte.0"),
    prefer = "return=minimal"
  )

  records <- purrr::transpose(data)
  n <- length(records)
  log_event("DB", glue::glue("Insertando {n} filas en lotes de {batch_size}"))

  inserted <- 0L
  for (i in seq(1L, n, by = batch_size)) {
    chunk <- records[i:min(i + batch_size - 1L, n)]
    body <- jsonlite::toJSON(chunk, auto_unbox = TRUE, na = "null", dataframe = "rows")
    resp <- supabase_request(cfg, table, method = "POST", body = body, prefer = "return=minimal")
    status <- httr2::resp_status(resp)
    if (status >= 300) {
      stop(sprintf("Supabase API error %s: %s", status, httr2::resp_body_string(resp)), call. = FALSE)
    }
    inserted <- inserted + length(chunk)
  }
  log_event("DB", glue::glue("Carga vía REST API completada: {inserted} filas en {cfg$db$schema}.{table}"))
}

run_carga <- function(cfg) {
  log_event("INFO", "Iniciando carga")

  modeled <- load_named_rds(cfg$model_dir, c("ced_saludmental"))
  ced_saludmental <- modeled$ced_saludmental |>
    filter(.data$ccaa %in% official_ccaa_levels()) |>
    mutate(periodo = as.integer(.data$periodo))

  assert_required_columns(
    ced_saludmental,
    c(
      "ccaa", "periodo", "genero", "origen",
      "t_mental", "brecha_rel", "antidep_ajustado", "hipno_ajustado", "suicidios",
      "censo", "n_personas_tm", "antidep_anual_total", "hipno_anual_total", "n_suicidios"
    ),
    "ced_saludmental"
  )
  assert_unique_keys(ced_saludmental, c("ccaa", "periodo", "genero", "origen"), "ced_saludmental carga")

  log_series_coverage(ced_saludmental, "ced_saludmental carga")
  log_table_quality(ced_saludmental, "ced_saludmental carga", c("periodo"))

  write_exports(cfg, ced_saludmental)

  if (isTRUE(cfg$with_db)) {
    if (supabase_api_available(cfg)) {
      log_event("DB", "Usando REST API (SUPABASE_URL detectada)")
      write_supabase_via_api(cfg, ced_saludmental)
    } else {
      log_event("DB", "Usando conexión PostgreSQL (pooler)")
      write_supabase_table(cfg, ced_saludmental)
    }
    log_event("DB", "Carga en Supabase completada")
  } else {
    log_event("INFO", "Carga a Supabase omitida (--with-db=false)")
  }

  log_event("OK", "Carga completada")

  invisible(list(ced_saludmental = ced_saludmental))
}
