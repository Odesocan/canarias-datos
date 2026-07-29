suppressPackageStartupMessages({
  library(DBI)
  library(dplyr)
  library(glue)
  library(purrr)
  library(RPostgres)
  library(readr)
  library(writexl)
})

connect_db <- function(cfg) {
  missing <- names(cfg$db)[vapply(cfg$db[c("name", "host", "port", "user", "password")], function(x) identical(x, "") || is.na(x), logical(1))]
  if (length(missing) > 0) {
    stop(sprintf("Faltan variables de entorno de BD: %s", paste(missing, collapse = ", ")), call. = FALSE)
  }

  DBI::dbConnect(
    RPostgres::Postgres(),
    dbname = cfg$db$name,
    host = cfg$db$host,
    port = cfg$db$port,
    user = cfg$db$user,
    password = cfg$db$password
  )
}

prepare_global_table <- function(tables) {
  global_tables <- purrr::map(
    tables,
    function(df) {
      cleaned <- df
      if (!"origen" %in% names(cleaned)) {
        cleaned <- dplyr::mutate(cleaned, origen = "real")
      }
      if ("genero" %in% names(cleaned)) {
        cleaned <- cleaned |>
          dplyr::filter(.data$genero == "total") |>
          dplyr::select(-dplyr::all_of("genero"))
      }
      cleaned
    }
  )

  merged <- merge_metric_tables(global_tables, c("ccaa", "periodo", "origen")) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels()) |>
    dplyr::mutate(
      dplyr::across(where(is.numeric), ~ round(.x, 2)),
      periodo = as.integer(.data$periodo)
    )

  assert_unique_keys(merged, c("ccaa", "periodo", "origen"), "ced_vivienda_global")
  merged
}

prepare_gender_table <- function(tables) {
  gender_tables <- purrr::map(
    tables,
    function(df) {
      if (!"origen" %in% names(df)) {
        df <- dplyr::mutate(df, origen = "real")
      }
      df
    }
  )

  merged <- merge_metric_tables(gender_tables, c("ccaa", "periodo", "genero", "origen")) |>
    dplyr::filter(.data$ccaa %in% official_ccaa_levels()) |>
    dplyr::mutate(
      dplyr::across(where(is.numeric), ~ round(.x, 2)),
      periodo = as.integer(.data$periodo)
    )

  assert_unique_keys(merged, c("ccaa", "periodo", "genero", "origen"), "ced_vivienda_gen")
  merged
}

write_exports <- function(cfg, global_df, gender_df) {
  readr::write_csv2(global_df, file.path(cfg$load_dir, "ced_vivienda_global.csv"))
  writexl::write_xlsx(global_df, file.path(cfg$load_dir, "ced_vivienda_global.xlsx"))
  readr::write_csv2(gender_df, file.path(cfg$load_dir, "ced_vivienda_gen.csv"))
  writexl::write_xlsx(gender_df, file.path(cfg$load_dir, "ced_vivienda_gen.xlsx"))
}

# Row Level Security — se re-aplica tras cada carga.
# dbWriteTable(overwrite = TRUE) hace DROP + CREATE, asi que la tabla nueva
# nace sin RLS, sin politica y sin permisos: sin este paso, o la tabla queda
# invisible para la web (anon no puede leer) o, si alguien concede permisos a
# mano, queda abierta a escritura. Mismo patron que Dependencia/4_carga/carga.R.
apply_rls <- function(con, schema, tables) {
  # Sin USAGE sobre el esquema, PostgREST responde 401 aunque la tabla tenga
  # GRANT SELECT y politica RLS.
  DBI::dbExecute(con, sprintf('GRANT USAGE ON SCHEMA "%s" TO anon, authenticated', schema))

  for (target in tables) {
    policy <- paste0(target, "_select_anon")
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
}

write_database <- function(cfg, global_df, gender_df) {
  con <- connect_db(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  DBI::dbExecute(con, sprintf('CREATE SCHEMA IF NOT EXISTS "%s"', cfg$db$schema))
  DBI::dbWriteTable(
    con,
    DBI::Id(schema = cfg$db$schema, table = "ced_vivienda_global"),
    global_df,
    overwrite = TRUE
  )
  DBI::dbWriteTable(
    con,
    DBI::Id(schema = cfg$db$schema, table = "ced_vivienda_gen"),
    gender_df,
    overwrite = TRUE
  )

  apply_rls(con, cfg$db$schema, c("ced_vivienda_global", "ced_vivienda_gen"))
}

run_carga <- function(cfg) {
  log_event("INFO", "Iniciando carga")

  modeled <- load_named_rds(
    cfg$model_dir,
    c(
      "dif_finmes",
      "espacio_insuf",
      "gasto_elevado",
      "hogares_mono",
      "precio_alquiler",
      "precio_venta",
      "retrasos_pagos",
      "salario_destinado"
    )
  )

  ced_vivienda_global <- prepare_global_table(modeled)
  ced_vivienda_gen <- prepare_gender_table(modeled[c("dif_finmes", "espacio_insuf", "gasto_elevado", "hogares_mono", "retrasos_pagos", "salario_destinado")])

  log_series_coverage(ced_vivienda_global, "ced_vivienda_global")
  log_series_coverage(ced_vivienda_gen, "ced_vivienda_gen")
  log_table_quality(ced_vivienda_global, "ced_vivienda_global", c("periodo"))
  log_table_quality(ced_vivienda_gen, "ced_vivienda_gen", c("periodo"))

  write_exports(cfg, ced_vivienda_global, ced_vivienda_gen)

  if (isTRUE(cfg$with_db)) {
    write_database(cfg, ced_vivienda_global, ced_vivienda_gen)
    log_event("DB", "Carga en PostgreSQL completada")
  }

  log_event("OK", "Carga completada")

  invisible(list(
    ced_vivienda_global = ced_vivienda_global,
    ced_vivienda_gen = ced_vivienda_gen
  ))
}
