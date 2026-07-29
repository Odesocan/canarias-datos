suppressPackageStartupMessages({
  library(dplyr)
  library(glue)
  library(janitor)
  library(purrr)
  library(stringr)
  library(tidyr)
  library(tibble)
})

run_transformacion <- function(cfg) {
  log_event("INFO", "Iniciando transformación")

  extracted <- load_named_rds(
    cfg$extraction_dir,
    c(
      "gasto_elevado",
      "gasto_elevado_gen",
      "dif_finmes",
      "dif_finmes_gen",
      "espacio_insuf",
      "espacio_insuf_gen",
      "retrasos_pagos",
      "retrasos_pagos_gen",
      "hogares_mono",
      "salario_mediano",
      "precio_venta_historico",
      "precio_venta_mensual",
      "precio_alquiler_historico",
      "precio_alquiler_mensual"
    )
  )

  gasto_total <- transform_ine_geo_table(extracted$gasto_elevado, "gasto_elevado")
  gasto_gap <- transform_ine_gender_table(extracted$gasto_elevado_gen, "gasto_elevado")
  gasto_elevado <- impute_gender_series(gasto_total, gasto_gap, "gasto_elevado", "gasto_elevado")

  dif_total <- transform_ine_geo_table(extracted$dif_finmes, "dif_finmes")
  dif_gap <- transform_ine_gender_table(extracted$dif_finmes_gen, "dif_finmes")
  dif_finmes <- impute_gender_series(dif_total, dif_gap, "dif_finmes", "dif_finmes")

  espacio_total <- transform_ine_geo_table(extracted$espacio_insuf, "espacio_insuf")
  espacio_gap <- transform_ine_gender_table(extracted$espacio_insuf_gen, "espacio_insuf")
  espacio_insuf <- impute_gender_series(espacio_total, espacio_gap, "espacio_insuf", "espacio_insuf")

  retrasos_total <- transform_ine_geo_table(extracted$retrasos_pagos, "retrasos_pagos")
  retrasos_gap <- transform_ine_gender_table(extracted$retrasos_pagos_gen, "retrasos_pagos")
  retrasos_pagos <- impute_gender_series(retrasos_total, retrasos_gap, "retrasos_pagos", "retrasos_pagos")

  hogares_mono <- transform_hogares_mono(extracted$hogares_mono)
  salario_mediano <- transform_salario_mediano(extracted$salario_mediano)

  precio_venta_historico <- prepare_price_historic(extracted$precio_venta_historico, "precio_venta_m2")
  precio_venta_mensual <- prepare_price_monthly_proxy(extracted$precio_venta_mensual, "precio_venta_m2")
  precio_venta <- combine_price_series(precio_venta_historico, precio_venta_mensual, "precio_venta")

  precio_alquiler_historico <- prepare_price_historic(extracted$precio_alquiler_historico, "precio_alquiler_m2")
  precio_alquiler_mensual <- prepare_price_monthly_proxy(extracted$precio_alquiler_mensual, "precio_alquiler_m2")
  precio_alquiler <- combine_price_series(precio_alquiler_historico, precio_alquiler_mensual, "precio_alquiler")

  outputs <- list(
    dif_finmes = dif_finmes,
    espacio_insuf = espacio_insuf,
    gasto_elevado = gasto_elevado,
    hogares_mono = hogares_mono,
    precio_alquiler = precio_alquiler,
    precio_venta = precio_venta,
    retrasos_pagos = retrasos_pagos,
    salario_mediano = salario_mediano
  )

  purrr::iwalk(outputs, function(df, name) {
    key_cols <- intersect(c("ccaa", "periodo", "genero"), names(df))
    assert_unique_keys(df, key_cols, label = name)
  })

  log_series_coverage(outputs$salario_mediano, "salario_mediano")
  log_series_coverage(outputs$precio_alquiler, "precio_alquiler")
  log_series_coverage(outputs$precio_venta, "precio_venta")

  save_named_rds(outputs, cfg$transform_dir)
  log_event("OK", glue("Transformación completada: {length(outputs)} datasets"))

  invisible(outputs)
}
