# Trazabilidad de la extracción — Castilla-La Mancha (`clm`)

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
| **2015** | 99 | `gastos_articulo.csv` | 12 | 51,5 % | 6.944,82 | — | no_aplica |
| **2016** | 99 | `gastos_articulo.csv` | 12 | 53,5 % | 7.114,21 | — | no_aplica |
| **2017** | 98 | `gastos_articulo.csv` | 12 | 54,1 % | 7.406,20 | — | no_aplica |
| **2018** | 98 | `gastos_articulo.csv` | 12 | 54,1 % | 7.609,67 | — | no_aplica |
| **2019** | 99 | `gastos_articulo.csv` | 12 | 53,5 % | 7.609,67 | — | no_aplica |
| **2020** | 100 | `gastos_articulo.csv` | 12 | 53,0 % | 8.093,15 | — | no_aplica |
| **2021** | 101 | `gastos_articulo.csv` | 12 | 52,5 % | 9.667,09 | — | no_aplica |
| **2022** | 111 | `tomo_I.pdf` | 12 | 50,5 % | 12.260,99 | — | no_aplica |
| **2023** | 114 | `tomo_I.pdf` | 12 | 49,1 % | 12.418,77 | — | no_aplica |
| **2024** | 114 | `tomo_I.pdf` | 12 | 50,0 % | 12.473,34 | — | no_aplica |
| **2025** | 113 | `tomo_I.pdf` | 12 | 50,4 % | 12.716,18 | — | no_aplica |
| **2026** | 113 | `tomo_I.pdf` | 12 | 50,4 % | 12.903,39 | — | no_aplica |

**URL(s) de origen:**
- <https://datosabiertos.castillalamancha.es/sites/datosabiertos.castillalamancha.es/files/2021-gastosf-comunidad-castilla-la-mancha.csv>
- <https://transparencia.castillalamancha.es/actuacion/ley-de-presupuestos-generales-de-castilla-la-mancha-2024>
- <https://transparencia.castillalamancha.es/actuacion/ley-de-presupuestos-generales-de-castilla-la-mancha-2025>
- <https://transparencia.castillalamancha.es/sites/default/files/migrate/actuaciones/087387da_tomo_1._texto_articulado_estado_de_ingresos_estados_de_gastos_y_pto_beneficios_fiscales.pdf>
- <https://transparencia.castillalamancha.es/sites/default/files/migrate/actuaciones/2f371878_tomo_i_v1_texto_articulado_estado_de_ingresos_y_estado_de_gastos.pdf>
- <https://transparencia.castillalamancha.es/sites/default/files/migrate/actuaciones/303dd96d_tomo_1._texto_articulado_estado_de_ingresos_estados_de_gastos_y_pto_beneficios_fiscales.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 2.443,11 | 2.651,78 | 2.745,00 | 2.828,44 | 2.828,44 | 3.060,23 | 3.740,07 | 3.697,84 | 3.700,36 | 3.934,18 | 3.860,44 | 4.152,86 |
| `educacion` | 1.515,80 | 1.649,85 | 1.718,01 | 1.801,38 | 1.801,38 | 1.947,04 | 2.231,74 | 2.354,32 | 2.424,97 | 2.473,72 | 2.530,78 | 2.633,02 |
| `soberania` | 1.236,88 | 1.264,10 | 1.268,57 | 1.276,30 | 1.276,30 | 1.286,28 | 1.322,22 | 1.323,42 | 1.328,09 | 1.368,50 | 1.332,42 | 1.334,98 |
| `direccion` | 21,76 | 12,76 | 13,40 | 14,21 | 14,21 | 15,82 | 18,20 | 21,32 | 21,09 | 18,37 | 19,41 | 21,05 |
| `vivienda` | 48,56 | 42,98 | 45,41 | 49,73 | 49,73 | 59,40 | 110,84 | 106,60 | 223,49 | 232,40 | 218,23 | 270,55 |
| `empleo` | 53,55 | 66,48 | 76,28 | 78,56 | 78,56 | 76,33 | 77,02 | 82,84 | 117,38 | 121,45 | 124,34 | 121,71 |
| `idi` | 21,46 | 22,79 | 23,57 | 24,11 | 24,11 | 27,04 | 38,49 | 39,52 | 42,62 | 38,67 | 44,93 | 50,87 |
| `dependencia` | 394,65 | 388,70 | 405,95 | 413,56 | 413,56 | 451,89 | 520,82 | 539,40 | 534,66 | 534,59 | 521,49 | 545,79 |
| `discapacidad` | 99,39 | 101,11 | 104,89 | 108,33 | 108,33 | 116,35 | 125,23 | 137,28 | 150,71 | 158,26 | 156,85 | 159,13 |
| `salud_mental` | 61,03 | 101,00 | 114,80 | 121,44 | 121,44 | 118,82 | 124,58 | 141,66 | 154,45 | 157,48 | 154,20 | 166,22 |
| `turismo` | 10,12 | 10,29 | 10,84 | 15,31 | 15,31 | 16,50 | 37,80 | 104,30 | 109,42 | 122,27 | 108,19 | 89,97 |
| `igualdad` | 14,71 | 16,66 | 17,47 | 18,06 | 18,06 | 23,89 | 29,30 | 46,37 | 47,09 | 50,06 | 46,92 | 48,13 |
| **Σ asignado** | 5.920,99 | 6.328,49 | 6.544,19 | 6.749,43 | 6.749,43 | 7.199,57 | 8.376,30 | 8.594,87 | 8.854,33 | 9.209,96 | 9.118,21 | 9.594,28 |
| *(sin concepto)* | 1.023,83 | 785,73 | 862,00 | 860,24 | 860,24 | 893,58 | 1.290,79 | 3.666,12 | 3.564,44 | 3.263,38 | 3.597,97 | 3.309,11 |
| **TOTAL extraído** | 6.944,82 | 7.114,21 | 7.406,20 | 7.609,67 | 7.609,67 | 8.093,15 | 9.667,09 | 12.260,99 | 12.418,77 | 12.473,34 | 12.716,18 | 12.903,39 |

**Conceptos sin ninguna línea en toda la serie:** `diversidad` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +8,5 % | +3,5 % | +3,0 % | +0,0 % | +8,2 % | +22,2 % | −1,1 % | +0,1 % | +6,3 % | −1,9 % | +7,6 % |
| `educacion` | +8,8 % | +4,1 % | +4,9 % | +0,0 % | +8,1 % | +14,6 % | +5,5 % | +3,0 % | +2,0 % | +2,3 % | +4,0 % |
| `soberania` | +2,2 % | +0,4 % | +0,6 % | +0,0 % | +0,8 % | +2,8 % | +0,1 % | +0,4 % | +3,0 % | −2,6 % | +0,2 % |
| `direccion` | −41,3 % ⚠ | +5,0 % | +6,0 % | +0,0 % | +11,3 % | +15,1 % | +17,2 % | −1,1 % | −12,9 % | +5,7 % | +8,4 % |
| `vivienda` | −11,5 % | +5,6 % | +9,5 % | +0,0 % | +19,4 % | +86,6 % ⚠ | −3,8 % | +109,7 % ⚠ | +4,0 % | −6,1 % | +24,0 % |
| `empleo` | +24,1 % | +14,8 % | +3,0 % | +0,0 % | −2,8 % | +0,9 % | +7,6 % | +41,7 % ⚠ | +3,5 % | +2,4 % | −2,1 % |
| `idi` | +6,2 % | +3,4 % | +2,3 % | +0,0 % | +12,2 % | +42,4 % ⚠ | +2,7 % | +7,8 % | −9,3 % | +16,2 % | +13,2 % |
| `dependencia` | −1,5 % | +4,4 % | +1,9 % | +0,0 % | +9,3 % | +15,3 % | +3,6 % | −0,9 % | −0,0 % | −2,5 % | +4,7 % |
| `discapacidad` | +1,7 % | +3,7 % | +3,3 % | +0,0 % | +7,4 % | +7,6 % | +9,6 % | +9,8 % | +5,0 % | −0,9 % | +1,5 % |
| `salud_mental` | +65,5 % ⚠ | +13,7 % | +5,8 % | +0,0 % | −2,2 % | +4,8 % | +13,7 % | +9,0 % | +2,0 % | −2,1 % | +7,8 % |
| `turismo` | +1,7 % | +5,4 % | +41,2 % ⚠ | +0,0 % | +7,8 % | +129,1 % ⚠ | +176,0 % ⚠ | +4,9 % | +11,8 % | −11,5 % | −16,8 % |
| `igualdad` | +13,3 % | +4,9 % | +3,4 % | +0,0 % | +32,3 % | +22,7 % | +58,3 % ⚠ | +1,6 % | +6,3 % | −6,3 % | +2,6 % |
| **TOTAL** | +2,4 % | +4,1 % | +2,7 % | +0,0 % | +6,4 % | +19,4 % | +26,8 % | +1,3 % | +0,4 % | +1,9 % | +1,5 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `salud_mental` | **SALTO** | 61,03 → 101,00 M€ (+65,5 % ⚠) |
| 2021 | `vivienda` | **SALTO** | 59,40 → 110,84 M€ (+86,6 % ⚠) |
| 2022 | `TOTAL` | **SALTO** | 9.667,09 → 12.260,99 M€ (+26,8 %) |
| 2022 | `turismo` | **SALTO** | 37,80 → 104,30 M€ (+176,0 % ⚠) |
| 2023 | `empleo` | **SALTO** | 82,84 → 117,38 M€ (+41,7 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 106,60 → 223,49 M€ (+109,7 % ⚠) |

### 4.1 · Códigos duplicados dentro del mismo año (25 casos, 4.091,56 M€ acumulados)

> Un mismo código aparece en **varias filas del mismo ejercicio**. Puede ser legítimo
> (mismo programa en varias secciones/centros gestores) o **doble conteo** que infla el total.
> Compruébalo contra el documento original antes de dar el año por bueno.

| Año | Código | Concepto | Filas | Importe sumado (M€) |
|---|---|---|---:|---:|
| 2023 | `718A` | `soberania` | 2 | 944,04 |
| 2022 | `718A` | `soberania` | 2 | 921,03 |
| 2024 | `521B` | `(sin concepto)` | 7 | 237,92 |
| 2023 | `521B` | `(sin concepto)` | 7 | 210,46 |
| 2022 | `521B` | `(sin concepto)` | 6 | 210,12 |
| 2026 | `521B` | `(sin concepto)` | 6 | 201,36 |
| 2025 | `521B` | `(sin concepto)` | 6 | 197,02 |
| 2024 | `512A` | `(sin concepto)` | 2 | 119,93 |
| 2023 | `512A` | `(sin concepto)` | 2 | 119,93 |
| 2026 | `512A` | `(sin concepto)` | 2 | 119,76 |
| 2022 | `512A` | `(sin concepto)` | 2 | 111,44 |
| 2025 | `512A` | `(sin concepto)` | 2 | 103,95 |
| 2026 | `126C` | `(sin concepto)` | 2 | 71,24 |
| 2025 | `126C` | `(sin concepto)` | 2 | 68,68 |
| 2024 | `126C` | `(sin concepto)` | 2 | 64,81 |
| 2023 | `126C` | `(sin concepto)` | 2 | 62,77 |
| 2022 | `126C` | `(sin concepto)` | 2 | 59,95 |
| 2024 | `323B` | `igualdad` | 2 | 50,06 |
| 2026 | `323B` | `igualdad` | 2 | 48,13 |
| 2025 | `323B` | `igualdad` | 2 | 46,92 |
| 2026 | `541B` | `idi` | 3 | 25,78 |
| 2023 | `541B` | `idi` | 3 | 25,17 |
| 2022 | `541B` | `idi` | 3 | 24,97 |
| 2025 | `541B` | `idi` | 3 | 23,43 |
| 2024 | `541B` | `idi` | 3 | 22,69 |

### 4.2 · Códigos que CAMBIAN de concepto entre años (1 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `315A` | 10,34 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:sanidad, 2025:sanidad, 2026:sanidad |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `gastos_articulo.csv` · 99 líneas · total extraído **6.944,82 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.443,11 M€ (2.443.105.240 €) · 10 códigos · 35,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.244.975.330 | 91,9 % |
| `412C` | Selección y formación del personal sanitario | 52.416.280 | 2,1 % |
| `311A` | Dirección y S.G. bienestar social | 30.283.020 | 1,2 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 27.238.920 | 1,1 % |
| `312A` | Pensiones y prestaciones asistenciales | 24.851.110 | 1,0 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 19.584.290 | 0,8 % |
| `411B` | Gestión y administración sanitaria | 18.653.930 | 0,8 % |
| `413A` | Epidemiología y promoción de la salud | 16.143.290 | 0,7 % |
| `413C` | Inspección sanitaria | 5.164.150 | 0,2 % |
| `541E` | Investigación sanitaria | 3.794.920 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.515,80 M€ (1.515.797.070 €) · 12 códigos · 21,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 559.844.530 | 36,9 % |
| `422A` | Educación infantil y primaria | 527.667.760 | 34,8 % |
| `422C` | Enseñanza universitaria | 137.277.760 | 9,1 % |
| `422D` | Atención a la diversidad | 114.312.890 | 7,5 % |
| `423A` | Promoción educativa | 41.702.260 | 2,8 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 38.256.290 | 2,5 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 35.282.210 | 2,3 % |
| `422F` | Educación permanente de adultos | 22.637.570 | 1,5 % |
| `322B` | Fomento y gestión del empleo | 20.379.790 | 1,3 % |
| `322A` | Relaciones laborales | 15.989.150 | 1,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.284.110 | 0,1 % |
| `442E` | Promoción y educación ambiental | 1.162.750 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.236,88 M€ (1.236.879.940 €) · 8 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 888.197.130 | 71,8 % |
| `716A` | Industrias y calidad agroalimentaria | 135.816.640 | 11,0 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 79.450.690 | 6,4 % |
| `717A` | Promoción y desarrollo rural | 61.236.780 | 5,0 % |
| `531A` | Regadíos y explotaciones agrarias | 43.110.180 | 3,5 % |
| `713B` | Producción animal | 15.799.370 | 1,3 % |
| `713A` | Producción vegetal | 11.858.830 | 1,0 % |
| `719A` | Producción, comercialización e industria vitivinícola | 1.410.320 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 21,76 M€ (21.757.310 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 21.757.310 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 48,56 M€ (48.559.460 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 41.398.310 | 85,3 % |
| `432A` | Gestión del urbanismo | 6.680.160 | 13,8 % |
| `432B` | Planificación territorial y sostenibilidad | 480.990 | 1,0 % |

</details>

<details open><summary><b><code>empleo</code> — 53,55 M€ (53.549.430 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 39.923.600 | 74,6 % |
| `324B` | Programas mixtos de formación y empleo | 13.625.830 | 25,4 % |

</details>

<details open><summary><b><code>idi</code> — 21,46 M€ (21.456.800 €) · 5 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 14.569.560 | 67,9 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 16,3 % |
| `541C` | Investigación y experimentación agraria | 3.230.240 | 15,1 % |
| `541H` | Investigación agroalimentaria y forestal | 153.000 | 0,7 % |
| `541D` | Investigación y estudios estadísticos y económicos | 4.000 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 394,65 M€ (394.645.380 €) · 2 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 389.383.670 | 98,7 % |
| `313B` | Prevención y apoyo a las familias | 5.261.710 | 1,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 99,39 M€ (99.388.360 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 99.388.360 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 61,03 M€ (61.025.190 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Atención y acompañamiento al menor | 35.054.230 | 57,4 % |
| `313A` | Programas sociales básicos | 25.970.960 | 42,6 % |

</details>

<details open><summary><b><code>turismo</code> — 10,12 M€ (10.119.350 €) · 4 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 5.491.200 | 54,3 % |
| `751B` | Promoción exterior | 3.725.550 | 36,8 % |
| `751D` | Ordenación y promoción de la artesanía | 452.600 | 4,5 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 4,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,71 M€ (14.706.850 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 14.706.850 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.023,83 M€ · 48 códigos · 14,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 427.519.520 |
| `442B` | Ordenación y conservación del medio natural | 100.726.930 |
| `513A` | Creación de infraestructuras de carreteras | 79.078.360 |
| `521B` | Desarrollo de la sociedad de la información | 71.318.260 |
| `513B` | Conservación y explotación de carreteras | 53.050.280 |
| `512A` | Creación de infraestructuras hidráulicas | 38.028.590 |
| `126C` | Medios de comunicación | 36.775.020 |
| `511A` | Dirección y servicios generales de fomento | 18.801.260 |
| `724A` | Competitividad empresarial | 17.532.160 |
| `613A` | Gestión tributaria | 14.582.910 |
| `452A` | Libros, archivos y bibliotecas | 12.702.590 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 11.776.020 |
| `722A` | Política industrial y energética | 11.470.650 |
| `513C` | Ordenación e inspección del transporte | 11.302.060 |
| `458A` | Patrimonio artístico y museos | 11.258.590 |
| `221A` | Protección ciudadana | 9.191.060 |
| `111A` | Actividad legislativa | 8.638.000 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 8.037.560 |
| `612C` | Control interno y contabilidad pública | 7.924.140 |
| `612D` | Administración del patrimonio | 7.566.780 |
| `121C` | Relación con las corporaciones locales | 7.558.440 |
| `121A` | Dirección y S.G. de presidencia y administraciones públicas | 7.106.410 |
| `521A` | Telecomunicaciones | 5.528.500 |
| `121B` | Administración de la función pública | 4.867.480 |
| `455A` | Gestión cultural | 4.193.870 |
| … | *resto: 23 códigos* | 37.294.130 |

</details>

### 2016

*Fuente: `gastos_articulo.csv` · 99 líneas · total extraído **7.114,21 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.651,78 M€ (2.651.780.070 €) · 12 códigos · 37,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.453.001.470 | 92,5 % |
| `412C` | Selección y formación del personal sanitario | 52.927.680 | 2,0 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 26.990.670 | 1,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 26.969.280 | 1,0 % |
| `311A` | Dirección y S.G. bienestar social | 21.168.390 | 0,8 % |
| `411B` | Gestión y administración sanitaria | 18.149.570 | 0,7 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 17.156.980 | 0,6 % |
| `413A` | Epidemiología y promoción de la salud | 17.036.990 | 0,6 % |
| `411A` | Direccion y servicios generales de sanidad | 6.509.530 | 0,2 % |
| `413C` | Inspección sanitaria | 4.807.460 | 0,2 % |
| `541E` | Investigación sanitaria | 4.502.170 | 0,2 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 2.559.880 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.649,85 M€ (1.649.848.580 €) · 13 códigos · 23,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 604.407.970 | 36,6 % |
| `422A` | Educación infantil y primaria | 536.437.120 | 32,5 % |
| `422C` | Enseñanza universitaria | 141.712.080 | 8,6 % |
| `422D` | Atención a la diversidad | 123.505.960 | 7,5 % |
| `322B` | Fomento y gestión del empleo | 111.308.210 | 6,7 % |
| `423A` | Promoción educativa | 42.916.300 | 2,6 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 35.734.960 | 2,2 % |
| `422F` | Educación permanente de adultos | 23.658.030 | 1,4 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 13.493.010 | 0,8 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 13.046.560 | 0,8 % |
| `322A` | Relaciones laborales | 1.390.720 | 0,1 % |
| `442E` | Promoción y educación ambiental | 1.228.950 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.008.710 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.264,10 M€ (1.264.101.430 €) · 7 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 953.603.580 | 75,4 % |
| `716A` | Industrias y calidad agroalimentaria | 125.189.460 | 9,9 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 79.673.340 | 6,3 % |
| `717A` | Promoción y desarrollo rural | 42.667.660 | 3,4 % |
| `531A` | Regadíos y explotaciones agrarias | 36.275.670 | 2,9 % |
| `713B` | Producción animal | 15.304.390 | 1,2 % |
| `713A` | Producción vegetal | 11.387.330 | 0,9 % |

</details>

<details open><summary><b><code>direccion</code> — 12,76 M€ (12.761.500 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 12.761.500 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 42,98 M€ (42.983.640 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 38.689.080 | 90,0 % |
| `432A` | Gestión del urbanismo | 3.746.310 | 8,7 % |
| `432B` | Planificación territorial y sostenibilidad | 548.250 | 1,3 % |

</details>

<details open><summary><b><code>empleo</code> — 66,48 M€ (66.476.340 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 49.478.640 | 74,4 % |
| `324B` | Programas mixtos de formación y empleo | 16.997.700 | 25,6 % |

</details>

<details open><summary><b><code>idi</code> — 22,79 M€ (22.786.400 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 9.930.230 | 43,6 % |
| `541H` | Investigación agroalimentaria y forestal | 6.004.790 | 26,4 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 15,4 % |
| `541C` | Investigación y experimentación agraria | 3.351.380 | 14,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 388,70 M€ (388.696.810 €) · 3 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 266.988.300 | 68,7 % |
| `313H` | Atención a la dependencia | 114.791.690 | 29,5 % |
| `313B` | Prevención y apoyo a las familias | 6.916.820 | 1,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 101,11 M€ (101.107.350 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 101.107.350 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 101,00 M€ (100.998.450 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 64.960.170 | 64,3 % |
| `313E` | Atención y acompañamiento al menor | 36.038.280 | 35,7 % |

</details>

<details open><summary><b><code>turismo</code> — 10,29 M€ (10.289.070 €) · 4 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 5.610.300 | 54,5 % |
| `751B` | Promoción exterior | 3.726.170 | 36,2 % |
| `751D` | Ordenación y promoción de la artesanía | 502.600 | 4,9 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 4,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,66 M€ (16.658.040 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 16.658.040 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 785,73 M€ · 46 códigos · 11,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 219.755.000 |
| `442B` | Ordenación y conservación del medio natural | 95.650.740 |
| `521B` | Desarrollo de la sociedad de la información | 73.490.440 |
| `513A` | Creación de infraestructuras de carreteras | 72.626.340 |
| `513B` | Conservación y explotación de carreteras | 43.606.450 |
| `126C` | Medios de comunicación | 39.739.170 |
| `512A` | Creación de infraestructuras hidráulicas | 32.143.190 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 18.986.640 |
| `724A` | Competitividad empresarial | 16.380.430 |
| `511A` | Dirección y servicios generales de fomento | 15.676.120 |
| `613A` | Gestión tributaria | 13.511.790 |
| `452A` | Libros, archivos y bibliotecas | 13.507.780 |
| `458A` | Patrimonio artístico y museos | 11.477.700 |
| `513C` | Ordenación e inspección del transporte | 11.134.040 |
| `722A` | Política industrial y energética | 11.057.480 |
| `111A` | Actividad legislativa | 9.693.000 |
| `221A` | Protección ciudadana | 8.316.030 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 8.280.770 |
| `612D` | Administración del patrimonio | 8.059.520 |
| `612C` | Control interno y contabilidad pública | 7.677.240 |
| `121C` | Relación con las corporaciones locales | 7.594.820 |
| `442C` | Gestión y protección de espacios naturales | 5.441.860 |
| `455A` | Gestión cultural | 4.895.230 |
| `121B` | Administración de la función pública | 4.361.220 |
| `442D` | Calidad ambiental | 3.868.330 |
| … | *resto: 21 códigos* | 28.795.000 |

</details>

### 2017

*Fuente: `gastos_articulo.csv` · 98 líneas · total extraído **7.406,20 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.745,00 M€ (2.745.004.850 €) · 12 códigos · 37,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.536.673.570 | 92,4 % |
| `412C` | Selección y formación del personal sanitario | 54.128.520 | 2,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 29.360.240 | 1,1 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 28.324.020 | 1,0 % |
| `413A` | Epidemiología y promoción de la salud | 20.578.950 | 0,7 % |
| `311A` | Dirección y S.G. bienestar social | 20.035.260 | 0,7 % |
| `411B` | Gestión y administración sanitaria | 18.784.170 | 0,7 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 17.495.030 | 0,6 % |
| `411A` | Direccion y servicios generales de sanidad | 9.265.100 | 0,3 % |
| `541E` | Investigación sanitaria | 4.205.770 | 0,2 % |
| `413C` | Inspección sanitaria | 3.678.150 | 0,1 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 2.476.070 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.718,01 M€ (1.718.009.180 €) · 13 códigos · 23,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 626.029.930 | 36,4 % |
| `422A` | Educación infantil y primaria | 566.455.010 | 33,0 % |
| `422C` | Enseñanza universitaria | 151.501.830 | 8,8 % |
| `422D` | Atención a la diversidad | 129.221.340 | 7,5 % |
| `322B` | Fomento y gestión del empleo | 113.322.320 | 6,6 % |
| `423A` | Promoción educativa | 42.983.530 | 2,5 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 37.834.690 | 2,2 % |
| `422F` | Educación permanente de adultos | 22.295.270 | 1,3 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 13.593.560 | 0,8 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 10.734.320 | 0,6 % |
| `442E` | Promoción y educación ambiental | 1.417.880 | 0,1 % |
| `322A` | Relaciones laborales | 1.390.720 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.228.780 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.268,57 M€ (1.268.571.620 €) · 7 códigos · 17,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 909.689.550 | 71,7 % |
| `716A` | Industrias y calidad agroalimentaria | 143.791.800 | 11,3 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 83.127.930 | 6,6 % |
| `717A` | Promoción y desarrollo rural | 52.446.050 | 4,1 % |
| `531A` | Regadíos y explotaciones agrarias | 47.683.570 | 3,8 % |
| `713B` | Producción animal | 16.444.670 | 1,3 % |
| `713A` | Producción vegetal | 15.388.050 | 1,2 % |

</details>

<details open><summary><b><code>direccion</code> — 13,40 M€ (13.400.260 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 13.400.260 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 45,41 M€ (45.406.150 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 40.242.270 | 88,6 % |
| `432A` | Gestión del urbanismo | 4.397.800 | 9,7 % |
| `432B` | Planificación territorial y sostenibilidad | 766.080 | 1,7 % |

</details>

<details open><summary><b><code>empleo</code> — 76,28 M€ (76.282.560 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 54.361.530 | 71,3 % |
| `324B` | Programas mixtos de formación y empleo | 21.921.030 | 28,7 % |

</details>

<details open><summary><b><code>idi</code> — 23,57 M€ (23.570.030 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 10.922.250 | 46,3 % |
| `541H` | Investigación agroalimentaria y forestal | 6.834.150 | 29,0 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 14,8 % |
| `541C` | Investigación y experimentación agraria | 2.313.630 | 9,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 405,95 M€ (405.947.960 €) · 3 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 279.790.040 | 68,9 % |
| `313H` | Atención a la dependencia | 119.044.330 | 29,3 % |
| `313B` | Prevención y apoyo a las familias | 7.113.590 | 1,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 104,89 M€ (104.891.360 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 104.891.360 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 114,80 M€ (114.799.440 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 77.533.850 | 67,5 % |
| `313E` | Atención y acompañamiento al menor | 37.265.590 | 32,5 % |

</details>

<details open><summary><b><code>turismo</code> — 10,84 M€ (10.842.640 €) · 4 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 6.070.190 | 56,0 % |
| `751B` | Promoción exterior | 3.789.850 | 35,0 % |
| `751D` | Ordenación y promoción de la artesanía | 532.600 | 4,9 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 4,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 17,47 M€ (17.467.220 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 17.467.220 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 862,00 M€ · 45 códigos · 11,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 235.895.000 |
| `442B` | Ordenación y conservación del medio natural | 100.430.180 |
| `513A` | Creación de infraestructuras de carreteras | 84.254.330 |
| `521B` | Desarrollo de la sociedad de la información | 77.947.030 |
| `513B` | Conservación y explotación de carreteras | 44.493.310 |
| `126C` | Medios de comunicación | 41.196.180 |
| `512A` | Creación de infraestructuras hidráulicas | 32.019.590 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 19.224.200 |
| `442D` | Calidad ambiental | 17.250.560 |
| `724A` | Competitividad empresarial | 16.679.320 |
| `513C` | Ordenación e inspección del transporte | 16.676.020 |
| `511A` | Dirección y servicios generales de fomento | 16.074.400 |
| `452A` | Libros, archivos y bibliotecas | 14.601.270 |
| `613A` | Gestión tributaria | 13.890.500 |
| `458A` | Patrimonio artístico y museos | 12.217.230 |
| `722A` | Política industrial y energética | 11.343.580 |
| `221A` | Protección ciudadana | 9.690.710 |
| `111A` | Actividad legislativa | 9.594.000 |
| `612D` | Administración del patrimonio | 9.054.090 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 8.523.190 |
| `633B` | Fondo de contingencia de ejecución presupuestaria | 8.430.000 |
| `612C` | Control interno y contabilidad pública | 7.907.990 |
| `121C` | Relación con las corporaciones locales | 7.689.670 |
| `442C` | Gestión y protección de espacios naturales | 6.638.190 |
| `455A` | Gestión cultural | 5.089.880 |
| … | *resto: 20 códigos* | 35.193.800 |

</details>

### 2018

*Fuente: `gastos_articulo.csv` · 98 líneas · total extraído **7.609,67 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.828,44 M€ (2.828.443.620 €) · 12 códigos · 37,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.612.703.730 | 92,4 % |
| `412C` | Selección y formación del personal sanitario | 55.998.580 | 2,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 34.426.080 | 1,2 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 28.615.350 | 1,0 % |
| `413A` | Epidemiología y promoción de la salud | 20.120.890 | 0,7 % |
| `311A` | Dirección y S.G. bienestar social | 19.241.350 | 0,7 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 18.460.380 | 0,7 % |
| `411B` | Gestión y administración sanitaria | 18.393.200 | 0,7 % |
| `411A` | Direccion y servicios generales de sanidad | 10.057.340 | 0,4 % |
| `541E` | Investigación sanitaria | 4.253.710 | 0,2 % |
| `413C` | Inspección sanitaria | 3.579.450 | 0,1 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 2.593.560 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.801,38 M€ (1.801.375.270 €) · 13 códigos · 23,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 661.554.240 | 36,7 % |
| `422A` | Educación infantil y primaria | 589.546.800 | 32,7 % |
| `422C` | Enseñanza universitaria | 154.045.020 | 8,6 % |
| `422D` | Atención a la diversidad | 134.761.480 | 7,5 % |
| `322B` | Fomento y gestión del empleo | 123.522.200 | 6,9 % |
| `423A` | Promoción educativa | 44.411.440 | 2,5 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 39.152.710 | 2,2 % |
| `422F` | Educación permanente de adultos | 23.392.340 | 1,3 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 13.344.510 | 0,7 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 11.233.870 | 0,6 % |
| `442E` | Promoción y educación ambiental | 3.157.290 | 0,2 % |
| `322A` | Relaciones laborales | 1.992.350 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.261.020 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.276,30 M€ (1.276.302.970 €) · 7 códigos · 16,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 925.939.380 | 72,5 % |
| `716A` | Industrias y calidad agroalimentaria | 108.678.800 | 8,5 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 83.533.120 | 6,5 % |
| `531A` | Regadíos y explotaciones agrarias | 75.343.640 | 5,9 % |
| `717A` | Promoción y desarrollo rural | 52.382.100 | 4,1 % |
| `713B` | Producción animal | 17.963.620 | 1,4 % |
| `713A` | Producción vegetal | 12.462.310 | 1,0 % |

</details>

<details open><summary><b><code>direccion</code> — 14,21 M€ (14.209.970 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 14.209.970 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 49,73 M€ (49.731.840 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 44.449.100 | 89,4 % |
| `432A` | Gestión del urbanismo | 4.501.980 | 9,1 % |
| `432B` | Planificación territorial y sostenibilidad | 780.760 | 1,6 % |

</details>

<details open><summary><b><code>empleo</code> — 78,56 M€ (78.559.290 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 56.637.450 | 72,1 % |
| `324B` | Programas mixtos de formación y empleo | 21.921.840 | 27,9 % |

</details>

<details open><summary><b><code>idi</code> — 24,11 M€ (24.105.210 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 11.751.020 | 48,7 % |
| `541H` | Investigación agroalimentaria y forestal | 6.540.770 | 27,1 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 14,5 % |
| `541C` | Investigación y experimentación agraria | 2.313.420 | 9,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 413,56 M€ (413.563.140 €) · 3 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 284.500.030 | 68,8 % |
| `313H` | Atención a la dependencia | 121.618.840 | 29,4 % |
| `313B` | Prevención y apoyo a las familias | 7.444.270 | 1,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 108,33 M€ (108.328.000 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 108.328.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 121,44 M€ (121.440.700 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 83.136.050 | 68,5 % |
| `313E` | Atención y acompañamiento al menor | 38.304.650 | 31,5 % |

</details>

<details open><summary><b><code>turismo</code> — 15,31 M€ (15.306.490 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 9.755.250 | 63,7 % |
| `751B` | Promoción exterior | 4.068.390 | 26,6 % |
| `751D` | Ordenación y promoción de la artesanía | 1.032.850 | 6,7 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 2,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 18,06 M€ (18.059.020 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 18.059.020 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 860,24 M€ · 45 códigos · 11,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 213.875.000 |
| `442B` | Ordenación y conservación del medio natural | 112.476.050 |
| `513A` | Creación de infraestructuras de carreteras | 87.038.870 |
| `521B` | Desarrollo de la sociedad de la información | 81.336.830 |
| `513B` | Conservación y explotación de carreteras | 47.722.490 |
| `126C` | Medios de comunicación | 41.862.540 |
| `512A` | Creación de infraestructuras hidráulicas | 28.212.220 |
| `513C` | Ordenación e inspección del transporte | 20.974.440 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 19.246.270 |
| `724A` | Competitividad empresarial | 17.190.180 |
| `511A` | Dirección y servicios generales de fomento | 16.363.030 |
| `452A` | Libros, archivos y bibliotecas | 15.227.670 |
| `613A` | Gestión tributaria | 14.005.460 |
| `458A` | Patrimonio artístico y museos | 12.252.460 |
| `722A` | Política industrial y energética | 11.155.150 |
| `111A` | Actividad legislativa | 9.815.000 |
| `221A` | Protección ciudadana | 9.588.360 |
| `612D` | Administración del patrimonio | 9.371.980 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 8.709.350 |
| `633B` | Fondo de contingencia de ejecución presupuestaria | 8.103.050 |
| `612C` | Control interno y contabilidad pública | 7.912.530 |
| `121C` | Relación con las corporaciones locales | 7.664.000 |
| `455A` | Gestión cultural | 6.356.160 |
| `442C` | Gestión y protección de espacios naturales | 6.351.240 |
| `442D` | Calidad ambiental | 6.259.490 |
| … | *resto: 20 códigos* | 41.173.640 |

</details>

### 2019

*Fuente: `gastos_articulo.csv` · 99 líneas · total extraído **7.609,67 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.828,44 M€ (2.828.443.620 €) · 12 códigos · 37,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.612.703.730 | 92,4 % |
| `412C` | Selección y formación del personal sanitario | 55.998.580 | 2,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 34.426.080 | 1,2 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 28.615.350 | 1,0 % |
| `413A` | Epidemiología y promoción de la salud | 20.120.890 | 0,7 % |
| `311A` | Dirección y S.G. bienestar social | 19.241.350 | 0,7 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 18.460.380 | 0,7 % |
| `411B` | Gestión y administración sanitaria | 18.393.200 | 0,7 % |
| `411A` | Direccion y servicios generales de sanidad | 10.057.340 | 0,4 % |
| `541E` | Investigación sanitaria | 4.253.710 | 0,2 % |
| `413C` | Inspección sanitaria | 3.579.450 | 0,1 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 2.593.560 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.801,38 M€ (1.801.375.270 €) · 13 códigos · 23,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 661.554.240 | 36,7 % |
| `422A` | Educación infantil y primaria | 589.546.800 | 32,7 % |
| `422C` | Enseñanza universitaria | 154.045.020 | 8,6 % |
| `422D` | Atención a la diversidad | 134.761.480 | 7,5 % |
| `322B` | Fomento y gestión del empleo | 123.522.200 | 6,9 % |
| `423A` | Promoción educativa | 44.411.440 | 2,5 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 39.152.710 | 2,2 % |
| `422F` | Educación permanente de adultos | 23.392.340 | 1,3 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 13.344.510 | 0,7 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 11.233.870 | 0,6 % |
| `442E` | Promoción y educación ambiental | 3.157.290 | 0,2 % |
| `322A` | Relaciones laborales | 1.992.350 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.261.020 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.276,30 M€ (1.276.302.970 €) · 7 códigos · 16,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 925.939.380 | 72,5 % |
| `716A` | Industrias y calidad agroalimentaria | 108.678.800 | 8,5 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 83.533.120 | 6,5 % |
| `531A` | Regadíos y explotaciones agrarias | 75.343.640 | 5,9 % |
| `717A` | Promoción y desarrollo rural | 52.382.100 | 4,1 % |
| `713B` | Producción animal | 17.963.620 | 1,4 % |
| `713A` | Producción vegetal | 12.462.310 | 1,0 % |

</details>

<details open><summary><b><code>direccion</code> — 14,21 M€ (14.209.970 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 14.209.970 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 49,73 M€ (49.731.840 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 44.449.100 | 89,4 % |
| `432A` | Gestión del urbanismo | 4.501.980 | 9,1 % |
| `432B` | Planificación territorial y sostenibilidad | 780.760 | 1,6 % |

</details>

<details open><summary><b><code>empleo</code> — 78,56 M€ (78.559.290 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 56.637.450 | 72,1 % |
| `324B` | Programas mixtos de formación y empleo | 21.921.840 | 27,9 % |

</details>

<details open><summary><b><code>idi</code> — 24,11 M€ (24.105.210 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 11.751.020 | 48,7 % |
| `541H` | Investigación agroalimentaria y forestal | 6.540.770 | 27,1 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 14,5 % |
| `541C` | Investigación y experimentación agraria | 2.313.420 | 9,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 413,56 M€ (413.563.140 €) · 3 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 284.500.030 | 68,8 % |
| `313H` | Atención a la dependencia | 121.618.840 | 29,4 % |
| `313B` | Prevención y apoyo a las familias | 7.444.270 | 1,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 108,33 M€ (108.328.000 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 108.328.000 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 121,44 M€ (121.440.700 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 83.136.050 | 68,5 % |
| `313E` | Atención y acompañamiento al menor | 38.304.650 | 31,5 % |

</details>

<details open><summary><b><code>turismo</code> — 15,31 M€ (15.306.490 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 9.755.250 | 63,7 % |
| `751B` | Promoción exterior | 4.068.390 | 26,6 % |
| `751D` | Ordenación y promoción de la artesanía | 1.032.850 | 6,7 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 2,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 18,06 M€ (18.059.020 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 18.059.020 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 860,24 M€ · 46 códigos · 11,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 213.875.000 |
| `442B` | Ordenación y conservación del medio natural | 112.476.050 |
| `513A` | Creación de infraestructuras de carreteras | 87.038.870 |
| `521B` | Desarrollo de la sociedad de la información | 81.336.830 |
| `513B` | Conservación y explotación de carreteras | 47.722.490 |
| `126C` | Medios de comunicación | 41.862.540 |
| `512A` | Creación de infraestructuras hidráulicas | 28.212.220 |
| `513C` | Ordenación e inspección del transporte | 20.974.440 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 19.246.270 |
| `724A` | Competitividad empresarial | 17.190.180 |
| `511A` | Dirección y servicios generales de fomento | 16.363.030 |
| `452A` | Libros, archivos y bibliotecas | 15.227.670 |
| `613A` | Gestión tributaria | 14.005.460 |
| `458A` | Patrimonio artístico y museos | 12.252.460 |
| `722A` | Política industrial y energética | 11.155.150 |
| `111A` | Actividad legislativa | 9.815.000 |
| `221A` | Protección ciudadana | 9.588.360 |
| `612D` | Administración del patrimonio | 9.371.980 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 8.709.350 |
| `633B` | Fondo de contingencia de ejecución presupuestaria | 8.103.050 |
| `612C` | Control interno y contabilidad pública | 7.912.530 |
| `121C` | Relación con las corporaciones locales | 7.664.000 |
| `455A` | Gestión cultural | 6.356.160 |
| `442C` | Gestión y protección de espacios naturales | 6.351.240 |
| `442D` | Calidad ambiental | 6.259.490 |
| … | *resto: 21 códigos* | 41.173.640 |

</details>

### 2020

*Fuente: `gastos_articulo.csv` · 100 líneas · total extraído **8.093,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.060,23 M€ (3.060.234.520 €) · 12 códigos · 37,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 2.826.642.250 | 92,4 % |
| `412C` | Selección y formación del personal sanitario | 60.441.950 | 2,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 46.393.540 | 1,5 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 29.529.270 | 1,0 % |
| `413A` | Epidemiología y promoción de la salud | 20.713.590 | 0,7 % |
| `311A` | Dirección y S.G. bienestar social | 19.735.200 | 0,6 % |
| `411B` | Gestión y administración sanitaria | 18.811.050 | 0,6 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 11.276.160 | 0,4 % |
| `411A` | Direccion y servicios generales de sanidad | 11.012.670 | 0,4 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 7.808.420 | 0,3 % |
| `541E` | Investigación sanitaria | 4.115.800 | 0,1 % |
| `413C` | Inspección sanitaria | 3.754.620 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.947,04 M€ (1.947.035.400 €) · 13 códigos · 24,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 706.211.100 | 36,3 % |
| `422A` | Educación infantil y primaria | 639.537.950 | 32,8 % |
| `422C` | Enseñanza universitaria | 182.569.940 | 9,4 % |
| `422D` | Atención a la diversidad | 144.930.380 | 7,4 % |
| `322B` | Fomento y gestión del empleo | 112.375.590 | 5,8 % |
| `423A` | Promoción educativa | 42.145.720 | 2,2 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 34.787.740 | 1,8 % |
| `422F` | Educación permanente de adultos | 28.348.960 | 1,5 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 23.134.070 | 1,2 % |
| `322A` | Relaciones laborales | 15.838.060 | 0,8 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 14.188.500 | 0,7 % |
| `442E` | Promoción y educación ambiental | 1.856.970 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 1.110.420 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.286,28 M€ (1.286.277.170 €) · 7 códigos · 15,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 926.929.310 | 72,1 % |
| `716A` | Industrias y calidad agroalimentaria | 108.579.970 | 8,4 % |
| `531A` | Regadíos y explotaciones agrarias | 85.197.380 | 6,6 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 84.481.190 | 6,6 % |
| `717A` | Promoción y desarrollo rural | 46.903.790 | 3,6 % |
| `713B` | Producción animal | 21.454.530 | 1,7 % |
| `713A` | Producción vegetal | 12.731.000 | 1,0 % |

</details>

<details open><summary><b><code>direccion</code> — 15,82 M€ (15.816.980 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 15.816.980 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 59,40 M€ (59.397.780 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 48.601.720 | 81,8 % |
| `432A` | Gestión del urbanismo | 10.043.120 | 16,9 % |
| `432B` | Planificación territorial y sostenibilidad | 752.940 | 1,3 % |

</details>

<details open><summary><b><code>empleo</code> — 76,33 M€ (76.325.520 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 50.087.740 | 65,6 % |
| `324B` | Programas mixtos de formación y empleo | 26.237.780 | 34,4 % |

</details>

<details open><summary><b><code>idi</code> — 27,04 M€ (27.037.220 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 14.630.310 | 54,1 % |
| `541H` | Investigación agroalimentaria y forestal | 7.090.150 | 26,2 % |
| `541F` | Fomento de la innovación tecnólogica | 3.500.000 | 12,9 % |
| `541C` | Investigación y experimentación agraria | 1.816.760 | 6,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 451,89 M€ (451.887.760 €) · 3 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 299.085.840 | 66,2 % |
| `313H` | Atención a la dependencia | 144.113.160 | 31,9 % |
| `313B` | Prevención y apoyo a las familias | 8.688.760 | 1,9 % |

</details>

<details open><summary><b><code>discapacidad</code> — 116,35 M€ (116.345.440 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 116.345.440 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 118,82 M€ (118.822.830 €) · 2 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 78.820.850 | 66,3 % |
| `313E` | Atención y acompañamiento al menor | 40.001.980 | 33,7 % |

</details>

<details open><summary><b><code>turismo</code> — 16,50 M€ (16.500.020 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 10.272.690 | 62,3 % |
| `751B` | Promoción exterior | 4.097.330 | 24,8 % |
| `751D` | Ordenación y promoción de la artesanía | 1.680.000 | 10,2 % |
| `751E` | Ordenación y promoción del comercio | 450.000 | 2,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 23,89 M€ (23.888.690 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 23.888.690 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 893,58 M€ · 47 códigos · 11,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 211.050.000 |
| `442B` | Ordenación y conservación del medio natural | 112.296.310 |
| `521B` | Desarrollo de la sociedad de la información | 88.177.900 |
| `513B` | Conservación y explotación de carreteras | 55.992.830 |
| `513A` | Creación de infraestructuras de carreteras | 55.339.810 |
| `126C` | Medios de comunicación | 53.632.860 |
| `512A` | Creación de infraestructuras hidráulicas | 46.785.370 |
| `724A` | Competitividad empresarial | 31.375.810 |
| `513C` | Ordenación e inspección del transporte | 26.492.440 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 21.360.960 |
| `511A` | Dirección y servicios generales de fomento | 15.614.020 |
| `613A` | Gestión tributaria | 15.188.130 |
| `452A` | Libros, archivos y bibliotecas | 14.582.950 |
| `458A` | Patrimonio artístico y museos | 12.460.760 |
| `111A` | Actividad legislativa | 11.253.000 |
| `221A` | Protección ciudadana | 10.229.600 |
| `612D` | Administración del patrimonio | 9.624.060 |
| `722A` | Política industrial y energética | 8.916.510 |
| `612C` | Control interno y contabilidad pública | 8.783.780 |
| `442C` | Gestión y protección de espacios naturales | 8.269.840 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 7.931.770 |
| `455A` | Gestión cultural | 7.410.080 |
| `121C` | Relación con las corporaciones locales | 6.568.460 |
| `121B` | Administración de la función pública | 5.385.300 |
| `633B` | Fondo de contingencia de ejecución presupuestaria | 4.790.370 |
| … | *resto: 22 códigos* | 44.069.110 |

</details>

### 2021

*Fuente: `gastos_articulo.csv` · 101 líneas · total extraído **9.667,09 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.740,07 M€ (3.740.071.530 €) · 12 códigos · 38,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | Atención integrada de la salud | 3.469.900.690 | 92,8 % |
| `412C` | Selección y formación del personal sanitario | 74.938.090 | 2,0 % |
| `312A` | Pensiones y prestaciones asistenciales | 46.999.090 | 1,3 % |
| `413B` | Sanidad ambiental e higiene de los alimentos | 32.160.650 | 0,9 % |
| `413A` | Epidemiología y promoción de la salud | 29.149.810 | 0,8 % |
| `311A` | Dirección y S.G. bienestar social | 22.538.000 | 0,6 % |
| `411B` | Gestión y administración sanitaria | 20.329.610 | 0,5 % |
| `413D` | Calidad y humanización de la asistencia sanitaria | 20.285.050 | 0,5 % |
| `411A` | Direccion y servicios generales de sanidad | 11.363.550 | 0,3 % |
| `541E` | Investigación sanitaria | 5.743.960 | 0,2 % |
| `413C` | Inspección sanitaria | 4.072.060 | 0,1 % |
| `412E` | planificación, atención a la salud e I. sanitarias | 2.590.970 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.231,74 M€ (2.231.740.420 €) · 13 códigos · 23,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | Educación secundaria, F.P. y educación de régimen especial | 811.378.000 | 36,4 % |
| `422A` | Educación infantil y primaria | 709.142.630 | 31,8 % |
| `422C` | Enseñanza universitaria | 198.215.150 | 8,9 % |
| `422D` | Atención a la diversidad | 158.859.990 | 7,1 % |
| `322B` | Fomento y gestión del empleo | 154.752.860 | 6,9 % |
| `423A` | Promoción educativa | 43.033.540 | 1,9 % |
| `421A` | Dirección y S.G. de educación, cultura y deportes | 41.700.990 | 1,9 % |
| `322A` | Relaciones laborales | 39.308.580 | 1,8 % |
| `322C` | Orientación e intermediación en mercado de trabajo | 29.595.960 | 1,3 % |
| `422F` | Educación permanente de adultos | 29.553.810 | 1,3 % |
| `321A` | Dirección y S.G. de economía, empresas y empleo | 13.725.400 | 0,6 % |
| `442E` | Promoción y educación ambiental | 1.554.690 | 0,1 % |
| `421B` | Formación P. profesorado e innovación educativa | 918.820 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 1.322,22 M€ (1.322.219.090 €) · 7 códigos · 13,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | Política agraria comunitaria | 958.252.950 | 72,5 % |
| `531A` | Regadíos y explotaciones agrarias | 126.326.030 | 9,6 % |
| `716A` | Industrias y calidad agroalimentaria | 94.820.320 | 7,2 % |
| `717A` | Promoción y desarrollo rural | 58.567.430 | 4,4 % |
| `711A` | Dirección y S.G. de agricultura, medio ambiente y desarrollo rural | 48.526.930 | 3,7 % |
| `713B` | Producción animal | 22.522.680 | 1,7 % |
| `713A` | Producción vegetal | 13.202.750 | 1,0 % |

</details>

<details open><summary><b><code>direccion</code> — 18,20 M€ (18.200.180 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y servicios generales de la presidencia | 18.200.180 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 110,84 M€ (110.840.190 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Promoción de la vivienda | 95.365.410 | 86,0 % |
| `432A` | Gestión del urbanismo | 11.035.760 | 10,0 % |
| `432B` | Planificación territorial y sostenibilidad | 4.439.020 | 4,0 % |

</details>

<details open><summary><b><code>empleo</code> — 77,02 M€ (77.019.810 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | Formación profesional para el empleo | 48.481.530 | 62,9 % |
| `324B` | Programas mixtos de formación y empleo | 28.538.280 | 37,1 % |

</details>

<details open><summary><b><code>idi</code> — 38,49 M€ (38.493.510 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Investigación, innovación y desarrollo tecnológico | 23.055.890 | 59,9 % |
| `541H` | Investigación agroalimentaria y forestal | 8.859.540 | 23,0 % |
| `541F` | Fomento de la innovación tecnólogica | 4.500.000 | 11,7 % |
| `541C` | Investigación y experimentación agraria | 2.078.080 | 5,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 520,82 M€ (520.818.030 €) · 3 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a las personas mayores | 360.521.230 | 69,2 % |
| `313H` | Atención a la dependencia | 151.904.500 | 29,2 % |
| `313B` | Prevención y apoyo a las familias | 8.392.300 | 1,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 125,23 M€ (125.225.230 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | Atención a las personas con discapacidad | 125.225.230 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 124,58 M€ (124.578.950 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Programas sociales básicos | 83.171.140 | 66,8 % |
| `313E` | Atención y acompañamiento al menor | 41.407.810 | 33,2 % |

</details>

<details open><summary><b><code>turismo</code> — 37,80 M€ (37.795.770 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenación y promoción del turismo | 29.039.070 | 76,8 % |
| `751B` | Promoción exterior | 4.105.500 | 10,9 % |
| `751D` | Ordenación y promoción de la artesanía | 3.367.200 | 8,9 % |
| `751E` | Ordenación y promoción del comercio | 1.284.000 | 3,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 29,30 M€ (29.301.150 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | Promoción de la mujer | 29.301.150 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.290,79 M€ · 48 códigos · 13,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deuda pública | 162.610.000 |
| `442B` | Ordenación y conservación del medio natural | 149.864.040 |
| `512A` | Creación de infraestructuras hidráulicas | 149.348.270 |
| `521B` | Desarrollo de la sociedad de la información | 128.242.920 |
| `513B` | Conservación y explotación de carreteras | 76.123.900 |
| `724A` | Competitividad empresarial | 63.037.860 |
| `442F` | Evaluación ambiental y cambio climático | 61.509.200 |
| `126C` | Medios de comunicación | 54.746.530 |
| `513A` | Creación de infraestructuras de carreteras | 48.298.490 |
| `513C` | Ordenación e inspección del transporte | 46.139.630 |
| `521A` | Telecomunicaciones | 42.576.040 |
| `722A` | Política industrial y energética | 41.523.570 |
| `612D` | Administración del patrimonio | 25.292.490 |
| `442D` | Calidad ambiental | 23.985.570 |
| `452A` | Libros, archivos y bibliotecas | 16.235.820 |
| `458A` | Patrimonio artístico y museos | 16.132.140 |
| `633A` | Imprevistos y funciones no clasificadas | 15.788.920 |
| `511A` | Dirección y servicios generales de fomento | 15.249.440 |
| `613A` | Gestión tributaria | 14.970.650 |
| `611A` | Dirección y S.G. de hacienda y administraciones públicas | 14.895.950 |
| `442A` | Dirección y servicios generales de desarrollo sostenible | 13.152.680 |
| `457A` | Infraestructura, fomento y apoyo al deporte | 11.789.260 |
| `111A` | Actividad legislativa | 11.613.000 |
| `221A` | Protección ciudadana | 10.306.400 |
| `442C` | Gestión y protección de espacios naturales | 10.270.580 |
| … | *resto: 23 códigos* | 67.082.030 |

</details>

### 2022

*Fuente: `tomo_I.pdf` · 111 líneas · total extraído **12.260,99 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.697,84 M€ (3.697.839.940 €) · 12 códigos · 30,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | ATENCIÓN INTEGRADA DE LA SALUD | 3.416.795.180 | 92,4 % |
| `412C` | SELECCIÓN Y FORMACIÓN DEL PERSONAL SANITARIO | 81.035.820 | 2,2 % |
| `312A` | PENSIONES Y PRESTACIONES ASISTENCIALES | 47.052.790 | 1,3 % |
| `413B` | SANIDAD AMBIENTAL E HIGIENE DE LOS ALIMENTOS | 32.372.590 | 0,9 % |
| `413A` | EPIDEMIOLOGÍA Y PROMOCIÓN DE LA SALUD | 27.795.470 | 0,8 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES DE BIENESTAR SOCIAL | 24.591.360 | 0,7 % |
| `413D` | HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 22.334.800 | 0,6 % |
| `411B` | GESTIÓN Y ADMINISTRACIÓN SANITARIA | 22.284.980 | 0,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 12.118.290 | 0,3 % |
| `541E` | INVESTIGACIÓN SANITARIA | 6.028.180 | 0,2 % |
| `413C` | INSPECCIÓN SANITARIA | 4.277.090 | 0,1 % |
| `412E` | PLANIFICACIÓN, ATENCIÓN A LA SALUD E INSTITUCIONES SANITARIAS | 1.153.390 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.354,32 M€ (2.354.316.640 €) · 13 códigos · 19,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | EDUCACIÓN SECUNDARIA, FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE RÉGIMENESPECIAL | 862.694.370 | 36,6 % |
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 743.697.290 | 31,6 % |
| `422C` | ENSEÑANZA UNIVERSITARIA | 206.675.860 | 8,8 % |
| `422D` | ATENCIÓN A LA DIVERSIDAD | 169.546.530 | 7,2 % |
| `322B` | FOMENTO Y GESTIÓN DEL EMPLEO | 140.201.230 | 6,0 % |
| `423A` | PROMOCIÓN EDUCATIVA | 52.855.480 | 2,2 % |
| `322C` | DIALOGO SOCIAL E INTERMEDIACIÓN LABORAL | 48.536.070 | 2,1 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN, CULTURA Y DEPORTE | 39.136.870 | 1,7 % |
| `322A` | PERSONAL AUTÓNOMO, TRABAJO Y ECONOMÍA SOCIAL | 30.990.620 | 1,3 % |
| `422F` | EDUCACIÓN PERMANENTE DE PERSONAS ADULTAS | 29.689.390 | 1,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, EMPRESAS Y EMPLEO | 15.267.260 | 0,6 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO E INNOVACIÓN EDUCATIVA | 13.353.880 | 0,6 % |
| `442E` | PROMOCIÓN Y EDUCACIÓN AMBIENTAL | 1.671.790 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.323,42 M€ (1.323.418.140 €) · 7 códigos · 10,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | POLÍTICA AGRARIA COMUNITARIA *(×2 filas)* | 921.026.830 | 69,6 % |
| `531A` | REGADÍOS Y EXPLOTACIONES AGRARIAS | 133.729.540 | 10,1 % |
| `716A` | INDUSTRIAS Y CALIDAD AGROALIMENTARIA | 96.394.120 | 7,3 % |
| `717A` | PROMOCIÓN Y DESARROLLO RURAL | 61.335.760 | 4,6 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES DE AGRICULTURA, AGUA Y DESARROLLO RURAL | 48.188.820 | 3,6 % |
| `713A` | PRODUCCIÓN VEGETAL | 33.584.140 | 2,5 % |
| `713B` | PRODUCCIÓN ANIMAL | 29.158.930 | 2,2 % |

</details>

<details open><summary><b><code>direccion</code> — 21,32 M€ (21.323.780 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA | 21.323.780 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 106,60 M€ (106.598.350 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN DE LA VIVIENDA | 89.197.620 | 83,7 % |
| `432A` | GESTIÓN DEL URBANISMO | 14.887.710 | 14,0 % |
| `432B` | PLANIFICACIÓN TERRITORIAL | 2.513.020 | 2,4 % |

</details>

<details open><summary><b><code>empleo</code> — 82,84 M€ (82.841.930 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL PARA EL EMPLEO | 53.969.110 | 65,1 % |
| `324B` | PROGRAMAS MIXTOS DE FORMACIÓN Y EMPLEO | 28.872.820 | 34,9 % |

</details>

<details open><summary><b><code>idi</code> — 39,52 M€ (39.521.180 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | INVESTIGACIÓN, INNOVACIÓN Y DESARROLLO TECNOLÓGICO *(×3 filas)* | 24.974.730 | 63,2 % |
| `541H` | INVESTIGACIÓN AGROALIMENTARIA Y FORESTAL | 7.536.150 | 19,1 % |
| `541F` | FOMENTO DE LA INNOVACIÓN TECNOLÓGICA | 4.950.000 | 12,5 % |
| `541C` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 2.060.300 | 5,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 539,40 M€ (539.400.320 €) · 3 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | ATENCIÓN A LAS PERSONAS MAYORES | 369.095.370 | 68,4 % |
| `313H` | ATENCIÓN A LA DEPENDENCIA | 161.516.750 | 29,9 % |
| `313B` | PREVENCIÓN Y APOYO A LAS FAMILIAS | 8.788.200 | 1,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 137,28 M€ (137.281.350 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | ATENCIÓN A LAS PERSONAS CON DISCAPACIDAD | 137.281.350 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 141,66 M€ (141.662.370 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PROGRAMAS SOCIALES BÁSICOS | 90.346.760 | 63,8 % |
| `313E` | ATENCIÓN Y ACOMPAÑAMIENTO AL MENOR | 51.315.610 | 36,2 % |

</details>

<details open><summary><b><code>turismo</code> — 104,30 M€ (104.299.320 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 94.374.360 | 90,5 % |
| `751B` | PROMOCIÓN EXTERIOR | 4.348.960 | 4,2 % |
| `751D` | ORDENACIÓN Y PROMOCIÓN DE LA ARTESANÍA | 3.656.000 | 3,5 % |
| `751E` | ORDENACIÓN Y PROMOCIÓN DEL COMERCIO | 1.920.000 | 1,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 46,37 M€ (46.371.280 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA IGUALDAD DE GÉNERO | 46.371.280 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.666,12 M€ · 48 códigos · 29,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | DEUDA PÚBLICA | 2.478.767.000 |
| `521B` | DESARROLLO DE LA SOCIEDAD DE LA INFORMACIÓN *(×6 filas)* | 210.117.730 |
| `442B` | ORDENACIÓN Y CONSERVACIÓN DEL MEDIO NATURAL | 173.553.390 |
| `512A` | CREACIÓN DE INFRAESTRUCTURA HIDRÁULICA *(×2 filas)* | 111.442.890 |
| `513A` | CREACIÓN DE INFRAESTRUCTURAS DE CARRETERAS | 64.677.660 |
| `513B` | CONSERVACIÓN Y EXPLOTACIÓN DE CARRETERAS | 60.390.590 |
| `126C` | MEDIOS DE COMUNICACIÓN *(×2 filas)* | 59.950.460 |
| `513C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 52.848.440 |
| `722A` | POLÍTICA INDUSTRIAL Y ENERGÉTICA | 46.175.480 |
| `612D` | ADMINISTRACIÓN DEL PATRIMONIO | 43.112.650 |
| `724A` | COMPETITIVIDAD EMPRESARIAL | 36.524.180 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 27.147.200 |
| `442D` | CALIDAD AMBIENTAL | 26.249.760 |
| `521A` | TELECOMUNICACIONES | 23.159.810 |
| `442F` | ECONOMÍA CIRCULAR Y CAMBIO CLIMÁTICO | 22.618.210 |
| `442C` | GESTIÓN Y PROTECCIÓN DE ESPACIOS NATURALES | 20.590.980 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA Y ADMINISTRACIONES PÚBLICAS | 19.126.540 |
| `458A` | PATRIMONIO ARTÍSTICO Y MUSEOS | 18.194.060 |
| `457A` | INFRAESTRUCTURA, FOMENTO Y APOYO AL DEPORTE | 16.492.430 |
| `613A` | GESTIÓN TRIBUTARIA | 16.024.880 |
| `452A` | LIBROS, ARCHIVOS Y BIBLIOTECAS | 15.945.980 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES DE FOMENTO | 15.779.990 |
| `442A` | DIRECCIÓN Y SERVICIOS GENERALES DE DESARROLLO SOSTENIBLE | 13.983.040 |
| `455A` | GESTIÓN CULTURAL | 13.548.920 |
| `111A` | ACTIVIDAD LEGISLATIVA | 11.535.000 |
| … | *resto: 23 códigos* | 68.159.750 |

</details>

### 2023

*Fuente: `tomo_I.pdf` · 114 líneas · total extraído **12.418,77 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.700,36 M€ (3.700.358.300 €) · 12 códigos · 29,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | ATENCIÓN INTEGRADA DE LA SALUD | 3.392.201.900 | 91,7 % |
| `412C` | SELECCIÓN Y FORMACIÓN DEL PERSONAL SANITARIO | 85.390.320 | 2,3 % |
| `312A` | PENSIONES Y PRESTACIONES ASISTENCIALES | 49.422.880 | 1,3 % |
| `413A` | EPIDEMIOLOGÍA Y PROMOCIÓN DE LA SALUD | 44.102.460 | 1,2 % |
| `413B` | SANIDAD AMBIENTAL E HIGIENE DE LOS ALIMENTOS | 32.358.830 | 0,9 % |
| `411B` | GESTIÓN Y ADMINISTRACIÓN SANITARIA | 25.375.630 | 0,7 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES DE BIENESTAR SOCIAL | 24.416.570 | 0,7 % |
| `413D` | HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 23.241.950 | 0,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 12.369.100 | 0,3 % |
| `541E` | INVESTIGACIÓN SANITARIA | 6.119.010 | 0,2 % |
| `413C` | INSPECCIÓN SANITARIA | 4.266.520 | 0,1 % |
| `412E` | PLANIFICACIÓN, ATENCIÓN A LA SALUD E INSTITUCIONES SANITARIAS | 1.093.130 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.424,97 M€ (2.424.973.030 €) · 13 códigos · 19,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | EDUCACIÓN SECUNDARIA, FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE RÉGIMENESPECIAL | 888.047.540 | 36,6 % |
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 766.609.970 | 31,6 % |
| `422C` | ENSEÑANZA UNIVERSITARIA | 219.462.470 | 9,1 % |
| `422D` | ATENCIÓN A LA DIVERSIDAD | 181.724.260 | 7,5 % |
| `322B` | FOMENTO Y GESTIÓN DEL EMPLEO | 127.123.550 | 5,2 % |
| `423A` | PROMOCIÓN EDUCATIVA | 55.896.590 | 2,3 % |
| `322C` | DIALOGO SOCIAL E INTERMEDIACIÓN LABORAL | 46.870.820 | 1,9 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN, CULTURA Y DEPORTE | 43.040.500 | 1,8 % |
| `322A` | PERSONAL AUTÓNOMO, TRABAJO Y ECONOMÍA SOCIAL | 35.272.410 | 1,5 % |
| `422F` | EDUCACIÓN PERMANENTE DE PERSONAS ADULTAS | 30.740.660 | 1,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, EMPRESAS Y EMPLEO | 14.523.290 | 0,6 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO E INNOVACIÓN EDUCATIVA | 13.789.050 | 0,6 % |
| `442E` | PROMOCIÓN Y EDUCACIÓN AMBIENTAL | 1.871.920 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.328,09 M€ (1.328.093.030 €) · 7 códigos · 10,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | POLÍTICA AGRARIA COMUNITARIA *(×2 filas)* | 944.038.320 | 71,1 % |
| `531A` | REGADÍOS Y EXPLOTACIONES AGRARIAS | 139.915.970 | 10,5 % |
| `716A` | INDUSTRIAS Y CALIDAD AGROALIMENTARIA | 93.210.630 | 7,0 % |
| `717A` | PROMOCIÓN Y DESARROLLO RURAL | 57.674.800 | 4,3 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES DE AGRICULTURA, AGUA Y DESARROLLO RURAL | 47.364.420 | 3,6 % |
| `713B` | PRODUCCIÓN ANIMAL | 29.315.690 | 2,2 % |
| `713A` | PRODUCCIÓN VEGETAL | 16.573.200 | 1,2 % |

</details>

<details open><summary><b><code>direccion</code> — 21,09 M€ (21.088.800 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA | 21.088.800 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 223,49 M€ (223.490.620 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN DE LA VIVIENDA | 200.065.980 | 89,5 % |
| `432A` | GESTIÓN DEL URBANISMO | 12.006.100 | 5,4 % |
| `432B` | PLANIFICACIÓN TERRITORIAL | 11.418.540 | 5,1 % |

</details>

<details open><summary><b><code>empleo</code> — 117,38 M€ (117.383.250 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL PARA EL EMPLEO | 75.921.480 | 64,7 % |
| `324B` | PROGRAMAS MIXTOS DE FORMACIÓN Y EMPLEO | 41.461.770 | 35,3 % |

</details>

<details open><summary><b><code>idi</code> — 42,62 M€ (42.620.650 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | INVESTIGACIÓN, INNOVACIÓN Y DESARROLLO TECNOLÓGICO *(×3 filas)* | 25.166.740 | 59,0 % |
| `541H` | INVESTIGACIÓN AGROALIMENTARIA Y FORESTAL | 10.067.470 | 23,6 % |
| `541F` | FOMENTO DE LA INNOVACIÓN TECNOLÓGICA | 4.950.000 | 11,6 % |
| `541C` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 2.436.440 | 5,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 534,66 M€ (534.656.150 €) · 3 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | ATENCIÓN A LAS PERSONAS MAYORES | 367.927.260 | 68,8 % |
| `313H` | ATENCIÓN A LA DEPENDENCIA | 157.502.650 | 29,5 % |
| `313B` | PREVENCIÓN Y APOYO A LAS FAMILIAS | 9.226.240 | 1,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 150,71 M€ (150.707.730 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | ATENCIÓN A LAS PERSONAS CON DISCAPACIDAD | 150.707.730 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 154,45 M€ (154.450.780 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PROGRAMAS SOCIALES BÁSICOS | 97.248.070 | 63,0 % |
| `313E` | ATENCIÓN Y ACOMPAÑAMIENTO AL MENOR | 57.202.710 | 37,0 % |

</details>

<details open><summary><b><code>turismo</code> — 109,42 M€ (109.416.570 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 94.826.900 | 86,7 % |
| `751E` | ORDENACIÓN Y PROMOCIÓN DEL COMERCIO | 6.430.000 | 5,9 % |
| `751B` | PROMOCIÓN EXTERIOR | 4.503.660 | 4,1 % |
| `751D` | ORDENACIÓN Y PROMOCIÓN DE LA ARTESANÍA | 3.656.010 | 3,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 47,09 M€ (47.094.720 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA IGUALDAD DE GÉNERO | 47.094.720 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.564,44 M€ · 50 códigos · 28,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | DEUDA PÚBLICA | 2.325.908.600 |
| `521B` | DESARROLLO DE LA SOCIEDAD DE LA INFORMACIÓN *(×7 filas)* | 210.456.670 |
| `442B` | ORDENACIÓN Y CONSERVACIÓN DEL MEDIO NATURAL | 153.160.760 |
| `512A` | CREACIÓN DE INFRAESTRUCTURA HIDRÁULICA *(×2 filas)* | 119.928.190 |
| `513C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 74.440.730 |
| `513A` | CREACIÓN DE INFRAESTRUCTURAS DE CARRETERAS | 69.767.500 |
| `126C` | MEDIOS DE COMUNICACIÓN *(×2 filas)* | 62.767.470 |
| `722A` | POLÍTICA INDUSTRIAL Y ENERGÉTICA | 61.256.460 |
| `513B` | CONSERVACIÓN Y EXPLOTACIÓN DE CARRETERAS | 52.984.810 |
| `724A` | COMPETITIVIDAD EMPRESARIAL | 38.972.420 |
| `442F` | ECONOMÍA CIRCULAR Y CAMBIO CLIMÁTICO | 31.785.210 |
| `442C` | GESTIÓN Y PROTECCIÓN DE ESPACIOS NATURALES | 30.258.140 |
| `612D` | ADMINISTRACIÓN DEL PATRIMONIO | 28.224.370 |
| `442D` | CALIDAD AMBIENTAL | 27.784.570 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA Y ADMINISTRACIONES PÚBLICAS | 25.812.960 |
| `521A` | TELECOMUNICACIONES | 24.564.460 |
| `458A` | PATRIMONIO ARTÍSTICO Y MUSEOS | 19.511.220 |
| `457A` | INFRAESTRUCTURA, FOMENTO Y APOYO AL DEPORTE | 17.981.930 |
| `442A` | DIRECCIÓN Y SERVICIOS GENERALES DE DESARROLLO SOSTENIBLE | 16.598.680 |
| `452A` | LIBROS, ARCHIVOS Y BIBLIOTECAS | 16.391.210 |
| `613A` | GESTIÓN TRIBUTARIA | 16.135.770 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES DE FOMENTO | 14.820.550 |
| `221A` | PROTECCIÓN CIUDADANA | 14.294.150 |
| `455A` | GESTIÓN CULTURAL | 14.097.440 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 11.854.950 |
| … | *resto: 25 códigos* | 84.679.780 |

</details>

### 2024

*Fuente: `tomo_I.pdf` · 114 líneas · total extraído **12.473,34 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.934,18 M€ (3.934.175.090 €) · 13 códigos · 31,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | ATENCIÓN INTEGRADA DE LA SALUD | 3.601.572.230 | 91,5 % |
| `412C` | SELECCIÓN Y FORMACIÓN DEL PERSONAL SANITARIO | 95.490.650 | 2,4 % |
| `413A` | EPIDEMIOLOGÍA Y PROMOCIÓN DE LA SALUD | 51.660.550 | 1,3 % |
| `312A` | PENSIONES Y PRESTACIONES ASISTENCIALES | 45.282.090 | 1,2 % |
| `413B` | SANIDAD AMBIENTAL E HIGIENE DE LOS ALIMENTOS | 34.629.170 | 0,9 % |
| `411B` | GESTIÓN Y ADMINISTRACIÓN SANITARIA | 28.246.170 | 0,7 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES DE BIENESTAR SOCIAL | 24.601.470 | 0,6 % |
| `413D` | HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 24.137.080 | 0,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 12.112.710 | 0,3 % |
| `541E` | INVESTIGACIÓN SANITARIA | 6.574.210 | 0,2 % |
| `413C` | INSPECCIÓN SANITARIA | 4.691.750 | 0,1 % |
| `315A` | SEGURIDAD Y SALUD LABORAL | 4.007.720 | 0,1 % |
| `412E` | PLANIFICACIÓN, ATENCIÓN A LA SALUD E INSTITUCIONES SANITARIAS | 1.169.290 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.473,72 M€ (2.473.722.660 €) · 13 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | EDUCACIÓN SECUNDARIA, FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE RÉGIMENESPECIAL | 917.297.540 | 37,1 % |
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 777.772.010 | 31,4 % |
| `422C` | ENSEÑANZA UNIVERSITARIA | 238.098.700 | 9,6 % |
| `422D` | ATENCIÓN A LA DIVERSIDAD | 191.137.170 | 7,7 % |
| `322B` | FOMENTO Y GESTIÓN DEL EMPLEO | 112.963.440 | 4,6 % |
| `423A` | PROMOCIÓN EDUCATIVA | 53.027.450 | 2,1 % |
| `322C` | DIALOGO SOCIAL E INTERMEDIACIÓN LABORAL | 45.574.620 | 1,8 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN, CULTURA Y DEPORTE | 45.362.060 | 1,8 % |
| `422F` | EDUCACIÓN PERMANENTE DE PERSONAS ADULTAS | 34.396.450 | 1,4 % |
| `322A` | PERSONAL AUTÓNOMO, TRABAJO Y ECONOMÍA SOCIAL | 32.786.810 | 1,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, EMPRESAS Y EMPLEO | 15.986.210 | 0,6 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO E INNOVACIÓN EDUCATIVA | 7.383.120 | 0,3 % |
| `442E` | PROMOCIÓN Y EDUCACIÓN AMBIENTAL | 1.937.080 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.368,50 M€ (1.368.495.640 €) · 7 códigos · 11,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | POLÍTICA AGRARIA COMUNITARIA | 967.064.250 | 70,7 % |
| `531A` | REGADÍOS Y EXPLOTACIONES AGRARIAS | 162.513.330 | 11,9 % |
| `716A` | INDUSTRIAS Y CALIDAD AGROALIMENTARIA | 86.552.430 | 6,3 % |
| `717A` | PROMOCIÓN Y DESARROLLO RURAL | 50.034.320 | 3,7 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES DE AGRICULTURA, GANADERÍA Y DESARROLLORURAL | 48.693.820 | 3,6 % |
| `713B` | PRODUCCIÓN ANIMAL | 37.906.670 | 2,8 % |
| `713A` | PRODUCCIÓN VEGETAL | 15.730.820 | 1,1 % |

</details>

<details open><summary><b><code>direccion</code> — 18,37 M€ (18.372.490 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA | 18.372.490 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 232,40 M€ (232.403.540 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN DE LA VIVIENDA | 215.031.370 | 92,5 % |
| `432A` | GESTIÓN DEL URBANISMO | 8.980.660 | 3,9 % |
| `432B` | PLANIFICACIÓN TERRITORIAL | 8.391.510 | 3,6 % |

</details>

<details open><summary><b><code>empleo</code> — 121,45 M€ (121.452.570 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL EN EL ÁMBITO LABORAL | 78.667.630 | 64,8 % |
| `324B` | PROGRAMAS MIXTOS DE FORMACIÓN Y EMPLEO | 42.784.940 | 35,2 % |

</details>

<details open><summary><b><code>idi</code> — 38,67 M€ (38.668.490 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | INVESTIGACIÓN, INNOVACIÓN Y DESARROLLO TECNOLÓGICO *(×3 filas)* | 22.692.050 | 58,7 % |
| `541H` | INVESTIGACIÓN AGROALIMENTARIA Y FORESTAL | 8.433.500 | 21,8 % |
| `541F` | FOMENTO DE LA INNOVACIÓN TECNOLÓGICA | 4.950.000 | 12,8 % |
| `541C` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 2.592.940 | 6,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 534,59 M€ (534.594.760 €) · 3 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | ATENCIÓN A LAS PERSONAS MAYORES | 368.471.530 | 68,9 % |
| `313H` | ATENCIÓN A LA DEPENDENCIA | 156.853.360 | 29,3 % |
| `313B` | PREVENCIÓN Y APOYO A LAS FAMILIAS | 9.269.870 | 1,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 158,26 M€ (158.259.930 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | ATENCIÓN A LAS PERSONAS CON DISCAPACIDAD | 158.259.930 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 157,48 M€ (157.475.920 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PROGRAMAS SOCIALES BÁSICOS | 98.084.970 | 62,3 % |
| `313E` | ATENCIÓN Y ACOMPAÑAMIENTO AL MENOR | 59.390.950 | 37,7 % |

</details>

<details open><summary><b><code>turismo</code> — 122,27 M€ (122.274.720 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 107.740.990 | 88,1 % |
| `751E` | ORDENACIÓN Y PROMOCIÓN DEL COMERCIO | 6.430.000 | 5,3 % |
| `751B` | PROMOCIÓN EXTERIOR | 4.547.730 | 3,7 % |
| `751D` | ORDENACIÓN Y PROMOCIÓN DE LA ARTESANÍA | 3.556.000 | 2,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 50,06 M€ (50.062.700 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA IGUALDAD DE GÉNERO *(×2 filas)* | 50.062.700 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.263,38 M€ · 49 códigos · 26,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | DEUDA PÚBLICA | 1.902.740.000 |
| `521B` | DESARROLLO DE LA SOCIEDAD DE LA INFORMACIÓN *(×7 filas)* | 237.918.480 |
| `442B` | ORDENACIÓN Y CONSERVACIÓN DEL MEDIO NATURAL | 187.189.260 |
| `722A` | POLÍTICA INDUSTRIAL Y ENERGÉTICA | 169.771.750 |
| `512A` | CREACIÓN DE INFRAESTRUCTURA HIDRÁULICA *(×2 filas)* | 119.932.310 |
| `513C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 76.830.320 |
| `126C` | MEDIOS DE COMUNICACIÓN *(×2 filas)* | 64.806.880 |
| `513A` | CREACIÓN DE INFRAESTRUCTURAS DE CARRETERAS | 60.706.050 |
| `513B` | CONSERVACIÓN Y EXPLOTACIÓN DE CARRETERAS | 51.544.960 |
| `724A` | COMPETITIVIDAD EMPRESARIAL | 39.363.830 |
| `612D` | ADMINISTRACIÓN DEL PATRIMONIO | 32.745.160 |
| `442C` | GESTIÓN Y PROTECCIÓN DE ESPACIOS NATURALES | 31.648.170 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA, ADMINISTRACIONES PÚBLICAS | 25.027.390 |
| `458A` | PATRIMONIO ARTÍSTICO Y MUSEOS | 24.507.870 |
| `521A` | TELECOMUNICACIONES | 22.053.620 |
| `442F` | ECONOMÍA CIRCULAR Y CAMBIO CLIMÁTICO | 19.931.840 |
| `452A` | LIBROS, ARCHIVOS Y BIBLIOTECAS | 15.782.350 |
| `442A` | DIRECCIÓN Y SERVICIOS GENERALES DE DESARROLLO SOSTENIBLE | 15.262.860 |
| `613A` | GESTIÓN TRIBUTARIA | 14.807.620 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES DE FOMENTO | 14.561.130 |
| `221A` | PROTECCIÓN CIUDADANA | 14.427.730 |
| `111A` | ACTIVIDAD LEGISLATIVA | 13.210.000 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 12.494.670 |
| `457A` | INFRAESTRUCTURA, FOMENTO Y APOYO AL DEPORTE | 11.554.320 |
| `455A` | GESTIÓN CULTURAL | 10.419.200 |
| … | *resto: 24 códigos* | 74.146.480 |

</details>

### 2025

*Fuente: `tomo_I.pdf` · 113 líneas · total extraído **12.716,18 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.860,44 M€ (3.860.441.540 €) · 13 códigos · 30,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | ATENCIÓN INTEGRADA DE LA SALUD | 3.515.500.790 | 91,1 % |
| `412C` | SELECCIÓN Y FORMACIÓN DEL PERSONAL SANITARIO | 100.507.650 | 2,6 % |
| `413A` | EPIDEMIOLOGÍA Y PROMOCIÓN DE LA SALUD | 49.901.910 | 1,3 % |
| `312A` | PENSIONES Y PRESTACIONES ASISTENCIALES | 45.734.160 | 1,2 % |
| `413B` | SANIDAD AMBIENTAL E HIGIENE DE LOS ALIMENTOS | 35.808.480 | 0,9 % |
| `411B` | GESTIÓN Y ADMINISTRACIÓN SANITARIA | 28.731.350 | 0,7 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES DE BIENESTAR SOCIAL | 26.278.400 | 0,7 % |
| `413D` | HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 24.396.990 | 0,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 13.198.600 | 0,3 % |
| `315A` | SEGURIDAD Y SALUD LABORAL | 8.275.860 | 0,2 % |
| `541E` | INVESTIGACIÓN SANITARIA | 6.595.730 | 0,2 % |
| `413C` | INSPECCIÓN SANITARIA | 4.564.110 | 0,1 % |
| `412E` | PLANIFICACIÓN, ATENCIÓN A LA SALUD E INSTITUCIONES SANITARIAS | 947.510 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.530,78 M€ (2.530.782.640 €) · 13 códigos · 19,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | EDUCACIÓN SECUNDARIA, FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE RÉGIMENESPECIAL | 963.488.410 | 38,1 % |
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 786.677.850 | 31,1 % |
| `422C` | ENSEÑANZA UNIVERSITARIA | 246.011.580 | 9,7 % |
| `422D` | ATENCIÓN A LA DIVERSIDAD | 195.703.670 | 7,7 % |
| `322B` | FOMENTO Y GESTIÓN DEL EMPLEO | 106.642.300 | 4,2 % |
| `423A` | PROMOCIÓN EDUCATIVA | 53.450.450 | 2,1 % |
| `322C` | DIALOGO SOCIAL E INTERMEDIACIÓN LABORAL | 42.973.630 | 1,7 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN, CULTURA Y DEPORTE | 41.390.780 | 1,6 % |
| `322A` | PERSONAL AUTÓNOMO, TRABAJO Y ECONOMÍA SOCIAL | 37.447.970 | 1,5 % |
| `422F` | EDUCACIÓN PERMANENTE DE PERSONAS ADULTAS | 35.310.100 | 1,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, EMPRESAS Y EMPLEO | 16.559.670 | 0,7 % |
| `442E` | PROMOCIÓN Y EDUCACIÓN AMBIENTAL | 2.870.050 | 0,1 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO E INNOVACIÓN EDUCATIVA | 2.256.180 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.332,42 M€ (1.332.420.740 €) · 7 códigos · 10,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | POLÍTICA AGRARIA COMUNITARIA | 912.250.210 | 68,5 % |
| `531A` | REGADÍOS Y EXPLOTACIONES AGRARIAS | 172.605.910 | 13,0 % |
| `716A` | INDUSTRIAS Y CALIDAD AGROALIMENTARIA | 98.532.080 | 7,4 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES DE AGRICULTURA, GANADERÍA Y DESARROLLORURAL | 50.537.460 | 3,8 % |
| `717A` | PROMOCIÓN Y DESARROLLO RURAL | 43.198.040 | 3,2 % |
| `713B` | PRODUCCIÓN ANIMAL | 36.825.240 | 2,8 % |
| `713A` | PRODUCCIÓN VEGETAL | 18.471.800 | 1,4 % |

</details>

<details open><summary><b><code>direccion</code> — 19,41 M€ (19.411.360 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA | 19.411.360 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 218,23 M€ (218.226.660 €) · 3 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN DE LA VIVIENDA | 200.287.420 | 91,8 % |
| `432A` | GESTIÓN DEL URBANISMO | 9.654.220 | 4,4 % |
| `432B` | PLANIFICACIÓN TERRITORIAL | 8.285.020 | 3,8 % |

</details>

<details open><summary><b><code>empleo</code> — 124,34 M€ (124.336.360 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL EN EL ÁMBITO LABORAL | 82.710.230 | 66,5 % |
| `324B` | PROGRAMAS MIXTOS DE FORMACIÓN Y EMPLEO | 41.626.130 | 33,5 % |

</details>

<details open><summary><b><code>idi</code> — 44,93 M€ (44.929.700 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | INVESTIGACIÓN, INNOVACIÓN Y DESARROLLO TECNOLÓGICO *(×3 filas)* | 23.433.590 | 52,2 % |
| `541H` | INVESTIGACIÓN AGROALIMENTARIA Y FORESTAL | 8.933.070 | 19,9 % |
| `541C` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 7.613.040 | 16,9 % |
| `541F` | FOMENTO DE LA INNOVACIÓN TECNOLÓGICA | 4.950.000 | 11,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 521,49 M€ (521.492.210 €) · 3 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | ATENCIÓN A LAS PERSONAS MAYORES | 363.130.580 | 69,6 % |
| `313H` | ATENCIÓN A LA DEPENDENCIA | 149.561.830 | 28,7 % |
| `313B` | PREVENCIÓN Y APOYO A LAS FAMILIAS | 8.799.800 | 1,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 156,85 M€ (156.848.960 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | ATENCIÓN A LAS PERSONAS CON DISCAPACIDAD | 156.848.960 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 154,20 M€ (154.203.960 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PROGRAMAS SOCIALES BÁSICOS | 96.773.250 | 62,8 % |
| `313E` | ATENCIÓN Y ACOMPAÑAMIENTO AL MENOR | 57.430.710 | 37,2 % |

</details>

<details open><summary><b><code>turismo</code> — 108,19 M€ (108.190.760 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 95.339.020 | 88,1 % |
| `751D` | ORDENACIÓN Y PROMOCIÓN DE LA ARTESANÍA | 6.298.020 | 5,8 % |
| `751B` | PROMOCIÓN EXTERIOR | 4.633.720 | 4,3 % |
| `751E` | ORDENACIÓN Y PROMOCIÓN DEL COMERCIO | 1.920.000 | 1,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 46,92 M€ (46.924.570 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA IGUALDAD DE GÉNERO *(×2 filas)* | 46.924.570 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.597,97 M€ · 49 códigos · 28,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | DEUDA PÚBLICA | 2.238.260.000 |
| `442B` | ORDENACIÓN Y CONSERVACIÓN DEL MEDIO NATURAL | 219.510.460 |
| `521B` | DESARROLLO DE LA SOCIEDAD DE LA INFORMACIÓN *(×6 filas)* | 197.016.180 |
| `722A` | POLÍTICA INDUSTRIAL Y ENERGÉTICA | 159.958.380 |
| `512A` | CREACIÓN DE INFRAESTRUCTURA HIDRÁULICA *(×2 filas)* | 103.951.090 |
| `513C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 71.985.170 |
| `126C` | MEDIOS DE COMUNICACIÓN *(×2 filas)* | 68.683.510 |
| `513A` | CREACIÓN DE INFRAESTRUCTURAS DE CARRETERAS | 66.365.040 |
| `513B` | CONSERVACIÓN Y EXPLOTACIÓN DE CARRETERAS | 61.340.180 |
| `724A` | COMPETITIVIDAD EMPRESARIAL | 50.749.580 |
| `442C` | GESTIÓN Y PROTECCIÓN DE ESPACIOS NATURALES | 32.704.120 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 31.794.820 |
| `612D` | ADMINISTRACIÓN DEL PATRIMONIO | 26.055.860 |
| `458A` | PATRIMONIO ARTÍSTICO Y MUSEOS | 25.202.930 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA, ADMINISTRACIONES PÚBLICAS | 21.589.420 |
| `442F` | ECONOMÍA CIRCULAR Y CAMBIO CLIMÁTICO | 21.090.920 |
| `613A` | GESTIÓN TRIBUTARIA | 16.955.680 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES DE FOMENTO | 16.656.330 |
| `452A` | LIBROS, ARCHIVOS Y BIBLIOTECAS | 15.937.880 |
| `442A` | DIRECCIÓN Y SERVICIOS GENERALES DE DESARROLLO SOSTENIBLE | 15.907.350 |
| `221A` | PROTECCIÓN CIUDADANA | 15.210.450 |
| `111A` | ACTIVIDAD LEGISLATIVA | 13.465.000 |
| `457A` | INFRAESTRUCTURA, FOMENTO Y APOYO AL DEPORTE | 11.915.460 |
| `455A` | GESTIÓN CULTURAL | 11.630.520 |
| `612F` | CONTRATACIÓN CENTRALIZADA | 11.245.970 |
| … | *resto: 24 códigos* | 72.788.270 |

</details>

### 2026

*Fuente: `tomo_I.pdf` · 113 líneas · total extraído **12.903,39 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.152,86 M€ (4.152.856.370 €) · 13 códigos · 32,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412D` | ATENCIÓN INTEGRADA DE LA SALUD | 3.783.900.960 | 91,1 % |
| `412C` | SELECCIÓN Y FORMACIÓN DEL PERSONAL SANITARIO | 109.042.620 | 2,6 % |
| `413A` | EPIDEMIOLOGÍA Y PROMOCIÓN DE LA SALUD | 50.889.390 | 1,2 % |
| `312A` | PENSIONES Y PRESTACIONES ASISTENCIALES | 50.575.240 | 1,2 % |
| `413B` | SANIDAD AMBIENTAL E HIGIENE DE LOS ALIMENTOS | 36.362.640 | 0,9 % |
| `411B` | GESTIÓN Y ADMINISTRACIÓN SANITARIA | 29.705.170 | 0,7 % |
| `413D` | HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 26.967.500 | 0,6 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES DE BIENESTAR SOCIAL | 26.690.010 | 0,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 15.025.140 | 0,4 % |
| `315A` | SEGURIDAD Y SALUD LABORAL | 10.338.090 | 0,2 % |
| `541E` | INVESTIGACIÓN SANITARIA | 7.197.770 | 0,2 % |
| `413C` | INSPECCIÓN SANITARIA | 4.951.570 | 0,1 % |
| `412E` | PLANIFICACIÓN, ATENCIÓN A LA SALUD E INSTITUCIONES SANITARIAS | 1.210.270 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.633,02 M€ (2.633.020.170 €) · 13 códigos · 20,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422B` | EDUCACIÓN SECUNDARIA, FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE RÉGIMENESPECIAL | 994.415.530 | 37,8 % |
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 816.167.760 | 31,0 % |
| `422C` | ENSEÑANZA UNIVERSITARIA | 263.333.910 | 10,0 % |
| `422D` | ATENCIÓN A LA DIVERSIDAD | 203.897.920 | 7,7 % |
| `322B` | FOMENTO Y GESTIÓN DEL EMPLEO | 107.894.470 | 4,1 % |
| `423A` | PROMOCIÓN EDUCATIVA | 58.074.080 | 2,2 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN, CULTURA Y DEPORTE | 46.049.860 | 1,7 % |
| `322C` | DIALOGO SOCIAL E INTERMEDIACIÓN LABORAL | 44.937.670 | 1,7 % |
| `322A` | PERSONAL AUTÓNOMO, TRABAJO Y ECONOMÍA SOCIAL | 39.329.530 | 1,5 % |
| `422F` | EDUCACIÓN PERMANENTE DE PERSONAS ADULTAS | 36.069.990 | 1,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, EMPRESAS Y EMPLEO | 17.544.740 | 0,7 % |
| `442E` | PROMOCIÓN Y EDUCACIÓN AMBIENTAL | 2.969.210 | 0,1 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO E INNOVACIÓN EDUCATIVA | 2.335.500 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.334,98 M€ (1.334.980.130 €) · 7 códigos · 10,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `718A` | POLÍTICA AGRARIA COMUNITARIA | 916.225.620 | 68,6 % |
| `531A` | REGADÍOS Y EXPLOTACIONES AGRARIAS | 198.692.640 | 14,9 % |
| `716A` | INDUSTRIAS Y CALIDAD AGROALIMENTARIA | 74.845.070 | 5,6 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES DE AGRICULTURA, GANADERÍA Y DESARROLLORURAL | 50.739.440 | 3,8 % |
| `713B` | PRODUCCIÓN ANIMAL | 38.718.480 | 2,9 % |
| `717A` | PROMOCIÓN Y DESARROLLO RURAL | 34.568.010 | 2,6 % |
| `713A` | PRODUCCIÓN VEGETAL | 21.190.870 | 1,6 % |

</details>

<details open><summary><b><code>direccion</code> — 21,05 M€ (21.047.560 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA | 21.047.560 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 270,55 M€ (270.553.240 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN DE LA VIVIENDA | 247.729.110 | 91,6 % |
| `432B` | PLANIFICACIÓN TERRITORIAL | 13.143.410 | 4,9 % |
| `432A` | GESTIÓN DEL URBANISMO | 9.680.720 | 3,6 % |

</details>

<details open><summary><b><code>empleo</code> — 121,71 M€ (121.712.450 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL EN EL ÁMBITO LABORAL | 89.501.010 | 73,5 % |
| `324B` | PROGRAMAS MIXTOS DE FORMACIÓN Y EMPLEO | 32.211.440 | 26,5 % |

</details>

<details open><summary><b><code>idi</code> — 50,87 M€ (50.872.500 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | INVESTIGACIÓN, INNOVACIÓN Y DESARROLLO TECNOLÓGICO *(×3 filas)* | 25.777.130 | 50,7 % |
| `541C` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 11.087.800 | 21,8 % |
| `541H` | INVESTIGACIÓN AGROALIMENTARIA Y FORESTAL | 9.057.570 | 17,8 % |
| `541F` | FOMENTO DE LA INNOVACIÓN TECNOLÓGICA | 4.950.000 | 9,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 545,79 M€ (545.785.820 €) · 3 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | ATENCIÓN A LAS PERSONAS MAYORES | 369.725.020 | 67,7 % |
| `313H` | ATENCIÓN A LA DEPENDENCIA | 166.757.440 | 30,6 % |
| `313B` | PREVENCIÓN Y APOYO A LAS FAMILIAS | 9.303.360 | 1,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 159,13 M€ (159.133.450 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | ATENCIÓN A LAS PERSONAS CON DISCAPACIDAD | 159.133.450 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 166,22 M€ (166.223.990 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PROGRAMAS SOCIALES BÁSICOS | 100.771.530 | 60,6 % |
| `313E` | ATENCIÓN Y ACOMPAÑAMIENTO AL MENOR | 65.452.460 | 39,4 % |

</details>

<details open><summary><b><code>turismo</code> — 89,97 M€ (89.966.570 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 77.689.580 | 86,4 % |
| `751B` | PROMOCIÓN EXTERIOR | 5.612.850 | 6,2 % |
| `751D` | ORDENACIÓN Y PROMOCIÓN DE LA ARTESANÍA | 3.944.140 | 4,4 % |
| `751E` | ORDENACIÓN Y PROMOCIÓN DEL COMERCIO | 2.720.000 | 3,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 48,13 M€ (48.128.970 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA IGUALDAD DE GÉNERO *(×2 filas)* | 48.128.970 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.309,11 M€ · 49 códigos · 25,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | DEUDA PÚBLICA | 1.816.444.700 |
| `442B` | ORDENACIÓN Y CONSERVACIÓN DEL MEDIO NATURAL | 219.818.130 |
| `722A` | POLÍTICA INDUSTRIAL Y ENERGÉTICA | 214.447.250 |
| `521B` | DESARROLLO DE LA SOCIEDAD DE LA INFORMACIÓN *(×6 filas)* | 201.364.610 |
| `512A` | CREACIÓN DE INFRAESTRUCTURA HIDRÁULICA *(×2 filas)* | 119.759.750 |
| `513A` | CREACIÓN DE INFRAESTRUCTURAS DE CARRETERAS | 71.943.360 |
| `126C` | MEDIOS DE COMUNICACIÓN *(×2 filas)* | 71.239.500 |
| `513B` | CONSERVACIÓN Y EXPLOTACIÓN DE CARRETERAS | 67.361.110 |
| `724A` | COMPETITIVIDAD EMPRESARIAL | 60.643.460 |
| `442F` | ECONOMÍA CIRCULAR Y CAMBIO CLIMÁTICO | 49.849.520 |
| `513C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 46.491.510 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 31.754.360 |
| `612D` | ADMINISTRACIÓN DEL PATRIMONIO | 29.235.730 |
| `442C` | GESTIÓN Y PROTECCIÓN DE ESPACIOS NATURALES | 27.053.580 |
| `221A` | PROTECCIÓN CIUDADANA | 26.542.310 |
| `458A` | PATRIMONIO ARTÍSTICO Y MUSEOS | 25.819.050 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA, ADMINISTRACIONES PÚBLICAS | 22.099.260 |
| `613A` | GESTIÓN TRIBUTARIA | 20.022.630 |
| `442A` | DIRECCIÓN Y SERVICIOS GENERALES DE DESARROLLO SOSTENIBLE | 18.180.040 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES DE FOMENTO | 17.251.540 |
| `452A` | LIBROS, ARCHIVOS Y BIBLIOTECAS | 16.604.080 |
| `111A` | ACTIVIDAD LEGISLATIVA | 13.934.770 |
| `612F` | CONTRATACIÓN CENTRALIZADA | 13.454.510 |
| `457A` | INFRAESTRUCTURA, FOMENTO Y APOYO AL DEPORTE | 12.508.360 |
| `455A` | GESTIÓN CULTURAL | 11.463.070 |
| … | *resto: 24 códigos* | 83.823.900 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py clm     # regenera este documento
python3 tools/auditoria_magnitud.py clm        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa clm --anio <año> \
    --input ../fuentes/raw/clm/<año>/<fichero> --output /tmp/clm.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-clm.md`](limitaciones-clm.md)

