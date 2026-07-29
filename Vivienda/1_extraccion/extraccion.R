suppressPackageStartupMessages({
  library(dplyr)
  library(glue)
  library(ineapir)
  library(janitor)
  library(purrr)
  library(readr)
  library(readxl)
  library(tidyr)
})

download_ine_workbook <- function(url) {
  destfile <- tempfile(fileext = ".xlsx")
  utils::download.file(url, destfile = destfile, mode = "wb", quiet = TRUE)
  destfile
}

read_ine_sheet2 <- function(url) {
  path <- download_ine_workbook(url)
  on.exit(unlink(path), add = TRUE)
  suppressMessages(readxl::read_excel(path, sheet = 2))
}

read_raw_or_previous_price <- function(cfg, raw_name, dataset_name) {
  raw_path <- cfg$raw_files[[raw_name]]
  if (!is.null(raw_path) && file.exists(raw_path)) {
    return(suppressMessages(readr::read_csv(raw_path, show_col_types = FALSE)))
  }

  previous_path <- file.path(cfg$extraction_dir, paste0(dataset_name, ".rds"))
  if (file.exists(previous_path)) {
    log_event("WARN", glue("{dataset_name}: sin raw nuevo; se reutiliza RDS previo"))
    return(readRDS(previous_path))
  }

  stop(
    glue("{dataset_name}: no hay raw nuevo ni RDS previo en {previous_path}"),
    call. = FALSE
  )
}

run_extraccion <- function(cfg) {
  log_event("INFO", "Iniciando extracción")
  assert_raw_inputs(cfg)

  raw_prices <- list(
    precio_venta_historico = read_raw_or_previous_price(cfg, "venta_historico", "precio_venta_historico"),
    precio_venta_mensual = read_raw_or_previous_price(cfg, "venta_mensual", "precio_venta_mensual"),
    precio_alquiler_historico = read_raw_or_previous_price(cfg, "alquiler_historico", "precio_alquiler_historico"),
    precio_alquiler_mensual = read_raw_or_previous_price(cfg, "alquiler_mensual", "precio_alquiler_mensual")
  )

  datasets <- c(
    raw_prices,
    list(
      gasto_elevado = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D125_ICV_geo_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=73%2F135%2F125_ICV_geo_24.xlsx&ssbinary=true"),
      gasto_elevado_gen = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D125_ICV_indiv_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=708%2F233%2F125_ICV_indiv_24.xlsx&ssbinary=true"),
      dif_finmes = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D121_ICV_geo_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=69%2F681%2F121_ICV_geo_24.xlsx&ssbinary=true"),
      dif_finmes_gen = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D121_ICV_indiv_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=960%2F647%2F121_ICV_indiv_24.xlsx&ssbinary=true"),
      espacio_insuf = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D124_ICV_geo_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=584%2F527%2F124_ICV_geo_24.xlsx&ssbinary=true"),
      espacio_insuf_gen = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D124_ICV_indiv_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=259%2F593%2F124_ICV_indiv_24.xlsx&ssbinary=true"),
      retrasos_pagos = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D133_ICV_geo_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=614%2F16%2F133_ICV_geo_24.xlsx&ssbinary=true"),
      retrasos_pagos_gen = read_ine_sheet2("https://www.ine.es/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition&blobheadervalue1=attachment%3B+filename%3D133_ICV_indiv_24.xlsx&blobkey=urldata&blobtable=MungoBlobs&blobwhere=417%2F46%2F133_ICV_indiv_24.xlsx&ssbinary=true"),
      hogares_mono = {
        hogares_path <- tempfile(fileext = ".csv")
        on.exit(unlink(hogares_path), add = TRUE)
        utils::download.file(
          "https://www.ine.es/jaxi/files/_px/es/csv_bdsc/t20/p274/serie/def/p02/l0/02015.csv_bdsc?nocab=1",
          destfile = hogares_path,
          mode = "wb",
          quiet = TRUE
        )
        suppressMessages(readr::read_csv2(hogares_path, show_col_types = FALSE))
      },
      salario_mediano = ineapir::get_data_table(idTable = 28191, tip = "A", unnest = TRUE)
    )
  )

  save_named_rds(datasets, cfg$extraction_dir)
  log_event("OK", glue("Extracción completada: {length(datasets)} datasets"))

  invisible(datasets)
}
