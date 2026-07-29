# Trazabilidad de la extracción — Comunidad Foral de Navarra (`nav`)

> **Qué códigos presupuestarios alimentan cada concepto, año por año, y con qué importe.**
> Generado automáticamente por [`tools/build_trazabilidad_md.py`](../../../tools/build_trazabilidad_md.py)
> desde `1_extraccion/staging_gasto.rds` (capa `autonomica`). Rev.: 2026-07-27.

## 0 · Cómo leer este documento

- **Unidad: € NOMINALES.** El staging guarda euros corrientes; la tabla final
  `presupuestos.ced_presupuestos` guarda € **constantes** (deflactados), así que los
  números de la BD y de la visualización D3 serán distintos (~×1,3 en los años antiguos).
  Para auditar el ORIGEN de un outlier, usa estas cifras; para auditar la serie publicada,
  recuerda aplicar el deflactor.
- El **importe de cada concepto-año es la suma de los importes de los códigos listados**
  en §5. Si un concepto salta de un año a otro, §4 te dice en qué año y §5 qué código
  entró o salió.
- `(sin concepto)` = líneas extraídas que **no** mapean a ninguno de los 13 conceptos
  (deuda, dirección general no social, etc.). Es esperable que sea el 25-40 % del total;
  no es un error, pero un salto brusco aquí suele señalar un cambio de clasificación.
- Marca ⚠ = variación interanual ≥ 40 % en un concepto que pesa
  ≥ 0,5 % del total del año. Es un **candidato a revisión**, no un error probado:
  puede ser un cambio presupuestario real.

## 1 · Fuente y cobertura, año por año

| Año | Filas | Documento fuente | Conceptos | % líneas con concepto | Total extraído (M€ nom.) | Prórroga | Consolidación |
|---|---:|---|---:|---:|---:|:-:|---|
| **2015** | 167 | `programa_csv.csv` | 13 | 39,5 % | 3.458,31 | — | no_aplica |
| **2016** | 168 | `programa_csv.csv` | 13 | 39,9 % | 3.506,17 | — | no_aplica |
| **2017** | 173 | `programa_csv.csv` | 13 | 39,3 % | 3.731,45 | — | no_aplica |
| **2018** | 172 | `programa_csv.csv` | 13 | 40,1 % | 3.889,81 | — | no_aplica |
| **2019** | 167 | `programa_csv.csv` | 12 | 40,1 % | 4.016,55 | — | no_aplica |
| **2020** | 170 | `programa_csv.csv` | 12 | 40,0 % | 4.256,57 | — | no_aplica |
| **2021** | 170 | `programa_csv.csv` | 12 | 40,6 % | 4.481,44 | — | no_aplica |
| **2022** | 170 | `programa_csv.csv` | 12 | 39,4 % | 4.767,03 | — | no_aplica |
| **2023** | 169 | `programa_csv.csv` | 12 | 40,2 % | 5.238,73 | — | no_aplica |
| **2024** | 167 | `programa_csv.csv` | 12 | 41,3 % | 5.835,97 | — | no_aplica |
| **2025** | 168 | `programa_csv.csv` | 12 | 41,1 % | 5.986,57 | — | no_aplica |
| **2026** | 167 | `programa_csv.csv` | 12 | 41,3 % | 6.318,65 | — | no_aplica |

**URL(s) de origen:**
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2015>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2016>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2017>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2018>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2019>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2020>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2021>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2022>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2023>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2024>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2025>
- <https://presupuesto.navarra.es/es/politicas#view=functional&year=2026>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 904,88 | 950,29 | 1.006,12 | 1.024,60 | 1.047,75 | 1.122,23 | 1.211,36 | 1.217,77 | 1.285,84 | 1.415,38 | 1.460,10 | 1.508,38 |
| `educacion` | 573,15 | 600,95 | 643,35 | 654,54 | 689,94 | 758,24 | 821,49 | 891,41 | 940,10 | 1.002,70 | 1.033,26 | 1.063,94 |
| `soberania` | 86,76 | 94,87 | 101,94 | 105,05 | 117,07 | 110,14 | 101,14 | 112,09 | 124,97 | 133,59 | 144,21 | 141,03 |
| `direccion` | 0,53 | 0,48 | 0,59 | 0,60 | 0,36 | 0,37 | 0,38 | 0,38 | 0,39 | 0,41 | 0,42 | 0,42 |
| `vivienda` | 55,57 | 47,15 | 55,05 | 62,87 | 62,25 | 59,25 | 65,78 | 102,57 | 113,05 | 149,45 | 151,34 | 155,00 |
| `empleo` | 51,43 | 50,73 | 58,88 | 60,54 | 59,79 | 62,68 | 64,67 | 82,71 | 81,67 | 75,65 | 75,52 | 77,69 |
| `idi` | 53,33 | 69,93 | 86,91 | 55,67 | 56,83 | 59,29 | 67,36 | 83,73 | 87,39 | 80,78 | 72,07 | 78,11 |
| `dependencia` | 132,52 | 135,87 | 140,86 | 148,96 | 164,75 | 165,53 | 176,03 | 208,25 | 244,25 | 251,02 | 254,34 | 266,74 |
| `discapacidad` | 0,21 | 0,42 | 1,37 | 1,51 | — | — | — | — | — | — | — | — |
| `salud_mental` | 27,15 | 27,59 | 28,98 | 30,66 | 34,25 | 36,30 | 37,89 | 38,74 | 41,09 | 43,84 | 44,17 | 45,73 |
| `diversidad` | 0,39 | 0,57 | 0,72 | 0,66 | 0,60 | 2,47 | 3,39 | 4,56 | 4,89 | 6,03 | 6,32 | 6,69 |
| `turismo` | 7,56 | 7,62 | 9,17 | 11,08 | 11,48 | 11,11 | 12,54 | 9,58 | 22,20 | 27,49 | 18,63 | 25,13 |
| `igualdad` | 3,80 | 2,92 | 3,63 | 4,17 | 4,58 | 4,78 | 5,36 | 7,29 | 6,86 | 6,76 | 6,82 | 8,07 |
| **Σ asignado** | 1.897,29 | 1.989,38 | 2.137,57 | 2.160,90 | 2.249,66 | 2.392,39 | 2.567,38 | 2.759,07 | 2.952,69 | 3.193,09 | 3.267,20 | 3.376,92 |
| *(sin concepto)* | 1.561,02 | 1.516,79 | 1.593,89 | 1.728,90 | 1.766,90 | 1.864,18 | 1.914,06 | 2.007,96 | 2.286,04 | 2.642,88 | 2.719,37 | 2.941,73 |
| **TOTAL extraído** | 3.458,31 | 3.506,17 | 3.731,45 | 3.889,81 | 4.016,55 | 4.256,57 | 4.481,44 | 4.767,03 | 5.238,73 | 5.835,97 | 5.986,57 | 6.318,65 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +5,0 % | +5,9 % | +1,8 % | +2,3 % | +7,1 % | +7,9 % | +0,5 % | +5,6 % | +10,1 % | +3,2 % | +3,3 % |
| `educacion` | +4,9 % | +7,1 % | +1,7 % | +5,4 % | +9,9 % | +8,3 % | +8,5 % | +5,5 % | +6,7 % | +3,0 % | +3,0 % |
| `soberania` | +9,3 % | +7,5 % | +3,0 % | +11,4 % | −5,9 % | −8,2 % | +10,8 % | +11,5 % | +6,9 % | +7,9 % | −2,2 % |
| `direccion` | −9,5 % | +23,2 % | +0,9 % | −39,3 % | +2,3 % | +1,9 % | +0,8 % | +2,0 % | +4,1 % | +2,3 % | +0,5 % |
| `vivienda` | −15,2 % | +16,8 % | +14,2 % | −1,0 % | −4,8 % | +11,0 % | +55,9 % ⚠ | +10,2 % | +32,2 % | +1,3 % | +2,4 % |
| `empleo` | −1,4 % | +16,1 % | +2,8 % | −1,2 % | +4,8 % | +3,2 % | +27,9 % | −1,3 % | −7,4 % | −0,2 % | +2,9 % |
| `idi` | +31,1 % | +24,3 % | −35,9 % | +2,1 % | +4,3 % | +13,6 % | +24,3 % | +4,4 % | −7,6 % | −10,8 % | +8,4 % |
| `dependencia` | +2,5 % | +3,7 % | +5,8 % | +10,6 % | +0,5 % | +6,3 % | +18,3 % | +17,3 % | +2,8 % | +1,3 % | +4,9 % |
| `discapacidad` | +100,5 % ⚠ | +225,4 % ⚠ | +10,3 % | **a 0** ⛔ | · | · | · | · | · | · | · |
| `salud_mental` | +1,6 % | +5,1 % | +5,8 % | +11,7 % | +6,0 % | +4,4 % | +2,2 % | +6,1 % | +6,7 % | +0,7 % | +3,5 % |
| `diversidad` | +45,1 % ⚠ | +25,9 % | −8,5 % | −8,2 % | +309,3 % ⚠ | +37,2 % | +34,5 % | +7,2 % | +23,3 % | +5,0 % | +5,8 % |
| `turismo` | +0,8 % | +20,3 % | +20,8 % | +3,7 % | −3,2 % | +12,8 % | −23,6 % | +131,8 % ⚠ | +23,8 % | −32,2 % | +34,9 % |
| `igualdad` | −23,1 % | +24,2 % | +14,8 % | +10,0 % | +4,2 % | +12,2 % | +35,9 % | −5,9 % | −1,5 % | +0,9 % | +18,2 % |
| **TOTAL** | +1,4 % | +6,4 % | +4,2 % | +3,3 % | +6,0 % | +5,3 % | +6,4 % | +9,9 % | +11,4 % | +2,6 % | +5,5 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2022 | `vivienda` | **SALTO** | 65,78 → 102,57 M€ (+55,9 % ⚠) |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `programa_csv.csv` · 167 líneas · total extraído **3.458,31 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 904,88 M€ (904.884.244 €) · 10 códigos · 26,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 485.320.291 | 53,6 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 140.149.444 | 15,5 % |
| `31.3122` | Sanidad / Atención primaria de salud | 131.250.893 | 14,5 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 105.929.260 | 11,7 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 18.987.634 | 2,1 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 16.882.035 | 1,9 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 5.187.997 | 0,6 % |
| `31.3112` | Sanidad / Formación sanitaria | 831.880 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 174.810 | 0,0 % |
| `31.3134` | Sanidad / Terapias avanzadas, medicina regenerativa y trasplantes | 170.000 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 573,15 M€ (573.147.512 €) · 18 códigos · 16,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 337.913.954 | 59,0 % |
| `32.3223` | Educación / Enseñanzas universitarias | 56.150.823 | 9,8 % |
| `32.322D` | Educación / Educación primaria | 44.237.038 | 7,7 % |
| `32.3222` | Educación / Educación secundaria | 34.709.233 | 6,1 % |
| `32.3221` | Educación / Educación infantil | 25.336.372 | 4,4 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 16.400.000 | 2,9 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 12.455.564 | 2,2 % |
| `32.322E` | Educación / Formación profesional | 11.208.919 | 2,0 % |
| `32.322C` | Educación / Bachillerato | 9.443.591 | 1,6 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 8.830.883 | 1,5 % |
| `32.3224` | Educación / Educación especial | 6.355.659 | 1,1 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 3.639.114 | 0,6 % |
| `32.3225` | Educación / Enseñanzas artísticas | 2.354.412 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.066.648 | 0,4 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 1.179.000 | 0,2 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 671.820 | 0,1 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 114.472 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 80.010 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 86,76 M€ (86.756.412 €) · 9 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 24.101.822 | 27,8 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 16.993.766 | 19,6 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 16.228.182 | 18,7 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 12.510.155 | 14,4 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 8.688.924 | 10,0 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 6.285.006 | 7,2 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 1.383.576 | 1,6 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 564.971 | 0,7 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 10 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,53 M€ (532.700 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 532.700 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 55,57 M€ (55.570.729 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 45.405.710 | 81,7 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 6.109.752 | 11,0 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 2.188.104 | 3,9 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 990.222 | 1,8 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 716.941 | 1,3 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 160.000 | 0,3 % |

</details>

<details open><summary><b><code>empleo</code> — 51,43 M€ (51.433.626 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 21.564.463 | 41,9 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 11.034.973 | 21,5 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 10.532.417 | 20,5 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 3.888.216 | 7,6 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 2.994.659 | 5,8 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 1.418.898 | 2,8 % |

</details>

<details open><summary><b><code>idi</code> — 53,33 M€ (53.329.419 €) · 5 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 28.971.930 | 54,3 % |
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 21.240.409 | 39,8 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 1.374.310 | 2,6 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 953.908 | 1,8 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 788.862 | 1,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 132,52 M€ (132.524.989 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 132.424.989 | 99,9 % |
| `23.2314` | Servicios sociales y promoción social / Servicios sociales a personas mayores | 100.000 | 0,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 0,21 M€ (210.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2313` | Servicios sociales y promoción social / Servicios sociales a personas con discapacidad | 210.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 27,15 M€ (27.149.023 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 27.149.023 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,39 M€ (393.182 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 393.182 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 7,56 M€ (7.558.346 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 4.627.341 | 61,2 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.683.403 | 22,3 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 912.000 | 12,1 % |
| `43.4323` | Comercio, Turismo y Pymes / Promoción hotelera y de complejos turísticos | 335.602 | 4,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,80 M€ (3.800.874 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 2.797.917 | 73,6 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.002.957 | 26,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.561,02 M€ · 101 códigos · 45,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 520.741.424 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 195.292.776 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 121.071.125 |
| `21.2111` | Pensiones / Pensiones contributivas | 78.190.295 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 65.445.698 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 55.349.692 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 54.174.740 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 51.690.721 |
| `45.4531` | Infraestructuras / Infraestructura del transporte ferroviario | 48.015.000 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 30.988.398 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 25.941.621 |
| `11.1121` | Justicia / Órganos judiciales | 23.759.139 |
| `42.4222` | Industria y energía / Desarrollo industrial | 20.505.010 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 17.768.393 |
| `13.1311` | Seguridad ciudadana e instituciones penitenciarias / Dirección y servicios generales de seguridad y protección civil | 14.856.229 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 13.778.505 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 13.714.362 |
| `91.9112` | Alta dirección / Actividad legislativa | 13.444.107 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 13.226.973 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 11.146.862 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 10.706.602 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 10.598.002 |
| `45.4561` | Infraestructuras / Calidad del agua | 9.947.623 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 8.234.183 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 7.617.326 |
| … | *resto: 76 códigos* | 124.816.017 |

</details>

### 2016

*Fuente: `programa_csv.csv` · 168 líneas · total extraído **3.506,17 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 950,29 M€ (950.290.485 €) · 10 códigos · 27,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 527.269.126 | 55,5 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 140.519.425 | 14,8 % |
| `31.3122` | Sanidad / Atención primaria de salud | 136.477.252 | 14,4 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 95.534.761 | 10,1 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 24.539.500 | 2,6 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 19.532.587 | 2,1 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 5.242.545 | 0,6 % |
| `31.3112` | Sanidad / Formación sanitaria | 848.978 | 0,1 % |
| `31.3134` | Sanidad / Terapias avanzadas, medicina regenerativa y trasplantes | 170.000 | 0,0 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 156.311 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 600,95 M€ (600.949.459 €) · 18 códigos · 17,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 360.192.830 | 59,9 % |
| `32.3223` | Educación / Enseñanzas universitarias | 55.210.148 | 9,2 % |
| `32.322D` | Educación / Educación primaria | 45.237.627 | 7,5 % |
| `32.3222` | Educación / Educación secundaria | 34.954.230 | 5,8 % |
| `32.3221` | Educación / Educación infantil | 26.026.153 | 4,3 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 17.000.000 | 2,8 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 14.072.548 | 2,3 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 11.116.798 | 1,8 % |
| `32.322E` | Educación / Formación profesional | 10.891.883 | 1,8 % |
| `32.322C` | Educación / Bachillerato | 9.611.206 | 1,6 % |
| `32.3224` | Educación / Educación especial | 6.557.735 | 1,1 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 3.644.114 | 0,6 % |
| `32.3225` | Educación / Enseñanzas artísticas | 2.615.339 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.092.176 | 0,3 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 879.828 | 0,1 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 654.525 | 0,1 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 114.064 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 78.255 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 94,87 M€ (94.866.733 €) · 9 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.506.358 | 22,7 % |
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 21.448.246 | 22,6 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 14.934.058 | 15,7 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 13.149.443 | 13,9 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 12.774.401 | 13,5 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 6.224.333 | 6,6 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 2.658.353 | 2,8 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 1.625.119 | 1,7 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 546.422 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 0,48 M€ (481.967 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 481.967 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 47,15 M€ (47.147.276 €) · 7 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 40.999.000 | 87,0 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 1.870.000 | 4,0 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 1.424.000 | 3,0 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.234.253 | 2,6 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.060.023 | 2,2 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 400.000 | 0,8 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 160.000 | 0,3 % |

</details>

<details open><summary><b><code>empleo</code> — 50,73 M€ (50.728.092 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 20.368.448 | 40,2 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 11.597.871 | 22,9 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 9.546.801 | 18,8 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 4.150.276 | 8,2 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 3.700.000 | 7,3 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 1.364.696 | 2,7 % |

</details>

<details open><summary><b><code>idi</code> — 69,93 M€ (69.929.845 €) · 5 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 35.904.021 | 51,3 % |
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 21.334.926 | 30,5 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 9.269.421 | 13,3 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 2.525.950 | 3,6 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 895.527 | 1,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 135,87 M€ (135.868.207 €) · 2 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 135.523.207 | 99,7 % |
| `23.2314` | Servicios sociales y promoción social / Servicios sociales a personas mayores | 345.000 | 0,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 0,42 M€ (421.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2313` | Servicios sociales y promoción social / Servicios sociales a personas con discapacidad | 421.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 27,59 M€ (27.585.465 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 27.585.465 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,57 M€ (570.545 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 570.545 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 7,62 M€ (7.618.845 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 4.801.986 | 63,0 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.484.010 | 19,5 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 820.000 | 10,8 % |
| `43.4323` | Comercio, Turismo y Pymes / Promoción hotelera y de complejos turísticos | 512.849 | 6,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,92 M€ (2.921.014 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 1.709.057 | 58,5 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.211.957 | 41,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.516,79 M€ · 101 códigos · 43,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 534.359.859 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 204.951.230 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 104.342.362 |
| `21.2111` | Pensiones / Pensiones contributivas | 85.993.511 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 77.763.336 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 63.464.156 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 53.855.873 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 30.110.566 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 27.012.037 |
| `11.1121` | Justicia / Órganos judiciales | 24.862.600 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 22.265.027 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 20.227.303 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 15.446.874 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 14.799.034 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 14.367.064 |
| `42.4222` | Industria y energía / Desarrollo industrial | 13.780.520 |
| `91.9112` | Alta dirección / Actividad legislativa | 13.609.385 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 12.337.412 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 12.215.013 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 10.867.994 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 10.215.589 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 9.674.637 |
| `23.2316` | Servicios sociales y promoción social / Reinserción social | 9.552.177 |
| `45.4567` | Infraestructuras / Conservación y mejora de masas forestales | 7.887.862 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 7.522.095 |
| … | *resto: 76 códigos* | 115.307.951 |

</details>

### 2017

*Fuente: `programa_csv.csv` · 173 líneas · total extraído **3.731,45 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.006,12 M€ (1.006.123.754 €) · 10 códigos · 27,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 546.281.197 | 54,3 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 149.985.894 | 14,9 % |
| `31.3122` | Sanidad / Atención primaria de salud | 140.375.109 | 14,0 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 113.986.497 | 11,3 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 27.197.816 | 2,7 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 21.567.208 | 2,1 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 5.433.621 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 919.024 | 0,1 % |
| `31.3134` | Sanidad / Terapias avanzadas, medicina regenerativa y trasplantes | 210.000 | 0,0 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 167.388 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 643,35 M€ (643.352.335 €) · 19 códigos · 17,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 386.189.712 | 60,0 % |
| `32.3223` | Educación / Enseñanzas universitarias | 58.051.836 | 9,0 % |
| `32.322D` | Educación / Educación primaria | 46.272.309 | 7,2 % |
| `32.3222` | Educación / Educación secundaria | 35.434.241 | 5,5 % |
| `32.3221` | Educación / Educación infantil | 27.007.592 | 4,2 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 17.869.992 | 2,8 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 17.300.010 | 2,7 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 13.067.887 | 2,0 % |
| `32.322E` | Educación / Formación profesional | 10.896.143 | 1,7 % |
| `32.322C` | Educación / Bachillerato | 9.698.870 | 1,5 % |
| `32.3224` | Educación / Educación especial | 6.762.209 | 1,1 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 4.523.915 | 0,7 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 3.694.104 | 0,6 % |
| `32.3225` | Educación / Enseñanzas artísticas | 2.850.029 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.509.468 | 0,4 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 811.874 | 0,1 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 151.064 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 86.080 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 101,94 M€ (101.943.559 €) · 9 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 27.029.811 | 26,5 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 23.994.783 | 23,5 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 14.403.130 | 14,1 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 13.915.704 | 13,7 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 12.939.058 | 12,7 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 6.538.009 | 6,4 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 2.551.675 | 2,5 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 442.603 | 0,4 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 128.786 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,59 M€ (593.678 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 593.678 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 55,05 M€ (55.046.540 €) · 7 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 40.375.000 | 73,3 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 10.316.820 | 18,7 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 1.824.000 | 3,3 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.146.071 | 2,1 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.117.649 | 2,0 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 167.000 | 0,3 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 100.000 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 58,88 M€ (58.876.993 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 21.749.823 | 36,9 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 11.057.387 | 18,8 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 9.440.513 | 16,0 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 7.130.000 | 12,1 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 5.100.000 | 8,7 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 4.399.270 | 7,5 % |

</details>

<details open><summary><b><code>idi</code> — 86,91 M€ (86.911.374 €) · 5 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 40.895.238 | 47,1 % |
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 31.654.920 | 36,4 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 9.674.973 | 11,1 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 4.038.241 | 4,6 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 648.002 | 0,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 140,86 M€ (140.857.234 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 140.657.234 | 99,9 % |
| `23.2314` | Servicios sociales y promoción social / Servicios sociales a personas mayores | 200.000 | 0,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 1,37 M€ (1.370.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2313` | Servicios sociales y promoción social / Servicios sociales a personas con discapacidad | 1.370.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 28,98 M€ (28.979.216 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 28.979.216 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,72 M€ (718.077 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 718.077 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 9,17 M€ (9.165.335 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 6.466.199 | 70,6 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.550.000 | 16,9 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 1.050.000 | 11,5 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 99.136 | 1,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,63 M€ (3.628.690 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 2.044.062 | 56,3 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.584.628 | 43,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.593,89 M€ · 105 códigos · 42,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 494.529.720 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 207.689.636 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 109.309.434 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 94.827.722 |
| `21.2111` | Pensiones / Pensiones contributivas | 89.641.860 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 70.536.744 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 55.745.742 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 39.309.172 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 31.702.584 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 27.532.315 |
| `11.1121` | Justicia / Órganos judiciales | 26.573.143 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 24.950.538 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 21.819.813 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 20.128.446 |
| `42.4222` | Industria y energía / Desarrollo industrial | 15.825.832 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 15.068.310 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 14.715.553 |
| `45.4561` | Infraestructuras / Calidad del agua | 14.696.095 |
| `91.9112` | Alta dirección / Actividad legislativa | 14.297.135 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 13.287.048 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 13.151.454 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 12.434.322 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 12.229.931 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 11.549.037 |
| `23.2316` | Servicios sociales y promoción social / Reinserción social | 9.311.949 |
| … | *resto: 80 códigos* | 133.022.946 |

</details>

### 2018

*Fuente: `programa_csv.csv` · 172 líneas · total extraído **3.889,81 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.024,60 M€ (1.024.602.853 €) · 9 códigos · 26,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 558.301.638 | 54,5 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 153.030.998 | 14,9 % |
| `31.3122` | Sanidad / Atención primaria de salud | 144.645.268 | 14,1 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 105.825.263 | 10,3 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 33.206.833 | 3,2 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 22.890.675 | 2,2 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 5.686.544 | 0,6 % |
| `31.3112` | Sanidad / Formación sanitaria | 864.504 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 151.130 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 654,54 M€ (654.538.007 €) · 19 códigos · 16,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 379.273.599 | 57,9 % |
| `32.3223` | Educación / Enseñanzas universitarias | 60.787.878 | 9,3 % |
| `32.322D` | Educación / Educación primaria | 48.859.887 | 7,5 % |
| `32.3222` | Educación / Educación secundaria | 36.753.475 | 5,6 % |
| `32.3221` | Educación / Educación infantil | 27.862.126 | 4,3 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 21.940.949 | 3,4 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 17.850.010 | 2,7 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 13.613.127 | 2,1 % |
| `32.322E` | Educación / Formación profesional | 11.218.913 | 1,7 % |
| `32.322C` | Educación / Bachillerato | 9.656.045 | 1,5 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 7.418.811 | 1,1 % |
| `32.3224` | Educación / Educación especial | 7.247.064 | 1,1 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.484.104 | 0,7 % |
| `32.3225` | Educación / Enseñanzas artísticas | 3.180.513 | 0,5 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.654.962 | 0,4 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 1.358.464 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 117.000 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 86.080 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 105,05 M€ (105.050.595 €) · 9 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 29.711.865 | 28,3 % |
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 21.490.715 | 20,5 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 17.270.796 | 16,4 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 14.627.165 | 13,9 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 11.073.356 | 10,5 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 6.641.139 | 6,3 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 3.503.562 | 3,3 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 466.764 | 0,4 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 265.233 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 0,60 M€ (599.212 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 599.212 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 62,87 M€ (62.868.394 €) · 7 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 42.470.000 | 67,6 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 15.511.670 | 24,7 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 2.033.000 | 3,2 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.435.631 | 2,3 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.151.093 | 1,8 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 167.000 | 0,3 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 100.000 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 60,54 M€ (60.539.965 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 22.191.129 | 36,7 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 11.142.822 | 18,4 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 10.693.587 | 17,7 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 6.772.000 | 11,2 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 5.000.000 | 8,3 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 4.740.427 | 7,8 % |

</details>

<details open><summary><b><code>idi</code> — 55,67 M€ (55.673.776 €) · 7 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 38.874.994 | 69,8 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 7.008.757 | 12,6 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 4.770.788 | 8,6 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 1.855.440 | 3,3 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 1.831.000 | 3,3 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 715.327 | 1,3 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 617.470 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 148,96 M€ (148.959.127 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 148.809.127 | 99,9 % |
| `23.2314` | Servicios sociales y promoción social / Servicios sociales a personas mayores | 150.000 | 0,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 1,51 M€ (1.511.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2313` | Servicios sociales y promoción social / Servicios sociales a personas con discapacidad | 1.511.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 30,66 M€ (30.662.441 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 30.662.441 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,66 M€ (656.900 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 656.900 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 11,08 M€ (11.075.362 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 8.251.496 | 74,5 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.660.000 | 15,0 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 1.050.000 | 9,5 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 113.866 | 1,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,17 M€ (4.166.938 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 2.344.300 | 56,3 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.822.638 | 43,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.728,90 M€ · 103 códigos · 44,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 542.071.743 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 219.915.434 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 116.381.272 |
| `21.2111` | Pensiones / Pensiones contributivas | 93.376.270 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 88.695.736 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 78.962.845 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 55.411.827 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 36.641.289 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 29.079.285 |
| `11.1121` | Justicia / Órganos judiciales | 28.299.712 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 27.337.836 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 26.253.015 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 24.173.065 |
| `42.4222` | Industria y energía / Desarrollo industrial | 23.949.217 |
| `92.921C` | Servicios de carácter general / Informática | 22.370.692 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 22.331.062 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 19.574.251 |
| `45.4561` | Infraestructuras / Calidad del agua | 15.804.559 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 14.858.080 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 14.762.178 |
| `91.9112` | Alta dirección / Actividad legislativa | 14.423.528 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 13.963.674 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 13.142.677 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 12.513.383 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 11.399.357 |
| … | *resto: 78 códigos* | 163.208.643 |

</details>

### 2019

*Fuente: `programa_csv.csv` · 167 líneas · total extraído **4.016,55 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.047,75 M€ (1.047.750.152 €) · 9 códigos · 26,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 590.261.169 | 56,3 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 154.767.154 | 14,8 % |
| `31.3122` | Sanidad / Atención primaria de salud | 151.629.243 | 14,5 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 103.378.277 | 9,9 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 24.200.438 | 2,3 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 16.647.734 | 1,6 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 5.849.945 | 0,6 % |
| `31.3112` | Sanidad / Formación sanitaria | 795.150 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 221.042 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 689,94 M€ (689.939.162 €) · 19 códigos · 17,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 407.038.186 | 59,0 % |
| `32.3223` | Educación / Enseñanzas universitarias | 65.014.595 | 9,4 % |
| `32.322D` | Educación / Educación primaria | 45.868.668 | 6,6 % |
| `32.3222` | Educación / Educación secundaria | 37.207.809 | 5,4 % |
| `32.3221` | Educación / Educación infantil | 29.331.124 | 4,3 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 23.420.931 | 3,4 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 18.100.010 | 2,6 % |
| `32.322E` | Educación / Formación profesional | 12.147.111 | 1,8 % |
| `32.3224` | Educación / Educación especial | 11.957.359 | 1,7 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 11.021.666 | 1,6 % |
| `32.322C` | Educación / Bachillerato | 10.939.700 | 1,6 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 5.719.566 | 0,8 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.484.104 | 0,6 % |
| `32.3225` | Educación / Enseñanzas artísticas | 3.988.064 | 0,6 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 1.847.025 | 0,3 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 1.509.464 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 86.080 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 82.700 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 117,07 M€ (117.065.311 €) · 9 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 32.728.332 | 28,0 % |
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 25.742.929 | 22,0 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 17.453.196 | 14,9 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 14.700.741 | 12,6 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 13.634.003 | 11,6 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 7.112.623 | 6,1 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 3.941.746 | 3,4 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 1.300.000 | 1,1 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 451.741 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,36 M€ (363.723 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 363.723 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 62,25 M€ (62.245.306 €) · 7 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 38.723.650 | 62,2 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 18.644.467 | 30,0 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 2.379.010 | 3,8 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.240.866 | 2,0 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.178.313 | 1,9 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 78.000 | 0,1 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 1.000 | 0,0 % |

</details>

<details open><summary><b><code>empleo</code> — 59,79 M€ (59.789.949 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 23.869.742 | 39,9 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 10.491.600 | 17,5 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 9.384.841 | 15,7 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 6.202.000 | 10,4 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 5.000.000 | 8,4 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 4.841.766 | 8,1 % |

</details>

<details open><summary><b><code>idi</code> — 56,83 M€ (56.830.229 €) · 7 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 40.686.649 | 71,6 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 5.847.637 | 10,3 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 5.276.772 | 9,3 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.184.997 | 3,8 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 1.982.000 | 3,5 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 852.154 | 1,5 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 20 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 164,75 M€ (164.750.303 €) · 1 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 164.750.303 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 34,25 M€ (34.254.463 €) · 1 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 34.254.463 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,60 M€ (603.324 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 603.324 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 11,48 M€ (11.480.457 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 8.558.845 | 74,6 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.662.010 | 14,5 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 1.043.500 | 9,1 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 216.102 | 1,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,58 M€ (4.584.648 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 2.423.619 | 52,9 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 2.161.029 | 47,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.766,90 M€ · 100 códigos · 44,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 545.270.982 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 229.835.949 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 117.788.268 |
| `21.2111` | Pensiones / Pensiones contributivas | 99.892.527 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 77.601.718 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 72.646.054 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 56.928.125 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 55.359.766 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 40.470.751 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 29.240.415 |
| `11.1121` | Justicia / Órganos judiciales | 28.062.569 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 26.432.729 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 26.346.914 |
| `92.921C` | Servicios de carácter general / Informática | 23.273.197 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 17.151.006 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 16.379.963 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 15.773.945 |
| `91.9112` | Alta dirección / Actividad legislativa | 15.290.537 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 14.985.093 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 14.858.649 |
| `42.4222` | Industria y energía / Desarrollo industrial | 14.571.515 |
| `45.4561` | Infraestructuras / Calidad del agua | 13.898.234 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 13.760.266 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 13.152.486 |
| `23.2316` | Servicios sociales y promoción social / Reinserción social | 9.893.507 |
| … | *resto: 75 códigos* | 178.030.093 |

</details>

### 2020

*Fuente: `programa_csv.csv` · 170 líneas · total extraído **4.256,57 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.122,23 M€ (1.122.231.413 €) · 9 códigos · 26,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 621.800.334 | 55,4 % |
| `31.3122` | Sanidad / Atención primaria de salud | 158.926.938 | 14,2 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 151.960.010 | 13,5 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 132.272.385 | 11,8 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 26.140.660 | 2,3 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 24.224.463 | 2,2 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 6.047.675 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 719.768 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 139.180 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 758,24 M€ (758.237.455 €) · 19 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 459.242.046 | 60,6 % |
| `32.3223` | Educación / Enseñanzas universitarias | 72.856.230 | 9,6 % |
| `32.322D` | Educación / Educación primaria | 47.929.197 | 6,3 % |
| `32.3222` | Educación / Educación secundaria | 38.906.438 | 5,1 % |
| `32.3221` | Educación / Educación infantil | 30.939.070 | 4,1 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 23.209.599 | 3,1 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 18.510.010 | 2,4 % |
| `32.322E` | Educación / Formación profesional | 12.746.647 | 1,7 % |
| `32.3224` | Educación / Educación especial | 12.477.775 | 1,6 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 11.726.015 | 1,5 % |
| `32.322C` | Educación / Bachillerato | 11.439.935 | 1,5 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 5.827.962 | 0,8 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.484.104 | 0,6 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.018.165 | 0,5 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 1.992.468 | 0,3 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 1.586.293 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 82.700 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 110,14 M€ (110.139.479 €) · 9 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 27.474.904 | 24,9 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.140.529 | 19,2 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 18.135.880 | 16,5 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 14.805.323 | 13,4 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 13.959.172 | 12,7 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 7.665.868 | 7,0 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 4.526.369 | 4,1 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 1.904.696 | 1,7 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 526.738 | 0,5 % |

</details>

<details open><summary><b><code>direccion</code> — 0,37 M€ (372.128 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 372.128 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 59,25 M€ (59.249.094 €) · 7 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 42.054.844 | 71,0 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 11.804.331 | 19,9 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 2.517.220 | 4,2 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.449.372 | 2,4 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.253.307 | 2,1 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 100.010 | 0,2 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 70.010 | 0,1 % |

</details>

<details open><summary><b><code>empleo</code> — 62,68 M€ (62.681.582 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 27.158.513 | 43,3 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 10.959.983 | 17,5 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 9.375.844 | 15,0 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 5.335.242 | 8,5 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 5.000.000 | 8,0 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 4.852.000 | 7,7 % |

</details>

<details open><summary><b><code>idi</code> — 59,29 M€ (59.288.428 €) · 8 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 45.254.429 | 76,3 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 5.498.348 | 9,3 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 3.051.969 | 5,1 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.236.407 | 3,8 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 2.204.314 | 3,7 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 807.951 | 1,4 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 235.000 | 0,4 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 10 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 165,53 M€ (165.529.340 €) · 1 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 165.529.340 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 36,30 M€ (36.296.315 €) · 1 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 36.296.315 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,47 M€ (2.469.702 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 2.469.702 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 11,11 M€ (11.114.698 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 8.139.287 | 73,2 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.725.010 | 15,5 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 775.000 | 7,0 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 475.401 | 4,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,78 M€ (4.777.592 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 3.021.807 | 63,2 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.755.785 | 36,8 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.864,18 M€ · 102 códigos · 43,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 585.686.575 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 236.955.252 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 124.447.887 |
| `21.2111` | Pensiones / Pensiones contributivas | 103.643.027 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 80.810.775 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 65.971.430 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 61.613.174 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 46.262.080 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 41.431.333 |
| `11.1121` | Justicia / Órganos judiciales | 30.702.485 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 30.507.133 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 30.122.370 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 29.538.329 |
| `92.921C` | Servicios de carácter general / Informática | 25.355.975 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 19.797.542 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 17.449.516 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 16.715.543 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 16.060.095 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 15.890.241 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 15.754.954 |
| `91.9112` | Alta dirección / Actividad legislativa | 15.569.816 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 15.209.901 |
| `45.4521` | Infraestructuras / Gestión e infraestructuras de recursos hidráulicos | 14.702.915 |
| `42.4222` | Industria y energía / Desarrollo industrial | 13.876.340 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 13.861.449 |
| … | *resto: 77 códigos* | 196.244.660 |

</details>

### 2021

*Fuente: `programa_csv.csv` · 170 líneas · total extraído **4.481,44 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.211,36 M€ (1.211.356.190 €) · 9 códigos · 27,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 674.706.414 | 55,7 % |
| `31.3122` | Sanidad / Atención primaria de salud | 179.574.813 | 14,8 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 155.242.906 | 12,8 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 138.376.957 | 11,4 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 28.917.086 | 2,4 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 27.084.258 | 2,2 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 6.604.365 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 721.413 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 127.978 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 821,49 M€ (821.486.275 €) · 19 códigos · 18,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 497.890.652 | 60,6 % |
| `32.3223` | Educación / Enseñanzas universitarias | 80.355.943 | 9,8 % |
| `32.322D` | Educación / Educación primaria | 48.278.866 | 5,9 % |
| `32.3222` | Educación / Educación secundaria | 39.921.043 | 4,9 % |
| `32.3221` | Educación / Educación infantil | 31.873.674 | 3,9 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 23.736.543 | 2,9 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 21.366.392 | 2,6 % |
| `32.322E` | Educación / Formación profesional | 16.023.979 | 2,0 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 15.429.782 | 1,9 % |
| `32.3224` | Educación / Educación especial | 13.254.512 | 1,6 % |
| `32.322C` | Educación / Bachillerato | 11.647.924 | 1,4 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 9.199.037 | 1,1 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.454.104 | 0,5 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.027.331 | 0,5 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.004.584 | 0,2 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 1.676.408 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 82.700 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 101,14 M€ (101.135.130 €) · 9 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 21.346.794 | 21,1 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.109.749 | 20,9 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 17.972.847 | 17,8 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 15.870.546 | 15,7 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 11.533.778 | 11,4 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 8.867.621 | 8,8 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 3.843.890 | 3,8 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 569.895 | 0,6 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 20.010 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,38 M€ (379.021 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 379.021 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 65,78 M€ (65.777.382 €) · 7 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 53.093.243 | 80,7 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 6.826.713 | 10,4 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 2.659.542 | 4,0 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.682.950 | 2,6 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.054.134 | 1,6 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 400.010 | 0,6 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 60.790 | 0,1 % |

</details>

<details open><summary><b><code>empleo</code> — 64,67 M€ (64.669.872 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 31.117.748 | 48,1 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 10.126.601 | 15,7 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 8.580.556 | 13,3 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 5.629.967 | 8,7 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 4.700.000 | 7,3 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 4.515.000 | 7,0 % |

</details>

<details open><summary><b><code>idi</code> — 67,36 M€ (67.356.127 €) · 8 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 49.814.697 | 74,0 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 5.648.182 | 8,4 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 5.500.672 | 8,2 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 2.659.125 | 3,9 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.235.007 | 3,3 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 827.073 | 1,2 % |
| `46.4677` | Investigación, desarrollo e innovación / Investigación y desarrollo de la sociedad de la información | 356.371 | 0,5 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 315.000 | 0,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 176,03 M€ (176.033.515 €) · 2 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 175.843.515 | 99,9 % |
| `23.2314` | Servicios sociales y promoción social / Servicios sociales a personas mayores | 190.000 | 0,1 % |

</details>

<details open><summary><b><code>salud_mental</code> — 37,89 M€ (37.892.168 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 37.892.168 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,39 M€ (3.388.906 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 3.388.906 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 12,54 M€ (12.541.041 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 8.533.655 | 68,0 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 2.453.000 | 19,6 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 1.078.200 | 8,6 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 476.186 | 3,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 5,36 M€ (5.362.500 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 3.424.154 | 63,9 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 1.938.346 | 36,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.914,06 M€ · 101 códigos · 42,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 560.088.306 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 256.662.566 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 141.528.692 |
| `21.2111` | Pensiones / Pensiones contributivas | 105.123.029 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 81.475.094 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 62.903.201 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 59.974.047 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 49.687.755 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 37.981.100 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 36.369.253 |
| `11.1121` | Justicia / Órganos judiciales | 31.687.923 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 30.388.356 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 26.201.417 |
| `92.921C` | Servicios de carácter general / Informática | 26.138.346 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 23.782.266 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 21.628.856 |
| `42.4222` | Industria y energía / Desarrollo industrial | 20.915.894 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 20.238.517 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 18.249.706 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 17.588.035 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 17.177.236 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 15.734.579 |
| `91.9112` | Alta dirección / Actividad legislativa | 15.413.225 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 15.336.731 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 13.666.682 |
| … | *resto: 76 códigos* | 208.120.098 |

</details>

### 2022

*Fuente: `programa_csv.csv` · 170 líneas · total extraído **4.767,03 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.217,77 M€ (1.217.768.301 €) · 9 códigos · 25,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 674.736.852 | 55,4 % |
| `31.3122` | Sanidad / Atención primaria de salud | 178.524.667 | 14,7 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 159.440.735 | 13,1 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 129.997.812 | 10,7 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 37.110.649 | 3,0 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 30.667.851 | 2,5 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 6.298.028 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 811.786 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 179.921 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 891,41 M€ (891.414.962 €) · 19 códigos · 18,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 517.970.300 | 58,1 % |
| `32.3223` | Educación / Enseñanzas universitarias | 92.751.418 | 10,4 % |
| `32.322D` | Educación / Educación primaria | 50.124.997 | 5,6 % |
| `32.3222` | Educación / Educación secundaria | 41.522.285 | 4,7 % |
| `32.3221` | Educación / Educación infantil | 36.505.366 | 4,1 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 33.778.185 | 3,8 % |
| `32.322E` | Educación / Formación profesional | 30.110.421 | 3,4 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 21.423.403 | 2,4 % |
| `32.3224` | Educación / Educación especial | 13.913.094 | 1,6 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 13.267.424 | 1,5 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 13.257.316 | 1,5 % |
| `32.322C` | Educación / Bachillerato | 12.113.841 | 1,4 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.484.104 | 0,5 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.071.500 | 0,5 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 3.155.810 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.603.343 | 0,3 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 99.354 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 112,09 M€ (112.088.961 €) · 9 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 26.904.589 | 24,0 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 21.954.109 | 19,6 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.007.964 | 18,7 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 16.137.785 | 14,4 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 13.244.848 | 11,8 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 8.602.138 | 7,7 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 3.368.764 | 3,0 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 543.000 | 0,5 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 325.764 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 0,38 M€ (382.185 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 382.185 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 102,57 M€ (102.566.186 €) · 7 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 64.224.850 | 62,6 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 31.589.642 | 30,8 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 3.124.501 | 3,0 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 1.691.754 | 1,6 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.075.429 | 1,0 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 600.010 | 0,6 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 260.000 | 0,3 % |

</details>

<details open><summary><b><code>empleo</code> — 82,71 M€ (82.705.639 €) · 6 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 36.137.996 | 43,7 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 13.448.117 | 16,3 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 13.311.828 | 16,1 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 7.200.000 | 8,7 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 6.929.698 | 8,4 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 5.678.000 | 6,9 % |

</details>

<details open><summary><b><code>idi</code> — 83,73 M€ (83.730.303 €) · 7 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 65.150.602 | 77,8 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 5.612.752 | 6,7 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 5.101.040 | 6,1 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 4.299.699 | 5,1 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.295.010 | 2,7 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 951.200 | 1,1 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 320.000 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 208,25 M€ (208.247.972 €) · 1 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 208.247.972 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 38,74 M€ (38.741.281 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 38.741.281 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,56 M€ (4.558.830 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 4.558.830 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 9,58 M€ (9.579.817 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 6.407.412 | 66,9 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 1.752.020 | 18,3 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 912.000 | 9,5 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 508.385 | 5,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,29 M€ (7.289.244 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 4.800.069 | 65,9 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 2.489.175 | 34,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.007,96 M€ · 103 códigos · 42,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 573.089.091 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 272.386.600 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 129.291.581 |
| `21.2111` | Pensiones / Pensiones contributivas | 110.987.189 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 96.310.654 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 65.787.803 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 52.360.179 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 43.725.612 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 39.880.705 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 37.839.866 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 37.754.755 |
| `11.1121` | Justicia / Órganos judiciales | 32.700.983 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 32.168.511 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 31.363.128 |
| `92.921C` | Servicios de carácter general / Informática | 29.638.495 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 22.800.387 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 20.493.671 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 20.093.380 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 19.238.457 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 17.571.001 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 16.990.000 |
| `42.4252` | Industria y energía / Incentivos sobre medidas energéticas | 16.643.472 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 16.434.090 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 16.012.502 |
| `91.9112` | Alta dirección / Actividad legislativa | 15.785.102 |
| … | *resto: 78 códigos* | 240.613.315 |

</details>

### 2023

*Fuente: `programa_csv.csv` · 169 líneas · total extraído **5.238,73 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.285,84 M€ (1.285.836.840 €) · 9 códigos · 24,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 719.193.327 | 55,9 % |
| `31.3122` | Sanidad / Atención primaria de salud | 183.575.073 | 14,3 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 160.177.678 | 12,5 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 139.234.764 | 10,8 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 44.522.434 | 3,5 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 31.573.394 | 2,5 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 6.544.993 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 831.651 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 183.526 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 940,10 M€ (940.095.265 €) · 19 códigos · 17,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 527.673.479 | 56,1 % |
| `32.3223` | Educación / Enseñanzas universitarias | 99.537.806 | 10,6 % |
| `32.322D` | Educación / Educación primaria | 53.467.950 | 5,7 % |
| `32.3221` | Educación / Educación infantil | 47.874.105 | 5,1 % |
| `32.3222` | Educación / Educación secundaria | 44.316.990 | 4,7 % |
| `32.322E` | Educación / Formación profesional | 37.725.460 | 4,0 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 28.451.744 | 3,0 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 27.632.350 | 2,9 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 16.395.246 | 1,7 % |
| `32.3224` | Educación / Educación especial | 15.767.669 | 1,7 % |
| `32.322C` | Educación / Bachillerato | 12.913.354 | 1,4 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 11.615.447 | 1,2 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.740.910 | 0,5 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.609.704 | 0,5 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 4.163.424 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 2.846.499 | 0,3 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 175.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 100.327 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 124,97 M€ (124.966.970 €) · 9 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 30.041.730 | 24,0 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 23.087.131 | 18,5 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.377.023 | 17,1 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 16.992.771 | 13,6 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 15.440.545 | 12,4 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 9.549.990 | 7,6 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 5.636.451 | 4,5 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 2.509.129 | 2,0 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 332.200 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 0,39 M€ (389.779 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 389.779 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 113,05 M€ (113.051.804 €) · 7 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 66.339.958 | 58,7 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 38.182.389 | 33,8 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 3.981.383 | 3,5 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 2.021.343 | 1,8 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.287.166 | 1,1 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 1.000.010 | 0,9 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 239.555 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 81,67 M€ (81.668.075 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 38.804.764 | 47,5 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 11.889.496 | 14,6 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 11.191.527 | 13,7 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 7.200.000 | 8,8 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 7.002.288 | 8,6 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 5.580.000 | 6,8 % |

</details>

<details open><summary><b><code>idi</code> — 87,39 M€ (87.391.215 €) · 7 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 67.388.785 | 77,1 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 6.386.867 | 7,3 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 5.839.368 | 6,7 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 3.551.010 | 4,1 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.820.000 | 3,2 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 929.545 | 1,1 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 475.640 | 0,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 244,25 M€ (244.247.845 €) · 1 códigos · 4,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 244.247.845 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 41,09 M€ (41.086.982 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 41.086.982 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,89 M€ (4.885.492 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 4.885.492 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 22,20 M€ (22.203.102 €) · 5 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 12.128.288 | 54,6 % |
| `45.4583` | Infraestructuras / Infraestructura turística | 5.840.887 | 26,3 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 3.077.110 | 13,9 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 666.000 | 3,0 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 490.817 | 2,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,86 M€ (6.862.411 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 4.487.575 | 65,4 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 2.374.836 | 34,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.286,04 M€ · 101 códigos · 43,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 635.090.863 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 303.948.425 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 172.709.221 |
| `21.2111` | Pensiones / Pensiones contributivas | 118.349.813 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 114.057.620 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 74.191.293 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 71.399.813 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 54.020.675 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 44.556.253 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 43.151.337 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 39.768.116 |
| `42.4252` | Industria y energía / Incentivos sobre medidas energéticas | 39.730.339 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 38.413.483 |
| `11.1121` | Justicia / Órganos judiciales | 36.390.282 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 36.109.279 |
| `92.921C` | Servicios de carácter general / Informática | 34.692.779 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 23.922.351 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 21.911.936 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 21.836.353 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 19.236.350 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 18.507.967 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 18.130.125 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 18.018.457 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 17.056.478 |
| `91.9112` | Alta dirección / Actividad legislativa | 16.766.902 |
| … | *resto: 76 códigos* | 254.078.023 |

</details>

### 2024

*Fuente: `programa_csv.csv` · 167 líneas · total extraído **5.835,97 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.415,38 M€ (1.415.375.379 €) · 9 códigos · 24,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 777.865.251 | 55,0 % |
| `31.3122` | Sanidad / Atención primaria de salud | 203.112.127 | 14,4 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 181.019.576 | 12,8 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 179.821.128 | 12,7 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 36.253.044 | 2,6 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 29.282.286 | 2,1 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 6.993.995 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 869.428 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 158.544 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.002,70 M€ (1.002.695.363 €) · 19 códigos · 17,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 565.119.856 | 56,4 % |
| `32.3223` | Educación / Enseñanzas universitarias | 110.588.420 | 11,0 % |
| `32.322D` | Educación / Educación primaria | 56.678.381 | 5,7 % |
| `32.3221` | Educación / Educación infantil | 49.997.886 | 5,0 % |
| `32.3222` | Educación / Educación secundaria | 46.468.503 | 4,6 % |
| `32.322E` | Educación / Formación profesional | 43.334.604 | 4,3 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 29.878.057 | 3,0 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 29.780.629 | 3,0 % |
| `32.3224` | Educación / Educación especial | 19.122.996 | 1,9 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 16.003.654 | 1,6 % |
| `32.322C` | Educación / Bachillerato | 13.357.330 | 1,3 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 6.473.969 | 0,6 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.759.873 | 0,5 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.596.000 | 0,5 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 3.391.317 | 0,3 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 2.775.387 | 0,3 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 180.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 100.700 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 133,59 M€ (133.593.576 €) · 9 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 31.227.943 | 23,4 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 25.657.052 | 19,2 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 21.538.554 | 16,1 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 17.925.466 | 13,4 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 17.794.292 | 13,3 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 10.149.059 | 7,6 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 8.713.135 | 6,5 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 568.055 | 0,4 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 20.020 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,41 M€ (405.611 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 405.611 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 149,45 M€ (149.448.923 €) · 7 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 107.846.718 | 72,2 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 29.850.510 | 20,0 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 4.538.671 | 3,0 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 3.555.874 | 2,4 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 2.000.010 | 1,3 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.407.140 | 0,9 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 250.000 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 75,65 M€ (75.647.559 €) · 6 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 33.451.673 | 44,2 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 11.873.426 | 15,7 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 8.539.185 | 11,3 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 8.448.431 | 11,2 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 8.007.844 | 10,6 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 5.327.000 | 7,0 % |

</details>

<details open><summary><b><code>idi</code> — 80,78 M€ (80.781.074 €) · 8 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 59.850.612 | 74,1 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 6.938.786 | 8,6 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 4.866.818 | 6,0 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 3.594.113 | 4,4 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.971.830 | 3,7 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 953.161 | 1,2 % |
| `46.4621` | Investigación, desarrollo e innovación / Investigación y estudios sociológicos | 948.743 | 1,2 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 657.011 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 251,02 M€ (251.016.523 €) · 1 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 251.016.523 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 43,84 M€ (43.843.236 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 43.843.236 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,03 M€ (6.025.467 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 6.025.467 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 27,49 M€ (27.494.971 €) · 5 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 19.831.481 | 72,1 % |
| `45.4583` | Infraestructuras / Infraestructura turística | 3.208.647 | 11,7 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 2.626.463 | 9,6 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 1.067.580 | 3,9 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 760.800 | 2,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,76 M€ (6.760.311 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 4.072.083 | 60,2 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 2.688.228 | 39,8 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.642,88 M€ · 98 códigos · 45,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 837.100.867 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 315.353.575 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 193.963.494 |
| `21.2111` | Pensiones / Pensiones contributivas | 124.557.207 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 121.863.604 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 87.860.684 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 77.246.229 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 58.426.614 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 57.609.371 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 48.666.457 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 46.186.313 |
| `92.921C` | Servicios de carácter general / Informática | 39.797.051 |
| `11.1121` | Justicia / Órganos judiciales | 38.654.494 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 38.282.153 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 31.570.965 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 25.484.460 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 25.310.555 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 23.041.769 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 20.726.000 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 20.520.649 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 20.320.261 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 19.946.942 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 19.907.548 |
| `42.4252` | Industria y energía / Incentivos sobre medidas energéticas | 19.685.748 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 19.122.207 |
| … | *resto: 73 códigos* | 311.679.344 |

</details>

### 2025

*Fuente: `programa_csv.csv` · 168 líneas · total extraído **5.986,57 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.460,10 M€ (1.460.097.315 €) · 9 códigos · 24,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 816.590.246 | 55,9 % |
| `31.3122` | Sanidad / Atención primaria de salud | 210.137.088 | 14,4 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 187.660.297 | 12,9 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 182.035.898 | 12,5 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 37.281.089 | 2,6 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 17.956.140 | 1,2 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 7.387.797 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 886.884 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 161.876 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.033,26 M€ (1.033.257.219 €) · 19 códigos · 17,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 603.400.631 | 58,4 % |
| `32.3223` | Educación / Enseñanzas universitarias | 107.375.009 | 10,4 % |
| `32.322D` | Educación / Educación primaria | 59.224.819 | 5,7 % |
| `32.3221` | Educación / Educación infantil | 52.482.642 | 5,1 % |
| `32.3222` | Educación / Educación secundaria | 48.233.274 | 4,7 % |
| `32.322E` | Educación / Formación profesional | 34.233.702 | 3,3 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 32.494.522 | 3,1 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 20.856.232 | 2,0 % |
| `32.3224` | Educación / Educación especial | 19.847.147 | 1,9 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 17.812.895 | 1,7 % |
| `32.322C` | Educación / Bachillerato | 13.919.596 | 1,3 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 7.830.696 | 0,8 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.893.786 | 0,5 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.663.741 | 0,5 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 3.438.084 | 0,3 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 2.181.228 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 180.000 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 101.414 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 87.801 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 144,21 M€ (144.213.954 €) · 9 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 41.224.983 | 28,6 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 28.726.316 | 19,9 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 22.111.733 | 15,3 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 18.078.518 | 12,5 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 17.458.953 | 12,1 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 10.300.813 | 7,1 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 4.332.694 | 3,0 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 1.416.276 | 1,0 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 563.668 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,42 M€ (415.046 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 415.046 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 151,34 M€ (151.339.888 €) · 7 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 105.208.302 | 69,5 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 30.589.402 | 20,2 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 6.718.058 | 4,4 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 3.628.259 | 2,4 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 3.535.225 | 2,3 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.409.632 | 0,9 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 251.010 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 75,52 M€ (75.522.428 €) · 6 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 34.957.797 | 46,3 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 13.052.546 | 17,3 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 8.500.000 | 11,3 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 8.321.160 | 11,0 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 7.843.925 | 10,4 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 2.847.000 | 3,8 % |

</details>

<details open><summary><b><code>idi</code> — 72,07 M€ (72.065.748 €) · 8 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 53.264.339 | 73,9 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 6.891.434 | 9,6 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 3.400.642 | 4,7 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 2.972.141 | 4,1 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.655.300 | 3,7 % |
| `46.4621` | Investigación, desarrollo e innovación / Investigación y estudios sociológicos | 1.451.085 | 2,0 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 891.797 | 1,2 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 539.010 | 0,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 254,34 M€ (254.338.477 €) · 1 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 254.338.477 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 44,17 M€ (44.170.464 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 44.170.464 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,32 M€ (6.323.846 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 6.323.846 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 18,63 M€ (18.630.446 €) · 5 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 12.494.136 | 67,1 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 2.467.157 | 13,2 % |
| `45.4583` | Infraestructuras / Infraestructura turística | 2.442.354 | 13,1 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 841.799 | 4,5 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 385.000 | 2,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,82 M€ (6.824.312 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 3.980.565 | 58,3 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 2.843.747 | 41,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.719,37 M€ · 99 códigos · 45,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 874.103.383 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 331.567.528 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 200.050.824 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 149.627.126 |
| `21.2111` | Pensiones / Pensiones contributivas | 127.993.467 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 93.858.308 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 70.842.868 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 57.790.617 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 56.128.094 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 50.380.891 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 47.882.101 |
| `92.921C` | Servicios de carácter general / Informática | 41.050.747 |
| `11.1121` | Justicia / Órganos judiciales | 40.525.027 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 40.422.954 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 28.124.663 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 27.159.046 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 25.488.976 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 23.090.000 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 23.020.588 |
| `45.4521` | Infraestructuras / Gestión e infraestructuras de recursos hidráulicos | 22.105.421 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 20.272.000 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 20.166.477 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 19.735.214 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 18.747.573 |
| `91.9112` | Alta dirección / Actividad legislativa | 17.590.272 |
| … | *resto: 74 códigos* | 291.642.890 |

</details>

### 2026

*Fuente: `programa_csv.csv` · 167 líneas · total extraído **6.318,65 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.508,38 M€ (1.508.379.759 €) · 9 códigos · 23,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3123` | Sanidad / Atención especializada de salud | 843.380.851 | 55,9 % |
| `31.3122` | Sanidad / Atención primaria de salud | 214.475.780 | 14,2 % |
| `31.3131` | Sanidad / Oferta y uso racional de medicamentos y productos sanitarios | 192.887.307 | 12,8 % |
| `31.3111` | Sanidad / Dirección y servicios generales de sanidad y política social | 187.235.136 | 12,4 % |
| `31.3139` | Sanidad / Otras acciones públicas de protección de la salud | 38.118.192 | 2,5 % |
| `31.3128` | Sanidad / Infraestructura y equipamiento de centros sanitarios | 23.643.658 | 1,6 % |
| `31.3127` | Sanidad / Servicios auxiliares de centros sanitarios | 7.584.754 | 0,5 % |
| `31.3112` | Sanidad / Formación sanitaria | 891.534 | 0,1 % |
| `31.3132` | Sanidad / Salud pública y sanidad exterior | 162.547 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.063,94 M€ (1.063.943.100 €) · 19 códigos · 16,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32.3220` | Educación / Dirección y servicios generales de enseñanza | 625.337.621 | 58,8 % |
| `32.3223` | Educación / Enseñanzas universitarias | 107.514.340 | 10,1 % |
| `32.322D` | Educación / Educación primaria | 60.755.751 | 5,7 % |
| `32.3221` | Educación / Educación infantil | 55.263.848 | 5,2 % |
| `32.3222` | Educación / Educación secundaria | 49.467.550 | 4,6 % |
| `32.322E` | Educación / Formación profesional | 33.968.907 | 3,2 % |
| `32.3241` | Educación / Servicios complementarios de la enseñanza | 31.391.762 | 3,0 % |
| `32.3224` | Educación / Educación especial | 21.122.116 | 2,0 % |
| `32.3251` | Educación / Construcción, equipamiento y material didáctico | 20.095.231 | 1,9 % |
| `32.3211` | Educación / Dirección y servicios generales de educación | 18.453.155 | 1,7 % |
| `32.322C` | Educación / Bachillerato | 14.275.794 | 1,3 % |
| `32.322A` | Educación / Nuevas tecnologías aplicadas a la educación | 10.852.619 | 1,0 % |
| `32.3231` | Educación / Becas y ayudas a estudiantes | 4.965.986 | 0,5 % |
| `32.3225` | Educación / Enseñanzas artísticas | 4.642.040 | 0,4 % |
| `32.3229` | Educación / Otras enseñanzas (idiomas, especiales y otros) | 3.695.636 | 0,3 % |
| `32.3212` | Educación / Formación permanente del profesorado de Educación | 1.755.953 | 0,2 % |
| `32.322G` | Educación / Deporte en edad escolar y en la universidad | 180.000 | 0,0 % |
| `32.3227` | Educación / Educación compensatoria y de adultos | 102.791 | 0,0 % |
| `32.3242` | Educación / Apoyo a otras actividades educativas | 102.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 141,03 M€ (141.025.876 €) · 9 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41.4121` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción agrícola | 35.145.455 | 24,9 % |
| `41.4142` | Agricultura, ganadería y alimentación / Desarrollo sostenible del medio rural | 28.214.042 | 20,0 % |
| `41.4141` | Agricultura, ganadería y alimentación / Gestión de los recursos hídricos para el regadío | 22.991.184 | 16,3 % |
| `41.4131` | Agricultura, ganadería y alimentación / Competitividad de la industria agroalimentaria y calidad alimentaria | 18.483.717 | 13,1 % |
| `41.4111` | Agricultura, ganadería y alimentación / Dirección y servicios generales de agricultura, ganadería y alimentación | 17.738.916 | 12,6 % |
| `41.4122` | Agricultura, ganadería y alimentación / Competitividad, calidad y defensa de la producción ganadera | 10.595.482 | 7,5 % |
| `41.4143` | Agricultura, ganadería y alimentación / Reordenación de la propiedad y concentración parcelaria | 7.280.217 | 5,2 % |
| `41.4123` | Agricultura, ganadería y alimentación / Regulación de los mercados agrarios | 558.843 | 0,4 % |
| `41.4144` | Agricultura, ganadería y alimentación / Fomento y mejora de las infraestructuras agrarias | 18.020 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,42 M€ (416.946 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `91.9121` | Alta dirección / Gobierno de Navarra | 416.946 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 155,00 M€ (154.995.622 €) · 7 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `26.2614` | Acceso a la vivienda y fomento de la edificación / Ayudas para rehabilitación, construcción y acceso a la vivienda | 104.034.509 | 67,1 % |
| `26.2616` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora de la infraestructura urbana en el ámbito municipal | 33.226.132 | 21,4 % |
| `26.2612` | Acceso a la vivienda y fomento de la edificación / Promoción y administración de viviendas | 7.293.517 | 4,7 % |
| `26.2611` | Acceso a la vivienda y fomento de la edificación / Dirección y servicios generales de vivienda | 5.440.384 | 3,5 % |
| `26.2617` | Acceso a la vivienda y fomento de la edificación / Urbanismo y política del suelo | 3.225.083 | 2,1 % |
| `45.4516` | Infraestructuras / Dirección y servicios generales de urbanismo | 1.452.497 | 0,9 % |
| `26.2615` | Acceso a la vivienda y fomento de la edificación / Mantenimiento y mejora del patrimonio inmobiliario | 323.500 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 77,69 M€ (77.686.463 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `24.2411` | Fomento del empleo / Fomento de la inserción y estabilidad laboral | 36.558.067 | 47,1 % |
| `24.2413` | Fomento del empleo / Actuaciones en el mercado de trabajo | 13.201.843 | 17,0 % |
| `49.4941` | Otras actuaciones de carácter económico / Administración de las relaciones laborales y condiciones de trabajo | 8.719.859 | 11,2 % |
| `24.2422` | Fomento del empleo / Escuelas taller, casas de oficios y talleres de empleo | 8.465.750 | 10,9 % |
| `24.2421` | Fomento del empleo / Formación profesional ocupacional | 7.853.944 | 10,1 % |
| `24.2412` | Fomento del empleo / Desarrollo de la economía social y de la responsabilidad social de las empresas | 2.887.000 | 3,7 % |

</details>

<details open><summary><b><code>idi</code> — 78,11 M€ (78.112.661 €) · 8 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `46.4673` | Investigación, desarrollo e innovación / Investigación y desarrollo tecnológico-industrial | 55.535.497 | 71,1 % |
| `46.4651` | Investigación, desarrollo e innovación / Investigación sanitaria | 7.651.388 | 9,8 % |
| `49.4911` | Otras actuaciones de carácter económico / Ordenación, administración y promoción de las telecomunicaciones y de la sociedad de la información | 5.797.370 | 7,4 % |
| `46.4679` | Investigación, desarrollo e innovación / Innovación tecnológica de las telecomunicaciones | 3.886.010 | 5,0 % |
| `46.4674` | Investigación, desarrollo e innovación / Investigación y experimentación agraria y forestal | 2.771.759 | 3,5 % |
| `46.4621` | Investigación, desarrollo e innovación / Investigación y estudios sociológicos | 1.173.065 | 1,5 % |
| `46.4681` | Investigación, desarrollo e innovación / Estudios técnicos en el sector agrario | 883.572 | 1,1 % |
| `46.4691` | Investigación, desarrollo e innovación / Otras Innovaciones Tecnológicas | 414.000 | 0,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 266,74 M€ (266.742.173 €) · 1 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.231B` | Servicios sociales y promoción social / Autonomía personal y atención a la dependencia | 266.742.173 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 45,73 M€ (45.731.453 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31.3124` | Sanidad / Asistencia psiquiátrica y psíquica | 45.731.453 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,69 M€ (6.692.492 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2319` | Servicios sociales y promoción social / Integración de los inmigrantes | 6.692.492 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,13 M€ (25.129.683 €) · 5 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43.4321` | Comercio, Turismo y Pymes / Coordinación y promoción del turismo | 18.195.258 | 72,4 % |
| `43.4314` | Comercio, Turismo y Pymes / Ordenación y modernización de las estructuras comerciales | 2.860.187 | 11,4 % |
| `45.4583` | Infraestructuras / Infraestructura turística | 2.842.354 | 11,3 % |
| `43.4312` | Comercio, Turismo y Pymes / Dirección y servicios generales de comercio y turismo | 846.884 | 3,4 % |
| `43.4313` | Comercio, Turismo y Pymes / Ordenación y promoción del comercio exterior | 385.000 | 1,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,07 M€ (8.068.171 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `23.2322` | Servicios sociales y promoción social / Igualdad de oportunidades entre mujeres y hombres | 4.762.671 | 59,0 % |
| `23.2323` | Servicios sociales y promoción social / Actuaciones para la previsión integral de la violencia de género | 3.305.500 | 41,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.941,73 M€ · 98 códigos · 46,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `94.9411` | Transferencias a otras administraciones públicas / Convenio económico con el Estado | 932.224.800 |
| `94.9421` | Transferencias a otras administraciones públicas / Participación en los tributos de la Hacienda Pública de Navarra | 345.601.242 |
| `23.2315` | Servicios sociales y promoción social / Protección a la familia | 209.545.270 |
| `21.2111` | Pensiones / Pensiones contributivas | 132.142.741 |
| `45.4532` | Infraestructuras / Creación de infraestructura de carreteras | 131.456.155 |
| `92.9214` | Servicios de carácter general / Administración, gestión y control de personal | 97.320.243 |
| `13.1321` | Seguridad ciudadana e instituciones penitenciarias / Seguridad ciudadana | 93.621.320 |
| `23.2317` | Servicios sociales y promoción social / Atención a la infancia | 68.449.836 |
| `44.4411` | Subvenciones al transporte / Subvenciones y apoyo al transporte terrestre | 64.401.286 |
| `45.4533` | Infraestructuras / Conservación y explotación de carreteras | 60.325.470 |
| `95.9511` | Deuda pública / Amortización y gastos financieros de la deuda pública en moneda nacional | 49.183.324 |
| `42.4252` | Industria y energía / Incentivos sobre medidas energéticas | 48.955.399 |
| `92.921C` | Servicios de carácter general / Informática | 46.124.560 |
| `13.1342` | Seguridad ciudadana e instituciones penitenciarias / Prevención y extinción de incendios y salvamento | 43.388.630 |
| `11.1121` | Justicia / Órganos judiciales | 40.075.821 |
| `92.9234` | Servicios de carácter general / Dirección y servicios generales de economía y hacienda | 36.681.652 |
| `92.9211` | Servicios de carácter general / Dirección, organización y servicios generales de la Administración Pública | 27.125.435 |
| `21.2121` | Pensiones / Pensiones no contributivas y prestaciones asistenciales | 25.726.075 |
| `33.3361` | Cultura / Fomento y apoyo de las actividades deportivas | 25.453.338 |
| `33.3341` | Cultura / Promoción y cooperación cultural | 24.131.233 |
| `45.4562` | Infraestructuras / Protección y mejora del medio ambiente | 23.715.282 |
| `94.9423` | Transferencias a otras administraciones públicas / Otras transferencias | 22.386.670 |
| `14.1431` | Política exterior / Cooperación para el desarrollo | 20.770.067 |
| `23.2310` | Servicios sociales y promoción social / Programación general de protección y promoción social | 20.030.277 |
| `93.9321` | Administración financiera y tributaria / Aplicación del sistema tributario | 19.960.136 |
| … | *resto: 73 códigos* | 332.931.522 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py nav     # regenera este documento
python3 tools/auditoria_magnitud.py nav        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa nav --anio <año> \
    --input ../fuentes/raw/nav/<año>/<fichero> --output /tmp/nav.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-nav.md`](limitaciones-nav.md)

