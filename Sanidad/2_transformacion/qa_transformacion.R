# =============================================================================
# Sanidad · Canarias en Datos — QA de la etapa de TRANSFORMACIÓN
# Perfil de columnas de ced_sanidad, cobertura, equilibrio por género y
# validación del único índice sintético (mortalidad evitable).
# Salidas: 2_transformacion/qa/qa_ced_sanidad.csv + informe por consola.
# =============================================================================

suppressPackageStartupMessages({ require_packages(c("dplyr", "glue")); library(dplyr); library(glue) })

qa_transformacion <- function(cfg) {
  qa_dir <- file.path(cfg$transform_dir, "qa"); ensure_dir(qa_dir)
  ced <- readRDS(file.path(cfg$transform_dir, "ced_sanidad.rds"))
  KEYS <- c("ccaa", "periodo", "genero")

  # Perfil por columna (indicadores numéricos)
  ind_cols <- setdiff(names(ced), c(KEYS, "origen_pib"))
  perfil <- purrr::map_dfr(ind_cols, function(col) {
    v <- ced[[col]]
    data.frame(
      columna = col,
      con_dato = sum(!is.na(v)),
      na_pct = round(100 * mean(is.na(v)), 1),
      min = round(suppressWarnings(min(v, na.rm = TRUE)), 2),
      mediana = round(suppressWarnings(median(v, na.rm = TRUE)), 2),
      max = round(suppressWarnings(max(v, na.rm = TRUE)), 2),
      anio_min = suppressWarnings(min(ced$periodo[!is.na(v)])),
      anio_max = suppressWarnings(max(ced$periodo[!is.na(v)])),
      stringsAsFactors = FALSE
    )
  })
  write.csv(perfil, file.path(qa_dir, "qa_ced_sanidad.csv"), row.names = FALSE)

  # Chequeos clave
  gbal <- table(ced$genero)
  dup <- ced |> count(across(all_of(KEYS))) |> filter(.data$n > 1) |> nrow()
  sys_cols <- c("med_ae","med_ap","enf_ae","enf_ap","camas","gasto_farmacia_pct",
                "pct_pib_sanidad","espera_quir","espera_ae")
  sys_on_hm <- sapply(intersect(sys_cols, names(ced)), function(c)
    sum(!is.na(ced[[c]][ced$genero != "total"])))
  idx_gen <- ced |> filter(!is.na(mort_evitable_idx)) |> distinct(genero) |> pull(genero)

  cat("\n=================== QA TRANSFORMACIÓN — ced_sanidad ===================\n")
  cat(sprintf("Filas: %d | Columnas: %d | CCAA: %d | Periodo: %d-%d\n",
              nrow(ced), ncol(ced), n_distinct(ced$ccaa), min(ced$periodo), max(ced$periodo)))
  cat(sprintf("Claves duplicadas (ccaa,periodo,genero): %d %s\n", dup, ifelse(dup==0,"✓","✗")))
  cat(sprintf("Equilibrio por género — total:%d hombres:%d mujeres:%d\n", gbal["total"], gbal["hombres"], gbal["mujeres"]))
  cat(sprintf("Índice mort. evitable presente en géneros: %s\n", paste(sort(idx_gen), collapse=", ")))
  cat(sprintf("Indicadores de sistema con valor en filas H/M (debe ser 0): %s\n",
              paste(sprintf("%s=%d", names(sys_on_hm), sys_on_hm), collapse=" | ")))
  cat("\n--- Perfil de columnas ---\n")
  print(as.data.frame(perfil), row.names = FALSE)
  cat("\n=====================================================================\n")
  invisible(perfil)
}
