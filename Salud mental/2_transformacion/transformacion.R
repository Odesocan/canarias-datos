suppressPackageStartupMessages({
  require_packages(c("dplyr", "glue", "purrr", "stringr", "tibble", "tidyr"))
  library(dplyr)
  library(glue)
  library(purrr)
  library(stringr)
  library(tibble)
  library(tidyr)
})

# ----------------------------------------------------------------------------
# Helpers de género — siempre "genero", nunca "sexo"
# ----------------------------------------------------------------------------

normalize_genero <- function(x) {
  raw <- tolower(trimws(as.character(x)))
  dplyr::case_when(
    raw %in% c("total", "ambos sexos", "ambos") ~ "total",
    raw %in% c("hombres", "hombre", "varones", "varón", "varon", "h") ~ "hombres",
    raw %in% c("mujeres", "mujer", "m") ~ "mujeres",
    TRUE ~ NA_character_
  )
}

parse_suicidios_nombre <- function(nombre) {
  genero <- sub("^.*?,\\s*([^,]+)$", "\\1", nombre)
  nombre_sin_genero <- sub(",\\s*[^,]+$", "", nombre)
  edad <- sub("^.*?,\\s*([^,]+)$", "\\1", nombre_sin_genero)
  ccaa <- sub(",\\s*[^,]+$", "", nombre_sin_genero)

  tibble::tibble(
    ccaa_raw = ccaa,
    edad = edad,
    genero = normalize_genero(genero)
  )
}

# ----------------------------------------------------------------------------
# Tidy de cada raw INCLASNS
# ----------------------------------------------------------------------------

tidy_sns_indicator <- function(raw, value_name) {
  assert_required_columns(
    raw,
    c("ccaa_raw", "anio", "sexo", "valor"),
    sprintf("INCLASNS %s", value_name)
  )

  raw |>
    dplyr::mutate(
      ccaa = normalize_ccaa_name(.data$ccaa_raw),
      genero = normalize_genero(.data$sexo),
      periodo = suppressWarnings(as.integer(.data$anio)),
      !!value_name := suppressWarnings(as.numeric(.data$valor))
    ) |>
    dplyr::filter(
      !is.na(.data$genero),
      !is.na(.data$periodo),
      !is.na(.data[[value_name]]),
      .data$ccaa %in% official_ccaa_levels(include_national = TRUE)
    ) |>
    dplyr::group_by(.data$ccaa, .data$periodo, .data$genero) |>
    dplyr::summarise(
      !!value_name := mean(.data[[value_name]], na.rm = TRUE),
      .groups = "drop"
    )
}

# ----------------------------------------------------------------------------
# Imputación: Total para t_mental no viene de la API (siempre NaN). Se calcula
# como promedio ponderado por censo de los valores Hombres y Mujeres.
# ----------------------------------------------------------------------------

add_total_via_censo <- function(df, value_col, censo_df) {
  base <- df |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    dplyr::inner_join(
      dplyr::filter(censo_df, .data$genero %in% c("hombres", "mujeres")),
      by = c("ccaa", "periodo", "genero")
    ) |>
    dplyr::group_by(.data$ccaa, .data$periodo) |>
    dplyr::summarise(
      !!value_col := sum(.data[[value_col]] * .data$censo, na.rm = TRUE) /
        sum(.data$censo, na.rm = TRUE),
      .groups = "drop"
    ) |>
    dplyr::mutate(genero = "total") |>
    dplyr::select(dplyr::all_of(c("ccaa", "periodo", "genero", value_col)))

  dplyr::bind_rows(df, base)
}

# ----------------------------------------------------------------------------
# Imputación de género para fármacos (DHD) a partir de la prevalencia de
# trastornos mentales por sexo (estructura del cuaderno metodológico CED-01).
#
# Supuesto: el consumo por habitante guarda entre sexos la misma razón que la
# prevalencia, razon = t_mental mujeres / t_mental hombres, en cada CCAA y año.
# Con la población de cada sexo como peso, el total publicado es
#   total = (h × pob_h + m × pob_m) / (pob_h + pob_m),  con m = razon × h
# de donde
#   h = total × (pob_h + pob_m) / (pob_h + razon × pob_m)
#   m = razon × h
# Es la misma ponderación con la que se construye el total de t_mental.
#
# La fórmula anterior (h = total × (1 − b), m = total × (1 + b), con
# b = (m − h) / m de la prevalencia) no conservaba la razón: la del consumo
# salía en torno a 3 cuando la de la prevalencia era 2, así que la brecha del
# consumo quedaba exagerada.
# ----------------------------------------------------------------------------

impute_gender_with_ratio <- function(total_df, t_mental_df, censo_df, value_col) {
  razon <- t_mental_df |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    dplyr::select("ccaa", "periodo", "genero", "t_mental") |>
    tidyr::pivot_wider(names_from = "genero", values_from = "t_mental") |>
    dplyr::transmute(
      ccaa = .data$ccaa,
      periodo = .data$periodo,
      razon = dplyr::if_else(
        !is.na(.data$hombres) & .data$hombres > 0 & !is.na(.data$mujeres),
        .data$mujeres / .data$hombres,
        NA_real_
      )
    )

  poblacion <- censo_df |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    dplyr::select("ccaa", "periodo", "genero", "censo") |>
    tidyr::pivot_wider(names_from = "genero", values_from = "censo", names_prefix = "pob_")

  base <- total_df |>
    dplyr::filter(.data$genero == "total") |>
    dplyr::select("ccaa", "periodo", value_total = !!value_col) |>
    dplyr::inner_join(razon, by = c("ccaa", "periodo")) |>
    dplyr::inner_join(poblacion, by = c("ccaa", "periodo")) |>
    dplyr::filter(!is.na(.data$razon), .data$pob_hombres > 0, .data$pob_mujeres > 0) |>
    dplyr::mutate(
      valor_h = .data$value_total * (.data$pob_hombres + .data$pob_mujeres) /
        (.data$pob_hombres + .data$razon * .data$pob_mujeres),
      valor_m = .data$razon * .data$valor_h
    )

  hombres <- base |>
    dplyr::transmute(
      ccaa = .data$ccaa,
      periodo = .data$periodo,
      genero = "hombres",
      !!value_col := .data$valor_h
    )

  mujeres <- base |>
    dplyr::transmute(
      ccaa = .data$ccaa,
      periodo = .data$periodo,
      genero = "mujeres",
      !!value_col := .data$valor_m
    )

  total_only <- total_df |>
    dplyr::filter(.data$genero == "total")

  dplyr::bind_rows(total_only, hombres, mujeres)
}

# ----------------------------------------------------------------------------
# Pipeline principal
# ----------------------------------------------------------------------------

run_transformacion <- function(cfg) {
  log_event("INFO", "Iniciando transformación")

  extracted <- load_named_rds(
    cfg$extraction_dir,
    c("sns_t_mental", "sns_antidep", "sns_hipno", "suicidios", "censo")
  )

  # ---- 1. Censo anual por CCAA × género (INE 56940) -----------------------
  censo_rec <- compute_annual_census(extracted$censo)
  log_series_coverage(censo_rec, "censo")

  # ---- 2. Trastornos mentales (Hombres/Mujeres → Total ponderado + brecha)
  t_mental <- tidy_sns_indicator(extracted$sns_t_mental, "t_mental") |>
    add_total_via_censo("t_mental", censo_rec)

  brecha <- t_mental |>
    dplyr::filter(.data$genero %in% c("hombres", "mujeres")) |>
    tidyr::pivot_wider(names_from = "genero", values_from = "t_mental") |>
    dplyr::mutate(
      brecha_rel = dplyr::if_else(
        !is.na(.data$mujeres) & .data$mujeres != 0,
        ((.data$mujeres - .data$hombres) / .data$mujeres) * 100,
        NA_real_
      )
    ) |>
    dplyr::select("ccaa", "periodo", "brecha_rel")

  t_mental <- t_mental |>
    dplyr::left_join(brecha, by = c("ccaa", "periodo"))

  # ---- 3. DHD antidepresivos / hipnosedantes (Total → imputar género) -----
  antidep_total <- tidy_sns_indicator(extracted$sns_antidep, "antidep_ajustado")
  hipno_total   <- tidy_sns_indicator(extracted$sns_hipno,   "hipno_ajustado")

  antidep_rec <- impute_gender_with_ratio(antidep_total, t_mental, censo_rec, "antidep_ajustado")
  hipno_rec   <- impute_gender_with_ratio(hipno_total,   t_mental, censo_rec, "hipno_ajustado")

  # ---- 4. Suicidios (INE 46688) -------------------------------------------
  suicidios_rec <- extracted$suicidios |>
    dplyr::rename_with(tolower) |>
    dplyr::mutate(parsed = purrr::map(.data$nombre, parse_suicidios_nombre)) |>
    tidyr::unnest("parsed") |>
    dplyr::transmute(
      ccaa = normalize_ccaa_name(.data$ccaa_raw),
      periodo = suppressWarnings(as.integer(.data$nombreperiodo)),
      genero = .data$genero,
      edad = .data$edad,
      suicidios = suppressWarnings(as.numeric(.data$valor))
    ) |>
    dplyr::filter(
      .data$edad == "Todas las edades",
      !is.na(.data$genero),
      !is.na(.data$periodo),
      !is.na(.data$suicidios),
      .data$ccaa %in% official_ccaa_levels(include_national = TRUE)
    ) |>
    dplyr::select("ccaa", "periodo", "genero", "suicidios")

  # ---- 5. Merge dimensional -----------------------------------------------
  ced_saludmental <- merge_metric_tables(
    list(t_mental, antidep_rec, hipno_rec, suicidios_rec, censo_rec),
    c("ccaa", "periodo", "genero")
  )

  # Recortamos a periodos en los que tenemos al menos uno de los indicadores
  # principales (no quedarnos con años en los que solo hay censo o suicidios
  # antiguos pre-2010 sin valor en el resto).
  metric_cols <- c("t_mental", "antidep_ajustado", "hipno_ajustado", "suicidios")
  ced_saludmental <- ced_saludmental |>
    dplyr::filter(
      rowSums(!is.na(dplyr::across(dplyr::all_of(metric_cols)))) > 0
    )

  ced_saludmental <- ced_saludmental |>
    dplyr::arrange(.data$ccaa, .data$periodo, .data$genero)

  assert_unique_keys(ced_saludmental, c("ccaa", "periodo", "genero"), "ced_saludmental")
  log_series_coverage(ced_saludmental, "ced_saludmental")
  log_table_quality(ced_saludmental, "ced_saludmental", c("periodo"))

  save_named_rds(list(ced_saludmental = ced_saludmental), cfg$transform_dir)
  log_event("OK", "Transformación completada")

  invisible(list(ced_saludmental = ced_saludmental))
}
