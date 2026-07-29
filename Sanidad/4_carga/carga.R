# =============================================================================
# Sanidad · Canarias en Datos — ETAPA 4: CARGA
# Construye las tablas de distribución global_sanidad (género 'total') y
# gen_sanidad (hombres/mujeres), exporta CSV/XLSX y, si --with-db, las carga
# en Supabase (schema canendatos) vía REST API (DELETE + INSERT por lotes).
# Convención de origen a nivel de fila: 'proyeccion' si el año contiene alguna
# celda proyectada (bagged ETS), 'real' en caso contrario.
# Entrada: 3_modelado/ced_sanidad_largo.rds. Salida: 4_carga/* (+ Supabase).
# =============================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "tidyr", "purrr", "glue", "readr", "writexl", "httr2", "jsonlite", "DBI", "RPostgres"))
  library(dplyr); library(tidyr); library(glue); library(purrr)
})

GLOBAL_TABLE <- "global_sanidad"
GEN_TABLE    <- "gen_sanidad"

GLOBAL_INDICATORS <- c("avs_65", "mort_cancer", "mort_cardio", "mort_diabetes", "mort_ictus", "mort_epoc",
                       "mort_evitable_idx", "mort_evitable_idx_0_100",
                       "med_ae", "med_ap", "enf_ae", "enf_ap", "camas",
                       "gasto_farmacia_pct", "pct_pib_sanidad", "imp_sanidad_eur", "pib_regional_eur",
                       "espera_quir", "espera_ae", "reingresos_psiq", "poblacion_total")
GEN_INDICATORS    <- c("avs_65", "mort_cancer", "mort_cardio", "mort_diabetes", "mort_ictus", "mort_epoc",
                       "mort_evitable_idx", "mort_evitable_idx_0_100", "reingresos_psiq", "poblacion_total")

# ---- Construcción de las tablas anchas desde la tabla larga con origen -------
build_carga_tables <- function(cfg) {
  largo <- readRDS(file.path(cfg$model_dir, "ced_sanidad_largo.rds"))
  ccaa_ok <- official_ccaa_levels(include_national = FALSE)   # 17 CCAA + Ceuta + Melilla

  # origen a nivel de fila (ccaa, periodo, genero)
  origen_row <- largo |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$genero) |>
    dplyr::summarise(origen = if (any(.data$origen == "proyeccion")) "proyeccion" else "real", .groups = "drop")

  wide <- largo |>
    dplyr::select("ccaa", "periodo", "genero", "variable", "valor") |>
    tidyr::pivot_wider(names_from = "variable", values_from = "valor") |>
    dplyr::left_join(origen_row, by = c("ccaa", "periodo", "genero")) |>
    dplyr::filter(.data$ccaa %in% ccaa_ok) |>
    dplyr::mutate(periodo = as.integer(.data$periodo), ccaa_cod = ccaa_to_cod(.data$ccaa))

  round2 <- function(df, cols) dplyr::mutate(df, dplyr::across(dplyr::any_of(cols), ~ round(.x, 2)))

  global <- wide |>
    dplyr::filter(.data$genero == "total") |>
    round2(GLOBAL_INDICATORS) |>
    dplyr::select("ccaa", "ccaa_cod", "periodo", "origen", dplyr::any_of(GLOBAL_INDICATORS)) |>
    dplyr::arrange(.data$ccaa, .data$periodo)
  assert_required_columns(global, c("ccaa", "periodo", "origen"), "global_sanidad")
  if (anyDuplicated(global[c("ccaa", "periodo")])) stop("global_sanidad: claves (ccaa,periodo) duplicadas", call. = FALSE)

  gen <- wide |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    round2(GEN_INDICATORS) |>
    dplyr::select("ccaa", "ccaa_cod", "periodo", "genero", "origen", dplyr::any_of(GEN_INDICATORS)) |>
    dplyr::arrange(.data$ccaa, .data$periodo, .data$genero)
  if (anyDuplicated(gen[c("ccaa", "periodo", "genero")])) stop("gen_sanidad: claves duplicadas", call. = FALSE)

  list(global = global, gen = gen)
}

write_exports <- function(cfg, global_df, gen_df) {
  ensure_dir(cfg$load_dir)
  readr::write_csv2(global_df, file.path(cfg$load_dir, "global_sanidad.csv"))
  writexl::write_xlsx(global_df, file.path(cfg$load_dir, "global_sanidad.xlsx"))
  readr::write_csv2(gen_df, file.path(cfg$load_dir, "gen_sanidad.csv"))
  writexl::write_xlsx(gen_df, file.path(cfg$load_dir, "gen_sanidad.xlsx"))
  log_event("OK", glue("Exportados global_sanidad ({nrow(global_df)}) y gen_sanidad ({nrow(gen_df)}) a CSV/XLSX"))
}

# ---- Carga vía REST API (PostgREST). La tabla destino ya debe existir. -------
supabase_api_available <- function(cfg) nzchar(cfg$db$api_url) && nzchar(cfg$db$api_key)

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
    httr2::req_timeout(120) |>
    httr2::req_error(is_error = function(resp) FALSE)
  if (!is.null(prefer)) req <- httr2::req_headers(req, Prefer = prefer)
  if (!is.null(query))  req <- httr2::req_url_query(req, !!!query)
  if (!is.null(body))   req <- httr2::req_body_raw(req, body, type = "application/json")
  httr2::req_perform(req)
}

write_table_via_api <- function(cfg, data, table, batch_size = 500) {
  log_event("DB", glue("Vaciando {cfg$db$schema}.{table} vía REST API"))
  del <- supabase_request(cfg, table, method = "DELETE", query = list(periodo = "gte.0"), prefer = "return=minimal")
  if (httr2::resp_status(del) >= 300) {
    stop(glue("DELETE {table} error {httr2::resp_status(del)}: {httr2::resp_body_string(del)}"), call. = FALSE)
  }
  records <- purrr::transpose(data)
  n <- length(records); inserted <- 0L
  for (i in seq(1L, n, by = batch_size)) {
    chunk <- records[i:min(i + batch_size - 1L, n)]
    body <- jsonlite::toJSON(chunk, auto_unbox = TRUE, na = "null", dataframe = "rows")
    resp <- supabase_request(cfg, table, method = "POST", body = body, prefer = "return=minimal")
    if (httr2::resp_status(resp) >= 300) {
      stop(glue("INSERT {table} error {httr2::resp_status(resp)}: {httr2::resp_body_string(resp)}"), call. = FALSE)
    }
    inserted <- inserted + length(chunk)
  }
  log_event("DB", glue("Carga completada: {inserted} filas en {cfg$db$schema}.{table}"))
}

# ---- Carga vía pooler PostgreSQL (rol postgres, dueño de las tablas). --------
# TRUNCATE + append preserva la estructura, RLS y grants creados por el DDL
# (a diferencia de dbWriteTable(overwrite), que dropea y recrea la tabla).
connect_db_pg <- function(cfg) {
  if (tolower(cfg$db$host) %in% c("localhost", "127.0.0.1"))
    stop("SUPABASE_HOST no puede apuntar a localhost.", call. = FALSE)
  DBI::dbConnect(RPostgres::Postgres(), host = cfg$db$host, port = cfg$db$port,
                 dbname = cfg$db$name, user = cfg$db$user, password = cfg$db$password)
}

write_table_via_pg <- function(cfg, data, table) {
  con <- connect_db_pg(cfg); on.exit(DBI::dbDisconnect(con), add = TRUE)
  DBI::dbExecute(con, sprintf('TRUNCATE TABLE "%s"."%s"', cfg$db$schema, table))
  DBI::dbAppendTable(con, DBI::Id(schema = cfg$db$schema, table = table), data)
  log_event("DB", glue("PG: {nrow(data)} filas cargadas en {cfg$db$schema}.{table}"))
}

run_carga <- function(cfg) {
  log_event("INFO", "Iniciando carga")
  tabs <- build_carga_tables(cfg)
  write_exports(cfg, tabs$global, tabs$gen)

  if (isTRUE(cfg$with_db)) {
    # Preferimos el pooler PG (rol postgres = dueño). Si falla y hay REST API
    # con grants a service_role, se usa como alternativa.
    ok <- safe_step({
      write_table_via_pg(cfg, tabs$global, GLOBAL_TABLE)
      write_table_via_pg(cfg, tabs$gen, GEN_TABLE)
      TRUE
    }, label = "Carga PG pooler", default = FALSE)
    if (!isTRUE(ok)) {
      if (!supabase_api_available(cfg)) stop("Carga: PG pooler falló y no hay REST API configurada", call. = FALSE)
      log_event("DB", "PG pooler no disponible; usando REST API")
      write_table_via_api(cfg, tabs$global, GLOBAL_TABLE)
      write_table_via_api(cfg, tabs$gen, GEN_TABLE)
    }
    log_event("DB", "Carga en Supabase completada")
  } else {
    log_event("INFO", "Carga a Supabase omitida (--with-db=false)")
  }
  log_event("OK", "Carga completada")
  invisible(tabs)
}
