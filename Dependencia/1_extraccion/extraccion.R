# ===========================================================================
# extraccion.R -- Descarga y parseo de datos IMSERSO/SAAD
# ===========================================================================
# Fusiona las etapas 1 (scraping) y 2 (clasificacion de hojas) del pipeline
# original en una sola funcion run_extraccion(cfg).
# ===========================================================================

suppressPackageStartupMessages({
  require_packages(c(
    "stringr", "purrr", "readr", "fs",
    "dplyr", "readxl", "digest", "tidyr", "tibble"
  ))
  library(stringr)
  library(purrr)
  library(readr)
  library(fs)
  library(dplyr)
  library(readxl)
  library(digest)
  library(tidyr)
})

# ===========================================================================
# Helpers locales de extraccion
# ===========================================================================

safe_delay   <- function() Sys.sleep(runif(1, 0.25, 1.15))
safe_pause_l <- function() Sys.sleep(runif(1, 1.5, 3.5))

to_abs <- function(href, base_url) {
  ifelse(str_starts(href, "/"), paste0(base_url, href), href)
}

strip_uuid_tail <- function(url) {
  sub("/[0-9a-fA-F-]{32,36}$", "", url)
}

.eom_ym <- function(y, m) {
  if (is.na(y) || is.na(m) || m < 1 || m > 12) return(NA_character_)
  d <- as.Date(sprintf("%04d-%02d-01", y, m))
  format(seq(d, by = "1 month", length.out = 2)[2] - 1, "%Y%m%d")
}

.extract_ymd_flexible_scalar <- function(txt) {
  if (length(txt) == 0 || is.na(txt) || !nzchar(txt)) return(NA_character_)
  m <- stringr::str_match(txt, "(\\d{4})[-_/]?(\\d{1,2})[-_/]?(\\d{2})(?=(?:\\.(?:xls|xlsx|xlsm|xlsb)\\b)|[^0-9]|$)")
  if (!all(is.na(m))) return(sprintf("%04d%02d%02d", as.integer(m[2]), as.integer(m[3]), as.integer(m[4])))
  m <- stringr::str_match(txt, "(\\d{4})[-_/]?(\\d{1,2})(?=(?:\\.(?:xls|xlsx|xlsm|xlsb)\\b)|[^0-9]|$)")
  if (!all(is.na(m))) return(.eom_ym(as.integer(m[2]), as.integer(m[3])))
  NA_character_
}

extract_fecha_from <- function(x) {
  vapply(x, .extract_ymd_flexible_scalar, FUN.VALUE = character(1))
}

is_excel_ct <- function(ct) {
  if (is.null(ct)) return(FALSE)
  any(stringr::str_detect(
    tolower(ct),
    c("application/vnd\\.ms-excel",
      "application/vnd\\.openxmlformats-officedocument\\.spreadsheet\\.sheet",
      "application/vnd\\.ms-excel\\.sheet\\.binary\\.macroenabled",
      "application/octet-stream")
  ))
}

is_excel_ext <- function(u) {
  stringr::str_detect(tolower(u), "\\.(xls|xlsx|xlsm|xlsb)(\\b|\\?|#|/)")
}

ua_string <- "R (httr2) - IMSERSO unified scraper"

validate_excel_link <- function(u) {
  safe_delay()
  r <- tryCatch(
    request(u) |> req_user_agent(ua_string) |> req_method("HEAD") |> req_timeout(25) |> req_perform(),
    error = function(e) e
  )
  if (!inherits(r, "error") && resp_status(r) < 400) {
    ct <- resp_headers(r)[["content-type"]]
    return(is_excel_ct(ct) || is_excel_ext(u))
  }
  safe_delay()
  r2 <- tryCatch(
    request(u) |> req_user_agent(ua_string) |> req_range_bytes(0, 1024) |> req_timeout(25) |> req_perform(),
    error = function(e) e
  )
  if (!inherits(r2, "error") && resp_status(r2) < 400) {
    ct <- resp_headers(r2)[["content-type"]]
    return(is_excel_ct(ct) || is_excel_ext(u))
  }
  is_excel_ext(u)
}

download_file <- function(u, dest, referer) {
  safe_delay()
  req <- request(u) |>
    req_user_agent(ua_string) |>
    req_headers(Referer = referer, `Accept-Language` = "es-ES,es;q=0.9") |>
    req_timeout(seconds = 180) |>
    req_retry(max_tries = 6, backoff = ~ runif(1, 0.8, 2.2))
  r <- tryCatch(req_perform(req), error = function(e) e)
  if (inherits(r, "error")) {
    return(list(ok = FALSE, status = NA_integer_, bytes = NA_real_, note = paste("ERROR:", conditionMessage(r))))
  }
  status <- resp_status(r)
  if (status >= 200 && status < 300) {
    raw <- resp_body_raw(r)
    writeBin(raw, dest)
    cl <- resp_headers(r)[["content-length"]]
    bytes <- if (!is.null(cl)) suppressWarnings(as.numeric(cl)) else fs::file_info(dest)$size
    return(list(ok = TRUE, status = status, bytes = bytes, note = "Downloaded"))
  }
  list(ok = FALSE, status = status, bytes = NA_real_, note = "HTTP not OK")
}

sha1_file <- function(path) digest::digest(file = path, algo = "sha1")

dedupe_by_hash <- function(out_dir) {
  files <- fs::dir_ls(out_dir, regexp = "\\.(xls|xlsx|xlsm|xlsb)$", type = "file", recurse = FALSE)
  if (length(files) == 0) {
    return(tibble(file = character(), sha1 = character(), is_duplicate = logical(),
                  kept_as = character(), action = character(), new_path = character()))
  }
  df <- tibble(path = files, file = basename(files), sha1 = map_chr(files, sha1_file))
  choose_canonical <- function(subdf) {
    has_date <- stringr::str_detect(subdf$file, "\\d{8}")
    ord <- order(!has_date, nchar(subdf$file), subdf$file)
    subdf[ord, , drop = FALSE][1, , drop = FALSE]
  }
  chosen <- df |>
    group_by(sha1) |>
    group_modify(~ choose_canonical(.x)) |>
    ungroup() |>
    mutate(kept = TRUE)
  df2 <- df |>
    left_join(chosen |> select(sha1, kept_file = file), by = "sha1") |>
    mutate(is_duplicate = file != kept_file, kept_as = kept_file)
  dup_dir <- file.path(out_dir, "_duplicates")
  if (any(df2$is_duplicate)) dir_create(dup_dir)
  actions <- df2 |>
    mutate(
      action = if_else(is_duplicate, "moved_to_duplicates", "kept"),
      new_path = if_else(is_duplicate, file.path(dup_dir, file), file.path(out_dir, file))
    )
  to_move <- actions |> filter(is_duplicate)
  if (nrow(to_move) > 0) {
    purrr::pwalk(
      list(from = file.path(out_dir, to_move$file), to = to_move$new_path),
      function(from, to) if (fs::file_exists(from) && !fs::file_exists(to)) fs::file_move(from, to)
    )
  }
  actions |> select(file, sha1, is_duplicate, kept_as, action, new_path)
}

# ===========================================================================
# URLs alternativas por ano
# ===========================================================================

alt_urls <- list(
  "2018" = "https://imserso.es/-/informes-publicados-2028",
  "2023" = "https://imserso.es/-/2023",
  "2024" = "https://imserso.es/-/2024-1",
  "2025" = "https://imserso.es/-/2025-2",
  "2026" = "https://imserso.es/-/2026-3"
)

resolve_page_url <- function(yr, base_url) {
  yr <- as.integer(yr)
  candidates <- c(
    alt_urls[[as.character(yr)]],
    sprintf("https://imserso.es/-/%d", yr),
    sprintf("https://imserso.es/-/informes-publicados-%d", yr),
    sprintf("https://imserso.es/-/informes-estadisticos-%d", yr),
    sprintf("https://imserso.es/-/informes-sisaad-%d", yr),
    sprintf("https://imserso.es/-/informes-publicados-del-sisaad-%d", yr)
  ) |> unique() |> purrr::discard(is.null)

  for (u in candidates) {
    safe_delay()
    resp <- tryCatch(
      request(u) |> req_user_agent(ua_string) |> req_perform(),
      error = function(e) e
    )
    if (!inherits(resp, "error") && resp_status(resp) < 400) {
      return(list(url = u, resp = resp))
    }
  }
  NULL
}

# ===========================================================================
# Extraccion de enlaces Excel desde DOM
# ===========================================================================

extract_excel_links_from_dom <- function(page_resp, page_url, base_url) {
  html <- read_html(resp_body_string(page_resp))
  lis  <- html_elements(html, ".list-im ul > li")
  if (length(lis) == 0) return(tibble())

  out <- purrr::map_dfr(lis, function(li) {
    month_txt <- (li |> html_element("span.pdf") |> html_text2()) %||%
      (li |> html_element("span.xlsx") |> html_text2()) %||%
      NA_character_
    month_txt <- stringr::str_squish(month_txt)

    a_tag <- li |> html_element(
      xpath = ".//a[.//span[contains(@class,'xls') or contains(@class,'xlsx')]]"
    )
    if (is.na(a_tag)) {
      a_tag <- li |> html_element(
        xpath = ".//a[contains(@href,'.xls') or contains(@href,'.xlsx') or contains(@href,'.xlsm') or contains(@href,'.xlsb')]"
      )
    }
    href <- html_attr(a_tag, "href") %||% NA_character_

    tibble(month_txt = month_txt, href_rel = href)
  }) |>
    mutate(
      url_abs_uuid = to_abs(href_rel, base_url),
      url_abs      = strip_uuid_tail(url_abs_uuid),
      file_name    = basename(url_abs),
      fecha_ymd    = extract_fecha_from(file_name),
      has_excel_ext = is_excel_ext(url_abs),
      valid_link   = purrr::map_lgl(url_abs, validate_excel_link),
      periodo      = as.Date(fecha_ymd, "%Y%m%d")
    ) |>
    filter(!is.na(url_abs)) |>
    arrange(periodo)

  out
}

# ===========================================================================
# Lectura de hojas Excel
# ===========================================================================

safe_clean <- function(df) {
  df <- tibble::as_tibble(df, .name_repair = "unique")
  if (!requireNamespace("janitor", quietly = TRUE)) return(df)
  tryCatch(janitor::clean_names(df), error = function(e) df)
}

read_all_sheets_any <- function(path) {
  ext <- tolower(fs::path_ext(path))
  has_xlsb <- requireNamespace("readxlsb", quietly = TRUE)

  read_one <- function(sheet, fun) {
    tryCatch(fun(path, sheet = sheet),
             error = function(e) tibble(.leer_error = conditionMessage(e), .sheet = as.character(sheet)))
  }

  if (ext %in% c("xls", "xlsx", "xlsm")) {
    sheets <- tryCatch(readxl::excel_sheets(path), error = function(e) character(0))
    set_names(
      map(sheets, ~ safe_clean(read_one(.x, function(p, sheet) {
        readxl::read_excel(p, sheet = sheet, col_types = "text", .name_repair = "minimal", guess_max = 100000)
      }))),
      make.unique(sheets)
    )
  } else if (ext == "xlsb" && has_xlsb) {
    sheets <- tryCatch(readxlsb::workbook_sheets(path), error = function(e) character(0))
    set_names(
      map(sheets, ~ safe_clean(read_one(.x, function(p, sheet) {
        readxlsb::read_xlsb(p, sheet = sheet, col_types = "text")
      }))),
      make.unique(sheets)
    )
  } else {
    list()
  }
}

# ===========================================================================
# Scraping de un ano completo
# ===========================================================================

scrape_year <- function(yr, xls_dir, base_url) {
  log_event("SCRAPE", sprintf("Procesando ano %d", yr))
  out_dir <- file.path(xls_dir, as.character(yr))
  dir_create(out_dir)

  cached_files <- fs::dir_ls(out_dir, regexp = "\\.(xls|xlsx|xlsm|xlsb)$", type = "file", recurse = FALSE)
  cached_files <- cached_files[!grepl("/_duplicates/", cached_files, fixed = TRUE)]
  current_year <- as.integer(format(Sys.Date(), "%Y"))
  use_year_cache <- !isTRUE(getOption("dependencia.force_download", FALSE)) &&
    length(cached_files) > 0 &&
    yr < current_year

  if (use_year_cache) {
    log_event("CACHE", sprintf("Ano %d: usando %d archivos locales", yr, length(cached_files)))
    file_lists <- set_names(map(cached_files, read_all_sheets_any), basename(cached_files))
    fechas_arch <- extract_fecha_from(basename(cached_files))
    meses_arch  <- suppressWarnings(format(as.Date(fechas_arch, "%Y%m%d"), "%m"))
    meses_arch[is.na(meses_arch)] <- "00"
    meses_lbl <- sprintf("%02d", 1:12)
    tree <- lapply(c("00", meses_lbl), function(m) {
      sel <- which(meses_arch == m)
      if (length(sel) == 0) return(list())
      files_m <- basename(cached_files[sel])
      setNames(file_lists[files_m], files_m)
    })
    names(tree) <- c("00", meses_lbl)
    manifest_path <- file.path(out_dir, sprintf("manifest_imserso_xls_%d.csv", yr))
    manifest <- if (fs::file_exists(manifest_path)) readr::read_csv(manifest_path, show_col_types = FALSE) else tibble()
    return(list(year = yr, page = NA_character_, files = file_lists, by_month = tree, manifest = manifest))
  }

  require_packages(c("rvest", "httr2", "xml2"))
  library(rvest)
  library(httr2)
  library(xml2)
  hit <- resolve_page_url(yr, base_url)
  if (is.null(hit)) {
    log_event("WARN", sprintf("No se encontro pagina para %d", yr))
    return(NULL)
  }
  page_url <- hit$url
  resp <- hit$resp

  cand <- extract_excel_links_from_dom(resp, page_url, base_url)
  if (nrow(cand) == 0) {
    log_event("WARN", sprintf("Sin candidatos Excel en %s", page_url))
    return(NULL)
  }

  cand_ok <- cand |> filter(valid_link, has_excel_ext)
  if (nrow(cand_ok) == 0) {
    log_event("WARN", sprintf("Tras validacion no hay Excel en %d", yr))
    return(NULL)
  }

  cand_ok <- cand_ok |>
    mutate(
      ext = tools::file_ext(file_name),
      destino = if_else(
        !is.na(fecha_ymd) & nzchar(ext),
        paste0("estsisaad_", fecha_ymd, ".", ext),
        file_name
      ),
      dest_path = file.path(out_dir, destino)
    )

  results <- pmap_dfr(
    list(cand_ok$url_abs, cand_ok$dest_path, rep(page_url, nrow(cand_ok))),
    function(u, dest, ref) {
      info <- if (fs::file_exists(dest) && !isTRUE(getOption("dependencia.force_download", FALSE))) {
        list(ok = TRUE, status = NA_integer_, bytes = fs::file_info(dest)$size, note = "Existing local file")
      } else {
        download_file(u, dest, referer = ref)
      }
      tibble(url = u, file = basename(dest), ok = info$ok,
             status = info$status, bytes = info$bytes, note = info$note,
             path = dest)
    }
  )

  results <- results |>
    mutate(
      sha1 = if_else(ok & fs::file_exists(path), map_chr(path, sha1_file), NA_character_),
      year = yr,
      source_year_page = page_url,
      fetched_at = format(Sys.time(), tz = "Europe/Madrid")
    )
  write_csv(results, file.path(out_dir, sprintf("manifest_imserso_xls_%d.csv", yr)))

  dedup_report <- dedupe_by_hash(out_dir)
  if (nrow(dedup_report) > 0) {
    write_csv(dedup_report, file.path(out_dir, sprintf("dedupe_%d.csv", yr)))
  }

  xfiles <- fs::dir_ls(out_dir, regexp = "\\.(xls|xlsx|xlsm|xlsb)$", type = "file", recurse = FALSE)
  xfiles <- xfiles[!grepl("/_duplicates/", xfiles, fixed = TRUE)]
  if (length(xfiles) == 0) {
    log_event("WARN", sprintf("No quedan archivos tras deduplicar en %s", out_dir))
    return(NULL)
  }

  file_lists <- set_names(map(xfiles, read_all_sheets_any), basename(xfiles))

  fechas_arch <- extract_fecha_from(basename(xfiles))
  meses_arch  <- suppressWarnings(format(as.Date(fechas_arch, "%Y%m%d"), "%m"))
  meses_arch[is.na(meses_arch)] <- "00"

  meses_lbl <- sprintf("%02d", 1:12)
  tree <- lapply(c("00", meses_lbl), function(m) {
    sel <- which(meses_arch == m)
    if (length(sel) == 0) return(list())
    files_m <- basename(xfiles[sel])
    setNames(file_lists[files_m], files_m)
  })
  names(tree) <- c("00", meses_lbl)

  log_event("OK", sprintf("Ano %d: %d archivos, %d hojas totales",
                           yr, length(xfiles),
                           sum(map_int(file_lists, length))))

  list(
    year = yr,
    page = page_url,
    files = file_lists,
    by_month = tree,
    manifest = results
  )
}

# ===========================================================================
# Patrones por hoja (corte 2023: pipeline activo, formato xlsx granular)
# ===========================================================================

benpresaad_pattern_fn <- function(yr) {
  # Desde 2023 IMSERSO publica las beneficiarias bajo "benefefect_pre"
  "^\\s*\\d*\\s*(benefect[_-]?pre|benef\\s*efect[_-]?pre|benpresaad)\\s*$"
}

# Hojas activas (>=2023). Cada patron casa por nombre normalizado de hoja.
sheet_patterns <- list(
  solsaad             = "sol\\s*_?-?\\s*saad",
  perfsaad            = "^\\s*\\d*\\s*perfsaad\\s*$",
  dictsaad            = "dict\\s*_?-?\\s*saad",
  perfcuidador_ccaa   = "perfcuidador.*ccaa",
  tiempo_espera       = "tiempo\\s*espera",
  pendientes_resol    = "^\\s*\\d*\\s*pendresol\\s*$",
  pendientes_prest    = "^\\s*\\d*\\s*pendprest\\s*$",
  ppd_xls             = "solcasaadpot",   # 22solcasaadpot: poblacion + PPD por CCAA
  # 12BenefEfect (sin sufijo _pre): tabla completa con desglose
  #   personas_con_pia | con prestacion efectiva | pendientes de prestacion efectiva
  # Necesaria para el limbo de prestaciones (cuaderno v2 §7.4 - tres limbos).
  # El '$' final excluye explicitamente la sub-hoja '12BenefEfect_pre'.
  benefect_full       = "^\\s*\\d*\\s*benef[\\s_-]?efect\\s*$"
)

# ===========================================================================
# Funcion principal: run_extraccion
# ===========================================================================

run_extraccion <- function(cfg) {
  log_event("STEP", "Iniciando extraccion IMSERSO")
  options(dependencia.force_download = isTRUE(cfg$force_download))

  # --- Sub-paso 1: Scraping (cuaderno v2: corte 2023) ---
  years <- cfg$saad_years
  if (any(years < cfg$pipeline_start_year)) {
    log_event(
      "WARN",
      sprintf("Anios anteriores a %d quedan fuera del pipeline activo (cuaderno v2 §2)",
              cfg$pipeline_start_year)
    )
    years <- years[years >= cfg$pipeline_start_year]
  }
  all_years <- set_names(vector("list", length(years)), years)

  for (i in seq_along(years)) {
    safe_pause_l()
    all_years[[i]] <- scrape_year(years[i], cfg$xls_dir, cfg$base_url)
  }

  saad_by_year_month <- setNames(
    lapply(all_years, function(x) if (is.null(x)) list() else x$by_month),
    names(all_years)
  )

  log_event("INFO", sprintf("Extraccion completada: %d anios procesados", length(years)))

  # --- Sub-paso 2: Clasificacion de hojas ---
  log_event("INFO", "Clasificando hojas por tipo (matriz cuaderno §7)")

  solsaad <- extract_sheet_by_pattern(saad_by_year_month, sheet_patterns$solsaad)
  log_event("INFO", sprintf("solsaad: %d periodos", length(solsaad)))

  perfsaad <- extract_sheet_by_pattern(saad_by_year_month, sheet_patterns$perfsaad)
  log_event("INFO", sprintf("perfsaad: %d periodos", length(perfsaad)))

  dictsaad <- extract_sheet_by_pattern(saad_by_year_month, sheet_patterns$dictsaad)
  log_event("INFO", sprintf("dictsaad: %d periodos", length(dictsaad)))

  benpresaad <- extract_sheet_by_pattern(
    saad_by_year_month,
    pattern = NULL,
    year_pattern_fn = benpresaad_pattern_fn
  )
  log_event("INFO", sprintf("benpresaad: %d periodos", length(benpresaad)))

  perfcuidador_ccaa <- extract_sheet_by_pattern(
    saad_by_year_month, sheet_patterns$perfcuidador_ccaa
  )
  log_event("INFO", sprintf("perfcuidador_ccaa: %d periodos", length(perfcuidador_ccaa)))

  tiempo_espera <- extract_sheet_by_pattern(
    saad_by_year_month, sheet_patterns$tiempo_espera
  )
  log_event("INFO", sprintf("tiempo_espera: %d periodos", length(tiempo_espera)))

  pendientes_resol <- extract_sheet_by_pattern(
    saad_by_year_month, sheet_patterns$pendientes_resol
  )
  pendientes_prest <- extract_sheet_by_pattern(
    saad_by_year_month, sheet_patterns$pendientes_prest
  )
  pendsaad <- list(resol = pendientes_resol, prest = pendientes_prest)
  log_event("INFO", sprintf("pendsaad: resol=%d periodos | prest=%d periodos",
                            length(pendientes_resol), length(pendientes_prest)))

  ppd_xls <- extract_sheet_by_pattern(saad_by_year_month, sheet_patterns$ppd_xls)
  log_event("INFO", sprintf("ppd_xls (fallback): %d periodos", length(ppd_xls)))

  benefect_full <- extract_sheet_by_pattern(
    saad_by_year_month, sheet_patterns$benefect_full
  )
  log_event("INFO", sprintf("benefect_full (12BenefEfect): %d periodos",
                            length(benefect_full)))

  # --- Guardar outputs ---
  outputs <- list(
    saad_by_year_month = saad_by_year_month,
    solsaad           = solsaad,
    perfsaad          = perfsaad,
    dictsaad          = dictsaad,
    benpresaad        = benpresaad,
    perfcuidador_ccaa = perfcuidador_ccaa,
    tiempo_espera     = tiempo_espera,
    pendsaad          = pendsaad,
    ppd_xls           = ppd_xls,
    benefect_full     = benefect_full
  )

  save_named_rds(outputs, cfg$extraction_dir)

  log_event("OK", "Extraccion completada y guardada")
  invisible(outputs)
}
