# Trazabilidad de la extracción — Región de Murcia (`mur`)

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
| **2015** | 150 | `ley_completa.pdf` | 11 | 49,3 % | 4.907,80 | — | no_aplica |
| **2016** | 145 | `portal_movil.html` | 12 | 51,7 % | 5.138,12 | — | no_aplica |
| **2017** | 149 | `portal_movil.html` | 12 | 51,7 % | 5.319,90 | — | no_aplica |
| **2018** | 147 | `portal_movil.html` | 12 | 51,0 % | 5.771,84 | — | no_aplica |
| **2019** | 149 | `portal_movil.html` | 12 | 51,0 % | 6.056,85 | — | no_aplica |
| **2020** | 154 | `portal_movil.html` | 13 | 50,6 % | 6.464,75 | — | no_aplica |
| **2021** | 154 | `portal_movil.html` | 13 | 50,0 % | 7.054,37 | — | no_aplica |
| **2022** | 154 | `portal_movil.html` | 13 | 50,0 % | 7.267,84 | — | no_aplica |
| **2023** | 155 | `portal_movil.html` | 13 | 49,7 % | 8.157,16 | — | no_aplica |
| **2024** | 160 | `portal_movil.html` | 13 | 48,1 % | 8.237,04 | — | no_aplica |
| **2025** | 149 | `portal_movil.html` | 13 | 51,7 % | 8.460,50 | — | no_aplica |
| **2026** | 149 | `portal_movil.html` | 13 | 51,7 % | 8.460,50 | — | no_aplica |

**URL(s) de origen:**
- <https://www.carm.es/chac/interleg/Ley13-2014_Ptos_CARM%202015_completa.pdf>
- <https://www.carm.es/chac/leypresup2022/movil/index.html>
- <https://www.carm.es/chac/leypresup2023/movil/index.html>
- <https://www.carm.es/chac/leypresup2024/movil/index.html>
- <https://www.carm.es/chac/presupuesto2021/movil/index.html>
- <https://www.carm.es/chac/presupuestos2016/movil/index.html>
- <https://www.carm.es/chac/presupuestos2017/movil/index.html>
- <https://www.carm.es/chac/presupuestos2018/movil/index.html>
- <https://www.carm.es/chac/presupuestos2019/movil/index.html>
- <https://www.carm.es/chac/presupuestos2020/movil/index.html>
- <https://www.carm.es/chac/presupuestos2025/movil/index.html>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 1.859,50 | 1.958,97 | 2.000,86 | 2.124,38 | 2.188,49 | 2.203,43 | 2.487,11 | 2.530,06 | 2.661,16 | 2.847,36 | 2.972,29 | 2.972,29 |
| `educacion` | 1.301,37 | 1.340,62 | 1.360,05 | 1.418,94 | 1.477,74 | 1.580,02 | 1.625,73 | 1.708,89 | 1.831,25 | 2.174,38 | 2.333,24 | 2.333,24 |
| `soberania` | 111,99 | 93,47 | 114,99 | 133,88 | 124,52 | 125,33 | 136,68 | 159,20 | 172,05 | 163,49 | 185,07 | 185,07 |
| `direccion` | — | — | — | — | — | 0,50 | 0,50 | 0,62 | 0,64 | 0,69 | 0,74 | 0,74 |
| `vivienda` | 24,85 | 40,03 | 41,15 | 52,01 | 51,78 | 26,78 | 32,28 | 45,12 | 47,11 | 27,61 | 36,99 | 36,99 |
| `empleo` | 22,07 | 23,32 | 23,06 | 29,60 | 33,80 | 38,00 | 31,06 | 44,17 | 38,26 | 39,72 | 41,25 | 41,25 |
| `idi` | 24,56 | 24,65 | 24,26 | 28,84 | 29,68 | 18,48 | 29,20 | 29,18 | 20,61 | 20,46 | 21,39 | 21,39 |
| `dependencia` | 92,65 | 92,83 | 100,10 | 108,16 | 111,95 | 117,77 | 137,17 | 161,29 | 189,34 | 194,31 | 220,76 | 220,76 |
| `discapacidad` | 132,08 | 144,66 | 150,06 | 157,66 | 161,47 | 187,43 | 195,22 | 199,30 | 227,03 | 253,73 | 261,04 | 261,04 |
| `salud_mental` | 29,27 | 31,12 | 34,69 | 36,74 | 38,74 | 18,31 | 28,30 | 31,21 | 31,29 | 25,11 | 31,26 | 31,26 |
| `diversidad` | — | 6,49 | 7,17 | 15,84 | 14,98 | 5,06 | 4,06 | 4,06 | 6,49 | 7,25 | 6,16 | 6,16 |
| `turismo` | 40,34 | 24,89 | 29,77 | 31,29 | 17,09 | 23,15 | 59,90 | 47,54 | 73,71 | 47,24 | 45,85 | 45,85 |
| `igualdad` | 3,00 | 3,31 | 3,71 | 4,03 | 4,50 | 7,50 | 15,92 | 15,52 | 16,29 | 16,47 | 16,08 | 16,08 |
| **Σ asignado** | 3.641,68 | 3.784,36 | 3.889,88 | 4.141,36 | 4.254,75 | 4.351,75 | 4.783,15 | 4.976,17 | 5.315,21 | 5.817,83 | 6.172,12 | 6.172,12 |
| *(sin concepto)* | 1.266,12 | 1.353,76 | 1.430,02 | 1.630,47 | 1.802,10 | 2.113,00 | 2.271,22 | 2.291,67 | 2.841,95 | 2.419,21 | 2.288,38 | 2.288,38 |
| **TOTAL extraído** | 4.907,80 | 5.138,12 | 5.319,90 | 5.771,84 | 6.056,85 | 6.464,75 | 7.054,37 | 7.267,84 | 8.157,16 | 8.237,04 | 8.460,50 | 8.460,50 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +5,3 % | +2,1 % | +6,2 % | +3,0 % | +0,7 % | +12,9 % | +1,7 % | +5,2 % | +7,0 % | +4,4 % | +0,0 % |
| `educacion` | +3,0 % | +1,4 % | +4,3 % | +4,1 % | +6,9 % | +2,9 % | +5,1 % | +7,2 % | +18,7 % | +7,3 % | +0,0 % |
| `soberania` | −16,5 % | +23,0 % | +16,4 % | −7,0 % | +0,7 % | +9,1 % | +16,5 % | +8,1 % | −5,0 % | +13,2 % | +0,0 % |
| `direccion` | · | · | · | · | **nuevo** ⛔ | +0,9 % | +23,9 % | +3,3 % | +8,1 % | +7,4 % | +0,0 % |
| `vivienda` | +61,1 % ⚠ | +2,8 % | +26,4 % | −0,4 % | −48,3 % ⚠ | +20,5 % | +39,8 % | +4,4 % | −41,4 % ⚠ | +34,0 % | +0,0 % |
| `empleo` | +5,7 % | −1,1 % | +28,3 % | +14,2 % | +12,4 % | −18,3 % | +42,2 % ⚠ | −13,4 % | +3,8 % | +3,8 % | +0,0 % |
| `idi` | +0,3 % | −1,6 % | +18,9 % | +2,9 % | −37,8 % | +58,0 % ⚠ | −0,1 % | −29,4 % | −0,7 % | +4,5 % | +0,0 % |
| `dependencia` | +0,2 % | +7,8 % | +8,0 % | +3,5 % | +5,2 % | +16,5 % | +17,6 % | +17,4 % | +2,6 % | +13,6 % | +0,0 % |
| `discapacidad` | +9,5 % | +3,7 % | +5,1 % | +2,4 % | +16,1 % | +4,2 % | +2,1 % | +13,9 % | +11,8 % | +2,9 % | +0,0 % |
| `salud_mental` | +6,3 % | +11,4 % | +5,9 % | +5,5 % | −52,7 % ⚠ | +54,6 % ⚠ | +10,3 % | +0,2 % | −19,8 % | +24,5 % | +0,0 % |
| `diversidad` | **nuevo** ⛔ | +10,5 % | +120,8 % ⚠ | −5,4 % | −66,3 % ⚠ | −19,6 % | −0,2 % | +60,1 % ⚠ | +11,7 % | −15,1 % | +0,0 % |
| `turismo` | −38,3 % | +19,6 % | +5,1 % | −45,4 % ⚠ | +35,5 % | +158,7 % ⚠ | −20,6 % | +55,0 % ⚠ | −35,9 % | −3,0 % | +0,0 % |
| `igualdad` | +10,3 % | +11,9 % | +8,8 % | +11,5 % | +66,7 % ⚠ | +112,4 % ⚠ | −2,5 % | +4,9 % | +1,1 % | −2,3 % | +0,0 % |
| **TOTAL** | +4,7 % | +3,5 % | +8,5 % | +4,9 % | +6,7 % | +9,1 % | +3,0 % | +12,2 % | +1,0 % | +2,7 % | +0,0 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `vivienda` | **SALTO** | 24,85 → 40,03 M€ (+61,1 % ⚠) |
| 2019 | `turismo` | **SALTO** | 31,29 → 17,09 M€ (−45,4 % ⚠) |
| 2020 | `salud_mental` | **SALTO** | 38,74 → 18,31 M€ (−52,7 % ⚠) |
| 2020 | `vivienda` | **SALTO** | 51,78 → 26,78 M€ (−48,3 % ⚠) |
| 2021 | `turismo` | **SALTO** | 23,15 → 59,90 M€ (+158,7 % ⚠) |
| 2022 | `empleo` | **SALTO** | 31,06 → 44,17 M€ (+42,2 % ⚠) |
| 2023 | `turismo` | **SALTO** | 47,54 → 73,71 M€ (+55,0 % ⚠) |
| 2024 | `vivienda` | **SALTO** | 47,11 → 27,61 M€ (−41,4 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (2 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `442G` | 27,09 | 2015:(sin concepto), 2016:educacion, 2017:educacion, 2018:educacion, 2019:educacion, 2020:educacion, 2021:educacion, 2022:educacion, 2023:educacion, 2024:educacion, 2025:educacion, 2026:educacion |
| `313J` | 15,84 | 2015:(sin concepto), 2016:diversidad, 2017:diversidad, 2018:diversidad, 2019:diversidad, 2020:diversidad, 2021:diversidad, 2022:diversidad, 2023:diversidad, 2024:diversidad, 2025:diversidad, 2026:diversidad |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `ley_completa.pdf` · 150 líneas · total extraído **4.907,80 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.859,50 M€ (1.859.495.700 €) · 16 códigos · 37,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.805.295.761 | 97,1 % |
| `413B` | SALUD | 13.077.932 | 0,7 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 13.039.909 | 0,7 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 7.827.788 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.659.112 | 0,4 % |
| `413G` | INSPECCIÓN Y REGISTRO DE SERVICIOS SANITARIOS | 3.910.763 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.313.571 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.664.691 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.221.604 | 0,1 % |
| `413H` | INVESTIGACION Y FORMACION | 946.790 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 903.661 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 724.146 | 0,0 % |
| `413E` | ORDENACIÓN SANITARIA | 651.599 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 605.346 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 568.220 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 84.807 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.301,37 M€ (1.301.370.707 €) · 21 códigos · 26,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 354.826.741 | 27,3 % |
| `422E` | EDUCACIÓN SECUNDARIA | 337.377.671 | 25,9 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 244.812.249 | 18,8 % |
| `421B` | UNIVERSIDADES | 172.642.222 | 13,3 % |
| `322A` | FOMENTO DEL EMPLEO | 30.254.653 | 2,3 % |
| `422L` | ENSEÑANZAS ARTISTICAS Y DEPORTIVAS | 28.609.070 | 2,2 % |
| `422F` | EDUCACIÓN ESPECIAL | 28.273.723 | 2,2 % |
| `422H` | FORMACIÓN PROFESIONAL | 26.058.530 | 2,0 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 25.393.910 | 2,0 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 14.852.445 | 1,1 % |
| `422Q` | ENSEÑANZAS DE IDIOMAS Y ARTISTICAS SUPERIORES | 11.904.725 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 7.944.669 | 0,6 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 6.754.387 | 0,5 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.503.755 | 0,3 % |
| `422C` | CALIDAD EDUCATIVA | 2.474.879 | 0,2 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 1.971.854 | 0,2 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 1.480.500 | 0,1 % |
| `422M` | ORDENACIÓN ACADÉMICA | 970.142 | 0,1 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 469.473 | 0,0 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 468.800 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 326.309 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 111,99 M€ (111.985.399 €) · 12 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `531A` | REFORMA Y DESARROLLO RURAL | 38.020.847 | 34,0 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 17.321.932 | 15,5 % |
| `712A` | TRANSFERENCIA TECNOLÓGICA Y MODERNIZACIÓN EXPLOTAC | 17.221.306 | 15,4 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 12.978.636 | 11,6 % |
| `712B` | PESCA Y ACUICULTURA | 6.847.954 | 6,1 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 6.732.068 | 6,0 % |
| `711B` | AYUDAS COMUNITARIAS | 3.787.239 | 3,4 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 3.225.590 | 2,9 % |
| `442B` | BIODIVERSIDAD, CAZA Y PESCA FLUVIAL | 2.137.211 | 1,9 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 1.741.122 | 1,6 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.397.995 | 1,2 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 573.499 | 0,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 24,85 M€ (24.852.219 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 21.018.592 | 84,6 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 3.315.866 | 13,3 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 306.458 | 1,2 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 211.303 | 0,9 % |

</details>

<details open><summary><b><code>empleo</code> — 22,07 M€ (22.065.249 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 22.065.249 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 24,56 M€ (24.561.951 €) · 6 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542B` | INVESTIGACIONES AGROALIMENTARIAS | 11.574.373 | 47,1 % |
| `542A` | FORMACION AGRARIA | 5.741.210 | 23,4 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 4.835.249 | 19,7 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 1.474.168 | 6,0 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 669.970 | 2,7 % |
| `542E` | POLÍTICA CIENTÍFICA | 266.981 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 92,65 M€ (92.652.199 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 76.188.729 | 82,2 % |
| `313D` | PROTECCIÓN DEL MENOR | 13.743.192 | 14,8 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 2.720.278 | 2,9 % |

</details>

<details open><summary><b><code>discapacidad</code> — 132,08 M€ (132.081.078 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 72.834.407 | 55,1 % |
| `313F` | PERSONAS CON DISCAPACIDAD | 59.246.671 | 44,9 % |

</details>

<details open><summary><b><code>salud_mental</code> — 29,27 M€ (29.270.886 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PERSONAS CON TRASTORNO MENTAL Y OTROS COLECTIVOS | 15.766.812 | 53,9 % |
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 11.545.113 | 39,4 % |
| `514A` | PUERTOS Y COSTAS | 1.905.380 | 6,5 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 53.581 | 0,2 % |

</details>

<details open><summary><b><code>turismo</code> — 40,34 M€ (40.341.138 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | URBANISMO | 38.987.009 | 96,6 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 986.014 | 2,4 % |
| `313H` | TURISMO SOCIAL | 368.115 | 0,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,00 M€ (3.003.152 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 1.745.112 | 58,1 % |
| `323B` | IGUALDAD | 1.258.040 | 41,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.266,12 M€ · 76 códigos · 25,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 718.872.045 |
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES | 64.441.073 |
| `441A` | SANEAMIENTO Y DEPURACIÓN DE POBLACIONES | 31.900.862 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 30.793.078 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 28.925.632 |
| `442G` | VIGILANCIA E INSPECCIÓN AMBIENTAL | 27.087.767 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 24.951.091 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 19.238.166 |
| `222A` | SEGURIDAD CIUDADANA | 18.854.000 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 17.565.567 |
| `613C` | GESTIÓN Y RECAUDACION TRIBUTARIA | 15.088.278 |
| `512A` | PLANIFICACIÓN DE RECURSOS | 14.793.511 |
| `442F` | PLANIFICAC., AREAS PROTEGIDAS Y DEFENSA M. NATURAL | 14.725.847 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 14.702.865 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 14.067.441 |
| `442E` | INFORMACIÓN,INTEGRACIÓN AMBIENTAL Y ASUNTOS GRALES | 13.050.017 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 12.409.935 |
| `458A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO | 12.174.750 |
| `313Q` | REFORMA JUVENIL | 10.579.726 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 9.827.058 |
| `111A` | ASAMBLEA REGIONAL | 9.413.775 |
| `453A` | MUSEOS | 7.319.619 |
| `513A` | TRANSPORTES | 7.239.802 |
| `121B` | FUNCIÓN PÚBLICA E INSPECCION Y CALIDAD SERVICIOS | 7.054.101 |
| `442D` | GESTIÓN Y PROTECCIÓN FORESTAL | 7.019.159 |
| … | *resto: 51 códigos* | 114.025.569 |

</details>

### 2016

*Fuente: `portal_movil.html` · 145 líneas · total extraído **5.138,12 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.958,97 M€ (1.958.971.130 €) · 17 códigos · 38,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.656.127.053 | 84,5 % |
| `311A` | DIRECCIÓN Y SERVICIOS GENERALES | 243.427.694 | 12,4 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 19.221.793 | 1,0 % |
| `413B` | SALUD | 11.862.567 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 7.981.509 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.227.294 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.971.662 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.191.134 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.649.427 | 0,1 % |
| `413H` | INVESTIGACIÓN Y FORMACIÓN | 1.374.125 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.277.251 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 963.658 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 759.967 | 0,0 % |
| `413E` | ORDENACIÓN SANITARIA | 653.893 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 619.369 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 577.412 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 85.322 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.340,62 M€ (1.340.619.726 €) · 22 códigos · 26,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 362.918.270 | 27,1 % |
| `422E` | EDUCACIÓN SECUNDARIA | 351.966.869 | 26,3 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 251.337.954 | 18,7 % |
| `421B` | UNIVERSIDADES | 181.493.164 | 13,5 % |
| `422H` | FORMACIÓN PROFESIONAL | 37.189.093 | 2,8 % |
| `322A` | FOMENTO DEL EMPLEO | 35.245.694 | 2,6 % |
| `422F` | EDUCACIÓN ESPECIAL | 29.160.572 | 2,2 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 26.801.770 | 2,0 % |
| `422L` | ENSEÑANZAS DE IDIOMAS, ARTISTICAS Y DEPORTIVAS | 19.766.425 | 1,5 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 8.561.992 | 0,6 % |
| `422Q` | ENSEÑANZAS ARTÍSTICAS SUPERIORES | 7.026.897 | 0,5 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 6.771.334 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.519.120 | 0,4 % |
| `442G` | PREVENCIÓN, REDUCCIÓN Y GESTIÓN DE RESIDUOS | 4.773.133 | 0,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.516.276 | 0,3 % |
| `422C` | CALIDAD EDUCATIVA | 2.772.384 | 0,2 % |
| `422P` | EDUCACIÓN DE PERSONAS ADULTAS | 2.099.187 | 0,2 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 1.865.000 | 0,1 % |
| `422M` | ORDENACIÓN ACADÉMICA | 561.028 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 493.292 | 0,0 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 452.360 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 327.912 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 93,47 M€ (93.468.320 €) · 11 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 20.752.468 | 22,2 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 16.314.614 | 17,5 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 12.712.431 | 13,6 % |
| `712E` | PROMOC. Y MEJORA INDUSTRIA, LA COMERCIALIZ. Y CALIDAD | 12.298.589 | 13,2 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 9.519.835 | 10,2 % |
| `712B` | PESCA Y ACUICULTURA | 6.792.659 | 7,3 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 6.493.332 | 6,9 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 3.744.853 | 4,0 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 1.838.874 | 2,0 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 1.624.471 | 1,7 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.376.194 | 1,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 40,03 M€ (40.025.740 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 22.687.982 | 56,7 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 12.632.523 | 31,6 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 3.096.074 | 7,7 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 1.297.691 | 3,2 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 311.470 | 0,8 % |

</details>

<details open><summary><b><code>empleo</code> — 23,32 M€ (23.321.012 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 23.321.012 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 24,65 M€ (24.646.907 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACIÓN Y TRANSFERENCIA TECNOLÓGICA | 14.897.015 | 60,4 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 4.938.592 | 20,0 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 3.265.686 | 13,2 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 1.545.614 | 6,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 92,83 M€ (92.828.035 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 76.164.706 | 82,0 % |
| `313D` | PROTECCIÓN DEL MENOR | 13.841.920 | 14,9 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC. MATERIA DEPENDENCIA | 2.821.409 | 3,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 144,66 M€ (144.664.512 €) · 2 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 81.771.360 | 56,5 % |
| `313F` | PERSONAS CON DISCAPACIDAD | 62.893.152 | 43,5 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,12 M€ (31.122.884 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PERSONAS CON TRASTORNO MENTAL Y OTROS COLECTIVOS | 16.681.546 | 53,6 % |
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 11.855.935 | 38,1 % |
| `514A` | PUERTOS Y COSTAS | 2.531.142 | 8,1 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 54.261 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,49 M€ (6.492.454 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACIÓN COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 6.492.454 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 24,89 M€ (24.890.377 €) · 3 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | URBANISMO | 23.409.545 | 94,1 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.109.154 | 4,5 % |
| `313H` | TURISMO SOCIAL | 371.678 | 1,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,31 M€ (3.312.552 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 2.008.968 | 60,6 % |
| `323B` | IGUALDAD | 1.303.584 | 39,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.353,76 M€ · 70 códigos · 26,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 834.009.043 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 76.499.029 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 44.299.886 |
| `513A` | TRANSPORTES | 34.605.219 |
| `126J` | CENTRO REGIONAL DE INFORMÁTICA | 32.303.646 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 22.250.034 |
| `442D` | GESTIÓN FORESTAL | 20.076.024 |
| `222A` | SEGURIDAD CIUDADANA | 18.854.000 |
| `223B` | CONSORCIO REGIONAL EXTINC. INCENDIOS Y SALVAMENTO | 16.617.865 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLÓGICOS | 16.389.821 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 12.391.315 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 12.258.140 |
| `442E` | INFORMACIÓN Y EVALUACIÓN AMBIENTAL | 11.674.482 |
| `441A` | SANEAMIEN. DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 11.434.398 |
| `313Q` | REFORMA JUVENIL | 10.587.303 |
| `111A` | ASAMBLEA REGIONAL | 10.332.394 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC. Y SOCIEDAD INFORM | 9.538.825 |
| `121B` | FUNCIÓN PÚBLICA E INSPECCIÓN Y CALIDAD SERVICIOS | 9.260.834 |
| `612E` | GESTIÓN DEL PATRIMONIO DE LA COMUNIDAD AUTÓNOMA | 8.737.769 |
| `453A` | MUSEOS | 8.389.413 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 7.747.801 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 7.210.524 |
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES | 6.476.159 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 6.431.004 |
| `724A` | DESARROLLO DE LA ECONOMÍA SOCIAL | 6.196.133 |
| … | *resto: 45 códigos* | 99.186.385 |

</details>

### 2017

*Fuente: `portal_movil.html` · 149 líneas · total extraído **5.319,90 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.000,86 M€ (2.000.860.733 €) · 19 códigos · 37,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.681.259.295 | 84,0 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 258.517.154 | 12,9 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 20.226.634 | 1,0 % |
| `413B` | SALUD | 12.713.407 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 8.043.708 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.210.874 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.587.481 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.440.637 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.714.304 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.282.514 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 1.189.265 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.062.451 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 928.974 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 772.637 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 606.595 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 179.913 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 55.894 | 0,0 % |
| `412P` | NUEVAS ESTRUC Y PGMAS SANIT. GESTIÓN Y EVALUACION | 43.181 | 0,0 % |
| `411E` | AGENCIA PARA LA EXCELENCIA EN LA PRÁCTICA CLÍNICA | 25.815 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.360,05 M€ (1.360.050.701 €) · 22 códigos · 25,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 374.450.361 | 27,5 % |
| `422E` | EDUCACIÓN SECUNDARIA | 363.860.505 | 26,8 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 246.265.720 | 18,1 % |
| `421B` | UNIVERSIDADES | 183.345.979 | 13,5 % |
| `322A` | FOMENTO DEL EMPLEO | 30.592.557 | 2,2 % |
| `422F` | EDUCACIÓN ESPECIAL | 30.463.199 | 2,2 % |
| `422H` | FORMACIÓN PROFESIONAL | 27.992.988 | 2,1 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 27.279.066 | 2,0 % |
| `422L` | ENSEÑANZAS DE IDIOMAS, ARTISTICAS Y DEPORTIVAS | 19.796.633 | 1,5 % |
| `422Q` | ENSEÑANZAS ARTISTICAS SUPERIORES | 9.423.792 | 0,7 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 8.761.194 | 0,6 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 8.475.057 | 0,6 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 7.969.034 | 0,6 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 6.615.117 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.207.108 | 0,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 2.909.714 | 0,2 % |
| `422C` | CALIDAD EDUCATIVA | 2.700.561 | 0,2 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 2.432.720 | 0,2 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 448.253 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 419.319 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 328.970 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 312.854 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 114,99 M€ (114.988.164 €) · 11 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 31.181.183 | 27,1 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 21.009.577 | 18,3 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 14.027.665 | 12,2 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 13.830.889 | 12,0 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 10.612.812 | 9,2 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 10.197.476 | 8,9 % |
| `712B` | PESCA Y ACUICULTURA | 6.344.899 | 5,5 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 3.349.892 | 2,9 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 1.754.065 | 1,5 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 1.646.298 | 1,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.033.408 | 0,9 % |

</details>

<details open><summary><b><code>vivienda</code> — 41,15 M€ (41.154.042 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 20.592.100 | 50,0 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 14.986.148 | 36,4 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 4.839.281 | 11,8 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 418.290 | 1,0 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 318.223 | 0,8 % |

</details>

<details open><summary><b><code>empleo</code> — 23,06 M€ (23.062.691 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 23.062.691 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 24,26 M€ (24.259.845 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 14.761.730 | 60,8 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 5.223.296 | 21,5 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 2.476.058 | 10,2 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 1.798.761 | 7,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 100,10 M€ (100.101.578 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 82.770.305 | 82,7 % |
| `313D` | PROTECCIÓN DEL MENOR | 14.545.545 | 14,5 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 2.785.728 | 2,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 150,06 M€ (150.059.877 €) · 2 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 83.957.569 | 55,9 % |
| `313F` | PERSONAS CON DISCAPACIDAD | 66.102.308 | 44,1 % |

</details>

<details open><summary><b><code>salud_mental</code> — 34,69 M€ (34.685.621 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PERSONAS CON TRASTORNO MENTAL Y OTROS COLECTIVOS | 17.517.407 | 50,5 % |
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 11.974.147 | 34,5 % |
| `514A` | PUERTOS Y COSTAS | 5.146.618 | 14,8 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 47.449 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 7,17 M€ (7.173.529 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 7.173.529 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,77 M€ (29.772.868 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | URBANISMO | 28.571.082 | 96,0 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 800.994 | 2,7 % |
| `313H` | TURISMO SOCIAL | 400.792 | 1,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,71 M€ (3.706.919 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 2.114.395 | 57,0 % |
| `323B` | IGUALDAD | 1.592.524 | 43,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.430,02 M€ · 72 códigos · 26,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 880.221.617 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 76.786.389 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 49.370.312 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 36.915.163 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 29.282.795 |
| `442D` | GESTIÓN FORESTAL | 27.189.443 |
| `513A` | TRANSPORTES | 19.916.124 |
| `222A` | SEGURIDAD CIUDADANA | 18.854.000 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 17.182.599 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 17.037.865 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 16.685.502 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 12.647.426 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 12.362.123 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 12.288.375 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 12.276.675 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 11.068.819 |
| `313Q` | REFORMA JUVENIL | 10.587.133 |
| `111A` | ASAMBLEA REGIONAL | 10.401.257 |
| `612E` | GESTIÓN DEL PATRIMONIO DE LA COMUNIDAD AUTÓNOMA | 9.782.524 |
| `458A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO | 8.432.868 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 8.287.014 |
| `121B` | FUNCIÓN PÚBLICA E INSPECCION Y CALIDAD SERVICIOS | 7.991.936 |
| `453A` | MUSEOS | 7.976.468 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 7.103.000 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 6.792.422 |
| … | *resto: 47 códigos* | 102.579.955 |

</details>

### 2018

*Fuente: `portal_movil.html` · 147 líneas · total extraído **5.771,84 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.124,38 M€ (2.124.384.788 €) · 17 códigos · 36,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.792.002.792 | 84,4 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 271.706.579 | 12,8 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 17.475.648 | 0,8 % |
| `413B` | SALUD | 14.057.308 | 0,7 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 8.533.011 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 5.820.246 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.637.173 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.571.556 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.808.572 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 1.747.169 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.285.252 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.126.568 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.064.657 | 0,1 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 791.687 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 592.756 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 107.665 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 56.149 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.418,94 M€ (1.418.935.986 €) · 21 códigos · 24,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 397.680.991 | 28,0 % |
| `422E` | EDUCACIÓN SECUNDARIA | 368.257.487 | 26,0 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 263.638.256 | 18,6 % |
| `421B` | UNIVERSIDADES | 192.548.235 | 13,6 % |
| `422F` | EDUCACIÓN ESPECIAL | 32.914.246 | 2,3 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 31.433.609 | 2,2 % |
| `322A` | FOMENTO DEL EMPLEO | 30.434.190 | 2,1 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 24.568.835 | 1,7 % |
| `422H` | FORMACIÓN PROFESIONAL | 23.960.918 | 1,7 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 12.952.609 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 9.854.550 | 0,7 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 8.038.603 | 0,6 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 7.099.754 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.270.963 | 0,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.304.740 | 0,2 % |
| `422C` | CALIDAD EDUCATIVA | 2.929.828 | 0,2 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 2.617.721 | 0,2 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 454.782 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 335.060 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 326.338 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 314.271 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 133,88 M€ (133.875.189 €) · 12 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 36.625.257 | 27,4 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 21.285.506 | 15,9 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 18.185.695 | 13,6 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 17.184.954 | 12,8 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 14.020.763 | 10,5 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 10.226.260 | 7,6 % |
| `712B` | PESCA Y ACUICULTURA | 7.288.718 | 5,4 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 3.727.523 | 2,8 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 1.820.450 | 1,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.722.743 | 1,3 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 1.557.320 | 1,2 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 230.000 | 0,2 % |

</details>

<details open><summary><b><code>vivienda</code> — 52,01 M€ (52.012.726 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 23.551.455 | 45,3 % |
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 23.341.846 | 44,9 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 4.403.004 | 8,5 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 419.976 | 0,8 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 296.445 | 0,6 % |

</details>

<details open><summary><b><code>empleo</code> — 29,60 M€ (29.595.660 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 29.595.660 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 28,84 M€ (28.839.541 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 15.354.819 | 53,2 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 9.054.203 | 31,4 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 2.653.747 | 9,2 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 1.776.772 | 6,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 108,16 M€ (108.157.734 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 89.548.100 | 82,8 % |
| `313D` | PROTECCIÓN DEL MENOR | 16.031.632 | 14,8 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 2.578.002 | 2,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 157,66 M€ (157.662.439 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 86.821.185 | 55,1 % |
| `313F` | PERSONAS CON DISCAPACIDAD | 70.841.254 | 44,9 % |

</details>

<details open><summary><b><code>salud_mental</code> — 36,74 M€ (36.739.376 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PERSONAS CON TRASTORNO MENTAL Y OTROS COLECTIVOS | 18.589.456 | 50,6 % |
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 12.882.691 | 35,1 % |
| `514A` | PUERTOS Y COSTAS | 5.219.499 | 14,2 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 47.730 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 15,84 M€ (15.836.157 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 15.836.157 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 31,29 M€ (31.287.502 €) · 3 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | URBANISMO | 30.139.059 | 96,3 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 775.139 | 2,5 % |
| `313H` | TURISMO SOCIAL | 373.304 | 1,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,03 M€ (4.034.881 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 2.444.433 | 60,6 % |
| `323B` | IGUALDAD | 1.590.448 | 39,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.630,47 M€ · 72 códigos · 28,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.052.966.384 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 64.393.686 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 45.404.784 |
| `513A` | TRANSPORTES | 40.766.682 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 34.830.464 |
| `442D` | GESTIÓN FORESTAL | 30.781.681 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 30.618.082 |
| `222A` | SEGURIDAD CIUDADANA | 19.043.000 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 18.357.835 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 15.252.865 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 14.234.928 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 12.423.791 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 12.386.435 |
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES | 12.374.764 |
| `111A` | ASAMBLEA REGIONAL | 12.107.819 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 11.692.976 |
| `121B` | FUNCIÓN PÚBLICA E INSPECCION Y CALIDAD SERVICIOS | 11.462.541 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 11.155.894 |
| `313Q` | REFORMA JUVENIL | 10.916.679 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 10.600.412 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 9.498.109 |
| `458A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO | 9.423.097 |
| `612E` | GESTIÓN DEL PATRIMONIO DE LA COMUNIDAD AUTÓNOMA | 8.117.406 |
| `112B` | COMUNICACIÓN Y ASISTENCIA INFORMATIVA DE LA C.A. | 7.254.540 |
| `442J` | ENERGÍAS LIMPIAS | 6.824.622 |
| … | *resto: 47 códigos* | 117.584.398 |

</details>

### 2019

*Fuente: `portal_movil.html` · 149 líneas · total extraído **6.056,85 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.188,49 M€ (2.188.488.008 €) · 17 códigos · 36,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.847.325.103 | 84,4 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 280.808.980 | 12,8 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 15.566.890 | 0,7 % |
| `413B` | SALUD | 14.124.068 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 9.450.844 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.114.049 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.626.594 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.525.307 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 1.906.764 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.864.394 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.325.440 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.212.982 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.076.772 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 837.401 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 651.951 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 57.476 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 12.993 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.477,74 M€ (1.477.742.295 €) · 21 códigos · 24,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 406.714.801 | 27,5 % |
| `422E` | EDUCACIÓN SECUNDARIA | 392.248.027 | 26,5 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 278.150.297 | 18,8 % |
| `421B` | UNIVERSIDADES | 206.363.564 | 14,0 % |
| `422F` | EDUCACIÓN ESPECIAL | 34.680.625 | 2,3 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 32.210.266 | 2,2 % |
| `322A` | FOMENTO DEL EMPLEO | 27.330.273 | 1,8 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 25.036.851 | 1,7 % |
| `422H` | FORMACIÓN PROFESIONAL | 16.518.567 | 1,1 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 13.455.902 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 11.908.418 | 0,8 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 9.141.781 | 0,6 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 7.236.734 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.153.860 | 0,3 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 3.702.889 | 0,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.465.896 | 0,2 % |
| `422C` | CALIDAD EDUCATIVA | 2.817.331 | 0,2 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 604.777 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 338.868 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 337.446 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 325.122 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 124,52 M€ (124.516.464 €) · 13 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 34.621.283 | 27,8 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 23.733.504 | 19,1 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 11.806.815 | 9,5 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 10.302.900 | 8,3 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 10.075.633 | 8,1 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 9.160.191 | 7,4 % |
| `531C` | CAMINOS RURALES | 8.500.000 | 6,8 % |
| `712B` | PESCA Y ACUICULTURA | 5.572.868 | 4,5 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 4.092.500 | 3,3 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 2.611.120 | 2,1 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 1.939.986 | 1,6 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.846.303 | 1,5 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 253.361 | 0,2 % |

</details>

<details open><summary><b><code>vivienda</code> — 51,78 M€ (51.781.136 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 24.048.960 | 46,4 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.176.833 | 42,8 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 3.947.366 | 7,6 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 1.356.412 | 2,6 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 251.565 | 0,5 % |

</details>

<details open><summary><b><code>empleo</code> — 33,80 M€ (33.799.587 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 33.799.587 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 29,68 M€ (29.682.179 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 15.486.733 | 52,2 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 7.789.344 | 26,2 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 3.333.181 | 11,2 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 3.072.921 | 10,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 111,95 M€ (111.952.655 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 92.479.317 | 82,6 % |
| `313D` | PROTECCIÓN DEL MENOR | 16.883.677 | 15,1 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 2.589.661 | 2,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 161,47 M€ (161.471.097 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 88.638.627 | 54,9 % |
| `313F` | PERSONAS CON DISCAPACIDAD | 72.832.470 | 45,1 % |

</details>

<details open><summary><b><code>salud_mental</code> — 38,74 M€ (38.741.805 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PERSONAS CON TRASTORNO MENTAL Y OTROS COLECTIVOS | 19.855.667 | 51,3 % |
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 13.209.039 | 34,1 % |
| `514A` | PUERTOS Y COSTAS | 5.628.094 | 14,5 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 49.005 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 14,98 M€ (14.983.978 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 14.983.978 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 17,09 M€ (17.089.291 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | URBANISMO | 16.027.372 | 93,8 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 690.301 | 4,0 % |
| `313H` | TURISMO SOCIAL | 371.618 | 2,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,50 M€ (4.498.419 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 2.829.971 | 62,9 % |
| `323B` | IGUALDAD | 1.668.448 | 37,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.802,10 M€ · 73 códigos · 29,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.229.571.967 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 50.024.483 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 41.333.725 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 36.934.865 |
| `513A` | TRANSPORTES | 34.306.547 |
| `442D` | GESTIÓN FORESTAL | 33.899.615 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 28.905.818 |
| `121B` | FUNCIÓN PÚBLICA E INSPECCION Y CALIDAD SERVICIOS | 24.334.982 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 19.483.082 |
| `222A` | SEGURIDAD CIUDADANA | 19.043.000 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 15.531.992 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 15.352.865 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 14.253.208 |
| `111A` | ASAMBLEA REGIONAL | 12.552.679 |
| `313Q` | REFORMA JUVENIL | 11.435.608 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 10.991.658 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 10.965.674 |
| `458A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO | 10.845.886 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 10.010.033 |
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES | 8.936.970 |
| `612E` | GESTIÓN DEL PATRIMONIO DE LA COMUNIDAD AUTÓNOMA | 8.576.714 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 8.296.008 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 7.616.519 |
| `724A` | DESARROLLO DE LA ECONOMÍA SOCIAL | 7.492.766 |
| `112B` | COMUNICACIÓN Y ASISTENCIA INFORMATIVA DE LA C.A. | 7.170.424 |
| … | *resto: 48 códigos* | 124.237.730 |

</details>

### 2020

*Fuente: `portal_movil.html` · 154 líneas · total extraído **6.464,75 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.203,43 M€ (2.203.429.680 €) · 17 códigos · 34,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.846.790.041 | 83,8 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 291.951.274 | 13,2 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 17.319.580 | 0,8 % |
| `413B` | SALUD | 15.246.590 | 0,7 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 10.148.976 | 0,5 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.160.895 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.784.689 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.589.873 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 2.103.807 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 1.991.593 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.395.347 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.313.317 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.058.785 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 863.099 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 671.519 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.852 | 0,0 % |
| `411D` | CALIDAD ASISTENCIAL | 12.443 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.580,02 M€ (1.580.015.261 €) · 22 códigos · 24,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 431.292.325 | 27,3 % |
| `422E` | EDUCACIÓN SECUNDARIA | 402.373.944 | 25,5 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 284.600.835 | 18,0 % |
| `421B` | UNIVERSIDADES | 208.441.872 | 13,2 % |
| `422F` | EDUCACIÓN ESPECIAL | 37.325.761 | 2,4 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 33.233.205 | 2,1 % |
| `322A` | FOMENTO DEL EMPLEO | 30.839.246 | 2,0 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 30.045.916 | 1,9 % |
| `321B` | DIRECCIÓN Y SERVICIOS GENERALES | 28.791.594 | 1,8 % |
| `422H` | FORMACIÓN PROFESIONAL | 15.966.982 | 1,0 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 14.779.175 | 0,9 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 13.647.591 | 0,9 % |
| `422C` | CALIDAD EDUCATIVA | 12.668.745 | 0,8 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 12.346.337 | 0,8 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 7.253.130 | 0,5 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 7.229.551 | 0,5 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 3.979.297 | 0,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.769.157 | 0,2 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 426.482 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 348.193 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 340.812 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 315.111 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 125,33 M€ (125.334.263 €) · 13 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 33.032.112 | 26,4 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 21.241.209 | 16,9 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 12.730.860 | 10,2 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 12.085.685 | 9,6 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 11.974.083 | 9,6 % |
| `531C` | CAMINOS RURALES | 11.500.000 | 9,2 % |
| `712B` | PESCA Y ACUICULTURA | 6.602.964 | 5,3 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 6.390.499 | 5,1 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 4.149.003 | 3,3 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.010.714 | 1,6 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.719.747 | 1,4 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 1.634.026 | 1,3 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 263.361 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 0,50 M€ (496.314 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 496.314 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 26,78 M€ (26.782.024 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 22.597.042 | 84,4 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 3.430.036 | 12,8 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 520.521 | 1,9 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 234.425 | 0,9 % |

</details>

<details open><summary><b><code>empleo</code> — 38,00 M€ (38.000.877 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 38.000.877 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 18,48 M€ (18.475.584 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 6.623.916 | 35,9 % |
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 5.381.086 | 29,1 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 3.956.692 | 21,4 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 2.513.890 | 13,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 117,77 M€ (117.774.419 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 97.250.937 | 82,6 % |
| `313D` | PROTECCIÓN DEL MENOR | 17.953.217 | 15,2 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 2.570.265 | 2,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 187,43 M€ (187.428.003 €) · 2 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 103.529.877 | 55,2 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 83.898.126 | 44,8 % |

</details>

<details open><summary><b><code>salud_mental</code> — 18,31 M€ (18.307.335 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 13.154.405 | 71,9 % |
| `514A` | PUERTOS Y COSTAS | 5.102.527 | 27,9 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 50.403 | 0,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,06 M€ (5.055.006 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 5.055.006 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,15 M€ (23.152.099 €) · 5 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 13.183.158 | 56,9 % |
| `432A` | URBANISMO | 7.643.606 | 33,0 % |
| `751E` | COMPETITIVIDAD Y CALIDAD TURÍSTICAS | 991.503 | 4,3 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 947.908 | 4,1 % |
| `313H` | TURISMO SOCIAL | 385.924 | 1,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,50 M€ (7.498.328 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 5.981.116 | 79,8 % |
| `323B` | IGUALDAD | 1.517.212 | 20,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.113,00 M€ · 76 códigos · 32,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.485.614.050 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 83.575.873 |
| `513A` | TRANSPORTES | 52.960.269 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 37.963.679 |
| `442D` | GESTIÓN FORESTAL | 37.442.834 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 34.984.085 |
| `121B` | FUNCIÓN PÚBLICA | 26.562.987 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 22.704.438 |
| `112A` | DIRECCIÓN Y SERVICIOS GENERALES | 21.892.738 |
| `222A` | SEGURIDAD CIUDADANA | 18.843.000 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 16.848.512 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 15.302.865 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 13.471.362 |
| `111A` | ASAMBLEA REGIONAL | 13.110.198 |
| `313Q` | REFORMA JUVENIL | 11.747.617 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 11.675.092 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 10.992.348 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 10.879.239 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 10.692.158 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 9.367.443 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 8.472.203 |
| `442J` | ENERGÍAS LIMPIAS | 7.923.231 |
| `724A` | DESARROLLO DE LA ECONOMÍA SOCIAL | 7.249.434 |
| `612E` | GESTIÓN DEL PATRIMONIO DE LA COMUNIDAD AUTÓNOMA | 7.105.918 |
| `112B` | COMUNICACIÓN Y ASISTENCIA INFORMATIVA DE LA C.A. | 7.038.618 |
| … | *resto: 51 códigos* | 128.576.307 |

</details>

### 2021

*Fuente: `portal_movil.html` · 154 líneas · total extraído **7.054,37 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.487,11 M€ (2.487.112.377 €) · 16 códigos · 35,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.082.265.102 | 83,7 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 311.638.333 | 12,5 % |
| `413B` | SALUD | 38.823.421 | 1,6 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 17.617.278 | 0,7 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 10.531.545 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.171.023 | 0,2 % |
| `413E` | ORDENACIÓN SANITARIA | 4.471.770 | 0,2 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.882.783 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.764.191 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.231.484 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 2.114.334 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.809.267 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.171.065 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 915.989 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 677.119 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.625,73 M€ (1.625.728.693 €) · 21 códigos · 23,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 458.085.890 | 28,2 % |
| `422E` | EDUCACIÓN SECUNDARIA | 423.975.436 | 26,1 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 298.393.147 | 18,4 % |
| `421B` | UNIVERSIDADES | 213.755.984 | 13,1 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 43.492.761 | 2,7 % |
| `422F` | EDUCACIÓN ESPECIAL | 37.949.445 | 2,3 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 33.258.455 | 2,0 % |
| `322A` | FOMENTO DEL EMPLEO | 31.057.600 | 1,9 % |
| `422H` | FORMACIÓN PROFESIONAL | 16.804.122 | 1,0 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 16.474.066 | 1,0 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 13.837.019 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 12.505.826 | 0,8 % |
| `422C` | CALIDAD EDUCATIVA | 7.527.315 | 0,5 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 7.246.503 | 0,4 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.856.416 | 0,2 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 3.710.666 | 0,2 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 2.376.935 | 0,1 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 427.075 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 356.093 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 345.287 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 292.652 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 136,68 M€ (136.683.389 €) · 14 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 38.011.526 | 27,8 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.940.058 | 16,8 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 13.605.529 | 10,0 % |
| `531C` | CAMINOS RURALES | 9.900.000 | 7,2 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 9.662.950 | 7,1 % |
| `712B` | PESCA Y ACUICULTURA | 9.451.866 | 6,9 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 9.254.142 | 6,8 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 8.781.650 | 6,4 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 5.232.994 | 3,8 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 3.413.361 | 2,5 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 2.772.723 | 2,0 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.022.043 | 1,5 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.384.547 | 1,0 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 250.000 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 0,50 M€ (500.645 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 500.645 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 32,28 M€ (32.283.621 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 21.703.809 | 67,2 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 7.851.196 | 24,3 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 2.492.083 | 7,7 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 236.533 | 0,7 % |

</details>

<details open><summary><b><code>empleo</code> — 31,06 M€ (31.062.217 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 31.062.217 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 29,20 M€ (29.200.123 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 15.909.494 | 54,5 % |
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 5.872.388 | 20,1 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 5.660.500 | 19,4 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 1.757.741 | 6,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 137,17 M€ (137.172.304 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 108.607.934 | 79,2 % |
| `313D` | PROTECCIÓN DEL MENOR | 25.291.740 | 18,4 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 3.272.630 | 2,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 195,22 M€ (195.217.849 €) · 2 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 109.035.673 | 55,9 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 86.182.176 | 44,1 % |

</details>

<details open><summary><b><code>salud_mental</code> — 28,30 M€ (28.298.826 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 18.651.864 | 65,9 % |
| `514A` | PUERTOS Y COSTAS | 9.596.100 | 33,9 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 50.862 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,06 M€ (4.062.951 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 4.062.951 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 59,90 M€ (59.901.204 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 49.353.103 | 82,4 % |
| `432A` | URBANISMO | 5.502.795 | 9,2 % |
| `751E` | COMPETITIVIDAD Y CALIDAD TURÍSTICAS | 2.479.110 | 4,1 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 2.176.219 | 3,6 % |
| `313H` | TURISMO SOCIAL | 389.977 | 0,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 15,92 M€ (15.924.633 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | IGUALDAD | 8.793.966 | 55,2 % |
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 7.130.667 | 44,8 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.271,22 M€ · 77 códigos · 32,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.450.798.353 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 113.776.796 |
| `612F` | PLANIFICACIÓN Y FONDOS EUROPEOS | 105.218.474 |
| `513A` | TRANSPORTES | 44.789.193 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 41.705.750 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 39.053.082 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 36.770.189 |
| `442D` | GESTIÓN FORESTAL | 36.728.969 |
| `121B` | FUNCIÓN PÚBLICA | 25.059.795 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 23.016.967 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 22.889.518 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 22.723.545 |
| `222A` | SEGURIDAD CIUDADANA | 18.842.000 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 15.302.865 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 14.384.073 |
| `111A` | ASAMBLEA REGIONAL | 13.273.814 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 13.089.310 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 13.059.501 |
| `313Q` | REFORMA JUVENIL | 12.123.396 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 11.232.199 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 11.189.542 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 10.993.622 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 10.257.309 |
| `457A` | DEPORTES | 7.590.413 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 7.438.880 |
| … | *resto: 52 códigos* | 149.914.260 |

</details>

### 2022

*Fuente: `portal_movil.html` · 154 líneas · total extraído **7.267,84 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.530,06 M€ (2.530.062.207 €) · 16 códigos · 34,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.121.585.208 | 83,9 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 332.489.994 | 13,1 % |
| `413B` | SALUD | 21.171.601 | 0,8 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 19.651.800 | 0,8 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 10.759.164 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 6.739.829 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.990.681 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 2.812.999 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 2.414.359 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.284.981 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.801.884 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.390.941 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.321.591 | 0,1 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 933.756 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 685.746 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.708,89 M€ (1.708.893.865 €) · 21 códigos · 23,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 458.026.166 | 26,8 % |
| `422E` | EDUCACIÓN SECUNDARIA | 422.440.947 | 24,7 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 321.663.010 | 18,8 % |
| `421B` | UNIVERSIDADES | 222.052.219 | 13,0 % |
| `422F` | EDUCACIÓN ESPECIAL | 39.332.983 | 2,3 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 39.013.267 | 2,3 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 34.042.355 | 2,0 % |
| `322A` | FOMENTO DEL EMPLEO | 33.641.049 | 2,0 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 30.676.288 | 1,8 % |
| `422H` | FORMACIÓN PROFESIONAL | 22.735.050 | 1,3 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 17.700.993 | 1,0 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 14.753.253 | 0,9 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 14.256.348 | 0,8 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 13.061.145 | 0,8 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 8.682.602 | 0,5 % |
| `422C` | CALIDAD EDUCATIVA | 7.096.867 | 0,4 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 4.947.032 | 0,3 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.773.327 | 0,2 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 369.584 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 368.889 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 260.491 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 159,20 M€ (159.202.572 €) · 14 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 43.032.110 | 27,0 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 27.247.366 | 17,1 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 15.748.870 | 9,9 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 14.280.561 | 9,0 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 13.680.344 | 8,6 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 9.691.278 | 6,1 % |
| `531C` | CAMINOS RURALES | 8.400.000 | 5,3 % |
| `712B` | PESCA Y ACUICULTURA | 8.317.795 | 5,2 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 6.336.071 | 4,0 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 4.742.610 | 3,0 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 3.761.667 | 2,4 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.174.340 | 1,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.539.560 | 1,0 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 250.000 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 0,62 M€ (620.519 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 620.519 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 45,12 M€ (45.119.660 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 39.791.440 | 88,2 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 4.801.330 | 10,6 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 292.232 | 0,6 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 234.658 | 0,5 % |

</details>

<details open><summary><b><code>empleo</code> — 44,17 M€ (44.173.619 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 44.173.619 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 29,18 M€ (29.184.468 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 12.555.453 | 43,0 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 9.445.202 | 32,4 % |
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 6.620.837 | 22,7 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 562.976 | 1,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 161,29 M€ (161.289.755 €) · 3 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 125.206.365 | 77,6 % |
| `313D` | PROTECCIÓN DEL MENOR | 32.830.944 | 20,4 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 3.252.446 | 2,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 199,30 M€ (199.299.067 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 121.679.850 | 61,1 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 77.619.217 | 38,9 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,21 M€ (31.208.914 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 23.177.937 | 74,3 % |
| `514A` | PUERTOS Y COSTAS | 7.993.254 | 25,6 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 37.723 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,06 M€ (4.055.849 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACION COLECT. DESFAVORECIDOS Y VOLUNTARIADO | 4.055.849 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,54 M€ (47.540.280 €) · 5 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 41.821.916 | 88,0 % |
| `751E` | COMPETITIVIDAD Y CALIDAD TURÍSTICAS | 2.164.686 | 4,6 % |
| `432A` | URBANISMO | 1.636.887 | 3,4 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.540.322 | 3,2 % |
| `313H` | TURISMO SOCIAL | 376.469 | 0,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 15,52 M€ (15.521.729 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | IGUALDAD | 7.933.969 | 51,1 % |
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 7.587.760 | 48,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.291,67 M€ · 77 códigos · 31,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.580.049.230 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 81.402.364 |
| `612F` | PLANIFICACIÓN Y FONDOS EUROPEOS | 66.320.328 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 42.041.101 |
| `442D` | GESTIÓN FORESTAL | 37.855.221 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 35.294.702 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 29.414.734 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 28.258.004 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 23.320.968 |
| `513A` | TRANSPORTES | 22.003.139 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 21.346.495 |
| `121B` | FUNCIÓN PÚBLICA | 17.130.126 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 16.802.865 |
| `222A` | SEGURIDAD CIUDADANA | 16.422.000 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 15.832.475 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 14.397.354 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 13.893.199 |
| `111A` | ASAMBLEA REGIONAL | 13.662.328 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 12.489.578 |
| `313Q` | REFORMA JUVENIL | 12.345.640 |
| `442J` | ENERGÍAS LIMPIAS | 11.950.555 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 10.993.622 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 10.785.425 |
| `324B` | ACTUACIONES PARA LA CALIDAD PROFESIONAL | 8.950.571 |
| `633A` | FONDO GLOBAL DE RECURSOS PRESUPUESTARIOS | 7.725.355 |
| … | *resto: 52 códigos* | 140.982.345 |

</details>

### 2023

*Fuente: `portal_movil.html` · 155 líneas · total extraído **8.157,16 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.661,16 M€ (2.661.157.290 €) · 16 códigos · 32,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.171.166.070 | 81,6 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 383.953.486 | 14,4 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 48.801.818 | 1,8 % |
| `413B` | SALUD | 17.954.413 | 0,7 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 13.119.768 | 0,5 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 7.511.605 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 4.135.191 | 0,2 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 3.008.950 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 2.787.511 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.212.317 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.866.189 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.504.481 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.466.573 | 0,1 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 957.643 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 683.602 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.831,25 M€ (1.831.251.252 €) · 21 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 489.894.308 | 26,8 % |
| `422E` | EDUCACIÓN SECUNDARIA | 470.450.999 | 25,7 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 354.899.229 | 19,4 % |
| `421B` | UNIVERSIDADES | 245.560.802 | 13,4 % |
| `422F` | EDUCACIÓN ESPECIAL | 49.010.013 | 2,7 % |
| `322A` | FOMENTO DEL EMPLEO | 43.509.624 | 2,4 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 38.815.057 | 2,1 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 38.525.601 | 2,1 % |
| `422H` | FORMACIÓN PROFESIONAL | 31.977.109 | 1,7 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 14.994.824 | 0,8 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 12.978.922 | 0,7 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 10.379.539 | 0,6 % |
| `422C` | CALIDAD EDUCATIVA | 6.792.126 | 0,4 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.976.358 | 0,3 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 5.337.917 | 0,3 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 4.452.724 | 0,2 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 4.140.986 | 0,2 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 2.450.563 | 0,1 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 387.403 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 381.190 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 335.958 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 172,05 M€ (172.046.776 €) · 14 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 42.017.910 | 24,4 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 35.501.020 | 20,6 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 16.243.761 | 9,4 % |
| `712B` | PESCA Y ACUICULTURA | 15.214.810 | 8,8 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 12.759.594 | 7,4 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 12.474.503 | 7,3 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 10.826.170 | 6,3 % |
| `531C` | CAMINOS RURALES | 7.150.000 | 4,2 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 6.021.052 | 3,5 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 5.062.470 | 2,9 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 4.495.845 | 2,6 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.261.593 | 1,3 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 1.768.048 | 1,0 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 250.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,64 M€ (641.026 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 641.026 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 47,11 M€ (47.107.892 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 27.852.853 | 59,1 % |
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 18.700.853 | 39,7 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 312.937 | 0,7 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 241.249 | 0,5 % |

</details>

<details open><summary><b><code>empleo</code> — 38,26 M€ (38.258.107 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 38.258.107 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 20,61 M€ (20.610.121 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 10.727.291 | 52,0 % |
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 7.011.885 | 34,0 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 2.228.145 | 10,8 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 642.800 | 3,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 189,34 M€ (189.336.986 €) · 3 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 146.546.449 | 77,4 % |
| `313D` | PROTECCIÓN DEL MENOR | 39.097.754 | 20,6 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 3.692.783 | 2,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 227,03 M€ (227.025.405 €) · 2 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 138.070.824 | 60,8 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 88.954.581 | 39,2 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,29 M€ (31.286.223 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 25.155.896 | 80,4 % |
| `514A` | PUERTOS Y COSTAS | 6.091.131 | 19,5 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 39.196 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,49 M€ (6.492.289 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACIÓN Y VOLUNTARIADO | 6.492.289 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 73,71 M€ (73.705.868 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 67.375.507 | 91,4 % |
| `751E` | COMPETITIVIDAD Y CALIDAD TURÍSTICAS | 3.651.223 | 5,0 % |
| `432A` | URBANISMO | 1.229.204 | 1,7 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.035.345 | 1,4 % |
| `313H` | TURISMO SOCIAL | 414.589 | 0,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,29 M€ (16.288.187 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | IGUALDAD | 8.188.597 | 50,3 % |
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 8.099.590 | 49,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.841,95 M€ · 78 códigos · 34,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.803.979.997 |
| `721A` | DIRECCIÓN Y SERVICIOS GENERALES | 179.093.211 |
| `633A` | FONDO GLOBAL DE RECURSOS PRESUPUESTARIOS | 112.076.199 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 90.710.702 |
| `513A` | TRANSPORTES | 81.171.575 |
| `442D` | GESTIÓN FORESTAL | 46.374.291 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 36.842.116 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 33.743.997 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 25.626.059 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 25.178.983 |
| `442J` | ENERGÍAS LIMPIAS | 22.726.316 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 22.503.372 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.412.172 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 22.038.618 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 18.489.502 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 18.388.865 |
| `612F` | PROGRAMACIÓN Y GESTIÓN DE FONDOS EUROPEOS | 16.574.670 |
| `222A` | SEGURIDAD CIUDADANA | 16.422.000 |
| `111A` | ASAMBLEA REGIONAL | 14.949.702 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 14.575.510 |
| `313Q` | REFORMA JUVENIL | 14.410.553 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 13.242.344 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 10.994.434 |
| `121B` | FUNCIÓN PÚBLICA | 10.851.527 |
| `457A` | DEPORTES | 10.765.481 |
| … | *resto: 53 códigos* | 157.811.982 |

</details>

### 2024

*Fuente: `portal_movil.html` · 160 líneas · total extraído **8.237,04 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.847,36 M€ (2.847.362.340 €) · 16 códigos · 34,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.338.066.444 | 82,1 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 402.723.213 | 14,1 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 51.009.227 | 1,8 % |
| `413B` | SALUD | 16.871.117 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 12.001.086 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 7.221.655 | 0,3 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 3.949.551 | 0,1 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 3.186.002 | 0,1 % |
| `413H` | INVESTIGACION Y PROYECTOS | 3.063.370 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.252.333 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 1.804.661 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.488.107 | 0,1 % |
| `413E` | ORDENACIÓN SANITARIA | 1.390.288 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 1.324.826 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 982.787 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.174,38 M€ (2.174.381.671 €) · 21 códigos · 26,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 575.982.601 | 26,5 % |
| `422E` | EDUCACIÓN SECUNDARIA | 501.298.891 | 23,1 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 364.862.552 | 16,8 % |
| `421B` | UNIVERSIDADES | 261.969.377 | 12,0 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 154.661.329 | 7,1 % |
| `422F` | EDUCACIÓN ESPECIAL | 61.288.557 | 2,8 % |
| `322A` | FOMENTO DEL EMPLEO | 56.143.134 | 2,6 % |
| `422H` | FORMACIÓN PROFESIONAL | 55.003.307 | 2,5 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 45.827.411 | 2,1 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 42.094.421 | 1,9 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 12.787.396 | 0,6 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 12.340.640 | 0,6 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 11.789.773 | 0,5 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 4.419.510 | 0,2 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 4.321.141 | 0,2 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 3.872.089 | 0,2 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 2.347.430 | 0,1 % |
| `422C` | CALIDAD EDUCATIVA | 2.317.094 | 0,1 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 399.162 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 330.539 | 0,0 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 325.317 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 163,49 M€ (163.492.042 €) · 14 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 38.244.665 | 23,4 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 27.049.865 | 16,5 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 21.188.078 | 13,0 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 18.563.515 | 11,4 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 13.768.684 | 8,4 % |
| `712B` | PESCA Y ACUICULTURA | 9.145.199 | 5,6 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 8.797.600 | 5,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 8.184.859 | 5,0 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 6.381.559 | 3,9 % |
| `531C` | CAMINOS RURALES | 6.150.000 | 3,8 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.439.599 | 1,5 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 1.674.012 | 1,0 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 1.218.782 | 0,7 % |
| `712G` | PRODUCCIÓN AGRÍCOLA | 685.625 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,69 M€ (692.764 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 692.764 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 27,61 M€ (27.609.541 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 15.115.346 | 54,7 % |
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 11.349.393 | 41,1 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 884.784 | 3,2 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 260.018 | 0,9 % |

</details>

<details open><summary><b><code>empleo</code> — 39,72 M€ (39.724.648 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 39.724.648 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 20,46 M€ (20.462.159 €) · 4 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 10.970.993 | 53,6 % |
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 6.851.081 | 33,5 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 2.098.866 | 10,3 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 541.219 | 2,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 194,31 M€ (194.306.355 €) · 3 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 153.826.689 | 79,2 % |
| `313D` | PROTECCIÓN DEL MENOR | 36.604.687 | 18,8 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 3.874.979 | 2,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 253,73 M€ (253.727.169 €) · 2 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 163.144.771 | 64,3 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 90.582.398 | 35,7 % |

</details>

<details open><summary><b><code>salud_mental</code> — 25,11 M€ (25.105.724 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 22.006.375 | 87,7 % |
| `514A` | PUERTOS Y COSTAS | 3.059.146 | 12,2 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 40.203 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 7,25 M€ (7.252.103 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACIÓN Y VOLUNTARIADO | 7.252.103 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,24 M€ (47.243.581 €) · 5 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 37.731.734 | 79,9 % |
| `751E` | COMPETITIVIDAD Y CALIDAD TURÍSTICAS | 5.943.070 | 12,6 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.957.861 | 4,1 % |
| `432A` | URBANISMO | 1.194.220 | 2,5 % |
| `313H` | TURISMO SOCIAL | 416.696 | 0,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,47 M€ (16.465.371 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 8.246.780 | 50,1 % |
| `323B` | IGUALDAD | 8.218.591 | 49,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.419,21 M€ · 83 códigos · 29,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.376.496.986 |
| `513A` | TRANSPORTES | 127.762.134 |
| `633A` | FONDO GLOBAL DE RECURSOS PRESUPUESTARIOS | 112.076.199 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 98.004.298 |
| `121B` | FUNCIÓN PÚBLICA | 72.425.087 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 64.071.388 |
| `442D` | GESTIÓN FORESTAL | 47.197.342 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 37.063.084 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 36.152.242 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 27.579.310 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 22.488.722 |
| `222A` | SEGURIDAD CIUDADANA | 21.862.100 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 21.702.538 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 21.345.994 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 20.818.099 |
| `612F` | PROGRAMACIÓN Y GESTIÓN DE FONDOS EUROPEOS | 20.437.361 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 17.538.383 |
| `111A` | ASAMBLEA REGIONAL | 15.515.295 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 15.208.905 |
| `442J` | ENERGÍAS LIMPIAS | 15.101.364 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 14.636.060 |
| `313Q` | REFORMA JUVENIL | 14.371.890 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 11.246.174 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 11.099.077 |
| `313M` | FAMILIA | 10.581.368 |
| … | *resto: 58 códigos* | 166.431.903 |

</details>

### 2025

*Fuente: `portal_movil.html` · 149 líneas · total extraído **8.460,50 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.972,29 M€ (2.972.286.524 €) · 17 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.430.451.413 | 81,8 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 438.388.587 | 14,7 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 43.037.841 | 1,4 % |
| `413B` | SALUD | 17.803.380 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 13.241.652 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 7.359.120 | 0,2 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 4.466.709 | 0,2 % |
| `413H` | INVESTIGACION Y PROYECTOS | 3.444.450 | 0,1 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 3.120.484 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.812.487 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 2.502.523 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.481.349 | 0,0 % |
| `413E` | ORDENACIÓN SANITARIA | 1.437.125 | 0,0 % |
| `413I` | INSPECCIÓN CENTROS Y ESTABLECIMIENTOS SANITARIOS | 1.136.633 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 1.067.754 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 507.344 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.333,24 M€ (2.333.238.090 €) · 22 códigos · 27,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 606.495.443 | 26,0 % |
| `422E` | EDUCACIÓN SECUNDARIA | 552.366.050 | 23,7 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 374.990.243 | 16,1 % |
| `421B` | UNIVERSIDADES | 271.097.680 | 11,6 % |
| `321B` | DIRECCIÓN Y SERVICIOS GENERALES | 200.124.520 | 8,6 % |
| `422F` | EDUCACIÓN ESPECIAL | 62.892.592 | 2,7 % |
| `322A` | FOMENTO DEL EMPLEO | 58.166.932 | 2,5 % |
| `422H` | FORMACIÓN PROFESIONAL | 46.446.800 | 2,0 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 45.855.454 | 2,0 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 36.039.640 | 1,5 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 19.876.742 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 12.163.868 | 0,5 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 11.827.861 | 0,5 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 11.376.163 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.050.392 | 0,3 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 4.556.604 | 0,2 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 4.282.567 | 0,2 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 4.072.160 | 0,2 % |
| `422C` | CALIDAD EDUCATIVA | 2.560.400 | 0,1 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 336.923 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 333.367 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 325.689 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 185,07 M€ (185.070.075 €) · 13 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 35.521.625 | 19,2 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 33.182.298 | 17,9 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 25.447.078 | 13,7 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 21.056.699 | 11,4 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 17.556.003 | 9,5 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 13.912.970 | 7,5 % |
| `712B` | PESCA Y ACUICULTURA | 10.585.935 | 5,7 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 10.452.006 | 5,6 % |
| `531C` | CAMINOS RURALES | 8.075.000 | 4,4 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 2.730.000 | 1,5 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.508.390 | 1,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 2.361.699 | 1,3 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 1.680.372 | 0,9 % |

</details>

<details open><summary><b><code>direccion</code> — 0,74 M€ (743.869 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 743.869 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 36,99 M€ (36.991.194 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 22.980.822 | 62,1 % |
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 13.023.351 | 35,2 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 719.061 | 1,9 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 267.960 | 0,7 % |

</details>

<details open><summary><b><code>empleo</code> — 41,25 M€ (41.253.142 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 41.253.142 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 21,39 M€ (21.386.224 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 8.124.895 | 38,0 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 6.801.350 | 31,8 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 6.372.876 | 29,8 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 87.103 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 220,76 M€ (220.761.192 €) · 3 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 166.871.078 | 75,6 % |
| `313D` | PROTECCIÓN DEL MENOR | 48.915.288 | 22,2 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 4.974.826 | 2,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 261,04 M€ (261.039.302 €) · 2 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 168.663.594 | 64,6 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 92.375.708 | 35,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,26 M€ (31.256.422 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 28.367.948 | 90,8 % |
| `514A` | PUERTOS Y COSTAS | 2.846.693 | 9,1 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 41.781 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,16 M€ (6.158.402 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACIÓN Y VOLUNTARIADO | 6.158.402 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 45,85 M€ (45.848.955 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 42.487.569 | 92,7 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.738.808 | 3,8 % |
| `432A` | URBANISMO | 1.201.078 | 2,6 % |
| `313H` | TURISMO SOCIAL | 421.500 | 0,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,08 M€ (16.082.000 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 8.836.069 | 54,9 % |
| `323B` | IGUALDAD | 7.245.931 | 45,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.288,38 M€ · 72 códigos · 27,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.434.761.113 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 96.720.856 |
| `513A` | TRANSPORTES | 84.731.104 |
| `633A` | FONDO GLOBAL DE RECURSOS PRESUPUESTARIOS | 72.669.564 |
| `442D` | GESTIÓN FORESTAL | 47.212.647 |
| `442J` | ENERGÍAS LIMPIAS | 43.242.040 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 38.856.120 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 35.668.054 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 26.101.746 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 25.632.074 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 23.542.540 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 22.061.878 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 21.552.986 |
| `124B` | COORDINACIÓN DE POLICIAS LOCALES | 20.185.062 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 17.534.171 |
| `121B` | FUNCIÓN PÚBLICA | 17.380.811 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 16.968.483 |
| `111A` | ASAMBLEA REGIONAL | 15.827.552 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 15.061.441 |
| `313Q` | REFORMA JUVENIL | 14.615.013 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 14.188.619 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 14.054.171 |
| `313M` | FAMILIA | 13.523.231 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 11.573.184 |
| `612F` | PROGRAMACIÓN Y GESTIÓN DE FONDOS EUROPEOS | 11.154.388 |
| … | *resto: 47 códigos* | 133.561.864 |

</details>

### 2026

*Fuente: `portal_movil.html` · 149 líneas · total extraído **8.460,50 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.972,29 M€ (2.972.286.524 €) · 17 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.430.451.413 | 81,8 % |
| `311A` | DIRECCION Y SERVICIOS GENERALES | 438.388.587 | 14,7 % |
| `312A` | PRESTACIONES A LOS DESEMPLEADOS | 43.037.841 | 1,4 % |
| `413B` | SALUD | 17.803.380 | 0,6 % |
| `413D` | SALUD PÚBLICA E INSPECCIONES | 13.241.652 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES DEL IMAS | 7.359.120 | 0,2 % |
| `413G` | INSPECCIÓN DE SERVICIOS SANITARIOS | 4.466.709 | 0,2 % |
| `413H` | INVESTIGACION Y PROYECTOS | 3.444.450 | 0,1 % |
| `315B` | SEGURIDAD Y SALUD LABORAL | 3.120.484 | 0,1 % |
| `413F` | ORDENACIÓN FARMACÉUTICA | 2.812.487 | 0,1 % |
| `412F` | CENTRO DE ÁREA DE CARTAGENA | 2.502.523 | 0,1 % |
| `412J` | PLANIFICACIÓN SANITARIA | 1.481.349 | 0,0 % |
| `413E` | ORDENACIÓN SANITARIA | 1.437.125 | 0,0 % |
| `413I` | INSPECCIÓN CENTROS Y ESTABLECIMIENTOS SANITARIOS | 1.136.633 | 0,0 % |
| `412E` | CENTRO DE ÁREA DE LORCA | 1.067.754 | 0,0 % |
| `411B` | ATENCIÓN AL CIUDADANO | 507.344 | 0,0 % |
| `412M` | COORDINACIÓN REGIONAL DE TRANSPLANTES | 27.673 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.333,24 M€ (2.333.238.090 €) · 22 códigos · 27,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422D` | EDUCACIÓN INFANTIL Y PRIMARIA | 606.495.443 | 26,0 % |
| `422E` | EDUCACIÓN SECUNDARIA | 552.366.050 | 23,7 % |
| `422K` | GESTIÓN EDUCATIVA Y CENTROS CONCERTADOS | 374.990.243 | 16,1 % |
| `421B` | UNIVERSIDADES | 271.097.680 | 11,6 % |
| `321B` | DIRECCIÓN Y SERVICIOS GENERALES | 200.124.520 | 8,6 % |
| `422F` | EDUCACIÓN ESPECIAL | 62.892.592 | 2,7 % |
| `322A` | FOMENTO DEL EMPLEO | 58.166.932 | 2,5 % |
| `422H` | FORMACIÓN PROFESIONAL | 46.446.800 | 2,0 % |
| `422L` | ENSEÑANZAS DE RÉGIMEN ESPECIAL | 45.855.454 | 2,0 % |
| `422J` | SERVICIOS COMPLEMENTARIOS | 36.039.640 | 1,5 % |
| `442G` | PREVENCION, REDUCCION Y GESTION DE RESIDUOS | 19.876.742 | 0,9 % |
| `421D` | RECURSOS HUMANOS DE EDUCACIÓN | 12.163.868 | 0,5 % |
| `422P` | EDUCACION DE PERSONAS ADULTAS | 11.827.861 | 0,5 % |
| `422I` | TECNOLOGÍAS Y PROGRAMAS ESPECIALES DE EDUCACIÓN | 11.376.163 | 0,5 % |
| `421A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.050.392 | 0,3 % |
| `422N` | INSTITUTO DE LAS CUALIFICACIONES DE LA REG. MURCIA | 4.556.604 | 0,2 % |
| `422G` | EDUCACIÓN COMPENSATORIA | 4.282.567 | 0,2 % |
| `321A` | DIRECCIÓN Y SERVICIOS GRALES.DE EMPLEO Y FORMACIÓN | 4.072.160 | 0,2 % |
| `422C` | CALIDAD EDUCATIVA | 2.560.400 | 0,1 % |
| `421C` | CONSEJO ESCOLAR DE LA REGIÓN | 336.923 | 0,0 % |
| `422A` | ESCUELA UNIVERSITARIA DE ENFERMERÍA | 333.367 | 0,0 % |
| `422M` | ORDENACIÓN ACADÉMICA | 325.689 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 185,07 M€ (185.070.075 €) · 13 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `711B` | AYUDAS COMUNITARIAS | 35.521.625 | 19,2 % |
| `712E` | PROMOC.Y MEJORA INDUSTRIA,LA COMERCIALIZ.Y CALIDAD | 33.182.298 | 17,9 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 25.447.078 | 13,7 % |
| `531A` | REFORMA Y DESARROLLO RURAL | 21.056.699 | 11,4 % |
| `712A` | MODERNIZACIÓN DE EXPLOTACIONES | 17.556.003 | 9,5 % |
| `531B` | MODERNIZACIÓN Y MEJORA DE REGADÍOS | 13.912.970 | 7,5 % |
| `712B` | PESCA Y ACUICULTURA | 10.585.935 | 5,7 % |
| `712F` | PRODUCCIÓN Y SANIDAD GANADERA | 10.452.006 | 5,6 % |
| `531C` | CAMINOS RURALES | 8.075.000 | 4,4 % |
| `711C` | OFICINA ORGANISMO PAGADOR | 2.730.000 | 1,5 % |
| `712H` | LABORATORIO AGRARIO Y DE SANIDAD ANIMAL | 2.508.390 | 1,4 % |
| `712I` | SANIDAD VEGETAL Y PLANTAS DE VIVERO | 2.361.699 | 1,3 % |
| `712J` | DIFUSIÓN Y PROMOCIÓN DE LA CALIDAD AGROALIMENTARIA | 1.680.372 | 0,9 % |

</details>

<details open><summary><b><code>direccion</code> — 0,74 M€ (743.869 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112E` | SERVICIOS GRALES SECRETARÍA GRAL DE LA PRESIDENCIA | 743.869 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 36,99 M€ (36.991.194 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431C` | FOMENTO Y GESTIÓN DE VIVIENDA PÚBLICA Y SUELO | 22.980.822 | 62,1 % |
| `431A` | PROMOCIÓN Y REHABILITACIÓN DE VIVIENDAS | 13.023.351 | 35,2 % |
| `431B` | ACTUACIONES EN PATRIMONIO ARQUITECTÓNICO | 719.061 | 1,9 % |
| `431D` | CALIDAD EN LA EDIFICACIÓN | 267.960 | 0,7 % |

</details>

<details open><summary><b><code>empleo</code> — 41,25 M€ (41.253.142 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `324A` | FORMACIÓN PROFESIONAL OCUPACIONAL Y CONTINUA | 41.253.142 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 21,39 M€ (21.386.224 €) · 4 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | FORMACION Y TRANSFERENCIA TECNOLOGICA | 8.124.895 | 38,0 % |
| `542D` | INVESTIGACIÓN CIENTÍFICA Y TÉCNICA | 6.801.350 | 31,8 % |
| `542C` | INNOVACIÓN Y DESARROLLO TECNOLÓGICO | 6.372.876 | 29,8 % |
| `542F` | PROMOC. DE LA INNOVACIÓN Y MEJORA DE LA PRODUCTIV. | 87.103 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 220,76 M€ (220.761.192 €) · 3 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | PERSONAS MAYORES | 166.871.078 | 75,6 % |
| `313D` | PROTECCIÓN DEL MENOR | 48.915.288 | 22,2 % |
| `313O` | RECONOCIMIENTO DERECHO PRESTAC.MATERIA DEPENDENCIA | 4.974.826 | 2,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 261,04 M€ (261.039.302 €) · 2 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313F` | PERSONAS CON DISCAPACIDAD Y OTROS COLECTIVOS | 168.663.594 | 64,6 % |
| `314C` | PENSIONES, AYUDAS Y SUBVENCIONES | 92.375.708 | 35,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 31,26 M€ (31.256.422 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PLANIFICACIÓN Y EVALUACIÓN DE SERVICIOS SOCIALES | 28.367.948 | 90,8 % |
| `514A` | PUERTOS Y COSTAS | 2.846.693 | 9,1 % |
| `412I` | CENTRO DE ÁREA DE CARAVACA | 41.781 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,16 M€ (6.158.402 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | INMIGRACIÓN Y VOLUNTARIADO | 6.158.402 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 45,85 M€ (45.848.955 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751B` | DIRECCIÓN Y SERVICIOS GENERALES | 42.487.569 | 92,7 % |
| `432B` | ORDENACIÓN DEL TERRITORIO | 1.738.808 | 3,8 % |
| `432A` | URBANISMO | 1.201.078 | 2,6 % |
| `313H` | TURISMO SOCIAL | 421.500 | 0,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,08 M€ (16.082.000 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313P` | PREVENCIÓN VIOLENCIA DE GÉNERO | 8.836.069 | 54,9 % |
| `323B` | IGUALDAD | 7.245.931 | 45,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.288,38 M€ · 72 códigos · 27,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | AMORTIZAC.Y GTOS.FINANC.DEUDA PBCA.Y OTRAS OPERACI | 1.434.761.113 |
| `126J` | CENTRO REGIONAL DE INFORMATICA | 96.720.856 |
| `513A` | TRANSPORTES | 84.731.104 |
| `633A` | FONDO GLOBAL DE RECURSOS PRESUPUESTARIOS | 72.669.564 |
| `442D` | GESTIÓN FORESTAL | 47.212.647 |
| `442J` | ENERGÍAS LIMPIAS | 43.242.040 |
| `513C` | CONSERVACIÓN DE LA RED VIARIA | 38.856.120 |
| `512A` | ACONDICIONAMIENTO DE CAUCES Y ESTUDIOS HIDROLOGICO | 35.668.054 |
| `223B` | CONSORCIO REGIONAL EXTINC.INCENDIOS Y SALVAMENTO | 26.101.746 |
| `513D` | PLANIFICACIÓN Y MEJORAS EN LA RED VIARIA | 25.632.074 |
| `611A` | DIRECCIÓN Y SERVICIOS GENERALES | 23.542.540 |
| `442F` | BIODIVERSIDAD Y AREAS PROTEGIDAS | 22.061.878 |
| `112D` | COMUNICACIÓN AUDIOVISUAL | 21.552.986 |
| `124B` | COORDINACIÓN DE POLICIAS LOCALES | 20.185.062 |
| `444A` | PLAN DE COOPERACIÓN LOCAL | 17.534.171 |
| `121B` | FUNCIÓN PÚBLICA | 17.380.811 |
| `442L` | PROTECCIÓN DEL MAR MENOR | 16.968.483 |
| `111A` | ASAMBLEA REGIONAL | 15.827.552 |
| `313R` | RELACIONES CON EL TERCER SECTOR DE ACCIÓN SOCIAL | 15.061.441 |
| `313Q` | REFORMA JUVENIL | 14.615.013 |
| `441A` | SANEAMIEN.DEPURAC.Y ABASTECIMIENTO DE POBLACIONES | 14.188.619 |
| `521A` | ORDENACIÓN Y FOMENTO TELECOMUNIC.Y SOCIEDAD INFORM | 14.054.171 |
| `313M` | FAMILIA | 13.523.231 |
| `223A` | SERVICIO DE PROTECCIÓN CIVIL | 11.573.184 |
| `612F` | PROGRAMACIÓN Y GESTIÓN DE FONDOS EUROPEOS | 11.154.388 |
| … | *resto: 47 códigos* | 133.561.864 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py mur     # regenera este documento
python3 tools/auditoria_magnitud.py mur        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa mur --anio <año> \
    --input ../fuentes/raw/mur/<año>/<fichero> --output /tmp/mur.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-mur.md`](limitaciones-mur.md)

