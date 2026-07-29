# Trazabilidad de la extracción — Andalucía (`and`)

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
| **2015** | 100 | `gastos_csv.csv` | 12 | 43,0 % | 29.476,05 | — | no_aplica |
| **2016** | 101 | `gastos_csv.csv` | 12 | 40,6 % | 31.130,28 | — | no_aplica |
| **2017** | 110 | `memoria_programas.pdf` | 12 | 40,0 % | 33.066,10 | — | no_aplica |
| **2018** | 111 | `memoria_programas.pdf` | 12 | 39,6 % | 34.586,56 | — | no_aplica |
| **2019** | 112 | `memoria_programas.pdf` | 12 | 40,2 % | 34.685,07 | — | no_aplica |
| **2020** | 97 | `gastos_csv.csv` | 12 | 43,3 % | 38.277,95 | — | no_aplica |
| **2021** | 94 | `gastos_csv.csv` | 12 | 42,6 % | 39.750,62 | — | no_aplica |
| **2022** | 104 | `memoria_programas.pdf` | 12 | 40,4 % | 39.923,76 | — | prorroga |
| **2023** | 105 | `memoria_programas.pdf` | 12 | 35,2 % | 44.671,75 | — | no_aplica |
| **2024** | 105 | `memoria_programas.pdf` | 12 | 36,2 % | 45.740,39 | — | consolidado |
| **2025** | 107 | `memoria_programas.pdf` | 12 | 35,5 % | 48.384,98 | — | consolidado |
| **2026** | 107 | `memoria_programas.pdf` | 12 | 35,5 % | 51.120,36 | — | consolidado |

**URL(s) de origen:**
- <http://www.juntadeandalucia.es/export/drupaljda/cehap_presupuesto2018_tomo12.pdf>
- <https://www.juntadeandalucia.es/datosabiertos/portal/dataset/38ce8942-1834-4a25-a347-da4b536a8b9e/resource/02f5a4d2-f03c-4a19-b91b-a56d458eeced/download/gastos_2015.csv>
- <https://www.juntadeandalucia.es/datosabiertos/portal/dataset/e48d442c-2502-4a88-98fa-749a1fec01a9/resource/e407ce78-e63c-4160-87e4-ca6bdf4a619f/download/gastos.csv>
- <https://www.juntadeandalucia.es/datosabiertos/portal/dataset/edb22f68-f481-49e8-a8da-35cff3f98252/resource/21c37d7f-6aec-4fe8-838f-19e4a2f84990/download/gastos_2016.csv>
- <https://www.juntadeandalucia.es/datosabiertos/portal/dataset/f29ddd85-b4cf-4961-b2f6-30db9ee2933d/resource/8d4dcd66-1f5a-4361-9384-77d23931b525/download/gastos.csv>
- <https://www.juntadeandalucia.es/export/drupaljda/cehap_presupuesto2017_tomo12.pdf>
- <https://www.juntadeandalucia.es/export/drupaljda/cehap_presupuesto2019_tomo12.pdf>
- <https://www.juntadeandalucia.es/export/presup2023/estado/programas/tomo12-5b.pdf>
- <https://www.juntadeandalucia.es/export/presup2024/estado/programas/tomo12-5b.pdf>
- <https://www.juntadeandalucia.es/export/presup2025/estado/programas/tomo12-5b.pdf>
- <https://www.juntadeandalucia.es/export/presup2026/estado/programas/tomo12-5b.pdf>
- <https://www.juntadeandalucia.es/export/prorroga_presup2022/estado/programas/tomo12.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 8.388,30 | 8.657,78 | 9.129,97 | 9.627,55 | 9.613,26 | 10.765,89 | 11.453,59 | 12.214,50 | 13.644,94 | 14.055,56 | 15.041,54 | 15.950,81 |
| `educacion` | 6.587,40 | 6.808,22 | 7.019,19 | 7.329,75 | 7.296,32 | 7.887,89 | 8.500,80 | 8.744,58 | 8.808,59 | 9.319,09 | 9.693,33 | 9.998,48 |
| `soberania` | 2.320,44 | 2.304,64 | 2.090,30 | 2.125,29 | 2.228,42 | 2.577,05 | 2.824,01 | 2.822,72 | 2.459,66 | 2.596,56 | 2.628,58 | 2.480,51 |
| `vivienda` | 253,75 | 263,05 | 335,60 | 335,85 | 338,45 | 318,30 | 309,67 | 246,78 | 418,60 | 448,24 | 488,87 | 719,35 |
| `empleo` | 1.016,66 | 555,97 | 550,01 | 549,95 | 530,18 | 1.145,80 | 1.245,39 | 929,48 | 696,43 | 781,22 | 781,21 | 782,05 |
| `idi` | 554,56 | 651,52 | 683,77 | 734,50 | 862,87 | 705,86 | 433,67 | 278,32 | 359,53 | 362,24 | 443,42 | 471,73 |
| `dependencia` | 1.094,40 | 1.136,81 | 1.164,91 | 1.196,02 | 1.195,01 | 1.509,24 | 1.610,00 | 1.762,58 | 2.041,97 | 2.229,59 | 2.616,90 | 2.913,06 |
| `discapacidad` | 132,78 | 140,17 | 143,16 | 153,48 | 155,43 | 192,85 | 194,33 | 203,12 | 222,48 | 252,38 | 265,38 | 268,84 |
| `salud_mental` | 32,43 | 34,63 | 36,18 | 38,27 | 38,23 | 7,87 | 31,64 | 32,33 | 33,17 | 33,80 | 33,16 | 36,38 |
| `diversidad` | 2,59 | 2,76 | 3,26 | 4,92 | 4,97 | 5,50 | 4,02 | 3,74 | 10,58 | 10,62 | 10,87 | 10,71 |
| `turismo` | 100,52 | 101,69 | 116,20 | 118,72 | 120,31 | 136,12 | 138,38 | 158,42 | 198,63 | 177,17 | 146,52 | 160,83 |
| `igualdad` | 4,05 | 4,19 | 116,32 | 118,24 | 117,68 | 135,37 | 140,30 | 161,16 | 2,33 | 2,31 | 2,72 | 1,97 |
| **Σ asignado** | 20.487,88 | 20.661,43 | 21.388,86 | 22.332,54 | 22.501,12 | 25.387,75 | 26.885,82 | 27.557,73 | 28.896,91 | 30.268,78 | 32.152,50 | 33.794,72 |
| *(sin concepto)* | 8.988,17 | 10.468,84 | 11.677,24 | 12.254,01 | 12.183,95 | 12.890,20 | 12.864,81 | 12.366,03 | 15.774,84 | 15.471,61 | 16.232,49 | 17.325,64 |
| **TOTAL extraído** | 29.476,05 | 31.130,28 | 33.066,10 | 34.586,56 | 34.685,07 | 38.277,95 | 39.750,62 | 39.923,76 | 44.671,75 | 45.740,39 | 48.384,98 | 51.120,36 |

**Conceptos sin ninguna línea en toda la serie:** `direccion` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +3,2 % | +5,5 % | +5,4 % | −0,1 % | +12,0 % | +6,4 % | +6,6 % | +11,7 % | +3,0 % | +7,0 % | +6,0 % |
| `educacion` | +3,4 % | +3,1 % | +4,4 % | −0,5 % | +8,1 % | +7,8 % | +2,9 % | +0,7 % | +5,8 % | +4,0 % | +3,1 % |
| `soberania` | −0,7 % | −9,3 % | +1,7 % | +4,9 % | +15,6 % | +9,6 % | −0,0 % | −12,9 % | +5,6 % | +1,2 % | −5,6 % |
| `vivienda` | +3,7 % | +27,6 % | +0,1 % | +0,8 % | −6,0 % | −2,7 % | −20,3 % | +69,6 % ⚠ | +7,1 % | +9,1 % | +47,1 % ⚠ |
| `empleo` | −45,3 % ⚠ | −1,1 % | −0,0 % | −3,6 % | +116,1 % ⚠ | +8,7 % | −25,4 % | −25,1 % | +12,2 % | −0,0 % | +0,1 % |
| `idi` | +17,5 % | +5,0 % | +7,4 % | +17,5 % | −18,2 % | −38,6 % | −35,8 % | +29,2 % | +0,8 % | +22,4 % | +6,4 % |
| `dependencia` | +3,9 % | +2,5 % | +2,7 % | −0,1 % | +26,3 % | +6,7 % | +9,5 % | +15,9 % | +9,2 % | +17,4 % | +11,3 % |
| `discapacidad` | +5,6 % | +2,1 % | +7,2 % | +1,3 % | +24,1 % | +0,8 % | +4,5 % | +9,5 % | +13,4 % | +5,2 % | +1,3 % |
| `salud_mental` | +6,8 % | +4,5 % | +5,8 % | −0,1 % | −79,4 % ⚠ | +301,9 % ⚠ | +2,2 % | +2,6 % | +1,9 % | −1,9 % | +9,7 % |
| `diversidad` | +6,8 % | +17,8 % | +51,0 % ⚠ | +1,1 % | +10,6 % | −26,8 % | −7,0 % | +182,8 % ⚠ | +0,4 % | +2,3 % | −1,5 % |
| `turismo` | +1,2 % | +14,3 % | +2,2 % | +1,3 % | +13,1 % | +1,7 % | +14,5 % | +25,4 % | −10,8 % | −17,3 % | +9,8 % |
| `igualdad` | +3,6 % | +2,675,5 % ⚠ | +1,7 % | −0,5 % | +15,0 % | +3,6 % | +14,9 % | −98,6 % ⚠ | −0,8 % | +17,8 % | −27,6 % |
| **TOTAL** | +5,6 % | +6,2 % | +4,6 % | +0,3 % | +10,4 % | +3,8 % | +0,4 % | +11,9 % | +2,4 % | +5,8 % | +5,7 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `empleo` | **SALTO** | 1.016,66 → 555,97 M€ (−45,3 % ⚠) |
| 2020 | `empleo` | **SALTO** | 530,18 → 1.145,80 M€ (+116,1 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 246,78 → 418,60 M€ (+69,6 % ⚠) |
| 2026 | `vivienda` | **SALTO** | 488,87 → 719,35 M€ (+47,1 % ⚠) |

### 4.1 · Códigos duplicados dentro del mismo año (64 casos, 65.514,82 M€ acumulados)

> Un mismo código aparece en **varias filas del mismo ejercicio**. Puede ser legítimo
> (mismo programa en varias secciones/centros gestores) o **doble conteo** que infla el total.
> Compruébalo contra el documento original antes de dar el año por bueno.

| Año | Código | Concepto | Filas | Importe sumado (M€) |
|---|---|---|---:|---:|
| 2022 | `41H` | `sanidad` | 2 | 12.139,84 |
| 2026 | `81B` | `(sin concepto)` | 3 | 4.098,82 |
| 2025 | `81B` | `(sin concepto)` | 3 | 3.888,79 |
| 2022 | `81B` | `(sin concepto)` | 3 | 3.265,11 |
| 2024 | `81B` | `(sin concepto)` | 2 | 3.153,79 |
| 2019 | `81B` | `(sin concepto)` | 3 | 3.134,19 |
| 2017 | `81B` | `(sin concepto)` | 3 | 3.134,12 |
| 2018 | `81B` | `(sin concepto)` | 3 | 3.134,09 |
| 2023 | `81B` | `(sin concepto)` | 2 | 2.953,74 |
| 2026 | `12S` | `(sin concepto)` | 12 | 2.758,89 |
| 2023 | `12S` | `(sin concepto)` | 11 | 2.583,40 |
| 2025 | `12S` | `(sin concepto)` | 12 | 2.448,22 |
| 2024 | `12S` | `(sin concepto)` | 11 | 2.274,38 |
| 2026 | `71F` | `soberania` | 2 | 1.837,98 |
| 2025 | `71F` | `soberania` | 2 | 1.778,09 |
| 2023 | `71F` | `soberania` | 2 | 1.761,83 |
| 2024 | `71F` | `soberania` | 2 | 1.724,37 |
| 2022 | `71F` | `soberania` | 2 | 1.696,98 |
| 2019 | `71F` | `soberania` | 2 | 1.546,18 |
| 2018 | `71F` | `soberania` | 2 | 1.540,45 |
| 2017 | `71F` | `soberania` | 2 | 1.535,11 |
| 2017 | `31P` | `(sin concepto)` | 3 | 431,08 |
| 2019 | `31P` | `(sin concepto)` | 3 | 412,09 |
| 2018 | `31P` | `(sin concepto)` | 3 | 406,47 |
| 2024 | `61G` | `(sin concepto)` | 2 | 398,48 |
| 2022 | `31P` | `(sin concepto)` | 2 | 179,28 |
| 2019 | `61G` | `(sin concepto)` | 2 | 99,99 |
| 2018 | `61G` | `(sin concepto)` | 2 | 96,69 |
| 2017 | `61G` | `(sin concepto)` | 2 | 96,12 |
| 2023 | `61G` | `(sin concepto)` | 2 | 91,88 |
| … | *34 casos más* | | | |

### 4.2 · Códigos que CAMBIAN de concepto entre años (6 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `32L` | 765,62 | 2015:empleo, 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:empleo |
| `51A` | 251,56 | 2015:vivienda, 2016:(sin concepto), 2017:vivienda, 2018:vivienda, 2019:vivienda, 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `31A` | 126,62 | 2016:(sin concepto), 2017:igualdad, 2018:igualdad, 2019:igualdad |
| `45B` | 68,04 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:idi, 2026:idi |
| `45H` | 63,04 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:idi, 2025:idi, 2026:idi |
| `61J` | 61,79 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:idi |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `gastos_csv.csv` · 100 líneas · total extraído **29.476,05 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.388,30 M€ (8.388.296.442 €) · 6 códigos · 28,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACION Y FINANCIACION | 7.752.971.824 | 92,4 % |
| `41C` | ATENCION SANITARIA | 462.322.208 | 5,5 % |
| `41A` | D.Y S. GRALES. DE IGUALDAD, SALUD Y POLIT. SOC. | 114.964.763 | 1,4 % |
| `41K` | POLITICA DE CALIDAD Y MODERNIZACION | 25.635.368 | 0,3 % |
| `41D` | SALUD PUBLICA Y PARTICIPACION | 21.887.157 | 0,3 % |
| `41J` | INSPECCION DE SERVICIOS SANITARIOS | 10.515.122 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 6.587,40 M€ (6.587.403.880 €) · 10 códigos · 22,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACION SECUNDARIA Y FORMACION PROFESIONAL | 2.355.742.797 | 35,8 % |
| `42C` | EDUCACION INFANTIL Y PRIMARIA | 1.848.263.632 | 28,1 % |
| `42J` | UNIVERSIDADES | 1.152.598.389 | 17,5 % |
| `42E` | EDUCACION ESPECIAL | 299.374.564 | 4,5 % |
| `42F` | EDUCACION COMPENSATORIA | 274.415.529 | 4,2 % |
| `42I` | EDUCACION PARA LA PRIMERA INFANCIA | 267.700.281 | 4,1 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL | 158.665.717 | 2,4 % |
| `42A` | D.Y S. GRALES. DE EDUCACION, CULTURA Y DEPORTE | 103.432.399 | 1,6 % |
| `42G` | EDUCACION DE PERSONAS ADULTAS | 95.285.074 | 1,4 % |
| `42B` | FORMACION DEL PROFESORADO | 31.925.498 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 2.320,44 M€ (2.320.441.753 €) · 7 códigos · 7,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y GANADERO | 1.696.443.623 | 73,1 % |
| `71A` | D.Y S. GRALES. DE AGRICULTURA, PESCA Y DES. RURAL | 247.218.312 | 10,7 % |
| `71C` | REFORMA Y MEJORA DE LAS ESTRUCTURAS AGRARIAS | 171.293.327 | 7,4 % |
| `71H` | DESARROLLO RURAL | 91.981.587 | 4,0 % |
| `71E` | INCENTIVACION DEL SECTOR AGROINDUSTRIAL | 71.006.899 | 3,1 % |
| `71B` | ORDENAC. Y MEJORA DE LA PRODUC. AGRIC. Y GANAD. | 28.164.287 | 1,2 % |
| `71P` | PESCA | 14.333.718 | 0,6 % |

</details>

<details open><summary><b><code>vivienda</code> — 253,75 M€ (253.748.413 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACION Y SUELO | 192.176.379 | 75,7 % |
| `51A` | D.Y S. GRALES. DE FOMENTO Y VIVIENDA | 48.306.851 | 19,0 % |
| `43B` | ACT. MATERIA ORDENAC. TERRIT. Y CAMBIO CLIMATICO | 13.265.183 | 5,2 % |

</details>

<details open><summary><b><code>empleo</code> — 1.016,66 M€ (1.016.655.555 €) · 6 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32L` | EMPLEABILIDAD, INTERMEDIACION Y FOMENTO EMPLEO | 348.374.200 | 34,3 % |
| `32D` | FORMACION PROFESIONAL PARA EL EMPLEO | 327.880.919 | 32,3 % |
| `72C` | EMPRENDEDORES E INTERNAC. DE LA ECONOMIA ANDAL. | 195.389.761 | 19,2 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES | 124.984.997 | 12,3 % |
| `76A` | ORDENACION Y PROMOCION COMERCIAL | 17.099.334 | 1,7 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES | 2.926.344 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 554,56 M€ (554.563.795 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACION CIENTIFICA E INNOVACION | 350.039.500 | 63,1 % |
| `72A` | ENERGIA E INFRAESTRUCT. Y SERVICIOS TECNOLOGICOS | 166.659.426 | 30,1 % |
| `54C` | INNOVACION Y EVALUACION EDUCATIVA | 37.864.869 | 6,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.094,40 M€ (1.094.401.749 €) · 1 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO A. Y DISCAP. | 1.094.401.749 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 132,78 M€ (132.779.065 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCION A LA INFANCIA | 132.779.065 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 32,43 M€ (32.430.242 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE DROGODEPENDENCIAS | 32.430.242 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,59 M€ (2.588.349 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACION DE POLITICAS MIGRATORIAS | 2.588.349 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 100,52 M€ (100.523.803 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACION, ORDENACION Y PROMOCION TURISTICA | 66.284.051 | 65,9 % |
| `75A` | D.Y S. GRALES. DE TURISMO Y COMERCIO | 17.680.438 | 17,6 % |
| `75D` | CALIDAD, INNOVACION Y FOMENTO DEL TURISMO | 16.559.314 | 16,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,05 M€ (4.045.206 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` | PROTECC. CONTRA VIOLENCIA DE GENERO Y ASIST. VICT. | 4.045.206 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 8.988,17 M€ · 57 códigos · 30,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS CC.LL. | 3.037.036.566 |
| `01A` | ADMON. G. FINANC. Y AMORTIZACION DEUDA PUBLICA | 2.642.963.767 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS VIARIAS Y DE TRANSP. | 471.677.679 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS | 390.377.946 |
| `14B` | ADMINISTRACION DE JUSTICIA | 383.523.054 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA | 323.917.959 |
| `44E` | GESTION DEL MEDIO NATURAL | 227.151.314 |
| `32E` | INCLUSION SOCIAL | 152.235.281 |
| `52C` | COMUNICACION SOCIAL | 146.515.874 |
| `81A` | COOP. ECONOMICA Y COORDINACION CON LAS CC.LL. | 92.269.647 |
| `44A` | D.Y S. GRALES. DE MEDIO AMBIENTE Y ORDENAC. T. | 84.647.666 |
| `61G` | GESTION Y ADMON. DEL PATRIMONIO DE LA CA | 80.695.727 |
| `31N` | JUSTICIA JUVENIL Y COOPERACION | 77.691.310 |
| `61L` | COORDINACION Y CONTROL DE LA HACIENDA DE LA CA | 65.730.012 |
| `11A` | D.Y S. GRALES. DE LA PRESIDENCIA | 61.804.398 |
| `61J` | D.Y S.GRALES DE ECONOMIA, INNOVAC., CIENCIA Y EMP. | 61.790.593 |
| `31G` | BIENESTAR SOCIAL | 49.546.688 |
| `45B` | PLANIFICACION Y TUTELA DEL PATRIMONIO CULTURAL | 46.596.235 |
| `61I` | GESTION DE TECNOLOGIAS CORPORATIVAS | 43.943.836 |
| `82B` | COOPERACION PARA EL DESARROLLO | 42.108.111 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCION CIVIL | 40.219.522 |
| `61A` | D.Y S.GRALES. DE HACIENDA Y ADMON. PUBLICA | 39.096.312 |
| `11B` | ACTIVIDAD LEGISLATIVA | 38.463.769 |
| `44B` | PREVENCION Y CALIDAD AMBIENTAL | 26.654.929 |
| `44D` | ESPACIOS NATURALES Y PARTICIPACION CIUDADANA | 26.333.936 |
| … | *resto: 32 códigos* | 335.177.838 |

</details>

### 2016

*Fuente: `gastos_csv.csv` · 101 líneas · total extraído **31.130,28 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.657,78 M€ (8.657.784.983 €) · 6 códigos · 27,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` |  | 8.045.074.123 | 92,9 % |
| `41C` |  | 497.828.617 | 5,8 % |
| `41A` |  | 50.921.614 | 0,6 % |
| `41K` |  | 30.565.990 | 0,4 % |
| `41D` |  | 21.785.264 | 0,3 % |
| `41J` |  | 11.609.375 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 6.808,22 M€ (6.808.224.868 €) · 10 códigos · 21,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` |  | 2.447.542.915 | 35,9 % |
| `42C` |  | 1.939.086.578 | 28,5 % |
| `42J` |  | 1.186.412.300 | 17,4 % |
| `42E` |  | 304.475.705 | 4,5 % |
| `42F` |  | 283.190.324 | 4,2 % |
| `42I` |  | 278.408.570 | 4,1 % |
| `42H` |  | 165.379.586 | 2,4 % |
| `42G` |  | 98.731.101 | 1,5 % |
| `42A` |  | 73.439.298 | 1,1 % |
| `42B` |  | 31.558.491 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 2.304,64 M€ (2.304.635.011 €) · 6 códigos · 7,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` |  | 1.797.285.818 | 78,0 % |
| `71A` |  | 254.964.658 | 11,1 % |
| `71B` |  | 111.999.224 | 4,9 % |
| `71E` |  | 56.474.871 | 2,5 % |
| `71H` |  | 53.524.474 | 2,3 % |
| `71P` |  | 30.385.966 | 1,3 % |

</details>

<details open><summary><b><code>vivienda</code> — 263,05 M€ (263.048.857 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` |  | 240.878.749 | 91,6 % |
| `43B` |  | 22.170.108 | 8,4 % |

</details>

<details open><summary><b><code>empleo</code> — 555,97 M€ (555.967.600 €) · 6 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32D` |  | 238.730.033 | 42,9 % |
| `72C` |  | 147.374.730 | 26,5 % |
| `31C` |  | 133.386.594 | 24,0 % |
| `76A` |  | 17.279.953 | 3,1 % |
| `32A` |  | 16.310.671 | 2,9 % |
| `31M` |  | 2.885.619 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 651,52 M€ (651.517.336 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` |  | 328.606.423 | 50,4 % |
| `72A` |  | 281.344.074 | 43,2 % |
| `54C` |  | 41.566.839 | 6,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.136,81 M€ (1.136.809.504 €) · 1 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` |  | 1.136.809.504 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 140,17 M€ (140.170.311 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` |  | 140.170.311 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 34,63 M€ (34.632.142 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` |  | 34.632.142 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,76 M€ (2.764.143 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` |  | 2.764.143 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 101,69 M€ (101.687.931 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` |  | 67.431.726 | 66,3 % |
| `75A` |  | 23.752.155 | 23,4 % |
| `75D` |  | 10.504.050 | 10,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,19 M€ (4.190.854 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` |  | 4.190.854 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 10.468,84 M€ · 60 códigos · 33,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `81B` |  | 3.126.129.006 |
| `01A` |  | 2.997.568.478 |
| `32L` |  | 742.150.321 |
| `51B` |  | 472.893.571 |
| `31P` |  | 412.620.051 |
| `14B` |  | 400.054.713 |
| `44E` |  | 274.161.480 |
| `51D` |  | 265.776.801 |
| `32E` |  | 163.525.191 |
| `52C` |  | 145.956.451 |
| `31A` |  | 126.623.471 |
| `44A` |  | 92.450.473 |
| `81A` |  | 90.815.484 |
| `61G` |  | 85.980.484 |
| `31N` |  | 81.865.884 |
| `11A` |  | 78.985.132 |
| `61L` |  | 69.441.999 |
| `31G` |  | 58.904.643 |
| `61J` |  | 50.195.573 |
| `61I` |  | 50.151.971 |
| `61A` |  | 42.150.738 |
| `51A` |  | 42.110.110 |
| `82B` |  | 42.108.111 |
| `11B` |  | 39.977.605 |
| `22B` |  | 39.899.325 |
| … | *resto: 35 códigos* | 476.345.749 |

</details>

### 2017

*Fuente: `memoria_programas.pdf` · 110 líneas · total extraído **33.066,10 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.129,97 M€ (9.129.970.917 €) · 6 códigos · 27,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACION Y FINANCIACION 1.440.038 8.358.159.731 8.359.599.769 118.971.384 118.971.384 | 8.478.571.153 | 92,9 % |
| `41C` | ATENCION SANITARIA 241.622 513.086.442 513.328.064 4.053.579 4.053.579 | 517.381.643 | 5,7 % |
| `41A` | D.S.G. DE SALUD 65.243.987 6.819.497 31.500 72.094.984 515.000 515.000 | 72.609.984 | 0,8 % |
| `41K` | POLITICA DE CALIDAD Y MODERNIZACION 3.446.061 847.678 22.023.546 26.317.285 2.843.300 2.843.300 | 29.160.585 | 0,3 % |
| `41D` | SALUD PUBLICA Y PARTICIPACION 16.332.066 1.476.317 2.799.246 20.607.629 60.000 60.000 | 20.667.629 | 0,2 % |
| `41J` | INSPECCION DE SERVICIOS SANITARIOS 11.444.881 85.042 11.529.923 50.000 50.000 | 11.579.923 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 7.019,19 M€ (7.019.185.001 €) · 10 códigos · 21,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACION SECUNDARIA Y FORMACION 1.912.779.592 109.925.106 20.051 453.788.213 2.476.512.962 10.000.000 73.356.634 83.356.634 | 2.559.869.596 | 36,5 % |
| `42C` | EDUCACION INFANTIL Y PRIMARIA 1.526.977.613 23.294.549 5.000 348.745.380 1.899.022.542 15.000.000 68.059.053 83.059.053 | 1.982.081.595 | 28,2 % |
| `42J` | UNIVERSIDADES 3.527.567 228.420 127.587 719.596.370 723.479.944 1.626.562 466.319.217 467.945.779 5.070.118 5.070.118 | 1.196.495.841 | 17,0 % |
| `42E` | EDUCACION ESPECIAL 223.462.744 531.494 2.000 94.892.971 318.889.209 | 318.889.209 | 4,5 % |
| `42F` | EDUCACION COMPENSATORIA 125.778.496 16.489.676 1.000 149.914.569 292.183.741 | 292.183.741 | 4,2 % |
| `42I` | EDUCACION PARA LA PRIMERA INFANCIA 96.287.424 11.194.011 175.385.433 282.866.868 5.909.951 5.909.951 | 288.776.819 | 4,1 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 163.436.809 7.460.209 1.000 1.019.376 171.917.394 | 171.917.394 | 2,4 % |
| `42G` | EDUCACION DE PERSONAS ADULTAS 98.612.321 2.499.422 500 101.112.243 | 101.112.243 | 1,4 % |
| `42A` | D.S.G. DE EDUCACION 69.436.804 4.611.717 1.000 74.049.521 1.000.241 1.000.241 | 75.049.762 | 1,1 % |
| `42B` | FORMACION DEL PROFESORADO 28.175.031 4.633.770 32.808.801 | 32.808.801 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 2.090,30 M€ (2.090.298.945 €) · 7 códigos · 6,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 1.401.100.000 1.401.100.000 | 1.401.100.000 | 67,0 % |
| `71A` | D.S.G. DE AGRICULTURA, PESCA Y DESARROLLO 67.344.044 8.986.186 40.000 149.024.452 225.394.682 6.838.394 18.664.403 25.502.797 | 250.897.479 | 12,0 % |
| `71B` | ORDENACION Y MEJORA DE LA PRODUC. AGRIC. Y 1.753.000 6.063.639 7.816.639 10.879.617 128.968.255 139.847.872 | 147.664.511 | 7,1 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 3.391.280 250.000 150.000 3.791.280 16.441.306 113.776.231 130.217.537 | 134.008.817 | 6,4 % |
| `71H` | DESARROLLO RURAL 847.591 5.701.261 6.548.852 2.531.070 59.429.701 61.960.771 | 68.509.623 | 3,3 % |
| `71E` | INCENTIVACION DEL SECTOR AGROINDUSTRIAL 2.073.536 500.000 2.573.536 6.092.836 47.635.932 53.728.768 | 56.302.304 | 2,7 % |
| `71P` | PESCA 707.436 20.000 773.240 1.500.676 1.945.609 28.369.926 30.315.535 | 31.816.211 | 1,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 335,60 M€ (335.604.120 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACION Y SUELO 13.144.106 2.847.961 372.608 59.276.644 75.641.319 15.158.428 143.726.866 158.885.294 3.979.007 30.000.000 33.979.007 | 268.505.620 | 80,0 % |
| `51A` | D.S.G. DE FOMENTO Y VIVIENDA 33.991.212 7.379.842 31.103 41.402.157 4.470.824 4.470.824 | 45.872.981 | 13,7 % |
| `43B` | ACTUACIONES EN MATERIA ORDEN. TERRIT. Y 10.853.032 350.748 60.000 11.263.780 6.230.723 3.731.016 9.961.739 | 21.225.519 | 6,3 % |

</details>

<details open><summary><b><code>empleo</code> — 550,01 M€ (550.008.487 €) · 6 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32D` | FORMACION PROFESIONAL PARA EL EMPLEO 17.730.493 28.516.326 56.583.387 102.830.206 25.252.341 104.517.738 129.770.079 | 232.600.285 | 42,3 % |
| `72C` | EMPRENDEDORES E INTERNAC. DE LA ECONOMIA 7.756.365 17.848 75.318.843 83.093.056 2.748.109 62.545.335 65.293.444 | 148.386.500 | 27,0 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES 21.706.217 1.183.673 104.642.540 127.532.430 730.000 3.269.168 3.999.168 | 131.531.598 | 23,9 % |
| `76A` | ORDENACION Y PROMOCION COMERCIAL 5.779.480 224.000 1.240.000 7.243.480 3.663.196 7.452.187 11.115.383 | 18.358.863 | 3,3 % |
| `32A` | D.S.G. DE EMPLEO, EMPRESA Y COMERCIO 10.214.536 5.442.925 15.657.461 722.600 722.600 | 16.380.061 | 3,0 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES 1.411.450 1.299.516 18.150 2.729.116 22.064 22.064 | 2.751.180 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 683,77 M€ (683.769.226 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACION CIENTIFICA E INNOVACION 1.207.448 266.966 9.609.175 11.083.589 758.623 305.096.477 305.855.100 22.133.190 22.133.190 | 339.071.879 | 49,6 % |
| `72A` | ENERGIA E INFRAESTRUCT. Y SERVICIOS 15.493.493 1.751.005 24.231.405 41.475.903 29.511.944 225.203.235 254.715.179 | 296.191.082 | 43,3 % |
| `54C` | INNOVACION Y EVALUACION EDUCATIVA 15.218.825 10.971.871 26.190.696 22.092.973 222.596 22.315.569 | 48.506.265 | 7,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.164,91 M€ (1.164.914.040 €) · 1 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO A. Y 131.373.498 23.126.246 30.000 999.239.002 1.153.768.746 6.082.002 5.063.292 11.145.294 | 1.164.914.040 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 143,16 M€ (143.159.588 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCION A LA INFANCIA 45.341.985 63.212.435 30.900 34.474.268 143.059.588 100.000 100.000 | 143.159.588 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 36,18 M€ (36.175.436 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE DROGODEPENDENCIAS 3.679.290 7.973.102 22.222.379 33.874.771 76.040 2.224.625 2.300.665 | 36.175.436 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,26 M€ (3.257.191 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACION DE POLITICAS MIGRATORIAS 1.196.191 200.000 1.700.000 3.096.191 161.000 161.000 | 3.257.191 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 116,20 M€ (116.196.102 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACION, ORDENACION Y PROMOCION 7.200.612 21.687.337 28.887.949 1.982.591 37.303.206 39.285.797 | 68.173.746 | 58,7 % |
| `75A` | D.S.G. DE TURISMO Y DEPORTE 26.770.359 4.556.393 31.326.752 735.773 735.773 | 32.062.525 | 27,6 % |
| `75D` | CALIDAD, INNOVACION Y FOMENTO DEL TURISMO 1.186.816 2.664.247 3.851.063 498.859 11.609.909 12.108.768 | 15.959.831 | 13,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 116,32 M€ (116.317.661 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31A` | D.S.G. DE IGUALDAD Y POLÍTICAS SOCIALES 45.285.459 4.413.104 9.100 56.191.165 105.898.828 1.447.000 4.772.675 6.219.675 | 112.118.503 | 96,4 % |
| `31T` | PROTECC. CONTRA VIOLENCIA DE GENERO Y ASIST. 519.158 2.690.000 990.000 4.199.158 | 4.199.158 | 3,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 11.677,24 M€ · 66 códigos · 35,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON. G. FINANC. Y AMORTIZACION DEUDA 486.353 479.563.744 480.050.097 3.682.000.000 3.682.000.000 | 4.162.050.097 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 2.649.279.132 2.649.279.132 4.251.226 4.251.226 | 2.653.530.358 |
| `32L` | EMPLEABILIDAD, INTERMEDIACION Y FOMENTO 414.677.944 414.677.944 341.128.379 341.128.379 | 755.806.323 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS VIARIAS Y DE 31.211.926 298.249 7.861.046 165.115.368 204.486.589 246.809.864 66.900.366 313.710.230 | 518.196.819 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 480.000.000 480.000.000 | 480.000.000 |
| `14B` | ADMINISTRACION DE JUSTICIA 290.952.601 78.733.798 43.440.741 413.127.140 18.289.702 18.289.702 | 431.416.842 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 28.111.579 16.308.832 2.029.026 46.449.437 229.505.543 100.000 229.605.543 | 276.054.980 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 85.823.631 146.338.156 232.161.787 | 232.161.787 |
| `44E` | GESTION DEL MEDIO NATURAL 23.250.764 2.033.260 500.000 6.000 25.790.024 152.132.361 21.132.274 173.264.635 | 199.054.659 |
| `32E` | INCLUSION SOCIAL 161.675.008 161.675.008 26.891.051 26.891.051 | 188.566.059 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 169.633.992 169.633.992 | 169.633.992 |
| `44F` | SOSTENIBILIDAD E INFORMACION AMBIENTAL 1.244.518 866.114 131.660.689 133.771.321 14.099.904 1.125.550 15.225.454 | 148.996.775 |
| `52C` | COMUNICACION SOCIAL 1.629.145 1.849.387 140.679.000 144.157.532 4.260.000 4.260.000 | 148.417.532 |
| `44A` | D.S.G. DE M. AMBIENTE Y ORDENACIÓN DEL 75.566.665 14.115.055 500.000 90.181.720 10.392.928 10.392.928 | 100.574.648 |
| `61G` | GESTION Y ADMINISTRACION DEL PATRIMONIO DE LA 1.740.000 71.479.955 91.740 73.311.695 19.142.252 19.142.252 | 92.453.947 |
| `81A` | COOP. ECONOMICA Y COORDINACION CON LAS 5.179.051 170.620 836.000 6.185.671 488.479 76.277.265 76.765.744 | 82.951.415 |
| `31N` | JUSTICIA JUVENIL Y ASISTENCIA A VICTIMAS 6.690.500 73.030.665 2.200.000 81.921.165 133.557 133.557 | 82.054.722 |
| `11A` | D.S.G. DE LA PRESIDENCIA Y ADMINISTRACIÓN 56.450.650 14.143.344 2.508.505 73.102.499 5.278.436 192.249 5.470.685 | 78.573.184 |
| `61L` | COORDINACION Y CONTROL DE LA HACIENDA DE LA 813.037 906.811 70.083.335 71.803.183 | 71.803.183 |
| `31G` | BIENESTAR SOCIAL 2.079.014 57.832 50.645.323 52.782.169 | 52.782.169 |
| `61J` | D.S.G. DE ECONOMIA Y CONOCIMIENTO 44.620.895 6.171.081 4.334 50.796.310 1.583.916 1.583.916 | 52.380.226 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO 17.552.025 3.412.109 20.875.939 41.840.073 2.997.108 3.250.473 6.247.581 | 48.087.654 |
| `61I` | GESTION DE TECNOLOGIAS CORPORATIVAS 780.000 780.000 43.170.303 43.170.303 | 43.950.303 |
| `82B` | COOPERACION PARA EL DESARROLLO 42.464.733 42.464.733 111.908 111.908 | 42.576.641 |
| `61A` | D.S.G. DE HACIENDA Y ADMINISTRACION PUBLICA 26.845.966 3.801.759 10.352.107 40.999.832 82.200 365.031 447.231 | 41.447.063 |
| … | *resto: 41 códigos* | 523.720.336 |

</details>

### 2018

*Fuente: `memoria_programas.pdf` · 111 líneas · total extraído **34.586,56 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.627,55 M€ (9.627.553.896 €) · 6 códigos · 27,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACION Y FINANCIACION 1.488.380 8.809.879.184 8.811.367.564 103.786.408 103.786.408 | 8.915.153.972 | 92,6 % |
| `41C` | ATENCION SANITARIA 466.992 563.453.442 563.920.434 6.277.000 6.277.000 | 570.197.434 | 5,9 % |
| `41A` | D.S.G. DE SALUD 66.281.728 9.817.762 31.500 76.130.990 167.702 167.702 | 76.298.692 | 0,8 % |
| `41K` | POLITICA DE CALIDAD Y MODERNIZACION 3.366.012 764.478 23.689.460 27.819.950 1.499.491 4.236.793 5.736.284 | 33.556.234 | 0,3 % |
| `41D` | SALUD PUBLICA Y PARTICIPACION 16.561.961 1.458.210 1.796.396 19.816.567 212.856 287.750 500.606 | 20.317.173 | 0,2 % |
| `41J` | INSPECCION DE SERVICIOS SANITARIOS 11.896.049 85.042 11.981.091 49.300 49.300 | 12.030.391 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 7.329,75 M€ (7.329.745.592 €) · 10 códigos · 21,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACION SECUNDARIA Y FORMACION 2.064.625.827 113.412.747 20.051 450.452.414 2.628.511.039 10.242.000 78.563.129 88.805.129 | 2.717.316.168 | 37,1 % |
| `42C` | EDUCACION INFANTIL Y PRIMARIA 1.562.320.070 21.688.564 5.000 357.832.834 1.941.846.468 15.000.000 62.177.800 77.177.800 | 2.019.024.268 | 27,5 % |
| `42J` | UNIVERSIDADES 1.733.223 178.420 114.194 756.479.726 758.505.563 1.704.990 483.274.714 484.979.704 5.083.511 5.083.511 | 1.248.568.778 | 17,0 % |
| `42E` | EDUCACION ESPECIAL 226.186.658 531.494 2.000 112.080.324 338.800.476 | 338.800.476 | 4,6 % |
| `42F` | EDUCACION COMPENSATORIA 137.934.072 17.823.598 1.000 150.477.034 306.235.704 | 306.235.704 | 4,2 % |
| `42I` | EDUCACION PARA LA PRIMERA INFANCIA 101.834.401 11.194.011 184.645.850 297.674.262 4.648.491 4.648.491 | 302.322.753 | 4,1 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 172.048.643 7.679.963 1.000 1.134.930 180.864.536 | 180.864.536 | 2,5 % |
| `42G` | EDUCACION DE PERSONAS ADULTAS 102.744.234 2.395.695 450 105.140.379 | 105.140.379 | 1,4 % |
| `42A` | D.S.G. DE EDUCACION 71.381.212 4.611.717 1.000 75.993.929 1.035.241 1.035.241 | 77.029.170 | 1,1 % |
| `42B` | FORMACION DEL PROFESORADO 28.999.030 5.444.330 34.443.360 | 34.443.360 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 2.125,29 M€ (2.125.288.201 €) · 7 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 1.401.000.000 1.401.000.000 | 1.401.000.000 | 65,9 % |
| `71A` | D.S.G. DE AGRICULTURA, PESCA Y DESARROLLO 68.343.271 8.727.147 40.000 153.882.750 230.993.168 8.300.243 27.781.084 36.081.327 | 267.074.495 | 12,6 % |
| `71B` | ORDENACION Y MEJORA DE LA PRODUC. AGRIC. Y 1.725.170 7.880.000 9.605.170 8.137.238 144.750.089 152.887.327 | 162.492.497 | 7,6 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 34.501 3.741.280 250.000 150.000 4.175.781 15.979.474 119.296.776 135.276.250 | 139.452.031 | 6,6 % |
| `71P` | PESCA 705.135 20.000 1.422.888 2.148.023 2.889.650 56.597.390 59.487.040 | 61.635.063 | 2,9 % |
| `71E` | INCENTIVACION DEL SECTOR AGROINDUSTRIAL 2.030.417 1.500.000 3.530.417 5.184.102 49.915.487 55.099.589 | 58.630.006 | 2,8 % |
| `71H` | DESARROLLO RURAL 923.872 1.200.000 8.872.620 10.996.492 954.420 23.053.197 24.007.617 | 35.004.109 | 1,6 % |

</details>

<details open><summary><b><code>vivienda</code> — 335,85 M€ (335.848.665 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACION Y SUELO 13.028.857 3.009.080 372.608 61.133.997 77.544.542 20.450.474 123.479.123 143.929.597 2.790.038 30.000.000 32.790.038 | 254.264.177 | 75,7 % |
| `51A` | D.S.G. DE FOMENTO Y VIVIENDA 41.607.351 7.379.842 4.731.103 53.718.296 4.420.824 4.420.824 | 58.139.120 | 17,3 % |
| `43B` | ACTUACIONES EN MATERIA ORDEN. TERRIT. Y 10.938.861 250.748 60.000 11.249.609 8.597.498 3.598.261 12.195.759 | 23.445.368 | 7,0 % |

</details>

<details open><summary><b><code>empleo</code> — 549,95 M€ (549.950.970 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32D` | FORMACION PROFESIONAL PARA EL EMPLEO 17.778.887 6.275.369 52.469.998 76.524.254 5.844.821 156.806.705 162.651.526 | 239.175.780 | 43,5 % |
| `72C` | EMPRENDIMIENTO E INTERNACIONALIZ. ECON. 7.486.861 17.848 78.904.030 86.408.739 2.562.552 48.516.143 51.078.695 | 137.487.434 | 25,0 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES 21.778.041 1.273.673 105.192.980 128.244.694 730.000 3.900.000 4.630.000 | 132.874.694 | 24,2 % |
| `76A` | ORDENACION Y PROMOCION COMERCIAL 5.794.739 284.000 925.000 7.003.739 3.112.876 9.230.460 12.343.336 | 19.347.075 | 3,5 % |
| `32A` | D.S.G. DE EMPLEO, EMPRESA Y COMERCIO 11.280.731 5.692.925 16.973.656 812.600 812.600 | 17.786.256 | 3,2 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES 1.790.001 1.449.516 18.150 3.257.667 22.064 22.064 | 3.279.731 | 0,6 % |

</details>

<details open><summary><b><code>idi</code> — 734,50 M€ (734.495.734 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACION CIENTIFICA E INNOVACION 1.821.466 1.225.448 4.158.855 10.069.858 17.275.627 1.892.562 300.134.032 302.026.594 36.401.529 36.401.529 | 355.703.750 | 48,4 % |
| `72A` | ENERGIA E INFRAESTRUCT. Y SERVICIOS 15.532.968 1.376.005 24.413.842 41.322.815 37.235.222 248.776.056 286.011.278 | 327.334.093 | 44,6 % |
| `54C` | INNOVACION Y EVALUACION EDUCATIVA 16.557.356 13.581.198 30.138.554 21.048.592 270.745 21.319.337 | 51.457.891 | 7,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.196,02 M€ (1.196.024.692 €) · 1 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO A. Y 133.766.962 26.839.903 30.000 1.027.495.157 1.188.132.022 5.696.737 2.195.933 7.892.670 | 1.196.024.692 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 153,48 M€ (153.480.255 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCION A LA INFANCIA 46.951.031 66.465.435 30.900 39.632.889 153.080.255 400.000 400.000 | 153.480.255 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 38,27 M€ (38.267.726 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE DROGODEPENDENCIAS 3.742.078 8.534.701 25.130.947 37.407.726 110.000 750.000 860.000 | 38.267.726 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,92 M€ (4.917.755 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACION DE POLITICAS MIGRATORIAS 1.195.513 272.000 2.290.242 3.757.755 160.000 1.000.000 1.160.000 | 4.917.755 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 118,72 M€ (118.724.974 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACION, ORDENACION Y PROMOCION 7.564.803 14.119 21.901.662 29.480.584 3.934.616 40.837.665 44.772.281 | 74.252.865 | 62,5 % |
| `75A` | D.S.G. DE TURISMO Y DEPORTE 26.954.523 4.506.393 31.460.916 735.773 735.773 | 32.196.689 | 27,1 % |
| `75D` | CALIDAD, INNOVACION Y FOMENTO DEL TURISMO 1.222.217 3.077.259 4.299.476 285.062 7.690.882 7.975.944 | 12.275.420 | 10,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 118,24 M€ (118.244.988 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31A` | D.S.G. DE IGUALDAD Y POLÍTICAS SOCIALES 44.648.233 5.813.588 9.100 59.952.858 110.423.779 630.050 2.985.794 3.615.844 | 114.039.623 | 96,4 % |
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE GÉNERO 544.123 2.171.242 1.490.000 4.205.365 | 4.205.365 | 3,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.254,01 M€ · 67 códigos · 35,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON. G. FINANC. Y AMORTIZACION DEUDA 486.353 518.004.816 518.491.169 43.620.000 3.994.150.000 4.037.770.000 | 4.556.261.169 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 2.649.279.132 2.649.279.132 4.251.226 4.251.226 | 2.653.530.358 |
| `32L` | EMPLEABILIDAD, INTERMEDIACION Y FOMENTO 479.082.310 479.082.310 286.541.441 286.541.441 | 765.623.751 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS VIARIAS Y DE 24.886.245 632.251 184.023.007 209.541.503 241.376.700 94.621.306 335.998.006 | 545.539.509 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 480.000.000 480.000.000 | 480.000.000 |
| `14B` | ADMINISTRACION DE JUSTICIA 302.463.464 82.397.293 43.984.351 428.845.108 23.218.747 23.218.747 | 452.063.855 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 28.459.000 19.000.000 2.029.026 55.200 49.543.226 225.562.297 225.562.297 | 275.105.523 |
| `32E` | INCLUSION SOCIAL 235.231.577 235.231.577 5.042.278 5.042.278 | 240.273.855 |
| `44E` | GESTION DEL MEDIO NATURAL 23.339.013 1.993.011 500.000 61.000 25.893.024 140.951.559 35.908.212 176.859.771 | 202.752.795 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 58.067.110 138.426.511 196.493.621 | 196.493.621 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 171.633.992 171.633.992 | 171.633.992 |
| `44F` | SOSTENIBILIDAD E INFORMACION AMBIENTAL 1.283.952 844.744 142.675.400 144.804.096 13.956.736 1.052.014 15.008.750 | 159.812.846 |
| `52C` | COMUNICACION SOCIAL 1.513.255 1.566.650 141.437.920 144.517.825 4.672.000 4.672.000 | 149.189.825 |
| `44A` | D.S.G. DE M. AMBIENTE Y ORDENACIÓN DEL 78.043.888 12.823.913 500.000 91.367.801 9.104.990 9.104.990 | 100.472.791 |
| `31G` | BIENESTAR SOCIAL 2.082.295 129.235 82.789.443 85.000.973 1.505.950 7.500.000 9.005.950 | 94.006.923 |
| `61G` | GESTION Y ADMINISTRACION DEL PATRIMONIO DE LA 3.328.747 72.627.175 91.740 76.047.662 17.061.752 17.061.752 | 93.109.414 |
| `31N` | JUSTICIA JUVENIL Y ASISTENCIA A VICTIMAS 6.505.584 73.062.430 3.700.000 83.268.014 133.557 133.557 | 83.401.571 |
| `81A` | COOP. ECONOMICA Y COORDINACION CON LAS 5.201.955 145.620 900.000 6.247.575 1.258.703 75.561.316 76.820.019 | 83.067.594 |
| `11A` | D.S.G. PRESIDENCIA, ADMÓN LOCAL Y M. 57.576.095 13.000.999 2.523.850 73.100.944 6.564.086 192.249 6.756.335 | 79.857.279 |
| `61L` | COORDINACION Y CONTROL DE LA HACIENDA DE LA 981.403 906.811 72.891.317 74.779.531 95.000 95.000 | 74.874.531 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO 17.998.181 4.183.569 2.000 23.904.323 46.088.073 5.253.813 9.555.926 14.809.739 | 60.897.812 |
| `61J` | D.S.G. DE ECONOMIA Y CONOCIMIENTO 45.757.301 6.544.100 16.500 52.317.901 1.639.189 1.639.189 | 53.957.090 |
| `61I` | GESTION DE TECNOLOGIAS CORPORATIVAS 780.000 780.000 46.988.090 46.988.090 | 47.768.090 |
| `61A` | D.S.G. DE HACIENDA Y ADMINISTRACION PUBLICA 27.991.608 4.042.025 10.994.258 43.027.891 82.200 365.031 447.231 | 43.475.122 |
| `82B` | COOPERACION PARA EL DESARROLLO 43.064.733 43.064.733 111.908 111.908 | 43.176.641 |
| … | *resto: 42 códigos* | 547.667.615 |

</details>

### 2019

*Fuente: `memoria_programas.pdf` · 112 líneas · total extraído **34.685,07 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.613,26 M€ (9.613.264.022 €) · 6 códigos · 27,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACION Y FINANCIACION 1.444.182 8.825.049.516 8.826.493.698 75.862.713 75.862.713 | 8.902.356.411 | 92,6 % |
| `41C` | ATENCION SANITARIA 466.992 563.453.442 563.920.434 5.393.000 5.393.000 | 569.313.434 | 5,9 % |
| `41A` | D.S.G. DE SALUD 59.374.185 9.817.762 31.500 69.223.447 167.702 167.702 | 69.391.149 | 0,7 % |
| `41K` | POLITICA DE CALIDAD Y MODERNIZACION 3.757.622 215.326 24.244.460 28.217.408 1.888.193 11.190.615 13.078.808 | 41.296.216 | 0,4 % |
| `41D` | SALUD PUBLICA Y PARTICIPACION 16.752.092 1.494.410 1.680.976 19.927.478 320.688 341.750 662.438 | 20.589.916 | 0,2 % |
| `41J` | INSPECCION DE SERVICIOS SANITARIOS 10.182.854 94.042 10.276.896 40.000 40.000 | 10.316.896 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 7.296,32 M€ (7.296.321.233 €) · 10 códigos · 21,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACION SECUNDARIA Y FORMACION 2.101.384.834 113.521.987 20.051 453.238.850 2.668.165.722 10.201.155 50.188.574 60.389.729 | 2.728.555.451 | 37,4 % |
| `42C` | EDUCACION INFANTIL Y PRIMARIA 1.533.431.670 21.688.564 5.000 357.832.834 1.912.958.068 15.000.000 50.242.162 65.242.162 | 1.978.200.230 | 27,1 % |
| `42J` | UNIVERSIDADES 1.753.922 178.420 114.194 756.517.516 758.564.052 1.704.990 483.274.714 484.979.704 5.097.093 5.097.093 | 1.248.640.849 | 17,1 % |
| `42E` | EDUCACION ESPECIAL 227.753.387 531.494 2.000 115.474.486 343.761.367 | 343.761.367 | 4,7 % |
| `42I` | EDUCACION PARA LA PRIMERA INFANCIA 103.698.767 11.194.011 184.645.850 299.538.628 4.648.491 4.648.491 | 304.187.119 | 4,2 % |
| `42F` | EDUCACION COMPENSATORIA 138.974.703 17.823.598 1.000 135.042.378 291.841.679 | 291.841.679 | 4,0 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 180.058.090 7.679.963 1.000 1.134.930 188.873.983 | 188.873.983 | 2,6 % |
| `42G` | EDUCACION DE PERSONAS ADULTAS 97.340.543 2.395.695 450 99.736.688 | 99.736.688 | 1,4 % |
| `42A` | D.S.G. DE EDUCACION 73.893.121 4.611.717 1.000 78.505.838 1.007.866 1.007.866 | 79.513.704 | 1,1 % |
| `42B` | FORMACION DEL PROFESORADO 27.430.953 5.579.210 33.010.163 | 33.010.163 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 2.228,42 M€ (2.228.419.323 €) · 7 códigos · 6,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 1.401.000.000 1.401.000.000 | 1.401.000.000 | 62,9 % |
| `71A` | D.S.G. DE AGRICULTURA, PESCA Y DESARROLLO 68.011.550 8.727.147 40.000 146.118.508 222.897.205 9.430.119 33.325.142 42.755.261 | 265.652.466 | 11,9 % |
| `71B` | ORDENACION Y MEJORA DE LA PRODUC. AGRIC. Y 1.844.946 7.917.068 9.762.014 6.785.910 137.962.429 144.748.339 | 154.510.353 | 6,9 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRICOLA Y 94.742 3.741.280 250.000 150.000 4.236.022 15.790.034 125.155.847 140.945.881 | 145.181.903 | 6,5 % |
| `71E` | INCENTIVACION DEL SECTOR AGROINDUSTRIAL 2.289.749 1.500.000 3.789.749 5.538.323 112.432.350 117.970.673 | 121.760.422 | 5,5 % |
| `71H` | DESARROLLO RURAL 888.350 1.200.000 6.500.000 8.588.350 9.352.261 68.339.793 77.692.054 | 86.280.404 | 3,9 % |
| `71P` | PESCA 752.805 40.000 1.607.789 2.400.594 2.061.920 49.571.261 51.633.181 | 54.033.775 | 2,4 % |

</details>

<details open><summary><b><code>vivienda</code> — 338,45 M€ (338.451.933 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACION Y SUELO 13.229.168 3.102.158 372.608 49.614.338 66.318.272 17.477.745 128.753.274 146.231.019 2.790.038 30.000.000 32.790.038 | 245.339.329 | 72,5 % |
| `51A` | D.S.G. DE FOMENTO Y VIVIENDA 36.830.188 7.379.842 4.731.103 48.941.133 4.420.824 4.420.824 | 53.361.957 | 15,8 % |
| `43B` | ACTUACIONES EN MATERIA ORDEN. TERRIT. Y 11.657.584 250.748 60.000 11.968.332 21.468.020 6.314.295 27.782.315 | 39.750.647 | 11,7 % |

</details>

<details open><summary><b><code>empleo</code> — 530,18 M€ (530.179.843 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32D` | FORMACION PROFESIONAL PARA EL EMPLEO 18.391.761 5.423.479 116.525.934 140.341.174 7.022.828 98.303.929 105.326.757 | 245.667.931 | 46,3 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES 22.920.770 1.273.673 105.122.980 129.317.423 730.000 3.900.000 4.630.000 | 133.947.423 | 25,3 % |
| `72C` | EMPRENDIMIENTO E INTERNACIONALIZ. ECON. 5.900.133 66.611.435 72.511.568 1.989.258 35.157.482 37.146.740 | 109.658.308 | 20,7 % |
| `76A` | ORDENACION Y PROMOCION COMERCIAL 6.145.319 284.000 925.000 7.354.319 3.179.076 11.348.701 14.527.777 | 21.882.096 | 4,1 % |
| `32A` | D.S.G. DE EMPLEO, EMPRESA Y COMERCIO 9.395.271 5.692.925 15.088.196 812.600 812.600 | 15.900.796 | 3,0 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES 1.633.559 1.449.516 18.150 3.101.225 22.064 22.064 | 3.123.289 | 0,6 % |

</details>

<details open><summary><b><code>idi</code> — 862,87 M€ (862.871.752 €) · 4 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACION CIENTIFICA E INNOVACION 2.020.469 1.225.448 4.158.855 9.190.148 16.594.920 6.850.754 332.834.039 339.684.793 38.547.760 38.547.760 | 394.827.473 | 45,8 % |
| `72A` | ENERGIA E INFRAESTRUCT. Y SERVICIOS 15.328.318 1.394.505 25.293.552 42.016.375 57.216.744 258.740.341 315.957.085 | 357.973.460 | 41,5 % |
| `54C` | INNOVACION Y EVALUACION EDUCATIVA 16.607.356 11.961.286 28.568.642 32.811.556 270.745 33.082.301 | 61.650.943 | 7,1 % |
| `61J` | D.S.G. CONOCIMIENTO, INVESTIGACIÓN Y 40.220.087 6.544.100 16.500 46.780.687 1.639.189 1.639.189 | 48.419.876 | 5,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.195,01 M€ (1.195.006.504 €) · 1 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO A. Y 133.451.845 24.617.352 30.000 1.026.065.578 1.184.164.775 8.340.876 2.500.853 10.841.729 | 1.195.006.504 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 155,43 M€ (155.425.426 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCION A LA INFANCIA 47.274.202 67.807.435 30.900 39.632.889 154.745.426 680.000 680.000 | 155.425.426 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 38,23 M€ (38.229.327 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE DROGODEPENDENCIAS 3.877.471 8.534.701 24.647.947 37.060.119 115.000 1.054.208 1.169.208 | 38.229.327 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,97 M€ (4.972.084 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACION DE POLITICAS MIGRATORIAS 1.250.352 272.000 2.289.732 3.812.084 160.000 1.000.000 1.160.000 | 4.972.084 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 120,31 M€ (120.308.062 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACION, ORDENACION Y PROMOCION 7.851.197 8.460 21.901.662 29.761.319 3.688.298 39.785.152 43.473.450 | 73.234.769 | 60,9 % |
| `75A` | D.S.G. DE TURISMO Y DEPORTE 26.037.125 4.506.393 30.543.518 735.773 735.773 | 31.279.291 | 26,0 % |
| `75D` | CALIDAD, INNOVACION Y FOMENTO DEL TURISMO 1.249.886 3.077.259 4.327.145 474.009 10.992.848 11.466.857 | 15.794.002 | 13,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 117,68 M€ (117.675.286 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31A` | D.S.G. DE IGUALDAD Y POLÍTICAS SOCIALES 44.549.008 5.813.588 9.100 58.939.432 109.311.128 1.053.376 2.985.794 4.039.170 | 113.350.298 | 96,3 % |
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE GÉNERO 663.746 2.171.242 1.490.000 4.324.988 | 4.324.988 | 3,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.183,95 M€ · 67 códigos · 35,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON. G. FINANC. Y AMORTIZACION DEUDA 486.353 495.165.848 495.652.201 43.620.000 4.134.852.438 4.178.472.438 | 4.674.124.639 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 2.649.279.132 2.649.279.132 4.251.226 4.251.226 | 2.653.530.358 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS VIARIAS Y DE 24.286.234 667.039 183.737.518 208.690.791 248.860.791 92.178.360 341.039.151 | 549.729.942 |
| `32L` | EMPLEABILIDAD, INTERMEDIACION Y FOMENTO 462.836.427 462.836.427 69.982.644 69.982.644 | 532.819.071 |
| `81B` | COOPERACION ECONOMICA Y RELAC. FINANCIERAS 480.000.000 480.000.000 | 480.000.000 |
| `14B` | ADMINISTRACION DE JUSTICIA 303.826.591 82.397.293 43.984.351 430.208.235 22.713.351 22.713.351 | 452.921.586 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 29.652.752 19.088.294 2.029.026 55.200 50.825.272 259.261.601 259.261.601 | 310.086.873 |
| `32E` | INCLUSION SOCIAL 241.532.892 241.532.892 3.352.742 3.352.742 | 244.885.634 |
| `44E` | GESTION DEL MEDIO NATURAL 22.995.609 3.916.108 500.000 61.000 27.472.717 168.078.150 11.742.014 179.820.164 | 207.292.881 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 66.196.123 135.926.994 202.123.117 | 202.123.117 |
| `31P` | SERVICIO DE APOYO A LAS FAMILIAS 171.633.992 171.633.992 | 171.633.992 |
| `44F` | SOSTENIBILIDAD E INFORMACION AMBIENTAL 1.277.869 935.347 142.675.400 144.888.616 13.758.543 1.382.886 15.141.429 | 160.030.045 |
| `52C` | COMUNICACION SOCIAL 1.804.128 1.566.650 141.437.920 144.808.698 4.672.000 4.672.000 | 149.480.698 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 2.054.569 129.235 85.227.079 87.410.883 2.387.637 7.500.000 9.887.637 | 97.298.520 |
| `61G` | GESTION Y ADMINISTRACION DEL PATRIMONIO DE LA 6.300.000 72.627.175 91.740 79.018.915 17.061.752 17.061.752 | 96.080.667 |
| `44A` | D.S.G. DE M. AMBIENTE Y ORDENACIÓN DEL 71.872.841 12.823.913 500.000 85.196.754 9.633.206 9.633.206 | 94.829.960 |
| `81A` | COOP. ECONOMICA Y COORDINACION CON LAS 5.555.432 145.620 900.000 6.601.052 1.851.446 75.561.316 77.412.762 | 84.013.814 |
| `31N` | JUSTICIA JUVENIL Y ASISTENCIA A VICTIMAS 6.975.651 73.062.430 3.700.000 83.738.081 133.557 133.557 | 83.871.638 |
| `11A` | D.S.G. PRESIDENCIA, ADMÓN LOCAL Y M. 57.758.835 13.000.999 2.523.850 73.283.684 6.362.845 192.249 6.555.094 | 79.838.778 |
| `61L` | COORDINACION Y CONTROL DE LA HACIENDA DE LA 783.346 906.811 77.881.126 79.571.283 95.000 95.000 | 79.666.283 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO 16.843.680 4.183.569 2.000 25.479.323 46.508.572 9.168.393 7.358.431 16.526.824 | 63.035.396 |
| `61I` | GESTION DE TECNOLOGIAS CORPORATIVAS 780.000 780.000 48.041.011 48.041.011 | 48.821.011 |
| `82B` | COOPERACION PARA EL DESARROLLO 43.064.733 43.064.733 111.908 111.908 | 43.176.641 |
| `61A` | D.S.G. ECONOMÍA, HACIENDA Y ADMINISTRACIÓN 27.440.010 4.042.025 10.994.258 42.476.293 82.200 365.031 447.231 | 42.923.524 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCION CIVIL 17.256.564 15.991.615 530.000 33.778.179 8.274.400 8.274.400 | 42.052.579 |
| … | *resto: 42 códigos* | 539.681.385 |

</details>

### 2020

*Fuente: `gastos_csv.csv` · 97 líneas · total extraído **38.277,95 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 10.765,89 M€ (10.765.885.257 €) · 5 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACIÓN Y FINANCIACIÓN | 9.962.302.670 | 92,5 % |
| `41C` | ATENCIÓN SANITARIA | 724.826.093 | 6,7 % |
| `41K` | POLÍTICA DE CALIDAD Y MODERNIZACIÓN | 42.169.767 | 0,4 % |
| `41D` | SALUD PÚBLICA Y PARTICIPACIÓN | 25.069.330 | 0,2 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS | 11.517.397 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 7.887,89 M€ (7.887.891.327 €) · 10 códigos · 20,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION PROFESIONAL | 2.992.865.018 | 37,9 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA | 2.047.315.233 | 26,0 % |
| `42J` | UNIVERSIDADES | 1.348.372.131 | 17,1 % |
| `42E` | EDUCACIÓN ESPECIAL | 416.355.268 | 5,3 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA | 336.486.479 | 4,3 % |
| `42F` | EDUCACIÓN COMPENSATORIA | 302.499.748 | 3,8 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL | 229.417.569 | 2,9 % |
| `12L` | D.S.G. DE EDUCACIÓN Y DEPORTE | 98.992.757 | 1,3 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS | 91.691.232 | 1,2 % |
| `42B` | FORMACIÓN DEL PROFESORADO | 23.895.892 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.577,05 M€ (2.577.053.563 €) · 6 códigos · 6,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y GANADERO | 1.692.143.934 | 65,7 % |
| `12M` | D.S.G. AGRIC., GANADERÍA, PESCA Y DESA. SOSTENIBLE | 380.292.644 | 14,8 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. AGRIC. Y GANAD. | 283.056.815 | 11,0 % |
| `71E` | INCENTIVACIÓN DEL SECTOR AGROINDUSTRIAL | 103.611.701 | 4,0 % |
| `71H` | DESARROLLO RURAL | 65.731.960 | 2,6 % |
| `71P` | PESCA | 52.216.509 | 2,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 318,30 M€ (318.299.022 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO | 295.655.976 | 92,9 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y URBANISMO | 22.643.046 | 7,1 % |

</details>

<details open><summary><b><code>empleo</code> — 1.145,80 M€ (1.145.803.823 €) · 7 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32L` | EMPLEABILIDAD, INTERMEDIACIÓN Y FOMENTO DEL EMPLEO | 641.674.462 | 56,0 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO | 213.194.401 | 18,6 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL | 104.031.579 | 9,1 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES | 103.260.658 | 9,0 % |
| `12J` | D.S.G. EMPLEO, FORMACIÓN Y TRABAJO AUTÓNOMO | 59.104.757 | 5,2 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL | 20.959.315 | 1,8 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES | 3.578.651 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 705,86 M€ (705.858.590 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN | 406.903.762 | 57,6 % |
| `72A` | EMPRESA, EMPRENDI. INNOVADOR Y ECONOMÍA DIGITAL | 229.300.649 | 32,5 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA | 69.654.179 | 9,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.509,24 M€ (1.509.239.704 €) · 1 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. Y DISCAP. | 1.509.239.704 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 192,85 M€ (192.851.292 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA | 192.851.292 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 7,87 M€ (7.873.415 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES | 7.873.415 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,50 M€ (5.499.362 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS | 5.499.362 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 136,12 M€ (136.124.125 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN TURÍSTICA | 73.686.028 | 54,1 % |
| `11E` | D.S.G. TURISMO, REGENERACIÓN, JUSTICIA Y ADMON.LOC | 49.434.298 | 36,3 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL TURISMO | 13.003.799 | 9,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 135,37 M€ (135.373.478 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12P` | D.S.G. IGUALDAD, POLÍTICAS SOCIALES Y CONCILIACIÓN | 133.337.744 | 98,5 % |
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE GÉNERO | 2.035.734 | 1,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.890,20 M€ · 55 códigos · 33,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y AMORTIZACIÓN D. PUBLICA | 5.503.333.408 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS CON CC.LL. | 3.255.010.669 |
| `51B` | MOVILIDAD, INFRAESTRUCTURAS VIARIAS Y TRANSPORTES | 596.159.680 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA | 514.340.652 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA | 325.531.593 |
| `31P` | SERVICIO DE APOYO A FAMILIAS | 262.939.052 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN | 245.971.651 |
| `44E` | GESTIÓN DEL MEDIO NATURAL | 215.229.286 |
| `73A` | ORDENAC. ACTIVIDAD INDUSTRIAL, ENERGÉTICA Y MINERA | 194.439.038 |
| `44F` | INFORMACIÓN AMBIENTAL Y DINAMIZACIÓN SOC-ECO. SOST | 180.676.216 |
| `52C` | COMUNICACIÓN SOCIAL | 160.970.284 |
| `11A` | D.S.G. PRESIDENCIA, ADMON. PÚBLICA E INTERIOR | 112.930.996 |
| `61G` | GESTIÓN Y ADMINISTRACIÓN PATRIMONIO | 98.731.101 |
| `61L` | COORDINACIÓN DE LA HACIENDA DE LA COMUNI. AUTÓNOMA | 89.019.640 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS | 87.548.550 |
| `81A` | COOPERACIÓN ECONÓMICA Y COORDINACIÓN CON CC.LL. | 80.739.459 |
| `12O` | D.S.G. SALUD Y FAMILIAS | 74.777.849 |
| `63B` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 63.000.000 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO | 60.574.418 |
| `61I` | GESTIÓN DE TECNOLOGÍAS CORPORATIVAS | 55.804.887 |
| `12Q` | D.S.G. FOMENTO, INFRAES. Y ORDENACIÓN TERRITORIO | 49.539.270 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL | 48.843.071 |
| `32E` | PROYECTOS DE INTERÉS SOCIAL | 45.656.848 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL | 45.607.473 |
| `11B` | ACTIVIDAD LEGISLATIVA | 41.380.575 |
| … | *resto: 30 códigos* | 481.440.561 |

</details>

### 2021

*Fuente: `gastos_csv.csv` · 94 líneas · total extraído **39.750,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 11.453,59 M€ (11.453.591.430 €) · 4 códigos · 28,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACIÓN Y FINANCIACIÓN | 11.388.067.932 | 99,4 % |
| `41K` | POLÍTICA DE CALIDAD Y MODERNIZACIÓN | 31.935.867 | 0,3 % |
| `41D` | SALUD PÚBLICA Y PARTICIPACIÓN | 22.779.610 | 0,2 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS | 10.808.021 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 8.500,80 M€ (8.500.803.036 €) · 10 códigos · 21,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION PROFESIONAL | 3.242.708.708 | 38,1 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA | 2.121.099.828 | 25,0 % |
| `42J` | UNIVERSIDADES | 1.393.310.438 | 16,4 % |
| `12L` | D.S.G. DE EDUCACIÓN Y DEPORTE | 582.958.671 | 6,9 % |
| `42E` | EDUCACIÓN ESPECIAL | 426.064.293 | 5,0 % |
| `42F` | EDUCACIÓN COMPENSATORIA | 254.833.537 | 3,0 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL | 240.096.939 | 2,8 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA | 122.097.425 | 1,4 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS | 93.445.898 | 1,1 % |
| `42B` | FORMACIÓN DEL PROFESORADO | 24.187.299 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.824,01 M€ (2.824.012.606 €) · 6 códigos · 7,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y GANADERO | 1.730.951.141 | 61,3 % |
| `12M` | D.S.G. AGRIC., GANADERÍA, PESCA Y DESA. SOSTENIBLE | 536.054.668 | 19,0 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. AGRIC. Y GANAD. | 270.906.279 | 9,6 % |
| `71E` | INCENTIVACIÓN DEL SECTOR AGROINDUSTRIAL | 128.634.387 | 4,6 % |
| `71H` | DESARROLLO RURAL | 90.605.187 | 3,2 % |
| `71P` | PESCA | 66.860.944 | 2,4 % |

</details>

<details open><summary><b><code>vivienda</code> — 309,67 M€ (309.672.280 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO | 287.076.392 | 92,7 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y URBANISMO | 22.595.888 | 7,3 % |

</details>

<details open><summary><b><code>empleo</code> — 1.245,39 M€ (1.245.388.445 €) · 6 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12J` | D.S.G. EMPLEO, FORMACIÓN Y TRABAJO AUTÓNOMO | 806.230.899 | 64,7 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO | 214.807.519 | 17,2 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL | 103.298.981 | 8,3 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES LABORALES | 92.040.096 | 7,4 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL | 25.419.254 | 2,0 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES LABORALES | 3.591.696 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 433,67 M€ (433.671.834 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN | 345.943.274 | 79,8 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA | 58.693.251 | 13,5 % |
| `72A` | EMPRESA, EMPRENDI. INNOVADOR Y ECONOMÍA DIGITAL | 29.035.309 | 6,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.610,00 M€ (1.610.002.176 €) · 1 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. Y DISCAP. | 1.610.002.176 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 194,33 M€ (194.332.129 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA | 194.332.129 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,64 M€ (31.641.238 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES | 31.641.238 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,02 M€ (4.023.798 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS | 4.023.798 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 138,38 M€ (138.375.113 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN TURÍSTICA | 85.418.977 | 61,7 % |
| `11E` | D.S.G. TURISMO, REGENERACIÓN, JUSTICIA Y ADMON.LOC | 37.239.951 | 26,9 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL TURISMO | 15.716.185 | 11,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 140,30 M€ (140.301.532 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12P` | D.S.G. IGUALDAD, POLÍTICAS SOCIALES Y CONCILIACIÓN | 138.181.989 | 98,5 % |
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE GÉNERO | 2.119.543 | 1,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.864,81 M€ · 54 códigos · 32,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y AMORTIZACIÓN D. PUBLICA | 4.787.945.466 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS CON CC.LL. | 3.265.063.612 |
| `51B` | MOVILIDAD, INFRAESTRUCTURAS VIARIAS Y TRANSPORTES | 642.256.350 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA | 526.475.509 |
| `63B` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 489.275.599 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA | 356.231.973 |
| `44E` | GESTIÓN DEL MEDIO NATURAL | 270.899.605 |
| `12N` | D.S.G. TRANSF. ECÓNOM. , INDUSTRIA, CONOC. Y UNIV. | 265.971.118 |
| `11A` | D.S.G. PRESIDENCIA, ADMON. PÚBLICA E INTERIOR | 259.330.875 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN | 237.619.143 |
| `31P` | SERVICIO DE APOYO A FAMILIAS | 233.278.823 |
| `73A` | ORDENAC. ACTIVIDAD ENERGÉTICA | 170.074.882 |
| `52C` | COMUNICACIÓN SOCIAL | 161.597.374 |
| `61L` | COORDINACIÓN DE LA HACIENDA DE LA COMUNI. AUTÓNOMA | 93.629.435 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS | 88.106.358 |
| `61G` | GESTIÓN Y ADMINISTRACIÓN PATRIMONIO | 82.532.806 |
| `81A` | COOPERACIÓN ECONÓMICA Y COORDINACIÓN CON CC.LL. | 73.432.652 |
| `12Q` | D.S.G. FOMENTO, INFRAES. Y ORDENACIÓN TERRITORIO | 54.641.570 |
| `12O` | D.S.G. SALUD Y FAMILIAS | 54.099.174 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL | 52.788.870 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO | 52.194.571 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL | 50.143.443 |
| `32E` | PROYECTOS DE INTERÉS SOCIAL | 45.752.848 |
| `11B` | ACTIVIDAD LEGISLATIVA | 42.562.910 |
| `12K` | D.S.G. HACIENDA Y FINANCIACIÓN EUROPEA | 39.629.040 |
| … | *resto: 29 códigos* | 469.274.396 |

</details>

### 2022

*Fuente: `memoria_programas.pdf` · 104 líneas · total extraído **39.923,76 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 12.214,50 M€ (12.214.500.940 €) · 5 códigos · 30,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | PLANIFICACIÓN Y FINANCIACIÓN 1.123.742 12.028.267.744 12.029.391.486 56.736.120 56.736.120 | 12.086.127.606 | 98,9 % |
| `41H` | D.S.G. SALUD Y FAMILIAS 44.720.176 8.468.010 30.000 53.218.186 496.957 496.957 | 53.715.143 | 0,4 % |
| `41K` | POLÍTICA DE CALIDAD Y MODERNIZACIÓN 3.238.118 1.656.000 19.842.259 24.736.377 1.305.119 9.802.411 11.107.530 | 35.843.907 | 0,3 % |
| `41D` | SALUD PÚBLICA Y PARTICIPACIÓN 20.494.893 4.770.267 2.072.646 27.337.806 175.000 106.898 281.898 | 27.619.704 | 0,2 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS 11.044.580 110.000 11.154.580 40.000 40.000 | 11.194.580 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 8.744,58 M€ (8.744.579.745 €) · 10 códigos · 21,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION 2.566.644.386 104.124.001 45.000 529.340.665 3.200.154.052 1.411.081 1.411.081 | 3.201.565.133 | 36,6 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA 1.769.262.772 15.839.665 18.000 389.860.310 2.174.980.747 | 2.174.980.747 | 24,9 % |
| `42J` | UNIVERSIDADES 1.811.330 67.058 58.700 1.408.394.365 1.410.331.453 1.915.033 155.210.232 157.125.265 4.555.642 4.555.642 | 1.572.012.360 | 18,0 % |
| `12L` | D.S.G. DE EDUCACIÓN Y DEPORTE 81.586.339 6.049.465 2.000 398.142.097 485.779.901 765.366 74.850.725 75.616.091 | 561.395.992 | 6,4 % |
| `42E` | EDUCACIÓN ESPECIAL 307.507.079 282.704 6.000 125.419.825 433.215.608 102.000 102.000 | 433.317.608 | 5,0 % |
| `42F` | EDUCACIÓN COMPENSATORIA 194.980.680 22.817.726 2.500 87.659.418 305.460.324 | 305.460.324 | 3,5 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 247.911.803 4.578.741 2.000 371.535 252.864.079 | 252.864.079 | 2,9 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA 114.909.951 5.189.923 5.000 120.104.874 346.760 346.760 | 120.451.634 | 1,4 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS 96.400.211 1.469.856 500 450 97.871.017 | 97.871.017 | 1,1 % |
| `42B` | FORMACIÓN DEL PROFESORADO 19.127.143 5.533.708 24.660.851 | 24.660.851 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.822,72 M€ (2.822.716.779 €) · 7 códigos · 7,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 1.568.240.000 1.568.240.000 20.000 20.000 | 1.568.260.000 | 55,6 % |
| `12M` | D.S.G. AGRIC., GANADERÍA, PESCA Y DESA. 130.677.634 31.810.497 229.000 339.869.278 502.586.409 9.946.615 57.772.503 67.719.118 | 570.305.527 | 20,2 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. 5.752.107 3.718.891 12.225.651 21.696.649 56.735.613 209.645.615 266.381.228 | 288.077.877 | 10,2 % |
| `71E` | INCENTIVACIÓN DEL SECTOR 3.569.068 912.500 4.481.568 17.410.478 117.926.253 135.336.731 | 139.818.299 | 5,0 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 9.333.630 5.392.866 250.000 55.000 15.031.496 6.541.108 107.149.409 113.690.517 | 128.722.013 | 4,6 % |
| `71P` | PESCA 3.051.024 4.774.035 7.825.059 3.590.999 56.468.313 60.059.312 | 67.884.371 | 2,4 % |
| `71H` | DESARROLLO RURAL 1.609.723 106.000 12.174.660 13.890.383 96.398 45.661.911 45.758.309 | 59.648.692 | 2,1 % |

</details>

<details open><summary><b><code>vivienda</code> — 246,78 M€ (246.777.546 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO 15.284.638 135.000 50.000 37.184.211 52.653.849 3.032.143 127.275.323 130.307.466 1.100 40.000.000 40.001.100 | 222.962.415 | 90,3 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y 13.290.729 2.963.486 64.800 16.319.015 6.636.116 860.000 7.496.116 | 23.815.131 | 9,7 % |

</details>

<details open><summary><b><code>empleo</code> — 929,48 M€ (929.484.859 €) · 6 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12J` | D.S.G. EMPLEO, FORMACIÓN Y TRABAJO 42.101.964 9.716.081 45.500 467.287.323 519.150.868 5.519.866 29.443.510 34.963.376 | 554.114.244 | 59,6 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO 27.950.686 53.623.452 25.500 89.877.588 171.477.226 6.578.306 11.391.902 17.970.208 | 189.447.434 | 20,4 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL 7.498.403 315.000 62.828.983 70.642.386 625.000 32.765.085 33.390.085 | 104.032.471 | 11,2 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES 27.185.038 2.840.927 20.000 16.408.544 46.454.509 1.325.250 5.696.131 7.021.381 | 53.475.890 | 5,8 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL 7.541.014 198.000 2.169.800 9.908.814 4.398.455 10.610.144 15.008.599 | 24.917.413 | 2,7 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES 1.857.016 1.574.191 3.431.207 66.200 66.200 | 3.497.407 | 0,4 % |

</details>

<details open><summary><b><code>idi</code> — 278,32 M€ (278.322.080 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN 2.464.637 922.717 1.237.440 12.829.382 17.454.176 4.290.794 113.474.450 117.765.244 22.192.440 22.192.440 | 157.411.860 | 56,6 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA 38.175.865 19.671.367 500 11.039.209 68.886.941 14.680.653 460.280 15.140.933 | 84.027.874 | 30,2 % |
| `72A` | EMPRESA, EMPRENDI. INNOVADOR Y 6.670.758 3.449.023 1.455.364 11.575.145 6.469.328 18.837.873 25.307.201 | 36.882.346 | 13,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.762,58 M€ (1.762.584.911 €) · 1 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. 151.157.385 26.237.158 30.000 1.570.941.286 1.748.365.829 11.942.507 2.276.575 14.219.082 | 1.762.584.911 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 203,12 M€ (203.115.125 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA 57.277.455 102.512.409 30.900 40.615.209 200.435.973 2.679.152 2.679.152 | 203.115.125 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 32,33 M€ (32.325.730 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES 4.156.995 10.961.777 16.903.958 32.022.730 303.000 303.000 | 32.325.730 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,74 M€ (3.741.220 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS 1.214.220 192.000 1.215.000 2.621.220 120.000 1.000.000 1.120.000 | 3.741.220 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 158,42 M€ (158.420.836 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN 7.879.840 40.181 31.178.856 39.098.877 4.373.206 52.373.162 56.746.368 | 95.845.245 | 60,5 % |
| `11E` | D.S.G. TURISMO, REGENERACIÓN, JUSTICIA Y 23.297.195 11.888.508 35.185.703 4.935.851 4.935.851 | 40.121.554 | 25,3 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL 2.620.922 149.001 3.695.418 6.465.341 564.365 15.424.331 15.988.696 | 22.454.037 | 14,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 161,16 M€ (161.160.733 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12P` | D.S.G. IGUALDAD, POLÍTICAS SOCIALES Y 79.612.037 15.699.179 9.100 61.745.853 157.066.169 1.321.499 836.502 2.158.001 | 159.224.170 | 98,8 % |
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE 702.107 654.456 580.000 1.936.563 | 1.936.563 | 1,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.366,03 M€ · 62 códigos · 31,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y 731.143 404.988.681 405.719.824 4.658.234.951 4.658.234.951 | 5.063.954.775 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 2.749.951.739 2.749.951.739 4.412.773 4.412.773 | 2.754.364.512 |
| `51B` | MOVILIDAD, INFRAESTRUCTURAS VIARIAS Y 33.181.005 2.552.013 1.984.619 210.031.864 247.749.501 270.438.901 111.488.516 381.927.417 | 629.676.918 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA 374.284.775 94.945.771 49.544.400 518.774.946 26.448.426 26.448.426 | 545.223.372 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 510.000.000 510.000.000 | 510.000.000 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 31.995.427 13.358.435 1.500.000 46.853.862 306.514.697 962.000 307.476.697 | 354.330.559 |
| `44E` | GESTIÓN DEL MEDIO NATURAL 27.250.397 3.317.175 500.000 1.092.772 32.160.344 185.734.616 64.638.347 250.372.963 | 282.533.307 |
| `11A` | D.S.G. PRESIDENCIA, ADMON. PÚBLICA E 69.722.040 19.798.519 100.099.573 189.620.132 6.565.255 62.309.276 68.874.531 | 258.494.663 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 3.249.735 3.710.659 180.112.172 187.072.566 2.288.724 2.288.724 | 189.361.290 |
| `52C` | COMUNICACIÓN SOCIAL 2.048.422 2.017.457 141.080.787 145.146.666 16.072.441 3.490.000 19.562.441 | 164.709.107 |
| `12N` | D.S.G. TRANSF. ECÓNOM. , INDUSTRIA, CONOC. 9.180.536 3.661.828 4.550 29.898.050 42.744.964 2.495.558 104.621.018 107.116.576 | 149.861.540 |
| `31P` | SERVICIO DE APOYO A FAMILIAS 53.771.503 58.576.173 112.347.676 | 112.347.676 |
| `73A` | ORDENACIÓN ACTIVIDAD ENERGÉTICA 9.554.387 732.512 9.689.988 19.976.887 4.312.030 85.216.190 89.528.220 | 109.505.107 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS 7.838.230 84.383.889 450.000 92.672.119 120.000 120.000 | 92.792.119 |
| `61L` | COORDINACIÓN DE LA HACIENDA DE LA 2.389.684 1.297.801 76.518.350 80.205.835 5.120.000 5.120.000 | 85.325.835 |
| `61G` | GESTIÓN Y ADMINISTRACIÓN PATRIMONIO 64.743.718 120.000 64.863.718 4.298.745 4.298.745 | 69.162.463 |
| `31P` | SERVICIO DE APOYO A FAMILIAS 1.773.083 54.415.671 10.674.088 66.862.842 71.000 71.000 | 66.933.842 |
| `81A` | COOPERACIÓN ECONÓMICA Y COORDINACIÓN 5.619.360 70.000 4.165.000 9.854.360 288.654 49.970.311 50.258.965 | 60.113.325 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO 18.652.535 553.757 21.598.171 40.804.463 6.870.386 8.419.814 15.290.200 | 56.094.663 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL 10.960.325 190.000 209.419 11.359.744 39.274.905 39.274.905 | 50.634.649 |
| `12Q` | D.S.G. FOMENTO, INFRAES. Y ORDENACIÓN 35.964.170 9.170.028 96.103 45.230.301 5.187.024 5.187.024 | 50.417.325 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL 18.022.595 23.960.905 1.815.665 43.799.165 5.894.446 500.000 6.394.446 | 50.193.611 |
| `12R` | D.S.G. CULTURA Y PATRIMONIO HISTÓRICO 24.684.437 6.809.274 25.000 7.226.467 38.745.178 6.587.882 760.227 7.348.109 | 46.093.287 |
| `32E` | PROYECTOS DE INTERÉS SOCIAL 258.000 37.403.848 37.661.848 8.200.000 8.200.000 | 45.861.848 |
| `11B` | ACTIVIDAD LEGISLATIVA 21.527.300 8.349.450 1.900 11.343.790 41.222.440 1.190.470 1.190.470 150.000 150.000 | 42.562.910 |
| … | *resto: 37 códigos* | 525.481.051 |

</details>

### 2023

*Fuente: `memoria_programas.pdf` · 105 líneas · total extraído **44.671,75 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 13.644,94 M€ (13.644.937.026 €) · 4 códigos · 30,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | DIRECCIÓN Y SERVICIOS GENERALES 49.219.428 8.411.966 30.000 13.036.738.280 13.094.399.674 1.816.957 414.228.055 416.045.012 | 13.510.444.686 | 99,0 % |
| `41D` | SALUD PÚBLICA 22.969.581 58.308.873 10.960.027 92.238.481 996.000 77.773 1.073.773 | 93.312.254 | 0,7 % |
| `41K` | POLÍTICA DE CALIDAD Y MODERNIZACIÓN 3.388.890 1.656.000 20.439.952 25.484.842 4.010.656 4.010.656 | 29.495.498 | 0,2 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS 11.534.588 110.000 11.644.588 40.000 40.000 | 11.684.588 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 8.808,59 M€ (8.808.586.626 €) · 9 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION 2.758.177.447 187.755.611 45.000 586.437.977 3.532.416.035 3.480.544 3.480.544 | 3.535.896.579 | 40,1 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA 1.819.503.185 21.698.429 18.000 415.396.050 2.256.615.664 | 2.256.615.664 | 25,6 % |
| `42J` | UNIVERSIDADES 1.526.118 1.585.029 44.333 1.467.828.177 1.470.983.657 768.499 155.210.232 155.978.731 4.584.176 4.584.176 | 1.631.546.564 | 18,5 % |
| `42E` | EDUCACIÓN ESPECIAL 324.231.625 567.270 6.000 139.861.461 464.666.356 32.021 32.021 | 464.698.377 | 5,3 % |
| `42F` | EDUCACIÓN COMPENSATORIA 191.099.430 29.939.469 2.500 124.041.403 345.082.802 28.665 28.665 | 345.111.467 | 3,9 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 260.997.882 12.376.268 2.000 371.535 273.747.685 91.735 91.735 | 273.839.420 | 3,1 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA 114.764.997 5.284.346 5.000 120.054.343 52.578.904 52.578.904 | 172.633.247 | 2,0 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS 99.670.832 2.474.974 500 450 102.146.756 | 102.146.756 | 1,2 % |
| `42B` | FORMACIÓN DEL PROFESORADO 19.881.285 6.217.267 26.098.552 | 26.098.552 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.459,66 M€ (2.459.663.807 €) · 6 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 1.569.240.000 1.569.240.000 20.000 20.000 | 1.569.260.000 | 63,8 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. 8.892.222 2.805.000 12.632.235 24.329.457 101.918.196 287.362.265 389.280.461 | 413.609.918 | 16,8 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 9.644.100 6.042.758 250.000 15.936.858 7.410.666 169.219.634 176.630.300 | 192.567.158 | 7,8 % |
| `71E` | INCENTIVACIÓN DEL SECTOR 4.420.614 1.874.200 6.294.814 30.848.483 107.008.280 137.856.763 | 144.151.577 | 5,9 % |
| `71P` | PESCA 4.512.932 15.897.549 20.410.481 2.122.359 49.122.277 51.244.636 | 71.655.117 | 2,9 % |
| `71H` | DESARROLLO RURAL 1.506.123 106.000 9.433.034 11.045.157 248.501 57.126.379 57.374.880 | 68.420.037 | 2,8 % |

</details>

<details open><summary><b><code>vivienda</code> — 418,60 M€ (418.602.732 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO 16.563.268 135.000 50.000 77.244.708 93.992.976 3.587.185 257.441.060 261.028.245 43.000.000 43.000.000 | 398.021.221 | 95,1 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y 13.338.198 3.143.552 10.800 16.492.550 3.228.961 860.000 4.088.961 | 20.581.511 | 4,9 % |

</details>

<details open><summary><b><code>empleo</code> — 696,43 M€ (696.433.298 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32K` | POLÍTICAS ACTIVAS DE EMPLEO 7.978.536 261.609.367 269.587.903 1.523.790 1.523.790 | 271.111.693 | 38,9 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO 32.410.791 80.231.401 75.500 127.526.840 240.244.532 10.928.576 856.452 11.785.028 | 252.029.560 | 36,2 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL 9.500.578 83.000 5.000 31.715.286 41.303.864 225.000 45.810.579 46.035.579 | 87.339.443 | 12,5 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES 27.401.839 2.780.927 10.000 17.255.357 47.448.123 1.325.250 4.929.028 6.254.278 | 53.702.401 | 7,7 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL 8.349.787 681.973 2.150.000 11.181.760 3.332.122 14.242.108 17.574.230 | 28.755.990 | 4,1 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES 1.920.820 1.524.191 3.445.011 49.200 49.200 | 3.494.211 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 359,53 M€ (359.531.438 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN 4.377.358 2.164.355 972.652 11.821.326 19.335.691 508.103 177.472.173 177.980.276 22.457.228 22.457.228 | 219.773.195 | 61,1 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA 20.149.778 29.996.712 500 11.767.607 61.914.597 21.974.795 460.280 22.435.075 | 84.349.672 | 23,5 % |
| `72A` | INNOVACIÓN Y EMPRENDIMIENTO 7.242.560 1.046.414 37.251.125 45.540.099 2.087.412 7.781.060 9.868.472 | 55.408.571 | 15,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.041,97 M€ (2.041.969.111 €) · 1 códigos · 4,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. 154.641.574 26.877.221 30.000 1.723.309.347 1.904.858.142 58.395.596 78.715.373 137.110.969 | 2.041.969.111 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 222,48 M€ (222.481.616 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA 59.119.146 107.478.256 30.900 45.496.964 212.125.266 10.356.350 10.356.350 | 222.481.616 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 33,17 M€ (33.167.180 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES 4.294.056 10.984.898 17.770.226 33.049.180 118.000 118.000 | 33.167.180 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,58 M€ (10.579.800 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS 1.344.570 4.613.380 3.501.850 9.459.800 120.000 1.000.000 1.120.000 | 10.579.800 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 198,63 M€ (198.628.819 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN 8.778.082 4.000 28.753.850 37.535.932 5.289.259 145.430.912 150.720.171 | 188.256.103 | 94,8 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL 2.298.122 113.059 3.655.418 6.066.599 582.745 3.723.372 4.306.117 | 10.372.716 | 5,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,33 M€ (2.327.667 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE 655.092 892.575 780.000 2.327.667 | 2.327.667 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 15.774,84 M€ · 68 códigos · 35,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y 731.143 530.183.920 530.915.063 4.633.261.267 4.633.261.267 | 5.164.176.330 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 2.949.951.739 2.949.951.739 3.000.000 3.000.000 | 2.952.951.739 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 123.416.581 6.519.068 2.000 433.704.991 563.642.640 718.069 513.275.884 513.993.953 | 1.077.636.593 |
| `51B` | MOVILIDAD, INFRAESTRUCTURAS VIARIAS Y 35.754.993 2.678.358 1.846.469 225.014.240 265.294.060 562.523.942 188.165.288 750.689.230 | 1.015.983.290 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA 390.525.278 114.919.285 49.416.522 554.861.085 36.372.446 36.372.446 | 591.233.531 |
| `44E` | GESTIÓN DEL MEDIO NATURAL 30.223.858 2.498.267 200.000 197.339.341 230.261.466 202.269.024 94.920.687 297.189.711 | 527.451.177 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 32.625.593 13.309.757 1.500.000 47.435.350 379.138.806 7.416.000 386.554.806 | 433.990.156 |
| `11A` | D.S.G. PRESIDENCIA, INT.,DIALOGO SOC. Y 74.317.791 21.078.879 200.000 116.534.748 212.131.418 6.904.369 193.655.497 200.559.866 | 412.691.284 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 42.999.809 12.211.609 55.500 297.886.533 353.153.451 5.837.048 23.520.542 29.357.590 | 382.511.041 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 71.455.679 26.116.866 114.500 169.940.643 267.627.688 6.987.558 59.771.550 66.759.108 | 334.386.796 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 28.759.184 8.966.482 45.333.639 83.059.305 784.745 220.134.089 220.918.834 | 303.978.139 |
| `73A` | ORDENACIÓN ACTIVIDAD ENERGÉTICA 12.771.850 437.815 11.644.205 24.853.870 1.754.313 206.188.477 207.942.790 | 232.796.660 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 4.397.697 4.760.016 181.650.689 190.808.402 1.713.207 4.323.365 6.036.572 | 196.844.974 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 88.898.697 19.743.705 9.100 57.447.372 166.098.874 8.301.377 12.100.308 20.401.685 | 186.500.559 |
| `52C` | COMUNICACIÓN SOCIAL 2.104.100 3.011.788 151.421.643 156.537.531 14.278.260 2.772.558 17.050.818 | 173.588.349 |
| `31P` | APOYO A FAMILIAS 91.260.543 69.744.672 161.005.215 | 161.005.215 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 68.249.673 19.559.261 114.500 103.456 88.026.890 13.879.752 29.679.996 43.559.748 | 131.586.638 |
| `61K` | COORDINACIÓN DE FONDOS EUROPEOS 8.086.613 32.953.470 41.040.083 14.899.197 14.899.197 75.000.000 75.000.000 | 130.939.280 |
| `73B` | ORDENACIÓN ACTIVIDAD INDUSTRIAL Y 10.685.014 940.380 3.005.685 14.631.079 20.461.617 90.650.069 111.111.686 | 125.742.765 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS 3.102.530 83.746.467 450.000 87.298.997 100.000 100.000 | 87.398.997 |
| `61G` | GESTIÓN Y ADMINISTRACIÓN PATRIMONIO 70.909.265 120.000 71.029.265 16.133.460 16.133.460 | 87.162.725 |
| `61L` | COORDINACIÓN DE LA HACIENDA DE LA 2.315.807 1.630.686 82.693.843 86.640.336 120.000 120.000 | 86.760.336 |
| `81A` | COOPERACIÓN ECONÓMICA Y COORDINACIÓN 5.684.366 35.000 3.105.000 8.824.366 337.534 71.077.320 71.414.854 | 80.239.220 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL 11.000.274 16.800 209.419 11.226.493 31.603.942 23.766.780 55.370.722 | 66.597.215 |
| `45H` | INDUSTRIAS CREATIVAS Y DEL LIBRO 19.802.581 1.031.452 23.109.122 43.943.155 9.867.209 8.004.146 17.871.355 | 61.814.510 |
| … | *resto: 43 códigos* | 768.872.323 |

</details>

### 2024

*Fuente: `memoria_programas.pdf` · 105 líneas · total extraído **45.740,39 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 14.055,56 M€ (14.055.560.408 €) · 4 códigos · 30,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | DIRECCIÓN Y SERVICIOS GENERALES 49.845.844 8.915.472 34.326 13.313.368.641 13.372.164.283 963.695 545.761.987 546.725.682 | 13.918.889.965 | 99,0 % |
| `41D` | SALUD PÚBLICA 19.649.973 59.521.856 10.626.655 89.798.484 3.261.305 527.773 3.789.078 | 93.587.562 | 0,7 % |
| `41K` | POLÍTICA DE CALIDAD Y MODERNIZACIÓN 3.495.662 1.643.424 20.567.540 25.706.626 5.143.618 5.143.618 | 30.850.244 | 0,2 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS 12.135.460 57.177 12.192.637 40.000 40.000 | 12.232.637 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 9.319,09 M€ (9.319.094.156 €) · 9 códigos · 20,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION 2.947.224.277 197.930.105 45.000 610.238.046 3.755.437.428 8.225.851 8.225.851 | 3.763.663.279 | 40,4 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA 1.895.728.873 23.378.301 18.000 426.804.701 2.345.929.875 | 2.345.929.875 | 25,2 % |
| `42J` | UNIVERSIDADES 1.787.165 10.000 29.762 1.536.171.256 1.537.998.183 155.260.232 155.260.232 2.965.581 2.965.581 | 1.696.223.996 | 18,2 % |
| `42E` | EDUCACIÓN ESPECIAL 383.471.976 496.330 6.000 146.175.348 530.149.654 | 530.149.654 | 5,7 % |
| `42F` | EDUCACIÓN COMPENSATORIA 276.161.255 27.128.984 2.500 93.470.126 396.762.865 33.333 33.333 | 396.796.198 | 4,3 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 282.836.970 11.103.494 2.000 371.535 294.313.999 106.667 106.667 | 294.420.666 | 3,2 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA 118.498.852 4.701.253 5.000 123.205.105 32.550.073 32.550.073 | 155.755.178 | 1,7 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS 103.480.774 2.307.841 500 450 105.789.565 | 105.789.565 | 1,1 % |
| `42B` | FORMACIÓN DEL PROFESORADO 20.793.439 9.572.306 30.365.745 | 30.365.745 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.596,56 M€ (2.596.558.672 €) · 6 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 1.569.240.000 1.569.240.000 20.000 20.000 | 1.569.260.000 | 60,4 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. 11.933.280 3.392.000 25.000 16.756.789 32.107.069 98.689.006 404.438.553 503.127.559 | 535.234.628 | 20,6 % |
| `71E` | INCENTIVACIÓN DEL SECTOR 5.073.487 1.758.829 6.832.316 20.196.787 149.350.322 169.547.109 | 176.379.425 | 6,8 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 14.250.159 5.846.432 250.000 20.346.591 6.666.187 128.100.262 134.766.449 | 155.113.040 | 6,0 % |
| `71H` | DESARROLLO RURAL 3.652.971 112.000 20.000 23.087.004 26.871.975 90.813.202 90.813.202 | 117.685.177 | 4,5 % |
| `71P` | PESCA 3.935.045 120.000 18.940.500 22.995.545 3.150.857 16.740.000 19.890.857 | 42.886.402 | 1,7 % |

</details>

<details open><summary><b><code>vivienda</code> — 448,24 M€ (448.235.300 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO 18.134.314 50.000 60.075.714 78.260.028 929.476 298.894.887 299.824.363 50.000.000 50.000.000 | 428.084.391 | 95,5 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y 13.094.061 3.520.056 16.614.117 2.856.792 680.000 3.536.792 | 20.150.909 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 781,22 M€ (781.223.880 €) · 6 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32K` | POLÍTICAS ACTIVAS DE EMPLEO 13.034.876 10.000 320.469.908 333.514.784 1.800.000 1.800.000 | 335.314.784 | 42,9 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO 34.949.564 65.471.979 75.500 163.323.136 263.820.179 15.000.423 8.268.252 23.268.675 | 287.088.854 | 36,7 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL 12.925.626 284.647 25.514.000 38.724.273 125.000 41.376.884 41.501.884 | 80.226.157 | 10,3 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES 28.308.288 1.333.555 5.000 15.268.118 44.914.961 1.529.250 4.880.410 6.409.660 | 51.324.621 | 6,6 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL 9.562.690 603.879 2.730.000 12.896.569 1.154.000 9.597.677 10.751.677 | 23.648.246 | 3,0 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES 1.989.827 1.524.191 41.000 3.555.018 66.200 66.200 | 3.621.218 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 362,24 M€ (362.235.848 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN 4.427.789 673.875 704.603 14.227.053 20.033.320 31.114 118.391.174 118.422.288 22.025.350 22.025.350 | 160.480.958 | 44,3 % |
| `72A` | INNOVACIÓN Y EMPRENDIMIENTO 1.574.427 720.597 39.271.489 41.566.513 2.703.269 59.509.951 62.213.220 | 103.779.733 | 28,6 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA 16.925.747 19.020.153 500 13.018.621 48.965.021 24.937.815 24.937.815 | 73.902.836 | 20,4 % |
| `45H` | TUTELA, INVESTIGACIÓN Y DIFUSIÓN 20.822.024 100.000 1.008.752 21.930.776 1.275.774 865.771 2.141.545 | 24.072.321 | 6,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.229,59 M€ (2.229.589.384 €) · 1 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. 156.291.105 31.752.398 30.000 1.892.139.891 2.080.213.394 74.164.698 75.211.292 149.375.990 | 2.229.589.384 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 252,38 M€ (252.376.683 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA 58.804.041 122.108.168 30.900 50.115.070 231.058.179 13.421.504 7.897.000 21.318.504 | 252.376.683 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 33,80 M€ (33.795.836 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES 4.537.361 11.524.918 17.499.557 33.561.836 234.000 234.000 | 33.795.836 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,62 M€ (10.622.729 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS 1.369.873 4.612.006 4.480.850 10.462.729 160.000 160.000 | 10.622.729 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 177,17 M€ (177.174.289 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN 8.181.936 86.780 28.968.121 37.236.837 94.808.023 94.808.023 | 132.044.860 | 74,5 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL 2.297.252 116.862 3.844.766 6.258.880 9.000 38.861.549 38.870.549 | 45.129.429 | 25,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,31 M€ (2.309.609 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE 650.034 769.575 890.000 2.309.609 | 2.309.609 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 15.471,61 M€ · 67 códigos · 33,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y 776.143 717.613.347 718.389.490 3.419.017.277 3.419.017.277 | 4.137.406.767 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 3.149.951.739 3.149.951.739 3.000.000 3.000.000 | 3.152.951.739 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 112.344.188 6.289.311 2.000 506.588.889 625.224.388 1.200.000 344.604.688 345.804.688 | 971.029.076 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS DEL 15.710.073 1.705.592 60.000 231.263.208 248.738.873 341.607.925 174.776.696 516.384.621 | 765.123.494 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA 416.271.357 104.556.449 53.172.000 573.999.806 72.921.750 72.921.750 | 646.921.556 |
| `44E` | GESTIÓN DEL MEDIO NATURAL 32.797.096 2.642.402 450.000 202.976.909 238.866.407 257.297.391 140.127.386 397.424.777 | 636.291.184 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 39.070.152 12.979.084 1.539.500 53.588.736 415.523.748 10.829.500 426.353.248 | 479.941.984 |
| `11A` | D.S.G. PRESIDENCIA, INT.,DIALOGO SOC. Y 72.530.380 14.548.444 200.000 194.191.898 281.470.722 1.864.641 187.142.547 189.007.188 | 470.477.910 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 45.177.173 10.721.282 25.000 360.463.865 416.387.320 6.623.050 24.813.500 31.436.550 | 447.823.870 |
| `61G` | GESTIÓN Y ADMINISTRACIÓN PATRIMONIO 39.532.920 50.000 39.582.920 354.118.466 354.118.466 | 393.701.386 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 72.514.980 33.478.205 30.000 183.392.847 289.416.032 8.217.408 49.304.616 57.522.024 | 346.938.056 |
| `51A` | INFRAESTRUCTURAS VIARIAS 20.151.722 1.674.422 1.796.469 23.622.613 227.933.704 227.933.704 | 251.556.317 |
| `61K` | COORDINACIÓN DE FONDOS EUROPEOS 10.006.543 55.932.312 65.938.855 8.676.645 8.676.645 175.000.000 175.000.000 | 249.615.500 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 4.171.391 29.754.746 176.004.175 209.930.312 | 209.930.312 |
| `31P` | APOYO A FAMILIAS 5.894.187 106.055.116 71.907.184 183.856.487 | 183.856.487 |
| `52C` | COMUNICACIÓN SOCIAL 2.225.216 2.975.738 160.588.874 165.789.828 14.128.260 3.215.510 17.343.770 | 183.133.598 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 93.714.422 11.788.826 9.100 62.892.163 168.404.511 4.013.886 2.455.855 6.469.741 | 174.874.252 |
| `61B` | POLÍTICA ECONÓMICA Y FINANCIERA Y 1.935.114 15.257 57.891.570 59.841.941 364.188 113.308.748 113.672.936 | 173.514.877 |
| `73B` | ORDENACIÓN ACTIVIDAD INDUSTRIAL Y 17.079.930 673.322 600.000 18.353.252 15.853.327 92.749.422 108.602.749 | 126.956.001 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 93.910.681 12.599.555 114.500 106.624.736 15.972.672 1.000.000 16.972.672 | 123.597.408 |
| `73A` | ORDENACIÓN ACTIVIDAD ENERGÉTICA 13.628.194 586.932 15.978.972 30.194.098 222.105 89.184.406 89.406.511 | 119.600.609 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL 10.987.970 49.638 235.072 11.272.680 21.304.076 68.276.651 89.580.727 | 100.853.407 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS 3.109.666 85.946.169 468.000 89.523.835 340.000 340.000 | 89.863.835 |
| `81A` | COOPERACIÓN ECONÓMICA Y COORDINACIÓN 6.157.816 54.000 3.105.000 9.316.816 2.450.573 70.702.739 73.153.312 | 82.470.128 |
| `61L` | COORDINACIÓN DE LA HACIENDA DE LA C. 2.335.879 1.618.687 77.255.626 81.210.192 120.000 120.000 | 81.330.192 |
| … | *resto: 42 códigos* | 871.852.999 |

</details>

### 2025

*Fuente: `memoria_programas.pdf` · 107 líneas · total extraído **48.384,98 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 15.041,54 M€ (15.041.542.563 €) · 3 códigos · 31,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | DIRECCIÓN Y SERVICIOS GENERALES 49.114.621 7.137.246 39.326 14.309.953.219 14.366.244.412 273.135 569.746.825 570.019.960 | 14.936.264.372 | 99,3 % |
| `41D` | SALUD PÚBLICA 20.869.272 59.774.443 9.643.725 90.287.440 2.486.000 2.486.000 | 92.773.440 | 0,6 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS 12.406.774 57.977 12.464.751 40.000 40.000 | 12.504.751 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 9.693,33 M€ (9.693.334.966 €) · 9 códigos · 20,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION 3.130.807.628 178.487.804 75.100 696.637.750 4.006.008.282 633.333 633.333 | 4.006.641.615 | 41,3 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA 1.968.497.486 25.459.198 30.040 460.778.235 2.454.764.959 100.000 100.000 | 2.454.864.959 | 25,3 % |
| `42J` | UNIVERSIDADES 1.934.451 24.653 14.986 1.576.809.153 1.578.783.243 158.210.232 158.210.232 1.059.790 1.059.790 | 1.738.053.265 | 17,9 % |
| `42E` | EDUCACIÓN ESPECIAL 408.426.735 525.218 10.013 137.956.492 546.918.458 | 546.918.458 | 5,6 % |
| `42F` | EDUCACIÓN COMPENSATORIA 239.523.203 27.354.891 4.172 93.602.784 360.485.050 66.667 66.667 | 360.551.717 | 3,7 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 299.829.788 14.201.405 3.338 415.452 314.449.983 281.934 281.934 | 314.731.917 | 3,2 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA 122.417.734 4.841.115 8.345 127.267.194 66.666 2.246.497 2.313.163 | 129.580.357 | 1,3 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS 108.606.736 2.229.125 834 550 110.837.245 | 110.837.245 | 1,1 % |
| `42B` | FORMACIÓN DEL PROFESORADO 21.898.751 9.256.682 31.155.433 | 31.155.433 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 2.628,58 M€ (2.628.577.595 €) · 6 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 1.568.700.395 1.568.700.395 | 1.568.700.395 | 59,7 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. 9.851.418 2.777.000 25.000 17.957.983 30.611.401 105.296.135 328.998.753 434.294.888 | 464.906.289 | 17,7 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 12.078.830 5.846.432 250.000 18.175.262 5.670.421 185.546.887 191.217.308 | 209.392.570 | 8,0 % |
| `71E` | INCENTIVACIÓN DEL SECTOR 5.597.159 1.194.068 50.000 6.841.227 15.413.083 185.363.102 200.776.185 | 207.617.412 | 7,9 % |
| `71H` | DESARROLLO RURAL 1.750.087 119.000 20.000 16.988.807 18.877.894 108.054.165 108.054.165 | 126.932.059 | 4,8 % |
| `71P` | PESCA 3.925.870 33.000 21.043.000 25.001.870 2.832.000 23.195.000 26.027.000 | 51.028.870 | 1,9 % |

</details>

<details open><summary><b><code>vivienda</code> — 488,87 M€ (488.873.782 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO 16.864.460 1.705.325 50.000 45.571.581 64.191.366 969.576 350.031.569 351.001.145 50.000.000 50.000.000 | 465.192.511 | 95,2 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y 13.651.892 3.697.310 17.349.202 1.167.069 5.165.000 6.332.069 | 23.681.271 | 4,8 % |

</details>

<details open><summary><b><code>empleo</code> — 781,21 M€ (781.206.513 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32K` | POLÍTICAS ACTIVAS DE EMPLEO 9.893.037 5.000 297.885.067 307.783.104 3.509.015 3.509.015 | 311.292.119 | 39,8 % |
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO 36.120.073 39.639.006 32.000 194.827.765 270.618.844 7.978.161 4.975.000 12.953.161 | 283.572.005 | 36,3 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL 10.992.832 220.000 33.364.000 44.576.832 20.000 53.931.791 53.951.791 | 98.528.623 | 12,6 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES 29.940.646 8.420.635 50.000 14.227.627 52.638.908 975.250 4.880.410 5.855.660 | 58.494.568 | 7,5 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL 8.371.844 190.523 4.346.474 12.908.841 974.000 11.597.677 12.571.677 | 25.480.518 | 3,3 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES 2.219.229 1.572.191 41.260 3.832.680 6.000 6.000 | 3.838.680 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 443,42 M€ (443.415.578 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN 3.380.849 521.675 31.414.498 35.317.022 65.265 141.461.103 141.526.368 | 176.843.390 | 39,9 % |
| `72A` | INNOVACIÓN Y EMPRENDIMIENTO 1.740.893 771.260 40.903.139 43.415.292 1.000.000 48.545.285 49.545.285 | 92.960.577 | 21,0 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA 3.892.374 17.657.262 835 12.725.525 34.275.996 47.493.104 293.096 47.786.200 | 82.062.196 | 18,5 % |
| `45B` | INNOVACIÓN Y PROMOCIÓN CULTURAL 4.928.170 564.715 55.558.349 61.051.234 430.859 6.464.714 6.895.573 | 67.946.807 | 15,3 % |
| `45H` | TUTELA, INVESTIGACIÓN Y DIFUSIÓN 21.497.849 75.000 21.572.849 1.225.774 803.985 2.029.759 | 23.602.608 | 5,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.616,90 M€ (2.616.898.816 €) · 1 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. 166.474.871 30.644.852 30.000 2.293.987.109 2.491.136.832 37.717.937 88.044.047 125.761.984 | 2.616.898.816 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 265,38 M€ (265.377.200 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA 60.299.069 148.646.269 30.900 50.113.575 259.089.813 2.150.387 4.137.000 6.287.387 | 265.377.200 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 33,16 M€ (33.157.283 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES 4.736.798 10.930.283 17.340.102 33.007.183 150.100 150.100 | 33.157.283 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,87 M€ (10.872.167 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS 1.444.261 4.612.006 4.155.050 10.211.317 160.000 500.850 660.850 | 10.872.167 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 146,52 M€ (146.517.976 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN 8.718.846 4.771.570 42.824.592 56.315.008 28.000 51.246.550 51.274.550 | 107.589.558 | 73,4 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL 2.730.545 158.000 4.051.779 6.940.324 1.906.000 30.082.094 31.988.094 | 38.928.418 | 26,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,72 M€ (2.721.054 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE 653.629 777.425 1.290.000 2.721.054 | 2.721.054 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 16.232,49 M€ · 69 códigos · 33,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y 778.888 801.318.852 802.097.740 3.495.061.847 3.495.061.847 | 4.297.159.587 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 3.349.411.739 3.349.411.739 3.540.000 3.540.000 | 3.352.951.739 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 104.974.919 7.358.786 3.338 536.614.437 648.951.480 1.200.000 342.696.965 343.896.965 | 992.848.445 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS DEL 16.330.145 4.342.685 60.000 268.779.999 289.512.829 298.325.173 185.362.884 483.688.057 | 773.200.886 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA 439.667.825 112.478.472 53.677.725 605.824.022 55.711.337 55.711.337 | 661.535.359 |
| `11A` | D.S.G. PRESIDENCIA, INT.,DIALOGO SOC. Y 66.444.601 14.849.518 200.000 258.313.833 339.807.952 4.161.417 276.906.782 281.068.199 | 620.876.151 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 46.557.309 12.716.547 1.539.500 60.813.356 490.159.015 14.699.500 504.858.515 | 565.671.871 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 535.000.000 535.000.000 | 535.000.000 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 48.172.954 10.703.302 30.000 392.688.767 451.595.023 1.335.000 23.998.231 25.333.231 | 476.928.254 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 75.006.120 33.621.627 30.000 181.029.250 289.686.997 8.125.301 48.253.159 56.378.460 | 346.065.457 |
| `44E` | GESTIÓN FORESTAL Y BIODIVERSIDAD 19.760.981 41.944 275.000 20.000 20.097.925 195.624.623 89.313.849 284.938.472 | 305.036.397 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL 11.049.700 4.300.076 181.822.581 197.172.357 460.200 77.858.034 78.318.234 | 275.490.591 |
| `51A` | INFRAESTRUCTURAS VIARIAS 18.766.314 1.674.422 1.796.469 22.237.205 222.375.508 222.375.508 | 244.612.713 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 81.326.738 11.824.370 114.500 92.021.529 185.287.137 8.354.379 40.417.352 48.771.731 | 234.058.868 |
| `52C` | COMUNICACIÓN SOCIAL 2.424.883 975.738 170.994.665 174.395.286 17.297.424 2.992.325 20.289.749 | 194.685.035 |
| `73A` | ORDENACIÓN DE LA ACTIVIDAD ENERGÉTICA 14.672.331 269.037 15.271.610 30.212.978 482.105 161.540.867 162.022.972 | 192.235.950 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 90.610.166 11.853.853 9.100 82.888.775 185.361.894 2.848.606 1.743.904 4.592.510 | 189.954.404 |
| `73B` | ORDENACIÓN DE LA ACTIVIDAD INDUSTRIAL Y 17.124.388 963.682 20.000 18.108.070 16.208.771 132.548.968 148.757.739 | 166.865.809 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 4.138.494 25.646.466 124.858.950 154.643.910 | 154.643.910 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL 12.022.576 106.329 235.072 12.363.977 45.825.001 93.560.089 139.385.090 | 151.749.067 |
| `61B` | POLÍTICA ECONÓMICA Y FINANCIERA Y 2.198.848 32.802 60.734.164 62.965.814 358.188 68.710.647 69.068.835 | 132.034.649 |
| `31P` | APOYO A FAMILIAS 5.856.768 63.382.315 60.116.893 129.355.976 | 129.355.976 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS 3.259.887 88.588.751 248.000 92.096.638 100.000 100.000 | 92.196.638 |
| `44D` | ESPACIOS NATURALES PROTEGIDOS 14.199.982 1.791.016 175.000 16.165.998 59.142.336 12.713.400 71.855.736 | 88.021.734 |
| `32E` | PROYECTOS DE INTERÉS SOCIAL 1.194.870 73.232.070 74.426.940 960.008 9.421.170 10.381.178 | 84.808.118 |
| … | *resto: 44 códigos* | 974.498.647 |

</details>

### 2026

*Fuente: `memoria_programas.pdf` · 107 líneas · total extraído **51.120,36 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 15.950,81 M€ (15.950.811.279 €) · 3 códigos · 31,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `41H` | DIRECCIÓN Y SERVICIOS GENERALES 47.175.252 7.663.845 39.326 15.306.681.909 15.361.560.332 1.253.135 480.096.140 481.349.275 | 15.842.909.607 | 99,3 % |
| `41D` | SALUD PÚBLICA 20.273.495 63.170.886 10.179.995 93.624.376 2.436.365 2.436.365 | 96.060.741 | 0,6 % |
| `41J` | INSPECCIÓN DE SERVICIOS SANITARIOS 11.744.134 61.797 11.805.931 35.000 35.000 | 11.840.931 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 9.998,48 M€ (9.998.482.040 €) · 9 códigos · 19,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `42D` | EDUCACIÓN SECUNDARIA Y FORMACION 3.179.556.563 209.002.148 75.100 708.717.953 4.097.351.764 1.283.143 1.283.143 | 4.098.634.907 | 41,0 % |
| `42C` | EDUCACIÓN INFANTIL Y PRIMARIA 1.983.787.588 27.133.825 30.040 477.548.949 2.488.500.402 75.000 75.000 | 2.488.575.402 | 24,9 % |
| `42J` | UNIVERSIDADES 1.606.450 24.653 1.638.850.663 1.640.481.766 155.210.232 155.210.232 | 1.795.691.998 | 18,0 % |
| `42E` | EDUCACIÓN ESPECIAL 427.033.834 897.429 10.013 164.311.911 592.253.187 | 592.253.187 | 5,9 % |
| `42F` | EDUCACIÓN COMPENSATORIA 276.763.811 30.087.174 4.172 104.978.972 411.834.129 1.566.287 1.566.287 | 413.400.416 | 4,1 % |
| `42H` | ENSEÑANZAS DE REGIMEN ESPECIAL 306.342.969 12.360.763 3.338 421.535 319.128.605 168.231 168.231 | 319.296.836 | 3,2 % |
| `42I` | EDUCACIÓN PARA LA PRIMERA INFANCIA 119.842.795 13.571.585 8.345 133.422.725 55.939 664.575 720.514 | 134.143.239 | 1,3 % |
| `42G` | EDUCACIÓN DE PERSONAS ADULTAS 110.547.829 10.872.238 834 550 121.421.451 | 121.421.451 | 1,2 % |
| `42B` | FORMACIÓN DEL PROFESORADO 22.630.513 12.434.091 35.064.604 | 35.064.604 | 0,4 % |

</details>

<details open><summary><b><code>soberania</code> — 2.480,51 M€ (2.480.509.786 €) · 6 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 1.568.444.018 1.568.444.018 | 1.568.444.018 | 63,2 % |
| `71B` | ORDENACIÓN Y MEJORA DE LA PRODUC. 6.189.409 2.942.000 25.000 39.247.500 48.403.909 137.252.715 186.734.048 323.986.763 | 372.390.672 | 15,0 % |
| `71F` | APOYO AL SECTOR PRODUCTOR AGRÍCOLA Y 9.660.885 5.451.428 200.000 15.312.313 5.376.215 248.844.037 254.220.252 | 269.532.565 | 10,9 % |
| `71E` | INCENTIVACIÓN DEL SECTOR 3.256.710 1.011.330 4.268.040 21.100.197 104.057.084 125.157.281 | 129.425.321 | 5,2 % |
| `71H` | DESARROLLO RURAL 831.576 80.000 20.000 2.500.000 3.431.576 76.678.188 76.678.188 | 80.109.764 | 3,2 % |
| `71P` | PESCA 4.528.968 209.000 19.413.000 24.150.968 3.415.000 33.041.478 36.456.478 | 60.607.446 | 2,4 % |

</details>

<details open><summary><b><code>vivienda</code> — 719,35 M€ (719.346.413 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `43A` | VIVIENDA, REHABILITACIÓN Y SUELO 16.129.325 8.861.311 25.000 82.446.011 107.461.647 975.576 537.038.811 538.014.387 50.000.000 50.000.000 | 695.476.034 | 96,7 % |
| `43B` | ACTUACIONES EN MATERIA ORDENA. TERRIT. Y 12.958.994 4.547.310 17.506.304 364.075 6.000.000 6.364.075 | 23.870.379 | 3,3 % |

</details>

<details open><summary><b><code>empleo</code> — 782,05 M€ (782.050.538 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `32D` | FORMACIÓN PROFESIONAL PARA EL EMPLEO 32.409.664 21.343.090 50.000 253.588.070 307.390.824 13.078.925 5.259.943 18.338.868 | 325.729.692 | 41,7 % |
| `32K` | POLÍTICAS ACTIVAS DE EMPLEO 8.689.236 5.000 252.207.937 260.902.173 1.000.800 1.000.800 | 261.902.973 | 33,5 % |
| `72C` | TRABAJO AUTÓNOMO Y ECONOMÍA SOCIAL 9.805.665 240.000 2.000 23.088.600 33.136.265 20.000 79.431.791 79.451.791 | 112.588.056 | 14,4 % |
| `31C` | SEGURIDAD, SALUD Y RELACIONES 29.516.972 8.664.020 25.000 11.979.353 50.185.345 975.250 6.336.103 7.311.353 | 57.496.698 | 7,4 % |
| `76A` | ORDENACIÓN Y PROMOCIÓN COMERCIAL 8.159.155 213.000 5.657.050 14.029.205 974.000 5.596.345 6.570.345 | 20.599.550 | 2,6 % |
| `31M` | CONSEJO ANDALUZ DE RELACIONES 2.101.118 1.564.191 54.260 3.719.569 14.000 14.000 | 3.733.569 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 471,73 M€ (471.728.406 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `54A` | INVESTIGACIÓN CIENTÍFICA E INNOVACIÓN 3.247.342 456.973 49.813.168 53.517.483 105.208.996 105.208.996 | 158.726.479 | 33,6 % |
| `54C` | INNOVACIÓN Y EVALUACIÓN EDUCATIVA 42.129.713 14.241.998 835 13.068.621 69.441.167 55.461.285 55.461.285 | 124.902.452 | 26,5 % |
| `72A` | INNOVACIÓN Y EMPRENDIMIENTO 2.058.259 674.834 42.700.003 45.433.096 1.769.194 44.431.181 46.200.375 | 91.633.471 | 19,4 % |
| `45B` | INNOVACIÓN Y PROMOCIÓN CULTURAL 4.443.605 1.028.807 60.145.108 65.617.520 430.859 1.992.950 2.423.809 | 68.041.329 | 14,4 % |
| `45H` | TUTELA, INVESTIGACIÓN Y DIFUSIÓN 25.717.416 337.500 26.054.916 1.585.774 783.985 2.369.759 | 28.424.675 | 6,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.913,06 M€ (2.913.064.494 €) · 1 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31R` | ATENC. DEPENDENCIA, ENVEJECIMIENTO ACTI. 162.330.682 33.671.847 35.000 2.595.494.542 2.791.532.071 52.565.051 68.967.372 121.532.423 | 2.913.064.494 | 100,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 268,84 M€ (268.836.077 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31E` | ATENCIÓN A LA INFANCIA 58.426.859 153.585.652 30.900 53.583.278 265.626.689 3.209.388 3.209.388 | 268.836.077 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 36,38 M€ (36.381.544 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31B` | PLAN SOBRE ADICCIONES 4.640.470 13.479.746 18.093.328 36.213.544 168.000 168.000 | 36.381.544 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,71 M€ (10.709.103 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31J` | COORDINACIÓN DE POLÍTICAS MIGRATORIAS 1.281.197 4.772.006 4.655.900 10.709.103 | 10.709.103 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 160,83 M€ (160.831.101 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `75B` | PLANIFICACIÓN, ORDENACIÓN Y PROMOCIÓN 7.731.449 3.185.247 49.286.061 60.202.757 65.572 50.717.581 50.783.153 | 110.985.910 | 69,0 % |
| `75D` | CALIDAD, INNOVACIÓN Y FOMENTO DEL 3.954.426 3.745.907 4.126.779 11.827.112 26.909 37.991.170 38.018.079 | 49.845.191 | 31,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,97 M€ (1.971.376 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `31T` | PROTECCIÓN CONTRA LA VIOLENCIA DE 503.951 777.425 690.000 1.971.376 | 1.971.376 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 17.325,64 M€ · 69 códigos · 33,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `01A` | ADMON,GESTIÓN FINANCIERA Y 845.573 819.902.215 820.747.788 3.595.113.435 3.595.113.435 | 4.415.861.223 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 3.549.914.552 3.549.914.552 3.037.187 3.037.187 | 3.552.951.739 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 112.812.808 7.736.490 3.338 568.013.749 688.566.385 1.200.000 185.605.689 186.805.689 | 875.372.074 |
| `51D` | ACTUACIONES EN MATERIA DE AGUA 46.335.845 12.915.461 789.809 60.041.115 659.554.375 16.406.025 675.960.400 | 736.001.515 |
| `51B` | MOVILIDAD E INFRAESTRUCTURAS DEL 15.654.524 11.298.529 25.000 278.686.715 305.664.768 302.912.537 120.627.087 423.539.624 | 729.204.392 |
| `14B` | ADMINISTRACIÓN DE JUSTICIA 455.624.151 111.685.130 54.605.511 621.914.792 36.364.649 36.364.649 | 658.279.441 |
| `81B` | COOPER. ECONÓMICA Y RELAC. FINANCIERAS 545.000.000 545.000.000 | 545.000.000 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 7.356.114 1.541.101 3.050 229.679.395 238.579.660 162.105 264.562.196 264.724.301 | 503.303.961 |
| `73A` | ORDENACIÓN DE LA ACTIVIDAD ENERGÉTICA 14.291.703 176.046 16.901.835 31.369.584 375.096 427.705.590 428.080.686 | 459.450.270 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 46.737.602 10.643.704 30.000 377.154.163 434.565.469 1.458.000 22.606.117 24.064.117 | 458.629.586 |
| `63B` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS 10.000.000 500.000 16.000.000 26.500.000 411.650.000 411.650.000 | 438.150.000 |
| `61B` | POLÍTICA ECONÓMICA Y FINANCIERA Y 1.806.502 15.257 65.435.032 67.256.791 100.000 322.990.213 323.090.213 | 390.347.004 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 78.376.014 27.474.917 30.000 186.305.191 292.186.122 13.436.488 22.897.614 36.334.102 | 328.520.224 |
| `22B` | INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL 10.914.428 19.692.646 226.972.292 257.579.366 677.000 53.067.324 53.744.324 | 311.323.690 |
| `51A` | INFRAESTRUCTURAS VIARIAS 17.662.097 1.712.531 840.000 60.000 20.274.628 216.821.905 216.821.905 | 237.096.533 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 93.212.641 10.732.310 18.100 89.878.426 193.841.477 4.680.275 2.399.757 7.080.032 | 200.921.509 |
| `12S` | DIRECCIÓN Y SERVICIOS GENERALES 82.283.682 12.620.317 126.000 85.914.007 180.944.006 6.918.188 8.831.372 15.749.560 | 196.693.566 |
| `52C` | COMUNICACIÓN SOCIAL 2.253.717 1.355.945 173.741.085 177.350.747 17.189.596 1.853.063 19.042.659 | 196.393.406 |
| `44E` | GESTIÓN FORESTAL Y BIODIVERSIDAD 18.848.663 60.007 250.000 20.000 19.178.670 114.782.720 52.939.985 167.722.705 | 186.901.375 |
| `44B` | PREVENCIÓN Y CALIDAD AMBIENTAL 12.193.365 113.544 6.000 235.072 12.547.981 47.542.702 115.805.225 163.347.927 | 175.895.908 |
| `31G` | ACCIÓN COMUNITARIA E INSERCIÓN 3.733.603 31.782.900 126.921.448 162.437.951 756.416 756.416 | 163.194.367 |
| `73B` | ORDENACIÓN DE LA ACTIVIDAD INDUSTRIAL Y 16.567.313 862.472 215.000 17.644.785 13.361.272 131.885.891 145.247.163 | 162.891.948 |
| `31P` | APOYO A FAMILIAS 5.923.165 62.732.315 58.859.018 127.514.498 | 127.514.498 |
| `32E` | PROYECTOS DE INTERÉS SOCIAL 4.308.645 2.064.820 80.826.739 87.200.204 12.240.000 12.240.000 | 99.440.204 |
| `14C` | JUSTICIA JUVENIL Y ASISTENCIA A VÍCTIMAS 3.764.138 89.059.598 259.980 93.083.716 100.000 100.000 | 93.183.716 |
| … | *resto: 44 códigos* | 1.083.114.408 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py and     # regenera este documento
python3 tools/auditoria_magnitud.py and        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa and --anio <año> \
    --input ../fuentes/raw/and/<año>/<fichero> --output /tmp/and.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-and.md`](limitaciones-and.md)

