# ===========================================================================
# carga.R -- Salidas finales y carga atomica a Supabase
# ===========================================================================
# Cuaderno v2 §11.4: hub D3 con dos tablas
#   * ced_dependencia_global: CCAA x fecha x indicadores (real + proyeccion)
#   * ced_dependencia_gen:    CCAA x fecha x genero (estimacion via palanca)
# Cuaderno v2 §6.3: la desagregacion de genero en metricas no desagregadas en
# origen es una ESTIMACION INDICATIVA (flag origen_genero = 'estimado').
# Cuaderno v2 §8.7: la columna 'solicitudes' del dictsaad se renombra a
# 'solicitudes_dict' para evitar la colision con la de solsaad.
# ===========================================================================

suppressPackageStartupMessages({
  require_packages(c("dplyr", "glue", "purrr", "readr", "stringi", "tidyr"))
  library(dplyr); library(glue); library(purrr); library(readr); library(tidyr)
})

# ===========================================================================
# Helpers de carga
# ===========================================================================

sanitize_table_name <- function(x) {
  x <- tolower(x)
  x <- gsub("[^a-z0-9_]", "_", x)
  x <- gsub("_+", "_", x)
  x <- gsub("^_|_$", "", x)
  if (nchar(x) == 0) x <- "tabla"
  x
}

clean_invisibles <- function(x) {
  x <- stringi::stri_replace_all_regex(
    x,
    "[\\u00A0\\u202F\\u2007\\u2009\\u200A\\u2000-\\u2006\\u2008\\u200B\\u2060\\uFEFF\\t]",
    " "
  )
  x <- gsub("\\s+", " ", x)
  trimws(x)
}

to_utf8_df <- function(df) {
  df[] <- lapply(df, function(col) {
    if (is.factor(col)) col <- as.character(col)
    if (is.character(col)) {
      col <- enc2utf8(col)
      col <- clean_invisibles(col)
    }
    col
  })
  df
}

normalize_load_table <- function(df) {
  if ("ccaa" %in% names(df)) df <- df |> mutate(ccaa = normalize_ccaa_name(ccaa))
  df
}

# ===========================================================================
# ced_dependencia_global: dashboard_indicators con proyeccion + raws auxiliares
# ===========================================================================

# Combina dashboard_indicators (10 indicadores + origen) con las tablas raw
# que el dashboard quiera consultar a demanda (e.g. solicitudes absolutas).
# Resuelve la colision 'solicitudes' renombrando la de dictsaad (cuaderno §8.7).
prepare_global_table <- function(modeled) {
  if (!"dashboard_indicators" %in% names(modeled)) {
    stop("Falta dashboard_indicators en el directorio de modelado", call. = FALSE)
  }

  ind <- normalize_load_table(modeled[["dashboard_indicators"]])

  # Anexar variables crudas relevantes (no del dashboard pero utiles para
  # tooltip/drill-down). Solo ccaa+fecha; aceptamos NA en la proyeccion futura.
  raw_specs <- list(
    solsaad_all    = c("solicitudes"),
    benpresaad_all = c("pers_benef_prest", "atencion_residencial",
                       "pe_cuidados_fam", "pe_vinc_serv", "ayuda_domicilio",
                       "centros_dia_noche", "teleasistencia", "total"),
    dictsaad_all   = c("resoluciones_grado", "grado1", "grado2", "grado3",
                       "total_der_prest", "solicitudes_dict"),
    pend_grado     = c("pendientes_grado_total", "pendientes_grado_6m_o_mas"),
    pend_pia       = c("pendientes_pia_total"),
    benefect_full  = c("personas_con_pia", "personas_prest_efectiva",
                       "pendientes_prest_efectiva"),
    tiempo_espera  = c("tiempo_solicitud_grado", "tiempo_grado_prestacion")
  )

  enrich <- ind
  for (nm in names(raw_specs)) {
    if (!nm %in% names(modeled)) next
    df <- normalize_load_table(modeled[[nm]])
    if (!all(c("ccaa", "fecha") %in% names(df))) next

    if (nm == "dictsaad_all" && "solicitudes" %in% names(df) && !"solicitudes_dict" %in% names(df)) {
      df <- df |> dplyr::rename(solicitudes_dict = solicitudes)
    }
    cols <- intersect(raw_specs[[nm]], names(df))
    if (!length(cols)) next
    df <- df |>
      dplyr::select(dplyr::all_of(c("ccaa", "fecha", cols))) |>
      dplyr::group_by(ccaa, fecha) |>
      dplyr::summarise(dplyr::across(dplyr::everything(),
                                     ~ dplyr::first(.x[!is.na(.x)] %||% .x)),
                       .groups = "drop")
    enrich <- enrich |>
      dplyr::mutate(fecha = as.Date(fecha)) |>
      dplyr::left_join(df |> dplyr::mutate(fecha = as.Date(fecha)),
                       by = c("ccaa", "fecha"))
  }

  enrich |>
    dplyr::mutate(dplyr::across(where(is.numeric), ~ round(.x, 4))) |>
    dplyr::arrange(ccaa, fecha)
}

# ===========================================================================
# ced_dependencia_gen: palanca de genero (cuaderno §6.3)
# ===========================================================================

# Aplica el ratio mujer/(hombre+mujer) de perf_ccaa_genero a las metricas
# que el IMSERSO no desagrega en origen. Marca origen_genero='estimado'.
prepare_gen_table <- function(modeled) {
  if (!"dashboard_indicators" %in% names(modeled) || !"perf_ccaa_genero" %in% names(modeled)) {
    log_event("WARN", "Falta perf_ccaa_genero o dashboard_indicators: ced_dependencia_gen omitido")
    return(NULL)
  }

  ind <- normalize_load_table(modeled[["dashboard_indicators"]]) |>
    dplyr::mutate(fecha = as.Date(fecha))
  perf <- normalize_load_table(modeled[["perf_ccaa_genero"]]) |>
    dplyr::mutate(
      fecha = as.Date(fecha),
      pct_mujer  = mujer  / (hombre + mujer),
      pct_hombre = hombre / (hombre + mujer)
    ) |>
    dplyr::select(ccaa, fecha, pct_hombre, pct_mujer)

  # Para fechas proyectadas (sin perf_ccaa_genero) usamos el ultimo ratio
  # observado de cada CCAA. Asume continuidad estructural del genero (§6.3).
  last_ratio <- perf |>
    dplyr::group_by(ccaa) |>
    dplyr::slice_max(fecha, n = 1, with_ties = FALSE) |>
    dplyr::ungroup() |>
    dplyr::select(ccaa, pct_hombre_carry = pct_hombre, pct_mujer_carry = pct_mujer)

  # Indicadores PPD-relativizados a desagregar por genero (ratio_*, pct_* sobre
  # totales y series de tiempo se mantienen como caracteristicas estructurales
  # de cada CCAA x fecha sin desagregacion).
  vars_to_split <- intersect(
    c("cobertura_pct_ppd", "solicitudes_pct_ppd",
      "limbo_grado_pct_ppd", "limbo_pia_pct_ppd", "limbo_prestaciones_pct_ppd"),
    names(ind)
  )
  if (!length(vars_to_split)) return(NULL)

  joined <- ind |>
    dplyr::left_join(perf, by = c("ccaa", "fecha")) |>
    dplyr::left_join(last_ratio, by = "ccaa") |>
    dplyr::mutate(
      pct_hombre = dplyr::coalesce(pct_hombre, pct_hombre_carry),
      pct_mujer  = dplyr::coalesce(pct_mujer,  pct_mujer_carry)
    ) |>
    dplyr::select(-pct_hombre_carry, -pct_mujer_carry)

  long <- purrr::map_dfr(c("hombre", "mujer"), function(g) {
    pct_col <- if (g == "hombre") "pct_hombre" else "pct_mujer"
    out <- joined |>
      dplyr::mutate(genero = g, origen_genero = "estimado")
    for (v in vars_to_split) {
      out[[v]] <- out[[v]] * out[[pct_col]]
    }
    out |>
      dplyr::select(ccaa, fecha, genero, origen_genero,
                    dplyr::any_of(c("origen", vars_to_split, "pct_mujeres_benef")))
  })

  long |>
    dplyr::mutate(dplyr::across(where(is.numeric), ~ round(.x, 4))) |>
    dplyr::arrange(ccaa, fecha, genero)
}

# ===========================================================================
# Exportacion CSV / XLSX
# ===========================================================================

write_outputs <- function(cfg, global_df, gen_df) {
  csv_global <- file.path(cfg$load_dir, "ced_dependencia_global.csv")
  readr::write_csv2(to_utf8_df(global_df), csv_global)
  exported <- csv_global

  if (!is.null(gen_df)) {
    csv_gen <- file.path(cfg$load_dir, "ced_dependencia_gen.csv")
    readr::write_csv2(to_utf8_df(gen_df), csv_gen)
    exported <- c(exported, csv_gen)
  }

  if (requireNamespace("writexl", quietly = TRUE)) {
    sheets <- list(global = global_df)
    if (!is.null(gen_df)) sheets$gen <- gen_df
    xlsx_path <- file.path(cfg$load_dir, "ced_dependencia.xlsx")
    writexl::write_xlsx(sheets, xlsx_path)
    exported <- c(exported, xlsx_path)
    log_event("INFO", "Exportados CSV (global+gen) y XLSX")
  } else {
    log_event("WARN", "writexl no disponible; se omite XLSX")
  }

  exported
}

write_dataset_exports <- function(cfg, tables) {
  csv_dir <- file.path(cfg$load_dir, "tables_csv")
  ensure_dir(csv_dir)

  data_tables <- tables[vapply(tables, inherits, logical(1), "data.frame")]
  data_tables <- purrr::map(data_tables, normalize_load_table)
  exported <- purrr::imap_chr(data_tables, function(df, nm) {
    path <- file.path(csv_dir, paste0(sanitize_table_name(nm), ".csv"))
    readr::write_csv2(to_utf8_df(df), path)
    path
  })

  log_event("INFO", sprintf("Exportadas %d tablas auxiliares en %s", length(exported), csv_dir))
  invisible(exported)
}

# ===========================================================================
# Indices unicos + RLS (cuaderno §11.6) - se re-aplican tras cada DROP+RENAME
# ===========================================================================

apply_indices_and_rls <- function(con, schema, hub_tables = c("ced_dependencia_global", "ced_dependencia_gen")) {
  exists_table <- function(t) {
    res <- DBI::dbGetQuery(con, sprintf(
      "SELECT 1 FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s'",
      schema, t
    ))
    nrow(res) > 0
  }

  # Permiso a nivel de schema (sin esto PostgREST devuelve 401 'permission
  # denied for schema' aunque las tablas tengan GRANT SELECT y politicas RLS).
  DBI::dbExecute(con, sprintf('GRANT USAGE ON SCHEMA "%s" TO anon, authenticated', schema))

  if (exists_table("ced_dependencia_global")) {
    DBI::dbExecute(con, sprintf(
      'CREATE UNIQUE INDEX IF NOT EXISTS ced_dependencia_global_pk_idx
         ON "%s"."ced_dependencia_global" (ccaa, fecha, origen)',
      schema
    ))
    DBI::dbExecute(con, sprintf(
      'ALTER TABLE "%s"."ced_dependencia_global" ENABLE ROW LEVEL SECURITY', schema
    ))
    DBI::dbExecute(con, sprintf(
      'DROP POLICY IF EXISTS ced_dependencia_global_select_anon ON "%s"."ced_dependencia_global"', schema
    ))
    DBI::dbExecute(con, sprintf(
      'CREATE POLICY ced_dependencia_global_select_anon
         ON "%s"."ced_dependencia_global" FOR SELECT
         TO anon, authenticated USING (TRUE)', schema
    ))
    DBI::dbExecute(con, sprintf(
      'GRANT SELECT ON "%s"."ced_dependencia_global" TO anon, authenticated', schema
    ))
    log_event("DB", "Indice unico + RLS aplicados a ced_dependencia_global")
  }

  if (exists_table("ced_dependencia_gen")) {
    DBI::dbExecute(con, sprintf(
      'CREATE UNIQUE INDEX IF NOT EXISTS ced_dependencia_gen_pk_idx
         ON "%s"."ced_dependencia_gen" (ccaa, fecha, genero, origen)',
      schema
    ))
    DBI::dbExecute(con, sprintf(
      'ALTER TABLE "%s"."ced_dependencia_gen" ENABLE ROW LEVEL SECURITY', schema
    ))
    DBI::dbExecute(con, sprintf(
      'DROP POLICY IF EXISTS ced_dependencia_gen_select_anon ON "%s"."ced_dependencia_gen"', schema
    ))
    DBI::dbExecute(con, sprintf(
      'CREATE POLICY ced_dependencia_gen_select_anon
         ON "%s"."ced_dependencia_gen" FOR SELECT
         TO anon, authenticated USING (TRUE)', schema
    ))
    DBI::dbExecute(con, sprintf(
      'GRANT SELECT ON "%s"."ced_dependencia_gen" TO anon, authenticated', schema
    ))
    log_event("DB", "Indice unico + RLS aplicados a ced_dependencia_gen")
  }
}

# ===========================================================================
# Carga atomica a Supabase (staging + RENAME)
# ===========================================================================

write_supabase_tables <- function(cfg, tables) {
  require_packages(c("DBI", "RPostgres"))
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  schema <- cfg$db$schema
  DBI::dbExecute(con, sprintf('CREATE SCHEMA IF NOT EXISTS "%s"', schema))

  tables_to_upload <- tables[vapply(tables, inherits, logical(1), "data.frame")]

  purrr::iwalk(tables_to_upload, function(df, nombre) {
    target  <- sanitize_table_name(nombre)
    staging <- sprintf("%s_staging_%s", target, format(Sys.time(), "%Y%m%d%H%M%S"))
    df_clean <- to_utf8_df(df)

    DBI::dbBegin(con)
    tryCatch({
      DBI::dbWriteTable(
        con, DBI::Id(schema = schema, table = staging),
        df_clean, overwrite = TRUE
      )
      DBI::dbExecute(con, sprintf('DROP TABLE IF EXISTS "%s"."%s"', schema, target))
      DBI::dbExecute(con, sprintf('ALTER TABLE "%s"."%s" RENAME TO "%s"', schema, staging, target))
      DBI::dbCommit(con)
      log_event("DB", sprintf("Tabla %s.%s cargada (%d filas)", schema, target, nrow(df_clean)))
    }, error = function(e) {
      DBI::dbRollback(con)
      log_event("ERROR", sprintf("Fallo cargando %s: %s", target, conditionMessage(e)))
    })
  })

}

# ===========================================================================
# Tablas hub: upsert idempotente en la capa de publicacion (incidencia 2026-10)
# ===========================================================================
# Las tablas que lee la web se actualizan fila a fila, nunca con DROP/TRUNCATE:
#   1. Una fila 'real' nueva sustituye a la 'proyeccion' del mismo mes.
#   2. Filas con la misma clave y el mismo origen se actualizan (revisiones
#      del IMSERSO de meses ya publicados).
#   3. Una 'proyeccion' nunca pisa una fila 'real'.
#   4. Las filas que no existian se insertan.
#   5. Se borran solo proyecciones que el nuevo modelo ya no genera.
# Las filas 'real' que no vienen en la carga no se tocan.

publication_keys <- list(
  ced_dependencia_global = c("ccaa", "fecha"),
  ced_dependencia_gen    = c("ccaa", "fecha", "genero")
)

qualified_name <- function(con, schema, table) {
  paste0(DBI::dbQuoteIdentifier(con, schema), ".", DBI::dbQuoteIdentifier(con, table))
}

table_columns <- function(con, schema, table) {
  DBI::dbGetQuery(con, sprintf(
    "SELECT column_name FROM information_schema.columns
      WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position",
    DBI::dbQuoteString(con, schema), DBI::dbQuoteString(con, table)
  ))$column_name
}

upsert_publication_table <- function(con, schema, table, df, keys) {
  target_cols <- table_columns(con, schema, table)
  if (!length(target_cols)) {
    stop(sprintf("No existe %s.%s: crea la tabla antes de cargar", schema, table), call. = FALSE)
  }
  sobran <- setdiff(names(df), target_cols)
  faltan <- setdiff(target_cols, names(df))
  if (length(sobran)) log_event("WARN", sprintf("%s: columnas no presentes en destino, no se cargan: %s", table, paste(sobran, collapse = ", ")))
  if (length(faltan)) log_event("WARN", sprintf("%s: columnas del destino sin dato en la carga (quedan NULL en filas nuevas): %s", table, paste(faltan, collapse = ", ")))

  cols <- intersect(target_cols, names(df))
  assert_required_columns(df, c(keys, "origen"), label = table)
  assert_unique_keys(df, keys, label = table)
  if (any(!df$origen %in% c("real", "proyeccion"))) {
    stop(sprintf("%s: origen solo puede ser 'real' o 'proyeccion'", table), call. = FALSE)
  }

  tgt <- qualified_name(con, schema, table)
  tmp <- DBI::dbQuoteIdentifier(con, paste0("tmp_", table))
  qk <- DBI::dbQuoteIdentifier(con, keys)
  qc <- DBI::dbQuoteIdentifier(con, cols)
  key_match <- paste(sprintf("t.%s = s.%s", qk, qk), collapse = " AND ")
  set_cols <- setdiff(cols, c(keys, "origen"))
  set_clause <- paste(sprintf("%s = s.%s", DBI::dbQuoteIdentifier(con, set_cols),
                              DBI::dbQuoteIdentifier(con, set_cols)), collapse = ", ")
  dup_sql <- sprintf("SELECT count(*) AS n FROM (SELECT 1 FROM %s GROUP BY %s HAVING count(*) > 1) d",
                     tgt, paste(qk, collapse = ", "))
  real_sql <- sprintf("SELECT count(*) AS n FROM %s WHERE origen = 'real'", tgt)

  DBI::dbWriteTable(con, paste0("tmp_", table), to_utf8_df(df[cols]), temporary = TRUE, overwrite = TRUE)

  DBI::dbBegin(con)
  res <- tryCatch({
    reales_antes <- DBI::dbGetQuery(con, real_sql)$n
    n <- c(
      proyeccion_sustituida = DBI::dbExecute(con, sprintf(
        "DELETE FROM %s t USING %s s WHERE %s AND t.origen = 'proyeccion' AND s.origen = 'real'",
        tgt, tmp, key_match)),
      actualizadas = DBI::dbExecute(con, sprintf(
        "UPDATE %s t SET %s FROM %s s WHERE %s AND t.origen = s.origen",
        tgt, set_clause, tmp, key_match)),
      insertadas = DBI::dbExecute(con, sprintf(
        "INSERT INTO %s (%s) SELECT %s FROM %s s
          WHERE NOT EXISTS (SELECT 1 FROM %s t WHERE %s)",
        tgt, paste(qc, collapse = ", "), paste(paste0("s.", qc), collapse = ", "), tmp, tgt, key_match)),
      proyeccion_obsoleta = DBI::dbExecute(con, sprintf(
        "DELETE FROM %s t WHERE t.origen = 'proyeccion'
            AND NOT EXISTS (SELECT 1 FROM %s s WHERE %s AND s.origen = 'proyeccion')",
        tgt, tmp, key_match))
    )

    duplicadas <- DBI::dbGetQuery(con, dup_sql)$n
    reales_despues <- DBI::dbGetQuery(con, real_sql)$n
    if (duplicadas > 0) stop(sprintf("quedarian %d claves duplicadas (real y proyeccion conviviendo)", duplicadas))
    if (reales_despues < reales_antes) stop(sprintf("se perderian filas reales (%d -> %d)", reales_antes, reales_despues))

    DBI::dbCommit(con)
    n
  }, error = function(e) {
    DBI::dbRollback(con)
    stop(sprintf("Upsert de %s.%s revertido: %s", schema, table, conditionMessage(e)), call. = FALSE)
  })
  DBI::dbExecute(con, sprintf("DROP TABLE IF EXISTS %s", tmp))

  log_event("DB", sprintf(
    "%s.%s: %s", schema, table,
    paste(sprintf("%s=%d", names(res), as.integer(res)), collapse = " | ")
  ))
  invisible(res)
}

# Copia las tablas publicadas en el esquema de staging (sin permisos para
# anon/authenticated) para ensayar sobre ella exactamente el mismo upsert.
prepare_staging_copy <- function(con, cfg, table) {
  pub <- qualified_name(con, cfg$db$publish_schema, table)
  stg <- qualified_name(con, cfg$db$staging_schema, table)
  DBI::dbExecute(con, sprintf("CREATE SCHEMA IF NOT EXISTS %s", DBI::dbQuoteIdentifier(con, cfg$db$staging_schema)))
  DBI::dbExecute(con, sprintf("DROP TABLE IF EXISTS %s", stg))
  DBI::dbExecute(con, sprintf("CREATE TABLE %s (LIKE %s INCLUDING ALL)", stg, pub))
  DBI::dbExecute(con, sprintf("INSERT INTO %s SELECT * FROM %s", stg, pub))
  DBI::dbExecute(con, sprintf("ALTER TABLE %s ENABLE ROW LEVEL SECURITY", stg))
}

# Resumen de lo que cambiaria en produccion: filas por mes y origen antes y
# despues, y diferencias en meses reales que ya estaban publicados.
summarise_staging_diff <- function(con, cfg, table, keys) {
  antes <- DBI::dbReadTable(con, DBI::Id(schema = cfg$db$publish_schema, table = table))
  despues <- DBI::dbReadTable(con, DBI::Id(schema = cfg$db$staging_schema, table = table))

  cuenta <- function(df, sufijo) {
    df |>
      dplyr::count(fecha, origen, name = "filas") |>
      tidyr::pivot_wider(names_from = origen, values_from = filas, values_fill = 0,
                         names_prefix = paste0(sufijo, "_"))
  }
  por_mes <- dplyr::full_join(cuenta(antes, "antes"), cuenta(despues, "despues"), by = "fecha") |>
    dplyr::mutate(dplyr::across(-fecha, ~ tidyr::replace_na(.x, 0L))) |>
    dplyr::arrange(fecha)

  num_cols <- setdiff(intersect(names(antes)[vapply(antes, is.numeric, logical(1))], names(despues)), keys)
  comunes <- dplyr::inner_join(
    antes |> dplyr::filter(origen == "real"),
    despues |> dplyr::filter(origen == "real"),
    by = keys, suffix = c(".antes", ".despues")
  )
  revisiones <- purrr::map_dfr(num_cols, function(v) {
    a <- comunes[[paste0(v, ".antes")]]; d <- comunes[[paste0(v, ".despues")]]
    cambia <- (is.na(a) != is.na(d)) | (!is.na(a) & !is.na(d) & abs(a - d) > 1e-6 * pmax(1, abs(a)))
    if (!any(cambia)) return(NULL)
    tibble::tibble(
      variable = v, filas_cambian = sum(cambia),
      meses = paste(sort(unique(format(comunes$fecha[cambia], "%Y-%m"))), collapse = " "),
      max_dif_abs = suppressWarnings(max(abs(a - d)[cambia], na.rm = TRUE))
    )
  })

  out_dir <- file.path(cfg$load_dir, "staging")
  ensure_dir(out_dir)
  readr::write_csv2(por_mes, file.path(out_dir, sprintf("%s_filas_por_mes.csv", table)))
  readr::write_csv2(revisiones, file.path(out_dir, sprintf("%s_revisiones_meses_reales.csv", table)))
  log_event("INFO", sprintf("%s: resumen de staging en %s", table, out_dir))
  invisible(list(por_mes = por_mes, revisiones = revisiones))
}

write_publication_tables <- function(cfg, hub_tables) {
  require_packages(c("DBI", "RPostgres"))
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  target_schema <- if (identical(cfg$db_target, "produccion")) cfg$db$publish_schema else cfg$db$staging_schema
  log_event("DB", sprintf("Destino de las tablas hub: %s (%s)", target_schema, cfg$db_target))

  for (table in names(hub_tables)) {
    if (identical(cfg$db_target, "staging")) prepare_staging_copy(con, cfg, table)
    upsert_publication_table(con, target_schema, table, hub_tables[[table]], publication_keys[[table]])
    if (identical(cfg$db_target, "staging")) {
      summarise_staging_diff(con, cfg, table, publication_keys[[table]])
    }
  }

  if (identical(cfg$db_target, "produccion")) apply_indices_and_rls(con, cfg$db$publish_schema)
}

# Comprobacion de solo lectura: lo que ve la web. Se ejecuta aunque el cron no
# escriba, porque fue justo ahi donde la incidencia 2026-10 paso desapercibida:
# la extraccion llegaba a agosto y la tabla publicada seguia en marzo.
check_published_freshness <- function(cfg) {
  if (!nzchar(cfg$db$host) || !nzchar(cfg$db$user) || !nzchar(cfg$db$password)) {
    log_event("INFO", "Sin credenciales: no se comprueba la antiguedad de la tabla publicada")
    return(invisible(NULL))
  }
  tryCatch({
    con <- connect_supabase(cfg)
    on.exit(DBI::dbDisconnect(con), add = TRUE)
    ultimo <- DBI::dbGetQuery(con, sprintf(
      "SELECT max(fecha) AS ultimo FROM %s WHERE origen = 'real'",
      qualified_name(con, cfg$db$publish_schema, "ced_dependencia_global")
    ))$ultimo
    check_freshness(ultimo, sprintf("Tabla publicada %s.ced_dependencia_global", cfg$db$publish_schema))
  }, error = function(e) {
    log_event("WARN", sprintf("No se pudo comprobar la tabla publicada: %s", conditionMessage(e)))
  })
}

# ===========================================================================
# Pipeline principal: run_carga
# ===========================================================================

run_carga <- function(cfg) {
  log_event("STEP", "Iniciando carga (cuaderno v2 §11.4)")

  # 1. Cargar artefactos de modelado
  model_rds <- list.files(cfg$model_dir, pattern = "\\.rds$", full.names = TRUE)
  modeled <- purrr::map(model_rds, readRDS)
  names(modeled) <- gsub("\\.rds$", "", basename(model_rds))
  log_event("INFO", sprintf("Cargados %d artefactos de modelado", length(modeled)))

  # 2. Tabla principal: ced_dependencia_global (10 indicadores + raws + proyeccion)
  ced_global <- prepare_global_table(modeled)
  log_event("INFO", sprintf("ced_dependencia_global: %d filas | %d CCAA",
                            nrow(ced_global), dplyr::n_distinct(ced_global$ccaa)))

  # 3. Tabla de genero: ced_dependencia_gen (estimacion via palanca §6.3)
  ced_gen <- prepare_gen_table(modeled)
  if (!is.null(ced_gen)) {
    log_event("INFO", sprintf("ced_dependencia_gen: %d filas | flag origen_genero='estimado'",
                              nrow(ced_gen)))
  }

  # 4. Logging de calidad
  log_series_coverage(ced_global, "ced_dependencia_global")
  log_table_quality(ced_global, "ced_dependencia_global", c("fecha"))
  if (!is.null(ced_gen)) log_series_coverage(ced_gen, "ced_dependencia_gen")

  # 5. Exportar CSV (global + gen) y XLSX
  exported_files <- write_outputs(cfg, ced_global, ced_gen)
  write_dataset_exports(cfg, modeled)

  # 6. Carga a Supabase (con --with-db=true)
  #    Tablas hub -> upsert en canendatos (produccion) o ced_staging (staging).
  #    Tablas intermedias -> esquema de trabajo 'saad', solo en produccion.
  if (isTRUE(cfg$with_db)) {
    hub <- list(ced_dependencia_global = ced_global)
    if (!is.null(ced_gen)) hub[["ced_dependencia_gen"]] <- ced_gen
    write_publication_tables(cfg, hub)

    if (identical(cfg$db_target, "produccion") && isTRUE(cfg$aux_tables)) {
      write_supabase_tables(cfg, modeled)
    } else {
      log_event("INFO", "Tablas intermedias de 'saad' no se escriben (staging o --aux-tables=false)")
    }
    log_event("DB", sprintf("Carga en Supabase completada (%s)", cfg$db_target))
  } else {
    log_event("INFO", "Carga a Supabase omitida (--with-db=false)")
  }
  check_published_freshness(cfg)

  # 7. Verificacion
  purrr::walk(exported_files, assert_file_exists)

  log_event("OK", "Carga completada")
  invisible(list(global = ced_global, gen = ced_gen))
}
