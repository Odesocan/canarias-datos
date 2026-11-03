# Validacion contra los valores de referencia de Cristian (paso 4)
suppressPackageStartupMessages({library(dplyr)})
dir <- commandArgs(TRUE)[1]
rd <- function(n) readRDS(file.path(dir, paste0(n, ".rds")))
dict <- rd("dictsaad_all"); ben <- rd("benpresaad_all"); bef <- rd("benefect_full")
pg <- rd("pend_grado"); pp <- rd("pend_pia"); te <- rd("tiempo_espera"); di <- rd("dashboard_indicators")
if ("origen" %in% names(di)) di <- di %>% filter(origen == "real")
f <- function(x) as.Date(paste0(x, "-01"))
base <- function(fecha_, ambito) {
  sel <- function(d) { d <- d %>% filter(fecha == f(fecha_)); if (ambito == "Canarias") d %>% filter(ccaa == "Canarias") else d }
  tibble(
    mes = fecha_, ambito = ambito, n_ccaa = nrow(sel(dict)),
    solicitudes = sum(sel(dict)$solicitudes), resol_grado = sum(sel(dict)$resoluciones_grado),
    con_derecho = sum(sel(dict)$total_der_prest), con_pia = sum(sel(bef)$personas_con_pia),
    prest_efectiva = sum(sel(bef)$personas_prest_efectiva),
    pe_cuid_fam = sum(sel(ben)$pe_cuidados_fam), total_prest = sum(sel(ben)$total)
  )
}
obs <- bind_rows(base("2026-03", "Canarias"), base("2026-09", "Canarias"), base("2026-09", "España"))
esp <- tribble(~mes, ~ambito, ~solicitudes, ~resol_grado, ~con_derecho, ~con_pia, ~prest_efectiva,
  "2026-03", "Canarias", 83951, 80739, 71932, 71093, 55032,
  "2026-09", "Canarias", 91922, 89676, 80132, 79828, 67740,
  "2026-09", "España", 2421624, 2335648, 1899661, 1782644, 1748901)
chk <- list()
add <- function(nombre, obtenido, esperado, tol = 0) chk[[length(chk) + 1]] <<- tibble(control = nombre, obtenido = obtenido, esperado = esperado, ok = abs(obtenido - esperado) <= tol)
for (i in seq_len(nrow(esp))) for (v in c("solicitudes", "resol_grado", "con_derecho", "con_pia", "prest_efectiva")) {
  o <- obs %>% filter(mes == esp$mes[i], ambito == esp$ambito[i])
  add(sprintf("%s %s %s", esp$mes[i], esp$ambito[i], v), o[[v]], esp[[v]][i])
}
can <- function(d, m) d %>% filter(ccaa == "Canarias", fecha == f(m))
for (m in c("2026-03", "2026-09")) {
  e <- if (m == "2026-03") c(3212, 839, 16061, 26.55) else c(2246, 304, 12088, 29.81)
  add(paste(m, "Canarias pendientes_grado_total"), can(pg, m)$pendientes_grado_total[1], e[1])
  add(paste(m, "Canarias pendientes_pia_total"), can(pp, m)$pendientes_pia_total[1], e[2])
  add(paste(m, "Canarias pendientes_prest_efectiva"), can(bef, m)$pendientes_prest_efectiva[1], e[3])
  add(paste(m, "Canarias cobertura_pct_ppd"), round(can(di, m)$cobertura_pct_ppd[1], 2), e[4])
}
add("2026-09 Canarias limbo_prestaciones_pct_ppd", round(can(di, "2026-09")$limbo_prestaciones_pct_ppd[1], 2), 4.51)
add("2026-09 Canarias pe_cuidados_fam", can(ben, "2026-09")$pe_cuidados_fam[1], 35533)
add("2026-09 Canarias total prestaciones", can(ben, "2026-09")$total[1], 100565)
add("2026-09 Canarias pct_pecef", round(can(di, "2026-09")$pct_pecef[1], 2), 35.33)
add("2026-09 Canarias tiempo sol->prestacion (dias)", can(te, "2026-09")$tiempo_espera_total_dias[1], 214)
add("2026-09 España pe_cuidados_fam", obs$pe_cuid_fam[3], 809815)
add("2026-09 España total prestaciones", obs$total_prest[3], 2582569)
add("2026-09 España n_ccaa (17 + Ceuta y Melilla)", obs$n_ccaa[3], 18)
ppd <- rd("censo_ppd") %>% filter(periodo == 2026)
add("PPD 2026 Canarias", round(ppd$ppd[ppd$ccaa == "Canarias"]), 267797)
add("PPD 2026 suma CCAA", floor(sum(ppd$ppd)), 6689939)
res <- bind_rows(chk)
print(as.data.frame(res), right = FALSE)
cat(sprintf("\n%d/%d controles OK\n", sum(res$ok), nrow(res)))
if (!all(res$ok)) quit(status = 1)
