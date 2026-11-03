# ===========================================================================
# transformacion.R -- Limpieza, normalizacion CCAA y enriquecimiento PPD
# ===========================================================================
# Refactoriza las etapas 3 (3_transformacion.R ~3949 lineas) y
# 4 (4_transformacion2.R ~831 lineas) del pipeline original.
# ===========================================================================

suppressPackageStartupMessages({
  require_packages(c(
    "dplyr", "purrr", "stringr", "readr", "tibble",
    "stringi", "tidyr", "lubridate"
  ))
  library(dplyr)
  library(purrr)
  library(stringr)
  library(readr)
  library(tibble)
  library(stringi)
  library(tidyr)
  library(lubridate)
})

# ===========================================================================
# Helpers internos de transformacion
# ===========================================================================

norm_key_local <- function(x) {
  x |>
    as.character() |>
    enc2utf8() |>
    stringr::str_replace_all("\u00AD|\u200B", "") |>
    stringi::stri_replace_all_regex("[\\u00A0\\u202F\\t]", " ") |>
    stringr::str_trim() |>
    stringr::str_replace_all("\\s+", " ") |>
    stringi::stri_trans_general("Latin-ASCII") |>
    tolower()
}

dehyphenate_soft <- function(x) {
  x <- gsub("\u00AD", "", x, useBytes = TRUE)
  gsub("(?<=\\p{L})-\\s*(?=\\p{L})", "", x, perl = TRUE)
}

col_signature <- function(x, nhead = 40) {
  v <- head(as.character(x), nhead)
  v <- dehyphenate_soft(v)
  v <- norm_txt(v)
  paste(unique(v[!is.na(v) & v != ""]), collapse = " | ")
}

is_number_col <- function(sig_key) {
  has_n <- str_detect(sig_key, "\\b(n[o\u00BA]?\\.?|num(\\.?|ero)?|n\\.?\\s*o|numero|n\\.)\\b")
  has_p <- str_detect(sig_key, "%|\\bporcentaje\\b")
  has_n & !has_p
}

is_percent_col <- function(sig_key) {
  str_detect(sig_key, "%|\\bporcentaje\\b")
}

parse_num_es_vec <- function(v) {
  x <- stringr::str_squish(as.character(v))
  x[x %in% c("", "NA", "N/A", "n.d.", "-", "NULL")] <- NA_character_
  x <- stringr::str_replace_all(x, "%", "")

  out <- rep(NA_real_, length(x))
  has_comma <- !is.na(x) & stringr::str_detect(x, ",")
  has_dot <- !is.na(x) & !has_comma & stringr::str_detect(x, "\\.")

  out[has_comma] <- suppressWarnings(as.numeric(
    stringr::str_replace_all(stringr::str_replace_all(x[has_comma], "\\.", ""), ",", ".")
  ))

  dot_idx <- which(has_dot)
  dot_values <- x[dot_idx]
  dot_is_grouping <- stringr::str_detect(dot_values, "^[-+]?\\d{1,3}(\\.\\d{3})+$")
  out[dot_idx[dot_is_grouping]] <- suppressWarnings(as.numeric(stringr::str_replace_all(dot_values[dot_is_grouping], "\\.", "")))
  out[dot_idx[!dot_is_grouping]] <- suppressWarnings(as.numeric(dot_values[!dot_is_grouping]))

  plain <- !is.na(x) & !has_comma & !has_dot
  out[plain] <- suppressWarnings(as.numeric(x[plain]))
  out
}

# CCAA matching con patrones + fuzzy (usa los nombres IMSERSO originales)
ccaa_canon <- function(txt, max_dist = 2) {
  if (is.null(txt) || is.na(txt) || txt == "") return(NA_character_)

  ref <- tibble::tibble(
    canon = c(
      "Andaluc\u00eda", "Arag\u00f3n", "Asturias, Principado de",
      "Illes Balears", "Canarias", "Cantabria",
      "Castilla y Le\u00f3n", "Castilla - La Mancha", "Catalu\u00f1a",
      "Comunitat Valenciana", "Extremadura", "Galicia",
      "Madrid, Comunidad de", "Murcia, Regi\u00f3n de",
      "Navarra, Comunidad Foral de", "Pa\u00eds Vasco",
      "La Rioja", "Ceuta y Melilla"
    )
  ) |> mutate(canon = enc2utf8(canon), norm = norm_key_local(canon))

  txt_key <- norm_key_local(txt)

  out <- dplyr::case_when(
    str_detect(txt_key, "\\bandalucia\\b") ~ "Andaluc\u00eda",
    str_detect(txt_key, "\\baragon\\b") ~ "Arag\u00f3n",
    str_detect(txt_key, "asturias.*principado") ~ "Asturias, Principado de",
    str_detect(txt_key, "(balears|baleares|islas baleares|illes)") ~ "Illes Balears",
    str_detect(txt_key, "\\bcanarias\\b") ~ "Canarias",
    str_detect(txt_key, "\\bcantabria\\b") ~ "Cantabria",
    str_detect(txt_key, "castilla y leon") ~ "Castilla y Le\u00f3n",
    str_detect(txt_key, "castilla( |-)?la mancha") ~ "Castilla - La Mancha",
    str_detect(txt_key, "catalun?a|catalunya") ~ "Catalu\u00f1a",
    str_detect(txt_key, "comunitat valenciana|comunidad valenciana") ~ "Comunitat Valenciana",
    str_detect(txt_key, "\\bextremadura\\b") ~ "Extremadura",
    str_detect(txt_key, "\\bgalicia\\b") ~ "Galicia",
    str_detect(txt_key, "madrid.*comunidad") ~ "Madrid, Comunidad de",
    str_detect(txt_key, "murcia.*region") ~ "Murcia, Regi\u00f3n de",
    str_detect(txt_key, "navarra.*comunidad foral") ~ "Navarra, Comunidad Foral de",
    str_detect(txt_key, "pais vasco|pa[i]{1,2}s vasco") ~ "Pa\u00eds Vasco",
    str_detect(txt_key, "rioja,? la|\\bla rioja\\b") ~ "La Rioja",
    str_detect(txt_key, "ceuta y melilla") ~ "Ceuta y Melilla",
    # Desde el informe de 2026-05 Ceuta y Melilla vienen en filas separadas;
    # combine_ceuta_melilla() las agrega en "Ceuta y Melilla" como la base.
    str_detect(txt_key, "^ceuta$") ~ "Ceuta",
    str_detect(txt_key, "^melilla$") ~ "Melilla",
    TRUE ~ NA_character_
  )

  if (is.na(out)) {
    dist <- if (requireNamespace("stringdist", quietly = TRUE)) {
      tryCatch(
        stringdist::stringdist(txt_key, ref$norm, method = "lv"),
        error = function(e) rep(NA_real_, nrow(ref))
      )
    } else {
      rep(NA_real_, nrow(ref))
    }
    if (length(dist) && any(!is.na(dist))) {
      dmin <- min(dist, na.rm = TRUE)
      if (is.finite(dmin) && dmin <= max_dist) out <- ref$canon[which.min(dist)]
    }
  }

  out
}

detect_ccaa_col <- function(df, max_dist = 2, min_hits = 3) {
  if (ncol(df) == 0) return(NA_integer_)
  scores <- sapply(seq_len(ncol(df)), function(j) {
    v <- norm_txt(df[[j]])
    sum(vapply(v, function(x) {
      tryCatch(!is.na(ccaa_canon(x, max_dist = max_dist)), error = function(e) FALSE)
    }, logical(1)))
  })
  j_best <- which.max(scores)
  if (!length(j_best) || scores[j_best] < min_hits) NA_integer_ else j_best
}

# ===========================================================================
# 1. SOLICITUDES AL SAAD
# ===========================================================================

process_one_solsaad <- function(df, nm, max_dist = 2) {
  periodo <- periodo_from_name(nm)
  df <- as_tibble(df)
  if (ncol(df) == 0) return(tibble(ccaa = character(), solicitudes = numeric(), periodo = character()))

  j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
  if (is.na(j_ccaa)) return(tibble(ccaa = character(), solicitudes = numeric(), periodo = character()))
  df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa))]

  other_cols <- if (ncol(df2) > 1) df2[, -1, drop = FALSE] else tibble(.dummy = NA_character_)
  solicitudes_vec <- apply(other_cols, 1, function(row) first_numeric_in_row(unlist(row, use.names = FALSE)))

  tibble(
    raw_name    = as.character(df2[[1]]),
    solicitudes = as.numeric(solicitudes_vec)
  ) |>
    mutate(
      norm = norm_txt(raw_name),
      ccaa = vapply(norm, ccaa_canon, character(1), max_dist = max_dist)
    ) |>
    filter(!is.na(ccaa), !str_detect(norm_key_local(norm), "^total$")) |>
    transmute(ccaa, solicitudes, periodo = periodo)
}

process_solsaad <- function(solsaad_list) {
  clean <- imap(solsaad_list, ~ process_one_solsaad(.x, nm = .y, max_dist = 2))
  result <- bind_rows(clean) |> filter(solicitudes != 0)
  log_event("INFO", sprintf("solsaad_all: %d filas", nrow(result)))
  result
}

# ===========================================================================
# 2. BENEFICIARIAS DE PRESTACIONES (benpresaad)
# ===========================================================================

benpresaad_target_specs <- function() {
  tibble::tribble(
    ~canon,                ~labels_key,
    "pers_benef_prest",    c("personas beneficiarias con prestaciones",
                             "personas con prestaciones",
                             "beneficiarias con prestaciones",
                             "beneficiarios con prestaciones",
                             "personas con resolucion de pia",
                             "personas con resolucion pia"),
    "prev_dep_prom_ap",    c("prevencion dependencia y promocion a.personal",
                             "prevencion de la dependencia",
                             "promocion de la autonomia personal",
                             "promocion autonomia personal"),
    "teleasistencia",      c("teleasistencia", "tele-asistencia"),
    "ayuda_domicilio",     c("ayuda a domicilio", "servicio de ayuda a domicilio"),
    "centros_dia_noche",   c("centros de dia/noche", "centros de dia", "centros de noche",
                             "centros dia", "centros noche"),
    "atencion_residencial", c("atencion residencial", "servicios residenciales", "centros residenciales"),
    # Desde 2026-05 las etiquetas llevan punto tras la E ("P.E. Cuidados
    # Familiares") y las variantes "p.e cuidados" dejaban la columna en NA.
    "pe_vinc_serv",        c("p.e vinculada servicio", "prestacion economica vinculada servicio",
                             "prestacion vinculada al servicio", "p\\.e\\. vinculada servicio"),
    "pe_cuidados_fam",     c("p.e cuidados familiares", "prestacion economica cuidados familiares",
                             "prestacion cuidados familiares", "p\\.e\\. cuidados familiares"),
    "pe_asist_pers",       c("p.e asist. personal", "p.e asistencia personal",
                             "prestacion economica asistencia personal",
                             "p\\.e\\. asist\\. personal", "p\\.e\\. asistencia personal"),
    "total",               c("^total$", "total"),
    "ratio_prest_x_benef", c("ratio de prestaciones por persona beneficiaria",
                             "ratio de prestaciones por persona",
                             "ratio prestaciones por persona",
                             "ratio de prestaciones efectivas por persona",
                             "ratio de prestaciones por persona con resolucion de pia")
  ) |>
    mutate(labels_key = lapply(labels_key, norm_key_local))
}

find_ratio_col <- function(sigs_key) {
  needed <- c("ratio", "prestacion", "persona")
  hits <- which(vapply(
    sigs_key,
    function(s) all(str_detect(s, paste0("\\b", needed, "\\w*\\b"))),
    logical(1)
  ))
  if (length(hits)) hits[1] else NA_integer_
}

map_benpresaad_columns <- function(df_no_ccaa) {
  sigs     <- vapply(df_no_ccaa, col_signature, FUN.VALUE = character(1))
  sigs_key <- norm_key_local(sigs)
  S <- benpresaad_target_specs()
  out <- setNames(rep(NA_integer_, nrow(S)), S$canon)

  for (i in seq_len(nrow(S))) {
    canon_i <- S$canon[i]
    if (canon_i == "ratio_prest_x_benef") {
      out[[canon_i]] <- find_ratio_col(sigs_key)
      next
    }
    patt <- paste0("\\b(", paste(S$labels_key[[i]], collapse = "|"), ")\\b")
    idx <- which(str_detect(sigs_key, patt))
    if (!length(idx)) next
    idx_n <- idx[is_number_col(sigs_key[idx])]
    out[[canon_i]] <- (idx_n[1] %||% idx[1])
  }
  out
}

process_one_benpresaad <- function(df, nm, max_dist = 2) {
  fecha <- periodo_from_name(nm)
  df <- as_tibble(df)
  if (ncol(df) == 0) return(tibble(ccaa = character(), fecha = character()))

  j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
  if (is.na(j_ccaa)) return(tibble(ccaa = character(), fecha = character()))
  df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa))]

  norm_col <- norm_txt(df2[[1]])
  ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
  idx <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
  if (!length(idx)) return(tibble(ccaa = character(), fecha = character()))

  col_map <- map_benpresaad_columns(df2[, -1, drop = FALSE])

  base <- tibble(ccaa = ccaa_vec[idx])
  for (vname in names(col_map)) {
    j_rel <- col_map[[vname]]
    base[[vname]] <- if (is.na(j_rel)) NA_real_ else parse_num_es_vec(df2[[j_rel + 1L]][idx])
  }

  base |>
    mutate(fecha = fecha, .after = ccaa) |>
    mutate(
      ratio_prest_x_benef = dplyr::if_else(
        is.na(ratio_prest_x_benef) | ratio_prest_x_benef > 10,
        total / pers_benef_prest,
        ratio_prest_x_benef
      )
    ) |>
    select(ccaa, fecha, pers_benef_prest, prev_dep_prom_ap, teleasistencia,
           ayuda_domicilio, centros_dia_noche, atencion_residencial,
           pe_vinc_serv, pe_cuidados_fam, pe_asist_pers, total, ratio_prest_x_benef)
}

process_benpresaad <- function(benpresaad_list) {
  nms <- names(benpresaad_list) %||% as.character(seq_along(benpresaad_list))
  result <- purrr::map2_dfr(benpresaad_list, nms, ~ process_one_benpresaad(.x, .y))
  log_event("INFO", sprintf("benpresaad_all: %d filas", nrow(result)))
  result
}

# ===========================================================================
# 3. VALORACIONES Y DICTAMENES (dictsaad)
# ===========================================================================

dictsaad_target_specs <- function() {
  tibble::tribble(
    ~canon,               ~labels_key,
    "solicitudes",        c("\\bsolicitudes\\b", "numero de solicitudes"),
    "resoluciones_grado", c("\\bresoluc(ion|iones)\\b.*\\bgrado\\b",
                            "\\bdictamen(es)?\\b.*\\bgrado\\b"),
    "grado3", c("(\\bgrado\\b.*\\biii\\b|\\biii\\b.*\\bgrado\\b)", "\\bgrado\\s*3\\b", "\\bgrado\\s*iii\\b"),
    "grado2", c("(\\bgrado\\b.*\\bii\\b|\\bii\\b.*\\bgrado\\b)", "\\bgrado\\s*2\\b", "\\bgrado\\s*ii\\b"),
    "grado1", c("(\\bgrado\\b.*\\b(i(?!i)|1|l)\\b|\\b(i(?!i)|1|l)\\b.*\\bgrado\\b)", "\\bgrado\\s*1\\b", "\\bgrado\\s*i\\b"),
    "total_der_prest", c("\\btotal\\b.*\\bderecho\\b.*\\bprest", "\\btotal\\b.*\\bpersonas\\b.*\\bderecho\\b")
  )
}

map_dictsaad_columns <- function(df_no_ccaa) {
  sigs     <- vapply(df_no_ccaa, col_signature, FUN.VALUE = character(1))
  sigs_key <- norm_key_local(sigs)
  left_key  <- c("", head(sigs_key, -1))
  right_key <- c(tail(sigs_key, -1), "")
  neigh_key <- paste(left_key, sigs_key, right_key, sep = " | ")
  is_num <- is_number_col(sigs_key)
  is_pct <- is_percent_col(sigs_key)

  S <- dictsaad_target_specs()
  out <- setNames(as.list(rep(NA_integer_, nrow(S) + 3L)),
                  c(S$canon, "ratio_g3", "ratio_g2", "ratio_g1"))
  get_pat <- function(ci) paste0("(", paste(S$labels_key[S$canon == ci][[1]], collapse = "|"), ")")

  for (ci in c("solicitudes", "total_der_prest")) {
    pat <- get_pat(ci)
    idx <- which(is_num & str_detect(sigs_key, pat))
    if (length(idx)) out[[ci]] <- idx[1]
  }

  pat_res <- get_pat("resoluciones_grado")
  idx_res <- which(is_num & (str_detect(sigs_key, pat_res) | str_detect(neigh_key, pat_res)))
  if (length(idx_res)) {
    pri <- idx_res[str_detect(sigs_key[idx_res], pat_res)]
    out[["resoluciones_grado"]] <- (pri[1] %||% idx_res[1])
  }

  for (ci in c("grado3", "grado2", "grado1")) {
    pat <- get_pat(ci)
    idx <- which(is_num & (str_detect(sigs_key, pat) | str_detect(neigh_key, pat)))
    if (length(idx)) {
      pri <- idx[str_detect(sigs_key[idx], pat)]
      out[[ci]] <- (pri[1] %||% idx[1])
    }
  }

  has_res <- str_detect(neigh_key, pat_res)
  for (g in list(list("grado3", "ratio_g3"), list("grado2", "ratio_g2"), list("grado1", "ratio_g1"))) {
    pat <- get_pat(g[[1]])
    idx <- which(is_pct & has_res & str_detect(neigh_key, pat))
    if (length(idx)) out[[g[[2]]]] <- idx[1]
  }

  out
}

process_one_dictsaad <- function(df, nm, max_dist = 2) {
  fecha <- periodo_from_name(nm)
  df <- as_tibble(df)
  if (ncol(df) == 0) return(tibble(ccaa = character(), fecha = character()))

  j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
  if (is.na(j_ccaa)) return(tibble(ccaa = character(), fecha = character()))
  df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa))]

  norm_col <- norm_txt(df2[[1]])
  ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
  idx <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
  if (!length(idx)) return(tibble(ccaa = character(), fecha = character()))

  col_map <- map_dictsaad_columns(df2[, -1, drop = FALSE])

  base <- tibble(ccaa = ccaa_vec[idx])
  for (vname in names(col_map)) {
    j_rel <- col_map[[vname]]
    base[[vname]] <- if (is.na(j_rel)) NA_real_ else parse_num_es_vec(df2[[j_rel + 1L]][idx])
  }

  base |>
    mutate(fecha = fecha, .after = ccaa) |>
    mutate(
      ratio_g3 = dplyr::if_else(is.na(ratio_g3) & !is.na(total_der_prest) & total_der_prest > 0, 100 * grado3 / total_der_prest, ratio_g3),
      ratio_g2 = dplyr::if_else(is.na(ratio_g2) & !is.na(total_der_prest) & total_der_prest > 0, 100 * grado2 / total_der_prest, ratio_g2),
      ratio_g1 = dplyr::if_else(is.na(ratio_g1) & !is.na(total_der_prest) & total_der_prest > 0, 100 * grado1 / total_der_prest, ratio_g1)
    ) |>
    select(ccaa, fecha, solicitudes, resoluciones_grado,
           grado3, grado2, grado1, ratio_g3, ratio_g2, ratio_g1, total_der_prest)
}

process_dictsaad <- function(dictsaad_list) {
  nms <- names(dictsaad_list) %||% as.character(seq_along(dictsaad_list))
  result <- purrr::map2_dfr(dictsaad_list, nms, ~ process_one_dictsaad(.x, .y))
  log_event("INFO", sprintf("dictsaad_all: %d filas", nrow(result)))
  result
}

# ===========================================================================
# 3b. Ceuta y Melilla (incidencia 2026-10)
# ===========================================================================
# La base publica "Ceuta y Melilla" como una sola fila. Hasta 2026-04 el IMSERSO
# la daba agregada; desde 2026-05 vienen separadas y se perdian (17 CCAA).
# Si en un mes existe la fila agregada se usa esa; si no, se suman Ceuta y
# Melilla. Las columnas que no son recuentos se recalculan (recalc) o quedan NA.
combine_ceuta_melilla <- function(df, recalc = list()) {
  if (!nrow(df) || !all(c("ccaa", "fecha") %in% names(df))) return(df)
  partes <- c("Ceuta", "Melilla")
  if (!any(df$ccaa %in% partes)) return(df)

  con_agregada <- unique(df$fecha[df$ccaa == "Ceuta y Melilla"])
  sueltas <- df |> dplyr::filter(.data$ccaa %in% partes, !.data$fecha %in% con_agregada)
  resto <- df |> dplyr::filter(!.data$ccaa %in% partes)
  if (!nrow(sueltas)) return(resto)

  num_cols <- names(df)[vapply(df, is.numeric, logical(1))]
  suma_cols <- setdiff(num_cols, names(recalc))
  combinadas <- sueltas |>
    dplyr::group_by(.data$fecha) |>
    dplyr::summarise(
      n_partes = dplyr::n_distinct(.data$ccaa),
      dplyr::across(dplyr::all_of(suma_cols), ~ sum(.x)),
      .groups = "drop"
    ) |>
    dplyr::filter(.data$n_partes == 2) |>
    dplyr::select(-"n_partes") |>
    dplyr::mutate(ccaa = "Ceuta y Melilla")
  for (v in names(recalc)) combinadas[[v]] <- recalc[[v]](combinadas)

  dplyr::bind_rows(resto, combinadas[intersect(names(df), names(combinadas))])
}

# ===========================================================================
# 4. Normalizacion CCAA con diccionario CED
# ===========================================================================

apply_ccaa_normalization <- function(df) {
  if (!"ccaa" %in% names(df)) return(df)

  df |>
    mutate(
      ccaa = stringr::str_replace(ccaa, "^\\d{2}\\s+", ""),
      ccaa = normalize_ccaa_name(ccaa)
    ) |>
    filter(!stringr::str_detect(ccaa, regex("^Media Estatal$", ignore_case = TRUE)))
}

# ===========================================================================
# 5. Normalizacion de fechas
# ===========================================================================

normalize_fecha_column <- function(df) {
  if (!"fecha" %in% names(df)) {
    if ("periodo" %in% names(df)) {
      df <- dplyr::rename(df, fecha = periodo)
    } else {
      return(df)
    }
  }

  fecha_chr <- as.character(df$fecha)
  fecha_chr <- stringr::str_trim(fecha_chr)
  fecha_chr[fecha_chr == ""] <- NA_character_

  fecha_chr <- ifelse(
    is.na(fecha_chr), NA_character_,
    dplyr::case_when(
      str_detect(fecha_chr, "^\\d{4}-\\d{2}$") ~ paste0(fecha_chr, "-01"),
      str_detect(fecha_chr, "^\\d{4}-\\d{2}-\\d{2}$") ~ fecha_chr,
      str_detect(fecha_chr, "^\\d{6}$") ~ paste0(substr(fecha_chr, 1, 4), "-", substr(fecha_chr, 5, 6), "-01"),
      TRUE ~ fecha_chr
    )
  )

  df$fecha <- as.Date(fecha_chr, format = "%Y-%m-%d")
  df
}

# ===========================================================================
# 6. PERFIL DE GENERO (perf_ccaa_genero, perf_genero) - cuaderno §6
# ===========================================================================

# perf_ccaa_genero: hoja 61aperfcuidadorCCAA
process_perf_ccaa_genero <- function(perfcuidador_list, max_dist = 2) {
  if (!length(perfcuidador_list)) {
    return(tibble(ccaa = character(), fecha = character(),
                  hombre = numeric(), mujer = numeric()))
  }

  rows <- imap(perfcuidador_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (ncol(df) < 5) return(NULL)

    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    sigs_key <- norm_key_local(vapply(other, col_signature, FUN.VALUE = character(1)))
    j_hom <- which(str_detect(sigs_key, "\\bhombre"))[1]
    j_muj <- which(str_detect(sigs_key, "\\bmujer"))[1]
    if (is.na(j_hom) || is.na(j_muj)) {
      # Fallback: primeras dos columnas con valores numericos parseables
      num_cols <- which(vapply(other, function(c) any(!is.na(parse_num_es_vec(c))), logical(1)))
      if (length(num_cols) < 2) return(NULL)
      j_hom <- num_cols[1]; j_muj <- num_cols[2]
    }

    tibble(
      ccaa   = ccaa_vec[keep],
      fecha  = fecha,
      hombre = parse_num_es_vec(other[[j_hom]][keep]),
      mujer  = parse_num_es_vec(other[[j_muj]][keep])
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("perf_ccaa_genero: %d filas", nrow(result)))
  result
}

# perf_genero: 26perfsaad - perfil nacional sumando edades por sexo
process_perf_genero_nacional <- function(perfsaad_list) {
  if (!length(perfsaad_list)) {
    return(tibble(fecha = character(), genero = character(),
                  n_exp = numeric(), pct_sobre_total = numeric()))
  }

  rows <- imap(perfsaad_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (nrow(df) < 5 || ncol(df) < 4) return(NULL)

    sexo_col <- df[[1]]
    sexo_norm <- tolower(norm_txt(sexo_col))
    idx_m <- which(str_detect(sexo_norm, "^mujer"))
    idx_h <- which(str_detect(sexo_norm, "^hombre"))
    if (!length(idx_m) || !length(idx_h)) return(NULL)

    sum_row <- function(i) {
      vals <- parse_num_es_vec(unlist(df[i, -1], use.names = FALSE))
      sum(vals[!is.na(vals)])
    }
    n_m <- sum_row(idx_m[1]); n_h <- sum_row(idx_h[1])
    total <- n_m + n_h
    if (!is.finite(total) || total == 0) return(NULL)

    tibble(
      fecha = rep(fecha, 2),
      genero = c("Hombre", "Mujer"),
      n_exp = c(n_h, n_m),
      pct_sobre_total = c(n_h / total, n_m / total)
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("perf_genero (nacional): %d filas", nrow(result)))
  result
}

# ===========================================================================
# 7. PENDIENTES (cuello de botella) - cuaderno §7.4
# ===========================================================================

# 10pendResol -> pend_grado: pendientes >=6 meses de resolucion de grado
process_pend_grado <- function(pend_resol_list, max_dist = 2) {
  if (!length(pend_resol_list)) {
    return(tibble(ccaa = character(), fecha = character(),
                  pendientes_grado_total = numeric(),
                  pendientes_grado_6m_o_mas = numeric()))
  }

  rows <- imap(pend_resol_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (ncol(df) < 4) return(NULL)

    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    num_idx <- which(vapply(other, function(c) any(!is.na(parse_num_es_vec(c))), logical(1)))
    if (length(num_idx) < 4) return(NULL)
    # Convencion IMSERSO: Total | Motivo Nº | Motivo % | <6m Nº | <6m % | >=6m Nº | >=6m %
    j_total <- num_idx[1]
    j_6m    <- num_idx[length(num_idx) - 1]   # penultimo numero = >=6m Nº
    if (length(num_idx) >= 6) j_6m <- num_idx[6]

    tibble(
      ccaa  = ccaa_vec[keep],
      fecha = fecha,
      pendientes_grado_total    = parse_num_es_vec(other[[j_total]][keep]),
      pendientes_grado_6m_o_mas = parse_num_es_vec(other[[j_6m]][keep])
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("pend_grado: %d filas", nrow(result)))
  result
}

# 12BenefEfect -> benefect_full: desglose con prestacion efectiva vs pendiente.
# Esta hoja distingue, sobre las personas con resolucion de PIA, cuantas reciben
# prestacion efectiva y cuantas estan pendientes de recibirla. Es la fuente del
# tercer limbo (limbo de las prestaciones), conceptualmente distinto del limbo
# del PIA (10pendPrest) y del limbo del grado (10pendResol).
#
# Las columnas se localizan por su cabecera, no por posicion. Hasta 2026-04 la
# hoja traia una columna intermedia (prestaciones) con valores solo en algunas
# CCAA; desde 2026-05 viene vacia y la lectura posicional tomaba porcentajes
# (84,86) como personas con prestacion efectiva (incidencia 2026-10).
#   personas con resolucion de PIA (Nº)
#   personas beneficiarias con prestacion efectiva (Nº)
#   personas con resolucion de PIA aun sin recibir prestacion (Nº)  <- contraste
map_benefect_columns <- function(other) {
  sigs_key <- norm_key_local(vapply(other, col_signature, FUN.VALUE = character(1)))
  is_num <- is_number_col(sigs_key)
  first_hit <- function(hit) {
    idx <- which(is_num & hit)
    if (length(idx)) idx[1] else NA_integer_
  }
  c(
    pia        = first_hit(str_detect(sigs_key, "resolucion de pia") &
                             !str_detect(sigs_key, "sin recibir|efectiva")),
    efectiva   = first_hit(str_detect(sigs_key, "prestacion efectiva") &
                             !str_detect(sigs_key, "sin recibir")),
    pendientes = first_hit(str_detect(sigs_key, "sin recibir"))
  )
}

process_benefect_full <- function(benefect_list, max_dist = 2) {
  if (!length(benefect_list)) {
    return(tibble(ccaa = character(), fecha = character(),
                  personas_con_pia = numeric(),
                  personas_prest_efectiva = numeric(),
                  pendientes_prest_efectiva = numeric()))
  }

  rows <- imap(benefect_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (ncol(df) < 8) return(NULL)

    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    cols <- map_benefect_columns(other)
    if (anyNA(cols[c("pia", "efectiva")])) {
      log_event("WARN", sprintf("12BenefEfect %s: no se localizan las columnas de PIA y prestacion efectiva", nm))
      return(NULL)
    }

    pia      <- parse_num_es_vec(other[[cols[["pia"]]]][keep])
    efectiva <- parse_num_es_vec(other[[cols[["efectiva"]]]][keep])
    # Definicion de la base: pendientes = personas con PIA - con prestacion
    # efectiva. La columna 'aun sin recibir prestacion' solo se usa de contraste.
    pendientes <- pia - efectiva
    if (!is.na(cols[["pendientes"]])) {
      publicado <- parse_num_es_vec(other[[cols[["pendientes"]]]][keep])
      difiere <- which(!is.na(publicado) & abs(publicado - pendientes) > 0.5)
      if (length(difiere)) {
        log_event("WARN", sprintf(
          "12BenefEfect %s: PIA - efectiva no cuadra con la columna publicada en %s",
          nm, paste(ccaa_vec[keep][difiere], collapse = ", ")
        ))
      }
    }

    tibble(
      ccaa  = ccaa_vec[keep],
      fecha = fecha,
      personas_con_pia          = pia,
      personas_prest_efectiva   = efectiva,
      pendientes_prest_efectiva = pendientes
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("benefect_full: %d filas", nrow(result)))
  result
}

# 10pendPrest -> pend_pia: pendientes resolucion de PIA (limbo)
process_pend_pia <- function(pend_prest_list, max_dist = 2) {
  if (!length(pend_prest_list)) {
    return(tibble(ccaa = character(), fecha = character(),
                  pendientes_pia_total = numeric()))
  }

  rows <- imap(pend_prest_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (ncol(df) < 3) return(NULL)

    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    num_idx <- which(vapply(other, function(c) any(!is.na(parse_num_es_vec(c))), logical(1)))
    if (!length(num_idx)) return(NULL)

    tibble(
      ccaa  = ccaa_vec[keep],
      fecha = fecha,
      pendientes_pia_total = parse_num_es_vec(other[[num_idx[1]]][keep])
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("pend_pia: %d filas", nrow(result)))
  result
}

# ===========================================================================
# 8. TIEMPO DE ESPERA - cuaderno §7.5
# ===========================================================================

process_tiempo_espera <- function(tiempo_list, max_dist = 2) {
  if (!length(tiempo_list)) {
    return(tibble(ccaa = character(), fecha = character(),
                  tiempo_solicitud_grado = numeric(),
                  tiempo_grado_prestacion = numeric(),
                  tiempo_espera_total_dias = numeric()))
  }

  rows <- imap(tiempo_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    df <- as_tibble(df, .name_repair = "unique")
    if (ncol(df) < 6) return(NULL)

    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    # Convencion IMSERSO 9TiempoEspera (post-2023):
    # bloque1 (sol->grado): Nº | Tiempo
    # bloque2 (grado->derecho): Nº | Tiempo
    # bloque3 (sol->prestacion): Nº | Tiempo
    is_num <- vapply(other, function(c) any(!is.na(parse_num_es_vec(c))), logical(1))
    num_idx <- which(is_num)
    if (length(num_idx) < 6) return(NULL)
    # Tiempo es siempre la 2a, 4a, 6a columna numerica
    j_t1 <- num_idx[2]; j_t2 <- num_idx[4]; j_t3 <- num_idx[6]

    tibble(
      ccaa  = ccaa_vec[keep],
      fecha = fecha,
      tiempo_solicitud_grado    = parse_num_es_vec(other[[j_t1]][keep]),
      tiempo_grado_prestacion   = parse_num_es_vec(other[[j_t2]][keep]),
      tiempo_espera_total_dias  = parse_num_es_vec(other[[j_t3]][keep])
    )
  })

  result <- bind_rows(rows)
  log_event("INFO", sprintf("tiempo_espera: %d filas", nrow(result)))
  result
}

# ===========================================================================
# 9. PPD: obligatoria con fallback XLS - cuaderno §5, §8.4
# ===========================================================================

# Primaria: general.censo_ppd en Supabase
load_ppd_from_supabase <- function(cfg) {
  con <- connect_supabase(cfg)
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  ppd_raw <- DBI::dbGetQuery(con, sprintf(
    'SELECT * FROM "%s"."%s";', cfg$ppd_schema, cfg$ppd_table
  ))

  if (!nrow(ppd_raw)) {
    stop(sprintf('Tabla %s.%s vacia', cfg$ppd_schema, cfg$ppd_table), call. = FALSE)
  }

  vars_obj <- c("ppd", "censo_total", "ppd_rel", "ppd_pct")
  ppd_wide <- ppd_raw |>
    mutate(
      ccaa     = as.character(ccaa),
      sexo     = as.character(sexo),
      periodo  = as.integer(periodo),
      variable = as.character(variable),
      tipo     = if ("tipo" %in% names(ppd_raw)) as.character(tipo) else "observado"
    ) |>
    filter(variable %in% vars_obj) |>
    select(ccaa, sexo, periodo, tipo, variable, valor) |>
    pivot_wider(names_from = variable, values_from = valor)

  if (any(tolower(ppd_wide$sexo) == "ambos sexos", na.rm = TRUE)) {
    censo_ppd <- ppd_wide |> filter(tolower(sexo) == "ambos sexos") |> select(-sexo)
  } else {
    censo_ppd <- ppd_wide |>
      mutate(sexo = tolower(sexo)) |>
      filter(sexo %in% c("hombres", "mujeres")) |>
      group_by(ccaa, periodo, tipo) |>
      summarise(
        ppd         = sum(ppd, na.rm = TRUE),
        censo_total = sum(censo_total, na.rm = TRUE),
        ppd_rel     = ppd / censo_total,
        ppd_pct     = round(ppd_rel * 100, 2),
        .groups = "drop"
      )
  }

  censo_ppd <- censo_ppd |>
    mutate(tipo = tolower(tipo)) |>
    arrange(ccaa, periodo, factor(tipo, levels = c("observado", "forecast"))) |>
    group_by(ccaa, periodo) |> slice(1) |> ungroup() |>
    mutate(fuente = "supabase_censo_ppd")

  censo_ppd
}

# Fallback: hoja 22solcasaadpot (poblacion + PPD por CCAA, anuales)
load_ppd_from_xls <- function(ppd_xls_list, max_dist = 2) {
  if (!length(ppd_xls_list)) {
    return(tibble(ccaa = character(), periodo = integer(),
                  ppd = numeric(), censo_total = numeric()))
  }

  rows <- imap(ppd_xls_list, function(df, nm) {
    fecha <- periodo_from_name(nm)
    if (is.na(fecha)) return(NULL)
    yr <- as.integer(substr(fecha, 1, 4))

    df <- as_tibble(df, .name_repair = "unique")
    j_ccaa <- detect_ccaa_col(df, max_dist = max_dist)
    if (is.na(j_ccaa)) return(NULL)
    df2 <- df[, c(j_ccaa, setdiff(seq_len(ncol(df)), j_ccaa)), drop = FALSE]

    norm_col <- norm_txt(df2[[1]])
    ccaa_vec <- vapply(norm_col, ccaa_canon, character(1), max_dist = max_dist)
    keep <- which(!is.na(ccaa_vec) & !str_detect(norm_key_local(norm_col), "^total$"))
    if (!length(keep)) return(NULL)

    other <- df2[, -1, drop = FALSE]
    num_idx <- which(vapply(other, function(c) any(!is.na(parse_num_es_vec(c))), logical(1)))
    if (length(num_idx) < 3) return(NULL)
    # 22solcasaadpot: col1 = Pob CCAA Nº, col2 = % s/total, col3 = PPD Nº, col4 = % s/total
    j_censo <- num_idx[1]
    j_ppd   <- num_idx[3]

    tibble(
      ccaa        = ccaa_vec[keep],
      fecha       = fecha,
      periodo     = yr,
      censo_total = parse_num_es_vec(other[[j_censo]][keep]),
      ppd         = parse_num_es_vec(other[[j_ppd]][keep])
    ) |>
      combine_ceuta_melilla() |>
      dplyr::mutate(periodo = yr) |>
      dplyr::select(-"fecha")
  })

  result <- bind_rows(rows) |>
    group_by(ccaa, periodo) |>
    summarise(
      ppd         = mean(ppd, na.rm = TRUE),
      censo_total = mean(censo_total, na.rm = TRUE),
      .groups     = "drop"
    ) |>
    mutate(
      ppd_rel = ppd / censo_total,
      ppd_pct = round(ppd_rel * 100, 2),
      tipo    = "observado",
      fuente  = "xls_22solcasaadpot"
    )

  result
}

# PPD anual fijada (incidencia 2026-10). La PPD de un ano es la media de los
# informes mensuales de ese ano, asi que la del ano en curso cambia cada mes y
# arrastra todas las tasas ya publicadas. Los anos listados en
# ppd_anual_fijada.csv conservan el valor con el que se publicaron.
ppd_fijada_path <- function(cfg) file.path(cfg$transform_dir, "ppd_anual_fijada.csv")

apply_ppd_fijada <- function(censo_ppd, cfg) {
  path <- ppd_fijada_path(cfg)
  if (!file.exists(path)) return(censo_ppd)
  fijada <- readr::read_csv2(path, show_col_types = FALSE,
                             col_types = readr::cols(ccaa = "c", periodo = "i", ppd = "d", .default = "c"))
  anios <- sort(unique(fijada$periodo))
  log_event("INFO", sprintf("PPD fijada para %s (%s)", paste(anios, collapse = ", "), basename(path)))

  calculada <- censo_ppd |> dplyr::filter(.data$periodo %in% anios)
  if (nrow(calculada)) {
    cmp <- calculada |>
      dplyr::inner_join(fijada |> dplyr::select("ccaa", "periodo", ppd_fijada = "ppd"), by = c("ccaa", "periodo")) |>
      dplyr::filter(abs(.data$ppd - .data$ppd_fijada) >= 1)
    if (nrow(cmp)) {
      log_event("WARN", sprintf(
        "La PPD recalculada difiere de la fijada en %d CCAA-ano (p.ej. %s %d: %s calculada vs %s fijada); se usa la fijada",
        nrow(cmp), cmp$ccaa[1], cmp$periodo[1], format(round(cmp$ppd[1])), format(cmp$ppd_fijada[1])
      ))
    }
  }

  censo_base <- censo_ppd |> dplyr::select("ccaa", "periodo", dplyr::any_of("censo_total"))
  fijas <- fijada |>
    dplyr::select("ccaa", "periodo", "ppd") |>
    dplyr::left_join(censo_base, by = c("ccaa", "periodo")) |>
    dplyr::mutate(
      ppd_rel = .data$ppd / .data$censo_total,
      ppd_pct = round(.data$ppd_rel * 100, 2),
      tipo = "observado",
      fuente = "ppd_anual_fijada"
    )

  dplyr::bind_rows(censo_ppd |> dplyr::filter(!.data$periodo %in% anios), fijas) |>
    dplyr::arrange(.data$ccaa, .data$periodo)
}

load_ppd <- function(cfg, ppd_xls_list) {
  censo_ppd <- load_ppd_sin_fijar(cfg, ppd_xls_list)
  apply_ppd_fijada(censo_ppd, cfg)
}

load_ppd_sin_fijar <- function(cfg, ppd_xls_list) {
  ppd_db <- tryCatch(load_ppd_from_supabase(cfg), error = function(e) {
    log_event("WARN", sprintf("PPD Supabase fallo: %s", conditionMessage(e)))
    NULL
  })

  if (!is.null(ppd_db) && nrow(ppd_db) > 0) {
    log_event("OK", sprintf("PPD desde Supabase (%s.%s): %d filas | fuente=supabase_censo_ppd",
                            cfg$ppd_schema, cfg$ppd_table, nrow(ppd_db)))
    return(ppd_db)
  }

  log_event("WARN", "PPD no disponible en Supabase; usando fallback XLS (cuaderno §5.2)")
  ppd_xls <- load_ppd_from_xls(ppd_xls_list)
  if (nrow(ppd_xls) == 0) {
    log_event("ERROR", "PPD no disponible ni en Supabase ni en XLS: indicadores 1, 2, 4, 5 quedaran sin relativizar")
    return(tibble(ccaa = character(), periodo = integer(),
                  ppd = numeric(), censo_total = numeric(),
                  ppd_rel = numeric(), ppd_pct = numeric(),
                  tipo = character(), fuente = character()))
  }
  log_event("OK", sprintf("PPD desde XLS: %d filas | fuente=xls_22solcasaadpot", nrow(ppd_xls)))
  ppd_xls
}

# Une PPD anual a tablas mensuales por (ccaa, anio)
to_yyyy_mm <- function(x) {
  if (inherits(x, "Date")) return(format(x, "%Y-%m"))
  x_chr <- as.character(x)
  x_chr[x_chr %in% c("", "NA")] <- NA_character_
  ifelse(!is.na(x_chr) & str_detect(x_chr, "^\\d{4}-\\d{2}"), substr(x_chr, 1, 7), NA_character_)
}

attach_ppd_to_table <- function(df, censo_ppd) {
  if (!nrow(censo_ppd) || !all(c("ccaa", "fecha") %in% names(df))) return(df)
  ppd_lookup <- censo_ppd |>
    mutate(ccaa = normalize_ccaa_name(ccaa)) |>
    select(ccaa, periodo, ppd, censo_total)

  df |>
    mutate(.anio = as.integer(substr(to_yyyy_mm(fecha), 1, 4))) |>
    left_join(ppd_lookup, by = c("ccaa" = "ccaa", ".anio" = "periodo")) |>
    select(-.anio)
}

# ===========================================================================
# 10. INDICADORES DEL DASHBOARD (cuaderno §4) - 10 variables
# ===========================================================================

# Identidades contables del SAAD que deben cumplirse cada mes y CCAA. Si una
# hoja cambia de maquetacion y el parser toma la columna equivocada, alguna se
# rompe: es la alarma temprana que falto en la incidencia 2026-10.
#   pendientes de grado = solicitudes - resoluciones de grado      (10pendResol)
#   pendientes de PIA   = con derecho - con resolucion de PIA      (10pendPrest)
#   con resolucion de PIA coincide en 41benpresaad y 12BenefEfect
check_identidades_saad <- function(joined, tolerancia = 0.5) {
  reglas <- list(
    pendientes_grado = c("pendientes_grado_total", "solicitudes_dict", "resoluciones_grado"),
    pendientes_pia   = c("pendientes_pia_total", "total_der_prest", "pers_benef_prest"),
    personas_pia     = c("personas_con_pia", "pers_benef_prest")
  )
  for (nm in names(reglas)) {
    cols <- reglas[[nm]]
    if (!all(cols %in% names(joined))) next
    esperado <- if (length(cols) == 3) joined[[cols[2]]] - joined[[cols[3]]] else joined[[cols[2]]]
    malos <- which(!is.na(joined[[cols[1]]]) & !is.na(esperado) &
                     abs(joined[[cols[1]]] - esperado) > tolerancia)
    if (length(malos)) {
      ej <- head(malos, 5)
      log_event("WARN", sprintf(
        "Identidad %s no cuadra en %d filas (p.ej. %s)", nm, length(malos),
        paste(sprintf("%s %s", joined$ccaa[ej], format(as.Date(joined$fecha[ej]), "%Y-%m")), collapse = "; ")
      ))
    } else {
      log_event("OK", sprintf("Identidad %s: cuadra en todas las filas", nm))
    }
  }
}

compute_dashboard_indicators <- function(tables, censo_ppd) {
  has_ppd <- nrow(censo_ppd) > 0

  base_keys <- c("ccaa", "fecha")
  # Salvaguarda: el IMSERSO publica algunas CCAA con asterisco en ciertas hojas;
  # tras la normalizacion pueden quedar duplicados (ccaa, fecha). Tomamos el primero.
  dedup <- function(df) {
    if (!all(base_keys %in% names(df))) return(df)
    df |> dplyr::group_by(dplyr::across(dplyr::all_of(base_keys))) |>
      dplyr::summarise(dplyr::across(dplyr::everything(), ~ dplyr::first(.x[!is.na(.x)] %||% .x)),
                       .groups = "drop")
  }

  joined <- merge_metric_tables(
    list(
      dedup(tables$solsaad_all),
      dedup(tables$benpresaad_all),
      dedup(tables$dictsaad_all) |>
        dplyr::rename(solicitudes_dict = solicitudes),
      dedup(tables$pend_grado),
      dedup(tables$pend_pia),
      dedup(tables$tiempo_espera),
      dedup(tables$perf_ccaa_genero),
      dedup(tables$benefect_full)
    ),
    keys = base_keys
  )

  check_identidades_saad(joined)

  if (has_ppd) {
    joined <- attach_ppd_to_table(joined, censo_ppd)
  } else {
    joined$ppd         <- NA_real_
    joined$censo_total <- NA_real_
  }

  # Convencion de nombres: todos los indicadores relativizados a Poblacion
  # Potencialmente Dependiente terminan en *_pct_ppd y se almacenan ya como
  # porcentaje (x100). Esto evita el factor de display 0.1 que arrastraba el D3
  # cuando se guardaban como por mil.
  #
  # Los tres limbos de la dependencia son tres fenomenos administrativos
  # distintos del flujo SAAD, cada uno con su fuente IMSERSO oficial:
  #   - limbo_grado:        sin dictamen de grado todavia
  #                         (sheet 10pendResol -> pendientes_grado_total).
  #   - limbo_pia:          con dictamen pero pendientes de resolucion de PIA
  #                         (sheet 10pendPrest -> pendientes_pia_total).
  #   - limbo_prestaciones: con PIA aprobado pero sin prestacion efectiva
  #                         (sheet 12BenefEfect col 5 -> pendientes_prest_efectiva).
  # NB: total_der_prest - pers_benef_prest NO sirve para limbo_prestaciones,
  # porque IMSERSO publica esa diferencia como pendientes_pia_total (identidad
  # contable observada en los datos). El IMSERSO desglosa la sub-poblacion
  # 'con PIA pero sin prestacion efectiva' solo en la hoja 12BenefEfect.
  ind <- joined |>
    mutate(
      cobertura_pct_ppd            = if (has_ppd) pers_benef_prest / ppd * 100 else NA_real_,
      solicitudes_pct_ppd          = if (has_ppd) solicitudes / ppd * 100 else NA_real_,
      limbo_grado_pct_ppd          = if (has_ppd) pendientes_grado_total / ppd * 100 else NA_real_,
      limbo_pia_pct_ppd            = if (has_ppd) pendientes_pia_total / ppd * 100 else NA_real_,
      limbo_prestaciones_pct_ppd   = if (has_ppd) pendientes_prest_efectiva / ppd * 100 else NA_real_,
      pct_mujeres_benef            = mujer / (hombre + mujer) * 100,
      pct_pecef                    = pe_cuidados_fam / total * 100,
      pct_atencion_residencial     = atencion_residencial / total * 100,
      ratio_prest_x_benef          = dplyr::if_else(
        is.na(ratio_prest_x_benef) | ratio_prest_x_benef <= 0 | ratio_prest_x_benef > 10,
        total / pers_benef_prest, ratio_prest_x_benef
      ),
      pct_grado3 = dplyr::if_else(
        !is.na(total_der_prest) & total_der_prest > 0,
        grado3 / total_der_prest * 100,
        NA_real_
      )
    ) |>
    select(
      dplyr::all_of(base_keys),
      ppd, censo_total,
      dplyr::all_of(dashboard_indicator_names()),
      tiempo_solicitud_grado, tiempo_grado_prestacion
    )

  if (!has_ppd) {
    ind <- ind |> select(-ppd, -censo_total)
  }

  log_event("INFO", sprintf("dashboard_indicators: %d filas | %d indicadores",
                            nrow(ind), length(dashboard_indicator_names())))
  ind
}

# ===========================================================================
# Funcion principal: run_transformacion
# ===========================================================================

run_transformacion <- function(cfg) {
  log_event("STEP", "Iniciando transformacion (cuaderno v2 - matriz 10 indicadores)")

  # 1. Cargar datos extraidos
  needed <- c("solsaad", "perfsaad", "dictsaad", "benpresaad",
              "perfcuidador_ccaa", "tiempo_espera", "pendsaad", "ppd_xls",
              "benefect_full")
  extracted <- load_named_rds(cfg$extraction_dir, needed)

  # 2. Procesar tablas operativas
  solsaad_all      <- process_solsaad(extracted$solsaad)
  benpresaad_all   <- process_benpresaad(extracted$benpresaad)
  dictsaad_all     <- process_dictsaad(extracted$dictsaad)
  perf_ccaa_genero <- process_perf_ccaa_genero(extracted$perfcuidador_ccaa)
  perf_genero      <- process_perf_genero_nacional(extracted$perfsaad)
  pend_grado       <- process_pend_grado(extracted$pendsaad$resol)
  pend_pia         <- process_pend_pia(extracted$pendsaad$prest)
  tiempo_espera    <- process_tiempo_espera(extracted$tiempo_espera)
  benefect_full    <- process_benefect_full(extracted$benefect_full)

  # 3. Normalizacion CCAA + fechas + corte 2023 (cuaderno §2)
  to_normalize <- list(
    solsaad_all      = solsaad_all,
    benpresaad_all   = benpresaad_all,
    dictsaad_all     = dictsaad_all,
    perf_ccaa_genero = perf_ccaa_genero,
    pend_grado       = pend_grado,
    pend_pia         = pend_pia,
    tiempo_espera    = tiempo_espera,
    benefect_full    = benefect_full
  )
  na_recalc <- function(d) NA_real_
  recalc_ceuta_melilla <- list(
    benpresaad_all = list(ratio_prest_x_benef = function(d) d$total / d$pers_benef_prest),
    dictsaad_all = list(
      ratio_g3 = function(d) 100 * d$grado3 / d$resoluciones_grado,
      ratio_g2 = function(d) 100 * d$grado2 / d$resoluciones_grado,
      ratio_g1 = function(d) 100 * d$grado1 / d$resoluciones_grado
    ),
    tiempo_espera = list(tiempo_solicitud_grado = na_recalc, tiempo_grado_prestacion = na_recalc,
                         tiempo_espera_total_dias = na_recalc)
  )
  for (nm in setdiff(names(to_normalize), "perf_ccaa_genero")) {
    to_normalize[[nm]] <- combine_ceuta_melilla(to_normalize[[nm]], recalc_ceuta_melilla[[nm]] %||% list())
  }
  # perf_ccaa_genero queda fuera a proposito: la base nunca ha tenido
  # "Ceuta y Melilla" en esa tabla y anadirla cambiaria meses ya publicados.
  to_normalize$perf_ccaa_genero <- to_normalize$perf_ccaa_genero |>
    dplyr::filter(!.data$ccaa %in% c("Ceuta", "Melilla"))
  to_normalize <- lapply(to_normalize, apply_ccaa_normalization)
  to_normalize <- lapply(to_normalize, normalize_fecha_column)

  start_year <- as.integer(cfg$pipeline_start_year %||% 2023L)
  to_normalize <- lapply(to_normalize, function(df) {
    if (!"fecha" %in% names(df) || !nrow(df)) return(df)
    df |> dplyr::filter(is.na(.data$fecha) | lubridate::year(.data$fecha) >= start_year)
  })

  # 4. PPD obligatoria con fallback XLS (cuaderno §8.4)
  censo_ppd <- load_ppd(cfg, extracted$ppd_xls)

  # 5. Calcular los 10 indicadores del dashboard (cuaderno §4)
  dashboard_indicators <- compute_dashboard_indicators(to_normalize, censo_ppd)
  check_freshness(
    suppressWarnings(max(as.Date(dashboard_indicators$fecha[!is.na(dashboard_indicators$pct_pecef)]))),
    "Extraccion IMSERSO (dashboard_indicators)"
  )

  # 6. Lista final de salidas
  all_tables <- c(
    to_normalize,
    list(
      perf_genero          = perf_genero,
      censo_ppd            = censo_ppd,
      dashboard_indicators = dashboard_indicators
    )
  )

  # 7. Log de cobertura
  for (nm in names(all_tables)) {
    if ("ccaa" %in% names(all_tables[[nm]]) || "fecha" %in% names(all_tables[[nm]])) {
      log_series_coverage(all_tables[[nm]], nm)
    }
  }

  # 8. Guardar
  save_named_rds(all_tables, cfg$transform_dir)

  log_event("OK", "Transformacion completada")
  invisible(all_tables)
}
