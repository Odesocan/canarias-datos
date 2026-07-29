# Trazabilidad de la extracción — Comunidad Valenciana (`val`)

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
| **2015** | 122 | `tomo_II.html` | 10 | 42,6 % | 17.188,15 | — | no_aplica |
| **2016** | 129 | `tomo_II.html` | 12 | 45,0 % | 17.155,82 | — | no_aplica |
| **2017** | 128 | `tomo_II.html` | 12 | 43,8 % | 17.724,97 | — | no_aplica |
| **2018** | 128 | `tomo_II.html` | 12 | 43,8 % | 19.956,91 | — | no_aplica |
| **2019** | 131 | `tomo_II.html` | 12 | 42,7 % | 22.096,21 | — | no_aplica |
| **2020** | 153 | `tomo_II.html` | 12 | 45,8 % | 23.021,99 | — | no_aplica |
| **2021** | 154 | `tomo_II.html` | 12 | 45,5 % | 25.627,55 | — | no_aplica |
| **2022** | 169 | `tomo_II.html` | 12 | 47,3 % | 27.967,47 | — | no_aplica |
| **2023** | 174 | `tomo_II.html` | 12 | 46,6 % | 28.438,26 | — | no_aplica |
| **2024** | 173 | `tomo_II.html` | 13 | 46,2 % | 29.732,20 | — | no_aplica |
| **2025** | 174 | `tomo_II.html` | 13 | 43,1 % | 32.291,43 | — | no_aplica |
| **2026** | 176 | `tomo_II.html` | 13 | 42,6 % | 33.305,51 | — | no_aplica |

**URL(s) de origen:**
- <https://hisenda.gva.es/auto/presupuestos/2015/index_c.html>
- <https://hisenda.gva.es/auto/presupuestos/2016/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2017/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2018/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2019/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2020/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2021/index_cas.html>
- <https://hisenda.gva.es/auto/presupuestos/2022/T2_ES.html>
- <https://hisenda.gva.es/auto/presupuestos/2023/T2_ES.html>
- <https://hisenda.gva.es/auto/presupuestos/2024/T2_ES.html>
- <https://hisenda.gva.es/auto/presupuestos/2025/T2_ES.html>
- <https://hisenda.gva.es/auto/presupuestos/2026/T2_ES.html>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 5.440,59 | 5.853,34 | 6.034,15 | 6.346,30 | 6.603,09 | 6.744,50 | 7.496,79 | 7.801,43 | 8.214,44 | 8.432,15 | 9.081,45 | 9.293,31 |
| `educacion` | 3.991,32 | 4.183,28 | 4.394,33 | 4.568,05 | 4.946,00 | 5.124,74 | 5.550,77 | 6.132,54 | 6.432,87 | 6.600,31 | 7.230,13 | 7.572,36 |
| `soberania` | 135,62 | 187,35 | 198,98 | 221,56 | 246,73 | 254,57 | 268,26 | 273,30 | 282,55 | 295,54 | 311,27 | 304,09 |
| `direccion` | 8,12 | 8,15 | 8,63 | 9,91 | 11,38 | 14,52 | 11,77 | 13,34 | 18,49 | 19,84 | 21,15 | 23,05 |
| `vivienda` | 41,97 | 83,39 | 98,20 | 102,84 | 170,32 | 194,29 | 216,86 | 381,26 | 423,12 | 418,55 | 316,43 | 408,61 |
| `empleo` | 138,35 | 170,21 | 166,17 | 174,12 | 167,54 | 169,46 | 259,03 | 266,15 | 285,20 | 208,25 | 303,50 | 215,37 |
| `idi` | 61,62 | 54,81 | 63,99 | 77,53 | 95,58 | 105,41 | 148,63 | 254,52 | 274,20 | 252,83 | 226,08 | 323,62 |
| `dependencia` | 489,97 | 601,54 | 593,98 | 624,71 | 823,33 | 1.202,12 | 1.386,46 | 1.480,11 | 1.589,47 | 1.710,30 | 1.920,15 | 2.028,21 |
| `discapacidad` | — | 200,43 | 215,30 | 233,46 | 279,77 | 49,15 | 51,76 | 59,42 | 55,10 | 52,63 | 58,80 | 61,11 |
| `salud_mental` | 87,27 | 89,62 | 87,82 | 89,37 | 91,02 | 95,77 | 108,57 | 129,29 | 136,92 | 158,55 | 192,13 | 218,81 |
| `diversidad` | — | — | — | — | — | — | — | — | — | 17,90 | 21,40 | 18,63 |
| `turismo` | 96,16 | 112,84 | 118,12 | 129,12 | 138,42 | 135,99 | 136,08 | 128,29 | 133,88 | 111,26 | 141,76 | 150,60 |
| `igualdad` | — | 18,38 | 20,74 | 25,47 | 39,21 | 42,82 | 43,69 | 67,67 | 69,53 | 59,20 | 61,55 | 67,33 |
| **Σ asignado** | 10.490,99 | 11.563,34 | 12.000,40 | 12.602,43 | 13.612,40 | 14.133,33 | 15.678,66 | 16.987,32 | 17.915,76 | 18.337,30 | 19.885,80 | 20.685,09 |
| *(sin concepto)* | 6.697,16 | 5.592,48 | 5.724,57 | 7.354,48 | 8.483,82 | 8.888,66 | 9.948,89 | 10.980,15 | 10.522,50 | 11.394,90 | 12.405,63 | 12.620,42 |
| **TOTAL extraído** | 17.188,15 | 17.155,82 | 17.724,97 | 19.956,91 | 22.096,21 | 23.021,99 | 25.627,55 | 27.967,47 | 28.438,26 | 29.732,20 | 32.291,43 | 33.305,51 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +7,6 % | +3,1 % | +5,2 % | +4,0 % | +2,1 % | +11,2 % | +4,1 % | +5,3 % | +2,7 % | +7,7 % | +2,3 % |
| `educacion` | +4,8 % | +5,0 % | +4,0 % | +8,3 % | +3,6 % | +8,3 % | +10,5 % | +4,9 % | +2,6 % | +9,5 % | +4,7 % |
| `soberania` | +38,1 % | +6,2 % | +11,3 % | +11,4 % | +3,2 % | +5,4 % | +1,9 % | +3,4 % | +4,6 % | +5,3 % | −2,3 % |
| `direccion` | +0,4 % | +5,9 % | +14,8 % | +14,9 % | +27,5 % | −19,0 % | +13,4 % | +38,5 % | +7,3 % | +6,6 % | +9,0 % |
| `vivienda` | +98,7 % ⚠ | +17,8 % | +4,7 % | +65,6 % ⚠ | +14,1 % | +11,6 % | +75,8 % ⚠ | +11,0 % | −1,1 % | −24,4 % | +29,1 % |
| `empleo` | +23,0 % | −2,4 % | +4,8 % | −3,8 % | +1,1 % | +52,9 % ⚠ | +2,7 % | +7,2 % | −27,0 % | +45,7 % ⚠ | −29,0 % |
| `idi` | −11,1 % | +16,8 % | +21,2 % | +23,3 % | +10,3 % | +41,0 % ⚠ | +71,2 % ⚠ | +7,7 % | −7,8 % | −10,6 % | +43,1 % ⚠ |
| `dependencia` | +22,8 % | −1,3 % | +5,2 % | +31,8 % | +46,0 % ⚠ | +15,3 % | +6,8 % | +7,4 % | +7,6 % | +12,3 % | +5,6 % |
| `discapacidad` | **nuevo** ⛔ | +7,4 % | +8,4 % | +19,8 % | −82,4 % ⚠ | +5,3 % | +14,8 % | −7,3 % | −4,5 % | +11,7 % | +3,9 % |
| `salud_mental` | +2,7 % | −2,0 % | +1,8 % | +1,8 % | +5,2 % | +13,4 % | +19,1 % | +5,9 % | +15,8 % | +21,2 % | +13,9 % |
| `diversidad` | · | · | · | · | · | · | · | · | **nuevo** ⛔ | +19,6 % | −13,0 % |
| `turismo` | +17,3 % | +4,7 % | +9,3 % | +7,2 % | −1,8 % | +0,1 % | −5,7 % | +4,4 % | −16,9 % | +27,4 % | +6,2 % |
| `igualdad` | **nuevo** ⛔ | +12,8 % | +22,8 % | +53,9 % ⚠ | +9,2 % | +2,0 % | +54,9 % ⚠ | +2,8 % | −14,9 % | +4,0 % | +9,4 % |
| **TOTAL** | −0,2 % | +3,3 % | +12,6 % | +10,7 % | +4,2 % | +11,3 % | +9,1 % | +1,7 % | +4,5 % | +8,6 % | +3,1 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `discapacidad` | **APARECE** | 0 → 200,43 M€ |
| 2019 | `vivienda` | **SALTO** | 102,84 → 170,32 M€ (+65,6 % ⚠) |
| 2020 | `dependencia` | **SALTO** | 823,33 → 1.202,12 M€ (+46,0 % ⚠) |
| 2020 | `discapacidad` | **SALTO** | 279,77 → 49,15 M€ (−82,4 % ⚠) |
| 2021 | `empleo` | **SALTO** | 169,46 → 259,03 M€ (+52,9 % ⚠) |
| 2021 | `idi` | **SALTO** | 105,41 → 148,63 M€ (+41,0 % ⚠) |
| 2022 | `idi` | **SALTO** | 148,63 → 254,52 M€ (+71,2 % ⚠) |
| 2022 | `vivienda` | **SALTO** | 216,86 → 381,26 M€ (+75,8 % ⚠) |
| 2025 | `empleo` | **SALTO** | 208,25 → 303,50 M€ (+45,7 % ⚠) |
| 2026 | `idi` | **SALTO** | 226,08 → 323,62 M€ (+43,1 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (4 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `313.4` | 279,77 | 2015:(sin concepto), 2016:discapacidad, 2017:discapacidad, 2018:discapacidad, 2019:discapacidad, 2020:discapacidad, 2021:discapacidad, 2022:discapacidad, 2023:discapacidad |
| `412B28` | 138,46 | 2024:salud_mental, 2025:sanidad, 2026:sanidad |
| `323.1` | 50,30 | 2015:(sin concepto), 2016:igualdad, 2017:igualdad, 2018:igualdad, 2019:igualdad, 2020:igualdad, 2021:igualdad, 2022:igualdad, 2023:igualdad |
| `442.5` | 46,86 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:educacion, 2021:educacion, 2022:educacion, 2023:educacion |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `tomo_II.html` · 122 líneas · total extraído **17.188,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.440,59 M€ (5.440.586.000 €) · 15 códigos · 31,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 3.901.190.220 | 71,7 % |
| `412.23` | Prestaciones Farmacéuticas | 884.805.340 | 16,3 % |
| `412.24` | Prestaciones Externas - | 207.600.000 | 3,8 % |
| `412.26` | Personal Sanitario Residente | 113.633.190 | 2,1 % |
| `412.27` | Prestaciones Externas - | 99.400.000 | 1,8 % |
| `412.1` | Centros Integrados de Salud Pública | 54.286.260 | 1,0 % |
| `413.1` | Salud | 43.548.610 | 0,8 % |
| `412.29` | Información para la Salud | 36.935.410 | 0,7 % |
| `411.1` | Dirección y Servicios Generales | 34.871.800 | 0,6 % |
| `311.1` | Dirección y Servicios Generales | 34.858.580 | 0,6 % |
| `411.6` | Análisis y Evaluación de la | 11.638.870 | 0,2 % |
| `412.25` | Servicios Generales de la Secretaría | 5.809.950 | 0,1 % |
| `411.2` | Administración Económico | 4.526.120 | 0,1 % |
| `411.3` | Administración de Recursos | 3.774.670 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 3.706.980 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 3.991,32 M€ (3.991.316.670 €) · 14 códigos · 23,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.3` | Enseñanza Secundaria | 1.588.457.940 | 39,8 % |
| `422.2` | Enseñanza Primaria | 1.516.592.130 | 38,0 % |
| `422.6` | Universidad y Estudios Superiores | 729.658.020 | 18,3 % |
| `421.4` | Administración Educativa y Cultural | 39.152.790 | 1,0 % |
| `421.3` | Ordenación Educativa | 34.350.240 | 0,9 % |
| `421.5` | Evaluación, Innovación, Calidad | 20.018.840 | 0,5 % |
| `421.1` | Dirección y Servicios Generales | 19.754.360 | 0,5 % |
| `422.4` | Formación Profesional y Enseñanzas | 13.109.260 | 0,3 % |
| `421.9` | Innovación Tecnológica Educativa | 9.828.670 | 0,2 % |
| `421.8` | Administración General de | 7.413.590 | 0,2 % |
| `422.5` | Promoción y Uso del Valenciano | 6.456.750 | 0,2 % |
| `421.2` | Administración de Personal y | 4.189.020 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 1.946.180 | 0,0 % |
| `422.7` | Consejo Escolar de la Comunitat | 388.880 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 135,62 M€ (135.618.340 €) · 7 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714.2` | Fomento y Garantía Agraria | 58.142.150 | 42,9 % |
| `711.1` | Dirección y Servicios Generales | 25.194.220 | 18,6 % |
| `714.1` | Ordenación y Mejora de la | 18.165.120 | 13,4 % |
| `714.8` | Desarrollo y Mejora de la Ganadería | 11.376.940 | 8,4 % |
| `714.4` | Concentración de la Oferta y el | 10.999.320 | 8,1 % |
| `714.7` | Desarrollo del Medio Rural | 6.795.240 | 5,0 % |
| `714.6` | Calidad Agroalimentaria | 4.945.350 | 3,6 % |

</details>

<details open><summary><b><code>direccion</code> — 8,12 M€ (8.118.230 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 8.118.230 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 41,97 M€ (41.974.450 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Arquitectura, Vivienda y Proyectos | 37.631.260 | 89,7 % |
| `432.2` | Urbanismo y Evaluación Ambiental | 4.343.190 | 10,3 % |

</details>

<details open><summary><b><code>empleo</code> — 138,35 M€ (138.352.840 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Servicio Valenciano de Empleo y - - - | 112.831.750 | 81,6 % |
| `315.1` | Condiciones de Trabajo y | 20.928.780 | 15,1 % |
| `322.55` | Promoción de Emprendedores, | 4.592.310 | 3,3 % |

</details>

<details open><summary><b><code>idi</code> — 61,62 M€ (61.622.870 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.2` | Investigación y Tecnología Agraria | 35.809.850 | 58,1 % |
| `542.5` | Investigación, Desarrollo | 22.878.510 | 37,1 % |
| `541.1` | Investigación y Normalización | 2.934.510 | 4,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 489,97 M€ (489.973.780 €) · 3 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.6` | Gestión de Centros y Programas | 278.154.940 | 56,8 % |
| `313.7` | Ordenación y Prestaciones de la | 160.035.190 | 32,7 % |
| `313.1` | Servicios Sociales | 51.783.650 | 10,6 % |

</details>

<details open><summary><b><code>salud_mental</code> — 87,27 M€ (87.267.340 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 74.752.040 | 85,7 % |
| `313.2` | Drogodependencias y Otras | 12.515.300 | 14,3 % |

</details>

<details open><summary><b><code>turismo</code> — 96,16 M€ (96.157.970 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 86.421.420 | 89,9 % |
| `761.1` | Ordenación y Promoción Comercial | 9.736.550 | 10,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 6.697,16 M€ · 70 códigos · 39,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - - | 5.003.005.870 |
| `141.1` | Administración de Justicia | 241.235.090 |
| `313.4` | Integración Social de Personas con | 183.281.290 |
| `612.6` | Gastos Diversos - | 173.801.220 |
| `513.1` | Infraestructuras Públicas | 132.835.640 |
| `313.3` | Menor | 98.168.570 |
| `513.3` | Planificación, Transportes y | 95.548.830 |
| `121.6` | Sistemas de Información | 90.903.460 |
| `722.2` | Política Industrial | 71.260.540 |
| `221.1` | Emergencias, Protección Civil, | 67.246.690 |
| `453.4` | Artes Plásticas y Escénicas | 48.879.840 |
| `512.1` | Gestión e Infraestructuras de | 44.041.730 |
| `613.1` | Tributos de la Generalitat | 41.047.200 |
| `511.1` | Dirección y Servicios Generales | 30.606.780 |
| `615.1` | Planificación y Previsión Económica | 28.083.940 |
| `111.1` | Actividad Legislativa | 28.002.810 |
| `442.4` | Medio Natural | 21.553.810 |
| `612.3` | Patrimonio de la Generalitat | 20.661.860 |
| `121.7` | Telecomunicaciones y Sociedad | 16.248.120 |
| `457.1` | Fomento de la Actividad Deportiva | 15.912.820 |
| `323.1` | Promoción de las Familias y las | 15.890.370 |
| `615.2` | Sector Público Empresarial | 15.639.120 |
| `762.1` | Comercio Exterior | 13.963.950 |
| `612.4` | Auditoría y Control Interno | 13.372.920 |
| `313.5` | Integración e Inclusión Social | 11.545.500 |
| … | *resto: 45 códigos* | 174.424.980 |

</details>

### 2016

*Fuente: `tomo_II.html` · 129 líneas · total extraído **17.155,82 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.853,34 M€ (5.853.342.630 €) · 16 códigos · 34,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 4.095.136.730 | 70,0 % |
| `412.23` | Prestaciones Farmacéuticas | 1.003.939.360 | 17,2 % |
| `412.24` | Prestaciones Externas - | 248.000.000 | 4,2 % |
| `412.26` | Personal Sanitario Residente | 115.951.810 | 2,0 % |
| `412.27` | Prestaciones Externas - | 107.800.000 | 1,8 % |
| `412.1` | Centros Integrados de Salud Pública | 56.598.320 | 1,0 % |
| `412.25` | Servicios Generales de la Secretaría | 47.128.990 | 0,8 % |
| `413.1` | Salud | 43.175.120 | 0,7 % |
| `412.29` | Información para la Salud | 38.568.930 | 0,7 % |
| `311.1` | Dirección y Servicios Generales | 33.814.080 | 0,6 % |
| `411.1` | Dirección y Servicios Generales | 21.494.230 | 0,4 % |
| `411.6` | Análisis y Evaluación de la | 15.997.260 | 0,3 % |
| `411.7` | Inspección | 13.093.340 | 0,2 % |
| `411.2` | Administración Económico | 4.758.190 | 0,1 % |
| `411.3` | Administración de Recursos | 3.997.370 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 3.888.900 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 4.183,28 M€ (4.183.282.590 €) · 15 códigos · 24,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.3` | Enseñanza Secundaria | 1.652.174.080 | 39,5 % |
| `422.2` | Enseñanza Primaria | 1.584.353.070 | 37,9 % |
| `422.6` | Universidad y Estudios Superiores | 772.824.110 | 18,5 % |
| `421.3` | Ordenación Educativa | 34.829.500 | 0,8 % |
| `421.4` | Administración Educativa y Cultural | 32.671.080 | 0,8 % |
| `421.1` | Dirección y Servicios Generales | 21.742.650 | 0,5 % |
| `421.9` | Innovación Tecnológica Educativa | 17.281.590 | 0,4 % |
| `422.4` | Formación Profesional y Enseñanzas | 16.223.030 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 14.398.130 | 0,3 % |
| `422.5` | Promoción del valenciano y gestión | 13.091.070 | 0,3 % |
| `421.6` | Formación del Profesorado | 9.945.140 | 0,2 % |
| `421.8` | Administración General de | 7.571.620 | 0,2 % |
| `421.2` | Administración de Personal | 3.707.830 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 2.059.490 | 0,0 % |
| `422.7` | Consejo Escolar de la Comunitat | 410.200 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 187,35 M€ (187.348.640 €) · 7 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714.2` | Ordenación y Mejora de la | 41.928.480 | 22,4 % |
| `714.8` | Agricultura y Ganadería | 32.918.190 | 17,6 % |
| `714.5` | Política Agraria Común y | 32.034.090 | 17,1 % |
| `531.1` | Estructuras Agrarias | 30.746.070 | 16,4 % |
| `711.1` | Dirección y Servicios Generales | 27.258.020 | 14,5 % |
| `714.1` | Ordenación y Mejora de la | 18.602.600 | 9,9 % |
| `714.7` | Desarrollo del Medio Rural | 3.861.190 | 2,1 % |

</details>

<details open><summary><b><code>direccion</code> — 8,15 M€ (8.153.490 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 8.153.490 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 83,39 M€ (83.395.000 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Arquitectura, Vivienda y Proyectos | 79.008.090 | 94,7 % |
| `432.2` | Urbanismo | 4.386.910 | 5,3 % |

</details>

<details open><summary><b><code>empleo</code> — 170,21 M€ (170.205.520 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Servicio Valenciano de Empleo y - - - | 141.496.970 | 83,1 % |
| `315.1` | Condiciones de Trabajo y | 23.541.120 | 13,8 % |
| `322.55` | Promoción de Emprendedores, | 5.167.430 | 3,0 % |

</details>

<details open><summary><b><code>idi</code> — 54,81 M€ (54.806.950 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 28.621.520 | 52,2 % |
| `542.2` | Calidad, Producción Ecológica, | 23.141.670 | 42,2 % |
| `541.1` | Investigación y Normalización | 3.043.760 | 5,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 601,54 M€ (601.536.660 €) · 4 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.6` | Gestión de Centros y Programas | 281.763.350 | 46,8 % |
| `313.7` | Ordenación y Prestaciones de la | 252.008.960 | 41,9 % |
| `313.1` | Servicios Sociales | 66.197.470 | 11,0 % |
| `311.3` | Planificación, Ordenación, | 1.566.880 | 0,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 200,43 M€ (200.433.920 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional | 200.433.920 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 89,62 M€ (89.616.610 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 77.174.530 | 86,1 % |
| `313.2` | Drogodependencias y Otras | 12.442.080 | 13,9 % |

</details>

<details open><summary><b><code>turismo</code> — 112,84 M€ (112.837.740 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 69.975.450 | 62,0 % |
| `761.1` | Ordenación y Promoción Comercial | 42.862.290 | 38,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 18,38 M€ (18.378.450 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 14.945.700 | 81,3 % |
| `313.8` | Igualdad en la Diversidad | 3.432.750 | 18,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 5.592,48 M€ · 71 códigos · 32,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - - | 4.055.240.950 |
| `141.1` | Administración de Justicia | 258.665.600 |
| `513.1` | Infraestructuras Públicas | 127.755.960 |
| `612.6` | Gastos Diversos - | 122.937.910 |
| `313.3` | Menor | 107.068.780 |
| `121.6` | Sistemas de Información | 92.342.580 |
| `221.1` | Emergencias, Protección Civil, | 90.531.030 |
| `513.3` | Planificación, Transportes y | 89.632.890 |
| `722.2` | Política Industrial | 79.991.820 |
| `453.4` | Artes Plásticas y Escénicas | 53.430.600 |
| `613.1` | Tributos de la Generalitat y Juego | 47.383.880 |
| `511.1` | Dirección y Servicios Generales | 29.114.740 |
| `462.7` | Servicio público de Radio - | 29.000.000 |
| `111.1` | Actividad Legislativa | 28.002.840 |
| `442.4` | Medio Natural y Evaluación | 25.538.340 |
| `512.1` | Gestión e Infraestructuras de | 19.273.150 |
| `457.1` | Fomento de la Actividad Deportiva | 16.988.730 |
| `121.7` | Telecomunicaciones y Sociedad | 16.976.220 |
| `313.5` | Inclusión Social | 16.804.060 |
| `442.9` | Prevención Incendios Forestales | 15.811.790 |
| `612.3` | Patrimonio de la Generalitat | 15.094.460 |
| `612.4` | Auditoría y Control Interno | 14.033.910 |
| `762.1` | Comercio Exterior | 13.925.970 |
| `134.1` | Cooperación Internacional al | 13.492.130 |
| `731.1` | Energía | 12.370.450 |
| … | *resto: 46 códigos* | 201.072.510 |

</details>

### 2017

*Fuente: `tomo_II.html` · 128 líneas · total extraído **17.724,97 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 6.034,15 M€ (6.034.154.520 €) · 16 códigos · 34,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 4.048.510.570 | 67,1 % |
| `412.23` | Prestaciones Farmacéuticas | 1.181.186.990 | 19,6 % |
| `412.24` | Prestaciones Externas - | 248.000.000 | 4,1 % |
| `412.27` | Prestaciones Externas - | 129.850.100 | 2,2 % |
| `412.26` | Personal Sanitario Residente | 116.412.000 | 1,9 % |
| `412.25` | Servicios Generales de la Secretaría | 70.047.070 | 1,2 % |
| `412.1` | Centros Integrados de Salud Pública | 52.699.440 | 0,9 % |
| `413.1` | Salud | 46.836.930 | 0,8 % |
| `412.29` | Información para la Salud | 38.440.810 | 0,6 % |
| `311.1` | Dirección y Servicios Generales | 37.709.070 | 0,6 % |
| `411.1` | Dirección y Servicios Generales | 21.330.730 | 0,4 % |
| `411.6` | Análisis y Evaluación de la | 16.807.850 | 0,3 % |
| `411.7` | Inspección | 12.903.700 | 0,2 % |
| `411.2` | Administración Económico | 5.294.740 | 0,1 % |
| `411.3` | Administración de Recursos | 4.303.060 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 3.821.460 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 4.394,33 M€ (4.394.327.370 €) · 15 códigos · 24,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.3` | Enseñanza Secundaria | 1.709.474.050 | 38,9 % |
| `422.2` | Enseñanza Primaria | 1.636.727.070 | 37,2 % |
| `422.6` | Universidad y Estudios Superiores | 868.202.720 | 19,8 % |
| `421.3` | Ordenación Educativa | 36.764.260 | 0,8 % |
| `421.1` | Dirección y Servicios Generales | 24.658.560 | 0,6 % |
| `421.6` | Formación del Profesorado | 21.678.910 | 0,5 % |
| `421.9` | Innovación Tecnológica Educativa | 18.530.370 | 0,4 % |
| `422.4` | Formación Profesional y Enseñanzas | 15.803.240 | 0,4 % |
| `421.4` | Administración Educativa y Cultural | 15.721.950 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 14.917.810 | 0,3 % |
| `422.5` | Promoción del Valenciano y Gestión | 14.463.820 | 0,3 % |
| `421.8` | Administración General de | 10.029.950 | 0,2 % |
| `421.2` | Administración de Personal | 4.875.890 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 2.089.870 | 0,0 % |
| `422.7` | Consejo Escolar de la Comunitat | 388.900 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 198,98 M€ (198.979.340 €) · 6 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711.1` | Dirección y Servicios Generales | 42.176.210 | 21,2 % |
| `714.2` | Ordenación y Mejora de la | 38.640.110 | 19,4 % |
| `714.8` | Agricultura y Ganadería | 36.193.980 | 18,2 % |
| `714.5` | Política Agraria Común y | 31.204.130 | 15,7 % |
| `531.1` | Estructuras Agrarias | 30.137.410 | 15,1 % |
| `714.1` | Ordenación y Mejora de la | 20.627.500 | 10,4 % |

</details>

<details open><summary><b><code>direccion</code> — 8,63 M€ (8.631.790 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 8.631.790 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 98,20 M€ (98.198.450 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Arquitectura, Vivienda y Proyectos | 90.878.060 | 92,5 % |
| `432.2` | Urbanismo | 7.320.390 | 7,5 % |

</details>

<details open><summary><b><code>empleo</code> — 166,17 M€ (166.171.540 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Servicio Valenciano de Empleo y - - - | 134.840.840 | 81,1 % |
| `315.1` | Condiciones de Trabajo y | 24.256.500 | 14,6 % |
| `322.55` | Promoción de Emprendedores, | 7.074.200 | 4,3 % |

</details>

<details open><summary><b><code>idi</code> — 63,99 M€ (63.987.810 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 32.072.980 | 50,1 % |
| `542.2` | Calidad, Producción Ecológica, | 28.757.700 | 44,9 % |
| `541.1` | Investigación y Normalización | 3.157.130 | 4,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 593,98 M€ (593.977.190 €) · 3 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.6` | Gestión de Centros de | 278.720.580 | 46,9 % |
| `313.7` | Ordenación y Prestaciones de la | 247.243.190 | 41,6 % |
| `313.1` | Servicios Sociales | 68.013.420 | 11,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 215,30 M€ (215.297.560 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional | 215.297.560 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 87,82 M€ (87.821.260 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 76.140.670 | 86,7 % |
| `313.2` | Drogodependencias y Otras | 11.680.590 | 13,3 % |

</details>

<details open><summary><b><code>turismo</code> — 118,12 M€ (118.119.260 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 72.628.630 | 61,5 % |
| `761.1` | Ordenación y Promoción Comercial | 45.490.630 | 38,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 20,74 M€ (20.736.830 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 17.699.310 | 85,4 % |
| `313.8` | Igualdad en la Diversidad | 3.037.520 | 14,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 5.724,57 M€ · 72 códigos · 32,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - - | 3.833.264.280 |
| `141.1` | Administración de Justicia | 275.488.700 |
| `612.6` | Gastos Diversos | 226.754.990 |
| `513.1` | Infraestructuras Públicas | 125.615.070 |
| `121.6` | Sistemas de Información | 120.481.500 |
| `313.3` | Infancia y Adolescencia | 119.212.430 |
| `722.2` | Política Industrial | 113.048.050 |
| `513.3` | Planificación, Transportes y | 101.585.580 |
| `221.1` | Emergencias, Protección Civil y | 89.852.830 |
| `313.5` | Inclusión Social | 61.105.210 |
| `453.4` | Artes Plásticas y Escénicas | 57.307.230 |
| `462.7` | Servicio público de Radio - | 55.000.000 |
| `613.3` | IVAT - - - | 45.000.000 |
| `125.1` | Administración Local y | 43.781.350 |
| `442.4` | Medio Natural y Evaluación | 31.519.610 |
| `111.1` | Actividad Legislativa | 28.002.840 |
| `512.1` | Gestión e Infraestructuras de | 27.151.090 |
| `457.1` | Fomento de la Actividad Deportiva | 22.379.560 |
| `454.1` | Promoción Cultural, Patrimonio | 21.695.760 |
| `121.7` | Telecomunicaciones y Sociedad | 19.731.920 |
| `442.9` | Prevención Incendios Forestales | 19.102.270 |
| `134.1` | Cooperación Internacional al | 18.717.300 |
| `612.3` | Patrimonio de la Generalitat | 18.095.120 |
| `511.1` | Dirección y Servicios Generales | 15.834.510 |
| `612.4` | Control Interno y Contabilidad | 14.346.990 |
| … | *resto: 47 códigos* | 220.496.970 |

</details>

### 2018

*Fuente: `tomo_II.html` · 128 líneas · total extraído **19.956,91 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 6.346,30 M€ (6.346.303.200 €) · 16 códigos · 31,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 4.234.191.620 | 66,7 % |
| `412.23` | Prestaciones Farmacéuticas | 1.220.096.750 | 19,2 % |
| `412.24` | Prestaciones Externas - | 281.950.000 | 4,4 % |
| `412.27` | Prestaciones Externas - | 137.350.100 | 2,2 % |
| `412.26` | Personal Sanitario Residente | 119.264.120 | 1,9 % |
| `412.25` | Servicios Generales de la Secretaría | 91.299.540 | 1,4 % |
| `412.1` | Centros de Salud Pública | 54.415.560 | 0,9 % |
| `412.29` | Información para la Salud | 45.567.440 | 0,7 % |
| `413.1` | Salud Pública | 45.291.840 | 0,7 % |
| `311.1` | Dirección y Servicios Generales | 44.973.300 | 0,7 % |
| `411.6` | Análisis y Evaluación de la | 23.320.690 | 0,4 % |
| `411.1` | Dirección y Servicios Generales | 21.019.120 | 0,3 % |
| `411.7` | Inspección | 12.633.810 | 0,2 % |
| `411.2` | Administración Económico | 6.002.920 | 0,1 % |
| `411.3` | Administración de Recursos | 5.041.960 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 3.884.430 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 4.568,05 M€ (4.568.049.700 €) · 15 códigos · 22,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 1.997.574.050 | 43,7 % |
| `422.3` | Enseñanza Secundaria | 1.560.981.780 | 34,2 % |
| `422.6` | Universidad y Estudios Superiores | 804.444.530 | 17,6 % |
| `421.3` | Ordenación Educativa | 48.970.460 | 1,1 % |
| `421.9` | Innovación Tecnológica Educativa | 25.527.320 | 0,6 % |
| `421.1` | Dirección y Servicios Generales | 25.320.970 | 0,6 % |
| `421.6` | Formación del Profesorado | 21.258.720 | 0,5 % |
| `422.4` | Formación Profesional y Enseñanzas | 19.276.930 | 0,4 % |
| `422.5` | Promoción del Valenciano y Gestión | 15.786.050 | 0,3 % |
| `421.5` | Evaluación, Innovación y Calidad | 14.884.070 | 0,3 % |
| `421.4` | Administración Educativa y Cultural | 13.054.990 | 0,3 % |
| `421.8` | Administración General de | 10.814.560 | 0,2 % |
| `421.2` | Administración de Personal | 7.245.210 | 0,2 % |
| `422.8` | Instituto Superior de Enseñanzas | 2.517.500 | 0,1 % |
| `422.7` | Consejo Escolar de la Comunitat | 392.560 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 221,56 M€ (221.557.690 €) · 6 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711.1` | Dirección y Servicios Generales | 43.424.490 | 19,6 % |
| `714.2` | Ordenación y Mejora de la | 43.296.500 | 19,5 % |
| `714.5` | Política Agraria Común y | 42.532.830 | 19,2 % |
| `714.8` | Agricultura y Ganadería | 37.955.390 | 17,1 % |
| `531.1` | Estructuras Agrarias | 31.834.100 | 14,4 % |
| `714.1` | Ordenación y Mejora de la | 22.514.380 | 10,2 % |

</details>

<details open><summary><b><code>direccion</code> — 9,91 M€ (9.906.490 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 9.906.490 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 102,84 M€ (102.836.690 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Arquitectura, Vivienda y Proyectos | 98.064.630 | 95,4 % |
| `432.2` | Urbanismo | 4.772.060 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 174,12 M€ (174.123.530 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Servicio Valenciano de Empleo y - - - | 140.599.320 | 80,7 % |
| `315.1` | Condiciones de Trabajo y | 25.631.830 | 14,7 % |
| `322.55` | Promoción de Emprendedores, | 7.892.380 | 4,5 % |

</details>

<details open><summary><b><code>idi</code> — 77,53 M€ (77.532.390 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 44.537.130 | 57,4 % |
| `542.2` | Calidad, Producción Ecológica, | 29.766.250 | 38,4 % |
| `541.1` | Investigación y Normalización | 3.229.010 | 4,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 624,71 M€ (624.710.410 €) · 3 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.6` | Gestión de Centros de | 288.165.780 | 46,1 % |
| `313.7` | Ordenación y Prestaciones de la | 256.721.810 | 41,1 % |
| `313.1` | Servicios Sociales | 79.822.820 | 12,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 233,46 M€ (233.458.270 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional | 233.458.270 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 89,37 M€ (89.365.100 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 77.273.850 | 86,5 % |
| `313.2` | Drogodependencias y Otras | 12.091.250 | 13,5 % |

</details>

<details open><summary><b><code>turismo</code> — 129,12 M€ (129.119.790 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 83.186.630 | 64,4 % |
| `761.1` | Ordenación y Promoción Comercial | 45.933.160 | 35,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 25,47 M€ (25.469.300 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 21.837.060 | 85,7 % |
| `313.8` | Igualdad en la Diversidad | 3.632.240 | 14,3 % |

</details>

<details><summary><code>(sin concepto)</code> — 7.354,48 M€ · 72 códigos · 36,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - - | 5.157.203.120 |
| `612.6` | Gastos Diversos | 294.189.390 |
| `141.1` | Administración de Justicia | 253.944.840 |
| `313.3` | Infancia y Adolescencia | 145.108.940 |
| `722.2` | Política Industrial | 128.511.410 |
| `513.3` | Planificación, Transportes y | 127.560.630 |
| `513.1` | Infraestructuras Públicas | 126.451.720 |
| `313.5` | Inclusión Social | 120.985.760 |
| `221.3` | Agencia Valenciana de Seguridad y | 108.961.920 |
| `121.6` | Sistemas de Información | 102.639.670 |
| `453.4` | Artes Plásticas y Escénicas | 65.106.890 |
| `462.7` | Servicio público de Radio - - - | 55.000.000 |
| `125.1` | Administración Local y | 52.821.770 |
| `613.3` | IVAT - - - | 49.000.000 |
| `112.7` | Reformas Democráticas y Acceso a | 44.106.330 |
| `442.4` | Medio Natural y Evaluación | 37.298.190 |
| `111.1` | Actividad Legislativa | 28.459.370 |
| `512.1` | Gestión e Infraestructuras de | 26.458.870 |
| `442.9` | Prevención Incendios Forestales | 25.543.520 |
| `457.1` | Fomento de la Actividad Deportiva | 25.135.070 |
| `112` | Agencia Valenciana de la - - - | 24.199.000 |
| `612.3` | Patrimonio de la Generalitat | 23.739.890 |
| `454.1` | Promoción Cultural, Patrimonio | 22.954.310 |
| `134.1` | Cooperación Internacional al | 22.631.840 |
| `615.2` | Modelo Económico y actuaciones | 18.267.390 |
| … | *resto: 47 códigos* | 268.197.160 |

</details>

### 2019

*Fuente: `tomo_II.html` · 131 líneas · total extraído **22.096,21 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 6.603,09 M€ (6.603.088.340 €) · 16 códigos · 29,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 4.416.328.040 | 66,9 % |
| `412.23` | Prestaciones Farmacéuticas | 1.238.112.190 | 18,8 % |
| `412.24` | Prestaciones Externas - | 279.297.000 | 4,2 % |
| `412.27` | Prestaciones Externas - | 138.998.000 | 2,1 % |
| `412.26` | Personal Sanitario Residente | 123.890.770 | 1,9 % |
| `412.25` | Servicios Generales de la Secretaría | 123.853.910 | 1,9 % |
| `311.1` | Dirección y Servicios Generales | 58.699.670 | 0,9 % |
| `412.1` | Centros de Salud Pública | 54.156.440 | 0,8 % |
| `412.29` | Información para la Salud | 51.129.750 | 0,8 % |
| `413.1` | Salud Pública | 46.735.600 | 0,7 % |
| `411.1` | Dirección y Servicios Generales | 21.797.410 | 0,3 % |
| `411.6` | Análisis y Evaluación de la | 20.317.490 | 0,3 % |
| `411.7` | Inspección | 12.840.730 | 0,2 % |
| `411.2` | Administración Económico | 6.508.150 | 0,1 % |
| `411.3` | Administración de Recursos | 6.177.430 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 4.245.760 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 4.946,00 M€ (4.945.999.170 €) · 15 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 2.214.156.690 | 44,8 % |
| `422.3` | Enseñanza Secundaria | 1.689.283.430 | 34,2 % |
| `422.6` | Universidad y Estudios Superiores | 806.644.770 | 16,3 % |
| `421.3` | Ordenación Educativa | 58.525.960 | 1,2 % |
| `421.9` | Innovación Tecnológica Educativa | 32.428.350 | 0,7 % |
| `421.1` | Dirección y Servicios Generales | 27.190.470 | 0,5 % |
| `421.6` | Formación del Profesorado | 25.265.310 | 0,5 % |
| `422.4` | Formación Profesional y Enseñanzas | 23.862.490 | 0,5 % |
| `422.5` | Promoción del Valenciano y Gestión | 17.885.420 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 16.225.740 | 0,3 % |
| `421.4` | Administración Educativa y Cultural | 12.883.130 | 0,3 % |
| `421.8` | Administración General de | 11.102.210 | 0,2 % |
| `421.2` | Administración de Personal | 7.211.250 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 2.928.350 | 0,1 % |
| `422.7` | Consejo Escolar de la Comunitat | 405.600 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 246,73 M€ (246.733.510 €) · 6 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711.1` | Dirección y Servicios Generales | 49.773.020 | 20,2 % |
| `714.5` | Política Agraria Común y | 45.595.930 | 18,5 % |
| `714.2` | Ordenación y Mejora de la | 44.580.620 | 18,1 % |
| `714.8` | Agricultura y Ganadería | 44.555.790 | 18,1 % |
| `531.1` | Estructuras Agrarias | 38.473.630 | 15,6 % |
| `714.1` | Ordenación y Mejora de la | 23.754.520 | 9,6 % |

</details>

<details open><summary><b><code>direccion</code> — 11,38 M€ (11.384.530 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 11.384.530 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 170,32 M€ (170.321.490 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Arquitectura, Vivienda y Proyectos | 165.245.150 | 97,0 % |
| `432.2` | Urbanismo | 5.076.340 | 3,0 % |

</details>

<details open><summary><b><code>empleo</code> — 167,54 M€ (167.540.960 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Servicio Valenciano de Empleo y - - - | 132.448.620 | 79,1 % |
| `315.1` | Condiciones de Trabajo y | 26.047.250 | 15,5 % |
| `322.55` | Promoción de Emprendedores, | 9.045.090 | 5,4 % |

</details>

<details open><summary><b><code>idi</code> — 95,58 M€ (95.580.270 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 58.258.470 | 61,0 % |
| `542.2` | Calidad, Producción Ecológica, | 33.982.390 | 35,6 % |
| `541.1` | Investigación y Normalización | 3.339.410 | 3,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 823,33 M€ (823.333.840 €) · 3 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.7` | Ordenación y Prestaciones de la | 370.770.790 | 45,0 % |
| `313.6` | Gestión de Centros de | 351.825.520 | 42,7 % |
| `313.1` | Servicios Sociales | 100.737.530 | 12,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 279,77 M€ (279.766.500 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional o | 279.766.500 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 91,02 M€ (91.018.350 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 79.688.030 | 87,6 % |
| `313.2` | Drogodependencias y Otras | 11.330.320 | 12,4 % |

</details>

<details open><summary><b><code>turismo</code> — 138,42 M€ (138.422.460 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 100.873.600 | 72,9 % |
| `761.1` | Ordenación y Promoción Comercial | 37.548.860 | 27,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 39,21 M€ (39.206.840 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 32.140.030 | 82,0 % |
| `313.8` | Igualdad en la Diversidad | 7.066.810 | 18,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 8.483,82 M€ · 75 códigos · 38,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - | 5.782.676.610 |
| `612.6` | Gastos Diversos | 452.270.710 |
| `141.1` | Administración de Justicia | 283.358.440 |
| `313.3` | Infancia y Adolescencia | 187.338.050 |
| `722.2` | Política Industrial | 183.115.440 |
| `513.3` | Planificación, Transportes y | 173.291.790 |
| `513.1` | Infraestructuras Públicas | 142.001.510 |
| `313.5` | Inclusión Social | 139.900.490 |
| `121.6` | Sistemas de Información | 122.899.940 |
| `221.3` | Agencia Valenciana de Seguridad y | 119.940.860 |
| `453.4` | Artes Plásticas y Escénicas | 72.840.250 |
| `125.1` | Administración Local y | 66.754.050 |
| `462.7` | Servicio público de Radio - - - | 55.000.000 |
| `112.7` | Reformas Democráticas y Acceso a | 54.708.990 |
| `613.3` | IVAT - - - | 51.578.870 |
| `442.4` | Medio Natural y Evaluación | 46.728.380 |
| `134.1` | Cooperación Internacional al | 32.653.950 |
| `512.1` | Gestión e Infraestructuras de | 31.963.950 |
| `457.1` | Fomento de la Actividad Deportiva | 29.071.100 |
| `111.1` | Actividad Legislativa | 28.643.350 |
| `442.9` | Prevención Incendios Forestales | 27.561.660 |
| `454.1` | Promoción Cultural, Patrimonio | 26.628.870 |
| `112` | Agencia Valenciana de la - - - | 24.699.000 |
| `612.3` | Patrimonio de la Generalitat | 24.199.820 |
| `731.1` | Energía | 21.041.640 |
| … | *resto: 50 códigos* | 302.950.240 |

</details>

### 2020

*Fuente: `tomo_II.html` · 153 líneas · total extraído **23.021,99 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 6.744,50 M€ (6.744.495.420 €) · 19 códigos · 29,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 4.511.841.890 | 66,9 % |
| `412.23` | Prestaciones Farmacéuticas | 1.239.430.450 | 18,4 % |
| `412.24` | Prestaciones Externas - | 286.487.000 | 4,2 % |
| `412.27` | Prestaciones Externas - | 151.500.000 | 2,2 % |
| `412.26` | Personal Sanitario Residente | 133.103.090 | 2,0 % |
| `412.25` | Servicios Generales de la Secretaría | 100.065.620 | 1,5 % |
| `311.1` | Dirección y Servicios Generales | 74.052.230 | 1,1 % |
| `412.1` | Centros de Salud Pública | 60.460.740 | 0,9 % |
| `412.29` | Información para la Salud | 51.019.160 | 0,8 % |
| `413.1` | Salud Pública | 50.394.870 | 0,7 % |
| `411.1` | Dirección y Servicios Generales | 28.141.210 | 0,4 % |
| `411.5` | Investigación en Ciencias de la | 20.847.890 | 0,3 % |
| `411.7` | Inspección | 13.257.520 | 0,2 % |
| `411.2` | Administración Económico | 6.753.700 | 0,1 % |
| `411.3` | Administración de Recursos | 6.305.390 | 0,1 % |
| `411.6` | Planificación y Atención al Paciente | 5.183.820 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 4.304.960 | 0,1 % |
| `311.4` | Instituto Valenciano de Formación, | 1.127.660 | 0,0 % |
| `411.9` | Servicios Generales de la Secretaría | 218.220 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 5.124,74 M€ (5.124.742.490 €) · 18 códigos · 22,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 2.272.401.160 | 44,3 % |
| `422.3` | Enseñanza Secundaria | 1.783.700.660 | 34,8 % |
| `422.6` | Universidad y Estudios Superiores | 825.839.560 | 16,1 % |
| `421.3` | Ordenación Educativa | 48.742.100 | 1,0 % |
| `421.1` | Dirección y Servicios Generales | 26.942.840 | 0,5 % |
| `421.6` | Formación del Profesorado | 25.324.410 | 0,5 % |
| `422.4` | Formación Profesional y Enseñanzas | 22.964.680 | 0,4 % |
| `421.9` | Innovación Tecnológica Educativa | 21.177.210 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 18.976.510 | 0,4 % |
| `422.5` | Promoción del Valenciano y Gestión | 17.987.310 | 0,4 % |
| `442.5` | Calidad y Educación Ambiental | 17.273.370 | 0,3 % |
| `421.4` | Administración Educativa y Cultural | 11.479.260 | 0,2 % |
| `421.7` | Infraestructuras Educativas | 9.751.620 | 0,2 % |
| `421.8` | Administración General de | 8.687.980 | 0,2 % |
| `422.9` | Inclusión Educativa | 5.150.600 | 0,1 % |
| `421.2` | Administración de Personal | 4.889.310 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 3.038.540 | 0,1 % |
| `422.7` | Consejo Escolar de la Comunitat | 415.370 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 254,57 M€ (254.566.260 €) · 6 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711.1` | Dirección y Servicios Generales | 61.941.930 | 24,3 % |
| `714.2` | Ordenación y Mejora de la | 43.363.070 | 17,0 % |
| `714.5` | Política Agraria Común | 43.268.490 | 17,0 % |
| `714.8` | Agricultura y Ganadería | 42.657.710 | 16,8 % |
| `531.1` | Estructuras Agrarias | 38.638.400 | 15,2 % |
| `714.1` | Ordenación y Mejora de la | 24.696.660 | 9,7 % |

</details>

<details open><summary><b><code>direccion</code> — 14,52 M€ (14.519.900 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 14.519.900 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 194,29 M€ (194.288.260 €) · 6 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Vivienda y Regeneración Urbana | 79.585.400 | 41,0 % |
| `431.5` | Calidad y Rehabilitación | 62.308.280 | 32,1 % |
| `431.4` | Emergencia Habitacional y Función | 34.019.260 | 17,5 % |
| `431.3` | Dirección y Servicios Generales | 7.691.150 | 4,0 % |
| `432.2` | Urbanismo | 6.334.440 | 3,3 % |
| `431.6` | Innovación Ecológica en la | 4.349.730 | 2,2 % |

</details>

<details open><summary><b><code>empleo</code> — 169,46 M€ (169.460.990 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Labora Servicio Valenciano de - - - | 134.679.960 | 79,5 % |
| `315.1` | Condiciones de Trabajo y | 25.574.840 | 15,1 % |
| `322.55` | Promoción del Emprendimiento, | 9.206.190 | 5,4 % |

</details>

<details open><summary><b><code>idi</code> — 105,41 M€ (105.405.520 €) · 5 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 60.728.330 | 57,6 % |
| `542.2` | Desarrollo Rural, Calidad, | 33.687.730 | 32,0 % |
| `542.1` | Dirección y Servicios Generales | 5.658.820 | 5,4 % |
| `541.1` | Investigación y Normalización | 3.407.260 | 3,2 % |
| `542.6` | Desarrollo Tecnológico e | 1.923.380 | 1,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.202,12 M€ (1.202.124.410 €) · 5 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `311.2` | Gestión y Organización del Sistema | 403.274.800 | 33,5 % |
| `313.7` | Ordenación y Prestaciones de la | 368.353.950 | 30,6 % |
| `311.3` | Planificación y Coordinación de | 363.987.270 | 30,3 % |
| `313.6` | Gestión de Centros de | 59.736.870 | 5,0 % |
| `313.1` | Servicios Sociales | 6.771.520 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 49,15 M€ (49.148.710 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional o | 49.148.710 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 95,77 M€ (95.767.400 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 83.741.110 | 87,4 % |
| `313.2` | Drogodependencias y Otras | 12.026.290 | 12,6 % |

</details>

<details open><summary><b><code>turismo</code> — 135,99 M€ (135.992.740 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 96.045.470 | 70,6 % |
| `761.1` | Ordenación y Promoción Comercial | 39.947.270 | 29,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 42,82 M€ (42.816.320 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 32.508.890 | 75,9 % |
| `313.8` | Igualdad en la Diversidad | 10.307.430 | 24,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 8.888,66 M€ · 83 códigos · 38,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - | 6.410.996.970 |
| `141.1` | Administración de Justicia | 297.715.290 |
| `612.6` | Gastos Diversos | 245.603.800 |
| `313.5` | Inclusión Social | 193.860.320 |
| `722.2` | Política Industrial | 172.071.580 |
| `513.3` | Planificación, Transportes y | 157.657.090 |
| `513.1` | Infraestructuras Públicas | 152.748.690 |
| `121.6` | Sistemas de Información | 130.422.690 |
| `221.3` | Agencia Valenciana de Seguridad y | 126.501.640 |
| `453.4` | Artes Plásticas y Escénicas | 80.263.510 |
| `125.1` | Administración Local y | 63.850.220 |
| `462.7` | Servicio público de Radio - - - | 56.018.600 |
| `313.3` | Infancia y Adolescencia | 55.547.820 |
| `112.7` | Reformas Democráticas y Acceso a | 55.049.810 |
| `613.3` | Agencia Tributaria Valenciana - - - | 53.437.400 |
| `442.4` | Medio Natural y Evaluación | 50.991.180 |
| `134.1` | Cooperación Internacional al | 33.833.500 |
| `512.1` | Gestión e Infraestructuras de | 32.923.060 |
| `457.1` | Fomento de la Actividad Deportiva | 31.140.350 |
| `111.1` | Actividad Legislativa | 29.337.160 |
| `454.1` | Promoción Cultural, Patrimonio | 28.575.170 |
| `112` | Agencia Valenciana de la - - - | 27.150.000 |
| `442.9` | Prevención Incendios Forestales | 25.641.550 |
| `612.3` | Patrimonio de la Generalitat | 23.055.470 |
| `511.1` | Dirección y Servicios Generales | 22.313.300 |
| … | *resto: 58 códigos* | 331.950.890 |

</details>

### 2021

*Fuente: `tomo_II.html` · 154 líneas · total extraído **25.627,55 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.496,79 M€ (7.496.786.990 €) · 19 códigos · 29,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 5.203.661.540 | 69,4 % |
| `412.23` | Prestaciones Farmacéuticas | 1.251.598.440 | 16,7 % |
| `412.24` | Prestaciones Externas - | 298.359.000 | 4,0 % |
| `412.27` | Prestaciones Externas - | 165.319.900 | 2,2 % |
| `412.26` | Personal Sanitario Residente | 137.989.480 | 1,8 % |
| `412.25` | Servicios Generales de la Secretaría | 97.711.120 | 1,3 % |
| `311.1` | Dirección y Servicios Generales | 73.353.970 | 1,0 % |
| `412.29` | Información para la Salud | 65.466.410 | 0,9 % |
| `412.1` | Centros de Salud Pública | 64.669.310 | 0,9 % |
| `413.1` | Salud Pública | 56.910.230 | 0,8 % |
| `411.1` | Dirección y Servicios Generales | 23.269.660 | 0,3 % |
| `411.5` | Investigación en Ciencias de la | 18.989.220 | 0,3 % |
| `411.7` | Inspección | 13.617.800 | 0,2 % |
| `411.2` | Administración Económico | 7.156.380 | 0,1 % |
| `411.3` | Administración de Recursos | 6.429.030 | 0,1 % |
| `411.6` | Planificación y Atención al Paciente | 5.724.880 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 4.388.610 | 0,1 % |
| `311.4` | Instituto Valenciano de Formación, | 1.949.780 | 0,0 % |
| `411.9` | Servicios Generales de la Secretaría | 222.230 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 5.550,77 M€ (5.550.771.650 €) · 18 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 2.174.494.540 | 39,2 % |
| `422.3` | Enseñanza Secundaria | 1.826.109.280 | 32,9 % |
| `422.6` | Universidad y Estudios Superiores | 884.989.820 | 15,9 % |
| `421.7` | Infraestructuras Educativas | 398.984.330 | 7,2 % |
| `422.4` | Formación Profesional y Enseñanzas | 48.661.550 | 0,9 % |
| `421.3` | Ordenación Educativa | 47.400.220 | 0,9 % |
| `421.1` | Dirección y Servicios Generales | 27.092.500 | 0,5 % |
| `421.5` | Evaluación, Innovación y Calidad | 23.956.970 | 0,4 % |
| `421.9` | Innovación Tecnológica Educativa | 22.407.510 | 0,4 % |
| `421.6` | Formación del Profesorado | 21.950.280 | 0,4 % |
| `442.5` | Calidad y Educación Ambiental | 21.420.110 | 0,4 % |
| `422.5` | Promoción del Valenciano y Gestión | 18.021.620 | 0,3 % |
| `421.4` | Administración Educativa y Cultural | 11.822.790 | 0,2 % |
| `421.8` | Administración General de | 8.946.780 | 0,2 % |
| `422.9` | Inclusión Educativa | 5.513.940 | 0,1 % |
| `421.2` | Administración de Personal | 5.166.400 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 3.409.120 | 0,1 % |
| `422.7` | Consejo Escolar de la Comunitat | 423.890 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 268,26 M€ (268.258.060 €) · 6 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711.1` | Dirección y Servicios Generales | 54.723.040 | 20,4 % |
| `714.8` | Agricultura y Ganadería | 49.531.340 | 18,5 % |
| `714.2` | Ordenación y Mejora de la | 48.416.390 | 18,0 % |
| `714.5` | Política Agraria Común | 46.658.390 | 17,4 % |
| `531.1` | Estructuras Agrarias | 42.474.550 | 15,8 % |
| `714.1` | Ordenación y Mejora de la | 26.454.350 | 9,9 % |

</details>

<details open><summary><b><code>direccion</code> — 11,77 M€ (11.765.140 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 11.765.140 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 216,86 M€ (216.863.020 €) · 7 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Vivienda y Regeneración Urbana | 101.546.640 | 46,8 % |
| `431.5` | Calidad y Rehabilitación | 47.864.600 | 22,1 % |
| `431.4` | Emergencia Habitacional y Función | 41.951.750 | 19,3 % |
| `432.2` | Urbanismo | 9.742.210 | 4,5 % |
| `431.3` | Dirección y Servicios Generales | 8.460.430 | 3,9 % |
| `431.6` | Innovación Ecológica en la | 6.035.630 | 2,8 % |
| `431.7` | Coordinación y Evaluación | 1.261.760 | 0,6 % |

</details>

<details open><summary><b><code>empleo</code> — 259,03 M€ (259.028.730 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Labora Servicio Valenciano de - - - | 215.504.440 | 83,2 % |
| `315.1` | Condiciones de Trabajo y | 28.883.280 | 11,2 % |
| `322.55` | Promoción del Emprendimiento, | 14.641.010 | 5,7 % |

</details>

<details open><summary><b><code>idi</code> — 148,63 M€ (148.627.900 €) · 5 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 99.797.350 | 67,1 % |
| `542.2` | Desarrollo Rural, Calidad, | 33.692.260 | 22,7 % |
| `542.6` | Desarrollo Tecnológico e | 6.831.850 | 4,6 % |
| `542.1` | Dirección y Servicios Generales | 4.837.060 | 3,3 % |
| `541.1` | Investigación y Normalización | 3.469.380 | 2,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.386,46 M€ (1.386.457.890 €) · 4 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `311.2` | Gestión y Organización del Sistema | 470.912.290 | 34,0 % |
| `311.3` | Planificación y Coordinación de | 448.536.630 | 32,4 % |
| `313.7` | Atención primaria y Dependencia | 394.430.690 | 28,4 % |
| `313.6` | Personas Mayores | 72.578.280 | 5,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 51,76 M€ (51.759.770 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional o | 51.759.770 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 108,57 M€ (108.573.050 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 95.202.830 | 87,7 % |
| `313.2` | Drogodependencias y Otras | 13.370.220 | 12,3 % |

</details>

<details open><summary><b><code>turismo</code> — 136,08 M€ (136.079.490 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 94.195.560 | 69,2 % |
| `761.1` | Ordenación y Promoción Comercial | 41.883.930 | 30,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 43,69 M€ (43.690.940 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 31.881.600 | 73,0 % |
| `313.8` | Igualdad en la Diversidad | 11.809.340 | 27,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 9.948,89 M€ · 84 códigos · 38,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - | 6.878.909.820 |
| `612.6` | Gastos Diversos | 416.195.270 |
| `141.1` | Administración de Justicia | 322.784.010 |
| `313.5` | Inclusión Social | 299.014.330 |
| `513.3` | Planificación, Transportes y | 208.867.620 |
| `722.2` | Política Industrial | 192.896.030 |
| `513.1` | Infraestructuras Públicas | 171.273.130 |
| `121.6` | Sistemas de Información | 153.498.910 |
| `221.3` | Agencia Valenciana de Seguridad y | 143.822.300 |
| `453.4` | Artes Plásticas y Escénicas | 87.497.580 |
| `125.1` | Administración Local y | 77.501.270 |
| `442.4` | Medio Natural y Evaluación | 68.904.590 |
| `313.3` | Infancia y Adolescencia | 65.199.260 |
| `112.7` | Reformas Democráticas y Acceso a | 59.490.120 |
| `462.7` | Servicio público de Radio - - - | 58.018.600 |
| `613.3` | Agencia Tributaria Valenciana - - - | 53.437.400 |
| `112` | Agencia Valenciana de la - - - | 50.000.000 |
| `457.1` | Fomento de la Actividad Deportiva | 35.089.600 |
| `134.1` | Cooperación Internacional al | 34.939.760 |
| `512.1` | Gestión e Infraestructuras de | 34.548.620 |
| `612.3` | Patrimonio de la Generalitat | 33.719.300 |
| `454.1` | Promoción Cultural, Patrimonio | 33.080.340 |
| `121.71` | Sociedad Digital | 33.075.310 |
| `111.1` | Actividad Legislativa | 30.107.670 |
| `514.3` | Puertos, Aeropuertos y Costas | 27.862.150 |
| … | *resto: 59 códigos* | 379.155.230 |

</details>

### 2022

*Fuente: `tomo_II.html` · 169 líneas · total extraído **27.967,47 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.801,43 M€ (7.801.429.240 €) · 20 códigos · 27,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 5.433.944.140 | 69,7 % |
| `412.23` | Prestaciones Farmacéuticas | 1.248.349.730 | 16,0 % |
| `412.24` | Prestaciones Externas - | 293.219.000 | 3,8 % |
| `412.27` | Prestaciones Externas - | 166.951.610 | 2,1 % |
| `412.26` | Personal Sanitario Residente | 144.934.140 | 1,9 % |
| `311.1` | Dirección y Servicios Generales | 89.231.410 | 1,1 % |
| `412.25` | Servicios Generales de la Secretaría | 79.962.110 | 1,0 % |
| `413.1` | Salud Pública | 74.451.020 | 1,0 % |
| `412.1` | Centros de Salud Pública | 69.454.340 | 0,9 % |
| `412.29` | Información para la Salud | 65.494.020 | 0,8 % |
| `412.99` | MRR. Asistencia Sanitaria - - - - - - | 37.420.000 | 0,5 % |
| `411.5` | Investigación en Ciencias de la | 28.554.740 | 0,4 % |
| `411.1` | Dirección y Servicios Generales | 26.016.340 | 0,3 % |
| `411.7` | Inspección | 14.318.670 | 0,2 % |
| `411.3` | Administración de Recursos | 7.145.970 | 0,1 % |
| `411.2` | Administración Económico | 7.117.170 | 0,1 % |
| `411.6` | Planificación y Atención al Paciente | 6.370.430 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 4.463.040 | 0,1 % |
| `311.4` | Instituto Valenciano de Formación, | 3.799.340 | 0,0 % |
| `411.9` | Servicios Generales de la Secretaría | 232.020 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 6.132,54 M€ (6.132.544.500 €) · 20 códigos · 21,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 2.306.802.230 | 37,6 % |
| `422.3` | Enseñanza Secundaria | 2.030.461.490 | 33,1 % |
| `422.6` | Universidad y Estudios Superiores | 1.008.576.370 | 16,4 % |
| `421.7` | Infraestructuras Educativas | 388.611.960 | 6,3 % |
| `421.99` | MRR. Transformación Digital de la - - - - - - | 102.360.340 | 1,7 % |
| `422.99` | MRR Educación y Formación | 70.459.100 | 1,1 % |
| `422.4` | Formación Profesional y Enseñanzas | 29.944.640 | 0,5 % |
| `421.1` | Dirección y Servicios Generales | 28.059.620 | 0,5 % |
| `442.5` | Calidad y Educación Ambiental | 24.588.050 | 0,4 % |
| `421.6` | Formación del Profesorado | 24.277.490 | 0,4 % |
| `421.9` | Innovación Tecnológica Educativa | 23.478.780 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 23.047.520 | 0,4 % |
| `422.5` | Promoción del Valenciano y Gestión | 18.939.050 | 0,3 % |
| `421.3` | Ordenación Educativa | 15.307.080 | 0,2 % |
| `421.4` | Administración Educativa y Cultural | 12.735.240 | 0,2 % |
| `421.8` | Administración General de | 9.058.970 | 0,1 % |
| `421.2` | Administración de Personal | 6.122.750 | 0,1 % |
| `422.9` | Inclusión Educativa | 5.800.470 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 3.476.130 | 0,1 % |
| `422.7` | Consejo Escolar de la Comunitat | 437.220 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 273,30 M€ (273.302.910 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714.8` | Agricultura y Ganadería | 60.588.190 | 22,2 % |
| `711.1` | Dirección y Servicios Generales | 54.095.340 | 19,8 % |
| `714.2` | Ordenación y Mejora de la | 50.092.830 | 18,3 % |
| `531.1` | Estructuras Agrarias | 43.712.470 | 16,0 % |
| `714.1` | Ordenación y Mejora de la | 30.835.030 | 11,3 % |
| `714.5` | Política Agraria Común | 28.879.350 | 10,6 % |
| `714.99` | MRR. Agricultura y Desarrollo - - - - - - - | 5.099.700 | 1,9 % |

</details>

<details open><summary><b><code>direccion</code> — 13,34 M€ (13.344.960 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 13.344.960 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 381,26 M€ (381.260.490 €) · 9 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Vivienda y Regeneración Urbana | 118.419.650 | 31,1 % |
| `431.99` | MRR Vivienda y Rehabilitación - - - | 112.861.090 | 29,6 % |
| `431.5` | Calidad y Rehabilitación | 56.866.740 | 14,9 % |
| `431.4` | Emergencia Habitacional y Función | 52.054.990 | 13,7 % |
| `432.2` | Urbanismo | 14.216.360 | 3,7 % |
| `451.99` | MRR Cultura y Deporte - | 9.449.540 | 2,5 % |
| `431.3` | Dirección y Servicios Generales | 8.943.510 | 2,3 % |
| `431.6` | Innovación Ecológica en la | 6.032.500 | 1,6 % |
| `431.7` | Coordinación y Evaluación | 2.416.110 | 0,6 % |

</details>

<details open><summary><b><code>empleo</code> — 266,15 M€ (266.150.430 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Labora Servicio Valenciano de - - - | 207.827.420 | 78,1 % |
| `315.1` | Condiciones de Trabajo y | 31.030.640 | 11,7 % |
| `322.55` | Promoción del Emprendimiento, | 18.342.370 | 6,9 % |
| `322.99` | MRR. Emprendimiento y - - - | 8.950.000 | 3,4 % |

</details>

<details open><summary><b><code>idi</code> — 254,52 M€ (254.517.110 €) · 8 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 98.653.140 | 38,8 % |
| `542.99` | MRR. Transformación Digital, - - - | 47.165.590 | 18,5 % |
| `542.7` | Industrias agroalimentarias, | 40.159.660 | 15,8 % |
| `121.99` | MRR. Transformación e Innovación - - - - - - | 29.710.570 | 11,7 % |
| `542.2` | Desarrollo Rural, Calidad, | 19.179.710 | 7,5 % |
| `542.6` | Desarrollo Tecnológico e | 9.273.760 | 3,6 % |
| `542.1` | Dirección y Servicios Generales | 6.834.090 | 2,7 % |
| `541.1` | Investigación y Normalización | 3.540.590 | 1,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.480,11 M€ (1.480.109.000 €) · 4 códigos · 5,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `311.2` | Gestión y Organización del Sistema | 553.075.920 | 37,4 % |
| `313.7` | Atención primaria y Dependencia | 446.293.450 | 30,2 % |
| `311.3` | Planificación y Coordinación de | 405.027.810 | 27,4 % |
| `313.6` | Personas Mayores | 75.711.820 | 5,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 59,42 M€ (59.417.930 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional o | 59.417.930 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 129,29 M€ (129.289.500 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 115.978.830 | 89,7 % |
| `313.2` | Drogodependencias y Otras | 13.310.670 | 10,3 % |

</details>

<details open><summary><b><code>turismo</code> — 128,29 M€ (128.285.500 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 93.961.340 | 73,2 % |
| `761.1` | Ordenación y Promoción Comercial | 34.324.160 | 26,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 67,67 M€ (67.667.820 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 48.467.880 | 71,6 % |
| `313.8` | Igualdad en la Diversidad | 19.199.940 | 28,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 10.980,15 M€ · 89 códigos · 39,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - | 7.406.216.730 |
| `141.1` | Administración de Justicia | 384.641.060 |
| `612.6` | Gastos Diversos | 308.095.060 |
| `313.5` | Inclusión Social | 277.751.860 |
| `513.3` | Planificación, Transportes y | 237.307.530 |
| `722.2` | Política Industrial | 196.964.400 |
| `121.6` | Sistemas de Información | 179.335.960 |
| `221.3` | Agencia Valenciana de Seguridad y | 168.068.830 |
| `513.1` | Infraestructuras Públicas | 165.563.050 |
| `313.99` | MRR. Mecanismo de Recuperación - | 146.324.640 |
| `513.99` | MRR. Actuaciones mejora de la - - - | 119.640.270 |
| `453.4` | Artes Plásticas y Escénicas | 95.825.660 |
| `442.4` | Medio Natural y Evaluación | 76.797.360 |
| `313.3` | Infancia y Adolescencia | 73.411.450 |
| `442.99` | MRR. Emergencia Climática y - | 71.549.310 |
| `462.7` | Servicio público de Radio - - - | 70.018.600 |
| `125.1` | Administración Local y | 69.680.550 |
| `134.1` | Cooperación Internacional al | 66.901.540 |
| `112.7` | Reformas Democráticas y Acceso a | 66.203.970 |
| `454.1` | Promoción Cultural, Patrimonio | 64.994.070 |
| `112` | Agencia Valenciana de la - - - | 56.400.000 |
| `613.3` | Agencia Tributaria Valenciana - - - | 54.437.400 |
| `612.3` | Patrimonio de la Generalitat | 39.923.410 |
| `457.1` | Fomento de la Actividad Deportiva | 36.017.450 |
| `111.1` | Actividad Legislativa | 30.706.650 |
| … | *resto: 64 códigos* | 517.375.140 |

</details>

### 2023

*Fuente: `tomo_II.html` · 174 líneas · total extraído **28.438,26 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.214,44 M€ (8.214.439.990 €) · 21 códigos · 28,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.22` | Asistencia Sanitaria | 5.738.163.190 | 69,9 % |
| `412.23` | Prestaciones Farmacéuticas | 1.235.240.340 | 15,0 % |
| `412.24` | Prestaciones Externas - | 353.658.160 | 4,3 % |
| `412.26` | Personal Sanitario Residente | 180.868.770 | 2,2 % |
| `412.27` | Prestaciones Externas - | 169.749.970 | 2,1 % |
| `311.1` | Dirección y Servicios Generales | 88.532.680 | 1,1 % |
| `413.1` | Salud Pública | 84.464.500 | 1,0 % |
| `412.25` | Servicios Generales de la Secretaría | 78.628.440 | 1,0 % |
| `412.29` | Información para la Salud | 75.507.510 | 0,9 % |
| `412.1` | Centros de Salud Pública | 70.511.460 | 0,9 % |
| `411.6` | Planificación y Atención al Paciente | 29.538.760 | 0,4 % |
| `411.1` | Dirección y Servicios Generales | 28.794.990 | 0,4 % |
| `412.99` | MRR. Asistencia Sanitaria - - - - - - | 23.129.420 | 0,3 % |
| `411.7` | Inspección | 16.202.440 | 0,2 % |
| `411.5` | Investigación en Ciencias de la | 15.063.810 | 0,2 % |
| `411.3` | Administración de Recursos | 8.012.840 | 0,1 % |
| `411.2` | Administración Económico | 7.872.690 | 0,1 % |
| `411.4` | Escuela Valenciana de Estudios para | 5.293.060 | 0,1 % |
| `311.4` | Instituto Valenciano de Formación, | 4.000.010 | 0,0 % |
| `413.99` | MRR. Salud Pública - | 641.680 | 0,0 % |
| `411.9` | Servicios Generales de la Secretaría | 565.270 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 6.432,87 M€ (6.432.865.520 €) · 20 códigos · 22,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422.2` | Enseñanza Primaria | 2.402.483.380 | 37,3 % |
| `422.3` | Enseñanza Secundaria | 2.219.446.350 | 34,5 % |
| `422.6` | Universidad y Estudios Superiores | 1.035.096.440 | 16,1 % |
| `421.7` | Infraestructuras Educativas | 409.939.830 | 6,4 % |
| `422.99` | MRR Educación y Formación | 70.378.150 | 1,1 % |
| `421.9` | Innovación Tecnológica Educativa | 48.582.960 | 0,8 % |
| `442.5` | Calidad y Educación Ambiental | 46.855.540 | 0,7 % |
| `422.4` | Formación Profesional y Enseñanzas | 39.017.480 | 0,6 % |
| `421.1` | Dirección y Servicios Generales | 28.863.270 | 0,4 % |
| `421.6` | Formación del Profesorado | 25.837.920 | 0,4 % |
| `421.5` | Evaluación, Innovación y Calidad | 25.552.100 | 0,4 % |
| `422.5` | Promoción del Valenciano y Gestión | 19.425.580 | 0,3 % |
| `421.3` | Ordenación Educativa | 16.796.970 | 0,3 % |
| `421.4` | Administración Educativa y Cultural | 14.135.230 | 0,2 % |
| `421.8` | Administración General de | 9.760.720 | 0,2 % |
| `421.2` | Administración de Personal | 7.996.880 | 0,1 % |
| `422.9` | Inclusión Educativa | 5.962.520 | 0,1 % |
| `422.8` | Instituto Superior de Enseñanzas | 4.194.900 | 0,1 % |
| `420.99` | MRR. Otras actuaciones educativas - - - - - - | 2.080.750 | 0,0 % |
| `422.7` | Consejo Escolar de la Comunitat | 458.550 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 282,55 M€ (282.549.210 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714.8` | Agricultura y Ganadería | 59.540.570 | 21,1 % |
| `711.1` | Dirección y Servicios Generales | 58.338.030 | 20,6 % |
| `714.2` | Ordenación y Mejora de la | 51.906.990 | 18,4 % |
| `531.1` | Estructuras Agrarias | 49.446.300 | 17,5 % |
| `714.1` | Ordenación y Mejora de la | 33.273.940 | 11,8 % |
| `714.5` | Política Agraria Común | 26.860.630 | 9,5 % |
| `714.99` | MRR. Agricultura y Desarrollo - - - - - - - | 3.182.750 | 1,1 % |

</details>

<details open><summary><b><code>direccion</code> — 18,49 M€ (18.488.650 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121.2` | Alta Dirección y Servicios | 18.488.650 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 423,12 M€ (423.116.830 €) · 9 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431.1` | Vivienda y Regeneración Urbana | 125.135.840 | 29,6 % |
| `431.99` | MRR Vivienda y Rehabilitación - - - | 113.711.050 | 26,9 % |
| `431.4` | Emergencia Habitacional y Función | 76.998.500 | 18,2 % |
| `431.5` | Calidad y Rehabilitación | 63.364.090 | 15,0 % |
| `432.2` | Urbanismo | 13.959.830 | 3,3 % |
| `431.3` | Dirección y Servicios Generales | 10.227.470 | 2,4 % |
| `431.6` | Innovación Ecológica en la | 8.568.640 | 2,0 % |
| `451.99` | MRR Cultura y Deporte - | 6.834.460 | 1,6 % |
| `431.7` | Coordinación y Evaluación | 4.316.950 | 1,0 % |

</details>

<details open><summary><b><code>empleo</code> — 285,20 M€ (285.203.190 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322.5` | Labora Servicio Valenciano de - - - | 234.366.860 | 82,2 % |
| `315.1` | Condiciones de Trabajo y | 31.689.100 | 11,1 % |
| `322.55` | Promoción del Emprendimiento, | 19.147.230 | 6,7 % |

</details>

<details open><summary><b><code>idi</code> — 274,20 M€ (274.196.730 €) · 8 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542.5` | Investigación, Desarrollo | 103.222.490 | 37,6 % |
| `121.99` | MRR. Transformación e Innovación - - - - - - | 66.010.850 | 24,1 % |
| `542.7` | Industrias agroalimentarias, | 45.505.690 | 16,6 % |
| `542.2` | Desarrollo Rural, Calidad, | 23.205.520 | 8,5 % |
| `542.99` | MRR. Transformación Digital, - - - | 13.900.100 | 5,1 % |
| `542.6` | Desarrollo Tecnológico e | 9.506.370 | 3,5 % |
| `542.1` | Dirección y Servicios Generales | 9.187.060 | 3,4 % |
| `541.1` | Investigación y Normalización | 3.658.650 | 1,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.589,47 M€ (1.589.466.350 €) · 4 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `311.2` | Gestión y Organización del Sistema | 620.566.990 | 39,0 % |
| `313.7` | Atención primaria y Dependencia | 487.828.010 | 30,7 % |
| `311.3` | Planificación y Coordinación de | 405.363.170 | 25,5 % |
| `313.6` | Personas Mayores | 75.708.180 | 4,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 55,10 M€ (55.098.660 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313.4` | Diversidad Funcional o | 55.098.660 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 136,92 M€ (136.918.770 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412.28` | Salud Mental y Atención Sanitaria | 122.153.350 | 89,2 % |
| `313.2` | Drogodependencias y Otras | 14.765.420 | 10,8 % |

</details>

<details open><summary><b><code>turismo</code> — 133,88 M€ (133.881.280 €) · 3 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751.1` | Ordenación y Promoción del | 95.897.210 | 71,6 % |
| `761.1` | Ordenación y Promoción Comercial | 36.272.220 | 27,1 % |
| `751.99` | MRR. Ordenación y Promoción del - - - - - - - | 1.711.850 | 1,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 69,53 M€ (69.531.500 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323.1` | Igualdad de Género | 50.296.010 | 72,3 % |
| `313.8` | Igualdad en la Diversidad | 19.235.490 | 27,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 10.522,50 M€ · 93 códigos · 37,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `11.1` | Servicio de la Deuda - | 6.607.479.250 |
| `141.1` | Administración de Justicia | 421.068.260 |
| `513.3` | Planificación, Transportes y | 331.560.480 |
| `313.5` | Inclusión Social | 331.317.520 |
| `612.6` | Gastos Diversos | 280.058.100 |
| `513.1` | Infraestructuras Públicas | 248.071.680 |
| `722.2` | Política Industrial | 226.893.510 |
| `121.6` | Sistemas de Información | 199.281.280 |
| `221.3` | Seguridad y Emergencias | 184.983.660 |
| `453.4` | Artes Plásticas y Escénicas | 106.911.270 |
| `313.99` | MRR. Mecanismo de Recuperación - | 90.870.560 |
| `442.4` | Medio Natural y Evaluación | 81.250.910 |
| `313.3` | Infancia y Adolescencia | 77.243.670 |
| `112.7` | Reformas Democráticas y Acceso a | 76.716.230 |
| `112` | Agencia Valenciana de la - - - | 75.744.000 |
| `134.1` | Cooperación Internacional al | 71.893.760 |
| `125.1` | Administración Local y | 70.971.670 |
| `462.7` | Servicio público de Radio - - - | 70.918.600 |
| `721.99` | MRR. Economía sostenible, sectores - | 61.116.780 |
| `442.99` | MRR. Emergencia Climática y - | 58.194.520 |
| `613.3` | Agencia Tributaria Valenciana - - - | 55.749.440 |
| `612.3` | Patrimonio de la Generalitat | 50.459.210 |
| `513.99` | MRR. Actuaciones mejora de la - - - - - - - | 42.633.070 |
| `454.1` | Promoción Cultural, Patrimonio | 42.517.260 |
| `442.9` | Prevención Incendios Forestales | 40.339.490 |
| … | *resto: 68 códigos* | 618.259.440 |

</details>

### 2024

*Fuente: `tomo_II.html` · 173 líneas · total extraído **29.732,20 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.432,15 M€ (8.432.147.040 €) · 21 códigos · 28,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B22` | Atención Hospitalaria | 4.246.596.680 | 50,4 % |
| `412B21` | Atención Primaria | 1.700.372.340 | 20,2 % |
| `412B23` | Prestaciones Farmacéuticas | 1.235.322.180 | 14,7 % |
| `412B24` | Prestaciones Externas | 376.208.210 | 4,5 % |
| `412B26` | Personal Sanitario Residente | 204.791.490 | 2,4 % |
| `412B27` | Prestaciones Externas | 169.749.960 | 2,0 % |
| `311A00` | Dirección y Servicios Generales | 86.520.500 | 1,0 % |
| `413A00` | Salud Pública | 85.644.180 | 1,0 % |
| `412B29` | Información para la Salud | 81.864.580 | 1,0 % |
| `412B25` | Servicios Generales de la | 78.141.200 | 0,9 % |
| `412A00` | Centros de Salud Pública | 72.149.260 | 0,9 % |
| `411A00` | Dirección y Servicios Generales | 29.207.470 | 0,3 % |
| `411G00` | Inspección | 16.794.760 | 0,2 % |
| `411E00` | Investigación en Ciencias de la | 15.208.280 | 0,2 % |
| `411C00` | Administración de Recursos | 8.434.460 | 0,1 % |
| `411B00` | Administración Económico | 8.290.570 | 0,1 % |
| `411F00` | Planificación y Atención al | 8.024.900 | 0,1 % |
| `411D00` | Escuela Valenciana de | 5.432.410 | 0,1 % |
| `412M00` | MRR. Asistencia Sanitaria | 2.473.700 | 0,0 % |
| `411H00` | Servicios Generales de la | 630.660 | 0,0 % |
| `413M00` | MRR Salud Pública | 289.250 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 6.600,31 M€ (6.600.309.300 €) · 19 códigos · 22,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A00` | Enseñanza Primaria | 2.561.671.760 | 38,8 % |
| `422B00` | Enseñanza Secundaria | 2.403.314.450 | 36,4 % |
| `422E00` | Universidad y Estudios | 1.035.617.620 | 15,7 % |
| `422I00` | Infraestructuras Educativas | 298.642.650 | 4,5 % |
| `421H00` | Innovación Tecnológica | 47.965.690 | 0,7 % |
| `442B00` | Calidad y Educación Ambiental | 33.585.250 | 0,5 % |
| `422M00` | MRR Educación y Formación | 31.662.440 | 0,5 % |
| `421F00` | Formación del Profesorado | 28.653.010 | 0,4 % |
| `421E00` | Evaluación, Innovación y | 27.363.830 | 0,4 % |
| `421A00` | Dirección y Servicios Generales | 27.169.120 | 0,4 % |
| `422C00` | Formación Profesional | 24.045.440 | 0,4 % |
| `422D00` | Promoción del Valenciano y | 19.531.560 | 0,3 % |
| `421C00` | Ordenación Educativa | 18.177.760 | 0,3 % |
| `421B00` | Administración de Personal | 11.332.590 | 0,2 % |
| `421G00` | Administración General de | 10.128.850 | 0,2 % |
| `421D00` | Administración Educativa | 10.033.790 | 0,2 % |
| `422H00` | Inclusión Educativa | 6.589.960 | 0,1 % |
| `422G00` | Instituto Superior de | 4.354.380 | 0,1 % |
| `422F00` | Consejo Escolar de la | 469.150 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 295,54 M€ (295.541.920 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714D00` | Agricultura y Ganadería | 59.528.060 | 20,1 % |
| `714B00` | Ordenación y Mejora de la | 51.301.760 | 17,4 % |
| `531A00` | Estructuras Agrarias | 50.951.110 | 17,2 % |
| `711A00` | Dirección y Servicios Generales | 50.777.930 | 17,2 % |
| `714A00` | Ordenación y Mejora de la | 29.846.870 | 10,1 % |
| `714F00` | Industria y Cadena | 28.419.210 | 9,6 % |
| `714C00` | Política Agraria Común | 24.716.980 | 8,4 % |

</details>

<details open><summary><b><code>direccion</code> — 19,84 M€ (19.837.670 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B00` | Alta Dirección y Servicios | 19.837.670 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 418,55 M€ (418.548.100 €) · 8 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431M00` | MRR Vivienda y Rehabilitación | 157.418.350 | 37,6 % |
| `431A00` | Vivienda y Regeneración | 80.114.370 | 19,1 % |
| `431D00` | Calidad y Rehabilitación | 73.554.080 | 17,6 % |
| `431C00` | Emergencia Habitacional y | 63.239.100 | 15,1 % |
| `432A00` | Urbanismo | 22.601.090 | 5,4 % |
| `451B00` | Dirección y Servicios Generales | 10.131.410 | 2,4 % |
| `431E00` | Innovación Ecológica en la | 7.779.980 | 1,9 % |
| `431F00` | Coordinación y Evaluación | 3.709.720 | 0,9 % |

</details>

<details open><summary><b><code>empleo</code> — 208,25 M€ (208.245.860 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A00` | Labora Servicio Valenciano de | 158.996.460 | 76,4 % |
| `315A00` | Condiciones de Trabajo y | 31.159.850 | 15,0 % |
| `322D00` | Promoción del Cooperativismo | 11.191.500 | 5,4 % |
| `322B00` | Promoción del Emprendimiento | 6.898.050 | 3,3 % |

</details>

<details open><summary><b><code>idi</code> — 252,83 M€ (252.834.540 €) · 8 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542C00` | Investigación, Desarrollo | 97.232.870 | 38,5 % |
| `542F00` | Agencia Valenciana de la | 63.022.000 | 24,9 % |
| `542E00` | Transferencia de Tecnología | 25.921.760 | 10,3 % |
| `542B00` | Desarrollo Rural, Calidad, | 23.081.100 | 9,1 % |
| `542M00` | MRR. Transformación Digital y | 21.008.860 | 8,3 % |
| `542D00` | Desarrollo Tecnológico e | 12.723.910 | 5,0 % |
| `542M01` | MRR. Ciencia e Investigación | 5.948.130 | 2,4 % |
| `541A00` | Investigación y Normalización | 3.895.910 | 1,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.710,30 M€ (1.710.297.880 €) · 4 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313I00` | Gestión y Organización del | 685.382.120 | 40,1 % |
| `313G00` | Atención primaria y | 537.493.320 | 31,4 % |
| `313J00` | Planificación y Coordinación de | 409.663.670 | 24,0 % |
| `313F00` | Personas Mayores | 77.758.770 | 4,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 52,63 M€ (52.625.140 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D00` | Personas con Discapacidad | 52.625.140 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 158,55 M€ (158.553.590 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B28` | Salud Mental y Atención | 138.460.890 | 87,3 % |
| `313B00` | Drogodependencias y Otras | 20.092.700 | 12,7 % |

</details>

<details open><summary><b><code>diversidad</code> — 17,90 M€ (17.895.490 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313H00` | Diversidad | 17.895.490 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 111,26 M€ (111.260.140 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A00` | Ordenación y Promoción del | 80.178.250 | 72,1 % |
| `761A00` | Ordenación y Promoción | 31.081.890 | 27,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 59,20 M€ (59.199.230 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B00` | Lucha contra la Violencia sobre | 36.656.610 | 61,9 % |
| `323A00` | Igualdad de Género | 22.542.620 | 38,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 11.394,90 M€ · 93 códigos · 38,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A00` | Servicio de la Deuda | 7.948.279.700 |
| `141A00` | Administración de Justicia | 460.232.510 |
| `313E00` | Inclusión Social | 348.389.840 |
| `612F00` | Gastos Diversos | 316.498.340 |
| `513B00` | Planificación, Transportes y | 260.861.850 |
| `722A00` | Política Industrial | 212.094.280 |
| `121F00` | Sistemas de Información | 206.140.190 |
| `221A00` | Seguridad y Emergencias | 176.043.280 |
| `513A00` | Infraestructuras Públicas | 137.302.810 |
| `453A00` | Promoción y Actividad Cultural | 82.635.450 |
| `125A00` | Administración Local y | 82.160.100 |
| `112F00` | Atención a las Víctimas y | 74.480.200 |
| `134A00` | Cooperación Internacional y | 73.642.860 |
| `313C00` | Familia, Infancia y | 73.486.320 |
| `462D00` | Servicio público de Radio | 72.734.040 |
| `442A00` | Medio Natural y Evaluación | 68.169.670 |
| `454A00` | Patrimonio Artístico, Museos y | 57.440.360 |
| `613B00` | Agencia Tributaria Valenciana | 55.749.440 |
| `612C00` | Patrimonio de la Generalitat | 39.821.620 |
| `457A00` | Fomento de la Actividad | 39.714.060 |
| `442F00` | Prevención Incendios | 36.668.760 |
| `111A00` | Actividad Legislativa | 34.105.590 |
| `512A00` | Gestión e Infraestructuras de | 29.191.420 |
| `762A00` | Comercio Exterior | 28.477.840 |
| `514A00` | Puertos, Aeropuertos y Costas | 26.029.510 |
| … | *resto: 68 códigos* | 454.549.410 |

</details>

### 2025

*Fuente: `tomo_II.html` · 174 líneas · total extraído **32.291,43 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.081,45 M€ (9.081.445.440 €) · 22 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B22` | Atención Hospitalaria | 4.398.211.030 | 48,4 % |
| `412B21` | Atención Primaria | 1.746.015.120 | 19,2 % |
| `412B23` | Prestaciones Farmacéuticas | 1.477.406.360 | 16,3 % |
| `412B24` | Prestaciones Externas | 376.208.210 | 4,1 % |
| `412B26` | Personal Sanitario Residente | 215.532.860 | 2,4 % |
| `412B27` | Prestaciones Externas | 170.374.890 | 1,9 % |
| `412B28` | Atención Sanitaria de Media y | 128.686.610 | 1,4 % |
| `412B29` | Información para la Salud | 127.515.600 | 1,4 % |
| `413A00` | Salud Pública | 87.289.900 | 1,0 % |
| `311A00` | Dirección y Servicios Generales | 86.606.280 | 1,0 % |
| `412B25` | Servicios Generales de la | 78.515.450 | 0,9 % |
| `412A00` | Centros de Salud Pública | 77.390.690 | 0,9 % |
| `411A00` | Dirección y Servicios Generales | 28.559.740 | 0,3 % |
| `411G00` | Inspección | 17.916.520 | 0,2 % |
| `411C00` | Administración de Recursos | 16.039.270 | 0,2 % |
| `411E00` | Investigación en Ciencias de la | 14.793.690 | 0,2 % |
| `411B00` | Administración Económico | 10.071.950 | 0,1 % |
| `412M00` | MRR. Asistencia Sanitaria | 9.301.050 | 0,1 % |
| `411F00` | Planificación y Atención al | 6.978.500 | 0,1 % |
| `411D00` | Escuela Valenciana de | 5.742.290 | 0,1 % |
| `411H00` | Servicios Generales de la | 1.860.730 | 0,0 % |
| `413M00` | MRR Salud Pública | 428.700 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 7.230,13 M€ (7.230.131.350 €) · 19 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A00` | Enseñanza Primaria | 2.745.867.090 | 38,0 % |
| `422B00` | Enseñanza Secundaria | 2.510.274.890 | 34,7 % |
| `422E00` | Universidad y Estudios | 1.094.090.270 | 15,1 % |
| `422I00` | Infraestructuras Educativas | 348.544.380 | 4,8 % |
| `442B00` | Calidad y Educación Ambiental | 228.887.660 | 3,2 % |
| `421H00` | Innovación Tecnológica | 73.580.610 | 1,0 % |
| `422C00` | Formación Profesional | 33.997.160 | 0,5 % |
| `421A00` | Dirección y Servicios Generales | 32.583.670 | 0,5 % |
| `421E00` | Evaluación, Innovación y | 29.645.820 | 0,4 % |
| `421F00` | Formación del Profesorado | 29.175.800 | 0,4 % |
| `422M00` | MRR Educación y Formación | 27.175.620 | 0,4 % |
| `421C00` | Ordenación Educativa | 16.978.430 | 0,2 % |
| `422D00` | Promoción del Valenciano y | 16.968.040 | 0,2 % |
| `421D00` | Administración Educativa, | 10.916.030 | 0,2 % |
| `421G00` | Administración General de | 10.632.560 | 0,1 % |
| `421B00` | Administración de Personal | 9.344.720 | 0,1 % |
| `422H00` | Inclusión Educativa | 6.693.210 | 0,1 % |
| `422G00` | Instituto Superior de | 4.260.680 | 0,1 % |
| `422F00` | Consejo Escolar de la | 514.710 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 311,27 M€ (311.269.080 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B00` | Ordenación y Mejora de la | 78.214.500 | 25,1 % |
| `714D00` | Agricultura y Ganadería | 64.457.200 | 20,7 % |
| `531A00` | Estructuras Agrarias | 39.462.800 | 12,7 % |
| `711A00` | Dirección y Servicios Generales | 38.916.720 | 12,5 % |
| `714F00` | Industria y Cadena | 38.634.280 | 12,4 % |
| `714A00` | Ordenación y Mejora de la | 29.061.110 | 9,3 % |
| `714C00` | Política Agraria Común | 22.522.470 | 7,2 % |

</details>

<details open><summary><b><code>direccion</code> — 21,15 M€ (21.145.700 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B00` | Alta Dirección y Servicios | 21.145.700 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 316,43 M€ (316.426.640 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431H00` | Vivienda y calidad e innovación | 197.506.820 | 62,4 % |
| `431I00` | Función social de la vivienda | 106.610.960 | 33,7 % |
| `432A00` | Urbanismo | 12.308.860 | 3,9 % |

</details>

<details open><summary><b><code>empleo</code> — 303,50 M€ (303.502.580 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A00` | Labora Servicio Valenciano de | 228.996.250 | 75,5 % |
| `315A00` | Condiciones de Trabajo y | 50.110.120 | 16,5 % |
| `322B00` | Impulso del Ecosistema | 12.487.480 | 4,1 % |
| `322D00` | Promoción del Cooperativismo | 11.908.730 | 3,9 % |

</details>

<details open><summary><b><code>idi</code> — 226,08 M€ (226.077.070 €) · 8 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542C00` | Investigación, Desarrollo | 99.920.350 | 44,2 % |
| `542F00` | Agencia Valenciana de la | 56.029.450 | 24,8 % |
| `542E00` | Transferencia de Tecnología | 27.388.380 | 12,1 % |
| `542B00` | Desarrollo Rural, Calidad, | 21.338.240 | 9,4 % |
| `542D00` | Desarrollo Tecnológico e | 17.566.340 | 7,8 % |
| `541A00` | Investigación y Normalización | 2.979.080 | 1,3 % |
| `542M00` | MRR. Transformación Digital y | 660.680 | 0,3 % |
| `221E00` | Innovación en Emergencias | 194.550 | 0,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.920,15 M€ (1.920.151.830 €) · 4 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313I00` | Gestión y Organización del | 709.153.540 | 36,9 % |
| `313G00` | Atención primaria y | 660.654.510 | 34,4 % |
| `313J00` | Planificación y Coordinación de | 460.766.160 | 24,0 % |
| `313F00` | Personas Mayores | 89.577.620 | 4,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 58,80 M€ (58.802.180 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D00` | Personas con Discapacidad | 58.802.180 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 192,13 M€ (192.134.990 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B00` | Salud Mental y Adicciones | 192.134.990 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 21,40 M€ (21.400.280 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313H00` | Diversidad | 21.400.280 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 141,76 M€ (141.756.740 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A00` | Ordenación y Promoción del | 91.111.520 | 64,3 % |
| `761A00` | Ordenación y Promoción | 50.645.220 | 35,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 61,55 M€ (61.554.780 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B00` | Lucha contra la Violencia sobre | 40.671.530 | 66,1 % |
| `323A00` | Igualdad de oportunidades | 20.883.250 | 33,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.405,63 M€ · 99 códigos · 38,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A00` | Servicio de la Deuda | 7.139.735.550 |
| `612F00` | Gastos Diversos | 834.079.140 |
| `141A00` | Administración de Justicia | 480.982.660 |
| `221A00` | Seguridad y Protección Civil | 435.332.750 |
| `722A00` | Política Industrial | 366.045.940 |
| `513B00` | Planificación, Transportes y | 358.644.490 |
| `313E00` | Inclusión Social | 356.937.110 |
| `611A00` | Dirección y Servicios Generales | 270.831.760 |
| `513A00` | Infraestructuras Públicas | 241.935.140 |
| `121F00` | Sistemas de Información | 221.594.670 |
| `442F00` | Prevención Incendios | 116.612.110 |
| `442A00` | Medio Natural y Evaluación | 99.896.590 |
| `512A00` | Gestión e Infraestructuras de | 97.056.740 |
| `134A00` | Cooperación Internacional y | 92.731.870 |
| `453A00` | Promoción y Actividad Cultural | 91.801.710 |
| `313C00` | Familia, Infancia y | 86.832.890 |
| `454A00` | Patrimonio Artístico, Museos y | 77.826.240 |
| `112F00` | Atención a las Víctimas y | 76.595.210 |
| `462D00` | Servicio público de Radio | 74.494.040 |
| `125B00` | Lucha contra el | 69.580.600 |
| `613B00` | Agencia Tributaria Valenciana | 54.779.440 |
| `457A00` | Fomento de la Actividad | 44.053.070 |
| `721A00` | Dirección y Servicios Generales | 39.620.760 |
| `762A00` | Internacionalización | 37.607.580 |
| `612C00` | Patrimonio de la Generalitat | 36.578.710 |
| … | *resto: 74 códigos* | 603.447.040 |

</details>

### 2026

*Fuente: `tomo_II.html` · 176 líneas · total extraído **33.305,51 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.293,31 M€ (9.293.305.060 €) · 22 códigos · 27,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B22` | Atención Hospitalaria | 4.521.522.020 | 48,7 % |
| `412B21` | Atención Primaria | 1.796.265.830 | 19,3 % |
| `412B23` | Prestaciones Farmacéuticas | 1.523.029.680 | 16,4 % |
| `412B24` | Prestaciones Externas | 386.208.210 | 4,2 % |
| `412B26` | Personal Sanitario Residente | 223.076.520 | 2,4 % |
| `412B27` | Prestaciones Externas | 170.374.890 | 1,8 % |
| `412B29` | Información para la Salud | 140.636.220 | 1,5 % |
| `412B28` | Atención Sanitaria de Media y | 122.732.620 | 1,3 % |
| `413A00` | Salud Pública | 86.775.690 | 0,9 % |
| `412B25` | Servicios Generales de la | 78.607.200 | 0,8 % |
| `412A00` | Centros de Salud Pública | 74.147.330 | 0,8 % |
| `311A00` | Dirección y Servicios Generales | 58.892.410 | 0,6 % |
| `411A00` | Dirección y Servicios Generales | 28.130.480 | 0,3 % |
| `411G00` | Inspección | 18.445.250 | 0,2 % |
| `411C00` | Administración de Recursos | 15.902.810 | 0,2 % |
| `411E00` | Investigación en Ciencias de la | 14.819.420 | 0,2 % |
| `411B00` | Administración Económico | 10.307.080 | 0,1 % |
| `412M00` | MRR. Asistencia Sanitaria | 8.020.780 | 0,1 % |
| `411F00` | Planificación y Atención al | 7.513.330 | 0,1 % |
| `411D00` | Escuela Valenciana de | 5.825.080 | 0,1 % |
| `411H00` | Servicios Generales de la | 1.932.760 | 0,0 % |
| `413M00` | MRR Salud Pública | 139.450 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 7.572,36 M€ (7.572.363.510 €) · 19 códigos · 22,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A00` | Enseñanza Primaria | 2.900.403.410 | 38,3 % |
| `422B00` | Enseñanza Secundaria | 2.652.733.870 | 35,0 % |
| `422E00` | Universidad y Estudios | 1.231.882.670 | 16,3 % |
| `422I00` | Infraestructuras Educativas | 403.660.800 | 5,3 % |
| `442B00` | Calidad y Educación Ambiental | 113.026.890 | 1,5 % |
| `421H00` | Innovación Tecnológica | 63.888.720 | 0,8 % |
| `421A00` | Dirección y Servicios Generales | 35.953.500 | 0,5 % |
| `422C00` | Formación Profesional | 34.280.560 | 0,5 % |
| `421E00` | Evaluación, Innovación y | 28.595.270 | 0,4 % |
| `421F00` | Formación del Profesorado | 27.085.680 | 0,4 % |
| `421C00` | Ordenación Educativa y | 17.266.750 | 0,2 % |
| `422D00` | Promoción del Valenciano | 16.861.060 | 0,2 % |
| `421D00` | Administración Educativa, | 12.081.330 | 0,2 % |
| `421G00` | Administración General de | 11.229.460 | 0,1 % |
| `421B00` | Administración de Personal | 9.993.130 | 0,1 % |
| `422H00` | Inclusión Educativa | 6.430.230 | 0,1 % |
| `422G00` | Instituto Superior de | 4.272.450 | 0,1 % |
| `422M00` | MRR Educación y Formación | 2.221.490 | 0,0 % |
| `422F00` | Consejo Escolar de la | 496.240 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 304,09 M€ (304.091.320 €) · 7 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B00` | Ordenación y Mejora de la | 89.315.560 | 29,4 % |
| `714D00` | Agricultura y Ganadería | 63.194.850 | 20,8 % |
| `711A00` | Dirección y Servicios Generales | 40.645.230 | 13,4 % |
| `714A00` | Ordenación y Mejora de la | 39.514.520 | 13,0 % |
| `714F00` | Industria y Cadena | 28.879.630 | 9,5 % |
| `714C00` | Política Agraria Común | 22.517.600 | 7,4 % |
| `531A00` | Estructuras Agrarias | 20.023.930 | 6,6 % |

</details>

<details open><summary><b><code>direccion</code> — 23,05 M€ (23.049.820 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B00` | Alta Dirección y Servicios | 23.049.820 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 408,61 M€ (408.610.000 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431H00` | Vivienda y calidad e innovación | 271.422.130 | 66,4 % |
| `431I00` | Función social de la vivienda | 78.349.220 | 19,2 % |
| `431B00` | Dirección y Servicios Generales | 39.901.220 | 9,8 % |
| `432A00` | Urbanismo | 18.937.430 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 215,37 M€ (215.370.650 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A00` | Labora Servicio Valenciano de | 157.012.410 | 72,9 % |
| `315A00` | Condiciones de Trabajo y | 34.831.120 | 16,2 % |
| `322D00` | Promoción del Cooperativismo | 11.996.360 | 5,6 % |
| `322B00` | Impulso del Ecosistema | 11.530.760 | 5,4 % |

</details>

<details open><summary><b><code>idi</code> — 323,62 M€ (323.618.140 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542C00` | Investigación, Desarrollo | 115.303.990 | 35,6 % |
| `542D00` | Desarrollo Tecnológico e | 99.795.280 | 30,8 % |
| `542F00` | Agencia Valenciana de la | 63.199.550 | 19,5 % |
| `542E00` | Transferencia de Tecnología | 23.988.180 | 7,4 % |
| `542B00` | Desarrollo Rural, I+D+i | 13.634.130 | 4,2 % |
| `221E00` | Innovación en Emergencias | 4.553.390 | 1,4 % |
| `541A00` | Investigación y Normalización | 3.143.620 | 1,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.028,21 M€ (2.028.205.580 €) · 4 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313I00` | Gestión y Organización del | 748.466.540 | 36,9 % |
| `313G00` | Atención primaria y | 700.064.320 | 34,5 % |
| `313J00` | Planificación y Coordinación de | 490.172.110 | 24,2 % |
| `313F00` | Personas Mayores | 89.502.610 | 4,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 61,11 M€ (61.112.500 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D00` | Personas con Discapacidad | 61.112.500 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 218,81 M€ (218.813.260 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B00` | Salud Mental y Adicciones | 218.813.260 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 18,63 M€ (18.625.630 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313H00` | Diversidad | 18.625.630 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 150,60 M€ (150.597.210 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A00` | Ordenación y Promoción del | 104.457.500 | 69,4 % |
| `761A00` | Ordenación y Promoción | 46.139.710 | 30,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 67,33 M€ (67.329.440 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B00` | Lucha contra la Violencia sobre | 45.261.630 | 67,2 % |
| `323A00` | Igualdad de oportunidades | 22.067.810 | 32,8 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.620,42 M€ · 101 códigos · 37,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A00` | Servicio de la Deuda | 8.398.589.200 |
| `141A00` | Administración de Justicia | 503.036.990 |
| `313E00` | Inclusión Social | 393.793.540 |
| `612F00` | Gastos Diversos | 304.498.450 |
| `513A00` | Infraestructuras Públicas | 257.562.490 |
| `121F00` | Sistemas de Información | 225.396.780 |
| `722A00` | Política Industrial | 215.194.820 |
| `513B00` | Planificación, Transportes y | 187.599.760 |
| `120B00` | Recuperación y Reconstrucción | 157.952.940 |
| `221G00` | Seguridad Pública | 139.247.790 |
| `512A00` | Gestión e Infraestructuras de | 118.406.760 |
| `313C00` | Familia, Infancia y | 112.939.600 |
| `442A00` | Medio Natural | 108.715.730 |
| `442F00` | Prevención Incendios | 107.150.380 |
| `453A00` | Promoción y Actividad Cultural | 86.129.050 |
| `221A00` | Seguridad y Protección Civil | 85.023.040 |
| `112F00` | Atención a las Víctimas y | 82.178.800 |
| `462D00` | Servicio público de Radio | 75.929.220 |
| `125B00` | Lucha contra el | 73.740.970 |
| `454A00` | Patrimonio Artístico, Museos y | 71.180.690 |
| `134A00` | Cooperación Internacional y | 67.522.860 |
| `613B00` | Agencia Tributaria Valenciana | 58.027.810 |
| `612C00` | Patrimonio de la Generalitat | 51.862.750 |
| `457A00` | Fomento de la Actividad | 44.982.380 |
| `721A00` | Dirección y Servicios Generales | 39.342.080 |
| … | *resto: 76 códigos* | 654.410.720 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py val     # regenera este documento
python3 tools/auditoria_magnitud.py val        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa val --anio <año> \
    --input ../fuentes/raw/val/<año>/<fichero> --output /tmp/val.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-val.md`](limitaciones-val.md)

