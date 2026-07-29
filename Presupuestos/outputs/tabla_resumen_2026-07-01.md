# Tabla resumen — Presupuestos autonómicos por anualidad extraída
**ODESOCAN · Canarias en Datos** — actualizado 2026-07-01 (run nocturno automatizado)

Fuente: catálogo vivo `outputs/smoke_regresion_py.csv` (extractores Python verificados en aislado).
Cada celda = **nº de filas-programa** extraídas. `E` = ERROR (raw no es la tabla programa+total). `~n` = AMARILLO (extrae pero por debajo de umbral estricto). `·` = año sin fuente extraíble en disco.

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | **Años** |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| **and** Andalucía | 114 | 115 | 102 | 102 | 103 | 111 | 112 | 97 | 88 | 88 | 88 | 88 | **12** |
| **ara** Aragón | 163 | E | 167 | 160 | 160 | 166 | 187 | 182 | 182 | 198 | 198 | 198 | **11** |
| **ast** Asturias | 107 | 91 | 91 | 90 | 90 | 95 | 96 | · | 96 | 104 | 105 | 104 | **11** |
| **bal** Baleares | 54 | 73 | · | 82 | 86 | 95 | 89 | 143 | 150 | 145 | 141 | · | **10** |
| **can** Canarias | 139 | 140 | 141 | 140 | 142 | 144 | 141 | 135 | 135 | 140 | 141 | 143 | **12** |
| **cat** Cataluña | 96 | 103 | 103 | · | 105 | 105 | · | 105 | 105 | 105 | · | 106 | **9** |
| **clm** Cast.-La Mancha | 99 | 99 | 98 | 98 | 99 | 100 | 101 | 111 | 114 | 114 | 113 | 113 | **12** |
| **cnt** Cantabria | 83 | 84 | 84 | 84 | 85 | 85 | 85 | 91 | 91 | 89 | 88 | 91 | **12** |
| **cym** Cast. y León | · | 103 | 102 | 102 | · | · | 104 | · | 107 | 104 | 103 | 103 | **8** |
| **ext** Extremadura | 78 | 77 | 77 | 77 | 77 | 80 | 80 | 79 | 81 | 79 | 79 | 79 | **12** |
| **gal** Galicia | 107 | 108 | 108 | 108 | 107 | 107 | 107 | ~16 | ~16 | 43 | 47 | ~18 | **9** |
| **lar** La Rioja | · | 70 | 74 | · | 73 | · | 81 | 64 | · | · | 58 | 60 | **7** |
| **mad** Madrid | 96 | 88 | 88 | 91 | 96 | 96 | 96 | 104 | 104 | 103 | 104 | 104 | **12** |
| **mur** Murcia | · | 145 | 149 | 147 | 149 | 154 | 154 | 154 | 155 | 160 | 149 | 149 | **11** |
| **nav** Navarra | 167 | 168 | 173 | 172 | 167 | 170 | 170 | 170 | 169 | 167 | 168 | 167 | **12** |
| **pvc** País Vasco | · | · | · | · | · | · | · | 116 | · | 118 | 122 | 122 | **4** |
| **val** C. Valenciana | · | 129 | 128 | 128 | 131 | 153 | 154 | 169 | 174 | 173 | 174 | 176 | **11** |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| **CCAA/año** | 12 | 15 | 15 | 14 | 15 | 14 | 15 | 14 | 14 | 16 | 16 | 15 | **175** |

**Cobertura total: 175 ejercicios-año válidos (VERDE + VERDE_PRAGM) · 17/17 CCAA · 3 AMARILLO (gal 2022/2023/2026) · 1 ERROR (ara/2016).**

## Detalle por CCAA (años · motor principal · máx. conceptos)

| CCAA | Años extraídos | N.º | Motor principal | Máx conc. |
|------|----------------|:---:|-----------------|:---------:|
| **and** Andalucía | 2015–2026 | 12 | `and-ckan-csv` | 12/13 |
| **ara** Aragón | 2015–2026 (2016 E) | 12 | `ara-pdf-program-total` | 11/13 |
| **ast** Asturias | 2015–2021, 2023–2026 | 11 | `ast-distribucion-gasto` | 10/13 |
| **bal** Baleares | 2015–2016, 2018–2025 | 10 | `bal-frameset-secciones` | 13/13 |
| **can** Canarias | 2015–2026 | 12 | `can-tomo3-resumen-programas` | 13/13 |
| **cat** Cataluña | 2015–2017, 2019–2020, 2022–2024, 2026 | 9 | `cat-programa-suma-secciones` | 13/13 |
| **clm** Cast.-La Mancha | 2015–2026 | 12 | `clm-gastosf-csv` | 13/13 |
| **cnt** Cantabria | 2015–2026 | 12 | `cnt-centros-suma-capitulos` | 12/13 |
| **cym** Cast. y León | 2016–2018, 2021, 2023–2026 | 8 | `cym-jcyl-datosabiertos` | 13/13 |
| **ext** Extremadura | 2015–2026 | 12 | `ext-doe-resumen-programa` | 11/13 |
| **gal** Galicia | 2015–2026 | 12 | `gal-progr-consellerias-ruleC` | 11/13 |
| **lar** La Rioja | 2016–2017, 2019, 2021–2022, 2025–2026 | 7 | `lar-pdfplumber-funcional-economico` | 13/13 |
| **mad** Madrid | 2015–2026 | 12 | `mad-libro-03-centros` | 11/13 |
| **mur** Murcia | 2016–2026 | 11 | `mur-html` | 13/13 |
| **nav** Navarra | 2015–2026 | 12 | `nav-breakdowns-functional` | 13/13 |
| **pvc** País Vasco | 2022, 2024–2026 | 4 | `pvc-csv-tidy` | 8/13 |
| **val** C. Valenciana | 2016–2026 | 11 | `val-rpc-secciones` | 13/13 |

## Referencia · presupuesto total por CCAA y año (€, serie 2015–2025)
*Totales de gasto consolidado (`outputs/importe_por_anio`), en millones €. Columna orientativa para dimensionar; el detalle por concepto se consolida en la carga R+psql matinal.*

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|------|----|----|----|----|----|----|----|----|----|----|----|
| **and** | 29.626 | 31.290 | 33.245 | 34.769 | 36.501 | 38.546 | 40.188 | 40.402 | 45.604 | 46.753 | 48.872 |
| **ara** | 5.254 | 5.130 | 5.577 | 6.162 | 6.162 | 6.467 | 7.454 | 7.444 | 8.250 | 8.546 | 8.546 |
| **ast** | 3.959 | 3.954 | 4.226 | 4.213 | 4.524 | 4.757 | 5.238 | 5.354 | 5.968 | 6.349 | 6.664 |
| **bal** | 4.036 | 4.241 | 4.668 | 5.009 | 5.458 | 5.893 | 5.882 | 6.398 | 7.133 | 7.321 | 7.469 |
| **can** | 6.901 | 7.265 | 7.339 | 8.273 | 8.833 | 9.603 | 9.531 | 9.974 | 11.059 | 11.971 | 12.343 |
| **cat** | 32.618 | 32.608 | 34.164 | 34.121 | 34.119 | 42.323 | 42.323 | 49.012 | 51.808 | 51.828 | 50.605 |
| **clm** | 8.206 | 8.420 | 8.941 | 9.219 | 9.219 | 10.505 | 12.102 | 12.274 | 12.432 | 12.473 | 12.716 |
| **cnt** | 2.501 | 2.465 | 2.603 | 2.731 | 2.854 | 2.888 | 3.078 | 3.343 | 3.507 | 3.548 | 3.756 |
| **cym** | 9.921 | 9.844 | 10.293 | 10.859 | 10.785 | 10.753 | 12.291 | 12.291 | 13.810 | 14.562 | 14.562 |
| **ext** | 5.366 | 5.197 | 5.172 | 5.434 | 5.798 | 6.006 | 6.424 | 7.000 | 7.781 | 8.127 | 8.098 |
| **gal** | 9.790 | 10.310 | 11.029 | 10.724 | 11.544 | 11.822 | 13.397 | 13.118 | 14.167 | 14.815 | 15.741 |
| **lar** | 1.287 | 1.337 | 1.456 | 1.519 | 1.488 | 1.575 | 1.891 | 1.950 | 1.909 | 1.974 | 2.115 |
| **mad** | 20.853 | 20.140 | 20.504 | 21.634 | 22.777 | 23.333 | 25.879 | 25.999 | 28.142 | 30.584 | 31.596 |
| **mur** | 4.642 | 4.916 | 5.093 | 5.515 | 5.800 | 6.197 | 6.754 | 6.963 | 7.771 | 7.819 | 8.037 |
| **nav** | 3.793 | 4.005 | 4.062 | 4.164 | 4.312 | 4.574 | 4.871 | 5.273 | 5.749 | 6.355 | 6.431 |
| **pvc** | 10.701 | 10.995 | 11.125 | 11.579 | 11.220 | 11.857 | 12.522 | 13.187 | 14.362 | 15.147 | 15.811 |
| **val** | 17.564 | 17.561 | 18.138 | 20.414 | 22.597 | 23.531 | 26.139 | 28.632 | 29.121 | 30.410 | 32.977 |

## Huecos pendientes y bloqueante de esta noche

El catálogo está prácticamente completo (175/~200 posibles ejercicios-año). Los huecos restantes **no** se pudieron cerrar esta noche: todos requieren **descargar el documento fuente correcto de internet**, y el sandbox nocturno tiene el `web_fetch` restringido por *provenance* (solo URLs ya vistas) y no permite `urllib`/`curl`. Los raws en disco para estos huecos son ley/BOPA (sin tabla programa+total), PDF con texto CID no recuperable, o stubs de 34 B.

| Combo | Estado del raw en disco | Acción para el run matinal (Mac, con red) |
|-------|-------------------------|--------------------------------------------|
| ara/2016 (E) | `ingresos_gastos.pdf` = solo texto de la Ley (retribuciones) | Descargar el tomo *Estado de gastos por programa* 2016 de hacienda.aragon.es |
| ast/2022 | `tomo_I.pdf` = Ley BOPA; sección de programas en glifos CID | Descargar el tomo *Distribución del gasto por programa* de transparencia.asturias.es |
| mur/2015 | `ley_completa.pdf` = texto de la Ley (462 pág, sin tabla) | Descargar el tomo de *Estado de gastos por programa* del visor Murcia |
| bal/2017, bal/2026 | `titol*_d.pdf` = stubs de 34 B | Re-descargar los PDF reales del frameset pressuposts.caib.es |
| pvc/2015–2021, 2023 | sin raw (tidy CSV desde 2022) | 2023: `.../2023A/Datuak_datos.csv`; 2015-21 = CSVs sueltos por concepto |
| lar/2018, 2020, 2023, 2024 | PDF con texto CID / columnas entrelazadas / invertido | 2024 clean pero detalle funcional entrelazado (falta educación); requiere reconstrucción por coordenadas |
| cat/2018, 2021, 2025 · cym 2015/2019/2020/2022 · val/2015 | sin raw en disco | añadir URL a fuentes.yml y descargar |