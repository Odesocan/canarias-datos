# Presupuestos por anualidad extraídos · ODESOCAN Canarias en Datos

**Fecha:** 2026-06-25 (Noche 29) · **Fuente:** `outputs/smoke_regresion_py.csv` (catálogo autoritativo)

Salud verificada esta noche en aislado (sin regresión, mount estable): `pvc/2025`=122, `ara/2017`=167, `and/2015`=114, `mur/2025`=106 filas — todos cuadran con el catálogo. Sin cambios de cobertura respecto a la Noche 28 (no hay raws nuevos descargables; ver §3).

## 1 · Matriz de cobertura (ejercicios extraídos en VERDE)

`✓` extraído y verificado · `·` sin extraer (falta raw válido) · `✗` ERROR (raw no es la tabla programa+total)

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | **n** |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Andalucía (and) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **12** |
| Aragón (ara) | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **11** |
| Asturias (ast) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | **11** |
| Baleares (bal) | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | **10** |
| Canarias (can) | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| Cataluña (cat) | ✓ | ✓ | ✓ | · | ✓ | ✓ | · | ✓ | ✓ | ✓ | · | ✓ | **9** |
| Cast.-La Mancha (clm) | · | · | · | · | · | · | · | · | · | ✓ | ✓ | ✓ | **3** |
| Cantabria (cnt) | · | · | · | · | · | · | · | · | · | · | ✓ | · | **1** |
| Cast. y León (cym) | · | · | · | · | · | · | · | · | · | · | · | ✓ | **1** |
| Extremadura (ext) | · | · | · | · | · | · | · | · | · | · | ✓ | ✓ | **2** |
| Galicia (gal) | · | · | · | · | · | · | · | · | · | · | ✓ | · | **1** |
| La Rioja (lar) | · | · | · | · | · | · | · | · | · | · | ✓ | · | **1** |
| Madrid (mad) | · | · | · | · | · | · | · | · | · | · | · | ✓ | **1** |
| Murcia (mur) | · | · | · | · | · | · | · | · | · | · | ✓ | · | **1** |
| Navarra (nav) | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| País Vasco (pvc) | · | · | · | · | · | · | · | ✓ | · | ✓ | ✓ | ✓ | **4** |
| C. Valenciana (val) | · | · | · | · | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | **5** |
| **Σ CCAA/año** | **5** | **4** | **4** | **6** | **7** | **7** | **6** | **8** | **8** | **10** | **14** | **12** | **91** |

**Total: 91 ejercicios-año en VERDE · 17/17 CCAA · 1 ERROR (ara/2016).**

## 2 · Presupuesto total consolidado por anualidad (millones €)

Totales del **presupuesto consolidado de gastos** (capa Hacienda / SGCIEF), completos para las 17 CCAA en 2015–2025. Sirven de referencia de conciliación frente a la extracción programa-a-programa de la Tabla 1 (capa autonómica). 2026 aún sin consolidar por Hacienda.

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|------|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andalucía (and) | 29,626 | 31,290 | 33,245 | 34,769 | 36,501 | 38,546 | 40,188 | 40,402 | 45,604 | 46,753 | 48,872 |
| Aragón (ara) | 5,254 | 5,130 | 5,577 | 6,162 | 6,162 | 6,467 | 7,454 | 7,444 | 8,250 | 8,546 | 8,546 |
| Asturias (ast) | 3,959 | 3,954 | 4,226 | 4,213 | 4,524 | 4,757 | 5,238 | 5,354 | 5,968 | 6,349 | 6,664 |
| Baleares (bal) | 4,036 | 4,241 | 4,668 | 5,009 | 5,458 | 5,893 | 5,882 | 6,398 | 7,133 | 7,321 | 7,469 |
| Canarias (can) | 6,901 | 7,265 | 7,339 | 8,273 | 8,833 | 9,603 | 9,531 | 9,974 | 11,059 | 11,971 | 12,343 |
| Cataluña (cat) | 32,618 | 32,608 | 34,164 | 34,121 | 34,119 | 42,323 | 42,323 | 49,012 | 51,808 | 51,828 | 50,605 |
| Cast.-La Mancha (clm) | 8,206 | 8,420 | 8,941 | 9,219 | 9,219 | 10,505 | 12,102 | 12,274 | 12,432 | 12,473 | 12,716 |
| Cantabria (cnt) | 2,501 | 2,465 | 2,603 | 2,731 | 2,854 | 2,888 | 3,078 | 3,343 | 3,507 | 3,548 | 3,756 |
| Cast. y León (cym) | 9,921 | 9,844 | 10,293 | 10,859 | 10,785 | 10,753 | 12,291 | 12,291 | 13,810 | 14,562 | 14,562 |
| Extremadura (ext) | 5,366 | 5,197 | 5,172 | 5,434 | 5,798 | 6,006 | 6,424 | 7,000 | 7,781 | 8,127 | 8,098 |
| Galicia (gal) | 9,790 | 10,310 | 11,029 | 10,724 | 11,544 | 11,822 | 13,397 | 13,118 | 14,167 | 14,815 | 15,741 |
| La Rioja (lar) | 1,287 | 1,337 | 1,456 | 1,519 | 1,488 | 1,575 | 1,891 | 1,950 | 1,909 | 1,974 | 2,115 |
| Madrid (mad) | 20,853 | 20,140 | 20,504 | 21,634 | 22,777 | 23,333 | 25,879 | 25,999 | 28,142 | 30,584 | 31,596 |
| Murcia (mur) | 4,642 | 4,916 | 5,093 | 5,515 | 5,800 | 6,197 | 6,754 | 6,963 | 7,771 | 7,819 | 8,037 |
| Navarra (nav) | 3,793 | 4,005 | 4,062 | 4,164 | 4,312 | 4,574 | 4,871 | 5,273 | 5,749 | 6,355 | 6,431 |
| País Vasco (pvc) | 10,701 | 10,995 | 11,125 | 11,579 | 11,220 | 11,857 | 12,522 | 13,187 | 14,362 | 15,147 | 15,811 |
| C. Valenciana (val) | 17,564 | 17,561 | 18,138 | 20,414 | 22,597 | 23,531 | 26,139 | 28,632 | 29,121 | 30,410 | 32,977 |

> Importes en millones de euros (presupuesto consolidado de gastos). Fuente: `outputs/importe_por_anio_2026-05-30.csv`.

## 3 · Candidatos de cobertura nueva — re-confirmados BLOQUEADOS (sin cambios desde mayo)

| Candidato | Raw en disco | Diagnóstico | Bloqueo |
|---|---|---|---|
| ast/2022 | `tomo_I.pdf` 19.8 MB (29-may) | Ley 6/2021 BOPA (articulado) → extracción da **0 filas** | Falta tomo "Distribución del gasto por programas" |
| bal/2017 | `secciones/titol*_d.pdf` = **34 B** c/u | Stubs de descargas 404 | Falta el PDF real de secciones |
| bal/2026 | `secciones/titol*_d.pdf` = **34 B** c/u | Stubs de descargas 404 | Falta el PDF real de secciones |
| gal/2026 | solo `portal_index.html` | El portal solo enlaza al dataset **0665/2025**; el 2026 aún no publicado por la Xunta | Dato no publicado aguas arriba |
| ara/2016 | `ingresos_gastos.pdf` 1.9 MB | Ley BOPA, no la tabla programa+total → **ERROR** | Falta el PDF programa+total |

Todos requieren descargar el raw correcto. En el sandbox `web_fetch` está restringido al *provenance set* (probado esta noche: el dataset 0665/2026 devuelve "URL not in provenance set") y no se permite `curl`/`wget`/`requests`. Sin descargas nuevas posibles aquí → pendiente de run con red estable fuera del sandbox.
