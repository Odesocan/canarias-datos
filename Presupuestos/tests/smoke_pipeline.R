#!/usr/bin/env Rscript
# ============================================================
# tests/smoke_pipeline.R — Prueba end-to-end con fixture local.
#
# Crea un escenario reproducible (sin red) con 3 CCAA y 2 ejercicios,
# ejecuta cada fase del pipeline y verifica:
#   - extracción produce manifest + staging
#   - transformación clasifica >0 filas y deja pendientes coherentes
#   - modelado calcula pct_pib_nacional, eur_per_capita, var_nominal_pct
#   - carga genera ced_presupuestos.csv/xlsx con la clave única
#
# Se ejecuta con: Rscript tests/smoke_pipeline.R
# ============================================================

suppressPackageStartupMessages({
  library(dplyr)
})

.resolve_proj <- function() {
  file_arg <- grep("^--file=", commandArgs(), value = TRUE)
  if (length(file_arg) > 0) {
    script_path <- sub("^--file=", "", file_arg[[1]])
    return(normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE))
  }
  normalizePath(file.path(getwd(), ".."), winslash = "/", mustWork = TRUE)
}
PROJECT <- if (exists("PROJECT_OVERRIDE")) PROJECT_OVERRIDE else .resolve_proj()
if (!file.exists(file.path(PROJECT, "00_maestro.R"))) {
  # Permite ejecutar desde la raíz del proyecto Presupuestos
  PROJECT <- normalizePath(file.path(getwd()), winslash = "/", mustWork = TRUE)
}
RAW_DIR <- file.path(PROJECT, "fuentes", "raw")
FUENTES_YML <- file.path(PROJECT, "fuentes.yml")

cat("[smoke] Proyecto:", PROJECT, "\n")

# 1) Preparar entorno limpio para el test ---------------------------------
artef <- c(file.path(PROJECT, "1_extraccion"),
           file.path(PROJECT, "2_transformacion"),
           file.path(PROJECT, "3_modelado"),
           file.path(PROJECT, "4_carga"))
for (d in artef) {
  rds <- list.files(d, pattern = "\\.rds$", full.names = TRUE)
  if (length(rds) > 0) file.remove(rds)
}
for (f in c("ced_presupuestos.csv","ced_presupuestos.xlsx")) {
  p <- file.path(PROJECT, "4_carga", f)
  if (file.exists(p)) file.remove(p)
}
manifest_log <- file.path(PROJECT, "logs", "manifest.jsonl")
if (file.exists(manifest_log)) file.remove(manifest_log)

# 2) Fixture: 3 CCAA × 2 años con un CSV pequeño cada uno -----------------
fixture_dir <- file.path(RAW_DIR, "_fixture_smoke")
dir.create(fixture_dir, recursive = TRUE, showWarnings = FALSE)

fixtures <- list(
  list(ccaa = "can", anio = 2024, alias = "smoke_can",
       rows = data.frame(
         codigo       = c("412","412A","313D","321","432","920","231G"),
         denominacion = c("Sanidad General",
                          "Servicio Canario de Salud",
                          "Atención a la Dependencia",
                          "Educación Infantil y Primaria",
                          "Promoción Turística",
                          "Igualdad — Instituto Canario de Igualdad",
                          "Programa de Discapacidad"),
         importe_eur  = c(3100000000,4200500000,520000000,1800000000,
                          180000000,28500000,310000000)
       )),
  list(ccaa = "can", anio = 2025, alias = "smoke_can",
       rows = data.frame(
         codigo       = c("412","412A","313D","321","432","920","231G"),
         denominacion = c("Sanidad General","Servicio Canario de Salud",
                          "Atención a la Dependencia",
                          "Educación Infantil y Primaria",
                          "Promoción Turística",
                          "Igualdad — Instituto Canario de Igualdad",
                          "Programa de Discapacidad"),
         importe_eur  = c(3275000000,4360100000,545000000,1880000000,
                          195000000,30100000,320000000)
       )),
  list(ccaa = "and", anio = 2024, alias = "smoke_and",
       rows = data.frame(
         codigo       = c("41A","41H","42","43A","32G","31P"),
         denominacion = c("Servicio Andaluz de Salud",
                          "Salud Mental Andalucía",
                          "Educación obligatoria",
                          "Vivienda — AVRA",
                          "Instituto Andaluz de la Mujer",
                          "Diversidad sexual y LGTBI"),
         importe_eur  = c(12800000000,650000000,7900000000,
                          410000000,55000000,12500000)
       )),
  list(ccaa = "and", anio = 2025, alias = "smoke_and",
       rows = data.frame(
         codigo       = c("41A","41H","42","43A","32G","31P"),
         denominacion = c("Servicio Andaluz de Salud","Salud Mental Andalucía",
                          "Educación obligatoria","Vivienda — AVRA",
                          "Instituto Andaluz de la Mujer","Diversidad sexual y LGTBI"),
         importe_eur  = c(13150000000,680000000,8200000000,
                          425000000,57000000,13100000)
       )),
  list(ccaa = "cat", anio = 2024, alias = "smoke_cat",
       rows = data.frame(
         codigo       = c("411","414","421","317","432","920"),
         denominacion = c("CatSalut — Atenció Primària",
                          "Salut Mental",
                          "Ensenyament obligatori",
                          "Atenció a la Dependència",
                          "Turisme Catalunya",
                          "Institut Català de les Dones"),
         importe_eur  = c(10500000000,580000000,
                          6900000000,720000000,
                          150000000,38000000)
       ))
)

# fuentes.yml temporal apuntando a los fixtures locales (capa autonomica)
fuentes_yml_test <- file.path(PROJECT, "tests", "_fuentes_smoke.yml")
yaml_lines <- c(
  "defaults:",
  "  user_agent: \"ODESOCAN-smoke/0.1\"",
  "  retries: 1",
  "  timeout_s: 5",
  ""
)

# Escribe los CSVs raw donde el pipeline los busca y construye yml
old_scipen <- getOption("scipen"); options(scipen = 999); on.exit(options(scipen = old_scipen), add = TRUE)
for (fx in fixtures) {
  destino_csv <- file.path(RAW_DIR, fx$ccaa, fx$anio, paste0(fx$alias, ".csv"))
  dir.create(dirname(destino_csv), recursive = TRUE, showWarnings = FALSE)
  # CSV con decimal "." (formato anglosajón sencillo) — extraccion.R
  # detecta el locale automáticamente
  utils::write.csv(fx$rows, destino_csv, row.names = FALSE, fileEncoding = "UTF-8")
}

# Una entrada por (ccaa, año, alias) en el yml temporal — URL local file://
for (cca in unique(vapply(fixtures, function(f) f$ccaa, character(1)))) {
  yaml_lines <- c(yaml_lines, paste0(cca, ":"), "  nombre: smoke", "  regimen: comun",
                  "  ejercicios:")
  for (anio in unique(vapply(Filter(function(f) f$ccaa == cca, fixtures),
                              function(f) as.integer(f$anio), integer(1)))) {
    alias_anio <- Filter(function(f) f$ccaa == cca && f$anio == anio, fixtures)
    yaml_lines <- c(yaml_lines, sprintf("    %d:", anio))
    for (entry in alias_anio) {
      csv_path <- file.path(RAW_DIR, cca, anio, paste0(entry$alias, ".csv"))
      yaml_lines <- c(yaml_lines, sprintf("      %s:", entry$alias),
                       "        tipo: csv",
                       sprintf("        url: \"file://%s\"", csv_path),
                       "        capa: autonomica",
                       "        consolidacion: consolidado")
    }
  }
}

# Capa Hacienda sintética: XLSX en fuentes/raw/hacienda/2024/
hacienda_dir <- file.path(RAW_DIR, "hacienda", "2024")
dir.create(hacienda_dir, recursive = TRUE, showWarnings = FALSE)
hacienda_xlsx <- file.path(hacienda_dir, "SGCIEF_2024.xlsx")
hacienda_html <- file.path(hacienda_dir, "consulta_web.html")
writeLines("<html><body>SGCIEF stub</body></html>", hacienda_html)
# Generamos el XLSX con un script Python sencillo (sin dependencias)
py_gen <- file.path(PROJECT, "tests", "_gen_hacienda_fixture.py")
writeLines(c(
  "from openpyxl import Workbook",
  "import sys",
  "wb = Workbook(); ws = wb.active; ws.title='Cap'",
  "ws.append(['CCAA','1. Personal','2. Bienes','3. Financieros','4. Transferencias corrientes','6. Inversiones reales','7. Transferencias capital','8. Activos','9. Pasivos'])",
  "for r in [('Andalucía',14500000000,4200000000,600000000,18000000000,2500000000,1200000000,200000000,1100000000),",
  "          ('Canarias',3100000000,1100000000,250000000,4500000000,800000000,300000000,80000000,280000000),",
  "          ('Cataluña',13800000000,4900000000,1200000000,17500000000,2200000000,950000000,300000000,4500000000)]:",
  "    ws.append(r)",
  "wb.save(sys.argv[1])"
), py_gen)
system2("python3", c(shQuote(py_gen), shQuote(hacienda_xlsx)))

yaml_lines <- c(yaml_lines,
  "hacienda:", "  nombre: \"Min Hacienda (smoke)\"",
  "  ejercicios:", "    2024:",
  "      consulta_web:",
  "        tipo: html",
  sprintf("        url: \"file://%s\"", hacienda_html),
  "        capa: hacienda",
  "        consolidacion: consolidado")

writeLines(yaml_lines, fuentes_yml_test)
cat("[smoke] Fixture yml escrito en", fuentes_yml_test, "\n")

# 3) Carga del pipeline con cfg apuntando al yml de smoke ----------------
source(file.path(PROJECT, "R", "ccaa_dictionary.R"))
source(file.path(PROJECT, "R", "pipeline_utils.R"))
source(file.path(PROJECT, "R", "correspondencias.R"))
source(file.path(PROJECT, "1_extraccion", "extraccion.R"))
source(file.path(PROJECT, "2_transformacion", "transformacion.R"))
source(file.path(PROJECT, "3_modelado", "modelado.R"))
source(file.path(PROJECT, "4_carga", "carga.R"))

smoke_with_db <- tolower(Sys.getenv("SMOKE_WITH_DB", "false")) %in% c("true","1","yes")
cfg <- build_pipeline_config(PROJECT, list(steps = "extraccion,transformacion,modelado,carga",
                                            "with-db" = if (smoke_with_db) "true" else "false"))
cfg$fuentes_yml <- fuentes_yml_test   # apuntar al fixture
cfg$horizon_year <- 2026L

# 4) Run paso a paso con asserts -----------------------------------------
expect_true <- function(cond, msg) {
  if (!isTRUE(cond)) stop(sprintf("[smoke FAIL] %s", msg), call. = FALSE)
  cat(sprintf("[smoke OK ] %s\n", msg))
}

cat("\n=== FASE 1 · Extracción ===\n")
run_extraccion(cfg)
manifest <- readRDS(file.path(cfg$extraction_dir, "manifest.rds"))
staging  <- readRDS(file.path(cfg$extraction_dir, "staging_gasto.rds"))
# manifest debe contener fixtures + 1 entrada hacienda
expect_true(nrow(manifest) >= length(fixtures) + 1,
            sprintf("manifest tiene %d filas (>= %d esperado)", nrow(manifest), length(fixtures)+1))
expected_min_rows <- sum(vapply(fixtures, function(f) nrow(f$rows), integer(1))) + 3*8
expect_true(nrow(staging) >= expected_min_rows,
            sprintf("staging tiene %d filas (>= %d esperado, incluye Hacienda)",
                    nrow(staging), expected_min_rows))
expect_true(all(c("codigo","denominacion","importe_eur","ccaa","ccaa_id3","anio","capa") %in% names(staging)),
            "staging contiene las columnas requeridas")
expect_true("hacienda" %in% unique(staging$capa),
            "staging incluye capa Hacienda")

cat("\n=== FASE 2 · Transformación ===\n")
run_transformacion(cfg)
norm <- readRDS(file.path(cfg$transform_dir, "gasto_normalizado.rds"))
pend <- readRDS(file.path(cfg$transform_dir, "pendientes_revision.rds"))
expect_true(nrow(norm) > 0, sprintf("gasto_normalizado tiene %d filas", nrow(norm)))
expect_true(all(norm$concepto %in% names(yaml::read_yaml(cfg$correspondencias_yml)$conceptos)),
            "todos los conceptos asignados existen en correspondencias.yml")
n_pend <- nrow(pend); n_total <- nrow(staging)
expect_true(n_pend <= n_total * 0.20,
            sprintf("pendientes (%d) ≤ 20%% del total (%d)", n_pend, n_total))

cat("\n=== FASE 3 · Modelado ===\n")
run_modelado(cfg)
ced <- readRDS(file.path(cfg$model_dir, "ced_presupuestos.rds"))
expect_true(nrow(ced) > 0, sprintf("ced_presupuestos modelado tiene %d filas", nrow(ced)))
expect_true(all(c("ccaa","periodo","genero","origen","capa") %in% names(ced)),
            "ced_presupuestos contiene la clave canónica")
pib_cols <- grep("^pib_", names(ced), value = TRUE)
imp_cols <- grep("^imp_", names(ced), value = TRUE)
pc_cols  <- grep("^pc_",  names(ced), value = TRUE)
expect_true(length(imp_cols) > 0, sprintf("imp_* cols=%d", length(imp_cols)))
expect_true(length(pib_cols) > 0, sprintf("pib_* cols=%d", length(pib_cols)))
expect_true(length(pc_cols) > 0,  sprintf("pc_* cols=%d", length(pc_cols)))

# % PIB nacional: Sanidad Canarias 2024 ~ 4.2B / 1.59T ≈ 0.26%
sanity <- ced |> filter(ccaa == "Canarias", periodo == 2024L)
if (nrow(sanity) > 0 && "pib_sanidad" %in% names(sanity)) {
  v <- sanity$pib_sanidad[1]
  expect_true(!is.na(v) && v > 0 && v < 5,
              sprintf("pct_pib_nacional sanidad Canarias 2024 = %.3f%%", v))
}

cat("\n=== FASE 4 · Carga (sin DB) ===\n")
run_carga(cfg)
csv_out <- file.path(cfg$load_dir, "ced_presupuestos.csv")
xlsx_out <- file.path(cfg$load_dir, "ced_presupuestos.xlsx")
expect_true(file.exists(csv_out),  "ced_presupuestos.csv escrito")
expect_true(file.exists(xlsx_out), "ced_presupuestos.xlsx escrito")
ced_csv <- readr::read_csv2(csv_out, show_col_types = FALSE)
expect_true(nrow(ced_csv) == nrow(ced),
            sprintf("CSV tiene %d filas (RDS %d)", nrow(ced_csv), nrow(ced)))

cat("\n[smoke] === Todas las fases superadas ===\n")
