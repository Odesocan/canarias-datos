# Trazabilidad de la extracción — País Vasco (`pvc`)

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
| **2015** | 105 | `GASTOSC.csv` | 10 | 33,3 % | 11.631,25 | — | no_aplica |
| **2016** | 106 | `GASTOSC.csv` | 10 | 33,0 % | 11.937,00 | — | no_aplica |
| **2017** | 108 | `GASTOSC.csv` | 10 | 34,3 % | 12.093,99 | — | no_aplica |
| **2018** | 109 | `GASTOSC.csv` | 10 | 33,9 % | 12.545,55 | — | no_aplica |
| **2019** | 110 | `GASTOSC.csv` | 10 | 33,6 % | 12.850,59 | — | no_aplica |
| **2020** | 110 | `GASTOSC.csv` | 10 | 33,6 % | 12.869,02 | — | no_aplica |
| **2021** | 112 | `GASTOSC.csv` | 10 | 34,8 % | 13.577,66 | — | no_aplica |
| **2022** | 113 | `csv_tidy.csv` | 10 | 34,5 % | 14.172,91 | — | no_aplica |
| **2023** | 113 | `csv_tidy.csv` | 10 | 34,5 % | 15.502,15 | — | no_aplica |
| **2024** | 114 | `csv_tidy.csv` | 10 | 34,2 % | 16.350,98 | — | no_aplica |
| **2025** | 119 | `csv_tidy.csv` | 10 | 34,5 % | 17.069,78 | — | no_aplica |
| **2026** | 119 | `csv_tidy.csv` | 10 | 34,5 % | 17.495,94 | — | no_aplica |

**URL(s) de origen:**
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2015A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2016A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2017A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2018A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2019P/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2020A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2021A/AdErAu_c.zip>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2022A/Datuak_datos.csv>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2023P/Datuak_datos.csv>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2024A/Datuak_datos.csv>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2025A/Datuak_datos.csv>
- <https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/2026A/Datuak_datos.csv>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 3.390,01 | 3.421,74 | 3.542,72 | 3.677,32 | 3.800,12 | 3.943,69 | 3.994,41 | 4.191,41 | 4.633,31 | 4.893,90 | 5.111,57 | 5.321,77 |
| `educacion` | 2.544,78 | 2.583,11 | 2.632,33 | 2.683,25 | 2.799,85 | 2.885,69 | 2.951,38 | 3.008,75 | 3.252,00 | 3.449,29 | 3.593,81 | 3.789,15 |
| `soberania` | 110,30 | 111,62 | 114,10 | 118,98 | 129,47 | 132,66 | 144,42 | 159,30 | 181,86 | 207,90 | 221,22 | 208,88 |
| `direccion` | 2,36 | 2,25 | 2,64 | 2,46 | 2,63 | 3,00 | 3,10 | 3,12 | 3,32 | 3,53 | 4,62 | 4,80 |
| `vivienda` | 110,72 | 112,68 | 125,39 | 135,02 | 150,58 | 164,07 | 173,43 | 193,45 | 225,53 | 253,47 | 321,80 | 442,04 |
| `empleo` | 697,00 | 731,92 | 720,64 | 766,45 | 796,20 | 857,42 | 886,74 | 923,36 | 788,75 | 807,33 | 838,17 | 418,21 |
| `idi` | 230,94 | 243,36 | 281,79 | 303,75 | 325,63 | 352,09 | 384,57 | 426,02 | 450,48 | 461,84 | 498,97 | 532,31 |
| `diversidad` | 4,22 | 4,23 | 4,28 | 4,52 | 6,35 | 6,71 | 8,11 | 8,51 | 16,10 | 17,50 | 19,02 | 18,04 |
| `turismo` | 13,60 | 13,61 | 17,17 | 18,34 | 18,84 | 19,88 | 18,83 | 25,96 | 26,00 | 24,85 | 25,08 | 27,13 |
| `igualdad` | 10,79 | 10,79 | 10,94 | 11,06 | 11,85 | 14,25 | 21,58 | 23,66 | 24,25 | 25,62 | 23,61 | 25,17 |
| **Σ asignado** | 7.114,69 | 7.235,31 | 7.452,01 | 7.721,15 | 8.041,52 | 8.379,46 | 8.586,58 | 8.963,53 | 9.601,60 | 10.145,23 | 10.657,89 | 10.787,49 |
| *(sin concepto)* | 4.516,55 | 4.701,69 | 4.641,98 | 4.824,40 | 4.809,08 | 4.489,55 | 4.991,08 | 5.209,37 | 5.900,55 | 6.205,74 | 6.411,89 | 6.708,44 |
| **TOTAL extraído** | 11.631,25 | 11.937,00 | 12.093,99 | 12.545,55 | 12.850,59 | 12.869,02 | 13.577,66 | 14.172,91 | 15.502,15 | 16.350,98 | 17.069,78 | 17.495,94 |

**Conceptos sin ninguna línea en toda la serie:** `dependencia`, `discapacidad`, `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +0,9 % | +3,5 % | +3,8 % | +3,3 % | +3,8 % | +1,3 % | +4,9 % | +10,5 % | +5,6 % | +4,4 % | +4,1 % |
| `educacion` | +1,5 % | +1,9 % | +1,9 % | +4,3 % | +3,1 % | +2,3 % | +1,9 % | +8,1 % | +6,1 % | +4,2 % | +5,4 % |
| `soberania` | +1,2 % | +2,2 % | +4,3 % | +8,8 % | +2,5 % | +8,9 % | +10,3 % | +14,2 % | +14,3 % | +6,4 % | −5,6 % |
| `direccion` | −4,6 % | +17,4 % | −6,8 % | +6,6 % | +14,4 % | +3,0 % | +0,7 % | +6,4 % | +6,3 % | +30,9 % | +4,0 % |
| `vivienda` | +1,8 % | +11,3 % | +7,7 % | +11,5 % | +9,0 % | +5,7 % | +11,5 % | +16,6 % | +12,4 % | +27,0 % | +37,4 % |
| `empleo` | +5,0 % | −1,5 % | +6,4 % | +3,9 % | +7,7 % | +3,4 % | +4,1 % | −14,6 % | +2,4 % | +3,8 % | −50,1 % ⚠ |
| `idi` | +5,4 % | +15,8 % | +7,8 % | +7,2 % | +8,1 % | +9,2 % | +10,8 % | +5,7 % | +2,5 % | +8,0 % | +6,7 % |
| `diversidad` | +0,2 % | +1,4 % | +5,5 % | +40,5 % ⚠ | +5,8 % | +20,9 % | +4,8 % | +89,3 % ⚠ | +8,7 % | +8,7 % | −5,1 % |
| `turismo` | +0,1 % | +26,2 % | +6,8 % | +2,7 % | +5,5 % | −5,3 % | +37,9 % | +0,2 % | −4,4 % | +0,9 % | +8,2 % |
| `igualdad` | +0,0 % | +1,5 % | +1,0 % | +7,2 % | +20,2 % | +51,4 % ⚠ | +9,7 % | +2,5 % | +5,6 % | −7,8 % | +6,6 % |
| **TOTAL** | +2,6 % | +1,3 % | +3,7 % | +2,4 % | +0,1 % | +5,5 % | +4,4 % | +9,4 % | +5,5 % | +4,4 % | +2,5 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2026 | `empleo` | **SALTO** | 838,17 → 418,21 M€ (−50,1 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (2 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `3110` | 120,71 | 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:empleo, 2022:empleo, 2023:empleo, 2024:empleo, 2025:empleo, 2026:empleo |
| `3111` | 52,41 | 2015:empleo, 2016:empleo, 2017:empleo, 2018:empleo, 2019:empleo, 2020:empleo, 2021:igualdad, 2022:igualdad, 2023:igualdad, 2024:igualdad, 2025:igualdad, 2026:igualdad |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `GASTOSC.csv` · 105 líneas · total extraído **11.631,25 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.390,01 M€ (3.390.005.398 €) · 6 códigos · 29,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 2.826.856.254 | 83,4 % |
| `4115` | Farmacia | 490.257.263 | 14,5 % |
| `4113` | Salud Pública | 42.766.691 | 1,3 % |
| `4111` | Estructura y Apoyo de Salud | 17.462.175 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 7.565.791 | 0,2 % |
| `4116` | Adicciones | 5.097.224 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 2.544,78 M€ (2.544.775.749 €) · 8 códigos · 21,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 965.257.160 | 37,9 % |
| `4222` | Educación Secundaria y Formación Profesional | 907.465.824 | 35,7 % |
| `4223` | Enseñanza Universitaria | 313.070.704 | 12,3 % |
| `4231` | Promoción Educativa | 171.091.074 | 6,7 % |
| `4224` | Enseñanzas de Régimen Especial | 56.452.627 | 2,2 % |
| `4211` | Estructura y Apoyo de Educación | 51.047.784 | 2,0 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 44.643.531 | 1,8 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.747.045 | 1,4 % |

</details>

<details open><summary><b><code>soberania</code> — 110,30 M€ (110.297.987 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 78.186.001 | 70,9 % |
| `7113` | Promoción y Calidad Alimentaria | 20.003.889 | 18,1 % |
| `7112` | Pesca | 12.108.097 | 11,0 % |

</details>

<details open><summary><b><code>direccion</code> — 2,36 M€ (2.357.504 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 2.357.504 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 110,72 M€ (110.722.750 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 106.897.930 | 96,5 % |
| `4313` | Ordenación Territorial | 3.824.820 | 3,5 % |

</details>

<details open><summary><b><code>empleo</code> — 697,00 M€ (696.996.646 €) · 5 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 423.360.244 | 60,7 % |
| `3231` | Formación | 226.803.174 | 32,5 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 42.125.934 | 6,0 % |
| `3212` | Economía Social | 3.814.776 | 0,5 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 892.518 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 230,94 M€ (230.936.721 €) · 6 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 117.651.319 | 50,9 % |
| `5414` | Fondo de Innovación | 37.000.000 | 16,0 % |
| `5412` | Investigación | 34.775.998 | 15,1 % |
| `5411` | Investigación y Desarrollo Agropesquero | 17.113.784 | 7,4 % |
| `1215` | Innovación y Administración Electrónica | 14.203.624 | 6,2 % |
| `7214` | Innovación y Estrategia de Competitividad | 10.191.996 | 4,4 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,22 M€ (4.216.387 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 4.216.387 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 13,60 M€ (13.597.537 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo | 13.597.537 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,79 M€ (10.785.000 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 5.782.000 | 53,6 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 5.003.000 | 46,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.516,55 M€ · 70 códigos · 38,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 989.517.396 |
| `3121` | Inclusión Social | 977.311.888 |
| `2223` | Ertzaintza en Servicio | 584.532.643 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 350.530.100 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 223.451.577 |
| `1411` | Administración de Justicia | 134.415.541 |
| `4515` | Medios de Comunicación Social | 115.578.106 |
| `1221` | Diversos Departamentos | 103.736.741 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 82.901.673 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 75.152.966 |
| `3124` | Política Familiar y Comunitaria | 63.105.953 |
| `4711` | Política Lingüística | 48.401.208 |
| `4715` | Euskaldunización del Sistema Educativo | 41.728.017 |
| `1312` | Cooperación al Desarrollo | 40.026.830 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 38.850.000 |
| `5121` | Planificación y Administración Hidráulica | 35.900.000 |
| `4513` | Promoción de la Cultura | 34.341.945 |
| `1412` | Justicia | 33.280.676 |
| `3112` | Trabajo | 28.242.115 |
| `1111` | Parlamento | 28.048.073 |
| `7612` | Comercio Interior | 27.335.019 |
| `4421` | Protección del Medio Ambiente | 26.593.808 |
| `1214` | Informática y Telecomunicaciones | 26.176.634 |
| `7613` | Internacionalización | 23.049.158 |
| `1212` | Servicios Generales | 21.277.959 |
| … | *resto: 45 códigos* | 363.067.295 |

</details>

### 2016

*Fuente: `GASTOSC.csv` · 106 líneas · total extraído **11.937,00 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.421,74 M€ (3.421.743.398 €) · 6 códigos · 28,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 2.858.197.799 | 83,5 % |
| `4115` | Farmacia | 491.648.967 | 14,4 % |
| `4113` | Salud Pública | 41.340.570 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 17.788.117 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 7.722.498 | 0,2 % |
| `4116` | Adicciones | 5.045.447 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.583,11 M€ (2.583.113.822 €) · 8 códigos · 21,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 956.043.830 | 37,0 % |
| `4222` | Educación Secundaria y Formación Profesional | 934.329.825 | 36,2 % |
| `4223` | Enseñanza Universitaria | 313.278.631 | 12,1 % |
| `4231` | Promoción Educativa | 181.239.560 | 7,0 % |
| `4211` | Estructura y Apoyo de Educación | 64.571.205 | 2,5 % |
| `4224` | Enseñanzas de Régimen Especial | 52.792.765 | 2,0 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 45.173.087 | 1,7 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.684.919 | 1,4 % |

</details>

<details open><summary><b><code>soberania</code> — 111,62 M€ (111.621.719 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 77.775.458 | 69,7 % |
| `7113` | Promoción y Calidad Alimentaria | 19.810.718 | 17,7 % |
| `7112` | Pesca | 14.035.543 | 12,6 % |

</details>

<details open><summary><b><code>direccion</code> — 2,25 M€ (2.249.055 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 2.249.055 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 112,68 M€ (112.679.947 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 108.981.480 | 96,7 % |
| `4313` | Ordenación Territorial | 3.698.467 | 3,3 % |

</details>

<details open><summary><b><code>empleo</code> — 731,92 M€ (731.920.592 €) · 5 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 457.812.582 | 62,5 % |
| `3231` | Formación | 225.059.624 | 30,7 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 44.330.015 | 6,1 % |
| `3212` | Economía Social | 3.816.928 | 0,5 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 901.443 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 243,36 M€ (243.361.518 €) · 6 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 116.690.317 | 47,9 % |
| `5414` | Fondo de Innovación | 50.700.000 | 20,8 % |
| `5412` | Investigación | 35.357.850 | 14,5 % |
| `5411` | Investigación y Desarrollo Agropesquero | 17.717.017 | 7,3 % |
| `1215` | Innovación y Administración Electrónica | 13.798.580 | 5,7 % |
| `7214` | Innovación y Estrategia de Competitividad | 9.097.754 | 3,7 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,23 M€ (4.225.123 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 4.225.123 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 13,61 M€ (13.607.069 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo | 13.607.069 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,79 M€ (10.785.000 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 5.782.000 | 53,6 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 5.003.000 | 46,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.701,69 M€ · 71 códigos · 39,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 1.170.217.585 |
| `3121` | Inclusión Social | 967.515.032 |
| `2223` | Ertzaintza en Servicio | 589.999.299 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 350.529.697 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 221.542.813 |
| `1411` | Administración de Justicia | 139.918.475 |
| `4515` | Medios de Comunicación Social | 119.975.738 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 86.058.535 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 82.499.807 |
| `1221` | Diversos Departamentos | 68.127.921 |
| `3124` | Política Familiar y Comunitaria | 64.836.011 |
| `4711` | Política Lingüística | 51.729.400 |
| `1312` | Cooperación al Desarrollo | 43.026.830 |
| `4715` | Euskaldunización del Sistema Educativo | 42.646.384 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 39.239.000 |
| `4513` | Promoción de la Cultura | 36.000.185 |
| `5121` | Planificación y Administración Hidráulica | 34.900.000 |
| `1412` | Justicia | 33.683.741 |
| `1111` | Parlamento | 28.440.747 |
| `3112` | Trabajo | 27.356.109 |
| `7612` | Comercio Interior | 27.336.713 |
| `1214` | Informática y Telecomunicaciones | 26.159.969 |
| `4421` | Protección del Medio Ambiente | 25.865.047 |
| `3123` | Servicios Sociales | 25.437.096 |
| `7613` | Internacionalización | 23.365.923 |
| … | *resto: 46 códigos* | 375.285.700 |

</details>

### 2017

*Fuente: `GASTOSC.csv` · 108 líneas · total extraído **12.093,99 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.542,72 M€ (3.542.717.000 €) · 6 códigos · 29,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 2.967.082.444 | 83,8 % |
| `4115` | Farmacia | 503.552.036 | 14,2 % |
| `4113` | Salud Pública | 41.796.074 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 17.635.650 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 8.068.440 | 0,2 % |
| `4116` | Adicciones | 4.582.356 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.632,33 M€ (2.632.327.803 €) · 8 códigos · 21,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 981.235.948 | 37,3 % |
| `4222` | Educación Secundaria y Formación Profesional | 959.455.141 | 36,4 % |
| `4223` | Enseñanza Universitaria | 316.963.796 | 12,0 % |
| `4231` | Promoción Educativa | 173.916.188 | 6,6 % |
| `4211` | Estructura y Apoyo de Educación | 64.530.933 | 2,5 % |
| `4224` | Enseñanzas de Régimen Especial | 54.672.095 | 2,1 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 46.071.465 | 1,8 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.482.237 | 1,3 % |

</details>

<details open><summary><b><code>soberania</code> — 114,10 M€ (114.103.909 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 78.066.641 | 68,4 % |
| `7113` | Promoción y Calidad Alimentaria | 20.210.251 | 17,7 % |
| `7112` | Pesca | 15.827.017 | 13,9 % |

</details>

<details open><summary><b><code>direccion</code> — 2,64 M€ (2.641.271 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 2.641.271 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 125,39 M€ (125.389.229 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 121.673.061 | 97,0 % |
| `4313` | Ordenación Territorial | 3.716.168 | 3,0 % |

</details>

<details open><summary><b><code>empleo</code> — 720,64 M€ (720.644.310 €) · 5 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 448.131.504 | 62,2 % |
| `3231` | Formación | 223.432.418 | 31,0 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 43.737.134 | 6,1 % |
| `3212` | Economía Social | 4.413.811 | 0,6 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 929.443 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 281,79 M€ (281.788.800 €) · 7 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 139.885.904 | 49,6 % |
| `5412` | Investigación | 44.276.003 | 15,7 % |
| `5414` | Fondo de Innovación | 38.350.000 | 13,6 % |
| `5415` | Agenda de Innovación Digital | 21.557.467 | 7,7 % |
| `5411` | Investigación y Desarrollo Agropesquero | 17.721.614 | 6,3 % |
| `1215` | Innovación y Administración Electrónica | 13.926.094 | 4,9 % |
| `7214` | Innovación y Estrategia de Competitividad | 6.071.718 | 2,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,28 M€ (4.283.087 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 4.283.087 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 17,17 M€ (17.170.804 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo | 15.028.190 | 87,5 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 2.142.614 | 12,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,94 M€ (10.942.892 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 5.810.000 | 53,1 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 5.132.892 | 46,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.641,98 M€ · 71 códigos · 38,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `3121` | Inclusión Social | 1.042.413.626 |
| `111` | Deuda Pública | 1.036.266.604 |
| `2223` | Ertzaintza en Servicio | 593.637.284 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 350.530.000 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 224.620.255 |
| `1411` | Administración de Justicia | 141.035.786 |
| `4515` | Medios de Comunicación Social | 126.128.738 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 103.947.756 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 71.004.240 |
| `3124` | Política Familiar y Comunitaria | 66.520.951 |
| `1221` | Diversos Departamentos | 62.814.200 |
| `4711` | Política Lingüística | 52.355.841 |
| `1312` | Cooperación al Desarrollo | 45.044.551 |
| `4715` | Euskaldunización del Sistema Educativo | 42.368.194 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 39.365.000 |
| `5121` | Planificación y Administración Hidráulica | 35.100.000 |
| `1412` | Justicia | 34.137.173 |
| `3123` | Servicios Sociales | 33.499.532 |
| `4513` | Promoción de la Cultura | 31.894.656 |
| `1214` | Informática y Telecomunicaciones | 31.083.876 |
| `1111` | Parlamento | 29.400.000 |
| `3112` | Trabajo | 27.538.155 |
| `4421` | Protección del Medio Ambiente | 25.918.259 |
| `7613` | Internacionalización | 22.664.967 |
| `1212` | Servicios Generales | 22.246.797 |
| … | *resto: 46 códigos* | 350.445.454 |

</details>

### 2018

*Fuente: `GASTOSC.csv` · 109 líneas · total extraído **12.545,55 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.677,32 M€ (3.677.317.000 €) · 6 códigos · 29,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.085.006.730 | 83,9 % |
| `4115` | Farmacia | 518.301.121 | 14,1 % |
| `4113` | Salud Pública | 42.956.621 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 17.906.342 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 8.487.681 | 0,2 % |
| `4116` | Adicciones | 4.658.505 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.683,25 M€ (2.683.253.688 €) · 8 códigos · 21,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 1.012.865.752 | 37,7 % |
| `4222` | Educación Secundaria y Formación Profesional | 969.791.597 | 36,1 % |
| `4223` | Enseñanza Universitaria | 320.478.584 | 11,9 % |
| `4231` | Promoción Educativa | 176.019.706 | 6,6 % |
| `4211` | Estructura y Apoyo de Educación | 65.016.640 | 2,4 % |
| `4224` | Enseñanzas de Régimen Especial | 55.758.582 | 2,1 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 47.329.283 | 1,8 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.993.544 | 1,3 % |

</details>

<details open><summary><b><code>soberania</code> — 118,98 M€ (118.978.614 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 79.642.048 | 66,9 % |
| `7113` | Promoción y Calidad Alimentaria | 20.294.593 | 17,1 % |
| `7112` | Pesca | 19.041.973 | 16,0 % |

</details>

<details open><summary><b><code>direccion</code> — 2,46 M€ (2.462.653 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 2.462.653 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 135,02 M€ (135.019.410 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 127.027.301 | 94,1 % |
| `4313` | Ordenación Territorial | 7.992.109 | 5,9 % |

</details>

<details open><summary><b><code>empleo</code> — 766,45 M€ (766.446.224 €) · 5 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 485.037.098 | 63,3 % |
| `3231` | Formación | 224.400.058 | 29,3 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 51.071.628 | 6,7 % |
| `3212` | Economía Social | 4.994.997 | 0,7 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 942.443 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 303,75 M€ (303.753.729 €) · 7 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 149.739.301 | 49,3 % |
| `5412` | Investigación | 50.915.023 | 16,8 % |
| `5414` | Fondo de Innovación | 40.550.000 | 13,3 % |
| `5415` | Agenda de Innovación Digital | 23.708.910 | 7,8 % |
| `5411` | Investigación y Desarrollo Agropesquero | 18.763.587 | 6,2 % |
| `1215` | Innovación y Administración Electrónica | 14.657.658 | 4,8 % |
| `7214` | Innovación y Estrategia de Competitividad | 5.419.250 | 1,8 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,52 M€ (4.518.474 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 4.518.474 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 18,34 M€ (18.343.057 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 15.526.427 | 84,6 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 2.816.630 | 15,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,06 M€ (11.056.800 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 5.817.000 | 52,6 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 5.239.800 | 47,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.824,40 M€ · 72 códigos · 38,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 1.346.774.720 |
| `3121` | Inclusión Social | 1.024.403.096 |
| `2223` | Ertzaintza en Servicio | 608.584.956 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 240.927.882 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 156.237.646 |
| `1411` | Administración de Justicia | 140.959.765 |
| `4515` | Medios de Comunicación Social | 130.933.582 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 103.026.533 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 87.617.375 |
| `3124` | Política Familiar y Comunitaria | 73.614.774 |
| `4711` | Política Lingüística | 54.659.565 |
| `1221` | Diversos Departamentos | 54.359.108 |
| `1312` | Cooperación al Desarrollo | 46.044.551 |
| `4715` | Euskaldunización del Sistema Educativo | 42.590.138 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 42.069.000 |
| `5121` | Planificación y Administración Hidráulica | 37.400.002 |
| `1412` | Justicia | 35.144.761 |
| `3123` | Servicios Sociales | 34.875.735 |
| `1214` | Informática y Telecomunicaciones | 33.548.250 |
| `4513` | Promoción de la Cultura | 32.890.954 |
| `1111` | Parlamento | 30.250.000 |
| `4421` | Protección del Medio Ambiente | 27.576.333 |
| `3112` | Trabajo | 26.747.726 |
| `1212` | Servicios Generales | 24.501.381 |
| `7613` | Internacionalización | 22.733.663 |
| … | *resto: 47 códigos* | 365.927.855 |

</details>

### 2019

*Fuente: `GASTOSC.csv` · 110 líneas · total extraído **12.850,59 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.800,12 M€ (3.800.123.000 €) · 6 códigos · 29,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.193.060.073 | 84,0 % |
| `4115` | Farmacia | 530.660.637 | 14,0 % |
| `4113` | Salud Pública | 42.869.805 | 1,1 % |
| `4111` | Estructura y Apoyo de Salud | 18.522.120 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 10.406.473 | 0,3 % |
| `4116` | Adicciones | 4.603.892 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.799,85 M€ (2.799.852.674 €) · 8 códigos · 21,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 1.058.396.185 | 37,8 % |
| `4222` | Educación Secundaria y Formación Profesional | 1.014.952.270 | 36,3 % |
| `4223` | Enseñanza Universitaria | 328.861.024 | 11,7 % |
| `4231` | Promoción Educativa | 175.865.093 | 6,3 % |
| `4211` | Estructura y Apoyo de Educación | 80.604.080 | 2,9 % |
| `4224` | Enseñanzas de Régimen Especial | 57.325.200 | 2,0 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 49.238.306 | 1,8 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 34.610.516 | 1,2 % |

</details>

<details open><summary><b><code>soberania</code> — 129,47 M€ (129.468.759 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 83.321.746 | 64,4 % |
| `7113` | Promoción y Calidad Alimentaria | 25.891.915 | 20,0 % |
| `7112` | Pesca | 20.255.098 | 15,6 % |

</details>

<details open><summary><b><code>direccion</code> — 2,63 M€ (2.625.941 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 2.625.941 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 150,58 M€ (150.581.895 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 141.806.292 | 94,2 % |
| `4313` | Ordenación Territorial | 8.775.603 | 5,8 % |

</details>

<details open><summary><b><code>empleo</code> — 796,20 M€ (796.195.298 €) · 5 códigos · 6,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 514.710.579 | 64,6 % |
| `3231` | Formación | 222.925.761 | 28,0 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 52.405.325 | 6,6 % |
| `3212` | Economía Social | 5.126.190 | 0,6 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.027.443 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 325,63 M€ (325.626.770 €) · 7 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 157.599.240 | 48,4 % |
| `5412` | Investigación | 58.497.685 | 18,0 % |
| `5414` | Fondo de Innovación | 41.206.250 | 12,7 % |
| `5415` | Agenda de Innovación Digital | 25.116.151 | 7,7 % |
| `5411` | Investigación y Desarrollo Agropesquero | 20.038.239 | 6,2 % |
| `1215` | Innovación y Administración Electrónica | 15.340.349 | 4,7 % |
| `7214` | Innovación y Estrategia de Competitividad | 7.828.856 | 2,4 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,35 M€ (6.346.607 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 6.346.607 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 18,84 M€ (18.843.039 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 15.496.857 | 82,2 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.346.182 | 17,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,85 M€ (11.853.004 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 6.165.000 | 52,0 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 5.688.004 | 48,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.809,08 M€ · 73 códigos · 37,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 1.331.216.386 |
| `3121` | Inclusión Social | 989.284.682 |
| `2223` | Ertzaintza en Servicio | 625.576.701 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 238.699.007 |
| `1411` | Administración de Justicia | 143.831.608 |
| `4515` | Medios de Comunicación Social | 135.772.745 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 108.870.639 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 99.447.416 |
| `3124` | Política Familiar y Comunitaria | 83.789.240 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 80.074.555 |
| `1221` | Diversos Departamentos | 58.339.304 |
| `4711` | Política Lingüística | 56.734.909 |
| `1312` | Cooperación al Desarrollo | 46.200.000 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 43.848.000 |
| `4715` | Euskaldunización del Sistema Educativo | 42.966.641 |
| `1412` | Justicia | 37.629.490 |
| `5121` | Planificación y Administración Hidráulica | 37.542.202 |
| `3123` | Servicios Sociales | 35.548.910 |
| `1214` | Informática y Telecomunicaciones | 33.423.663 |
| `4513` | Promoción de la Cultura | 32.310.429 |
| `1222` | Crédito Global | 32.000.000 |
| `1111` | Parlamento | 31.100.000 |
| `4421` | Protección del Medio Ambiente | 28.272.243 |
| `3112` | Trabajo | 27.942.917 |
| `1212` | Servicios Generales | 24.725.076 |
| … | *resto: 48 códigos* | 403.930.250 |

</details>

### 2020

*Fuente: `GASTOSC.csv` · 110 líneas · total extraído **12.869,02 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.943,69 M€ (3.943.691.000 €) · 6 códigos · 30,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.331.446.888 | 84,5 % |
| `4115` | Farmacia | 530.928.274 | 13,5 % |
| `4113` | Salud Pública | 46.460.807 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 18.809.564 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 11.190.302 | 0,3 % |
| `4116` | Adicciones | 4.855.165 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.885,69 M€ (2.885.693.937 €) · 8 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 1.090.827.924 | 37,8 % |
| `4222` | Educación Secundaria y Formación Profesional | 1.054.829.860 | 36,6 % |
| `4223` | Enseñanza Universitaria | 334.243.048 | 11,6 % |
| `4231` | Promoción Educativa | 177.058.416 | 6,1 % |
| `4211` | Estructura y Apoyo de Educación | 82.939.749 | 2,9 % |
| `4224` | Enseñanzas de Régimen Especial | 57.615.251 | 2,0 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 50.362.749 | 1,7 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 37.816.940 | 1,3 % |

</details>

<details open><summary><b><code>soberania</code> — 132,66 M€ (132.657.441 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 83.398.855 | 62,9 % |
| `7113` | Promoción y Calidad Alimentaria | 27.694.760 | 20,9 % |
| `7112` | Pesca | 21.563.826 | 16,3 % |

</details>

<details open><summary><b><code>direccion</code> — 3,00 M€ (3.004.739 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 3.004.739 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 164,07 M€ (164.070.631 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 155.621.677 | 94,9 % |
| `4313` | Ordenación Territorial | 8.448.954 | 5,1 % |

</details>

<details open><summary><b><code>empleo</code> — 857,42 M€ (857.419.119 €) · 5 códigos · 6,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 564.714.846 | 65,9 % |
| `3231` | Formación | 234.710.596 | 27,4 % |
| `3111` | Estructura y Apoyo de Empleo y Políticas Sociales | 51.233.304 | 6,0 % |
| `3212` | Economía Social | 5.709.856 | 0,7 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.050.517 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 352,09 M€ (352.088.741 €) · 7 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 169.367.492 | 48,1 % |
| `5412` | Investigación | 66.673.630 | 18,9 % |
| `5414` | Fondo de Innovación | 42.861.032 | 12,2 % |
| `5415` | Agenda de Innovación Digital | 26.277.948 | 7,5 % |
| `5411` | Investigación y Desarrollo Agropesquero | 23.103.861 | 6,6 % |
| `1215` | Innovación y Administración Electrónica | 15.656.259 | 4,4 % |
| `7214` | Innovación y Estrategia de Competitividad | 8.148.519 | 2,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,71 M€ (6.713.383 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 6.713.383 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 19,88 M€ (19.876.097 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 16.376.200 | 82,4 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.499.897 | 17,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,25 M€ (14.249.666 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 7.326.000 | 51,4 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 6.923.666 | 48,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.489,55 M€ · 73 códigos · 34,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `3121` | Inclusión Social | 949.054.484 |
| `111` | Deuda Pública | 929.803.492 |
| `2223` | Ertzaintza en Servicio | 626.871.021 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 241.827.157 |
| `7212` | Desarrollo Industrial y Apoyo a Emprendedores | 188.347.698 |
| `1411` | Administración de Justicia | 148.614.411 |
| `4515` | Medios de Comunicación Social | 143.775.000 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 96.650.996 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 95.297.000 |
| `3124` | Política Familiar y Comunitaria | 86.250.737 |
| `4711` | Política Lingüística | 60.699.089 |
| `1312` | Cooperación al Desarrollo | 49.234.387 |
| `1221` | Diversos Departamentos | 49.185.443 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 46.750.000 |
| `4715` | Euskaldunización del Sistema Educativo | 43.579.433 |
| `1412` | Justicia | 41.107.179 |
| `5121` | Planificación y Administración Hidráulica | 41.040.748 |
| `3123` | Servicios Sociales | 36.251.621 |
| `4513` | Promoción de la Cultura | 33.259.733 |
| `1111` | Parlamento | 31.950.000 |
| `1214` | Informática y Telecomunicaciones | 31.317.231 |
| `4421` | Protección del Medio Ambiente | 30.848.218 |
| `3112` | Trabajo | 28.675.112 |
| `4514` | Patrimonio Histórico Artístico | 25.900.096 |
| `1212` | Servicios Generales | 25.694.313 |
| … | *resto: 48 códigos* | 407.566.647 |

</details>

### 2021

*Fuente: `GASTOSC.csv` · 112 líneas · total extraído **13.577,66 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.994,41 M€ (3.994.412.000 €) · 6 códigos · 29,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.376.723.660 | 84,5 % |
| `4115` | Farmacia | 530.960.838 | 13,3 % |
| `4113` | Salud Pública | 48.353.140 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 19.615.257 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 13.879.593 | 0,3 % |
| `4116` | Adicciones | 4.879.512 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.951,38 M€ (2.951.381.469 €) · 8 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4221` | Educación Infantil y Primaria | 1.120.391.576 | 38,0 % |
| `4222` | Educación Secundaria y Formación Profesional | 1.094.351.054 | 37,1 % |
| `4223` | Enseñanza Universitaria | 345.895.223 | 11,7 % |
| `4231` | Promoción Educativa | 176.544.900 | 6,0 % |
| `4211` | Estructura y Apoyo de Educación | 74.466.250 | 2,5 % |
| `4224` | Enseñanzas de Régimen Especial | 56.474.510 | 1,9 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 49.737.837 | 1,7 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 33.520.119 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 144,42 M€ (144.423.189 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 83.546.686 | 57,8 % |
| `7112` | Pesca | 30.648.842 | 21,2 % |
| `7113` | Promoción y Calidad Alimentaria | 30.227.661 | 20,9 % |

</details>

<details open><summary><b><code>direccion</code> — 3,10 M€ (3.096.212 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 3.096.212 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 173,43 M€ (173.434.237 €) · 3 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 159.631.261 | 92,0 % |
| `4313` | Ordenación Territorial | 7.401.973 | 4,3 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 6.401.003 | 3,7 % |

</details>

<details open><summary><b><code>empleo</code> — 886,74 M€ (886.738.479 €) · 5 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 566.201.855 | 63,9 % |
| `3231` | Formación | 251.167.150 | 28,3 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 62.375.217 | 7,0 % |
| `3212` | Economía Social | 5.928.973 | 0,7 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.065.284 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 384,57 M€ (384.570.989 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 185.009.033 | 48,1 % |
| `5412` | Investigación | 69.923.364 | 18,2 % |
| `5414` | Fondo de Innovación | 51.666.683 | 13,4 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 35.256.282 | 9,2 % |
| `5411` | Investigación y Desarrollo Agropesquero | 26.141.147 | 6,8 % |
| `7214` | Innovación y Estrategia de Competitividad | 8.380.978 | 2,2 % |
| `1215` | Innovación y Administración Electrónica | 8.193.502 | 2,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 8,11 M€ (8.114.553 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 8.114.553 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 18,83 M€ (18.829.896 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 15.291.077 | 81,2 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.538.819 | 18,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 21,58 M€ (21.578.502 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 7.360.000 | 34,1 % |
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 7.214.836 | 33,4 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 7.003.666 | 32,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 4.991,08 M€ · 73 códigos · 36,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 983.213.981 |
| `3121` | Inclusión Social | 938.244.788 |
| `2223` | Ertzaintza en Servicio | 655.310.809 |
| `1229` | Medidas contra la crisis provocada por COVID-19 | 551.856.250 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 241.456.601 |
| `1411` | Administración de Justicia | 158.110.201 |
| `4515` | Medios de Comunicación Social | 148.850.000 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 85.909.926 |
| `3124` | Política Familiar y Comunitaria | 77.498.784 |
| `3123` | Servicios Sociales | 65.639.624 |
| `4711` | Política Lingüística | 64.929.095 |
| `7212` | Desarrollo Industrial | 63.953.921 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 58.683.000 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 50.864.000 |
| `1312` | Cooperación al Desarrollo | 49.264.291 |
| `1221` | Diversos Departamentos | 48.366.906 |
| `1214` | Informática y Telecomunicaciones | 46.443.118 |
| `5121` | Planificación y Administración Hidráulica | 45.000.000 |
| `4715` | Euskaldunización del Sistema Educativo | 44.278.238 |
| `1412` | Justicia | 41.050.713 |
| `4421` | Protección del Medio Ambiente | 35.459.274 |
| `4513` | Promoción de la Cultura | 33.025.113 |
| `1111` | Parlamento | 31.500.000 |
| `3112` | Trabajo | 30.589.223 |
| `1212` | Servicios Generales | 25.627.978 |
| … | *resto: 48 códigos* | 415.954.640 |

</details>

### 2022

*Fuente: `csv_tidy.csv` · 113 líneas · total extraído **14.172,91 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.191,41 M€ (4.191.412.000 €) · 6 códigos · 29,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.567.631.572 | 85,1 % |
| `4115` | Farmacia | 531.410.218 | 12,7 % |
| `4113` | Salud Pública | 50.981.432 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 20.531.649 | 0,5 % |
| `4114` | Investigación y Planificación Sanitaria | 15.972.136 | 0,4 % |
| `4116` | Adicciones | 4.884.993 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.008,75 M€ (3.008.746.454 €) · 8 códigos · 21,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 1.140.510.276 | 37,9 % |
| `4221` | Educación Infantil y Primaria | 1.076.094.102 | 35,8 % |
| `4223` | Enseñanza Universitaria | 352.058.551 | 11,7 % |
| `4231` | Promoción Educativa | 190.386.365 | 6,3 % |
| `4211` | Estructura y Apoyo de Educación | 94.603.792 | 3,1 % |
| `4224` | Enseñanzas de Régimen Especial | 67.744.463 | 2,3 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 51.791.391 | 1,7 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.557.514 | 1,2 % |

</details>

<details open><summary><b><code>soberania</code> — 159,30 M€ (159.302.686 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 91.818.648 | 57,6 % |
| `7113` | Promoción y Calidad Alimentaria | 38.863.091 | 24,4 % |
| `7112` | Pesca | 28.620.947 | 18,0 % |

</details>

<details open><summary><b><code>direccion</code> — 3,12 M€ (3.119.424 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 3.119.424 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 193,45 M€ (193.449.154 €) · 3 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 170.716.609 | 88,2 % |
| `4313` | Ordenación Territorial | 16.215.513 | 8,4 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 6.517.032 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 923,36 M€ (923.357.972 €) · 5 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 574.121.476 | 62,2 % |
| `3231` | Formación | 264.757.134 | 28,7 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 75.729.636 | 8,2 % |
| `3212` | Economía Social | 7.652.483 | 0,8 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.097.243 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 426,02 M€ (426.016.092 €) · 7 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 203.288.725 | 47,7 % |
| `5412` | Investigación | 74.141.042 | 17,4 % |
| `5414` | Fondo de Innovación | 53.248.107 | 12,5 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 47.605.661 | 11,2 % |
| `5411` | Investigación y Desarrollo Agropesquero | 30.449.398 | 7,1 % |
| `7214` | Innovación y Estrategia de Competitividad | 9.012.642 | 2,1 % |
| `1215` | Innovación y Administración Electrónica | 8.270.517 | 1,9 % |

</details>

<details open><summary><b><code>diversidad</code> — 8,51 M€ (8.507.633 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 8.507.633 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,96 M€ (25.960.688 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 22.313.447 | 86,0 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.647.241 | 14,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 23,66 M€ (23.661.933 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 8.523.933 | 36,0 % |
| `3223` | Emakunde-Instituto Vasco de la Mujer | 7.763.000 | 32,8 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 7.375.000 | 31,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 5.209,37 M€ · 74 códigos · 36,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 929.488.625 |
| `3121` | Inclusión Social | 883.286.944 |
| `2223` | Ertzaintza en Servicio | 686.301.665 |
| `1229` | Medidas contra la crisis provocada por COVID-19 | 353.058.812 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 297.142.587 |
| `1221` | Diversos Departamentos | 216.356.670 |
| `1411` | Administración de Justicia | 168.199.262 |
| `4515` | Medios de Comunicación Social | 161.907.000 |
| `7212` | Desarrollo Industrial | 105.850.125 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 80.584.631 |
| `3124` | Política Familiar y Comunitaria | 73.669.818 |
| `1413` | Programa 1413 | 69.949.980 |
| `4711` | Política Lingüística | 69.440.590 |
| `6311` | Política Financiera | 67.306.633 |
| `3123` | Servicios Sociales | 67.147.368 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 56.216.000 |
| `1312` | Cooperación al Desarrollo | 50.264.291 |
| `1214` | Informática y Telecomunicaciones | 50.163.428 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 48.193.000 |
| `5121` | Planificación y Administración Hidráulica | 47.895.522 |
| `4715` | Euskaldunización del Sistema Educativo | 45.154.775 |
| `1412` | Justicia | 41.833.513 |
| `4421` | Protección del Medio Ambiente | 41.322.376 |
| `4514` | Patrimonio Histórico Artístico | 35.761.984 |
| `4513` | Promoción de la Cultura | 35.327.337 |
| … | *resto: 49 códigos* | 527.548.028 |

</details>

### 2023

*Fuente: `csv_tidy.csv` · 113 líneas · total extraído **15.502,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.633,31 M€ (4.633.308.410 €) · 6 códigos · 29,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 3.973.650.051 | 85,8 % |
| `4115` | Farmacia | 561.368.405 | 12,1 % |
| `4113` | Salud Pública | 52.577.559 | 1,1 % |
| `4111` | Estructura y Apoyo de Salud | 20.804.467 | 0,4 % |
| `4114` | Investigación y Planificación Sanitaria | 20.562.238 | 0,4 % |
| `4116` | Adicciones | 4.345.690 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.252,00 M€ (3.251.996.590 €) · 8 códigos · 21,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 1.336.206.169 | 41,1 % |
| `4221` | Educación Infantil y Primaria | 1.138.091.431 | 35,0 % |
| `4223` | Enseñanza Universitaria | 374.941.910 | 11,5 % |
| `4231` | Promoción Educativa | 188.755.471 | 5,8 % |
| `4211` | Estructura y Apoyo de Educación | 73.889.411 | 2,3 % |
| `4224` | Enseñanzas de Régimen Especial | 67.144.520 | 2,1 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 39.040.331 | 1,2 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 33.927.347 | 1,0 % |

</details>

<details open><summary><b><code>soberania</code> — 181,86 M€ (181.855.054 €) · 3 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 93.942.598 | 51,7 % |
| `7113` | Promoción y Calidad Alimentaria | 60.399.664 | 33,2 % |
| `7112` | Pesca | 27.512.792 | 15,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,32 M€ (3.318.400 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 3.318.400 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 225,53 M€ (225.527.077 €) · 3 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 186.175.969 | 82,6 % |
| `4313` | Ordenación Territorial | 32.711.933 | 14,5 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 6.639.175 | 2,9 % |

</details>

<details open><summary><b><code>empleo</code> — 788,75 M€ (788.747.677 €) · 5 códigos · 5,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 425.438.467 | 53,9 % |
| `3231` | Formación | 271.282.380 | 34,4 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 82.689.467 | 10,5 % |
| `3212` | Economía Social | 8.208.350 | 1,0 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.129.013 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 450,48 M€ (450.482.141 €) · 7 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 211.208.800 | 46,9 % |
| `5412` | Investigación | 86.143.424 | 19,1 % |
| `5414` | Fondo de Innovación | 52.900.356 | 11,7 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 50.610.095 | 11,2 % |
| `5411` | Investigación y Desarrollo Agropesquero | 30.322.862 | 6,7 % |
| `7214` | Innovación y Estrategia de Competitividad | 10.488.899 | 2,3 % |
| `1215` | Innovación y Administración Electrónica | 8.807.705 | 2,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 16,10 M€ (16.104.285 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 16.104.285 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 26,00 M€ (26.001.642 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 22.088.780 | 85,0 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.912.862 | 15,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 24,25 M€ (24.254.815 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 8.916.998 | 36,8 % |
| `3223` | Emakunde-Instituto Vasco de la Mujer | 7.886.000 | 32,5 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 7.451.817 | 30,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 5.900,55 M€ · 74 códigos · 38,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `3121` | Inclusión Social | 1.349.934.262 |
| `111` | Deuda Pública | 989.688.783 |
| `2223` | Ertzaintza en Servicio | 709.213.701 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 321.891.789 |
| `1228` | Programa 1228 | 276.642.715 |
| `4515` | Medios de Comunicación Social | 182.957.000 |
| `1411` | Administración de Justicia | 175.978.610 |
| `3124` | Política Familiar y Comunitaria | 159.941.293 |
| `7212` | Desarrollo Industrial | 137.000.086 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 126.693.000 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 111.196.562 |
| `6311` | Política Financiera | 88.424.348 |
| `3123` | Servicios Sociales | 85.184.790 |
| `4711` | Política Lingüística | 73.545.542 |
| `1413` | Programa 1413 | 70.904.051 |
| `4715` | Euskaldunización del Sistema Educativo | 64.237.378 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 58.648.000 |
| `1214` | Informática y Telecomunicaciones | 55.638.695 |
| `1312` | Cooperación al Desarrollo | 50.421.110 |
| `5121` | Planificación y Administración Hidráulica | 48.195.522 |
| `4421` | Protección del Medio Ambiente | 44.097.138 |
| `1412` | Justicia | 43.862.600 |
| `1212` | Servicios Generales | 38.922.730 |
| `4513` | Promoción de la Cultura | 36.678.560 |
| `4514` | Patrimonio Histórico Artístico | 36.444.932 |
| … | *resto: 49 códigos* | 564.205.712 |

</details>

### 2024

*Fuente: `csv_tidy.csv` · 114 líneas · total extraído **16.350,98 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.893,90 M€ (4.893.900.000 €) · 6 códigos · 29,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 4.209.862.870 | 86,0 % |
| `4115` | Farmacia | 582.085.773 | 11,9 % |
| `4113` | Salud Pública | 56.541.635 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 20.865.082 | 0,4 % |
| `4114` | Investigación y Planificación Sanitaria | 19.510.512 | 0,4 % |
| `4116` | Adicciones | 5.034.128 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.449,29 M€ (3.449.291.856 €) · 8 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 1.463.174.070 | 42,4 % |
| `4221` | Educación Infantil y Primaria | 1.211.845.738 | 35,1 % |
| `4223` | Enseñanza Universitaria | 397.264.041 | 11,5 % |
| `4231` | Promoción Educativa | 185.449.508 | 5,4 % |
| `4224` | Enseñanzas de Régimen Especial | 71.196.796 | 2,1 % |
| `4211` | Estructura y Apoyo de Educación | 50.896.128 | 1,5 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 37.087.928 | 1,1 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 32.377.647 | 0,9 % |

</details>

<details open><summary><b><code>soberania</code> — 207,90 M€ (207.904.603 €) · 3 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 120.227.025 | 57,8 % |
| `7113` | Promoción y Calidad Alimentaria | 58.503.651 | 28,1 % |
| `7112` | Pesca | 29.173.927 | 14,0 % |

</details>

<details open><summary><b><code>direccion</code> — 3,53 M€ (3.528.813 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 3.528.813 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 253,47 M€ (253.469.311 €) · 3 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 210.800.252 | 83,2 % |
| `4313` | Ordenación Territorial | 36.149.617 | 14,3 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 6.519.442 | 2,6 % |

</details>

<details open><summary><b><code>empleo</code> — 807,33 M€ (807.325.895 €) · 5 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 431.872.838 | 53,5 % |
| `3231` | Formación | 278.384.360 | 34,5 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 88.115.463 | 10,9 % |
| `3212` | Economía Social | 7.797.601 | 1,0 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.155.633 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 461,84 M€ (461.841.800 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 204.192.192 | 44,2 % |
| `5412` | Investigación | 98.348.334 | 21,3 % |
| `5414` | Fondo de Innovación | 56.408.743 | 12,2 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 48.041.569 | 10,4 % |
| `5411` | Investigación y Desarrollo Agropesquero | 31.529.613 | 6,8 % |
| `7214` | Innovación y Estrategia de Competitividad | 14.107.750 | 3,1 % |
| `1215` | Innovación y Administración Electrónica | 9.213.599 | 2,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 17,50 M€ (17.503.465 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 17.503.465 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 24,85 M€ (24.847.812 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 20.984.107 | 84,5 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.863.705 | 15,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 25,62 M€ (25.620.770 €) · 3 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 9.686.880 | 37,8 % |
| `3223` | Emakunde-Instituto Vasco de la Mujer | 8.184.000 | 31,9 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 7.749.890 | 30,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 6.205,74 M€ · 75 códigos · 38,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `3121` | Inclusión Social | 1.494.359.475 |
| `111` | Deuda Pública | 861.402.513 |
| `2223` | Ertzaintza en Servicio | 737.976.372 |
| `1228` | Programa 1228 | 341.447.678 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 332.779.539 |
| `1411` | Administración de Justicia | 194.821.605 |
| `4515` | Medios de Comunicación Social | 193.755.000 |
| `3124` | Política Familiar y Comunitaria | 162.191.071 |
| `7212` | Desarrollo Industrial | 140.421.895 |
| `5136` | Variante Sur Ferroviaria de Bilbao-C. de Gestión | 128.222.000 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 118.302.936 |
| `3123` | Servicios Sociales | 90.053.724 |
| `6311` | Política Financiera | 84.839.914 |
| `4711` | Política Lingüística | 77.194.169 |
| `1413` | Programa 1413 | 74.062.172 |
| `3222` | Juventud | 65.471.610 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 61.640.000 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 60.503.000 |
| `1214` | Informática y Telecomunicaciones | 58.346.414 |
| `1312` | Cooperación al Desarrollo | 55.671.110 |
| `5121` | Planificación y Administración Hidráulica | 48.495.522 |
| `1412` | Justicia | 47.331.731 |
| `4421` | Protección del Medio Ambiente | 44.116.061 |
| `4513` | Promoción de la Cultura | 40.192.245 |
| `1212` | Servicios Generales | 39.318.398 |
| … | *resto: 50 códigos* | 652.824.521 |

</details>

### 2025

*Fuente: `csv_tidy.csv` · 119 líneas · total extraído **17.069,78 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.111,57 M€ (5.111.574.813 €) · 6 códigos · 29,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 4.400.959.951 | 86,1 % |
| `4115` | Farmacia | 602.670.021 | 11,8 % |
| `4113` | Salud Pública | 63.700.206 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 21.450.692 | 0,4 % |
| `4114` | Investigación y Planificación Sanitaria | 17.762.234 | 0,3 % |
| `4116` | Adicciones | 5.031.709 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.593,81 M€ (3.593.813.245 €) · 8 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 1.515.076.438 | 42,2 % |
| `4221` | Educación Infantil y Primaria | 1.169.490.359 | 32,5 % |
| `4223` | Enseñanza Universitaria | 456.629.240 | 12,7 % |
| `4231` | Promoción Educativa | 175.846.640 | 4,9 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 111.247.151 | 3,1 % |
| `4224` | Enseñanzas de Régimen Especial | 72.461.332 | 2,0 % |
| `4211` | Estructura y Apoyo de Educación | 52.561.031 | 1,5 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 40.501.054 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 221,22 M€ (221.216.137 €) · 4 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 132.462.196 | 59,9 % |
| `7113` | Promoción y Calidad Alimentaria | 54.266.994 | 24,5 % |
| `7112` | Pesca | 29.620.812 | 13,4 % |
| `7110` | Programa 7110 | 4.866.135 | 2,2 % |

</details>

<details open><summary><b><code>direccion</code> — 4,62 M€ (4.619.249 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 4.619.249 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 321,80 M€ (321.804.915 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 291.902.081 | 90,7 % |
| `4313` | Ordenación Territorial | 24.563.324 | 7,6 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 5.339.510 | 1,7 % |

</details>

<details open><summary><b><code>empleo</code> — 838,17 M€ (838.169.949 €) · 5 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 426.672.072 | 50,9 % |
| `3231` | Formación | 280.934.700 | 33,5 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 120.713.972 | 14,4 % |
| `3212` | Economía Social | 8.664.888 | 1,0 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.184.317 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 498,97 M€ (498.967.802 €) · 8 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 202.629.671 | 40,6 % |
| `5412` | Investigación | 111.246.300 | 22,3 % |
| `5414` | Fondo de Innovación | 76.692.318 | 15,4 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 45.700.114 | 9,2 % |
| `5411` | Investigación y Desarrollo Agropesquero | 31.814.126 | 6,4 % |
| `7214` | Innovación y Estrategia de Competitividad | 17.529.975 | 3,5 % |
| `1215` | Innovación y Administración Electrónica | 8.482.785 | 1,7 % |
| `5410` | Programa 5410 | 4.872.513 | 1,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 19,02 M€ (19.022.678 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 19.022.678 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,08 M€ (25.082.941 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 21.128.845 | 84,2 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.954.096 | 15,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 23,61 M€ (23.613.784 €) · 3 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3223` | Emakunde-Instituto Vasco de la Mujer | 7.983.000 | 33,8 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 7.899.890 | 33,5 % |
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 7.730.894 | 32,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 6.411,89 M€ · 78 códigos · 37,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `3121` | Inclusión Social | 1.495.378.928 |
| `111` | Deuda Pública | 1.024.802.826 |
| `2223` | Ertzaintza en Servicio | 752.905.950 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 458.801.573 |
| `1228` | Programa 1228 | 271.128.952 |
| `4515` | Medios de Comunicación Social | 200.650.000 |
| `1411` | Administración de Justicia | 200.040.736 |
| `3124` | Política Familiar y Comunitaria | 160.556.629 |
| `7212` | Desarrollo Industrial | 147.144.727 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 126.026.667 |
| `3123` | Servicios Sociales | 100.047.449 |
| `4711` | Política Lingüística | 88.140.412 |
| `1413` | Programa 1413 | 88.041.623 |
| `6311` | Política Financiera | 71.698.287 |
| `1214` | Informática y Telecomunicaciones | 68.854.800 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 68.030.000 |
| `5135` | Nueva Red Ferroviaria en la CAE-Créditos Gestión | 67.355.000 |
| `3222` | Juventud | 64.751.120 |
| `1312` | Cooperación al Desarrollo | 55.721.110 |
| `5121` | Planificación y Administración Hidráulica | 53.700.000 |
| `1412` | Justicia | 50.236.365 |
| `4421` | Protección del Medio Ambiente | 47.149.942 |
| `4513` | Promoción de la Cultura | 43.888.534 |
| `3112` | Trabajo | 41.461.826 |
| `1221` | Diversos Departamentos | 40.587.587 |
| … | *resto: 53 códigos* | 624.789.444 |

</details>

### 2026

*Fuente: `csv_tidy.csv` · 119 líneas · total extraído **17.495,94 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.321,77 M€ (5.321.765.500 €) · 6 códigos · 30,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4112` | Financiación y Contratación Sanitaria | 4.592.860.307 | 86,3 % |
| `4115` | Farmacia | 621.991.695 | 11,7 % |
| `4113` | Salud Pública | 63.353.075 | 1,2 % |
| `4111` | Estructura y Apoyo de Salud | 21.881.482 | 0,4 % |
| `4114` | Investigación y Planificación Sanitaria | 16.941.032 | 0,3 % |
| `4116` | Adicciones | 4.737.909 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.789,15 M€ (3.789.148.697 €) · 8 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4222` | Educación Secundaria y Formación Profesional | 1.553.926.050 | 41,0 % |
| `4221` | Educación Infantil y Primaria | 1.253.454.551 | 33,1 % |
| `4223` | Enseñanza Universitaria | 481.023.016 | 12,7 % |
| `4231` | Promoción Educativa | 204.516.916 | 5,4 % |
| `4225` | Innovación Educ. y Form. Perman. del Profesorado | 129.673.549 | 3,4 % |
| `4224` | Enseñanzas de Régimen Especial | 71.666.198 | 1,9 % |
| `4211` | Estructura y Apoyo de Educación | 59.308.491 | 1,6 % |
| `4226` | Aprendizaje Permanente y Ed. Personas Adultas EPA | 35.579.926 | 0,9 % |

</details>

<details open><summary><b><code>soberania</code> — 208,88 M€ (208.876.985 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7111` | Agricultura y Desarrollo Rural y Litoral | 125.502.384 | 60,1 % |
| `7113` | Promoción y Calidad Alimentaria | 47.391.771 | 22,7 % |
| `7112` | Pesca | 26.902.995 | 12,9 % |
| `7110` | Programa 7110 | 9.079.835 | 4,3 % |

</details>

<details open><summary><b><code>direccion</code> — 4,80 M€ (4.802.023 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `1217` | Relaciones Institucionales | 4.802.023 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 442,04 M€ (442.040.124 €) · 3 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4312` | Vivienda | 394.391.491 | 89,2 % |
| `4313` | Ordenación Territorial | 42.384.705 | 9,6 % |
| `4311` | Estructura y Apoyo Plan.Territ. Vivienda y Trans | 5.263.928 | 1,2 % |

</details>

<details open><summary><b><code>empleo</code> — 418,21 M€ (418.207.888 €) · 5 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3211` | Empleo | 219.491.405 | 52,5 % |
| `3231` | Formación | 126.801.120 | 30,3 % |
| `3110` | Estructura y Apoyo de Trabajo y Empleo | 62.222.542 | 14,9 % |
| `3212` | Economía Social | 8.478.896 | 2,0 % |
| `3213` | Consejo Superior de Cooperativas de Euskadi | 1.213.925 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 532,31 M€ (532.306.939 €) · 8 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `5413` | Tecnología | 245.661.921 | 46,2 % |
| `5412` | Investigación | 119.749.309 | 22,5 % |
| `5414` | Fondo de Innovación | 60.899.904 | 11,4 % |
| `5415` | Transformación Digital y Emprendimiento Innovador | 40.148.402 | 7,5 % |
| `5411` | Investigación y Desarrollo Agropesquero | 32.888.997 | 6,2 % |
| `7214` | Innovación y Estrategia de Competitividad | 19.050.126 | 3,6 % |
| `1215` | Innovación y Administración Electrónica | 8.412.228 | 1,6 % |
| `5410` | Programa 5410 | 5.496.052 | 1,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 18,04 M€ (18.044.148 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3122` | Inmigración | 18.044.148 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 27,13 M€ (27.129.421 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `7511` | Turismo y Hostelería | 23.148.583 | 85,3 % |
| `7510` | Estructura y Apoyo de Turismo, Comercio y Consumo | 3.980.838 | 14,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 25,17 M€ (25.172.718 €) · 3 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3111` | Estructura y Apoyo de Igualdad, Justicia y P. Soc | 8.723.218 | 34,7 % |
| `3223` | Emakunde-Instituto Vasco de la Mujer | 8.264.000 | 32,8 % |
| `3221` | Promoción de Igualdad Oportunidades para la Mujer | 8.185.500 | 32,5 % |

</details>

<details><summary><code>(sin concepto)</code> — 6.708,44 M€ · 78 códigos · 38,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `111` | Deuda Pública | 1.145.807.319 |
| `6311` | Política Financiera | 881.610.064 |
| `2223` | Ertzaintza en Servicio | 802.735.859 |
| `3121` | Inclusión Social | 786.645.055 |
| `5131` | Infraestructura y Gestión Transporte Ferroviario | 489.626.607 |
| `7212` | Desarrollo Industrial | 222.076.576 |
| `1411` | Administración de Justicia | 211.110.350 |
| `4515` | Medios de Comunicación Social | 210.238.600 |
| `3124` | Política Familiar y Comunitaria | 169.108.754 |
| `9119` | Otras Relaciones Financieras con Sec. Públi. Vasc | 119.908.176 |
| `3123` | Servicios Sociales | 99.498.747 |
| `4711` | Política Lingüística | 93.529.364 |
| `1413` | Programa 1413 | 86.601.085 |
| `1228` | Programa 1228 | 82.242.094 |
| `4713` | Inst. Alfabetización y Reeuskaldunización Adulto | 73.733.000 |
| `1214` | Informática y Telecomunicaciones | 65.128.427 |
| `7311` | Política y Desarrollo Energético y Minero | 59.944.321 |
| `1312` | Cooperación al Desarrollo | 55.721.110 |
| `5121` | Planificación y Administración Hidráulica | 55.259.411 |
| `1412` | Justicia | 54.223.577 |
| `1221` | Diversos Departamentos | 49.372.037 |
| `4513` | Promoción de la Cultura | 48.677.554 |
| `4421` | Protección del Medio Ambiente | 47.955.498 |
| `5136` | Variante Sur Ferroviaria de Bilbao-C. de Gestión | 46.100.000 |
| `3222` | Juventud | 44.760.554 |
| … | *resto: 53 códigos* | 706.829.418 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py pvc     # regenera este documento
python3 tools/auditoria_magnitud.py pvc        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa pvc --anio <año> \
    --input ../fuentes/raw/pvc/<año>/<fichero> --output /tmp/pvc.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-pvc.md`](limitaciones-pvc.md)

