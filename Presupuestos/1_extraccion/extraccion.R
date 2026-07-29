# ============================================================
# 1_extraccion/extraccion.R — Descarga las fuentes declaradas en
# fuentes.yml, calcula SHA-256, persiste un manifest idempotente y
# convierte cada fuente a un staging tidy de gasto.
#
# Implementa los principios del cuaderno (§2.2 y §2.4):
#   - idempotencia por SHA-256 (skip si el hash coincide con la captura previa)
#   - manifest.jsonl con metadatos auditables
#   - delegación a Python para PDFs (extract_pdf.py)
#   - registro de capa (hacienda | autonomica) y consolidación
#
# Salidas:
#   1_extraccion/manifest.rds         — manifest validado
#   1_extraccion/staging_gasto.rds    — tabla tidy lista para transformar
#   1_extraccion/manifest.jsonl       — manifest persistente (auditoría)
# ============================================================

suppressPackageStartupMessages({
  require_packages(c("yaml","httr","fs","digest","dplyr","readr","jsonlite","tibble","purrr"))
  library(dplyr)
})

.read_fuentes_yml <- function(path) {
  fuentes <- yaml::read_yaml(path)
  defaults <- fuentes$defaults %||% list()
  fuentes$defaults <- NULL
  attr(fuentes, "defaults") <- defaults
  fuentes
}

.descargar <- function(url, destino, user_agent = NULL, timeout = 60, retries = 3) {
  for (i in seq_len(retries)) {
    res <- tryCatch(
      httr::GET(url,
                httr::user_agent(user_agent %||% "ODESOCAN-CanariasEnDatos/0.1"),
                httr::timeout(timeout),
                httr::write_disk(destino, overwrite = TRUE)),
      error = function(e) e
    )
    if (inherits(res, "response") && httr::status_code(res) < 400) {
      return(invisible(list(ok = TRUE, status = httr::status_code(res))))
    }
    log_event("WARN", sprintf("Reintento %d/%d %s", i, retries, url))
    Sys.sleep(2 ^ i)
  }
  list(ok = FALSE, status = NA_integer_)
}

.local_fallback <- function(cfg, ccaa, ejercicio, alias, ext) {
  # Permite probar/desarrollar sin acceso a internet: si en fuentes/raw/ ya
  # hay un fichero del mismo alias, se reutiliza. La sec. 2.2 del cuaderno
  # prevé este caso para entornos sin red.
  candidato <- file.path(cfg$raw_dir, ccaa, ejercicio, paste0(alias, ext))
  if (file.exists(candidato)) return(candidato)
  NA_character_
}

.parsear_csv_xlsx <- function(path, meta) {
  cols_min <- c("codigo","denominacion","importe_eur")
  if (tolower(tools::file_ext(path)) %in% c("csv","tsv")) {
    # Detección heurística de locale: lee 30 filas como texto y decide si el
    # decimal es "," o "." según el patrón mayoritario.
    sample_lines <- tryCatch(readLines(path, n = 30, warn = FALSE), error = function(e) character())
    has_es_pattern <- any(grepl("\\d\\.\\d{3}(\\.|,)\\d", sample_lines)) ||
                       any(grepl("\\d+,\\d{1,2}([^0-9]|$)", sample_lines))
    locale_use <- if (has_es_pattern) {
      readr::locale(decimal_mark = ",", grouping_mark = ".")
    } else {
      readr::locale(decimal_mark = ".", grouping_mark = "")
    }
    df <- tryCatch(
      readr::read_delim(path, show_col_types = FALSE, locale = locale_use,
                         guess_max = 5000),
      error = function(e) readr::read_csv(path, show_col_types = FALSE)
    )
  } else if (tolower(tools::file_ext(path)) %in% c("xlsx","xls")) {
    require_packages("readxl")
    df <- readxl::read_excel(path)
  } else {
    return(NULL)
  }
  df <- as.data.frame(df)
  names(df) <- tolower(trimws(names(df)))

  # heurísticas de normalización: aceptamos sinónimos habituales
  ren <- c(
    "codigo" = "codigo", "código" = "codigo", "programa" = "codigo", "cod" = "codigo",
    "denominacion" = "denominacion", "denominación" = "denominacion",
    "descripcion" = "denominacion", "descripción" = "denominacion",
    "concepto" = "denominacion", "nombre" = "denominacion",
    "importe_eur" = "importe_eur", "importe" = "importe_eur",
    "credito_inicial" = "importe_eur", "credito" = "importe_eur",
    "presupuesto" = "importe_eur", "euros" = "importe_eur"
  )
  for (k in names(ren)) if (k %in% names(df) && !(ren[[k]] %in% names(df))) names(df)[names(df) == k] <- ren[[k]]

  if (!all(cols_min %in% names(df))) return(NULL)

  df$codigo <- as.character(df$codigo)
  df$denominacion <- as.character(df$denominacion)
  df$importe_eur <- parse_number_es(df$importe_eur)
  df <- df[!is.na(df$importe_eur), c(cols_min, setdiff(names(df), cols_min)), drop = FALSE]
  df
}

.parsear_hacienda <- function(cfg, src, dest_parquet, anio) {
  # Para la capa Hacienda usamos un helper Python dedicado (extract_hacienda.py).
  # Si el operador ha colocado un XLSX/CSV adicional en
  # fuentes/raw/hacienda/<anio>/, se prefiere ése sobre el HTML del visor.
  script <- file.path(cfg$extraction_dir, "extract_hacienda.py")
  if (!file.exists(script)) return(NULL)

  # Busca XLSX/CSV en fuentes/raw/hacienda/<anio>/ — si el ejercicio es un
  # rango ("2002-2026"), busca recursivamente en todos los subdirs.
  hacienda_root <- file.path(cfg$raw_dir, "hacienda")
  candidates <- character(0)
  if (grepl("-", anio)) {
    candidates <- list.files(hacienda_root, pattern = "\\.(xlsx|csv)$",
                              recursive = TRUE, full.names = TRUE, ignore.case = TRUE)
  } else {
    anio_dir <- file.path(hacienda_root, anio)
    if (dir.exists(anio_dir)) {
      candidates <- list.files(anio_dir, pattern = "\\.(xlsx|csv)$",
                                full.names = TRUE, ignore.case = TRUE)
    }
  }
  if (length(candidates) == 0) {
    log_event("INFO", sprintf("Sin XLSX/CSV en %s — capa Hacienda solo manifest", hacienda_root))
    return(NULL)
  }

  use_csv <- !requireNamespace("arrow", quietly = TRUE)
  # Acumula TODOS los XLSX/CSV de la capa Hacienda. Cada fichero per-CCAA
  # aporta sus 9 capítulos de gasto; con la serie SGCIEF son 17 CCAA × N años,
  # así que hay que rbind-ear todos los candidatos, no quedarse con el primero.
  acumulado <- list()
  for (cand in candidates) {
    # Si anio es un rango ("2002-2026"), extrae el año del nombre del fichero
    # o del directorio que lo contiene; si no, usa el primer año del rango.
    anio_efectivo <- if (grepl("^\\d{4}$", anio)) {
      anio
    } else {
      m <- regmatches(cand, regexpr("(?<![0-9])\\d{4}(?![0-9])", cand, perl = TRUE))
      if (length(m) > 0 && m != "") m else strsplit(anio, "-", fixed = TRUE)[[1]][1]
    }
    log_event("INFO", sprintf("Parseando capa Hacienda desde %s (anio=%s)",
                                basename(cand), anio_efectivo))
    # Salida por candidato: un fichero distinto por cada uno para no
    # sobrescribir el anterior antes de leerlo.
    out_target <- if (use_csv) {
      sub("\\.parquet$", sprintf("_%s.csv", tools::file_path_sans_ext(basename(cand))), dest_parquet)
    } else {
      sub("\\.parquet$", sprintf("_%s.parquet", tools::file_path_sans_ext(basename(cand))), dest_parquet)
    }
    res <- system2(cfg$python_bin,
                    args = c(shQuote(script),
                              "--mode", "parse",
                              "--input", shQuote(cand),
                              "--output", shQuote(out_target),
                              "--anio", as.character(anio_efectivo)),
                    stdout = TRUE, stderr = TRUE)
    exit <- attr(res, "status") %||% 0L
    if (identical(exit, 0L) || identical(exit, 0)) {
      if (file.exists(out_target)) {
        df_cand <- if (grepl("\\.csv$", out_target)) {
          tryCatch(utils::read.csv(out_target, stringsAsFactors = FALSE),
                   error = function(e) NULL)
        } else if (requireNamespace("arrow", quietly = TRUE)) {
          tryCatch(as.data.frame(arrow::read_parquet(out_target)),
                   error = function(e) NULL)
        } else NULL
        if (!is.null(df_cand) && nrow(df_cand) > 0) {
          acumulado[[length(acumulado) + 1L]] <- df_cand
        }
      }
    } else {
      log_event("WARN", sprintf("extract_hacienda.py exit=%s para %s — stdout: %s",
                                  exit, basename(cand), paste(head(res, 5), collapse=" | ")))
    }
  }
  if (length(acumulado) == 0) return(NULL)
  combinado <- dplyr::bind_rows(acumulado)
  log_event("INFO", sprintf("Capa Hacienda: %d filas de %d ficheros",
                              nrow(combinado), length(acumulado)))
  combinado
}

.parsear_pdf <- function(cfg, src, dest_parquet, ccaa, anio) {
  # Invoca el dispatcher CCAA-específico: python3 -m extractors --ccaa <id3> ...
  # Cada CCAA tiene su propio extractor en 1_extraccion/extractors/<id3>.py.
  use_csv <- !requireNamespace("arrow", quietly = TRUE)
  out_target <- if (use_csv) sub("\\.parquet$", ".csv", dest_parquet) else dest_parquet

  # Ejecuta el sub-pipeline CCAA: `python3 -m ccaa --ccaa <id3> ...`
  # Cada CCAA tiene su propia carpeta autocontenida en
  # 1_extraccion/ccaa/<id3>/ con extract.py + transform.py + correspondencias.yml.
  cwd_orig <- getwd()
  setwd(cfg$extraction_dir); on.exit(setwd(cwd_orig), add = TRUE)
  status <- system2(cfg$python_bin,
                    args = c("-m", "ccaa",
                             "--input",  shQuote(src),
                             "--output", shQuote(out_target),
                             "--ccaa",   ccaa,
                             "--anio",   as.character(anio)),
                    stdout = TRUE, stderr = TRUE)
  exit <- attr(status, "status") %||% 0L
  if (!is.null(exit) && !identical(exit, 0L) && !identical(exit, 0)) {
    log_event("WARN", sprintf("ccaa.%s exit=%s para %s", ccaa, exit, basename(src)))
    return(NULL)
  }
  if (!file.exists(out_target)) return(NULL)
  if (grepl("\\.csv$", out_target)) return(utils::read.csv(out_target, stringsAsFactors = FALSE))
  if (requireNamespace("arrow", quietly = TRUE)) arrow::read_parquet(out_target) else NULL
}

run_extraccion <- function(cfg) {
  log_event("INFO", "Iniciando extracción")
  fuentes <- .read_fuentes_yml(cfg$fuentes_yml)
  defaults <- attr(fuentes, "defaults")

  filtro_ccaa <- cfg$ccaa_filter
  filtro_year <- cfg$year_filter
  if (!is.null(filtro_year)) filtro_year <- as.character(filtro_year)

  manifest_jsonl <- file.path(cfg$logs_dir, "manifest.jsonl")
  ensure_dir(dirname(manifest_jsonl))

  manifest_prev <- if (file.exists(manifest_jsonl)) {
    tryCatch(jsonlite::stream_in(file(manifest_jsonl), verbose = FALSE),
             error = function(e) data.frame())
  } else data.frame()

  entradas <- list(); stagings <- list()

  for (cca in names(fuentes)) {
    if (!is.null(filtro_ccaa) && !(cca %in% strsplit(filtro_ccaa, ",", fixed = TRUE)[[1]])) next
    bloque <- fuentes[[cca]]
    if (is.null(bloque$ejercicios)) next

    for (ej in names(bloque$ejercicios)) {
      if (!is.null(filtro_year) && !(ej %in% filtro_year)) next
      for (alias in names(bloque$ejercicios[[ej]])) {
        meta <- bloque$ejercicios[[ej]][[alias]]
        if (is.null(meta$url) || is.null(meta$tipo)) next

        ext <- switch(meta$tipo, pdf=".pdf", csv=".csv", xlsx=".xlsx", html=".html", zip=".zip", ".bin")
        dest <- file.path(cfg$raw_dir, cca, ej, paste0(alias, ext))
        ensure_dir(dirname(dest))

        # 1) descarga o reutilización local
        if (isTRUE(cfg$dry_run)) {
          log_event("DRY", sprintf("Saltada descarga %s/%s/%s", cca, ej, alias))
          next
        }
        if (file.exists(dest) && !isTRUE(cfg$run_scraping)) {
          log_event("CACHE", sprintf("Reutilizado raw local %s", basename(dest)))
        } else {
          dl <- .descargar(meta$url, dest,
                           user_agent = defaults$user_agent,
                           timeout = defaults$timeout_s %||% 60,
                           retries = defaults$retries %||% 3)
          if (!isTRUE(dl$ok)) {
            fallback <- .local_fallback(cfg, cca, ej, alias, ext)
            if (!is.na(fallback)) {
              dest <- fallback
              log_event("LOCAL", sprintf("Usando fallback local %s", basename(dest)))
            } else {
              log_event("ERROR", sprintf("Descarga fallida %s/%s/%s (status=%s)",
                                          cca, ej, alias, dl$status))
              next
            }
          }
        }

        sha <- sha256_file(dest)
        size_bytes <- file.info(dest)$size

        prev_match <- if (is.data.frame(manifest_prev) && nrow(manifest_prev) > 0 &&
                          all(c("ccaa","ejercicio","alias","sha256") %in% names(manifest_prev))) {
          manifest_prev[manifest_prev$ccaa == cca &
                        as.character(manifest_prev$ejercicio) == as.character(ej) &
                        manifest_prev$alias == alias &
                        manifest_prev$sha256 == sha, , drop = FALSE]
        } else data.frame()

        skip <- nrow(prev_match) > 0
        if (skip) log_event("SKIP", sprintf("Hash coincide para %s/%s/%s — saltando parseo", cca, ej, alias))

        entrada <- list(
          ccaa = cca, ejercicio = as.character(ej), alias = alias, tipo = meta$tipo,
          capa = meta$capa %||% "autonomica",
          consolidacion = meta$consolidacion %||% "no_aplica",
          es_prorroga = isTRUE(meta$es_prorroga),
          url = meta$url, path_local = dest, sha256 = sha,
          size_bytes = as.numeric(size_bytes),
          fecha_captura_utc = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ", tz = "UTC"),
          skipped = skip
        )
        entradas[[length(entradas) + 1L]] <- entrada

        if (skip) next

        # 2) parseo según tipo (con desvío a parser Hacienda si capa==hacienda)
        df_raw <- NULL
        capa_meta <- meta$capa %||% "autonomica"
        if (capa_meta == "hacienda") {
          dest_pq <- file.path(cfg$extraction_dir, "_hacienda_cache", cca,
                                sprintf("%s_%s.parquet", ej, alias))
          ensure_dir(dirname(dest_pq))
          df_raw <- .parsear_hacienda(cfg, dest, dest_pq, ej)
        } else {
          # Para CUALQUIER tipo (pdf/csv/xlsx/html/zip) delega al dispatcher CCAA
          # específico. Cada extractor decide cómo procesar su formato.
          dest_pq <- file.path(cfg$extraction_dir, "_pdf_cache", cca,
                                sprintf("%s_%s.parquet", ej, alias))
          ensure_dir(dirname(dest_pq))
          df_raw <- .parsear_pdf(cfg, dest, dest_pq, cca, ej)
          # Si el dispatcher devolvió 0 filas y es CSV/XLSX, intenta el parser
          # genérico R (legado) como red de seguridad.
          if ((is.null(df_raw) || nrow(df_raw) == 0) && meta$tipo %in% c("csv","xlsx")) {
            df_raw <- .parsear_csv_xlsx(dest, meta)
          }
        }

        if (is.null(df_raw) || nrow(df_raw) == 0) {
          log_event("WARN", sprintf("Sin filas tras parseo %s/%s/%s", cca, ej, alias))
          next
        }

        # Asegura tipos para bind_rows entre fuentes heterogéneas
        if ("codigo" %in% names(df_raw)) df_raw$codigo <- as.character(df_raw$codigo)
        if ("denominacion" %in% names(df_raw)) df_raw$denominacion <- as.character(df_raw$denominacion)
        if ("importe_eur" %in% names(df_raw)) df_raw$importe_eur <- as.numeric(df_raw$importe_eur)
        if ("capitulo" %in% names(df_raw)) df_raw$capitulo <- suppressWarnings(as.integer(df_raw$capitulo))

        # ccaa_id3: si el parser ya lo trae (Hacienda multi-CCAA), respetarlo;
        # si no, viene del alias del fuentes.yml.
        if (!("ccaa_id3" %in% names(df_raw)) || all(is.na(df_raw$ccaa_id3)) ||
            all(df_raw$ccaa_id3 == "")) {
          df_raw$ccaa_id3 <- cca
        }
        df_raw$ccaa <- ced_id3_to_ccaa(df_raw$ccaa_id3)
        df_raw$ccaa[is.na(df_raw$ccaa)] <- df_raw$ccaa_id3[is.na(df_raw$ccaa)]
        # anio: respetar el del parser si ya viene (Hacienda); si no, derivar
        # del ejercicio del fuentes.yml. Si ej es un rango ("2002-2026"), usa
        # el primer año (anio inicial de la serie).
        ej_int <- suppressWarnings(as.integer(ej))
        if (is.na(ej_int)) ej_int <- suppressWarnings(as.integer(strsplit(ej, "-", fixed = TRUE)[[1]][1]))
        if ("anio" %in% names(df_raw)) {
          df_raw$anio <- suppressWarnings(as.integer(df_raw$anio))
          df_raw$anio[is.na(df_raw$anio)] <- ej_int
        } else {
          df_raw$anio <- ej_int
        }
        df_raw$capa           <- meta$capa %||% "autonomica"
        df_raw$consolidacion  <- meta$consolidacion %||% "no_aplica"
        df_raw$es_prorroga    <- isTRUE(meta$es_prorroga)
        df_raw$fuente_url     <- meta$url
        df_raw$fuente_sha256  <- sha
        df_raw$alias          <- alias
        df_raw$capitulo       <- df_raw$capitulo %||% NA_integer_
        df_raw$unidad_origen  <- df_raw$unidad_origen %||% "eur"

        stagings[[length(stagings) + 1L]] <- df_raw
        log_event("OK", sprintf("Parseo %s/%s/%s filas=%d", cca, ej, alias, nrow(df_raw)))
      }
    }
  }

  manifest <- if (length(entradas) > 0) {
    do.call(rbind, lapply(entradas, function(e) as.data.frame(e, stringsAsFactors = FALSE)))
  } else {
    data.frame()
  }
  staging <- if (length(stagings) > 0) {
    bind_rows(stagings)
  } else {
    tibble::tibble(codigo = character(0), denominacion = character(0),
                   importe_eur = numeric(0), ccaa = character(0),
                   ccaa_id3 = character(0), anio = integer(0),
                   capa = character(0), consolidacion = character(0),
                   es_prorroga = logical(0), fuente_url = character(0),
                   fuente_sha256 = character(0), alias = character(0))
  }

  # Persistencia manifest (acumulativo) + RDS de fase
  if (nrow(manifest) > 0) {
    con <- file(manifest_jsonl, open = "a")
    on.exit(close(con), add = TRUE)
    for (i in seq_len(nrow(manifest))) {
      cat(jsonlite::toJSON(as.list(manifest[i, ]), auto_unbox = TRUE, null = "null"),
          "\n", sep = "", file = con)
    }
  }

  save_named_rds(list(manifest = manifest, staging_gasto = staging),
                 dir_path = cfg$extraction_dir)

  log_event("OK", sprintf("Extracción terminada: %d fuentes, %d filas staging",
                            nrow(manifest), nrow(staging)))
  invisible(list(manifest = manifest, staging_gasto = staging))
}
