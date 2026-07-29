# Trazabilidad de la extracción — La Rioja (`lar`)

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
| **2015** | 69 | `funcional_economico.pdf` | 10 | 75,4 % | 1.284,25 | — | no_aplica |
| **2016** | 70 | `funcional_economico.pdf` | 11 | 77,1 % | 1.334,19 | — | no_aplica |
| **2017** | 74 | `funcional_economico.pdf` | 12 | 50,0 % | 1.452,54 | — | no_aplica |
| **2018** | 72 | `funcional_economico.pdf` | 12 | 51,4 % | 1.485,41 | — | no_aplica |
| **2019** | 73 | `funcional_economico.pdf` | 12 | 46,6 % | 1.533,40 | — | no_aplica |
| **2020** | 76 | `funcional_economico.pdf` | 11 | 40,8 % | 1.555,78 | — | no_aplica |
| **2021** | 81 | `funcional_economico.pdf` | 12 | 44,4 % | 1.809,33 | — | no_aplica |
| **2022** | 64 | `funcional_economico.pdf` | 12 | 48,4 % | 1.823,60 | — | no_aplica |
| **2023** | 62 | `detalle_gastos_funcional_economico.pdf` | 12 | 48,4 % | 1.732,17 | — | no_aplica |
| **2024** | 76 | `funcional_economico.pdf` | 13 | 46,1 % | 1.947,38 | — | no_aplica |
| **2025** | 58 | `funcional_economico.pdf` | 13 | 58,6 % | 2.014,04 | — | no_aplica |
| **2026** | 60 | `funcional_economico.pdf` | 13 | 51,7 % | 2.030,15 | — | no_aplica |

**URL(s) de origen:**
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1002276>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1063098>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1195165>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1281489>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1363191>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1455005>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1525461>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1664271>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=1683255>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=623978>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=763995>
- <https://www.larioja.org/larioja-client/cm/hacienda/images?idMmedia=967050>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 397,01 | 406,96 | 408,22 | 425,01 | 435,49 | 454,04 | 529,04 | 524,39 | 546,72 | 592,30 | 640,74 | 637,06 |
| `educacion` | 233,36 | 256,50 | 260,23 | 277,15 | 290,20 | 299,55 | 345,05 | 347,81 | 368,05 | 403,16 | 434,73 | 428,44 |
| `soberania` | 53,34 | 57,79 | 64,08 | 62,50 | 63,35 | 59,64 | 73,57 | 74,23 | 74,84 | 90,60 | 97,03 | 97,03 |
| `direccion` | 55,71 | 57,66 | 5,18 | 5,18 | 7,64 | 8,53 | 8,35 | 8,69 | 8,69 | 9,22 | 9,98 | 9,98 |
| `vivienda` | 6,99 | 6,22 | 11,08 | 11,19 | 11,74 | 11,99 | 19,36 | 19,43 | 21,53 | 30,99 | 28,38 | 28,38 |
| `empleo` | 63,42 | 27,49 | 22,17 | 22,91 | 22,61 | 20,72 | 25,99 | 24,80 | 27,50 | 29,00 | 27,16 | 27,16 |
| `idi` | 76,29 | 73,30 | 76,24 | 51,93 | 53,14 | 80,66 | 72,18 | 106,08 | 111,74 | 107,03 | 113,57 | 113,05 |
| `dependencia` | 90,57 | 91,62 | 71,06 | 71,46 | 58,82 | 59,36 | 68,20 | 72,09 | 77,43 | 82,75 | 89,18 | 89,18 |
| `discapacidad` | 15,97 | 15,99 | 22,29 | 22,10 | 22,66 | 21,77 | 25,40 | 24,28 | 25,88 | 28,38 | 29,80 | 29,80 |
| `salud_mental` | — | — | — | — | — | — | — | — | — | 1,57 | 1,64 | 1,64 |
| `diversidad` | — | — | 9,91 | 9,45 | 9,49 | 12,43 | 14,91 | 10,51 | 10,49 | 8,66 | 3,89 | 3,89 |
| `turismo` | 32,34 | 28,70 | 43,82 | 44,82 | 45,27 | — | 58,00 | 35,38 | 42,79 | 62,87 | 47,76 | 47,82 |
| `igualdad` | — | 5,23 | 1,72 | 1,97 | 2,64 | 2,86 | 2,93 | 19,35 | 18,55 | 4,46 | 3,86 | 4,36 |
| **Σ asignado** | 1.025,00 | 1.027,48 | 996,01 | 1.005,68 | 1.023,05 | 1.031,54 | 1.242,98 | 1.267,03 | 1.334,22 | 1.450,99 | 1.527,70 | 1.517,77 |
| *(sin concepto)* | 259,25 | 306,71 | 456,52 | 479,73 | 510,35 | 524,24 | 566,36 | 556,57 | 397,95 | 496,38 | 486,34 | 512,38 |
| **TOTAL extraído** | 1.284,25 | 1.334,19 | 1.452,54 | 1.485,41 | 1.533,40 | 1.555,78 | 1.809,33 | 1.823,60 | 1.732,17 | 1.947,38 | 2.014,04 | 2.030,15 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +2,5 % | +0,3 % | +4,1 % | +2,5 % | +4,3 % | +16,5 % | −0,9 % | +4,3 % | +8,3 % | +8,2 % | −0,6 % |
| `educacion` | +9,9 % | +1,5 % | +6,5 % | +4,7 % | +3,2 % | +15,2 % | +0,8 % | +5,8 % | +9,5 % | +7,8 % | −1,4 % |
| `soberania` | +8,3 % | +10,9 % | −2,5 % | +1,4 % | −5,9 % | +23,4 % | +0,9 % | +0,8 % | +21,1 % | +7,1 % | +0,0 % |
| `direccion` | +3,5 % | −91,0 % ⚠ | +0,0 % | +47,6 % ⚠ | +11,7 % | −2,1 % | +4,0 % | +0,0 % | +6,1 % | +8,3 % | +0,0 % |
| `vivienda` | −11,0 % | +78,2 % ⚠ | +1,0 % | +4,8 % | +2,1 % | +61,5 % ⚠ | +0,4 % | +10,8 % | +43,9 % ⚠ | −8,4 % | +0,0 % |
| `empleo` | −56,7 % ⚠ | −19,4 % | +3,4 % | −1,3 % | −8,4 % | +25,4 % | −4,6 % | +10,9 % | +5,5 % | −6,4 % | +0,0 % |
| `idi` | −3,9 % | +4,0 % | −31,9 % | +2,3 % | +51,8 % ⚠ | −10,5 % | +47,0 % ⚠ | +5,3 % | −4,2 % | +6,1 % | −0,5 % |
| `dependencia` | +1,2 % | −22,4 % | +0,6 % | −17,7 % | +0,9 % | +14,9 % | +5,7 % | +7,4 % | +6,9 % | +7,8 % | +0,0 % |
| `discapacidad` | +0,1 % | +39,4 % | −0,9 % | +2,5 % | −3,9 % | +16,7 % | −4,4 % | +6,6 % | +9,6 % | +5,0 % | +0,0 % |
| `salud_mental` | · | · | · | · | · | · | · | · | **nuevo** ⛔ | +4,5 % | +0,0 % |
| `diversidad` | · | **nuevo** ⛔ | −4,7 % | +0,5 % | +31,0 % | +20,0 % | −29,5 % | −0,2 % | −17,4 % | −55,1 % ⚠ | +0,0 % |
| `turismo` | −11,3 % | +52,7 % ⚠ | +2,3 % | +1,0 % | **a 0** ⛔ | **nuevo** ⛔ | −39,0 % | +21,0 % | +46,9 % ⚠ | −24,0 % | +0,1 % |
| `igualdad` | **nuevo** ⛔ | −67,1 % ⚠ | +14,3 % | +34,1 % | +8,3 % | +2,2 % | +561,1 % ⚠ | −4,1 % | −75,9 % ⚠ | −13,5 % | +12,9 % |
| **TOTAL** | +3,9 % | +8,9 % | +2,3 % | +3,2 % | +1,5 % | +16,3 % | +0,8 % | −5,0 % | +12,4 % | +3,4 % | +0,8 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `empleo` | **SALTO** | 63,42 → 27,49 M€ (−56,7 % ⚠) |
| 2017 | `direccion` | **SALTO** | 57,66 → 5,18 M€ (−91,0 % ⚠) |
| 2017 | `diversidad` | **APARECE** | 0 → 9,91 M€ |
| 2017 | `turismo` | **SALTO** | 28,70 → 43,82 M€ (+52,7 % ⚠) |
| 2017 | `vivienda` | **SALTO** | 6,22 → 11,08 M€ (+78,2 % ⚠) |
| 2020 | `idi` | **SALTO** | 53,14 → 80,66 M€ (+51,8 % ⚠) |
| 2020 | `turismo` | **DESAPARECE** | 45,27 M€ → 0 |
| 2021 | `turismo` | **APARECE** | 0 → 58,00 M€ |
| 2021 | `vivienda` | **SALTO** | 11,99 → 19,36 M€ (+61,5 % ⚠) |
| 2022 | `idi` | **SALTO** | 72,18 → 106,08 M€ (+47,0 % ⚠) |
| 2022 | `igualdad` | **SALTO** | 2,93 → 19,35 M€ (+561,1 % ⚠) |
| 2024 | `igualdad` | **SALTO** | 18,55 → 4,46 M€ (−75,9 % ⚠) |
| 2024 | `turismo` | **SALTO** | 42,79 → 62,87 M€ (+46,9 % ⚠) |
| 2024 | `vivienda` | **SALTO** | 21,53 → 30,99 M€ (+43,9 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (26 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `3.1.2.2` | 409,73 | 2015:discapacidad, 2016:discapacidad, 2017:sanidad, 2018:sanidad, 2019:sanidad, 2020:sanidad, 2021:sanidad, 2022:sanidad, 2023:sanidad, 2024:sanidad, 2025:sanidad, 2026:sanidad |
| `3.2.2.1` | 315,33 | 2015:empleo, 2016:empleo, 2017:educacion, 2018:educacion, 2019:educacion, 2020:educacion, 2021:educacion, 2022:educacion, 2023:educacion, 2024:educacion, 2025:educacion, 2026:educacion |
| `4.1.2.2` | 272,44 | 2015:sanidad, 2016:sanidad, 2017:soberania, 2018:soberania, 2019:soberania, 2020:soberania, 2021:soberania, 2022:soberania, 2023:soberania, 2024:soberania, 2025:soberania, 2026:soberania |
| `4.2.2.1` | 207,79 | 2015:educacion, 2016:educacion, 2020:(sin concepto), 2021:(sin concepto), 2024:(sin concepto) |
| `3.1.2.1` | 198,55 | 2015:dependencia, 2016:dependencia, 2017:sanidad, 2018:sanidad, 2019:sanidad, 2020:sanidad, 2021:sanidad, 2022:sanidad, 2023:sanidad, 2024:sanidad, 2025:sanidad, 2026:sanidad |
| `4.1.2.1` | 117,99 | 2015:sanidad, 2016:sanidad, 2017:soberania, 2018:soberania, 2019:soberania, 2020:soberania, 2021:soberania, 2022:soberania, 2023:soberania, 2024:soberania, 2025:soberania, 2026:soberania |
| `3.2.2.2` | 98,46 | 2015:empleo, 2016:empleo, 2017:educacion, 2018:educacion, 2019:educacion, 2020:educacion, 2021:educacion, 2022:educacion, 2023:educacion, 2024:educacion, 2025:educacion, 2026:educacion |
| `4.2.1.1` | 32,98 | 2015:educacion, 2016:educacion, 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `1.4.1.1` | 26,74 | 2015:direccion, 2016:direccion, 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `1.1.1.1` | 23,40 | 2015:direccion, 2016:direccion, 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `2.3.2.5` | 23,24 | 2017:dependencia, 2018:dependencia, 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `2.3.2.4` | 18,59 | 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:igualdad, 2023:igualdad, 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `4.3.1.1` | 14,96 | 2015:vivienda, 2016:vivienda, 2017:soberania, 2018:soberania, 2019:soberania, 2020:soberania, 2021:soberania, 2022:soberania, 2023:soberania, 2024:soberania, 2025:soberania, 2026:soberania |
| `3.1.2.3` | 12,67 | 2015:dependencia, 2016:dependencia, 2017:sanidad, 2018:sanidad, 2019:sanidad, 2020:sanidad, 2021:sanidad, 2022:sanidad, 2024:sanidad, 2025:sanidad, 2026:sanidad |
| `4.1.2.3` | 10,95 | 2015:sanidad, 2016:sanidad, 2017:soberania, 2018:soberania, 2019:soberania, 2020:soberania, 2021:soberania, 2022:soberania, 2023:soberania, 2024:soberania, 2025:soberania, 2026:soberania |
| `1.3.1.1` | 10,21 | 2015:direccion, 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `4.7.1.1` | 8,11 | 2017:(sin concepto), 2018:educacion, 2020:(sin concepto), 2021:(sin concepto), 2024:(sin concepto) |
| `3.1.1.1` | 6,49 | 2016:igualdad, 2017:sanidad, 2018:sanidad, 2019:sanidad, 2020:sanidad, 2021:sanidad, 2022:sanidad, 2023:sanidad, 2024:sanidad, 2025:sanidad, 2026:sanidad |
| `6.1.1.1` | 5,73 | 2015:(sin concepto), 2016:direccion |
| `4.1.1.1` | 5,66 | 2015:sanidad, 2016:sanidad, 2017:soberania, 2018:soberania, 2019:soberania, 2020:soberania, 2021:soberania, 2024:soberania |
| `4.2.1.3` | 3,58 | 2017:soberania, 2018:soberania, 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto) |
| `1.3.1.2` | 2,07 | 2015:direccion, 2016:direccion, 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `5.1.3.3` | 1,96 | 2015:(sin concepto), 2016:direccion |
| `2.3.3.2` | 1,55 | 2020:igualdad, 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto) |
| `7.2.1.1` | 0,97 | 2015:soberania, 2016:(sin concepto) |
| … | | *1 códigos más* |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `funcional_economico.pdf` · 69 líneas · total extraído **1.284,25 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 397,01 M€ (397.009.501 €) · 6 códigos · 30,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.2` | ATENCION ESPECIALIZADA | 262.342.628 | 66,1 % |
| `4.1.2.1` | ATENCION PRIMARIA SALUD SALUD | 115.697.325 | 29,1 % |
| `4.1.2.3` | FORMACION DEL | 8.042.659 | 2,0 % |
| `4.1.1.1` | DIRECCION Y GENERALES EMPLEO | 5.661.444 | 1,4 % |
| `4.1.3.1` | PROMOCION PROTECCION SANITARIO | 3.833.123 | 1,0 % |
| `4.1.3.2` | ACTIVIDADES PREVENCION Y SALUD | 1.432.322 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 233,36 M€ (233.361.150 €) · 4 códigos · 18,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.2.2.1` | ENSEÑANZA REGIMEN PROMOCION DE LA EDUCACION | 196.078.343 | 84,0 % |
| `4.2.2.3` | ENSEÑANZA UNIVERSITARIA B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica | 20.487.292 | 8,8 % |
| `4.2.2.2` | ENSEÑANZA REGIMEN ESPECIAL | 10.051.942 | 4,3 % |
| `4.2.1.1` | GENERALES Y SEGUIMIENTO DE SALUD LABORAL | 6.743.573 | 2,9 % |

</details>

<details open><summary><b><code>soberania</code> — 53,34 M€ (53.335.125 €) · 4 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5.3.1.1` | REFORMA Y DESARROLLO AGRARIO HIDRAÁLICAS | 30.355.547 | 56,9 % |
| `7.1.2.1` | ORGANIZACION Y ESTRUC.DE GENERAL. | 17.200.310 | 32,2 % |
| `7.1.1.1` | DIRECCION ADMINISTRACION | 4.813.025 | 9,0 % |
| `7.2.1.1` | ADMINISTRACION AGROALIMENTACIÑN AGRICULTURA, GANADER˝A | 966.243 | 1,8 % |

</details>

<details open><summary><b><code>direccion</code> — 55,71 M€ (55.714.757 €) · 12 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.4.1.1` | ADMINISTRACION JUSTICIA UNION EUROPEA | 26.744.886 | 48,0 % |
| `1.2.1.2` | DIRECCION ORGANIZACION C.A.R. ADMON. PUBLICA | 5.259.237 | 9,4 % |
| `2.1.1.1` | PROTECCION CIVIL | 4.671.690 | 8,4 % |
| `1.1.1.1` | ACTIVIDAD LEGISLATIVA | 4.575.926 | 8,2 % |
| `1.3.1.1` | ADMINISTRACION GENERAL DE | 3.313.153 | 5,9 % |
| `1.2.6.1` | INTERIOR EC.FINANC. A LAS CORPORACIONES L. | 3.187.187 | 5,7 % |
| `6.1.2.1` | PLANIFICACION, PRESUPUESTO, ADMON. | 2.342.983 | 4,2 % |
| `1.2.2.1` | ASESORAM.Y COLAB.JUR.Y FUNCION PUBLICA | 1.851.810 | 3,3 % |
| `1.3.1.2` | COOPERACION DESARROLLO PRESIDENCIA ACCION EXTERIOR | 1.572.368 | 2,8 % |
| `1.1.2.3` | ALTO ASESORAMIENTO DEL | 1.219.684 | 2,2 % |
| `1.1.2.1` | GABINETE DEL PRESIDENTE | 917.805 | 1,6 % |
| `1.3.1.3` | REPRESENTACION INSTITUCIONAL EN EXTERIOR | 58.028 | 0,1 % |

</details>

<details open><summary><b><code>vivienda</code> — 6,99 M€ (6.988.257 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.3.1.1` | PROMOCION AYUDA PARA | 6.867.257 | 98,3 % |
| `4.3.2.1` | PLANEAMIENTO, CONTROL VIVIENDA CONSTRUC.,REHABILIT. Y ACCESO | 121.000 | 1,7 % |

</details>

<details open><summary><b><code>empleo</code> — 63,42 M€ (63.419.484 €) · 2 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.2` | PROMOCIÑN EMPRESARIAL Y FORMACION OCUPACIONAL | 42.049.510 | 66,3 % |
| `3.2.2.1` | FOMENTO DEL EMPLEO Y LABORALES Y DE TRABAJO | 21.369.974 | 33,7 % |

</details>

<details open><summary><b><code>idi</code> — 76,29 M€ (76.289.102 €) · 9 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5.4.1.1` | NATURAL | 29.577.839 | 38,8 % |
| `5.4.6.1` | INVESTIGACIÑN, DESARROLLO E RELACIONADO CON EL M. AMBIENTE | 17.041.576 | 22,3 % |
| `5.4.4.1` | INVESTIGACIÑN Y DESARROLLO SALUD | 14.867.749 | 19,5 % |
| `5.4.7.1` | INVESTIGACIÑN Y DESARROLLO TECNOLOG˝AS | 9.661.727 | 12,7 % |
| `5.4.3.1` | INVESTIGACIÑN Y DESARROLLO CON | 3.341.285 | 4,4 % |
| `5.4.2.1` | INVESTIGACIÑN B`SICA INVESTIGACIÑN Y DESARROLLO | 1.103.409 | 1,4 % |
| `5.4.6.2` | I+D+i FORMACIÑN NUEVAS B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica y | 377.005 | 0,5 % |
| `5.4.5.1` | INVESTIGACIÑN Y DESARROLLO RELACIONADO CON EDUCACIÑN | 189.012 | 0,2 % |
| `5.4.9.3` | INNOVACIÑN EN ACTIVIDADES RELAC. CON AGRICULTURA | 129.500 | 0,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 90,57 M€ (90.566.970 €) · 4 códigos · 7,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.1.4` | ADMON. GRAL ATENCIÑN A | 86.632.190 | 95,7 % |
| `3.1.5.1` | ADMON. DE LAS RELACIONES DISCAPACIDAD Y DEPENDENCIA | 1.584.323 | 1,7 % |
| `3.1.2.3` | CENTRO DE VALORACION | 1.291.007 | 1,4 % |
| `3.1.2.1` | INFANCIA DEPENDENCIA Y PREST. SOCIALES | 1.059.450 | 1,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 15,97 M€ (15.969.280 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | MAYORES Y DISCAPACIDAD B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica | 15.969.280 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 32,34 M€ (32.342.632 €) · 8 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7.5.1.1` | COORDINACION PROMOCION DEL B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica | 10.291.616 | 31,8 % |
| `4.5.4.1` | PROMOCION AYUDA AL DEPORTE CULTURAL | 7.736.772 | 23,9 % |
| `4.5.3.1` | PROMOCION COOPERACION | 4.498.950 | 13,9 % |
| `4.5.2.1` | MUSEOS, ARCHIVOS BIBLIOTECAS EDUCACION, CULTURA Y TURISMO | 3.057.229 | 9,5 % |
| `4.5.1.1` | ADMINISTRACION M. AMBIENTE ACTUACIONES PARA PROTECCION DEL | 2.311.746 | 7,1 % |
| `4.5.6.1` | PROMOCION AYUDA | 2.185.360 | 6,8 % |
| `4.5.7.1` | PROMOCION DEL PATRIMONIO JUVENTUD | 1.760.820 | 5,4 % |
| `7.6.1.1` | ORDENACIÑN CONTROL DEL TURISMO | 500.139 | 1,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 259,25 M€ · 17 códigos · 20,2 % del año (se listan los 17 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `0.1.1.1` | B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica y | 137.180.946 |
| `5.3.2.1` | PROTECCION MEJORA DEL MEDIO | 24.480.450 |
| `4.4.1.1` | COOPERACION ECONOMICA PARA GESTION URBANA | 19.647.324 |
| `5.1.2.2` | CONSERVACION Y EXPLOTACION CARRETERAS | 16.650.560 |
| `4.4.3.2` | MEDIDAS PREVENTIVAS Y INFORMACION DEL CONSUMIDOR | 15.186.268 |
| `5.1.2.1` | CREACION INFRAESTRUCTURAS B I R I E S T I N C I E A P I F I C I E F I C I E EN Gastos por AdministraciÓn Pœblica | 9.658.661 |
| `6.1.4.1` | ADMINISTRACION Y GESTION | 6.815.179 |
| `6.1.1.1` | DIRECCIÑN GENERALES ARTES SEGURIDAD INDUSTRIAL, COMERCIALES | 5.727.398 |
| `5.1.2.3` | GESTION E INFRAESTRUCTURA CARRETERAS | 5.127.209 |
| `6.1.5.1` | CONTRATACIÑN Y PATRIMONIO TRIBUTARIA | 4.182.985 |
| `5.1.1.1` | ADMINISTRACION HISTORICO ARTISTICO | 3.974.840 |
| `4.4.2.1` | ORDENACION, CONTROL OBRAS LOCALES. | 3.568.283 |
| `6.1.3.1` | CONTROL INTERNO CONTABILIDAD ESTAD˝STICA GESTIÑN FINANCIERA | 2.406.616 |
| `5.1.2.4` | GESTION E INFRAESTRUCTURA TRANSPORTE. | 1.904.161 |
| `5.1.3.3` | OBRAS Y PLANIFICACIÑN PARQUE MOVIL. | 1.902.000 |
| `7.2.2.1` | REGULACION, PROTECCION DE LA INDUSTRIA. | 737.062 |
| `7.3.2.1` | AHORRO ENERGÉTICO PROPIEDAD Y CALIDAD INDUSTRIAL | 103.800 |

</details>

### 2016

*Fuente: `funcional_economico.pdf` · 70 líneas · total extraído **1.334,19 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 406,96 M€ (406.963.277 €) · 6 códigos · 30,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.2` | ATENCION ESPECIALIZADA | 272.442.298 | 66,9 % |
| `4.1.2.1` | ATENCION PRIMARIA DE SALUD | 117.988.518 | 29,0 % |
| `4.1.2.3` | FORMACION DEL PERSONAL | 7.797.044 | 1,9 % |
| `4.1.3.1` | PROMOCION Y PROTECCION DE LA | 4.258.088 | 1,0 % |
| `4.1.1.1` | DIRECCION Y SERVICIOS GENERALES | 3.066.154 | 0,8 % |
| `4.1.3.2` | ACTIVIDADES DE PREVENCIÓN Y | 1.411.175 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 256,50 M€ (256.504.296 €) · 5 códigos · 19,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.2.2.1` | ENSEÑANZA REGIMEN GENERAL | 207.792.296 | 81,0 % |
| `4.2.2.3` | ENSEÑANZA UNIVERSITARIA | 20.831.773 | 8,1 % |
| `4.2.2.4` | FORMACIÓN PARA EL EMPLEO | 10.621.000 | 4,1 % |
| `4.2.2.2` | ENSEÑANZA REGIMEN ESPECIAL | 10.421.543 | 4,1 % |
| `4.2.1.1` | SERVICIOS GENERALES Y PROMOCION DE LA EDUCACION, | 6.837.684 | 2,7 % |

</details>

<details open><summary><b><code>soberania</code> — 57,79 M€ (57.785.912 €) · 3 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5.3.1.1` | REFORMA Y DESARROLLO AGRARIO | 29.179.476 | 50,5 % |
| `7.1.2.1` | ORGANIZACION Y ESTRUC.DE LA AGRICULTURA, GANADERÍA Y | 24.147.924 | 41,8 % |
| `7.1.1.1` | DIRECCION Y ADMINISTRACION | 4.458.512 | 7,7 % |

</details>

<details open><summary><b><code>direccion</code> — 57,66 M€ (57.660.699 €) · 14 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.4.1.1` | ADMINISTRACION DE JUSTICIA | 18.009.860 | 31,2 % |
| `6.1.1.1` | DIRECCIÓN Y SERVICIOS GENERALES | 5.417.175 | 9,4 % |
| `1.2.1.2` | DIRECCION Y ORGANIZACION DE LA | 5.150.831 | 8,9 % |
| `1.1.1.1` | ACTIVIDAD LEGISLATIVA | 5.049.213 | 8,8 % |
| `2.1.1.1` | PROTECCION CIVIL | 4.941.080 | 8,6 % |
| `6.1.2.1` | PLANIFICACION, PRESUPUESTO, | 4.491.241 | 7,8 % |
| `1.2.6.1` | INTERIOR | 3.700.847 | 6,4 % |
| `1.1.2.2` | DIRECCIÓN Y COORDINACIÓN DE LA | 2.844.259 | 4,9 % |
| `1.3.1.2` | COOPERACION Y DESARROLLO | 2.071.413 | 3,6 % |
| `1.2.2.1` | ASESORAM.Y COLAB.JUR.Y | 1.986.014 | 3,4 % |
| `5.1.3.3` | OBRAS Y PLANIFICACIÓN | 1.956.788 | 3,4 % |
| `1.1.2.3` | ALTO ASESORAMIENTO DEL GOBIERNO Y DE LA ADMON. PUBLICA DE LA | 1.214.844 | 2,1 % |
| `1.1.2.1` | GABINETE DEL PRESIDENTE | 770.134 | 1,3 % |
| `1.3.1.3` | REPRESENTACION INSTITUCIONAL EN | 57.000 | 0,1 % |

</details>

<details open><summary><b><code>vivienda</code> — 6,22 M€ (6.219.759 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.3.1.1` | PROMOCION Y AYUDA PARA LA CONSTRUC.,REHABILIT. Y ACCESO A LA | 6.079.759 | 97,7 % |
| `4.3.2.1` | PLANEAMIENTO, CONTROL Y | 140.000 | 2,3 % |

</details>

<details open><summary><b><code>empleo</code> — 27,49 M€ (27.490.682 €) · 2 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.2` | PROMOCIÓN EMPRESARIAL Y | 16.549.474 | 60,2 % |
| `3.2.2.1` | FOMENTO DEL EMPLEO Y | 10.941.208 | 39,8 % |

</details>

<details open><summary><b><code>idi</code> — 73,30 M€ (73.303.485 €) · 9 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5.4.1.1` | ADMINISTRACIÓN GENERAL DE | 29.365.400 | 40,1 % |
| `5.4.6.1` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN EN MATERIA DE PROM. IND.Y | 16.541.576 | 22,6 % |
| `5.4.4.1` | INVESTIGACIÓN Y DESARROLLO | 15.116.018 | 20,6 % |
| `5.4.7.1` | INVESTIGACIÓN Y DESARROLLO | 6.637.980 | 9,1 % |
| `5.4.3.1` | INVESTIGACIÓN Y DESARROLLO CON | 3.646.862 | 5,0 % |
| `5.4.2.1` | INVESTIGACIÓN BÁSICA | 1.106.817 | 1,5 % |
| `5.4.6.2` | I+D+i FORMACIÓN NUEVAS | 596.332 | 0,8 % |
| `5.4.5.1` | INVESTIGACIÓN Y DESARROLLO | 169.500 | 0,2 % |
| `5.4.9.3` | INNOVACIÓN EN ACTIVIDADES DE SEGURIDAD INDUSTRIAL, COMERCIALES Y | 123.000 | 0,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 91,62 M€ (91.622.339 €) · 4 códigos · 6,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.1.4` | ADMON. GRAL DE ATENCIÓN A LA | 87.623.616 | 95,6 % |
| `3.1.5.1` | ADMON. DE LAS RELACIONES | 1.643.767 | 1,8 % |
| `3.1.2.3` | CENTRO DE VALORACION DE LA | 1.297.241 | 1,4 % |
| `3.1.2.1` | INFANCIA | 1.057.715 | 1,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 15,99 M€ (15.991.615 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | MAYORES Y DISCAPACIDAD | 15.991.615 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 28,70 M€ (28.703.861 €) · 7 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7.5.1.1` | COORDINACION Y PROMOCION DEL | 7.659.640 | 26,7 % |
| `4.5.4.1` | PROMOCION Y AYUDA AL DEPORTE | 7.184.697 | 25,0 % |
| `4.5.3.1` | PROMOCION Y COOPERACION | 4.894.596 | 17,1 % |
| `4.5.2.1` | MUSEOS, ARCHIVOS Y BIBLIOTECAS | 3.055.621 | 10,6 % |
| `4.5.1.1` | ADMINISTRACION GENERAL DE | 2.278.132 | 7,9 % |
| `4.5.6.1` | PROMOCION Y AYUDA A LA | 1.885.360 | 6,6 % |
| `4.5.7.1` | PROMOCION DEL PATRIMONIO | 1.745.815 | 6,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 5,23 M€ (5.232.243 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.1.1` | ADMINISTRACION GENERAL DE POLÍTICAS SOCIALES, FAMILIA, IGUALDAD Y | 5.232.243 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 306,71 M€ · 16 códigos · 23,0 % del año (se listan los 16 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `0.1.1.1` | AMORTIZACION Y GASTOS | 188.482.884 |
| `5.3.2.1` | PROTECCION Y MEJORA DEL MEDIO | 24.611.719 |
| `5.1.2.2` | CONSERVACION Y EXPLOTACION DE | 17.521.560 |
| `4.4.1.1` | COOPERACION ECONOMICA PARA | 17.515.371 |
| `4.4.3.2` | MEDIDAS PREVENTIVAS Y ACTUACIONES PARA LA PROTECCION DEL | 15.684.468 |
| `5.1.2.3` | GESTION E INFRAESTRUCTURA DE | 10.569.830 |
| `6.1.4.1` | ADMINISTRACION Y GESTION | 8.635.392 |
| `5.1.2.1` | CREACION DE INFRAESTRUCTURAS | 6.657.374 |
| `6.1.5.1` | CONTRATACIÓN Y PATRIMONIO | 4.358.669 |
| `4.4.2.1` | ORDENACION, CONTROL E | 3.511.135 |
| `6.1.3.1` | CONTROL INTERNO Y CONTABILIDAD | 2.410.985 |
| `5.1.2.4` | GESTION E INFRAESTRUCTURA DE | 1.846.345 |
| `5.1.1.1` | ADMINISTRACION GENERAL DE | 1.759.925 |
| `7.2.2.1` | REGULACION, PROTECCION DE LA | 1.682.746 |
| `7.2.1.1` | ADMINISTRACION GENERAL DE | 952.012 |
| `7.6.1.1` | ORDENACIÓN Y CONTROL DEL COMER. INTERIOR, ARTESANÍA Y DEFENSA | 511.417 |

</details>

### 2017

*Fuente: `funcional_economico.pdf` · 74 líneas · total extraído **1.452,54 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 408,22 M€ (408.215.639 €) · 6 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | ATENCIÓN ESPECIALIZADA | 267.922.976 | 65,6 % |
| `3.1.2.1` | ATENCIÓN PRIMARIA | 121.966.907 | 29,9 % |
| `3.1.2.3` | FORMACIÓN DEL PERSONAL | 7.403.420 | 1,8 % |
| `3.1.3.1` | ACCIONES DE SALUD PÚBLICA | 4.220.462 | 1,0 % |
| `3.1.3.2` | ORDENACIÓN, CONTROL E | 3.573.908 | 0,9 % |
| `3.1.1.1` | ADMINISTRACIÓN GENERAL DE | 3.127.966 | 0,8 % |

</details>

<details open><summary><b><code>educacion</code> — 260,23 M€ (260.232.242 €) · 6 códigos · 17,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | EDUCACIÓN INFANTIL Y PRIMARIA | 111.508.504 | 42,8 % |
| `3.2.2.2` | EDUCACIÓN SECUNDARIA | 80.027.706 | 30,8 % |
| `3.2.2.3` | FORMACIÓN PROFESIONAL | 25.680.208 | 9,9 % |
| `3.2.2.5` | ENSEÑANZA UNIVERSITARIA | 21.421.235 | 8,2 % |
| `3.2.1.1` | ADMINISTRACIÓN GENERAL DE | 11.308.333 | 4,3 % |
| `3.2.2.4` | ENSEÑANZA RÉGIMEN ESPECIAL | 10.286.256 | 4,0 % |

</details>

<details open><summary><b><code>soberania</code> — 64,08 M€ (64.084.883 €) · 7 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | DESARROLLO RURAL | 28.193.373 | 44,0 % |
| `4.1.2.2` | GARANTIA AGRARIA Y PREVISIÓN DE | 12.186.560 | 19,0 % |
| `4.1.2.3` | CALIDAD Y PROMOCIÓN | 8.690.748 | 13,6 % |
| `4.3.1.1` | PROMOCIÓN TURÍSTICA | 6.710.990 | 10,5 % |
| `4.1.1.1` | ADMINISTRACIÓN GENERAL DE | 4.490.362 | 7,0 % |
| `4.2.1.3` | INDUSTRIA AGROALIMENTARIA | 2.200.000 | 3,4 % |
| `4.3.1.2` | INFRAESTRUCTURAS TURÍSTICAS | 1.612.850 | 2,5 % |

</details>

<details open><summary><b><code>direccion</code> — 5,18 M€ (5.176.171 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD LEGISLATIVA | 5.176.171 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 11,08 M€ (11.084.961 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA | 10.730.661 | 96,8 % |
| `2.6.1.2` | URBANISMO | 354.300 | 3,2 % |

</details>

<details open><summary><b><code>empleo</code> — 22,17 M€ (22.170.495 €) · 2 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.2` | FORMACIÓN PARA EL EMPLEO | 11.351.181 | 51,2 % |
| `2.4.1.1` | POLÍTICAS DE EMPLEO | 10.819.314 | 48,8 % |

</details>

<details open><summary><b><code>idi</code> — 76,24 M€ (76.240.158 €) · 3 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACIÓN Y DESARROLLO | 41.868.903 | 54,9 % |
| `4.6.1.3` | SOCIEDAD DIGITAL | 26.875.456 | 35,3 % |
| `4.6.1.2` | INNOVACIÓN | 7.495.799 | 9,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 71,06 M€ (71.058.860 €) · 3 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` | MAYORES | 48.989.673 | 68,9 % |
| `2.3.2.5` | PRESTACIONES DE LA DEPENDENCIA | 12.596.555 | 17,7 % |
| `3.1.4.1` | ACTUACIONES SOCIOSANITARIAS | 9.472.632 | 13,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 22,29 M€ (22.293.635 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` | DISCAPACIDAD | 22.293.635 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,91 M€ (9.910.687 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | EXCLUSIÓN SOCIAL E INMIGRACIÓN | 9.910.687 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 43,82 M€ (43.820.964 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.2` | CONSERVACIÓN DE | 17.451.560 | 39,8 % |
| `4.5.1.3` | COOPERACIÓN ECONÓMICA LOCAL | 16.184.071 | 36,9 % |
| `4.5.1.1` | INFRAESTRUCTURAS BÁSICAS | 6.595.059 | 15,1 % |
| `4.5.1.4` | SERVICIOS GENERALES E | 3.590.274 | 8,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,72 M€ (1.723.164 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | MUJER | 1.723.164 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 456,52 M€ · 37 códigos · 31,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | AMORTIZACION Y GASTOS | 268.044.308 |
| `4.7.1.2` | GESTIÓN FORESTAL | 21.371.535 |
| `4.4.1.1` | TRANSPORTE | 15.956.000 |
| `4.7.1.4` | GESTIÓN DE RECURSOS HÍDRICOS | 15.575.630 |
| `1.1.1.1` | JUSTICIA | 15.204.161 |
| `2.3.2.6` | SERVICIOS COMUNITARIOS | 11.016.473 |
| `2.3.2.4` | INFANCIA Y MENORES | 10.363.312 |
| `9.2.3.1` | ADMINISTRACIÓN Y GESTIÓN | 8.807.644 |
| `4.2.1.1` | APOYO EMPRESARIAL EN GENERAL | 7.332.319 |
| `9.1.1.2` | FUNCIÓN PÚBLICA | 6.581.358 |
| `1.8.1.2` | ACTIVIDAD EJECUTIVA | 5.966.118 |
| `9.1.1.1` | SERVICIOS DE CARÁCTER GENERAL Y | 5.752.769 |
| `1.3.1.1` | PROTECCIÓN CIVIL | 5.668.870 |
| `3.4.1.1` | DEPORTE | 5.655.377 |
| `2.3.1.1` | ADMINISTRACIÓN GENERAL DE | 5.406.391 |
| `4.7.1.1` | BIODIVERSIDAD, USO PÚBLICO Y | 4.909.322 |
| `9.2.1.1` | ADMINISTRACIÓN DEL PATRIMONIO Y | 4.766.565 |
| `4.2.1.5` | COMERCIO | 4.031.545 |
| `4.2.1.4` | RELACIONES Y PREVENCIÓN DE | 3.586.672 |
| `4.7.1.3` | CALIDAD AMBIENTAL, RESIDUOS Y | 3.503.843 |
| `3.3.1.1` | PROMOCIÓN DE LA CULTURA | 3.264.230 |
| `3.3.1.2` | MUSEOS, ARCHIVOS Y BIBLIOTECAS | 3.110.415 |
| `9.2.4.1` | CONTROL INTERNO, AUDITORÍA Y | 2.410.964 |
| `3.3.2.1` | PATRIMONIO HISTÓRICO-ARTÍSTICO | 2.405.518 |
| `4.2.1.2` | REINDUSTRIALIZACIÓN | 2.321.235 |
| … | *resto: 12 códigos* | 13.510.567 |

</details>

### 2018

*Fuente: `funcional_economico.pdf` · 72 líneas · total extraído **1.485,41 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 425,01 M€ (425.013.914 €) · 6 códigos · 28,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | ATENCIÓN ESPECIALIZADA | 275.440.925 | 64,8 % |
| `3.1.2.1` | ATENCIÓN PRIMARIA | 131.094.991 | 30,8 % |
| `3.1.2.3` | FORMACIÓN DEL PERSONAL SANITARIO | 6.905.110 | 1,6 % |
| `3.1.3.1` | ACCIONES DE SALUD PÚBLICA | 4.469.598 | 1,1 % |
| `3.1.3.2` | ORDENACIÓN, CONTROL E INFORMACIÓN AL CONSUMIDOR | 3.574.002 | 0,8 % |
| `3.1.1.1` | ADMINISTRACIÓN GENERAL DE SALUD | 3.529.288 | 0,8 % |

</details>

<details open><summary><b><code>educacion</code> — 277,15 M€ (277.146.239 €) · 7 códigos · 18,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | EDUCACIÓN INFANTIL Y PRIMARIA | 114.214.607 | 41,2 % |
| `3.2.2.2` | EDUCACIÓN SECUNDARIA | 85.345.116 | 30,8 % |
| `3.2.2.3` | FORMACIÓN PROFESIONAL | 26.135.330 | 9,4 % |
| `3.2.2.5` | ENSEÑANZA UNIVERSITARIA | 22.180.587 | 8,0 % |
| `3.2.1.1` | ADMINISTRACIÓN GENERAL DE EDUCACIÓN | 12.909.022 | 4,7 % |
| `3.2.2.4` | ENSEÑANZA RÉGIMEN ESPECIAL | 10.890.244 | 3,9 % |
| `4.7.1.1` | BIODIVERSIDAD, USO PÚBLICO Y EDUCACIÓN AMBIENTAL | 5.471.333 | 2,0 % |

</details>

<details open><summary><b><code>soberania</code> — 62,50 M€ (62.501.365 €) · 7 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | DESARROLLO RURAL | 26.357.854 | 42,2 % |
| `4.1.2.2` | GARANTIA AGRARIA Y PREVISIÓN DE RIEGOS | 13.225.780 | 21,2 % |
| `4.1.2.3` | CALIDAD Y PROMOCIÓN AGROALIMENTARIA | 8.766.952 | 14,0 % |
| `4.3.1.1` | PROMOCIÓN TURÍSTICA | 5.973.427 | 9,6 % |
| `4.1.1.1` | ADMINISTRACIÓN GENERAL DE AGRICULTURA Y GANADERÍA | 4.384.752 | 7,0 % |
| `4.2.1.3` | INDUSTRIA AGROALIMENTARIA | 2.200.000 | 3,5 % |
| `4.3.1.2` | INFRAESTRUCTURAS TURÍSTICAS | 1.592.600 | 2,5 % |

</details>

<details open><summary><b><code>direccion</code> — 5,18 M€ (5.176.171 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD LEGISLATIVA | 5.176.171 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 11,19 M€ (11.194.045 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA | 10.768.548 | 96,2 % |
| `2.6.1.2` | URBANISMO | 425.497 | 3,8 % |

</details>

<details open><summary><b><code>empleo</code> — 22,91 M€ (22.913.948 €) · 2 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | POLÍTICAS DE EMPLEO | 11.924.606 | 52,0 % |
| `2.4.1.2` | FORMACIÓN PARA EL EMPLEO | 10.989.342 | 48,0 % |

</details>

<details open><summary><b><code>idi</code> — 51,93 M€ (51.933.998 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACIÓN Y DESARROLLO | 42.976.889 | 82,8 % |
| `4.6.1.2` | INNOVACIÓN | 8.957.109 | 17,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 71,46 M€ (71.460.874 €) · 3 códigos · 4,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` | MAYORES | 50.002.206 | 70,0 % |
| `2.3.2.5` | PRESTACIONES DE LA DEPENDENCIA | 11.776.668 | 16,5 % |
| `3.1.4.1` | ACTUACIONES SOCIOSANITARIAS | 9.682.000 | 13,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 22,10 M€ (22.100.156 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` | DISCAPACIDAD | 22.100.156 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,45 M€ (9.445.943 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | EXCLUSIÓN SOCIAL E INMIGRACIÓN | 9.445.943 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 44,82 M€ (44.821.438 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.2` | CONSERVACIÓN DE INFRAESTRUCTURAS BÁSICAS | 17.868.660 | 39,9 % |
| `4.5.1.3` | COOPERACIÓN ECONÓMICA LOCAL | 16.683.738 | 37,2 % |
| `4.5.1.1` | INFRAESTRUCTURAS BÁSICAS | 6.735.224 | 15,0 % |
| `4.5.1.4` | SERVICIOS GENERALES E INFRAESTRUCTURAS BÁSICAS | 3.533.816 | 7,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,97 M€ (1.970.231 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | MUJER | 1.970.231 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 479,73 M€ · 35 códigos · 32,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | AMORTIZACION Y GASTOS FINANCIEROS | 286.661.250 |
| `4.7.1.2` | GESTIÓN FORESTAL | 20.971.746 |
| `1.1.1.1` | JUSTICIA | 17.732.905 |
| `4.4.1.1` | TRANSPORTE | 16.097.056 |
| `4.7.1.4` | GESTIÓN DE RECURSOS HÍDRICOS | 15.103.741 |
| `2.3.2.6` | SERVICIOS COMUNITARIOS | 11.765.640 |
| `2.3.2.4` | INFANCIA Y MENORES | 11.021.135 |
| `9.2.3.1` | ADMINISTRACIÓN Y GESTIÓN TRIBUTARIA | 9.031.365 |
| `9.1.1.2` | FUNCIÓN PÚBLICA | 8.481.703 |
| `2.3.1.1` | ADMINISTRACIÓN GENERAL DE SERVICIOS SOCIALES | 7.117.689 |
| `3.4.1.1` | DEPORTE | 6.744.339 |
| `1.3.1.1` | PROTECCIÓN CIVIL | 6.531.825 |
| `1.8.1.2` | ACTIVIDAD EJECUTIVA | 6.366.888 |
| `9.1.1.1` | SERVICIOS DE CARÁCTER GENERAL Y ATENCIÓN AL CIUDADANO | 5.820.700 |
| `4.2.1.1` | APOYO EMPRESARIAL EN GENERAL | 5.437.819 |
| `9.2.1.1` | ADMINISTRACIÓN DEL PATRIMONIO Y COORDINACIÓN DE LA | 4.860.758 |
| `4.2.1.5` | COMERCIO | 4.261.458 |
| `4.2.1.4` | RELACIONES Y PREVENCIÓN DE RIESGOS LABORALES | 3.727.441 |
| `4.7.1.3` | CALIDAD AMBIENTAL, RESIDUOS Y ECONOMÍA CIRCULAR | 3.635.738 |
| `3.3.2.1` | PATRIMONIO HISTÓRICO-ARTÍSTICO | 3.443.716 |
| `3.3.1.2` | MUSEOS, ARCHIVOS Y BIBLIOTECAS | 3.311.846 |
| `3.3.1.1` | PROMOCIÓN DE LA CULTURA | 3.158.341 |
| `9.2.4.1` | CONTROL INTERNO, AUDITORÍA Y CONTABILIDAD | 2.633.671 |
| `2.7.1.1` | JUVENTUD | 2.451.931 |
| `4.2.1.2` | REINDUSTRIALIZACIÓN | 2.352.702 |
| … | *resto: 10 códigos* | 11.005.874 |

</details>

### 2019

*Fuente: `funcional_economico.pdf` · 73 líneas · total extraído **1.533,40 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 435,49 M€ (435.489.541 €) · 6 códigos · 28,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` |  | 285.026.317 | 65,4 % |
| `3.1.2.1` | A Y S C IS E T N E T N R C O I S A L D E E S | 131.063.989 | 30,1 % |
| `3.1.2.3` |  | 7.173.277 | 1,6 % |
| `3.1.3.1` | LA SALUD | 4.644.786 | 1,1 % |
| `3.1.3.2` |  | 3.791.024 | 0,9 % |
| `3.1.1.1` |  | 3.790.148 | 0,9 % |

</details>

<details open><summary><b><code>educacion</code> — 290,20 M€ (290.204.605 €) · 6 códigos · 18,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` |  | 120.626.168 | 41,6 % |
| `3.2.2.2` |  | 95.295.363 | 32,8 % |
| `3.2.2.3` | EDUCACIÓN F O R M A C IÓN | 27.675.695 | 9,5 % |
| `3.2.2.5` |  | 22.686.018 | 7,8 % |
| `3.2.1.1` |  | 12.611.392 | 4,3 % |
| `3.2.2.4` |  | 11.309.969 | 3,9 % |

</details>

<details open><summary><b><code>soberania</code> — 63,35 M€ (63.346.771 €) · 6 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` |  | 27.965.485 | 44,1 % |
| `4.1.2.2` |  | 13.330.722 | 21,0 % |
| `4.1.2.3` |  | 9.753.808 | 15,4 % |
| `4.3.1.1` |  | 6.124.021 | 9,7 % |
| `4.1.1.1` |  | 4.330.635 | 6,8 % |
| `4.3.1.2` |  | 1.842.100 | 2,9 % |

</details>

<details open><summary><b><code>direccion</code> — 7,64 M€ (7.640.547 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | SERVICIOS ACTIVIDAD ALTA ACTIVIDAD | 7.640.547 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 11,74 M€ (11.735.007 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` |  | 11.314.918 | 96,4 % |
| `2.6.1.2` | P P R R O O T M E O C C C IÓ IÓ N N Y | 420.089 | 3,6 % |

</details>

<details open><summary><b><code>empleo</code> — 22,61 M€ (22.612.330 €) · 2 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` |  | 11.824.319 | 52,3 % |
| `2.4.1.2` |  | 10.788.011 | 47,7 % |

</details>

<details open><summary><b><code>idi</code> — 53,14 M€ (53.135.779 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INNOVACION E I N N O V A C IÓN | 43.688.397 | 82,2 % |
| `4.6.1.2` |  | 9.447.382 | 17,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 58,82 M€ (58.823.612 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 49.107.638 | 83,5 % |
| `3.1.4.1` | A A C Y T IVIDADES | 9.715.974 | 16,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 22,66 M€ (22.663.575 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 22.663.575 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,49 M€ (9.489.340 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` |  | 9.489.340 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 45,27 M€ (45.269.841 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 16.653.738 | 36,8 % |
| `4.5.1.2` |  | 14.828.657 | 32,8 % |
| `4.5.1.1` | BÁSICAS | 10.177.584 | 22,5 % |
| `4.5.1.4` |  | 3.609.862 | 8,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,64 M€ (2.641.662 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` |  | 2.641.662 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 510,35 M€ · 39 códigos · 33,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` |  | 262.134.279 |
| `6.1.3.3` | ECONÓMICO I N N O V A C I O N E I N N O V A C IÓN | 27.127.181 |
| `6.7.1.2` |  | 21.660.338 |
| `1.1.1.1` |  | 17.951.753 |
| `4.4.1.1` |  | 15.442.000 |
| `6.7.1.4` |  | 14.824.919 |
| `2.3.2.6` |  | 12.457.594 |
| `2.3.2.4` | SERVICIOS ACCIÓN INFANCIA Y | 12.157.925 |
| `2.3.2.5` |  | 12.006.356 |
| `9.2.3.1` |  | 9.319.935 |
| `9.1.1.2` |  | 8.452.020 |
| `4.2.1.1` |  | 8.442.798 |
| `1.8.1.2` |  | 6.832.769 |
| `2.3.1.1` |  | 6.753.982 |
| `3.4.1.1` |  | 6.703.942 |
| `1.3.1.1` |  | 6.592.510 |
| `9.1.1.1` | SERVICIOS SERVICIOS SERVICIOS DE | 5.927.443 |
| `6.7.1.1` |  | 5.206.928 |
| `9.2.1.1` | DE LA | 4.876.712 |
| `4.2.1.5` |  | 4.325.182 |
| `6.7.1.3` |  | 3.802.045 |
| `4.2.1.4` |  | 3.773.035 |
| `3.3.1.2` |  | 3.479.447 |
| `3.3.2.1` | ÍSTICO | 3.449.661 |
| `3.3.1.1` |  | 3.125.300 |
| … | *resto: 14 códigos* | 23.521.336 |

</details>

### 2020

*Fuente: `funcional_economico.pdf` · 76 líneas · total extraído **1.555,78 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 454,04 M€ (454.040.465 €) · 6 códigos · 29,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | ATENCIÓN | 299.614.779 | 66,0 % |
| `3.1.2.1` | ATENCIÓN | 132.861.028 | 29,3 % |
| `3.1.2.3` | FORMACIÓN DEL | 8.338.626 | 1,8 % |
| `3.1.3.1` | ACCIONES DE | 5.145.769 | 1,1 % |
| `3.1.3.2` | ORDENACIÓN, | 4.073.436 | 0,9 % |
| `3.1.1.1` | ADMINISTRACIÓN | 4.006.827 | 0,9 % |

</details>

<details open><summary><b><code>educacion</code> — 299,55 M€ (299.552.395 €) · 6 códigos · 19,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | EDUCACIÓN | 121.080.330 | 40,4 % |
| `3.2.2.2` | EDUCACIÓN | 98.455.979 | 32,9 % |
| `3.2.2.3` | FORMACIÓN | 30.889.252 | 10,3 % |
| `3.2.2.5` | ENSEÑANZA | 24.600.600 | 8,2 % |
| `3.2.1.1` | ADMINISTRACIÓN | 12.269.341 | 4,1 % |
| `3.2.2.4` | ENSEÑANZA | 12.256.893 | 4,1 % |

</details>

<details open><summary><b><code>soberania</code> — 59,64 M€ (59.636.207 €) · 5 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | DESARROLLO | 27.312.461 | 45,8 % |
| `4.1.2.2` | GARANTIA | 13.507.489 | 22,6 % |
| `4.1.2.3` | CALIDAD Y | 8.760.301 | 14,7 % |
| `4.3.1.1` | PROMOCIÓN | 6.115.400 | 10,3 % |
| `4.1.1.1` | ADMINISTRACIÓN | 3.940.556 | 6,6 % |

</details>

<details open><summary><b><code>direccion</code> — 8,53 M€ (8.533.507 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD | 8.533.507 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 11,99 M€ (11.985.836 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA | 11.689.636 | 97,5 % |
| `2.6.1.2` | URBANISMO 0 | 296.200 | 2,5 % |

</details>

<details open><summary><b><code>empleo</code> — 20,72 M€ (20.716.746 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | POLÍTICAS DE | 12.604.351 | 60,8 % |
| `2.4.1.2` | FORMACIÓN PARA 0 | 8.112.395 | 39,2 % |

</details>

<details open><summary><b><code>idi</code> — 80,66 M€ (80.655.340 €) · 3 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACIÓN Y | 38.666.969 | 47,9 % |
| `4.6.1.3` | SOCIEDAD | 29.156.727 | 36,1 % |
| `4.6.1.2` | INNOVACIÓN | 12.831.644 | 15,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 59,36 M€ (59.357.460 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` | MAYORES | 49.677.523 | 83,7 % |
| `3.1.4.1` | ACTUACIONES 0 | 9.679.937 | 16,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 21,77 M€ (21.771.506 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` | DISCAPACIDAD | 21.771.506 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 12,43 M€ (12.427.922 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | EXCLUSIÓN | 12.427.922 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,86 M€ (2.862.201 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | MUJER | 1.999.126 | 69,8 % |
| `2.3.3.2` | IGUALDAD DE | 863.075 | 30,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 524,24 M€ · 45 códigos · 33,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | AMORTIZACION Y 0 0 | 258.642.155 |
| `4.7.1.2` | GESTIÓN | 21.948.940 |
| `1.1.1.1` | JUSTICIA | 20.187.880 |
| `4.4.1.3` | COOPERACIÓN 0 0 0 0 0 0 | 16.885.578 |
| `4.4.1.2` | CONSERVACIÓN 0 | 16.839.261 |
| `4.4.1.1` | TRANSPORTE 0 | 15.098.000 |
| `2.3.2.5` | PRESTACIONES | 15.028.595 |
| `2.3.2.6` | SERVICIOS | 13.730.359 |
| `4.7.1.4` | GESTIÓN DE | 13.438.004 |
| `9.1.1.1` | SERVICIOS DE | 12.974.910 |
| `2.3.2.4` | INFANCIA Y | 12.828.044 |
| `9.2.3.1` | ADMINISTRACIÓN | 9.136.364 |
| `4.2.1.1` | APOYO | 7.787.410 |
| `9.1.1.2` | FUNCIÓN PÚBLICA | 7.733.863 |
| `3.4.1.1` | DEPORTE | 7.574.603 |
| `1.3.1.1` | PROTECCIÓN | 7.033.134 |
| `9.2.1.1` | ADMINISTRACIÓN | 5.265.383 |
| `4.4.1.4` | SERVICIOS | 4.587.778 |
| `4.7.1.1` | BIODIVERSIDAD, | 4.429.293 |
| `4.2.1.5` | COMERCIO | 4.301.543 |
| `2.3.1.1` | ADMINISTRACIÓN | 4.263.097 |
| `4.2.1.4` | RELACIONES Y | 3.758.877 |
| `3.3.1.2` | MUSEOS, | 3.663.361 |
| `4.7.1.3` | CALIDAD | 3.622.899 |
| `4.2.1.3` | INDUSTRIA 0 0 0 0 0 0 | 3.575.000 |
| … | *resto: 20 códigos* | 29.906.904 |

</details>

### 2021

*Fuente: `funcional_economico.pdf` · 81 líneas · total extraído **1.809,33 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 529,04 M€ (529.044.979 €) · 6 códigos · 29,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | DE BIENES | 348.752.056 | 65,9 % |
| `3.1.2.1` | SPITALES, | 156.534.598 | 29,6 % |
| `3.1.2.3` |  | 9.259.929 | 1,8 % |
| `3.1.3.1` | B A L C I C C I A O S N ES | 6.370.965 | 1,2 % |
| `3.1.3.2` |  | 4.219.206 | 0,8 % |
| `3.1.1.1` | ODUCCIÓN SANIDAD S A N I D A D A | 3.908.225 | 0,7 % |

</details>

<details open><summary><b><code>educacion</code> — 345,05 M€ (345.047.771 €) · 5 códigos · 19,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | SEÑANZA | 258.110.451 | 74,8 % |
| `3.2.2.3` | PÚBLICOS DE | 36.234.470 | 10,5 % |
| `3.2.2.5` |  | 26.191.842 | 7,6 % |
| `3.2.2.2` |  | 12.928.336 | 3,7 % |
| `3.2.1.1` | EDUCACIÓN U C A C I Ó N A | 11.582.672 | 3,4 % |

</details>

<details open><summary><b><code>soberania</code> — 73,57 M€ (73.573.095 €) · 6 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | TRUCTURAS | 29.261.213 | 39,8 % |
| `4.1.2.2` | ECONÓMICO A | 14.823.651 | 20,1 % |
| `4.3.1.1` | A TUACIONES TURISMO T U R I S M O | 14.013.091 | 19,0 % |
| `4.1.2.3` |  | 10.949.695 | 14,9 % |
| `4.1.1.1` | A TUACIONES A RICULTURA Y A MINISTRACI A | 3.799.945 | 5,2 % |
| `4.3.1.2` |  | 725.500 | 1,0 % |

</details>

<details open><summary><b><code>direccion</code> — 8,35 M€ (8.352.260 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | G A I C S T L I A V T ID IV A A D , R A E L C T C A I ÓN DE | 8.352.260 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 19,36 M€ (19.355.606 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA V I V I E N D A | 18.691.106 | 96,6 % |
| `2.6.1.2` |  | 664.500 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 25,99 M€ (25.985.635 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO E M P L E O | 16.910.357 | 65,1 % |
| `2.4.1.2` |  | 9.075.278 | 34,9 % |

</details>

<details open><summary><b><code>idi</code> — 72,18 M€ (72.180.296 €) · 5 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | V ESTIGACION, V ESTIGACIÓN | 40.946.227 | 56,7 % |
| `4.6.1.2` |  | 28.590.974 | 39,6 % |
| `4.6.3.1` | G S IT O A C L I E D A D | 2.238.814 | 3,1 % |
| `4.6.3.3` |  | 354.475 | 0,5 % |
| `4.6.3.2` | INNOVACION | 49.806 | 0,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 68,20 M€ (68.201.540 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` | A TUACIONES C SE IA R L V E I S C I O S A C C I A C L I Ó N | 58.412.435 | 85,6 % |
| `3.1.4.1` | ANIFICACIÓN | 9.789.105 | 14,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 25,40 M€ (25.396.989 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 25.396.989 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 14,91 M€ (14.912.857 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | A C C IA C L I Ó N | 14.912.857 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 58,00 M€ (58.000.986 €) · 4 códigos · 3,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` | BÁSICAS | 25.104.965 | 43,3 % |
| `4.5.1.2` | URAS | 21.012.306 | 36,2 % |
| `4.5.1.1` | F RAESTRUCTU F RAESTRUCT | 7.361.628 | 12,7 % |
| `4.5.1.4` |  | 4.522.087 | 7,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,93 M€ (2.926.576 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | OMOCIÓN | 2.926.576 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 566,36 M€ · 45 códigos · 31,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | GENERAL B D L E I U C D A A B D L E I U C D A A | 286.092.310 |
| `4.4.1.1` | ANSPORTE A N S P O R T E | 41.327.000 |
| `4.7.1.2` |  | 21.999.676 |
| `1.1.1.1` | B S L E I R C V O I S C IOS JUSTICIA J U S T I C I A | 21.342.739 |
| `4.7.1.4` | A TUACIONES A M BI E E D N I T O E A M B I E E D N I T O E | 16.925.859 |
| `2.3.2.4` |  | 15.728.022 |
| `2.3.2.6` |  | 15.579.512 |
| `2.3.2.5` | PROTECCIÓN Y | 15.018.669 |
| `9.2.3.1` | L G E S S IS T T IÓ EM N A A | 10.908.740 |
| `9.1.1.1` | A TUACIONES S C E A R R V Á IC C I T O E S R S C E A R R V Á IC C I T O E S R | 10.805.510 |
| `3.4.1.1` | PÚBLICOS DE DEPORTE D E P O R T E | 8.495.833 |
| `1.3.1.1` | SEGURIDAD G U R I D A D | 8.332.077 |
| `4.7.1.1` | A M BI E E D N I T O E A M B I E E D N I T O E | 8.112.447 |
| `9.1.1.2` | DE CARACTER GENERAL | 7.498.179 |
| `9.1.2.1` | A F I MIBNI U NAT INS ACT RIREIA AR C A I Ó Y | 6.986.029 |
| `4.2.1.1` | D E U M S P T R R E IA S Y A , EMPRESA | 5.414.798 |
| `2.3.1.1` | A TUACIONES C SE IA R L V E I S C I O S R G V E I S C T I O I Ó S N D E A | 5.050.260 |
| `4.2.1.4` | ENERGIA | 4.758.838 |
| `3.3.1.1` | PREFERENTE C ULTURA C U L T U R A | 4.734.948 |
| `1.4.2.1` | OPERACIÓN A | 4.382.653 |
| `1.8.1.2` | EJECUTIVA Y LA | 4.378.639 |
| `4.7.1.3` | A | 4.034.430 |
| `3.3.1.2` | A | 3.783.015 |
| `3.3.2.1` | TS T ITC RÓO IMR IO C N O I -O A R T | 3.341.270 |
| `4.2.1.2` |  | 3.129.398 |
| … | *resto: 20 códigos* | 28.195.434 |

</details>

### 2022

*Fuente: `funcional_economico.pdf` · 64 líneas · total extraído **1.823,60 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 524,39 M€ (524.388.258 €) · 5 códigos · 28,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` |  | 329.235.699 | 62,8 % |
| `3.1.2.1` | CARÁCTER A I H S O TE S N P C IT I A A L L E E S S , Y S ERVICIOS | 173.833.354 | 33,1 % |
| `3.1.2.3` | PREFERENTE | 8.918.499 | 1,7 % |
| `3.1.3.1` | ACCIONES PÚBLICAS | 6.853.380 | 1,3 % |
| `3.1.1.1` | PRODUCCIÓN DE SANIDAD SANIDAD | 5.547.326 | 1,1 % |

</details>

<details open><summary><b><code>educacion</code> — 347,81 M€ (347.811.369 €) · 5 códigos · 19,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | ENSEÑANZA | 260.686.679 | 75,0 % |
| `3.2.2.3` |  | 34.092.547 | 9,8 % |
| `3.2.2.5` |  | 27.233.659 | 7,8 % |
| `3.2.1.1` | EDUCACIÓN EDUCACIÓN | 13.097.972 | 3,8 % |
| `3.2.2.2` |  | 12.700.512 | 3,7 % |

</details>

<details open><summary><b><code>soberania</code> — 74,23 M€ (74.231.604 €) · 5 códigos · 4,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | ESTRUCTURAS | 35.972.188 | 48,5 % |
| `4.1.2.2` |  | 15.827.862 | 21,3 % |
| `4.3.1.1` | TURISMO TURISMO | 12.454.028 | 16,8 % |
| `4.1.2.3` |  | 8.402.026 | 11,3 % |
| `4.3.1.2` |  | 1.575.500 | 2,1 % |

</details>

<details open><summary><b><code>direccion</code> — 8,69 M€ (8.685.655 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD ALTA DIRECCIÓN DE LA | 8.685.655 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 19,43 M€ (19.428.731 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA VIVIENDA | 18.477.231 | 95,1 % |
| `2.6.1.2` |  | 951.500 | 4,9 % |

</details>

<details open><summary><b><code>empleo</code> — 24,80 M€ (24.795.145 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO EMPLEO | 14.050.550 | 56,7 % |
| `2.4.1.2` |  | 10.744.595 | 43,3 % |

</details>

<details open><summary><b><code>idi</code> — 106,08 M€ (106.079.483 €) · 3 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACION, INVESTIGACIÓN, | 55.928.388 | 52,7 % |
| `4.6.1.3` |  | 37.383.216 | 35,2 % |
| `4.6.1.2` | INNOVACION INNOVACIÓN | 12.767.879 | 12,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 72,09 M€ (72.086.345 €) · 2 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 61.920.176 | 85,9 % |
| `3.1.4.1` | PLANIFICACIÓN | 10.166.169 | 14,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 24,28 M€ (24.284.690 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 24.284.690 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,51 M€ (10.512.734 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | ACCIÓN SOCIAL | 10.512.734 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 35,38 M€ (35.376.260 €) · 2 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 25.765.348 | 72,8 % |
| `4.5.1.1` | INFRAESTRUCTURAS | 9.610.912 | 27,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 19,35 M€ (19.346.609 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.4` | PROMOCIÓN SOCIAL | 16.381.455 | 84,7 % |
| `2.3.3.1` | PROMOCIÓN SOCIAL | 2.965.154 | 15,3 % |

</details>

<details><summary><code>(sin concepto)</code> — 556,57 M€ · 33 códigos · 30,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | DEUDA PUBLICA DEUDA PUBLICA | 357.385.174 |
| `1.1.1.1` | SERVICIOS JUSTICIA JUSTICIA | 22.031.923 |
| `4.7.1.2` |  | 21.871.393 |
| `4.7.1.4` |  | 17.789.639 |
| `2.3.2.6` |  | 16.665.030 |
| `2.3.2.5` |  | 13.616.874 |
| `9.2.3.1` | GESTIÓN DEL SISTEMA | 10.867.187 |
| `9.1.1.2` |  | 9.570.407 |
| `3.4.1.1` | DEPORTE DEPORTE | 8.489.273 |
| `1.3.1.1` | SEGURIDAD SEGURIDAD | 8.063.790 |
| `3.3.1.1` | CULTURA CULTURA | 7.420.355 |
| `4.4.1.1` | TRANSPORTE TRANSPORTE | 6.065.000 |
| `1.4.2.1` | COOPERACIÓN PARA EL | 5.111.321 |
| `4.2.1.1` | EMPRESA, EMPRESA | 5.092.639 |
| `4.2.1.4` | ENERGIA | 4.832.537 |
| `4.7.1.5` |  | 4.772.233 |
| `4.2.1.2` |  | 4.741.213 |
| `1.8.1.2` | EJECUTIVA Y | 4.627.374 |
| `3.3.1.2` |  | 3.802.548 |
| `3.3.2.1` | PATRIMONIO | 3.389.352 |
| `2.7.1.1` | JUVENTUD JUVENTUD | 3.192.497 |
| `9.2.4.1` | FISCALIZACIÓN Y | 2.970.425 |
| `9.3.1.1` | SERVICIOS A SERVICIOS A | 2.934.042 |
| `1.4.1.1` | ACCIÓN EXTERIOR | 2.026.153 |
| `4.2.1.5` |  | 1.661.273 |
| … | *resto: 8 códigos* | 7.579.359 |

</details>

### 2023

*Fuente: `detalle_gastos_funcional_economico.pdf` · 62 líneas · total extraído **1.732,17 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 546,72 M€ (546.720.797 €) · 4 códigos · 31,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` |  | 350.358.987 | 64,1 % |
| `3.1.2.1` | HOSPITALES, SERVICIOS | 183.550.476 | 33,6 % |
| `3.1.3.1` | ACCIONES PÚBLICAS | 7.180.544 | 1,3 % |
| `3.1.1.1` | PRODUCCIÓN DE SANIDAD S A N I D A D | 5.630.790 | 1,0 % |

</details>

<details open><summary><b><code>educacion</code> — 368,05 M€ (368.053.803 €) · 5 códigos · 21,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | ENSEÑANZA | 273.686.644 | 74,4 % |
| `3.2.2.3` |  | 36.185.381 | 9,8 % |
| `3.2.2.5` |  | 29.720.921 | 8,1 % |
| `3.2.1.1` | EDUCACIÓN E D U C A C I Ó N | 15.091.380 | 4,1 % |
| `3.2.2.2` |  | 13.369.477 | 3,6 % |

</details>

<details open><summary><b><code>soberania</code> — 74,84 M€ (74.838.757 €) · 5 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | ESTRUCTURAS | 35.287.677 | 47,2 % |
| `4.1.2.2` |  | 16.606.694 | 22,2 % |
| `4.3.1.1` | TURISMO T U R I S M O | 12.713.030 | 17,0 % |
| `4.1.2.3` |  | 8.905.856 | 11,9 % |
| `4.3.1.2` |  | 1.325.500 | 1,8 % |

</details>

<details open><summary><b><code>direccion</code> — 8,69 M€ (8.685.655 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD ALTA DIRECCIÓN DE LA | 8.685.655 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 21,53 M€ (21.532.755 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA V I V I E N D A | 20.381.255 | 94,7 % |
| `2.6.1.2` |  | 1.151.500 | 5,3 % |

</details>

<details open><summary><b><code>empleo</code> — 27,50 M€ (27.497.803 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO E M P L E O | 16.184.419 | 58,9 % |
| `2.4.1.2` |  | 11.313.384 | 41,1 % |

</details>

<details open><summary><b><code>idi</code> — 111,74 M€ (111.742.707 €) · 3 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACION, INVESTIGACIÓN, | 64.165.765 | 57,4 % |
| `4.6.1.3` |  | 37.030.813 | 33,1 % |
| `4.6.1.2` | INNOVACION I N N O V ACIÓN | 10.546.129 | 9,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 77,43 M€ (77.425.735 €) · 2 códigos · 4,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 66.765.747 | 86,2 % |
| `3.1.4.1` | PLANIFICACIÓN | 10.659.988 | 13,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 25,88 M€ (25.884.747 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 25.884.747 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 10,49 M€ (10.493.027 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | ACCIÓN SOCIAL | 10.493.027 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 42,79 M€ (42.790.032 €) · 2 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 29.319.852 | 68,5 % |
| `4.5.1.1` | INFRAESTRUCTURAS | 13.470.180 | 31,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 18,55 M€ (18.553.132 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.4` | PROMOCIÓN SOCIAL | 15.595.432 | 84,1 % |
| `2.3.3.1` | PROMOCIÓN SOCIAL | 2.957.700 | 15,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 397,95 M€ · 32 códigos · 23,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | DEUDA PUBLICA D E U D A P U B L I C A | 174.358.875 |
| `4.7.1.2` |  | 24.345.206 |
| `4.2.1.1` | EMPRESA, EMPRESA | 24.185.885 |
| `1.1.1.1` | SERVICIOS JUSTICIA J U S T I C I A | 22.238.330 |
| `2.3.2.6` |  | 18.431.118 |
| `4.7.1.4` |  | 17.962.791 |
| `2.3.2.5` |  | 14.721.351 |
| `9.2.3.1` | GESTIÓN DEL SISTEMA | 11.423.738 |
| `9.1.1.2` |  | 9.912.220 |
| `1.3.1.1` | SEGURIDAD S E G U R I D A D | 8.837.320 |
| `3.4.1.1` | DEPORTE D E P O R T E | 8.730.513 |
| `3.3.1.1` | CULTURA C U L T U R A | 7.932.549 |
| `4.7.1.5` |  | 6.294.700 |
| `4.4.1.1` | TRANSPORTE T R A N S P O R T E | 6.065.000 |
| `1.4.2.1` | COOPERACIÓN PARA EL | 5.101.046 |
| `1.8.1.2` | EJECUTIVA Y | 4.667.305 |
| `3.3.2.1` | PATRIMONIO | 4.629.914 |
| `3.3.1.2` |  | 4.253.338 |
| `2.7.1.1` | JUVENTUD J U V E N T U D | 4.112.524 |
| `9.2.4.1` | FISCALIZACIÓN Y | 3.110.180 |
| `9.3.1.1` | SERVICIOS A SERVICIOS A | 2.952.086 |
| `4.2.1.2` |  | 2.542.298 |
| `1.4.1.1` | ACCIÓN EXTERIOR | 2.121.709 |
| `4.2.1.5` |  | 2.037.384 |
| `2.3.3.2` |  | 1.549.800 |
| … | *resto: 7 códigos* | 5.431.789 |

</details>

### 2024

*Fuente: `funcional_economico.pdf` · 76 líneas · total extraído **1.947,38 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 592,30 M€ (592.298.603 €) · 6 códigos · 30,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | CARÁCTER | 372.502.251 | 62,9 % |
| `3.1.2.1` | HOSPITALES, SERVICIOS | 189.150.328 | 31,9 % |
| `3.1.2.3` |  | 11.862.331 | 2,0 % |
| `3.1.3.1` | PREFERENTE ACCIONES PÚBLICAS | 7.976.392 | 1,3 % |
| `3.1.1.1` | PRODUCCIÓN DE SANIDAD SANIDAD | 6.485.665 | 1,1 % |
| `3.1.3.2` |  | 4.321.636 | 0,7 % |

</details>

<details open><summary><b><code>educacion</code> — 403,16 M€ (403.158.839 €) · 5 códigos · 20,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | ENSENANZA REGIMEN GENERAL | 298.487.862 | 74,0 % |
| `3.2.2.3` | FORMACION PROFESIONAL | 43.249.892 | 10,7 % |
| `3.2.2.5` | ENSENANZA UNIVERSITARIA | 30.461.002 | 7,6 % |
| `3.2.1.1` | ADMINISTRACION GENERAL DE EDUCACION | 17.282.751 | 4,3 % |
| `3.2.2.2` | ENSENANZA REGIMEN ESPECIAL | 13.677.332 | 3,4 % |

</details>

<details open><summary><b><code>soberania</code> — 90,60 M€ (90.602.990 €) · 6 códigos · 4,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.1` | ESTRUCTURAS | 41.132.700 | 45,4 % |
| `4.1.2.2` |  | 21.679.268 | 23,9 % |
| `4.3.1.1` | TURISMO TURISMO | 14.961.671 | 16,5 % |
| `4.1.2.3` |  | 6.182.399 | 6,8 % |
| `4.1.1.1` | AR AC ÁC TU TE A R C IONES DE G A A N G AD R E IC R U ÍA LT URA Y G EN AD ER M A IN L I STRACIÓN G | 5.321.952 | 5,9 % |
| `4.3.1.2` | ACTUACIONES DE TURISMO TURISMO | 1.325.000 | 1,5 % |

</details>

<details open><summary><b><code>direccion</code> — 9,22 M€ (9.216.514 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD ALTA DIRECCIÓN DE LA | 9.216.514 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 30,99 M€ (30.992.918 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA VIVIENDA | 29.605.712 | 95,5 % |
| `2.6.1.2` | ACTUACIONES DE VIVIENDA VIVIENDA | 1.387.206 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 29,00 M€ (29.003.475 €) · 2 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO EMPLEO | 17.641.458 | 60,8 % |
| `2.4.1.2` |  | 11.362.017 | 39,2 % |

</details>

<details open><summary><b><code>idi</code> — 107,03 M€ (107.029.279 €) · 3 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACION, INVESTIGACIÓN, | 66.768.896 | 62,4 % |
| `4.6.1.3` | INNOVACION | 35.202.101 | 32,9 % |
| `4.6.1.2` |  | 5.058.282 | 4,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 82,75 M€ (82.746.928 €) · 2 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 70.792.310 | 85,6 % |
| `3.1.4.1` | PLANIFICACIÓN | 11.954.618 | 14,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 28,38 M€ (28.378.907 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 28.378.907 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 1,57 M€ (1.566.950 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.3.3` |  | 1.566.950 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 8,66 M€ (8.663.693 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | ACCIÓN SOCIAL | 8.663.693 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 62,87 M€ (62.871.065 €) · 4 códigos · 3,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 31.125.467 | 49,5 % |
| `4.5.1.2` |  | 17.011.641 | 27,1 % |
| `4.5.1.1` | INFRAESTRUCTURAS | 8.955.735 | 14,2 % |
| `4.5.1.4` |  | 5.778.222 | 9,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,46 M€ (4.462.909 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | PROMOCIÓN SOCIAL | 4.462.909 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 496,38 M€ · 41 códigos · 25,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | AMORTIZACION Y GASTOS FINANCIEROS | 176.892.127 |
| `4.2.1.1` | EMPRESA, EMPRESA | 32.983.751 |
| `4.7.1.2` | ACTUACIONES DE MEDIO AMBIENTE MEDIO AMBIENTE | 27.298.982 |
| `2.3.2.6` |  | 24.362.420 |
| `1.1.1.1` | SERVICIOS JUSTICIA JUSTICIA | 23.404.959 |
| `9.1.1.1` | R A A C C TU TE A R C I G O E N N E E S R D A E L C R S Á E C R T V E IC R IO G S E D N E E RAL C R SE Á R C V TE IC R IO G S E D N E E RAL G | 22.735.350 |
| `4.7.1.4` |  | 18.531.343 |
| `2.3.2.5` |  | 18.402.438 |
| `2.3.2.4` |  | 17.489.881 |
| `9.1.1.2` |  | 15.298.185 |
| `9.2.3.1` | ADMINISTRACION Y GESTION TRIBUTARIA | 12.264.577 |
| `3.4.1.1` | DEPORTE | 10.005.824 |
| `1.3.1.1` | SEGURIDAD SEGURIDAD | 8.929.033 |
| `3.3.1.1` | PROMOCION DE LA CULTURA | 8.422.372 |
| `4.4.1.1` | TRANSPORTE TRANSPORTE | 8.307.350 |
| `4.7.1.1` | MEDIO AMBIENTE MEDIO AMBIENTE P | 7.020.089 |
| `9.2.1.1` | N A A D N M C I I N E I R S A T R Y A CIÓN H C S I E E R N V D IC A I P O Ú S B D L E IC A P | 6.962.566 |
| `4.2.1.4` |  | 4.979.115 |
| `3.3.2.1` | PATRIMONIO HISTORICO-ARTISTICO | 4.952.718 |
| `3.3.1.2` | MUSEOS ARCHIVOS Y BIBLIOTECAS | 4.951.825 |
| `1.4.2.1` | COOPERACIÓN PARA EL | 4.906.500 |
| `1.8.1.2` |  | 4.359.567 |
| `2.7.1.1` | JUVENTUD JUVENTUD | 4.163.516 |
| `4.7.1.3` | R | 4.029.321 |
| `9.3.1.1` | SERVICIOS A ENTIDADES LOCALES | 3.607.598 |
| … | *resto: 16 códigos* | 21.122.895 |

</details>

### 2025

*Fuente: `funcional_economico.pdf` · 58 líneas · total extraído **2.014,04 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 640,74 M€ (640.739.777 €) · 6 códigos · 31,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | CARÁCTER | 409.728.143 | 63,9 % |
| `3.1.2.1` | HOSPITALES, SERVICIOS | 198.549.108 | 31,0 % |
| `3.1.2.3` |  | 12.671.699 | 2,0 % |
| `3.1.3.1` | ACCIONES PÚBLICAS | 9.780.071 | 1,5 % |
| `3.1.1.1` | PRODUCCIÓN DE SANIDAD SANIDAD | 6.326.076 | 1,0 % |
| `3.1.3.2` |  | 3.684.680 | 0,6 % |

</details>

<details open><summary><b><code>educacion</code> — 434,73 M€ (434.726.679 €) · 7 códigos · 21,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | ENSEÑANZA | 315.325.285 | 72,5 % |
| `3.2.2.3` |  | 47.446.696 | 10,9 % |
| `3.2.2.5` |  | 35.984.048 | 8,3 % |
| `3.2.1.1` | EDUCACIÓN EDUCACIÓN | 15.298.383 | 3,5 % |
| `3.2.2.2` | CARÁCTER | 14.408.941 | 3,3 % |
| `3.2.3.2` |  | 5.612.799 | 1,3 % |
| `3.2.3.1` | CULTURA | 650.527 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 97,03 M€ (97.033.492 €) · 5 códigos · 4,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.2` |  | 37.833.791 | 39,0 % |
| `4.1.2.1` | ESTRUCTURAS | 35.398.676 | 36,5 % |
| `4.3.1.1` | TURISMO TURISMO | 14.421.287 | 14,9 % |
| `4.1.2.3` |  | 6.704.738 | 6,9 % |
| `4.3.1.2` |  | 2.675.000 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 9,98 M€ (9.978.692 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD ALTA DIRECCIÓN DE LA | 9.978.692 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 28,38 M€ (28.375.471 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA VIVIENDA | 27.664.303 | 97,5 % |
| `2.6.1.2` | ACTUACIONES DE VIVIENDA VIVIENDA | 711.168 | 2,5 % |

</details>

<details open><summary><b><code>empleo</code> — 27,16 M€ (27.155.299 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO EMPLEO | 16.087.880 | 59,2 % |
| `2.4.1.2` |  | 11.067.419 | 40,8 % |

</details>

<details open><summary><b><code>idi</code> — 113,57 M€ (113.567.983 €) · 3 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACION, INVESTIGACIÓN, | 70.522.383 | 62,1 % |
| `4.6.1.3` |  | 33.015.041 | 29,1 % |
| `4.6.1.2` |  | 10.030.559 | 8,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 89,18 M€ (89.181.987 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 76.372.455 | 85,6 % |
| `3.1.4.1` | PLANIFICACIÓN | 12.809.532 | 14,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 29,80 M€ (29.795.599 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 29.795.599 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 1,64 M€ (1.636.719 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.3.3` |  | 1.636.719 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,89 M€ (3.887.158 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | ACCIÓN SOCIAL | 3.887.158 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,76 M€ (47.761.407 €) · 2 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 34.200.539 | 71,6 % |
| `4.5.1.1` | INFRAESTRUCTURAS | 13.560.868 | 28,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,86 M€ (3.861.053 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | PROMOCIÓN SOCIAL | 3.861.053 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 486,34 M€ · 24 códigos · 24,1 % del año (se listan los 24 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | DEUDA PUBLICA DEUDA PUBLICA | 235.049.281 |
| `4.2.1.1` | EMPRESA, EMPRESA | 32.955.213 |
| `4.7.1.2` |  | 26.281.527 |
| `2.3.2.6` |  | 25.814.667 |
| `2.3.2.5` |  | 23.239.887 |
| `1.1.1.1` | SERVICIOS JUSTICIA JUSTICIA | 22.384.311 |
| `2.3.2.4` |  | 18.587.238 |
| `4.7.1.4` |  | 17.511.204 |
| `9.1.1.2` |  | 15.500.041 |
| `9.2.3.1` | GESTIÓN DEL SISTEMA | 11.439.063 |
| `3.4.1.1` | DEPORTE DEPORTE | 11.223.572 |
| `1.3.1.1` | SEGURIDAD SEGURIDAD | 9.703.879 |
| `4.4.1.1` | TRANSPORTE TRANSPORTE | 8.361.350 |
| `1.4.2.1` | COOPERACIÓN PARA EL | 5.271.700 |
| `9.3.1.1` | SERVICIOS A SERVICIOS A | 4.997.379 |
| `1.8.1.2` |  | 4.712.806 |
| `9.2.4.1` | ACTUACIONES DE ADMINISTRACIÓN FISCALIZACIÓN Y | 3.811.124 |
| `1.4.1.1` | ACCIÓN EXTERIOR ACCIÓN EXTERIOR | 2.386.710 |
| `4.7.1.5` | ECONÓMICO | 2.383.723 |
| `1.3.1.2` |  | 1.483.850 |
| `9.1.1.3` |  | 1.389.020 |
| `9.2.5.1` | ESTADISTICA | 780.163 |
| `1.8.1.3` |  | 646.962 |
| `4.2.1.5` |  | 427.100 |

</details>

### 2026

*Fuente: `funcional_economico.pdf` · 60 líneas · total extraído **2.030,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 637,06 M€ (637.055.097 €) · 5 códigos · 31,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.2.2` | CARÁCTER | 409.728.143 | 64,3 % |
| `3.1.2.1` | HOSPITALES, SERVICIOS | 197.749.108 | 31,0 % |
| `3.1.2.3` |  | 12.671.699 | 2,0 % |
| `3.1.3.1` | ACCIONES PÚBLICAS | 10.580.071 | 1,7 % |
| `3.1.1.1` | PRODUCCIÓN DE SANIDAD SANIDAD | 6.326.076 | 1,0 % |

</details>

<details open><summary><b><code>educacion</code> — 428,44 M€ (428.443.953 €) · 5 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.2.2.1` | ENSEÑANZA | 315.325.285 | 73,6 % |
| `3.2.2.3` |  | 47.446.696 | 11,1 % |
| `3.2.2.5` |  | 35.984.048 | 8,4 % |
| `3.2.1.1` | EDUCACIÓN EDUCACIÓN | 15.298.383 | 3,6 % |
| `3.2.2.2` | CARÁCTER | 14.389.541 | 3,4 % |

</details>

<details open><summary><b><code>soberania</code> — 97,03 M€ (97.033.492 €) · 5 códigos · 4,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.1.2.2` |  | 37.833.791 | 39,0 % |
| `4.1.2.1` | ESTRUCTURAS | 35.398.676 | 36,5 % |
| `4.3.1.1` | TURISMO TURISMO | 14.421.287 | 14,9 % |
| `4.1.2.3` |  | 6.704.738 | 6,9 % |
| `4.3.1.2` |  | 2.675.000 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 9,98 M€ (9.978.692 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1.8.1.1` | ACTIVIDAD ALTA DIRECCIÓN DE LA | 9.978.692 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 28,38 M€ (28.375.471 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.6.1.1` | VIVIENDA VIVIENDA | 27.664.303 | 97,5 % |
| `2.6.1.2` | ACTUACIONES DE VIVIENDA VIVIENDA | 711.168 | 2,5 % |

</details>

<details open><summary><b><code>empleo</code> — 27,16 M€ (27.155.299 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.4.1.1` | EMPLEO EMPLEO | 16.087.880 | 59,2 % |
| `2.4.1.2` |  | 11.067.419 | 40,8 % |

</details>

<details open><summary><b><code>idi</code> — 113,05 M€ (113.047.983 €) · 3 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.6.1.1` | INVESTIGACION, INVESTIGACIÓN, | 70.522.383 | 62,4 % |
| `4.6.1.3` | INNOVACION | 32.495.041 | 28,7 % |
| `4.6.1.2` |  | 10.030.559 | 8,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 89,18 M€ (89.181.987 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.2` |  | 76.372.455 | 85,6 % |
| `3.1.4.1` | PLANIFICACIÓN | 12.809.532 | 14,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 29,80 M€ (29.795.599 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.3` |  | 29.795.599 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 1,64 M€ (1.636.719 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3.1.3.3` |  | 1.636.719 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,89 M€ (3.887.158 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.2.1` | ACCIÓN SOCIAL | 3.887.158 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,82 M€ (47.821.407 €) · 2 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4.5.1.3` |  | 34.260.539 | 71,6 % |
| `4.5.1.1` | INFRAESTRUCTURAS | 13.560.868 | 28,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,36 M€ (4.361.053 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `2.3.3.1` | PROMOCIÓN SOCIAL | 4.361.053 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 512,38 M€ · 29 códigos · 25,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `9.5.1.1` | DEUDA PUBLICA DEUDA PUBLICA | 234.189.281 |
| `4.2.1.1` | EMPRESA, EMPRESA | 32.955.213 |
| `4.7.1.2` |  | 26.281.527 |
| `2.3.2.6` |  | 25.814.667 |
| `2.3.2.5` |  | 23.239.887 |
| `1.1.1.1` | SERVICIOS JUSTICIA JUSTICIA | 22.884.311 |
| `2.3.2.4` |  | 18.587.238 |
| `4.7.1.4` |  | 17.561.204 |
| `9.1.1.2` |  | 15.500.041 |
| `3.4.1.1` | DEPORTE DEPORTE | 11.452.572 |
| `9.2.3.1` | GESTIÓN DEL SISTEMA | 11.439.063 |
| `1.3.1.1` | SEGURIDAD SEGURIDAD | 10.213.879 |
| `3.3.1.1` |  | 9.366.434 |
| `4.4.1.1` | TRANSPORTE TRANSPORTE | 8.361.350 |
| `3.3.1.2` |  | 5.612.799 |
| `1.4.2.1` | COOPERACIÓN PARA EL | 5.271.700 |
| `2.7.1.1` | JUVENTUD JUVENTUD | 5.108.938 |
| `9.3.1.1` | SERVICIOS A SERVICIOS A | 4.997.379 |
| `1.8.1.2` |  | 4.712.806 |
| `3.3.2.1` | PATRIMONIO | 4.610.325 |
| `9.2.4.1` | ACTUACIONES DE ADMINISTRACIÓN FISCALIZACIÓN Y | 3.811.124 |
| `1.4.1.1` | ACCIÓN EXTERIOR ACCIÓN EXTERIOR | 2.386.710 |
| `4.7.1.5` | ECONÓMICO | 2.383.723 |
| `1.3.1.2` |  | 1.743.850 |
| `9.1.1.3` |  | 1.389.020 |
| … | *resto: 4 códigos* | 2.504.752 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py lar     # regenera este documento
python3 tools/auditoria_magnitud.py lar        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa lar --anio <año> \
    --input ../fuentes/raw/lar/<año>/<fichero> --output /tmp/lar.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-lar.md`](limitaciones-lar.md)

