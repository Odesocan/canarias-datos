#!/usr/bin/env Rscript
# =============================================================================
# Dependencia / _analisis / analisis_asimetria_pre2023.R
# -----------------------------------------------------------------------------
# Cuantifica la asimetría informativa entre los registros del SAAD anteriores
# al 1-ene-2023 y los publicados a partir de esa fecha. Sirve como apoyo a la
# decisión de hasta dónde extender el análisis longitudinal: cuántas variables
# relevantes se "pierden" si se incorpora el histórico completo, y qué
# subconjunto de variables permite una serie comparable de larga duración.
#
# El análisis es estructural y semántico:
#   - Estructural: recorre `1_extraccion/saad_by_year_month.rds`, que captura
#     todas las hojas publicadas por el IMSERSO (no solo las clasificadas
#     por el ETL activo), y genera un inventario completo (año, mes, archivo,
#     hoja, ncol, nrow, firma de columnas, primera fila).
#   - Semántico: si existen las tablas procesadas en `2_transformacion/`,
#     calcula la cobertura (% NA) por columna y por periodo (pre/post 2023)
#     para detectar columnas presentes en la matriz pero vacías antes de 2023.
#
# Salidas (en `_analisis/`):
#   - inventario_estructural.csv              · una fila por hoja-mes
#   - resumen_hojas_por_periodo.csv           · presencia/ncol por tipo y periodo
#   - cambios_columnas_pre_post.csv           · columnas exclusivas pre/post
#   - cobertura_por_columna_periodo.csv       · si hay tablas transformadas
#   - informe_asimetria_pre2023.md            · informe legible final
#
# Uso:
#   Rscript _analisis/analisis_asimetria_pre2023.R
#   Rscript _analisis/analisis_asimetria_pre2023.R --cutoff 2023-01-01
#
# Notas:
#   - No requiere conexión a Supabase ni ejecución previa del pipeline; basta
#     con que exista `1_extraccion/saad_by_year_month.rds`.
#   - No modifica nada del ETL de producción.
# =============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(tibble)
  library(tidyr)
  library(purrr)
  library(stringr)
  library(readr)
})

# ---------------------------------------------------------------------------
# Localizar la raíz del módulo Dependencia
# ---------------------------------------------------------------------------

# Si el script se ejecuta desde la raíz del módulo, `getwd()` ya es la raíz.
# Si se ejecuta desde _analisis/, subimos un nivel.
locate_root <- function() {
  candidates <- c(getwd(), file.path(getwd(), ".."), dirname(getwd()))
  for (p in candidates) {
    if (file.exists(file.path(p, "00_maestro.R")) &&
        file.exists(file.path(p, "1_extraccion"))) {
      return(normalizePath(p))
    }
  }
  stop("No se encuentra la raíz del módulo Dependencia. Ejecuta el script ",
       "desde la carpeta `Dependencia/` o desde `Dependencia/_analisis/`.",
       call. = FALSE)
}

ROOT <- locate_root()
setwd(ROOT)

# Cargar utilidades del pipeline para usar el log_event consistente
utils_path <- file.path(ROOT, "utils", "pipeline_utils.R")
if (file.exists(utils_path)) {
  source(utils_path, local = TRUE)
} else {
  log_event <- function(level, msg) {
    cat(sprintf("[%s] %s\n", level, msg))
  }
}

# ---------------------------------------------------------------------------
# Argumentos CLI
# ---------------------------------------------------------------------------

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(name, default = NULL) {
  hit <- grep(paste0("^--", name, "(=|$)"), args, value = TRUE)
  if (!length(hit)) return(default)
  val <- sub(paste0("^--", name, "="), "", hit[1])
  if (val == hit[1]) {
    # Sin '=', se asume el siguiente argumento
    idx <- which(args == hit[1])
    if (idx < length(args)) args[idx + 1] else default
  } else {
    val
  }
}

CUTOFF      <- as.Date(get_arg("cutoff", "2023-01-01"))
RAW_RDS     <- file.path(ROOT, "1_extraccion", "saad_by_year_month.rds")
TRANSF_DIR  <- file.path(ROOT, "2_transformacion")
OUT_DIR     <- file.path(ROOT, "_analisis")
dir.create(OUT_DIR, showWarnings = FALSE, recursive = TRUE)

log_event("STEP", sprintf("Análisis de asimetría pre/post %s", CUTOFF))
log_event("INFO", sprintf("Raíz del módulo: %s", ROOT))

if (!file.exists(RAW_RDS)) {
  stop(sprintf("No se encuentra %s. Ejecuta primero la etapa de extracción.",
               RAW_RDS), call. = FALSE)
}

# ---------------------------------------------------------------------------
# 1. Inventario estructural: recorrer saad_by_year_month
# ---------------------------------------------------------------------------

log_event("STEP", "1. Inventario estructural de hojas")

raw_data <- readRDS(RAW_RDS)

# El árbol esperado es: año → mes → archivo (lista) → hoja (tibble).
# Defendemos contra heterogeneidades.

walk_raw <- function(raw) {
  rows <- list()
  i <- 0
  for (yr_name in names(raw)) {
    yr <- suppressWarnings(as.integer(yr_name))
    if (is.na(yr)) next
    year_list <- raw[[yr_name]]
    if (!is.list(year_list) || !length(year_list)) next

    for (mo_name in names(year_list)) {
      mo <- suppressWarnings(as.integer(mo_name))
      if (is.na(mo) || mo < 1 || mo > 12) next
      mo_list <- year_list[[mo_name]]
      if (!is.list(mo_list) || !length(mo_list)) next

      for (fi in seq_along(mo_list)) {
        file_obj <- mo_list[[fi]]
        if (!is.list(file_obj) || !length(file_obj)) next
        sheet_names <- names(file_obj)
        if (is.null(sheet_names)) sheet_names <- as.character(seq_along(file_obj))

        for (sh_idx in seq_along(file_obj)) {
          tb <- file_obj[[sh_idx]]
          sh_nm <- sheet_names[sh_idx]
          ncol_v <- if (is.data.frame(tb) || is.matrix(tb)) ncol(tb) else NA_integer_
          nrow_v <- if (is.data.frame(tb) || is.matrix(tb)) nrow(tb) else NA_integer_
          col_sig <- if (is.data.frame(tb)) paste(colnames(tb), collapse = " | ") else ""
          first_row <- if (is.data.frame(tb) && nrow(tb) >= 1) {
            paste(unlist(lapply(tb[1, ], as.character)), collapse = " | ")
          } else ""
          second_row <- if (is.data.frame(tb) && nrow(tb) >= 2) {
            paste(unlist(lapply(tb[2, ], as.character)), collapse = " | ")
          } else ""

          i <- i + 1
          rows[[i]] <- tibble(
            year       = yr,
            month      = mo,
            fecha      = as.Date(sprintf("%04d-%02d-01", yr, mo)),
            file_idx   = fi,
            sheet_name = sh_nm %||% NA_character_,
            ncol       = ncol_v,
            nrow       = nrow_v,
            col_signature = col_sig,
            first_row  = substr(first_row, 1, 800),
            second_row = substr(second_row, 1, 800)
          )
        }
      }
    }
  }
  if (!length(rows)) return(tibble())
  bind_rows(rows)
}

# `%||%` por si no está cargado dplyr internals
`%||%` <- function(a, b) if (is.null(a) || (length(a) == 1 && is.na(a))) b else a

inv <- walk_raw(raw_data)

if (!nrow(inv)) {
  stop("El inventario estructural está vacío. ¿saad_by_year_month.rds tiene contenido?",
       call. = FALSE)
}

# Clasifica cada hoja según los patrones que usa el ETL
# (replica `extraccion.R:403–406` y `R/pipeline_utils.R:260` para benpresaad)
classify_sheet <- function(sheet_name, year) {
  s <- ifelse(is.na(sheet_name), "", sheet_name)
  # Patrón ampliado para benpresaad_v2: el ETL actual busca solo
  # "benefect_pre" / "benef efect_pre", pero las publicaciones del IMSERSO
  # post-2023 nombran la hoja como "12BenefEfect" (prefijo numérico,
  # camelcase, sin separador). Este script reconoce la variante real.
  case_when(
    grepl("sol\\s*_?-?\\s*saad", s, ignore.case = TRUE)  ~ "solsaad",
    grepl("perf\\s*_?-?\\s*saad", s, ignore.case = TRUE) ~ "perfsaad",
    grepl("dict\\s*_?-?\\s*saad", s, ignore.case = TRUE) ~ "dictsaad",
    year <= 2022 & grepl("^\\s*\\d*\\s*benpresaad\\s*$", s, ignore.case = TRUE) ~ "benpresaad_v1",
    year >= 2023 & grepl("benef\\s*[_-]?\\s*efect", s, ignore.case = TRUE) ~ "benpresaad_v2",
    TRUE ~ "otros"
  )
}

inv <- inv %>%
  mutate(
    tipo_hoja = classify_sheet(sheet_name, year),
    periodo   = if_else(fecha >= CUTOFF, "post", "pre")
  )

write_csv(inv, file.path(OUT_DIR, "inventario_estructural.csv"))
log_event("OK", sprintf("Inventario: %d filas (%d hojas únicas) → inventario_estructural.csv",
                        nrow(inv), n_distinct(inv$sheet_name)))

# ---------------------------------------------------------------------------
# 2. Resumen por tipo de hoja y periodo
# ---------------------------------------------------------------------------

log_event("STEP", "2. Resumen por tipo de hoja × periodo")

# Agregamos a una fila por (año-mes, tipo_hoja) — quedándonos con la primera
# coincidencia si hubo varios archivos del mismo mes (replica el comportamiento
# de extract_sheet_by_pattern que toma la primera hoja que casa).
inv_canon <- inv %>%
  filter(tipo_hoja != "otros") %>%
  group_by(year, month, fecha, tipo_hoja, periodo) %>%
  arrange(file_idx, .by_group = TRUE) %>%
  slice(1) %>%
  ungroup()

# Conteo de meses observados y posibles por periodo
total_meses <- inv %>%
  distinct(year, month, fecha, periodo) %>%
  count(periodo, name = "n_meses_observados")

resumen_tipos <- inv_canon %>%
  group_by(tipo_hoja, periodo) %>%
  summarise(
    n_meses        = n(),
    ncol_mediana   = round(median(ncol, na.rm = TRUE), 1),
    ncol_min       = min(ncol, na.rm = TRUE),
    ncol_max       = max(ncol, na.rm = TRUE),
    nrow_mediana   = round(median(nrow, na.rm = TRUE), 1),
    n_firmas_dist  = n_distinct(col_signature),
    .groups = "drop"
  ) %>%
  left_join(total_meses, by = "periodo") %>%
  mutate(
    cobertura_pct = round(100 * n_meses / pmax(1, n_meses_observados), 1)
  ) %>%
  arrange(tipo_hoja, periodo)

write_csv(resumen_tipos, file.path(OUT_DIR, "resumen_hojas_por_periodo.csv"))
log_event("OK", "Resumen → resumen_hojas_por_periodo.csv")

# ---------------------------------------------------------------------------
# 3. Cambios en columnas: exclusivas pre vs exclusivas post
# ---------------------------------------------------------------------------

log_event("STEP", "3. Cambios de columnas pre vs post")

normalize_label <- function(x) {
  x %>%
    as.character() %>%
    iconv(to = "UTF-8") %>%
    str_replace_all("[^\\p{L}\\p{N}]+", "_") %>%
    str_replace_all("_+", "_") %>%
    str_remove_all("^_|_$") %>%
    str_to_lower()
}

# Para cada (tipo_hoja, periodo), reunimos el universo de etiquetas: usamos
# tanto `col_signature` (los nombres que asigna read_excel) como `first_row`
# y `second_row`, porque los XLS del IMSERSO suelen tener la cabecera
# semántica desplazada una o dos filas.
labels_long <- inv_canon %>%
  filter(tipo_hoja %in% c("solsaad", "perfsaad", "dictsaad",
                          "benpresaad_v1", "benpresaad_v2")) %>%
  select(tipo_hoja, periodo, year, month, col_signature, first_row, second_row) %>%
  mutate(across(c(col_signature, first_row, second_row),
                ~ str_split(.x, fixed(" | ")))) %>%
  pivot_longer(c(col_signature, first_row, second_row),
               names_to = "fuente_label", values_to = "labels") %>%
  unnest(labels) %>%
  mutate(label_norm = normalize_label(labels)) %>%
  filter(!is.na(label_norm), nchar(label_norm) > 1,
         !label_norm %in% c("na", "ccaa", "x", "x_1", "x_2", "v_1", "v_2")) %>%
  distinct(tipo_hoja, periodo, label_norm)

cambios <- labels_long %>%
  pivot_wider(names_from = periodo, values_from = periodo,
              values_fn = ~ TRUE, values_fill = FALSE) %>%
  mutate(
    estado = case_when(
      pre &  post ~ "comun",
      !pre &  post ~ "exclusiva_post_2023",
      pre & !post ~ "exclusiva_pre_2023",
      TRUE         ~ "ninguno"
    )
  ) %>%
  filter(estado != "ninguno") %>%
  arrange(tipo_hoja, estado, label_norm)

write_csv(cambios, file.path(OUT_DIR, "cambios_columnas_pre_post.csv"))

n_exclusivas_post <- cambios %>%
  filter(estado == "exclusiva_post_2023") %>%
  count(tipo_hoja)
n_exclusivas_pre <- cambios %>%
  filter(estado == "exclusiva_pre_2023") %>%
  count(tipo_hoja)
n_comunes <- cambios %>%
  filter(estado == "comun") %>%
  count(tipo_hoja)

log_event("OK", "Cambios → cambios_columnas_pre_post.csv")

# ---------------------------------------------------------------------------
# 4. Inventario semántico: cobertura (% NA) por columna y periodo
#    sobre las tablas ya transformadas, si existen
# ---------------------------------------------------------------------------

log_event("STEP", "4. Cobertura por columna y periodo (tablas transformadas)")

cobertura <- tibble()
processed_tables <- c("solsaad_all.rds", "benpresaad_all.rds", "dictsaad_all.rds")
existen <- processed_tables[file.exists(file.path(TRANSF_DIR, processed_tables))]

if (length(existen)) {
  for (fnm in existen) {
    tb <- readRDS(file.path(TRANSF_DIR, fnm))
    if (!is.data.frame(tb) || !"fecha" %in% names(tb)) next
    tb <- tb %>%
      mutate(fecha = suppressWarnings(as.Date(fecha)),
             periodo = if_else(fecha >= CUTOFF, "post", "pre"))
    metric_cols <- setdiff(names(tb), c("ccaa", "fecha", "periodo"))
    if (!length(metric_cols)) next

    cob <- tb %>%
      pivot_longer(all_of(metric_cols), names_to = "columna", values_to = "valor") %>%
      group_by(tabla = sub("\\.rds$", "", fnm), periodo, columna) %>%
      summarise(
        n_filas      = n(),
        n_no_na      = sum(!is.na(valor)),
        pct_no_na    = round(100 * mean(!is.na(valor)), 1),
        .groups = "drop"
      )
    cobertura <- bind_rows(cobertura, cob)
  }

  cob_wide <- cobertura %>%
    select(tabla, columna, periodo, pct_no_na) %>%
    pivot_wider(names_from = periodo, values_from = pct_no_na,
                values_fill = NA_real_) %>%
    rename(pct_no_na_pre = pre, pct_no_na_post = post) %>%
    mutate(
      diferencia_post_menos_pre = round(pct_no_na_post - pct_no_na_pre, 1),
      flag = case_when(
        is.na(pct_no_na_pre)  | pct_no_na_pre  < 5  ~ "solo_post_o_casi_vacia_pre",
        is.na(pct_no_na_post) | pct_no_na_post < 5  ~ "solo_pre_o_casi_vacia_post",
        diferencia_post_menos_pre >= 30             ~ "asimetria_marcada_post>>pre",
        diferencia_post_menos_pre <= -30            ~ "asimetria_marcada_pre>>post",
        TRUE                                         ~ "comparable"
      )
    ) %>%
    arrange(tabla, flag, columna)

  write_csv(cob_wide, file.path(OUT_DIR, "cobertura_por_columna_periodo.csv"))
  log_event("OK", "Cobertura → cobertura_por_columna_periodo.csv")
} else {
  log_event("WARN", paste(
    "No se encontraron tablas transformadas en", TRANSF_DIR,
    "— el análisis semántico se omite. Ejecuta la etapa de transformación primero."
  ))
  cob_wide <- tibble()
}

# ---------------------------------------------------------------------------
# 5. Informe markdown
# ---------------------------------------------------------------------------

log_event("STEP", "5. Generando informe markdown")

fmt_pct <- function(x) ifelse(is.na(x), "s/d", sprintf("%.1f%%", x))

meses_pre  <- total_meses %>% filter(periodo == "pre")  %>% pull(n_meses_observados) %>% as.integer()
meses_post <- total_meses %>% filter(periodo == "post") %>% pull(n_meses_observados) %>% as.integer()
if (!length(meses_pre))  meses_pre  <- 0
if (!length(meses_post)) meses_post <- 0

rango_pre  <- inv %>% filter(periodo == "pre")  %>% summarise(min = min(fecha), max = max(fecha))
rango_post <- inv %>% filter(periodo == "post") %>% summarise(min = min(fecha), max = max(fecha))

resumen_md <- resumen_tipos %>%
  arrange(tipo_hoja, periodo) %>%
  transmute(
    tipo_hoja, periodo,
    `meses con hoja` = n_meses,
    `cobertura %`    = cobertura_pct,
    `ncol mediana`   = ncol_mediana,
    `ncol min/max`   = paste0(ncol_min, "/", ncol_max),
    `firmas distintas` = n_firmas_dist
  )

md_path <- file.path(OUT_DIR, "informe_asimetria_pre2023.md")

con <- file(md_path, open = "w", encoding = "UTF-8")
on.exit(close(con), add = TRUE)

w <- function(...) writeLines(paste0(...), con)

w("# Asimetría informativa del SAAD pre-", format(CUTOFF, "%Y-%m-%d"), " vs post-", format(CUTOFF, "%Y-%m-%d"))
w("")
w("> Generado por `_analisis/analisis_asimetria_pre2023.R` el ", format(Sys.time(), "%Y-%m-%d %H:%M"), ".")
w("> Fuente: `1_extraccion/saad_by_year_month.rds` (todas las hojas publicadas por el IMSERSO).")
w("")
w("## 1. Cobertura temporal")
w("")
w("- **Pre-", format(CUTOFF, "%Y-%m-%d"), "**: ", meses_pre, " meses observados",
  if (meses_pre > 0) paste0(" (", rango_pre$min, " → ", rango_pre$max, ")") else "", ".")
w("- **Post-", format(CUTOFF, "%Y-%m-%d"), "**: ", meses_post, " meses observados",
  if (meses_post > 0) paste0(" (", rango_post$min, " → ", rango_post$max, ")") else "", ".")
w("")
w("## 2. Hojas presentes por tipo y periodo")
w("")
w("La columna *firmas distintas* indica cuántas combinaciones diferentes de cabecera ",
  "se han detectado para esa hoja en ese periodo. Una cifra alta sugiere inestabilidad ",
  "estructural (renombres, columnas que aparecen y desaparecen).")
w("")
w(paste("|", paste(names(resumen_md), collapse = " | "), "|"))
w(paste("|", paste(rep("---", ncol(resumen_md)), collapse = " | "), "|"))
for (i in seq_len(nrow(resumen_md))) {
  w(paste("|", paste(unlist(resumen_md[i, ]), collapse = " | "), "|"))
}
w("")
w("## 2.1 Hojas publicadas por el IMSERSO **no procesadas** por el ETL actual")
w("")
w("Listado de hojas que aparecen en `saad_by_year_month.rds` pero no casan con ",
  "ningún patrón del ETL (`solsaad`, `perfsaad`, `dictsaad`, `benpresaad_v1/v2`). ",
  "Su existencia indica capacidad informativa publicada por el IMSERSO que hoy ",
  "**no está llegando** a la tabla `ced_dependencia`.")
w("")

otros_post <- inv %>%
  filter(periodo == "post", tipo_hoja == "otros") %>%
  group_by(sheet_name) %>%
  summarise(
    n_meses_post     = n_distinct(paste(year, month)),
    ncol_mediana     = round(median(ncol, na.rm = TRUE), 1),
    nrow_mediana     = round(median(nrow, na.rm = TRUE), 1),
    primera_aparicion = min(fecha, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  arrange(desc(n_meses_post), sheet_name)

if (nrow(otros_post) > 0) {
  w("**Post-", format(CUTOFF, "%Y-%m-%d"), "** (", meses_post, " meses observados):")
  w("")
  w("| hoja | meses con la hoja | ncol mediana | nrow mediana | primera aparición |")
  w("|---|---|---|---|---|")
  for (i in seq_len(nrow(otros_post))) {
    r <- otros_post[i, ]
    w(sprintf("| `%s` | %d | %s | %s | %s |",
              r$sheet_name, r$n_meses_post,
              ifelse(is.na(r$ncol_mediana), "-", as.character(r$ncol_mediana)),
              ifelse(is.na(r$nrow_mediana), "-", as.character(r$nrow_mediana)),
              format(r$primera_aparicion, "%Y-%m")))
  }
  w("")
}

otros_pre <- inv %>%
  filter(periodo == "pre", tipo_hoja == "otros") %>%
  group_by(sheet_name) %>%
  summarise(
    n_meses_pre  = n_distinct(paste(year, month)),
    ncol_mediana = round(median(ncol, na.rm = TRUE), 1),
    .groups = "drop"
  ) %>%
  arrange(desc(n_meses_pre), sheet_name)

if (nrow(otros_pre) > 0) {
  w("**Pre-", format(CUTOFF, "%Y-%m-%d"), "** (", meses_pre, " meses observados, hojas con presencia ≥ 12 meses):")
  w("")
  otros_pre_filt <- otros_pre %>% filter(n_meses_pre >= 12)
  if (nrow(otros_pre_filt) > 0) {
    w("| hoja | meses con la hoja | ncol mediana |")
    w("|---|---|---|")
    for (i in seq_len(nrow(otros_pre_filt))) {
      r <- otros_pre_filt[i, ]
      w(sprintf("| `%s` | %d | %s |",
                r$sheet_name, r$n_meses_pre,
                ifelse(is.na(r$ncol_mediana), "-", as.character(r$ncol_mediana))))
    }
  } else {
    w("_Ninguna hoja \"otros\" pre-", format(CUTOFF, "%Y"), " supera el umbral de 12 meses._")
  }
  w("")
}

w("## 3. Cambios en el universo de columnas (etiquetas detectadas)")
w("")
w("Etiquetas únicas detectadas en cada hoja, separadas por *exclusivas pre*, ",
  "*exclusivas post* y *comunes*. Las exclusivas post identifican lo que se ",
  "**perdería** si se truncase la serie en pre-", format(CUTOFF, "%Y-%m-%d"), ".")
w("")
w("| tipo_hoja | comunes | exclusivas pre-", format(CUTOFF, "%Y"), " | exclusivas post-", format(CUTOFF, "%Y"), " |")
w("|---|---|---|---|")
todos_tipos <- sort(unique(c(n_comunes$tipo_hoja, n_exclusivas_pre$tipo_hoja, n_exclusivas_post$tipo_hoja)))
for (t in todos_tipos) {
  c_com <- n_comunes %>% filter(tipo_hoja == t) %>% pull(n) %>% as.integer()
  c_pre <- n_exclusivas_pre %>% filter(tipo_hoja == t) %>% pull(n) %>% as.integer()
  c_pos <- n_exclusivas_post %>% filter(tipo_hoja == t) %>% pull(n) %>% as.integer()
  w(sprintf("| %s | %d | %d | %d |", t,
            ifelse(length(c_com), c_com, 0L),
            ifelse(length(c_pre), c_pre, 0L),
            ifelse(length(c_pos), c_pos, 0L)))
}
w("")
w("Detalle completo en `cambios_columnas_pre_post.csv`.")
w("")

w("### 3.1 Top 30 etiquetas exclusivas de post-", format(CUTOFF, "%Y"), " por tipo de hoja")
w("")
top_post <- cambios %>%
  filter(estado == "exclusiva_post_2023") %>%
  group_by(tipo_hoja) %>%
  slice_head(n = 30) %>%
  ungroup()
for (t in unique(top_post$tipo_hoja)) {
  w("- **", t, "**: ",
    paste0("`", top_post %>% filter(tipo_hoja == t) %>% pull(label_norm), "`",
           collapse = ", "))
}
w("")

w("### 3.2 Top 30 etiquetas exclusivas de pre-", format(CUTOFF, "%Y"), " por tipo de hoja")
w("")
top_pre <- cambios %>%
  filter(estado == "exclusiva_pre_2023") %>%
  group_by(tipo_hoja) %>%
  slice_head(n = 30) %>%
  ungroup()
for (t in unique(top_pre$tipo_hoja)) {
  w("- **", t, "**: ",
    paste0("`", top_pre %>% filter(tipo_hoja == t) %>% pull(label_norm), "`",
           collapse = ", "))
}
w("")

w("## 4. Cobertura por columna en las tablas ya transformadas")
w("")
if (nrow(cob_wide) > 0) {
  w("Para cada columna métrica de las tablas en `2_transformacion/`, % de filas no-NA ",
    "en cada periodo. Una columna marcada *solo_post_o_casi_vacia_pre* indica que ese ",
    "indicador en la práctica no existe antes de ", format(CUTOFF, "%Y-%m-%d"), ".")
  w("")
  resumen_flag <- cob_wide %>% count(tabla, flag)
  w("**Distribución por flag**:")
  w("")
  w("| tabla | flag | n columnas |")
  w("|---|---|---|")
  for (i in seq_len(nrow(resumen_flag))) {
    r <- resumen_flag[i, ]
    w(sprintf("| %s | %s | %d |", r$tabla, r$flag, r$n))
  }
  w("")
  w("**Columnas exclusivas o casi exclusivas de post-", format(CUTOFF, "%Y"), "**:")
  w("")
  solo_post <- cob_wide %>% filter(flag == "solo_post_o_casi_vacia_pre")
  if (nrow(solo_post) > 0) {
    w("| tabla | columna | %no-NA pre | %no-NA post |")
    w("|---|---|---|---|")
    for (i in seq_len(nrow(solo_post))) {
      r <- solo_post[i, ]
      w(sprintf("| %s | %s | %s | %s |",
                r$tabla, r$columna, fmt_pct(r$pct_no_na_pre), fmt_pct(r$pct_no_na_post)))
    }
  } else {
    w("_Ninguna columna queda como exclusiva post según el umbral del 5%._")
  }
  w("")
  w("Detalle completo en `cobertura_por_columna_periodo.csv`.")
} else {
  w("> Las tablas transformadas no estaban disponibles cuando se ejecutó este análisis. ",
    "Ejecuta `00_maestro.R --steps=transformacion` y vuelve a lanzar este script para ",
    "obtener el inventario semántico.")
}
w("")

w("## 5. Lectura recomendada")
w("")
w("- **Subconjunto longitudinal seguro**: usar únicamente las columnas comunes a ",
  "ambos periodos y/o las que aparezcan con `flag = comparable` en la tabla de cobertura. ",
  "Permite un histórico desde ", format(rango_pre$min, "%Y"), " sin imputaciones ad-hoc.")
w("- **Subconjunto enriquecido (post-", format(CUTOFF, "%Y-%m-%d"), ")**: aprovecha el ",
  "detalle adicional aportado a partir de 2023 (perf_saad enriquecido, benefect_pre con ",
  "ratios y desgloses). Idóneo para análisis transversal, ranking territorial y dashboard.")
w("- **Estrategia híbrida**: publicar una vista A (longitudinal, columnas mínimas, ",
  "desde 2012) y una vista B (transversal, columnas completas, desde 2023), con un ",
  "campo `version_schema` que el front-end pueda usar para condicionar los gráficos ",
  "más detallados al periodo en que existen.")
w("")
w("> **Nota crítica**: la sección 2.1 lista hojas publicadas por el IMSERSO post-",
  format(CUTOFF, "%Y"), " que el ETL actual **no está procesando** (listas de espera, ",
  "pendientes de PIA, dictámenes y beneficiarios desglosados por grado, perfil de ",
  "resoluciones, etc.). Antes de tomar la decisión longitudinal/transversal, conviene ",
  "evaluar si ampliar los patrones de clasificación de hojas en `extraccion.R` ",
  "(actualmente limitados a `solsaad`, `perfsaad`, `dictsaad`, `benefect_pre`) para ",
  "incorporar estos bloques. Sin esa ampliación, una parte sustancial de la riqueza ",
  "informativa post-2023 permanece invisible para el dashboard, independientemente ",
  "del periodo elegido.")
w("")

log_event("OK", sprintf("Informe → %s", md_path))
log_event("STEP", "Análisis completado")

# ---------------------------------------------------------------------------
# Resumen en consola
# ---------------------------------------------------------------------------

cat("\n=== RESUMEN ===\n")
cat(sprintf("  Pre-%s : %d meses\n", CUTOFF, meses_pre))
cat(sprintf("  Post-%s: %d meses\n", CUTOFF, meses_post))
cat("\n  Hojas por periodo:\n")
print(resumen_tipos %>% select(tipo_hoja, periodo, n_meses, cobertura_pct, ncol_mediana))
cat("\n  Etiquetas exclusivas por periodo:\n")
exclusivas <- bind_rows(
  n_exclusivas_pre  %>% mutate(estado = "exclusiva_pre"),
  n_exclusivas_post %>% mutate(estado = "exclusiva_post"),
  n_comunes         %>% mutate(estado = "comun")
)
print(exclusivas %>% pivot_wider(names_from = estado, values_from = n, values_fill = 0))
cat("\nArtefactos en _analisis/:\n")
cat("  - inventario_estructural.csv\n")
cat("  - resumen_hojas_por_periodo.csv\n")
cat("  - cambios_columnas_pre_post.csv\n")
if (nrow(cob_wide) > 0) cat("  - cobertura_por_columna_periodo.csv\n")
cat("  - informe_asimetria_pre2023.md\n\n")

invisible(NULL)
