# Tabla resumen — Presupuestos autonómicos por anualidad extraída
**ODESOCAN · Canarias en Datos** — actualizado 2026-06-29 (Noche 31, 2.º run)

Fuente: catálogo vivo `outputs/smoke_regresion_py.csv` (extractores Python verificados en aislado).
Cada celda = nº de filas-programa extraídas en VERDE. `E` = ERROR (raw no es la tabla programa+total). `·` = año sin fuente extraíble.

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | **Años** |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| **and** Andalucía | 114 | 115 | 102 | 102 | 103 | 111 | 112 | 97 | 88 | 88 | 88 | 88 | **12** |
| **ara** Aragón | 163 | E | 167 | 160 | 160 | 166 | 187 | 182 | 182 | 198 | 198 | 198 | **11** |
| **ast** Asturias | 107 | 91 | 91 | 90 | 90 | 95 | 96 | · | 96 | 104 | 105 | 104 | **11** |
| **bal** Baleares | 54 | 73 | · | 82 | 86 | 95 | 89 | 143 | 150 | 145 | 141 | · | **10** |
| **can** Canarias | · | · | · | 140 | 142 | 144 | 141 | 135 | 135 | 140 | 141 | 143 | **9** |
| **cat** Cataluña | 96 | 103 | 103 | · | 105 | 105 | · | 105 | 105 | 105 | · | 106 | **9** |
| **clm** Cast.-La Mancha | · | · | · | · | · | · | · | · | · | 114 | 113 | 113 | **3** |
| **cnt** Cantabria | · | · | · | · | · | · | · | · | · | · | 91 | · | **1** |
| **cym** Cast. y León | · | · | · | · | · | · | · | · | · | · | · | 103 | **1** |
| **ext** Extremadura | · | · | · | · | · | · | · | · | · | · | 74 | 73 | **2** |
| **gal** Galicia | · | · | · | · | · | · | · | · | · | · | 47 | · | **1** |
| **lar** La Rioja | · | · | · | · | · | · | · | · | · | · | 56 | · | **1** |
| **mad** Madrid | · | · | · | · | · | · | · | · | · | · | · | 103 | **1** |
| **mur** Murcia | · | · | · | · | · | · | · | · | · | · | 106 | · | **1** |
| **nav** Navarra | · | · | · | 172 | 167 | 170 | 170 | 170 | 169 | 167 | 168 | 167 | **9** |
| **pvc** País Vasco | · | · | · | · | · | · | · | 116 | · | 118 | 122 | 122 | **4** |
| **val** C. Valenciana | · | · | · | · | · | · | · | 169 | 174 | 173 | 174 | 176 | **5** |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| **CCAA/año** | 5 | 4 | 4 | 6 | 7 | 7 | 6 | 8 | 8 | 10 | 14 | 12 | **91** |

**Cobertura total: 91 ejercicios-año en VERDE · 17/17 CCAA · 1 ERROR (ara/2016).**

## Detalle por CCAA (años VERDE · motor · conceptos)

| CCAA | Años VERDE | N.º años | Motor | Máx. conceptos |
|------|-----------|:------:|-------|:------:|
| **and** Andalucía | 2015–2026 | 12 | `and-ckan-csv` | 12/13 |
| **ara** Aragón | 2015, 2017–2026 (2016 E) | 11 | `ara-pdf-program-total` | 11/13 |
| **ast** Asturias | 2015–2021, 2023–2026 | 11 | `ast-distribucion-gasto` | 10/13 |
| **bal** Baleares | 2015–2016, 2018–2025 | 10 | `bal-frameset-secciones` | 13/13 |
| **can** Canarias | 2018–2026 | 9 | `can-tomo3-resumen-programas` | 13/13 |
| **cat** Cataluña | 2015–2017, 2019–2020, 2022–2024, 2026 | 9 | `cat-programa-suma-secciones` | 13/13 |
| **clm** Cast.-La Mancha | 2024–2026 | 3 | `clm-tomo-I-resumen-secciones` | 13/13 |
| **cnt** Cantabria | 2025 | 1 | `cnt-total-programa-suma-servicios` | 12/13 |
| **cym** Cast. y León | 2026 | 1 | `cym-jcyl-xls` | 13/13 |
| **ext** Extremadura | 2025–2026 | 2 | `ext-tomo-eig-suma-capitulos` | 13/13 |
| **gal** Galicia | 2025 | 1 | `gal-csv-abertos-xunta` | 8/13 |
| **lar** La Rioja | 2025 | 1 | `lar-camelot-funcional-economico` | 11/13 |
| **mad** Madrid | 2026 | 1 | `mad-libro-03-centros` | 11/13 |
| **mur** Murcia | 2025 | 1 | `mur-html` | 10/13 |
| **nav** Navarra | 2018–2026 | 9 | `nav-breakdowns-functional` | 13/13 |
| **pvc** País Vasco | 2022, 2024–2026 | 4 | `pvc-csv-tidy` | 8/13 |
| **val** C. Valenciana | 2022–2026 | 5 | `val-rpc-secciones` | 13/13 |
