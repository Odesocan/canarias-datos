suppressPackageStartupMessages({
  require_packages(c("glue", "ineapir", "purrr", "httr", "jsonlite"))
  library(glue)
  library(ineapir)
  library(purrr)
})

# Descarga un indicador INCLASNS combinando los géneros pedidos.
# generos: vector de NULL (=Total agregado) y/o "hombres"/"mujeres".
fetch_sns_indicator <- function(codigo, label, generos = list(NULL)) {
  parts <- list()
  for (g in generos) {
    suffix <- if (is.null(g) || !nzchar(g)) "Total" else g
    log_event("API", glue("INCLASNS indicador={codigo} ({label}) sexo={suffix}"))
    df <- sns_get_indicador(codigo, sexo = g)
    parts[[length(parts) + 1L]] <- df
  }
  do.call(rbind, parts)
}

run_extraccion <- function(cfg) {
  log_event("INFO", "Iniciando extracción")

  # ---- 1. INCLASNS (Indicadores Clave del SNS) -----------------------------
  # t_mental (1365): la API solo expone valores numéricos por género (Total
  # siempre viene NaN). Recogemos hombre y mujer explícitamente.
  # NB: la API exige los valores "hombre" / "mujer" (singular, minúscula).
  sns_t_mental <- fetch_sns_indicator(
    cfg$sns_indicators$sns_t_mental$codigo,
    cfg$sns_indicators$sns_t_mental$label,
    generos = list("hombre", "mujer")
  )
  validate_raw_dataset("sns_t_mental", sns_t_mental)

  # DHD antidepresivos / hipnosedantes: solo expone Total. Una sola llamada
  # sin parámetro sexo (la API devuelve "Total" con valor numérico).
  sns_antidep <- fetch_sns_indicator(
    cfg$sns_indicators$sns_antidep$codigo,
    cfg$sns_indicators$sns_antidep$label,
    generos = list(NULL)
  )
  validate_raw_dataset("sns_antidep", sns_antidep)

  sns_hipno <- fetch_sns_indicator(
    cfg$sns_indicators$sns_hipno$codigo,
    cfg$sns_indicators$sns_hipno$label,
    generos = list(NULL)
  )
  validate_raw_dataset("sns_hipno", sns_hipno)

  # ---- 2. INE 46688 — suicidios -------------------------------------------
  log_event("API", glue("INE tabla {cfg$ine_tables$suicidios$id} — {cfg$ine_tables$suicidios$label}"))
  suicidios <- ineapir::get_data_table(
    idTable = cfg$ine_tables$suicidios$id,
    tip = "A",
    unnest = TRUE
  )
  validate_raw_dataset("suicidios", suicidios)

  # ---- 3. INE 56940 — censo trimestral ------------------------------------
  log_event("API", glue("INE tabla {cfg$ine_tables$censo$id} — {cfg$ine_tables$censo$label}"))
  censo <- ineapir::get_data_table(
    idTable = cfg$ine_tables$censo$id,
    tip = "A",
    unnest = TRUE
  )
  validate_raw_dataset("censo", censo)

  # ---- Persistencia --------------------------------------------------------
  outputs <- list(
    sns_t_mental = sns_t_mental,
    sns_antidep = sns_antidep,
    sns_hipno = sns_hipno,
    suicidios = suicidios,
    censo = censo
  )

  save_named_rds(outputs, cfg$extraction_dir)
  log_event("OK", glue("Extracción completada: {length(outputs)} datasets"))

  invisible(outputs)
}
