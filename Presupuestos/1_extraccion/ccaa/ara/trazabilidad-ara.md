# Trazabilidad de la extracción — Aragón (`ara`)

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
| **2015** | 159 | `ingresos_gastos.pdf` | 9 | 28,3 % | 5.301,03 | — | no_aplica |
| **2016** | 158 | `ingresos_gastos.pdf` | 10 | 27,8 % | 5.153,25 | — | no_aplica |
| **2017** | 163 | `ingresos_gastos.pdf` | 10 | 28,8 % | 5.601,40 | — | no_aplica |
| **2018** | 156 | `ingresos_gastos.pdf` | 10 | 26,9 % | 6.193,32 | — | no_aplica |
| **2019** | 156 | `ingresos_gastos.pdf` | 10 | 26,9 % | 6.193,32 | — | prorroga |
| **2020** | 162 | `ingresos_gastos.pdf` | 10 | 25,9 % | 6.508,65 | — | no_aplica |
| **2021** | 183 | `ingresos_gastos.pdf` | 10 | 29,0 % | 7.500,92 | — | no_aplica |
| **2022** | 178 | `ingresos_gastos.pdf` | 10 | 27,0 % | 7.496,14 | — | no_aplica |
| **2023** | 178 | `ingresos_gastos.pdf` | 10 | 27,5 % | 8.307,15 | — | no_aplica |
| **2024** | 194 | `ingresos_gastos.pdf` | 11 | 29,4 % | 8.610,35 | — | no_aplica |
| **2025** | 194 | `ingresos_gastos.pdf` | 11 | 29,4 % | 8.610,35 | — | prorroga |
| **2026** | 194 | `ingresos_gastos.pdf` | 11 | 29,4 % | 8.610,35 | — | prorroga |

**URL(s) de origen:**
- <https://www.aragon.es/documents/d/guest/estado-de-ingresos-y-gastos-1?download=true>
- <https://www.aragon.es/documents/d/guest/estado-de-ingresos-y-gastos?download=true>
- <https://www.aragon.es/documents/d/guest/estado-ingresos-y-gastos?download=true>
- <https://www.aragon.es/documents/d/guest/estados-de-ingresos-y-gastos?download=true>
- <https://www.aragon.es/documents/d/guest/ingresos_gastos_24?download=true>
- <https://www.aragon.es/documents/d/guest/presupuestos-zip?download=true>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 1.604,44 | 1.806,28 | 1.903,12 | 2.006,05 | 2.006,05 | 2.078,64 | 2.366,55 | 2.250,32 | 2.557,97 | 2.771,99 | 2.771,99 | 2.771,99 |
| `educacion` | 879,55 | 958,48 | 1.040,67 | 1.090,32 | 1.090,32 | 1.182,20 | 1.294,79 | 1.311,65 | 1.373,14 | 1.519,82 | 1.519,82 | 1.519,82 |
| `soberania` | 647,91 | 631,00 | 635,47 | 642,67 | 642,67 | 651,86 | 673,95 | 689,55 | 715,07 | 735,05 | 735,05 | 735,05 |
| `direccion` | 3,01 | 2,38 | 2,17 | 2,20 | 2,20 | 2,47 | 2,51 | 2,52 | 2,77 | 2,86 | 2,86 | 2,86 |
| `vivienda` | 74,55 | 18,50 | 35,20 | 39,95 | 39,95 | 42,98 | 48,85 | 51,68 | 101,30 | 53,88 | 53,88 | 53,88 |
| `empleo` | 94,15 | 94,38 | 106,67 | 117,17 | 117,17 | 120,64 | 128,59 | 126,18 | 160,28 | 168,90 | 168,90 | 168,90 |
| `idi` | 57,79 | 51,57 | 78,98 | 83,68 | 83,68 | 71,35 | 87,92 | 78,95 | 79,78 | 77,19 | 77,19 | 77,19 |
| `salud_mental` | — | — | — | — | — | — | — | — | — | 16,11 | 16,11 | 16,11 |
| `diversidad` | — | 1,06 | 1,34 | 1,62 | 1,62 | 1,51 | 1,56 | 1,56 | 1,59 | 1,76 | 1,76 | 1,76 |
| `turismo` | 12,91 | 23,33 | 15,33 | 13,49 | 13,49 | 10,81 | 14,16 | 30,75 | 52,71 | 89,00 | 89,00 | 89,00 |
| `igualdad` | 3,18 | 3,36 | 3,86 | 4,19 | 4,19 | 6,28 | 6,18 | 9,18 | 8,25 | 16,23 | 16,23 | 16,23 |
| **Σ asignado** | 3.377,48 | 3.590,34 | 3.822,82 | 4.001,35 | 4.001,35 | 4.168,75 | 4.625,06 | 4.552,34 | 5.052,86 | 5.452,77 | 5.452,77 | 5.452,77 |
| *(sin concepto)* | 1.923,56 | 1.562,91 | 1.778,58 | 2.191,97 | 2.191,97 | 2.339,90 | 2.875,86 | 2.943,80 | 3.254,30 | 3.157,58 | 3.157,58 | 3.157,58 |
| **TOTAL extraído** | 5.301,03 | 5.153,25 | 5.601,40 | 6.193,32 | 6.193,32 | 6.508,65 | 7.500,92 | 7.496,14 | 8.307,15 | 8.610,35 | 8.610,35 | 8.610,35 |

**Conceptos sin ninguna línea en toda la serie:** `dependencia`, `discapacidad` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +12,6 % | +5,4 % | +5,4 % | +0,0 % | +3,6 % | +13,9 % | −4,9 % | +13,7 % | +8,4 % | +0,0 % | +0,0 % |
| `educacion` | +9,0 % | +8,6 % | +4,8 % | +0,0 % | +8,4 % | +9,5 % | +1,3 % | +4,7 % | +10,7 % | +0,0 % | +0,0 % |
| `soberania` | −2,6 % | +0,7 % | +1,1 % | +0,0 % | +1,4 % | +3,4 % | +2,3 % | +3,7 % | +2,8 % | +0,0 % | +0,0 % |
| `direccion` | −20,7 % | −8,9 % | +1,5 % | +0,0 % | +12,2 % | +1,5 % | +0,4 % | +9,8 % | +3,4 % | +0,0 % | +0,0 % |
| `vivienda` | −75,2 % ⚠ | +90,2 % ⚠ | +13,5 % | +0,0 % | +7,6 % | +13,6 % | +5,8 % | +96,0 % ⚠ | −46,8 % ⚠ | +0,0 % | +0,0 % |
| `empleo` | +0,2 % | +13,0 % | +9,8 % | +0,0 % | +3,0 % | +6,6 % | −1,9 % | +27,0 % | +5,4 % | +0,0 % | +0,0 % |
| `idi` | −10,8 % | +53,1 % ⚠ | +6,0 % | +0,0 % | −14,7 % | +23,2 % | −10,2 % | +1,0 % | −3,2 % | +0,0 % | +0,0 % |
| `salud_mental` | · | · | · | · | · | · | · | · | **nuevo** ⛔ | +0,0 % | +0,0 % |
| `diversidad` | **nuevo** ⛔ | +26,4 % | +21,0 % | +0,0 % | −6,6 % | +3,5 % | −0,4 % | +1,9 % | +10,7 % | +0,0 % | +0,0 % |
| `turismo` | +80,7 % ⚠ | −34,3 % | −12,0 % | +0,0 % | −19,9 % | +31,0 % | +117,1 % ⚠ | +71,4 % ⚠ | +68,8 % ⚠ | +0,0 % | +0,0 % |
| `igualdad` | +5,6 % | +15,0 % | +8,6 % | +0,0 % | +49,6 % ⚠ | −1,6 % | +48,7 % ⚠ | −10,1 % | +96,6 % ⚠ | +0,0 % | +0,0 % |
| **TOTAL** | −2,8 % | +8,7 % | +10,6 % | +0,0 % | +5,1 % | +15,2 % | −0,1 % | +10,8 % | +3,6 % | +0,0 % | +0,0 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `vivienda` | **SALTO** | 74,55 → 18,50 M€ (−75,2 % ⚠) |
| 2017 | `idi` | **SALTO** | 51,57 → 78,98 M€ (+53,1 % ⚠) |
| 2017 | `vivienda` | **SALTO** | 18,50 → 35,20 M€ (+90,2 % ⚠) |
| 2023 | `turismo` | **SALTO** | 30,75 → 52,71 M€ (+71,4 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 51,68 → 101,30 M€ (+96,0 % ⚠) |
| 2024 | `turismo` | **SALTO** | 52,71 → 89,00 M€ (+68,8 % ⚠) |
| 2024 | `vivienda` | **SALTO** | 101,30 → 53,88 M€ (−46,8 % ⚠) |

### 4.1 · Códigos duplicados dentro del mismo año (232 casos, 9.543,00 M€ acumulados)

> Un mismo código aparece en **varias filas del mismo ejercicio**. Puede ser legítimo
> (mismo programa en varias secciones/centros gestores) o **doble conteo** que infla el total.
> Compruébalo contra el documento original antes de dar el año por bueno.

| Año | Código | Concepto | Filas | Importe sumado (M€) |
|---|---|---|---:|---:|
| 2021 | `4121` | `sanidad` | 2 | 2.207,36 |
| 2021 | `3132` | `(sin concepto)` | 2 | 439,34 |
| 2017 | `4222` | `educacion` | 2 | 380,55 |
| 2017 | `4221` | `educacion` | 2 | 314,36 |
| 2023 | `4228` | `educacion` | 2 | 220,27 |
| 2021 | `3221` | `empleo` | 2 | 125,53 |
| 2024 | `5121` | `(sin concepto)` | 3 | 111,83 |
| 2026 | `5121` | `(sin concepto)` | 3 | 111,83 |
| 2025 | `5121` | `(sin concepto)` | 3 | 111,83 |
| 2017 | `3221` | `empleo` | 2 | 103,79 |
| 2024 | `4211` | `educacion` | 2 | 99,19 |
| 2026 | `4211` | `educacion` | 2 | 99,19 |
| 2025 | `4211` | `educacion` | 2 | 99,19 |
| 2021 | `4211` | `educacion` | 2 | 93,98 |
| 2023 | `4211` | `educacion` | 2 | 93,33 |
| 2023 | `5121` | `(sin concepto)` | 2 | 92,19 |
| 2015 | `5121` | `(sin concepto)` | 2 | 91,78 |
| 2022 | `5121` | `(sin concepto)` | 2 | 86,21 |
| 2021 | `5121` | `(sin concepto)` | 2 | 85,72 |
| 2016 | `5311` | `soberania` | 2 | 83,93 |
| 2024 | `5131` | `(sin concepto)` | 2 | 80,97 |
| 2026 | `5131` | `(sin concepto)` | 2 | 80,97 |
| 2025 | `5131` | `(sin concepto)` | 2 | 80,97 |
| 2020 | `5121` | `(sin concepto)` | 2 | 80,79 |
| 2019 | `5121` | `(sin concepto)` | 2 | 80,66 |
| 2018 | `5121` | `(sin concepto)` | 2 | 80,66 |
| 2022 | `4211` | `educacion` | 2 | 75,96 |
| 2024 | `6126` | `(sin concepto)` | 2 | 73,39 |
| 2026 | `6126` | `(sin concepto)` | 2 | 73,39 |
| 2025 | `6126` | `(sin concepto)` | 2 | 73,39 |
| … | *202 casos más* | | | |

### 4.2 · Códigos que CAMBIAN de concepto entre años (3 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `4231` | 16,71 | 2015:(sin concepto), 2016:(sin concepto), 2017:idi, 2018:idi, 2019:idi, 2020:idi, 2021:idi, 2022:idi, 2023:idi, 2024:idi, 2025:idi, 2026:idi |
| `5411` | 8,37 | 2015:idi, 2016:idi, 2017:idi, 2018:idi, 2019:idi, 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto) |
| `3133` | 5,85 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:igualdad, 2025:igualdad, 2026:igualdad |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `ingresos_gastos.pdf` · 159 líneas · total extraído **5.301,03 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.604,44 M€ (1.604.436.847 €) · 7 códigos · 30,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | Asistencia Sanitaria | 1.471.463.540 | 91,7 % |
| `4131` | Protección y Promoción de la Salud | 69.308.339 | 4,3 % |
| `4134` | Salud Pública | 26.127.822 | 1,6 % |
| `5425` | Investigación y Desarrollo en el Área de la Salud *(×2 filas)* | 15.653.151 | 1,0 % |
| `4111` | Serv. Gener. Sanidad, Bienestar Social y Familia | 10.122.574 | 0,6 % |
| `4124` | Producc. componentes sanguíneos y de tejidos | 8.925.387 | 0,6 % |
| `4132` | Servicios de Atención al Usuario | 2.836.035 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 879,55 M€ (879.551.896 €) · 11 códigos · 16,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 306.451.617 | 34,8 % |
| `4221` | Educación Infantil y Primaria | 272.353.120 | 31,0 % |
| `4228` | Educación Universitaria | 154.580.953 | 17,6 % |
| `4211` | Servicios Generales Educación,Univ.,Cultura y Dep. | 57.657.152 | 6,6 % |
| `4223` | Educación Especial | 45.397.280 | 5,2 % |
| `4224` | Enseñanzas Artísticas | 21.871.009 | 2,5 % |
| `4225` | Educación Permanente | 9.691.912 | 1,1 % |
| `4226` | Plan Aragonés de Formación Profesional | 4.348.902 | 0,5 % |
| `4227` | Formación del Profesorado | 3.337.538 | 0,4 % |
| `4212` | Gestión de Personal | 2.843.495 | 0,3 % |
| `4229` | Evaluación de la calidad de la Enseñanza Superior *(×2 filas)* | 1.018.918 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 647,91 M€ (647.905.750 €) · 7 códigos · 12,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7128` | Política Agraria Comunitaria | 438.900.000 | 67,7 % |
| `5311` | Mejora de Estructuras Agrarias y Desarrollo Rural | 93.330.524 | 14,4 % |
| `7122` | Coordinación y Gestión de Servicios Agroambient. | 44.920.969 | 6,9 % |
| `7123` | Producción Agraria y Gestión de Ayudas | 36.206.329 | 5,6 % |
| `7161` | Calidad y Seguridad Alimentaria | 19.104.022 | 2,9 % |
| `7121` | Desarrollo Agroalimentario y Fomento Asociativo | 14.991.792 | 2,3 % |
| `7111` | Serv.Gen. Agricultura, Ganadería y Medio Ambiente | 452.113 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,01 M€ (3.005.653 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | Presidencia y Órganos de la Presidencia | 3.005.653 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 74,55 M€ (74.547.890 €) · 3 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5111` | Serv.G. O.Públicas, Urbanismo, Vivienda y Ttes *(×2 filas)* | 61.763.794 | 82,9 % |
| `4312` | Gestión social de la vivienda | 9.986.422 | 13,4 % |
| `4311` | Promoción y Administración de Viviendas | 2.797.675 | 3,8 % |

</details>

<details open><summary><b><code>empleo</code> — 94,15 M€ (94.153.669 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | Fomento del Empleo. Instituto Aragonés de Empleo | 91.642.358 | 97,3 % |
| `6112` | Servicios Generales de Economía y Empleo | 2.411.311 | 2,6 % |
| `3222` | Fomento del Empleo. Escuelas Taller | 100.000 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 57,79 M€ (57.787.367 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | Investigación, Desarrollo e Innovación Tecnológica *(×2 filas)* | 21.554.853 | 37,3 % |
| `5421` | Investigación Agroalimentaria *(×2 filas)* | 19.030.813 | 32,9 % |
| `5424` | Investigación y Dllo. Sociedad de la Información | 12.078.777 | 20,9 % |
| `5411` | Serv. Generales Industria e Innovación | 3.682.923 | 6,4 % |
| `5422` | Investigación y Tecnología Aplicada a la Industria | 1.440.000 | 2,5 % |

</details>

<details open><summary><b><code>turismo</code> — 12,91 M€ (12.905.536 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Ordenación, Promoción y Fomento del Turismo *(×2 filas)* | 12.905.536 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,18 M€ (3.180.941 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | Promoción de la Mujer | 3.180.941 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.923,56 M€ · 79 códigos · 36,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Amortización y Gastos Financieros de la Deuda | 815.332.264 |
| `3132` | Gestión y Desarrollo de los Servicios Sociales | 302.993.491 |
| `5121` | Gestión e Infraestructura de Recursos Hidráulicos *(×2 filas)* | 91.778.300 |
| `5131` | Carreteras | 82.204.386 |
| `1421` | Servicios de Administración de Justicia | 70.267.759 |
| `6122` | Promoción y Desarrollo Económico | 69.334.371 |
| `9111` | Transferencias a Administraciones Comarcales *(×33 filas)* | 60.419.839 |
| `1266` | Televisión y Radio Autonómicas | 44.000.000 |
| `1252` | Política Territorial | 23.947.721 |
| `6129` | Fondo de Contingencia de Ejecución Presupuestaria | 23.273.432 |
| `5331` | Protección y mejora del Medio Natural | 22.821.005 |
| `5332` | Conservac. de la Biodivers y Desarrollo Sostenible | 18.428.779 |
| `1111` | Cortes de Aragón (Actividad Legislativa) | 17.773.524 |
| `5132` | Transportes | 17.352.139 |
| `1265` | Servicios Telemáticos *(×2 filas)* | 17.067.800 |
| `4323` | Arquitectura y Rehabilitación | 11.369.271 |
| `1211` | Servicios Generales de Presidencia y Justicia | 11.250.230 |
| `4422` | Protección y Mejora del Medio Ambiente | 10.852.864 |
| `6311` | Gestión e Inspección de Tributos | 10.777.263 |
| `1251` | Apoyo a la Administración Local | 10.554.838 |
| `1212` | Servicios Centrales, Edificios e Instalaciones | 10.180.094 |
| `7231` | Fomento Industrial | 9.346.157 |
| `6126` | Apoyo al Desarrollo Económico y Social | 9.282.900 |
| `6312` | Control Interno y Contabilidad | 9.016.290 |
| `4231` | Planificación y Programas Educativos | 8.573.086 |
| … | *resto: 54 códigos* | 145.359.351 |

</details>

### 2016

*Fuente: `ingresos_gastos.pdf` · 158 líneas · total extraído **5.153,25 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.806,28 M€ (1.806.281.339 €) · 7 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 1.683.910.000 | 93,2 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 51.950.880 | 2,9 % |
| `4134` | SALUD PÚBLICA | 30.704.471 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 16.723.832 | 0,9 % |
| `4111` | SERV. GENER. SANIDAD, BIENESTAR SOCIAL Y FAMILIA | 10.179.063 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 9.989.530 | 0,6 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.823.563 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 958,48 M€ (958.476.679 €) · 11 códigos · 18,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 341.828.201 | 35,7 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 294.618.959 | 30,7 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 163.798.183 | 17,1 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN,UNIV.,CULTURA Y DEP. | 63.634.623 | 6,6 % |
| `4223` | EDUCACIÓN ESPECIAL | 48.771.019 | 5,1 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 23.538.255 | 2,5 % |
| `4225` | EDUCACIÓN PERMANENTE | 10.324.963 | 1,1 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 4.422.021 | 0,5 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 3.612.862 | 0,4 % |
| `4212` | GESTIÓN DE PERSONAL | 2.871.986 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.055.605 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 631,00 M€ (630.995.481 €) · 7 códigos · 12,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7128` | POLÍTICA AGRARIA COMUNITARIA | 442.470.312 | 70,1 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL *(×2 filas)* | 83.928.544 | 13,3 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 43.986.586 | 7,0 % |
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 28.971.038 | 4,6 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 16.799.968 | 2,7 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 14.368.612 | 2,3 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE | 470.422 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,38 M€ (2.384.365 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.384.365 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 18,50 M€ (18.502.778 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 12.810.670 | 69,2 % |
| `5111` | SERV.G. O.PÚBLICAS, URBANISMO, VIVIENDA Y TTES | 3.924.025 | 21,2 % |
| `4311` | PROMOCIÓN Y ADMINISTRACIÓN DE VIVIENDAS | 1.768.083 | 9,6 % |

</details>

<details open><summary><b><code>empleo</code> — 94,38 M€ (94.381.995 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 91.728.176 | 97,2 % |
| `6112` | SERVICIOS GENERALES DE ECONOMÍA Y EMPLEO | 2.653.819 | 2,8 % |

</details>

<details open><summary><b><code>idi</code> — 51,57 M€ (51.572.792 €) · 5 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 19.504.538 | 37,8 % |
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 14.437.777 | 28,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 12.266.113 | 23,8 % |
| `5411` | SERV. GENERALES INDUSTRIA E INNOVACIÓN | 3.825.833 | 7,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 1.538.531 | 3,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,06 M€ (1.058.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.058.000 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,33 M€ (23.325.995 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO *(×2 filas)* | 23.325.995 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,36 M€ (3.359.367 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 3.359.367 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.562,91 M€ · 78 códigos · 30,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 518.951.895 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 338.910.415 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 69.705.211 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO | 65.188.209 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 61.135.054 |
| `5131` | CARRETERAS | 60.128.079 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 49.281.456 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 44.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 30.109.596 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 20.000.000 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 18.455.069 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 17.573.804 |
| `4323` | ARQUITECTURA Y REHABILITACIÓN | 14.844.801 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.384.840 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 14.171.688 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 14.033.656 |
| `4521` | ARCHIVOS Y MUSEOS | 12.447.045 |
| `4231` | PLANIFICACIÓN Y PROGRAMAS EDUCATIVOS | 12.244.785 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 10.144.001 |
| `5132` | TRANSPORTES | 9.937.739 |
| `6312` | CONTROL INTERNO Y CONTABILIDAD | 9.092.072 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 8.722.080 |
| `1212` | SERVICIOS CENTRALES, EDIFICIOS E INSTALACIONES | 8.139.734 |
| `7231` | FOMENTO INDUSTRIAL | 8.033.456 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL | 8.027.472 |
| … | *resto: 53 códigos* | 125.246.134 |

</details>

### 2017

*Fuente: `ingresos_gastos.pdf` · 163 líneas · total extraído **5.601,40 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.903,12 M€ (1.903.124.003 €) · 7 códigos · 34,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 1.775.025.460 | 93,3 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 57.543.213 | 3,0 % |
| `4134` | SALUD PÚBLICA | 31.767.083 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 15.158.889 | 0,8 % |
| `4111` | SERV. GENER. SANIDAD | 11.287.349 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 9.491.380 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.850.628 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.040,67 M€ (1.040.672.902 €) · 11 códigos · 18,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL *(×2 filas)* | 380.546.522 | 36,6 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA *(×2 filas)* | 314.364.880 | 30,2 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 169.810.206 | 16,3 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE | 70.201.972 | 6,7 % |
| `4223` | EDUCACIÓN ESPECIAL *(×2 filas)* | 56.098.969 | 5,4 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 25.947.717 | 2,5 % |
| `4225` | EDUCACIÓN PERMANENTE | 11.051.676 | 1,1 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 4.430.447 | 0,4 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 3.942.797 | 0,4 % |
| `4212` | GESTIÓN DE PERSONAL | 2.965.004 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.312.713 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 635,47 M€ (635.474.224 €) · 7 códigos · 11,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7128` | POLÍTICA AGRARIA COMUNITARIA | 446.274.744 | 70,2 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 81.618.484 | 12,8 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 43.879.021 | 6,9 % |
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 30.653.409 | 4,8 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 19.505.066 | 3,1 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 13.115.176 | 2,1 % |
| `7111` | SERV.GEN. DESARROLLO RURAL Y SOSTENIBILIDAD | 428.323 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,17 M€ (2.170.972 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.170.972 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 35,20 M€ (35.198.226 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 31.274.129 | 88,9 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA | 3.924.097 | 11,1 % |

</details>

<details open><summary><b><code>empleo</code> — 106,67 M€ (106.674.130 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO *(×2 filas)* | 103.787.004 | 97,3 % |
| `6112` | SERV G. ECONOMÍA, INDUSTRIA Y EMPLEO | 2.887.126 | 2,7 % |

</details>

<details open><summary><b><code>idi</code> — 78,98 M€ (78.976.929 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 23.853.935 | 30,2 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 19.340.543 | 24,5 % |
| `4231` | INNOVACIÓN, EQUIDAD Y PARTICIPACIÓN | 16.104.095 | 20,4 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.807.612 | 17,5 % |
| `5411` | SERV. G. INNOVACIÓN, INVESTIGACIÓN Y UNIVERSIDAD | 3.445.743 | 4,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 2.425.000 | 3,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,34 M€ (1.337.482 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | IGUALDAD Y APOYO A LA INMIGRACIÓN | 1.337.482 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 15,33 M€ (15.327.008 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO *(×2 filas)* | 15.327.008 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,86 M€ (3.863.624 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 3.863.624 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.778,58 M€ · 77 códigos · 31,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 695.151.368 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 366.130.543 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 72.500.806 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 66.654.658 |
| `5131` | CARRETERAS | 63.851.552 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×2 filas)* | 63.125.881 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×32 filas)* | 59.428.426 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 44.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 32.621.796 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 18.923.975 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 17.675.839 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 16.284.549 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 16.156.592 |
| `5132` | TRANSPORTES | 15.505.275 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.384.840 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 12.722.407 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 12.388.045 |
| `6311` | GESTIÓN E INSPECCIÓN DE TRIBUTOS | 10.467.645 |
| `1252` | POLÍTICA TERRITORIAL | 10.420.746 |
| `4581` | PROMOC. DE LA CULTURA Y PROT. DEL PATRIM. CULTURAL | 10.256.820 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA | 9.671.615 |
| `6312` | CONTROL INTERNO Y CONTABILIDAD | 8.943.037 |
| `4571` | FOMENTO Y APOYO A LA ACTIVIDAD DEPORTIVA *(×2 filas)* | 8.258.815 |
| `1212` | SERVICIOS CENTRALES, EDIFICIOS E INSTALACIONES | 7.827.677 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 7.277.574 |
| … | *resto: 52 códigos* | 117.948.806 |

</details>

### 2018

*Fuente: `ingresos_gastos.pdf` · 156 líneas · total extraído **6.193,32 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.006,05 M€ (2.006.052.858 €) · 7 códigos · 32,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 1.870.068.748 | 93,2 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 62.868.694 | 3,1 % |
| `4134` | SALUD PÚBLICA | 33.702.882 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 15.946.519 | 0,8 % |
| `4111` | SERV. GENER. SANIDAD | 11.037.080 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 9.690.000 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.738.935 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.090,32 M€ (1.090.322.967 €) · 11 códigos · 17,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 401.809.651 | 36,9 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 326.686.032 | 30,0 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 175.671.185 | 16,1 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE | 72.028.754 | 6,6 % |
| `4223` | EDUCACIÓN ESPECIAL | 61.964.560 | 5,7 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 26.335.310 | 2,4 % |
| `4225` | EDUCACIÓN PERMANENTE | 11.564.483 | 1,1 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 5.964.617 | 0,5 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 3.957.510 | 0,4 % |
| `4212` | GESTIÓN DE PERSONAL | 2.903.760 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.437.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 642,67 M€ (642.673.405 €) · 6 códigos · 10,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 462.218.850 | 71,9 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 84.987.410 | 13,2 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 45.579.455 | 7,1 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 35.064.890 | 5,5 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 14.388.480 | 2,2 % |
| `7111` | SERV.GEN. DESARROLLO RURAL Y SOSTENIBILIDAD | 434.320 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,20 M€ (2.204.455 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.204.455 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 39,95 M€ (39.953.112 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 34.004.181 | 85,1 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA | 5.948.931 | 14,9 % |

</details>

<details open><summary><b><code>empleo</code> — 117,17 M€ (117.165.149 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 114.110.641 | 97,4 % |
| `6112` | SERV G. ECONOMÍA, INDUSTRIA Y EMPLEO | 3.054.508 | 2,6 % |

</details>

<details open><summary><b><code>idi</code> — 83,68 M€ (83.677.199 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 24.449.064 | 29,2 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 21.472.784 | 25,7 % |
| `4231` | INNOVACIÓN, EQUIDAD Y PARTICIPACIÓN | 16.710.228 | 20,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.709.192 | 16,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 3.925.000 | 4,7 % |
| `5411` | SERV. G. INNOVACIÓN, INVESTIGACIÓN Y UNIVERSIDAD | 3.410.931 | 4,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,62 M€ (1.618.733 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | IGUALDAD Y APOYO A LA INMIGRACIÓN | 1.618.733 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 13,49 M€ (13.489.707 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO *(×2 filas)* | 13.489.707 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,19 M€ (4.194.067 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 4.194.067 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.191,97 M€ · 78 códigos · 35,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.025.540.663 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 388.985.824 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 80.664.921 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 72.931.813 |
| `5131` | CARRETERAS | 66.340.830 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO | 65.960.790 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 59.392.618 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 47.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 36.577.419 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 21.839.418 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 18.146.678 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 17.825.119 |
| `1252` | POLÍTICA TERRITORIAL *(×2 filas)* | 16.019.283 |
| `5132` | TRANSPORTES | 15.050.033 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.573.121 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.384.840 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 14.342.992 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 12.670.395 |
| `6311` | GESTIÓN E INSPECCIÓN DE TRIBUTOS | 11.447.630 |
| `4571` | FOMENTO Y APOYO A LA ACTIVIDAD DEPORTIVA | 11.139.456 |
| `4581` | PROMOC. DE LA CULTURA Y PROT. DEL PATRIM. CULTURAL | 10.799.475 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA | 9.862.518 |
| `6312` | CONTROL INTERNO Y CONTABILIDAD | 9.060.599 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 8.878.117 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL | 8.519.618 |
| … | *resto: 53 códigos* | 134.016.338 |

</details>

### 2019

*Fuente: `ingresos_gastos.pdf` · 156 líneas · total extraído **6.193,32 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.006,05 M€ (2.006.052.858 €) · 7 códigos · 32,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 1.870.068.748 | 93,2 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 62.868.694 | 3,1 % |
| `4134` | SALUD PÚBLICA | 33.702.882 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 15.946.519 | 0,8 % |
| `4111` | SERV. GENER. SANIDAD | 11.037.080 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 9.690.000 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.738.935 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.090,32 M€ (1.090.322.967 €) · 11 códigos · 17,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 401.809.651 | 36,9 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 326.686.032 | 30,0 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 175.671.185 | 16,1 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE | 72.028.754 | 6,6 % |
| `4223` | EDUCACIÓN ESPECIAL | 61.964.560 | 5,7 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 26.335.310 | 2,4 % |
| `4225` | EDUCACIÓN PERMANENTE | 11.564.483 | 1,1 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 5.964.617 | 0,5 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 3.957.510 | 0,4 % |
| `4212` | GESTIÓN DE PERSONAL | 2.903.760 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.437.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 642,67 M€ (642.673.405 €) · 6 códigos · 10,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 462.218.850 | 71,9 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 84.987.410 | 13,2 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 45.579.455 | 7,1 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 35.064.890 | 5,5 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 14.388.480 | 2,2 % |
| `7111` | SERV.GEN. DESARROLLO RURAL Y SOSTENIBILIDAD | 434.320 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,20 M€ (2.204.455 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.204.455 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 39,95 M€ (39.953.112 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 34.004.181 | 85,1 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA | 5.948.931 | 14,9 % |

</details>

<details open><summary><b><code>empleo</code> — 117,17 M€ (117.165.149 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 114.110.641 | 97,4 % |
| `6112` | SERV G. ECONOMÍA, INDUSTRIA Y EMPLEO | 3.054.508 | 2,6 % |

</details>

<details open><summary><b><code>idi</code> — 83,68 M€ (83.677.199 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 24.449.064 | 29,2 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 21.472.784 | 25,7 % |
| `4231` | INNOVACIÓN, EQUIDAD Y PARTICIPACIÓN | 16.710.228 | 20,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.709.192 | 16,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 3.925.000 | 4,7 % |
| `5411` | SERV. G. INNOVACIÓN, INVESTIGACIÓN Y UNIVERSIDAD | 3.410.931 | 4,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,62 M€ (1.618.733 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | IGUALDAD Y APOYO A LA INMIGRACIÓN | 1.618.733 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 13,49 M€ (13.489.707 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO *(×2 filas)* | 13.489.707 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,19 M€ (4.194.067 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 4.194.067 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.191,97 M€ · 78 códigos · 35,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.025.540.663 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 388.985.824 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 80.664.921 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 72.931.813 |
| `5131` | CARRETERAS | 66.340.830 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO | 65.960.790 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 59.392.618 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 47.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 36.577.419 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 21.839.418 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 18.146.678 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 17.825.119 |
| `1252` | POLÍTICA TERRITORIAL *(×2 filas)* | 16.019.283 |
| `5132` | TRANSPORTES | 15.050.033 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.573.121 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.384.840 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 14.342.992 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 12.670.395 |
| `6311` | GESTIÓN E INSPECCIÓN DE TRIBUTOS | 11.447.630 |
| `4571` | FOMENTO Y APOYO A LA ACTIVIDAD DEPORTIVA | 11.139.456 |
| `4581` | PROMOC. DE LA CULTURA Y PROT. DEL PATRIM. CULTURAL | 10.799.475 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA | 9.862.518 |
| `6312` | CONTROL INTERNO Y CONTABILIDAD | 9.060.599 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 8.878.117 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL | 8.519.618 |
| … | *resto: 53 códigos* | 134.016.338 |

</details>

### 2020

*Fuente: `ingresos_gastos.pdf` · 162 líneas · total extraído **6.508,65 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.078,64 M€ (2.078.641.796 €) · 7 códigos · 31,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 1.932.541.936 | 93,0 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 67.366.515 | 3,2 % |
| `4134` | SALUD PÚBLICA | 36.362.573 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 16.842.856 | 0,8 % |
| `4111` | SERV. GENER. SANIDAD | 13.012.092 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 9.793.427 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.722.398 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.182,20 M€ (1.182.200.938 €) · 13 códigos · 18,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 423.563.657 | 35,8 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 352.835.494 | 29,8 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 186.321.573 | 15,8 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE | 72.980.818 | 6,2 % |
| `4223` | EDUCACIÓN ESPECIAL | 71.986.891 | 6,1 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 28.303.122 | 2,4 % |
| `4232` | EQUIDAD | 16.140.613 | 1,4 % |
| `4225` | EDUCACIÓN PERMANENTE | 11.776.563 | 1,0 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 5.790.441 | 0,5 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 4.102.202 | 0,3 % |
| `4220` | FORMACIÓN PROFESIONAL | 3.928.684 | 0,3 % |
| `4212` | GESTIÓN DE PERSONAL | 2.983.775 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 651,86 M€ (651.857.327 €) · 6 códigos · 10,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 471.446.330 | 72,3 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 86.285.432 | 13,2 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 31.987.276 | 4,9 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 31.221.166 | 4,8 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 16.026.451 | 2,5 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE | 14.890.671 | 2,3 % |

</details>

<details open><summary><b><code>direccion</code> — 2,47 M€ (2.472.932 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.472.932 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 42,98 M€ (42.982.028 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 34.090.589 | 79,3 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA | 8.891.440 | 20,7 % |

</details>

<details open><summary><b><code>empleo</code> — 120,64 M€ (120.644.676 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 117.038.930 | 97,0 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO | 3.605.746 | 3,0 % |

</details>

<details open><summary><b><code>idi</code> — 71,35 M€ (71.350.540 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 30.173.715 | 42,3 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 22.970.104 | 32,2 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 12.316.538 | 17,3 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 4.075.000 | 5,7 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 1.815.183 | 2,5 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,51 M€ (1.511.098 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.511.098 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 10,81 M€ (10.810.854 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 10.810.854 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,28 M€ (6.276.133 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 6.276.133 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.339,90 M€ · 83 códigos · 36,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.049.218.828 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 407.692.365 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 80.793.866 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 74.680.670 |
| `5131` | CARRETERAS | 66.367.307 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.000.000 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.000.000 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 48.288.234 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 35.222.552 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 22.128.225 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 21.872.063 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 20.217.324 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×2 filas)* | 19.961.985 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 19.071.244 |
| `5132` | TRANSPORTES | 16.922.930 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.384.840 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.116.350 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 14.113.913 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 12.609.923 |
| `3111` | SERV. GRALES. CIUDADANÍA Y DERECHOS SOCIALES | 12.444.317 |
| `6311` | GESTIÓN E INSPECCIÓN DE TRIBUTOS | 12.068.024 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 11.975.544 |
| `1252` | POLÍTICA TERRITORIAL | 10.816.444 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA Y RELACS.INSTIT | 10.571.561 |
| … | *resto: 58 códigos* | 170.840.136 |

</details>

### 2021

*Fuente: `ingresos_gastos.pdf` · 183 líneas · total extraído **7.500,92 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.366,55 M€ (2.366.554.012 €) · 7 códigos · 31,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA *(×2 filas)* | 2.207.360.806 | 93,3 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 70.965.811 | 3,0 % |
| `4134` | SALUD PÚBLICA | 40.649.949 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 20.581.893 | 0,9 % |
| `4111` | SERV. GENER. SANIDAD | 13.971.926 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 10.271.982 | 0,4 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 2.751.646 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.294,79 M€ (1.294.794.241 €) · 13 códigos · 17,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 452.917.479 | 35,0 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 395.738.408 | 30,6 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 195.943.450 | 15,1 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 93.983.214 | 7,3 % |
| `4223` | EDUCACIÓN ESPECIAL | 74.683.344 | 5,8 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 30.611.756 | 2,4 % |
| `4232` | EQUIDAD | 16.432.752 | 1,3 % |
| `4225` | EDUCACIÓN PERMANENTE | 12.200.927 | 0,9 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 9.299.543 | 0,7 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 4.697.004 | 0,4 % |
| `4220` | FORMACIÓN PROFESIONAL | 3.749.135 | 0,3 % |
| `4212` | GESTIÓN DE PERSONAL | 3.050.123 | 0,2 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 673,95 M€ (673.945.493 €) · 6 códigos · 9,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 457.868.423 | 67,9 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 88.659.812 | 13,2 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 49.581.960 | 7,4 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 34.317.705 | 5,1 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE *(×2 filas)* | 27.141.804 | 4,0 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 16.375.790 | 2,4 % |

</details>

<details open><summary><b><code>direccion</code> — 2,51 M€ (2.510.993 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA | 2.510.993 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 48,85 M€ (48.846.603 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 32.660.168 | 66,9 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA *(×2 filas)* | 16.186.434 | 33,1 % |

</details>

<details open><summary><b><code>empleo</code> — 128,59 M€ (128.587.723 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO *(×2 filas)* | 125.529.987 | 97,6 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO | 3.057.736 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 87,92 M€ (87.919.449 €) · 5 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA *(×2 filas)* | 32.740.561 | 37,2 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×3 filas)* | 24.820.104 | 28,2 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN *(×2 filas)* | 18.873.239 | 21,5 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA *(×2 filas)* | 9.050.000 | 10,3 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 2.435.545 | 2,8 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,56 M€ (1.564.165 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.564.165 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 14,16 M€ (14.163.993 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO *(×3 filas)* | 14.163.993 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,18 M€ (6.176.133 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 6.176.133 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.875,86 M€ · 83 códigos · 38,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.435.170.630 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES *(×2 filas)* | 439.342.365 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 85.723.353 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 79.470.168 |
| `5131` | CARRETERAS | 72.688.026 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 64.621.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.009.900 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.000.000 |
| `6121` | PLANIFICACIÓN Y DIRECCIÓN PRESUPUESTARIA *(×2 filas)* | 49.928.108 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 38.650.861 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 36.624.973 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 30.886.815 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×3 filas)* | 26.273.540 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 23.001.329 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 21.990.652 |
| `5132` | TRANSPORTES *(×2 filas)* | 21.625.395 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 20.588.901 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 19.894.903 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 14.459.045 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.035.061 |
| `3111` | SERV. GRALES. CIUDADANÍA Y DERECHOS SOCIALES | 14.022.303 |
| `5426` | ADMINISTRACIÓN ELECTRÓNICA *(×2 filas)* | 12.786.457 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 12.638.911 |
| `6311` | GESTIÓN E INSPECCIÓN DE TRIBUTOS | 12.226.889 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 10.964.665 |
| … | *resto: 58 códigos* | 208.235.549 |

</details>

### 2022

*Fuente: `ingresos_gastos.pdf` · 178 líneas · total extraído **7.496,14 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.250,32 M€ (2.250.319.677 €) · 7 códigos · 30,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 2.097.949.379 | 93,2 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 64.508.527 | 2,9 % |
| `4134` | SALUD PÚBLICA | 39.356.375 | 1,7 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 19.680.457 | 0,9 % |
| `4111` | SERV. GENER. SANIDAD *(×2 filas)* | 14.147.502 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 11.067.430 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 3.610.007 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.311,65 M€ (1.311.647.998 €) · 13 códigos · 17,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 464.343.981 | 35,4 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 398.733.042 | 30,4 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 206.840.833 | 15,8 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 75.962.656 | 5,8 % |
| `4223` | EDUCACIÓN ESPECIAL | 75.832.023 | 5,8 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 29.832.287 | 2,3 % |
| `4232` | EQUIDAD | 15.475.830 | 1,2 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 12.685.520 | 1,0 % |
| `4225` | EDUCACIÓN PERMANENTE | 12.540.856 | 1,0 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 10.990.361 | 0,8 % |
| `4220` | FORMACIÓN PROFESIONAL | 3.756.363 | 0,3 % |
| `4212` | GESTIÓN DE PERSONAL | 3.167.141 | 0,2 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 689,55 M€ (689.552.472 €) · 6 códigos · 9,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 460.764.672 | 66,8 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 98.281.098 | 14,3 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 58.043.361 | 8,4 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 34.766.673 | 5,0 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 20.755.448 | 3,0 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE *(×2 filas)* | 16.941.221 | 2,5 % |

</details>

<details open><summary><b><code>direccion</code> — 2,52 M€ (2.521.555 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA *(×2 filas)* | 2.521.555 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 51,68 M€ (51.683.922 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 43.715.671 | 84,6 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA *(×2 filas)* | 7.968.251 | 15,4 % |

</details>

<details open><summary><b><code>empleo</code> — 126,18 M€ (126.175.339 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 122.879.490 | 97,4 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO *(×2 filas)* | 3.295.850 | 2,6 % |

</details>

<details open><summary><b><code>idi</code> — 78,95 M€ (78.952.585 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 30.920.776 | 39,2 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 28.529.453 | 36,1 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 12.824.452 | 16,2 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 4.650.000 | 5,9 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 2.027.903 | 2,6 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,56 M€ (1.558.191 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.558.191 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 30,75 M€ (30.748.157 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 30.748.157 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,18 M€ (9.184.305 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 9.184.305 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.943,80 M€ · 83 códigos · 39,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.507.582.787 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 396.786.192 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 86.213.998 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 77.796.328 |
| `5131` | CARRETERAS | 74.518.283 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 59.609.900 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 54.365.380 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.000.000 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 35.771.205 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 30.573.473 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 30.398.970 |
| `6111` | SERV. GEN. DE HACIENDA Y ADMINISTRACIÓN PÚBLICA *(×3 filas)* | 28.592.940 |
| `3111` | SERV. GRALES. CIUDADANÍA Y DERECHOS SOCIALES *(×2 filas)* | 27.217.786 |
| `7231` | FOMENTO INDUSTRIAL | 24.333.662 |
| `5132` | TRANSPORTES | 23.443.853 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 22.466.851 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 22.006.247 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 20.385.570 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 19.740.230 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×2 filas)* | 19.656.923 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 16.817.149 |
| `1252` | POLÍTICA TERRITORIAL *(×2 filas)* | 15.923.799 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.042.890 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA Y RELACS.INSTIT *(×2 filas)* | 13.301.765 |
| … | *resto: 58 códigos* | 208.730.792 |

</details>

### 2023

*Fuente: `ingresos_gastos.pdf` · 178 líneas · total extraído **8.307,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.557,97 M€ (2.557.966.488 €) · 7 códigos · 30,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 2.373.095.081 | 92,8 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 76.526.167 | 3,0 % |
| `4134` | SALUD PÚBLICA | 48.055.903 | 1,9 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 23.121.281 | 0,9 % |
| `4111` | SERV. GENER. SANIDAD *(×2 filas)* | 15.976.577 | 0,6 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 11.159.128 | 0,4 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 10.032.351 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 1.373,14 M€ (1.373.141.920 €) · 13 códigos · 16,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 480.923.284 | 35,0 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 416.017.266 | 30,3 % |
| `4228` | EDUCACIÓN UNIVERSITARIA *(×2 filas)* | 220.274.722 | 16,0 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 93.334.814 | 6,8 % |
| `4223` | EDUCACIÓN ESPECIAL | 78.815.006 | 5,7 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 30.588.808 | 2,2 % |
| `4232` | EQUIDAD | 15.447.104 | 1,1 % |
| `4225` | EDUCACIÓN PERMANENTE | 13.155.022 | 1,0 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 10.103.480 | 0,7 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 5.411.216 | 0,4 % |
| `4220` | FORMACIÓN PROFESIONAL | 4.029.727 | 0,3 % |
| `4212` | GESTIÓN DE PERSONAL | 3.554.366 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 715,07 M€ (715.069.103 €) · 6 códigos · 8,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 461.636.875 | 64,6 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 114.608.312 | 16,0 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 59.329.733 | 8,3 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENT. | 36.096.228 | 5,0 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 25.146.993 | 3,5 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE *(×2 filas)* | 18.250.961 | 2,6 % |

</details>

<details open><summary><b><code>direccion</code> — 2,77 M€ (2.768.334 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA *(×2 filas)* | 2.768.334 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 101,30 M€ (101.296.832 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA | 91.021.180 | 89,9 % |
| `5111` | SERV.G. VERTEB. TERRITORRIO, MOVILIDAD Y VIVIENDA *(×2 filas)* | 10.275.652 | 10,1 % |

</details>

<details open><summary><b><code>empleo</code> — 160,28 M€ (160.280.812 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 156.878.630 | 97,9 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO *(×2 filas)* | 3.402.182 | 2,1 % |

</details>

<details open><summary><b><code>idi</code> — 79,78 M€ (79.775.764 €) · 5 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 28.988.260 | 36,3 % |
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 26.574.786 | 33,3 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 16.963.354 | 21,3 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 4.049.365 | 5,1 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA | 3.200.000 | 4,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,59 M€ (1.588.071 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.588.071 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 52,71 M€ (52.714.983 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 52.714.983 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,25 M€ (8.254.418 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 8.254.418 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.254,30 M€ · 83 códigos · 39,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.481.112.768 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 416.560.196 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 129.395.111 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 93.880.601 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×2 filas)* | 92.186.053 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 88.765.675 |
| `5131` | CARRETERAS | 79.326.211 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 66.485.094 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.009.900 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.800.000 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 49.974.722 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 42.383.378 |
| `3111` | SERV. GRALES. CIUDADANÍA Y DERECHOS SOCIALES *(×2 filas)* | 37.711.676 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE | 32.287.964 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 31.991.615 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 31.726.167 |
| `5132` | TRANSPORTES | 29.640.217 |
| `7231` | FOMENTO INDUSTRIAL | 23.698.225 |
| `4422` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 23.529.130 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×2 filas)* | 22.544.614 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 21.261.603 |
| `1252` | POLÍTICA TERRITORIAL | 20.802.267 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 13.874.244 |
| `1211` | SERVICIOS GENERALES DE PRESIDENCIA Y RELACS.INSTIT *(×2 filas)* | 13.680.295 |
| … | *resto: 58 códigos* | 237.149.012 |

</details>

### 2024

*Fuente: `ingresos_gastos.pdf` · 194 líneas · total extraído **8.610,35 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.771,99 M€ (2.771.994.759 €) · 8 códigos · 32,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 2.585.125.203 | 93,3 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 67.486.561 | 2,4 % |
| `4134` | SALUD PÚBLICA | 51.868.433 | 1,9 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 27.047.777 | 1,0 % |
| `4111` | SERVICIOS GENERALES SANIDAD | 14.872.593 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 13.378.811 | 0,5 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 11.366.180 | 0,4 % |
| `4111` | SERV. GENER. SANIDAD | 849.201 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.519,82 M€ (1.519.817.440 €) · 13 códigos · 17,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 525.921.434 | 34,6 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 480.198.978 | 31,6 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 221.507.853 | 14,6 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 99.188.819 | 6,5 % |
| `4223` | EDUCACIÓN ESPECIAL | 97.636.420 | 6,4 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 34.357.723 | 2,3 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 18.394.398 | 1,2 % |
| `4225` | EDUCACIÓN PERMANENTE | 14.552.483 | 1,0 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 8.962.433 | 0,6 % |
| `4232` | EQUIDAD | 8.896.323 | 0,6 % |
| `4212` | GESTIÓN DE PERSONAL | 4.377.197 | 0,3 % |
| `4220` | FORMACIÓN PROFESIONAL | 4.336.275 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 735,05 M€ (735.047.604 €) · 8 códigos · 8,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 465.005.695 | 63,3 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 131.207.572 | 17,9 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 58.448.289 | 8,0 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENTALES | 35.350.714 | 4,8 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 23.860.213 | 3,2 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE | 16.891.949 | 2,3 % |
| `7111` | SERVICIOS GENERALES AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 2.829.667 | 0,4 % |
| `7129` | CAZA Y PESCA | 1.453.506 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 2,86 M€ (2.861.118 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA *(×2 filas)* | 2.861.118 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 53,88 M€ (53.876.321 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA *(×2 filas)* | 40.454.436 | 75,1 % |
| `5111` | SERVICIOS GENERALES FOMENTO, VIVIENDA, MOVILIDAD Y LOGÍSTICA *(×2 filas)* | 13.421.885 | 24,9 % |

</details>

<details open><summary><b><code>empleo</code> — 168,90 M€ (168.897.467 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 157.761.887 | 93,4 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO | 10.084.365 | 6,0 % |
| `6112` | SERVICIOS GENERALES ECONOMÍA, EMPLEO E INDUSTRIA | 1.051.215 | 0,6 % |

</details>

<details open><summary><b><code>idi</code> — 77,19 M€ (77.187.952 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 27.936.786 | 36,2 % |
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 27.799.487 | 36,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.863.534 | 18,0 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 4.181.144 | 5,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA *(×2 filas)* | 3.407.000 | 4,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,11 M€ (16.110.911 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4133` | SALUD MENTAL | 16.110.911 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,76 M€ (1.758.176 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.758.176 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 89,00 M€ (88.996.833 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 75.009.306 | 84,3 % |
| `4421` | SERV. GENER. MEDIO AMBIENTE Y TURISMO *(×3 filas)* | 13.987.527 | 15,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,23 M€ (16.225.351 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 9.207.949 | 56,8 % |
| `3133` | POLÍTICA INTEGRAL DE APOYO A LAS FAMILIAS Y DE IGUALDAD | 5.854.214 | 36,1 % |
| `3137` | IGUALDAD DE OPORTUNIDADES | 1.163.189 | 7,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.157,58 M€ · 87 códigos · 36,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.232.560.614 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 455.841.325 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 154.374.180 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×3 filas)* | 111.826.845 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 103.953.434 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 93.749.978 |
| `5131` | CARRETERAS *(×2 filas)* | 80.972.480 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 73.391.843 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 51.144.715 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.800.000 |
| `5132` | TRANSPORTES | 45.900.180 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 40.000.000 |
| `3111` | SERVICIOS GENERALES BIENESTAR SOCIAL Y FAMILIA *(×2 filas)* | 33.732.138 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 33.573.776 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×3 filas)* | 33.220.809 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 31.212.743 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE *(×2 filas)* | 30.846.657 |
| `1260` | DESPOBLACIÓN *(×2 filas)* | 23.000.260 |
| `1252` | POLÍTICA TERRITORIAL | 21.882.134 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 21.513.268 |
| `7231` | FOMENTO INDUSTRIAL | 20.660.198 |
| `4424` | CALIDAD AMBIENTAL | 20.081.736 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 14.801.276 |
| … | *resto: 62 códigos* | 255.013.585 |

</details>

### 2025

*Fuente: `ingresos_gastos.pdf` · 194 líneas · total extraído **8.610,35 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.771,99 M€ (2.771.994.759 €) · 8 códigos · 32,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 2.585.125.203 | 93,3 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 67.486.561 | 2,4 % |
| `4134` | SALUD PÚBLICA | 51.868.433 | 1,9 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 27.047.777 | 1,0 % |
| `4111` | SERVICIOS GENERALES SANIDAD | 14.872.593 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 13.378.811 | 0,5 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 11.366.180 | 0,4 % |
| `4111` | SERV. GENER. SANIDAD | 849.201 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.519,82 M€ (1.519.817.440 €) · 13 códigos · 17,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 525.921.434 | 34,6 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 480.198.978 | 31,6 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 221.507.853 | 14,6 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 99.188.819 | 6,5 % |
| `4223` | EDUCACIÓN ESPECIAL | 97.636.420 | 6,4 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 34.357.723 | 2,3 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 18.394.398 | 1,2 % |
| `4225` | EDUCACIÓN PERMANENTE | 14.552.483 | 1,0 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 8.962.433 | 0,6 % |
| `4232` | EQUIDAD | 8.896.323 | 0,6 % |
| `4212` | GESTIÓN DE PERSONAL | 4.377.197 | 0,3 % |
| `4220` | FORMACIÓN PROFESIONAL | 4.336.275 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 735,05 M€ (735.047.604 €) · 8 códigos · 8,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 465.005.695 | 63,3 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 131.207.572 | 17,9 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 58.448.289 | 8,0 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENTALES | 35.350.714 | 4,8 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 23.860.213 | 3,2 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE | 16.891.949 | 2,3 % |
| `7111` | SERVICIOS GENERALES AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 2.829.667 | 0,4 % |
| `7129` | CAZA Y PESCA | 1.453.506 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 2,86 M€ (2.861.118 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA *(×2 filas)* | 2.861.118 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 53,88 M€ (53.876.321 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA *(×2 filas)* | 40.454.436 | 75,1 % |
| `5111` | SERVICIOS GENERALES FOMENTO, VIVIENDA, MOVILIDAD Y LOGÍSTICA *(×2 filas)* | 13.421.885 | 24,9 % |

</details>

<details open><summary><b><code>empleo</code> — 168,90 M€ (168.897.467 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 157.761.887 | 93,4 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO | 10.084.365 | 6,0 % |
| `6112` | SERVICIOS GENERALES ECONOMÍA, EMPLEO E INDUSTRIA | 1.051.215 | 0,6 % |

</details>

<details open><summary><b><code>idi</code> — 77,19 M€ (77.187.952 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 27.936.786 | 36,2 % |
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 27.799.487 | 36,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.863.534 | 18,0 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 4.181.144 | 5,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA *(×2 filas)* | 3.407.000 | 4,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,11 M€ (16.110.911 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4133` | SALUD MENTAL | 16.110.911 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,76 M€ (1.758.176 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.758.176 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 89,00 M€ (88.996.833 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 75.009.306 | 84,3 % |
| `4421` | SERV. GENER. MEDIO AMBIENTE Y TURISMO *(×3 filas)* | 13.987.527 | 15,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,23 M€ (16.225.351 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 9.207.949 | 56,8 % |
| `3133` | POLÍTICA INTEGRAL DE APOYO A LAS FAMILIAS Y DE IGUALDAD | 5.854.214 | 36,1 % |
| `3137` | IGUALDAD DE OPORTUNIDADES | 1.163.189 | 7,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.157,58 M€ · 87 códigos · 36,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.232.560.614 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 455.841.325 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 154.374.180 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×3 filas)* | 111.826.845 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 103.953.434 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 93.749.978 |
| `5131` | CARRETERAS *(×2 filas)* | 80.972.480 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 73.391.843 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 51.144.715 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.800.000 |
| `5132` | TRANSPORTES | 45.900.180 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 40.000.000 |
| `3111` | SERVICIOS GENERALES BIENESTAR SOCIAL Y FAMILIA *(×2 filas)* | 33.732.138 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 33.573.776 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×3 filas)* | 33.220.809 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 31.212.743 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE *(×2 filas)* | 30.846.657 |
| `1260` | DESPOBLACIÓN *(×2 filas)* | 23.000.260 |
| `1252` | POLÍTICA TERRITORIAL | 21.882.134 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 21.513.268 |
| `7231` | FOMENTO INDUSTRIAL | 20.660.198 |
| `4424` | CALIDAD AMBIENTAL | 20.081.736 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 14.801.276 |
| … | *resto: 62 códigos* | 255.013.585 |

</details>

### 2026

*Fuente: `ingresos_gastos.pdf` · 194 líneas · total extraído **8.610,35 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.771,99 M€ (2.771.994.759 €) · 8 códigos · 32,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4121` | ASISTENCIA SANITARIA | 2.585.125.203 | 93,3 % |
| `4131` | PROTECCIÓN Y PROMOCIÓN DE LA SALUD | 67.486.561 | 2,4 % |
| `4134` | SALUD PÚBLICA | 51.868.433 | 1,9 % |
| `5425` | INVESTIGACIÓN Y DESARROLLO EN EL ÁREA DE LA SALUD *(×2 filas)* | 27.047.777 | 1,0 % |
| `4111` | SERVICIOS GENERALES SANIDAD | 14.872.593 | 0,5 % |
| `4132` | SERVICIOS DE ATENCIÓN AL USUARIO | 13.378.811 | 0,5 % |
| `4124` | PRODUCC. COMPONENTES SANGUÍNEOS Y DE TEJIDOS | 11.366.180 | 0,4 % |
| `4111` | SERV. GENER. SANIDAD | 849.201 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.519,82 M€ (1.519.817.440 €) · 13 códigos · 17,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | EDUC SECUNDARIA | 525.921.434 | 34,6 % |
| `4221` | EDUCACIÓN INFANTIL Y PRIMARIA | 480.198.978 | 31,6 % |
| `4228` | EDUCACIÓN UNIVERSITARIA | 221.507.853 | 14,6 % |
| `4211` | SERVICIOS GENERALES EDUCACIÓN, CULTURA Y DEPORTE *(×2 filas)* | 99.188.819 | 6,5 % |
| `4223` | EDUCACIÓN ESPECIAL | 97.636.420 | 6,4 % |
| `4224` | ENSEÑANZAS ARTÍSTICAS | 34.357.723 | 2,3 % |
| `4226` | PLAN ARAGONÉS DE FORMACIÓN PROFESIONAL | 18.394.398 | 1,2 % |
| `4225` | EDUCACIÓN PERMANENTE | 14.552.483 | 1,0 % |
| `4227` | FORMACIÓN DEL PROFESORADO | 8.962.433 | 0,6 % |
| `4232` | EQUIDAD | 8.896.323 | 0,6 % |
| `4212` | GESTIÓN DE PERSONAL | 4.377.197 | 0,3 % |
| `4220` | FORMACIÓN PROFESIONAL | 4.336.275 | 0,3 % |
| `4229` | EVALUACIÓN DE LA CALIDAD DE LA ENSEÑANZA SUPERIOR *(×2 filas)* | 1.487.105 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 735,05 M€ (735.047.604 €) · 8 códigos · 8,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7123` | PRODUCCIÓN AGRARIA Y GESTIÓN DE AYUDAS | 465.005.695 | 63,3 % |
| `5311` | MEJORA DE ESTRUCTURAS AGRARIAS Y DESARROLLO RURAL | 131.207.572 | 17,9 % |
| `7121` | DESARROLLO AGROALIMENTARIO Y FOMENTO ASOCIATIVO | 58.448.289 | 8,0 % |
| `7122` | COORDINACIÓN Y GESTIÓN DE SERVICIOS AGROAMBIENTALES | 35.350.714 | 4,8 % |
| `7161` | CALIDAD Y SEGURIDAD ALIMENTARIA | 23.860.213 | 3,2 % |
| `7111` | SERV.GEN. AGRICULTURA, GANADERÍA Y MEDIO AMBIENTE | 16.891.949 | 2,3 % |
| `7111` | SERVICIOS GENERALES AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 2.829.667 | 0,4 % |
| `7129` | CAZA Y PESCA | 1.453.506 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 2,86 M€ (2.861.118 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1121` | PRESIDENCIA Y ÓRGANOS DE LA PRESIDENCIA *(×2 filas)* | 2.861.118 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 53,88 M€ (53.876.321 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | GESTIÓN SOCIAL DE LA VIVIENDA *(×2 filas)* | 40.454.436 | 75,1 % |
| `5111` | SERVICIOS GENERALES FOMENTO, VIVIENDA, MOVILIDAD Y LOGÍSTICA *(×2 filas)* | 13.421.885 | 24,9 % |

</details>

<details open><summary><b><code>empleo</code> — 168,90 M€ (168.897.467 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3221` | FOMENTO DEL EMPLEO. INSTITUTO ARAGONÉS DE EMPLEO | 157.761.887 | 93,4 % |
| `6112` | SERV. GENERALES ECONOMÍA, PLANIFICACIÓN Y EMPLEO | 10.084.365 | 6,0 % |
| `6112` | SERVICIOS GENERALES ECONOMÍA, EMPLEO E INDUSTRIA | 1.051.215 | 0,6 % |

</details>

<details open><summary><b><code>idi</code> — 77,19 M€ (77.187.952 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5421` | INVESTIGACIÓN AGROALIMENTARIA *(×2 filas)* | 27.936.786 | 36,2 % |
| `5423` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN TECNOLÓGICA | 27.799.487 | 36,0 % |
| `5424` | INVESTIGACIÓN Y DLLO. SOCIEDAD DE LA INFORMACIÓN | 13.863.534 | 18,0 % |
| `4231` | INNOVACIÓN Y PARTICIPACIÓN | 4.181.144 | 5,4 % |
| `5422` | INVESTIGACIÓN Y TECNOLOGÍA APLICADA A LA INDUSTRIA *(×2 filas)* | 3.407.000 | 4,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,11 M€ (16.110.911 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4133` | SALUD MENTAL | 16.110.911 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,76 M€ (1.758.176 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3241` | APOYO A LA INMIGRACIÓN | 1.758.176 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 89,00 M€ (88.996.833 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | ORDENACIÓN, PROMOCIÓN Y FOMENTO DEL TURISMO | 75.009.306 | 84,3 % |
| `4421` | SERV. GENER. MEDIO AMBIENTE Y TURISMO *(×3 filas)* | 13.987.527 | 15,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,23 M€ (16.225.351 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3232` | PROMOCIÓN DE LA MUJER | 9.207.949 | 56,8 % |
| `3133` | POLÍTICA INTEGRAL DE APOYO A LAS FAMILIAS Y DE IGUALDAD | 5.854.214 | 36,1 % |
| `3137` | IGUALDAD DE OPORTUNIDADES | 1.163.189 | 7,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.157,58 M€ · 87 códigos · 36,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA | 1.232.560.614 |
| `3132` | GESTIÓN Y DESARROLLO DE LOS SERVICIOS SOCIALES | 455.841.325 |
| `6128` | FONDO DE GASTOS DE PERSONAL | 154.374.180 |
| `5121` | GESTIÓN E INFRAESTRUCTURA DE RECURSOS HIDRÁULICOS *(×3 filas)* | 111.826.845 |
| `7311` | FOMENTO Y GESTIÓN ENERGÉTICA | 103.953.434 |
| `1421` | SERVICIOS DE ADMINISTRACIÓN DE JUSTICIA | 93.749.978 |
| `5131` | CARRETERAS *(×2 filas)* | 80.972.480 |
| `6126` | APOYO AL DESARROLLO ECONÓMICO Y SOCIAL *(×2 filas)* | 73.391.843 |
| `9111` | TRANSFERENCIAS A ADMINISTRACIONES COMARCALES *(×33 filas)* | 63.521.436 |
| `6120` | FONDO INVERSIONES DE TERUEL | 60.000.000 |
| `5331` | PROTECCIÓN Y MEJORA DEL MEDIO NATURAL | 51.144.715 |
| `1266` | TELEVISIÓN Y RADIO AUTONÓMICAS | 50.800.000 |
| `5132` | TRANSPORTES | 45.900.180 |
| `6129` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 40.000.000 |
| `3111` | SERVICIOS GENERALES BIENESTAR SOCIAL Y FAMILIA *(×2 filas)* | 33.732.138 |
| `1251` | APOYO A LA ADMINISTRACIÓN LOCAL | 33.573.776 |
| `6122` | PROMOCIÓN Y DESARROLLO ECONÓMICO *(×3 filas)* | 33.220.809 |
| `1265` | SERVICIOS TELEMÁTICOS *(×2 filas)* | 31.212.743 |
| `5332` | CONSERVAC. DE LA BIODIVERS Y DESARROLLO SOSTENIBLE *(×2 filas)* | 30.846.657 |
| `1260` | DESPOBLACIÓN *(×2 filas)* | 23.000.260 |
| `1252` | POLÍTICA TERRITORIAL | 21.882.134 |
| `1111` | CORTES DE ARAGÓN (ACTIVIDAD LEGISLATIVA) | 21.513.268 |
| `7231` | FOMENTO INDUSTRIAL | 20.660.198 |
| `4424` | CALIDAD AMBIENTAL | 20.081.736 |
| `4521` | ARCHIVOS, MUSEOS Y BIBLIOTECAS | 14.801.276 |
| … | *resto: 62 códigos* | 255.013.585 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py ara     # regenera este documento
python3 tools/auditoria_magnitud.py ara        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa ara --anio <año> \
    --input ../fuentes/raw/ara/<año>/<fichero> --output /tmp/ara.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-ara.md`](limitaciones-ara.md)

