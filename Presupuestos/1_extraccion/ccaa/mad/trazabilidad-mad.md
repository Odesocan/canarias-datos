# Trazabilidad de la extracción — Comunidad de Madrid (`mad`)

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
| **2015** | 82 | `libro_03.pdf` | 10 | 31,7 % | 20.852,59 | — | no_aplica |
| **2016** | 73 | `libro_03.pdf` | 11 | 37,0 % | 20.139,61 | — | no_aplica |
| **2017** | 73 | `libro_03.pdf` | 11 | 37,0 % | 20.504,09 | — | no_aplica |
| **2018** | 76 | `libro_03.pdf` | 11 | 36,8 % | 21.633,75 | — | no_aplica |
| **2019** | 80 | `libro_03.pdf` | 11 | 36,2 % | 22.776,62 | — | no_aplica |
| **2020** | 80 | `libro_03.pdf` | 11 | 36,2 % | 22.776,62 | — | no_aplica |
| **2021** | 80 | `libro_03.pdf` | 11 | 36,2 % | 22.776,62 | — | no_aplica |
| **2022** | 89 | `libro_03.pdf` | 11 | 34,8 % | 25.900,85 | — | no_aplica |
| **2023** | 89 | `libro_03.pdf` | 11 | 34,8 % | 25.900,85 | — | no_aplica |
| **2024** | 87 | `libro_03.pdf` | 11 | 39,1 % | 30.446,56 | — | no_aplica |
| **2025** | 88 | `libro_03.pdf` | 11 | 39,8 % | 31.453,01 | — | no_aplica |
| **2026** | 88 | `libro_03.pdf` | 11 | 39,8 % | 33.271,72 | — | no_aplica |

**URL(s) de origen:**
- <https://www.comunidad.madrid/docs/assets/2017/01/17/03_estructuraymemoria_2015_0.pdf>
- <https://www.comunidad.madrid/docs/assets/2017/05/22/2016-libro-03-ingygastos-mempptocons.pdf>
- <https://www.comunidad.madrid/docs/assets/2018/01/05/2018-presupuesto-libro-03-resumenes-memoria.pdf>
- <https://www.comunidad.madrid/docs/assets/2021/12/22/2022-presupuesto-libro-03-ingresos-gastos.pdf>
- <https://www.comunidad.madrid/docs/assets/2023/12/29/2024-presupuesto-libro-03-ingresos-gastos.pdf>
- <https://www.comunidad.madrid/docs/assets/2024/12/27/2025-presupuesto-libro-03-ingresos-gastos.pdf>
- <https://www.comunidad.madrid/docs/assets/2025/10/24/2017_libro_03_ingresos-gastos-memoria.pdf>
- <https://www.comunidad.madrid/docs/assets/2025/10/24/2019-presupuesto-libro-03-ingresos-gastos.pdf>
- <https://www.comunidad.madrid/docs/assets/2025/12/26/2026-presupuesto-libro-03-ingresos-gastos.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 7.191,84 | 7.415,38 | 7.599,71 | 7.828,24 | 8.066,70 | 8.066,70 | 8.066,70 | 8.759,66 | 8.759,66 | 10.211,96 | 10.542,86 | 11.093,46 |
| `educacion` | 2.074,43 | 2.314,36 | 2.370,93 | 2.361,68 | 2.487,48 | 2.487,48 | 2.487,48 | 2.825,10 | 2.825,10 | 3.071,36 | 3.178,68 | 3.291,30 |
| `soberania` | — | 33,93 | 40,69 | 45,26 | 48,40 | 48,40 | 48,40 | 59,61 | 59,61 | 98,21 | 100,15 | 104,85 |
| `direccion` | 1,13 | 1,27 | 1,29 | 1,30 | 1,34 | 1,34 | 1,34 | 1,58 | 1,58 | 1,57 | 1,69 | 1,72 |
| `vivienda` | 336,08 | 515,60 | 447,57 | 356,21 | 348,90 | 348,90 | 348,90 | 292,39 | 292,39 | 551,30 | 766,51 | 794,13 |
| `empleo` | 206,24 | 457,12 | 467,98 | 485,13 | 500,76 | 500,76 | 500,76 | 427,31 | 427,31 | 408,11 | 439,50 | 437,51 |
| `idi` | 444,57 | 15,03 | 16,14 | 124,63 | 154,24 | 154,24 | 154,24 | 229,00 | 229,00 | 220,66 | 238,63 | 246,70 |
| `dependencia` | 1.220,06 | 1.073,08 | 1.167,42 | 1.258,14 | 1.324,04 | 1.324,04 | 1.324,04 | 1.468,15 | 1.468,15 | 1.809,83 | 1.882,52 | 2.043,28 |
| `discapacidad` | — | 302,97 | 309,73 | 334,83 | 341,82 | 341,82 | 341,82 | 426,66 | 426,66 | 450,66 | 450,97 | 497,64 |
| `diversidad` | 5,95 | — | — | — | — | — | — | — | — | — | — | — |
| `turismo` | 13,02 | 25,25 | 32,02 | 43,22 | 47,92 | 47,92 | 47,92 | 94,51 | 94,51 | 103,61 | 87,29 | 85,63 |
| `igualdad` | 21,54 | 22,47 | 22,57 | 23,72 | 24,87 | 24,87 | 24,87 | 32,81 | 32,81 | 40,54 | 39,85 | 38,27 |
| **Σ asignado** | 11.514,88 | 12.176,47 | 12.476,04 | 12.862,36 | 13.346,47 | 13.346,47 | 13.346,47 | 14.616,77 | 14.616,77 | 16.967,80 | 17.728,65 | 18.634,49 |
| *(sin concepto)* | 9.337,71 | 7.963,14 | 8.028,05 | 8.771,40 | 9.430,15 | 9.430,15 | 9.430,15 | 11.284,08 | 11.284,08 | 13.478,76 | 13.724,36 | 14.637,23 |
| **TOTAL extraído** | 20.852,59 | 20.139,61 | 20.504,09 | 21.633,75 | 22.776,62 | 22.776,62 | 22.776,62 | 25.900,85 | 25.900,85 | 30.446,56 | 31.453,01 | 33.271,72 |

**Conceptos sin ninguna línea en toda la serie:** `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +3,1 % | +2,5 % | +3,0 % | +3,0 % | +0,0 % | +0,0 % | +8,6 % | +0,0 % | +16,6 % | +3,2 % | +5,2 % |
| `educacion` | +11,6 % | +2,4 % | −0,4 % | +5,3 % | +0,0 % | +0,0 % | +13,6 % | +0,0 % | +8,7 % | +3,5 % | +3,5 % |
| `soberania` | **nuevo** ⛔ | +19,9 % | +11,2 % | +7,0 % | +0,0 % | +0,0 % | +23,2 % | +0,0 % | +64,8 % ⚠ | +2,0 % | +4,7 % |
| `direccion` | +12,0 % | +1,8 % | +1,0 % | +2,6 % | +0,0 % | +0,0 % | +17,8 % | +0,0 % | −0,7 % | +7,9 % | +1,5 % |
| `vivienda` | +53,4 % ⚠ | −13,2 % | −20,4 % | −2,1 % | +0,0 % | +0,0 % | −16,2 % | +0,0 % | +88,6 % ⚠ | +39,0 % | +3,6 % |
| `empleo` | +121,6 % ⚠ | +2,4 % | +3,7 % | +3,2 % | +0,0 % | +0,0 % | −14,7 % | +0,0 % | −4,5 % | +7,7 % | −0,5 % |
| `idi` | −96,6 % ⚠ | +7,4 % | +671,9 % ⚠ | +23,8 % | +0,0 % | +0,0 % | +48,5 % ⚠ | +0,0 % | −3,6 % | +8,1 % | +3,4 % |
| `dependencia` | −12,0 % | +8,8 % | +7,8 % | +5,2 % | +0,0 % | +0,0 % | +10,9 % | +0,0 % | +23,3 % | +4,0 % | +8,5 % |
| `discapacidad` | **nuevo** ⛔ | +2,2 % | +8,1 % | +2,1 % | +0,0 % | +0,0 % | +24,8 % | +0,0 % | +5,6 % | +0,1 % | +10,3 % |
| `diversidad` | **a 0** ⛔ | · | · | · | · | · | · | · | · | · | · |
| `turismo` | +93,9 % ⚠ | +26,8 % | +35,0 % | +10,9 % | +0,0 % | +0,0 % | +97,2 % ⚠ | +0,0 % | +9,6 % | −15,8 % | −1,9 % |
| `igualdad` | +4,3 % | +0,4 % | +5,1 % | +4,8 % | +0,0 % | +0,0 % | +31,9 % | +0,0 % | +23,6 % | −1,7 % | −4,0 % |
| **TOTAL** | −3,4 % | +1,8 % | +5,5 % | +5,3 % | +0,0 % | +0,0 % | +13,7 % | +0,0 % | +17,6 % | +3,3 % | +5,8 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `discapacidad` | **APARECE** | 0 → 302,97 M€ |
| 2016 | `empleo` | **SALTO** | 206,24 → 457,12 M€ (+121,6 % ⚠) |
| 2016 | `idi` | **SALTO** | 444,57 → 15,03 M€ (−96,6 % ⚠) |
| 2016 | `vivienda` | **SALTO** | 336,08 → 515,60 M€ (+53,4 % ⚠) |
| 2018 | `idi` | **SALTO** | 16,14 → 124,63 M€ (+671,9 % ⚠) |
| 2022 | `idi` | **SALTO** | 154,24 → 229,00 M€ (+48,5 % ⚠) |
| 2024 | `vivienda` | **SALTO** | 292,39 → 551,30 M€ (+88,6 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (6 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `12001` | 204,88 | 2015:(sin concepto), 2016:empleo, 2017:empleo, 2018:empleo, 2019:empleo, 2020:empleo, 2021:empleo, 2022:empleo, 2023:empleo, 2024:empleo, 2025:empleo, 2026:empleo |
| `15011` | 159,63 | 2015:(sin concepto), 2016:educacion, 2017:educacion, 2018:educacion, 2019:educacion, 2020:educacion, 2021:educacion, 2022:educacion, 2023:educacion, 2024:educacion, 2025:educacion, 2026:educacion |
| `16001` | 37,18 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:vivienda, 2023:vivienda, 2024:soberania, 2025:soberania, 2026:soberania |
| `14001` | 36,22 | 2015:vivienda, 2016:vivienda, 2017:vivienda, 2018:vivienda, 2019:vivienda, 2020:vivienda, 2021:vivienda, 2022:(sin concepto), 2023:(sin concepto), 2024:vivienda, 2025:vivienda, 2026:vivienda |
| `17011` | 35,87 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:sanidad, 2023:sanidad, 2024:sanidad, 2025:sanidad, 2026:sanidad |
| `16206` | 30,37 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:idi, 2020:idi, 2021:idi, 2022:idi, 2023:idi, 2024:idi, 2025:idi, 2026:idi |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `libro_03.pdf` · 82 líneas · total extraído **20.852,59 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.191,84 M€ (7.191.837.009 €) · 3 códigos · 34,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILENO DE SALUD | 7.170.114.000 | 99,7 % |
| `17001` | S.G.T. DE SANIDAD | 20.358.323 | 0,3 % |
| `17002` | VICECONSEJERIA DE ORDENACION SANITARIA E INFRAESTRU | 1.364.686 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.074,43 M€ (2.074.434.949 €) · 6 códigos · 9,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE BECAS Y AYUDAS A LA EDUCACION | 1.023.116.141 | 49,3 % |
| `15014` | D.G. DE UNIVERSIDADES E INVESTIGACION | 873.971.992 | 42,1 % |
| `15010` | D.G. DE EDUCACION INFANTIL Y PRIMARIA | 77.091.160 | 3,7 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACION Y REINSERCION DEL M | 38.177.793 | 1,8 % |
| `15001` | S.G.T. DE EDUCACION, JUVENTUD Y DEPORTE | 32.128.614 | 1,5 % |
| `15013` | D.G. DE MEJORA DE LA CALIDAD DE LA ENSENANZA | 29.949.249 | 1,4 % |

</details>

<details open><summary><b><code>direccion</code> — 1,13 M€ (1.134.027 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.134.027 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 336,08 M€ (336.084.222 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | INSTITUTO DE LA VIVIENDA DE MADRID | 240.784.918 | 71,6 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACION | 54.247.471 | 16,1 % |
| `14001` | S.G.T. DE TRANSPORTES, INFRAESTRUCTURAS Y VIVIENDA | 34.685.266 | 10,3 % |
| `16012` | D.G. DE URBANISMO Y ESTRATEGIA TERRITORIAL | 6.366.567 | 1,9 % |

</details>

<details open><summary><b><code>empleo</code> — 206,24 M€ (206.240.146 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DE EMPLEO | 156.404.230 | 75,8 % |
| `20001` | S.G.T. EMPLEO, TURISMO Y CULTURA | 38.984.069 | 18,9 % |
| `20018` | D.G. DE ESTRATEGIA Y FOMENTO DE EMPLEO | 10.851.847 | 5,3 % |

</details>

<details open><summary><b><code>idi</code> — 444,57 M€ (444.566.824 €) · 2 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `12002` | VICECONSEJERIA DE INNOVACION, INDUSTRIA, COMERCIO Y | 415.900.299 | 93,6 % |
| `17010` | D.G. DE INVESTIGACION, FORMACION E INFRAESTRUCTURAS | 28.666.525 | 6,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.220,06 M€ (1.220.062.890 €) · 4 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19010` | D.G. DE SERVICIOS SOCIALES | 393.356.009 | 32,2 % |
| `19011` | D.G. DEL MAYOR | 297.378.010 | 24,4 % |
| `19102` | SERVICIO REGIONAL DE BIENESTAR SOCIAL | 273.718.261 | 22,4 % |
| `19014` | D.G. DE COORDINACION DE LA DEPENDENCIA | 255.610.610 | 21,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,95 M€ (5.950.745 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19015` | D.G. DE INMIGRACION | 5.950.745 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 13,02 M€ (13.023.263 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20014` | D.G. DE TURISMO | 13.023.263 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 21,54 M€ (21.543.341 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 21.543.341 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 9.337,71 M€ · 56 códigos · 44,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | D.G. DE POLITICA FINANCIERA, TESORERIA Y PATRIMONIO | 3.885.955.165 |
| `15016` | D.G. DE RECURSOS HUMANOS | 1.986.944.621 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 957.658.537 |
| `11012` | D.G. DE RELACIONES CON LA ADMINISTRACION DE JUSTICIA | 355.582.931 |
| `26001` | D.G. DE PRESUPUESTOS Y RECURSOS HUMANOS | 312.442.736 |
| `14012` | D.G. DE CARRETERAS | 209.781.031 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA Y PORTAVOCIA DEL GOBIE | 191.260.997 |
| `15011` | REGIMEN ESPECIAL | 122.936.546 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 112.960.169 |
| `11011` | D.G. DE PROTECCION CIUDADANA | 112.094.052 |
| `19105` | INSTITUTO MADRILENO DE LA FAMILIA Y EL MENOR | 110.196.996 |
| `20017` | D.G. DE FORMACION | 99.044.172 |
| `11010` | D.G. DE SEGURIDAD E INTERIOR | 96.448.234 |
| `11017` | D.G. DE COOPERACION CON LA ADMINISTRACION LOCAL | 66.523.635 |
| `16010` | D.G. DE MEDIO AMBIENTE | 52.823.569 |
| `20010` | D.G. DE BELLAS ARTES, DEL LIBRO Y DE ARCHIVOS | 43.098.899 |
| `14011` | D.G. DE INFRAESTRUCTURAS | 41.741.022 |
| `20011` | D.G. DE ARTES ESCENICAS, MUSICA Y AUDIOVISUAL | 36.959.936 |
| `15002` | VICECONSEJERIA DE ORGANIZACION EDUCATIVA | 36.805.637 |
| `17106` | AGENCIA ANTIDROGA DE LA COMUNIDAD DE MADRID | 36.115.325 |
| `17011` | DIRECCION GENERAL DE ORDENACION E INSPECCION | 35.868.682 |
| `12016` | D.G. DE TRIBUTOS Y ORDENACION Y GESTION DE JUEGO | 34.548.931 |
| `15018` | D.G. DE JUVENTUD Y DEPORTES | 29.874.318 |
| `12001` | S.G.T.DE ECONOMIA Y HACIENDA | 29.867.716 |
| `16011` | D.G. DE EVALUACION AMBIENTAL | 27.910.858 |
| … | *resto: 31 códigos* | 312.266.539 |

</details>

### 2016

*Fuente: `libro_03.pdf` · 73 líneas · total extraído **20.139,61 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.415,38 M€ (7.415.379.241 €) · 3 códigos · 36,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILENO DE SALUD | 7.283.234.315 | 98,2 % |
| `17012` | D.G. DE SALUD PUBLICA | 107.826.618 | 1,5 % |
| `17001` | S.G.T. DE SANIDAD | 24.318.308 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 2.314,36 M€ (2.314.363.938 €) · 6 códigos · 11,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE INNOVACION, BECAS Y AYUDAS | 1.106.799.776 | 47,8 % |
| `15014` | D.G. DE UNIVERSIDADES E INVESTIGACION | 954.421.032 | 41,2 % |
| `15010` | D.G. DE EDUCACION INFANTIL, PRIMARIA Y SECUNDARIA | 154.805.596 | 6,7 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACION Y REINSERCION DEL M | 38.514.629 | 1,7 % |
| `15001` | S.G.T. DE EDUCACION, JUVENTUD Y DEPORTE | 30.496.605 | 1,3 % |
| `15011` | D.G. DE FORMACION PROFESIONAL Y ENSENANZAS DE REGI | 29.326.300 | 1,3 % |

</details>

<details open><summary><b><code>soberania</code> — 33,93 M€ (33.927.477 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA Y GANADERIA | 33.927.477 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,27 M€ (1.269.790 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.269.790 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 515,60 M€ (515.604.020 €) · 4 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE MADRID | 242.829.877 | 47,1 % |
| `16012` | D.G. DE URBANISMO | 180.132.017 | 34,9 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACION | 68.750.309 | 13,3 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E INFRAESTRUCTURAS | 23.891.817 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 457,12 M€ (457.123.724 €) · 4 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PUBLICO DE EMPLEO | 204.912.924 | 44,8 % |
| `12001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 197.396.272 | 43,2 % |
| `20002` | VICECONSEJERIA DE HACIENDA Y EMPLEO | 36.252.878 | 7,9 % |
| `20001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 18.561.650 | 4,1 % |

</details>

<details open><summary><b><code>idi</code> — 15,03 M€ (15.029.996 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17010` | D.G. DE PLANIFICACION, INVESTIGACION Y FORMACION | 15.029.996 | 100,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.073,08 M€ (1.073.078.872 €) · 3 códigos · 5,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCION A LA DEPENDENCIA Y AL MAYOR | 564.939.399 | 52,6 % |
| `19102` | AGENCIA MADRILENA DE ATENCION SOCIAL | 336.769.302 | 31,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACION SOCIAL | 171.370.171 | 16,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 302,97 M€ (302.971.858 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCION A PERSONAS CON DISCAPACIDAD | 302.971.858 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,25 M€ (25.251.048 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 13.466.239 | 53,3 % |
| `4001` | OFICINA DE CULTURA Y TURISMOOFICINA DE CULTURA Y TUR | 11.784.809 | 46,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 22,47 M€ (22.471.311 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 22.471.311 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 7.963,14 M€ · 46 códigos · 39,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PUBLICA | 2.528.447.338 |
| `15016` | D.G. DE RECURSOS HUMANOS | 1.990.501.093 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.159.630.369 |
| `12010` | D.G. DE ECONOMIA Y POLITICA FINANCIERA | 428.616.569 |
| `11012` | D.G. DE JUSTICIA | 363.677.354 |
| `26001` | CREDITOS CENTRALIZADOS | 220.229.418 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 187.988.409 |
| `11011` | D.G. DE PROTECCION CIUDADANA | 116.251.832 |
| `20017` | D.G. DE FORMACION | 112.223.456 |
| `11010` | D.G. DE SEGURIDAD | 97.906.652 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 92.506.916 |
| `16016` | D.G. DE ADMINISTRACION LOCAL | 66.156.873 |
| `16010` | D.G. DE MEDIO AMBIENTE | 48.927.552 |
| `4010` | D.G. DE PROMOCION CULTURAL | 48.502.400 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 45.437.306 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 45.101.083 |
| `15018` | D.G. DE JUVENTUD Y DEPORTE | 44.701.451 |
| `12016` | D.G. DE TRIBUTOS Y ORDENACION Y GESTION DE JUEGO | 35.346.899 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA Y PORTAVOCIA DEL GOBIE | 31.803.479 |
| `19001` | S.G.T.POLITICAS SOCIALES Y FAMILIA | 31.744.393 |
| `1001` | ASAMBLEA DE MADRID | 28.362.000 |
| `16001` | TERRITORIO | 26.000.329 |
| `17011` | DIRECCION GENERAL DE INSPECCION Y ORDENACION | 19.507.926 |
| `12018` | INTERVENCION GENERAL | 19.093.332 |
| `20114` | INSTITUTO REGIONAL DE SEGURIDAD Y SALUD EN EL TRABAJ | 18.807.160 |
| … | *resto: 21 códigos* | 155.666.441 |

</details>

### 2017

*Fuente: `libro_03.pdf` · 73 líneas · total extraído **20.504,09 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.599,71 M€ (7.599.708.222 €) · 3 códigos · 37,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILENO DE SALUD | 7.451.957.970 | 98,1 % |
| `17012` | D.G. DE SALUD PUBLICA | 113.475.119 | 1,5 % |
| `17001` | S.G.T. DE SANIDAD | 34.275.133 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.370,93 M€ (2.370.928.847 €) · 6 códigos · 11,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE INNOVACION, BECAS Y AYUDAS | 1.125.217.320 | 47,5 % |
| `15014` | D.G. DE UNIVERSIDADES E INVESTIGACION | 999.710.656 | 42,2 % |
| `15010` | D.G. DE EDUCACION INFANTIL, PRIMARIA Y SECUNDARIA | 149.702.179 | 6,3 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACION Y REINSERCION DEL M | 37.695.646 | 1,6 % |
| `15001` | S.G.T. DE EDUCACION, JUVENTUD Y DEPORTE | 31.862.444 | 1,3 % |
| `15011` | D.G. DE FORMACION PROFESIONAL Y ENSENANZAS DE REGI | 26.740.602 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 40,69 M€ (40.692.773 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA Y GANADERIA | 40.692.773 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,29 M€ (1.292.258 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.292.258 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 447,57 M€ (447.569.338 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE MADRID | 268.836.416 | 60,1 % |
| `16012` | D.G. DE URBANISMO | 84.897.259 | 19,0 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACION | 57.612.231 | 12,9 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E INFRAESTRUCTURAS | 36.223.432 | 8,1 % |

</details>

<details open><summary><b><code>empleo</code> — 467,98 M€ (467.975.285 €) · 4 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PUBLICO DE EMPLEO | 206.943.801 | 44,2 % |
| `12001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 195.573.372 | 41,8 % |
| `20002` | VICECONSEJERIA DE HACIENDA Y EMPLEO | 36.518.167 | 7,8 % |
| `20001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 28.939.945 | 6,2 % |

</details>

<details open><summary><b><code>idi</code> — 16,14 M€ (16.144.647 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17010` | D.G. DE PLANIFICACION, INVESTIGACION Y FORMACION | 16.144.647 | 100,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.167,42 M€ (1.167.421.468 €) · 3 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCION A LA DEPENDENCIA Y AL MAYOR | 602.871.548 | 51,6 % |
| `19102` | AGENCIA MADRILENA DE ATENCION SOCIAL | 347.241.624 | 29,7 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACION SOCIAL | 217.308.296 | 18,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 309,73 M€ (309.725.958 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCION A PERSONAS CON DISCAPACIDAD | 309.725.958 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 32,02 M€ (32.015.390 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 20.257.566 | 63,3 % |
| `4001` | OFICINA DE CULTURA Y TURISMOOFICINA DE CULTURA Y TUR | 11.757.824 | 36,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 22,57 M€ (22.566.555 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 22.566.555 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 8.028,05 M€ · 46 códigos · 39,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PUBLICA | 2.642.941.714 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.021.693.565 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.232.008.534 |
| `11012` | D.G. DE JUSTICIA | 410.762.131 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 191.046.623 |
| `16016` | D.G. DE ADMINISTRACION LOCAL | 169.230.778 |
| `20017` | D.G. DE FORMACION | 144.801.092 |
| `11011` | D.G. DE PROTECCION CIUDADANA | 134.790.338 |
| `26001` | CREDITOS CENTRALIZADOS | 107.066.587 |
| `11010` | D.G. DE SEGURIDAD | 98.494.992 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 98.421.413 |
| `30001` | FONDO DE CONTINGENCIA | 92.695.119 |
| `16010` | D.G. DE MEDIO AMBIENTE | 51.695.913 |
| `4010` | D.G. DE PROMOCION CULTURAL | 49.992.679 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 48.792.419 |
| `15018` | D.G. DE JUVENTUD Y DEPORTE | 47.422.941 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 47.235.226 |
| `19001` | S.G.T. DE POLITICAS SOCIALES Y FAMILIA | 37.391.240 |
| `15002` | VICECONSEJERIA DE ORGANIZACION EDUCATIVA | 37.312.561 |
| `12016` | D.G. DE TRIBUTOS Y ORDENACION Y GESTION DE JUEGO | 35.633.054 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA Y PORTAVOCIA DEL GOBIE | 35.223.194 |
| `12010` | D.G. DE ECONOMIA Y POLITICA FINANCIERA | 29.722.211 |
| `1001` | ASAMBLEA DE MADRID | 28.681.000 |
| `16001` | TERRITORIO | 26.676.900 |
| `17011` | D.G. DE INSPECCION Y ORDENACION | 19.856.638 |
| … | *resto: 21 códigos* | 188.464.112 |

</details>

### 2018

*Fuente: `libro_03.pdf` · 76 líneas · total extraído **21.633,75 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 7.828,24 M€ (7.828.244.717 €) · 3 códigos · 36,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILENO DE SALUD | 7.701.162.955 | 98,4 % |
| `17012` | D.G. DE SALUD PUBLICA | 93.614.755 | 1,2 % |
| `17001` | S.G.T. DE SANIDAD | 33.467.007 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 2.361,68 M€ (2.361.681.788 €) · 6 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE BECAS Y AYUDAS AL ESTUDIO | 1.165.197.736 | 49,3 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSENANZAS ARTISTICAS SUPERI | 945.274.034 | 40,0 % |
| `15010` | D.G. DE EDUCACION INFANTIL, PRIMARIA Y SECUNDARIA | 150.080.327 | 6,4 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACION Y REINSERCION DEL M | 37.740.225 | 1,6 % |
| `15001` | S.G.T. DE EDUCACION E INVESTIGACION | 36.306.300 | 1,5 % |
| `15011` | D.G. DE FORMACION PROFESIONAL Y ENSENANZAS DE REGI | 27.083.166 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 45,26 M€ (45.256.684 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA Y GANADERIA | 45.256.684 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,30 M€ (1.304.974 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.304.974 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 356,21 M€ (356.209.532 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE MADRID | 232.965.521 | 65,4 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACION | 62.263.089 | 17,5 % |
| `16012` | D.G. DE URBANISMO | 35.081.950 | 9,8 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E INFRAESTRUCTURAS | 25.898.972 | 7,3 % |

</details>

<details open><summary><b><code>empleo</code> — 485,13 M€ (485.126.035 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PUBLICO DE EMPLEO | 217.339.889 | 44,8 % |
| `12001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 201.155.422 | 41,5 % |
| `20002` | VICECONSEJERIA DE HACIENDA Y EMPLEO | 37.571.766 | 7,7 % |
| `20001` | S.G.T. DE ECONOMIA, EMPLEO Y HACIENDA | 29.058.958 | 6,0 % |

</details>

<details open><summary><b><code>idi</code> — 124,63 M€ (124.626.170 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACION E INNOVACION | 107.993.981 | 86,7 % |
| `17010` | D.G. DE PLANIFICACION, INVESTIGACION Y FORMACION | 16.632.189 | 13,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.258,14 M€ (1.258.136.922 €) · 3 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCION A LA DEPENDENCIA Y AL MAYOR | 660.518.083 | 52,5 % |
| `19102` | AGENCIA MADRILENA DE ATENCION SOCIAL | 362.768.435 | 28,8 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACION SOCIAL | 234.850.404 | 18,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 334,83 M€ (334.830.730 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCION A PERSONAS CON DISCAPACIDAD | 334.830.730 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 43,22 M€ (43.215.293 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 23.827.754 | 55,1 % |
| `4001` | S.G.T.CULTURA, TURISMO Y DEPORTES | 19.387.539 | 44,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 23,72 M€ (23.722.547 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 23.722.547 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 8.771,40 M€ · 48 códigos · 40,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PUBLICA | 2.997.543.219 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.100.146.473 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.333.017.708 |
| `11012` | D.G. DE JUSTICIA | 440.543.934 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 208.720.529 |
| `16016` | D.G. DE ADMINISTRACION LOCAL | 189.839.751 |
| `20017` | D.G. DE FORMACION | 167.469.117 |
| `26001` | CREDITOS CENTRALIZADOS | 153.367.174 |
| `11011` | D.G. DE EMERGENCIAS | 152.410.628 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 115.794.459 |
| `30001` | FONDO DE CONTINGENCIA | 96.649.376 |
| `11010` | D.G. DE SEGURIDAD, PROTECCION CIVIL Y FORMACION | 87.751.351 |
| `16010` | D.G. DE MEDIO AMBIENTE | 69.664.033 |
| `19001` | S.G.T. DE POLITICAS SOCIALES Y FAMILIA | 63.862.679 |
| `4010` | D.G. DE PROMOCION CULTURAL | 53.441.169 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 50.528.988 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 49.299.422 |
| `4014` | D.G. DE JUVENTUD Y DEPORTE | 48.672.860 |
| `12016` | D.G. DE TRIBUTOS Y ORDENACION Y GESTION DE JUEGO | 35.539.621 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA Y PORTAVOCIA DEL GOBIE | 33.775.276 |
| `1001` | ASAMBLEA DE MADRID | 29.752.700 |
| `16001` | S.G.T. DE MEDIO AMBIENTE, ADMIN. LOCAL Y ORDEN. TERRIT | 26.848.153 |
| `12017` | D.G. DE CONTRATACION, PATRIMONIO Y TESORERIA | 21.723.595 |
| `15002` | VICECONSEJERIA DE ORGANIZACION EDUCATIVA | 20.201.525 |
| `17011` | D.G. DE INSPECCION Y ORDENACION | 20.182.751 |
| … | *resto: 23 códigos* | 204.648.777 |

</details>

### 2019

*Fuente: `libro_03.pdf` · 80 líneas · total extraído **22.776,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.066,70 M€ (8.066.704.298 €) · 3 códigos · 35,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 7.930.064.052 | 98,3 % |
| `17012` | D.G. DE SALUD PÚBLICA | 97.919.046 | 1,2 % |
| `17001` | S.G.T. DE SANIDAD | 38.721.200 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.487,48 M€ (2.487.484.407 €) · 6 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE BECAS Y AYUDAS AL ESTUDIO | 1.244.401.888 | 50,0 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSEÑANZAS ARTÍSTICAS | 988.086.344 | 39,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y SECUNDARIA | 157.168.100 | 6,3 % |
| `5104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 38.544.669 | 1,5 % |
| `15001` | S.G.T. DE EDUCACIÓN E INVESTIGACIÓN | 31.462.944 | 1,3 % |
| `15011` | D.G. DE FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE | 27.820.462 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 48,40 M€ (48.402.728 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 48.402.728 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,34 M€ (1.338.573 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.338.573 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 348,90 M€ (348.895.987 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 223.708.273 | 64,1 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 78.326.673 | 22,4 % |
| `16012` | D.G. DE URBANISMO Y SUELO | 30.726.065 | 8,8 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E | 16.134.976 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 500,76 M€ (500.762.141 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 228.712.505 | 45,7 % |
| `12001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 204.878.735 | 40,9 % |
| `20002` | VICECONSEJERÍA DE HACIENDA Y EMPLEO | 34.892.127 | 7,0 % |
| `20001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 32.278.774 | 6,4 % |

</details>

<details open><summary><b><code>idi</code> — 154,24 M€ (154.239.111 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN | 115.577.668 | 74,9 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 21.776.614 | 14,1 % |
| `17010` | D.G. DE PLANIFICACIÓN, INVESTIGACIÓN Y FORMACIÓN | 16.884.829 | 10,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.324,04 M€ (1.324.040.720 €) · 3 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN A LA DEPENDENCIA Y AL MAYOR | 699.339.471 | 52,8 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 388.908.318 | 29,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN SOCIAL | 235.792.931 | 17,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 341,82 M€ (341.816.832 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 341.816.832 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,92 M€ (47.918.752 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 24.437.277 | 51,0 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTES | 23.481.475 | 49,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 24,87 M€ (24.865.106 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 24.865.106 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 9.430,15 M€ · 51 códigos · 41,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.371.532.091 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.228.439.108 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.394.254.493 |
| `5010` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 365.672.016 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 213.017.273 |
| `11021` | D.G. DE ADMINISTRACIÓN LOCAL | 193.051.452 |
| `20017` | D.G. DE FORMACIÓN | 170.311.016 |
| `11011` | D.G. DE EMERGENCIAS | 161.933.072 |
| `26001` | CRÉDITOS CENTRALIZADOS | 144.679.108 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 115.906.409 |
| `30001` | FONDO DE CONTINGENCIA | 100.400.000 |
| `11010` | D.G. DE SEGURIDAD, PROTECCIÓN CIVIL Y FORMACIÓN | 96.532.010 |
| `5011` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 93.699.621 |
| `16010` | D.G. DE MEDIO AMBIENTE Y SOSTENIBILIDAD | 88.656.618 |
| `19001` | S.G.T. DE POLÍTICAS SOCIALES Y FAMILIA | 76.913.421 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 55.807.549 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 55.426.096 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 52.882.493 |
| `11001` | S.G.T. DE LA VICEPRESIDENCIA, CONSEJERÍA DE | 40.566.979 |
| `4014` | D.G. DE DEPORTES | 39.754.019 |
| `12016` | D.G. DE TRIBUTOS | 33.684.491 |
| `1001` | ASAMBLEA DE MADRID | 32.127.600 |
| `12017` | D.G. DE CONTRATACIÓN, PATRIMONIO Y TESORERÍA | 27.814.598 |
| `16001` | S.G.T. DE MEDIO AMBIENTE Y ORDENACIÓN DEL | 26.191.918 |
| `12018` | INTERVENCIÓN GENERAL | 21.196.032 |
| … | *resto: 26 códigos* | 229.700.026 |

</details>

### 2020

*Fuente: `libro_03.pdf` · 80 líneas · total extraído **22.776,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.066,70 M€ (8.066.704.298 €) · 3 códigos · 35,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 7.930.064.052 | 98,3 % |
| `17012` | D.G. DE SALUD PÚBLICA | 97.919.046 | 1,2 % |
| `17001` | S.G.T. DE SANIDAD | 38.721.200 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.487,48 M€ (2.487.484.407 €) · 6 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE BECAS Y AYUDAS AL ESTUDIO | 1.244.401.888 | 50,0 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSEÑANZAS ARTÍSTICAS | 988.086.344 | 39,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y SECUNDARIA | 157.168.100 | 6,3 % |
| `5104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 38.544.669 | 1,5 % |
| `15001` | S.G.T. DE EDUCACIÓN E INVESTIGACIÓN | 31.462.944 | 1,3 % |
| `15011` | D.G. DE FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE | 27.820.462 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 48,40 M€ (48.402.728 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 48.402.728 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,34 M€ (1.338.573 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.338.573 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 348,90 M€ (348.895.987 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 223.708.273 | 64,1 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 78.326.673 | 22,4 % |
| `16012` | D.G. DE URBANISMO Y SUELO | 30.726.065 | 8,8 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E | 16.134.976 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 500,76 M€ (500.762.141 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 228.712.505 | 45,7 % |
| `12001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 204.878.735 | 40,9 % |
| `20002` | VICECONSEJERÍA DE HACIENDA Y EMPLEO | 34.892.127 | 7,0 % |
| `20001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 32.278.774 | 6,4 % |

</details>

<details open><summary><b><code>idi</code> — 154,24 M€ (154.239.111 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN | 115.577.668 | 74,9 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 21.776.614 | 14,1 % |
| `17010` | D.G. DE PLANIFICACIÓN, INVESTIGACIÓN Y FORMACIÓN | 16.884.829 | 10,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.324,04 M€ (1.324.040.720 €) · 3 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN A LA DEPENDENCIA Y AL MAYOR | 699.339.471 | 52,8 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 388.908.318 | 29,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN SOCIAL | 235.792.931 | 17,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 341,82 M€ (341.816.832 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 341.816.832 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,92 M€ (47.918.752 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 24.437.277 | 51,0 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTES | 23.481.475 | 49,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 24,87 M€ (24.865.106 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 24.865.106 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 9.430,15 M€ · 51 códigos · 41,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.371.532.091 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.228.439.108 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.394.254.493 |
| `5010` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 365.672.016 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 213.017.273 |
| `11021` | D.G. DE ADMINISTRACIÓN LOCAL | 193.051.452 |
| `20017` | D.G. DE FORMACIÓN | 170.311.016 |
| `11011` | D.G. DE EMERGENCIAS | 161.933.072 |
| `26001` | CRÉDITOS CENTRALIZADOS | 144.679.108 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 115.906.409 |
| `30001` | FONDO DE CONTINGENCIA | 100.400.000 |
| `11010` | D.G. DE SEGURIDAD, PROTECCIÓN CIVIL Y FORMACIÓN | 96.532.010 |
| `5011` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 93.699.621 |
| `16010` | D.G. DE MEDIO AMBIENTE Y SOSTENIBILIDAD | 88.656.618 |
| `19001` | S.G.T. DE POLÍTICAS SOCIALES Y FAMILIA | 76.913.421 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 55.807.549 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 55.426.096 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 52.882.493 |
| `11001` | S.G.T. DE LA VICEPRESIDENCIA, CONSEJERÍA DE | 40.566.979 |
| `4014` | D.G. DE DEPORTES | 39.754.019 |
| `12016` | D.G. DE TRIBUTOS | 33.684.491 |
| `1001` | ASAMBLEA DE MADRID | 32.127.600 |
| `12017` | D.G. DE CONTRATACIÓN, PATRIMONIO Y TESORERÍA | 27.814.598 |
| `16001` | S.G.T. DE MEDIO AMBIENTE Y ORDENACIÓN DEL | 26.191.918 |
| `12018` | INTERVENCIÓN GENERAL | 21.196.032 |
| … | *resto: 26 códigos* | 229.700.026 |

</details>

### 2021

*Fuente: `libro_03.pdf` · 80 líneas · total extraído **22.776,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.066,70 M€ (8.066.704.298 €) · 3 códigos · 35,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 7.930.064.052 | 98,3 % |
| `17012` | D.G. DE SALUD PÚBLICA | 97.919.046 | 1,2 % |
| `17001` | S.G.T. DE SANIDAD | 38.721.200 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.487,48 M€ (2.487.484.407 €) · 6 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE BECAS Y AYUDAS AL ESTUDIO | 1.244.401.888 | 50,0 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSEÑANZAS ARTÍSTICAS | 988.086.344 | 39,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y SECUNDARIA | 157.168.100 | 6,3 % |
| `5104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 38.544.669 | 1,5 % |
| `15001` | S.G.T. DE EDUCACIÓN E INVESTIGACIÓN | 31.462.944 | 1,3 % |
| `15011` | D.G. DE FORMACIÓN PROFESIONAL Y ENSEÑANZAS DE | 27.820.462 | 1,1 % |

</details>

<details open><summary><b><code>soberania</code> — 48,40 M€ (48.402.728 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 48.402.728 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,34 M€ (1.338.573 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.338.573 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 348,90 M€ (348.895.987 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 223.708.273 | 64,1 % |
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 78.326.673 | 22,4 % |
| `16012` | D.G. DE URBANISMO Y SUELO | 30.726.065 | 8,8 % |
| `14001` | S.G.T. DE TRANSPORTES, VIVIENDA E | 16.134.976 | 4,6 % |

</details>

<details open><summary><b><code>empleo</code> — 500,76 M€ (500.762.141 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 228.712.505 | 45,7 % |
| `12001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 204.878.735 | 40,9 % |
| `20002` | VICECONSEJERÍA DE HACIENDA Y EMPLEO | 34.892.127 | 7,0 % |
| `20001` | S.G.T. DE ECONOMÍA, EMPLEO Y HACIENDA | 32.278.774 | 6,4 % |

</details>

<details open><summary><b><code>idi</code> — 154,24 M€ (154.239.111 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN | 115.577.668 | 74,9 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 21.776.614 | 14,1 % |
| `17010` | D.G. DE PLANIFICACIÓN, INVESTIGACIÓN Y FORMACIÓN | 16.884.829 | 10,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.324,04 M€ (1.324.040.720 €) · 3 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN A LA DEPENDENCIA Y AL MAYOR | 699.339.471 | 52,8 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 388.908.318 | 29,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN SOCIAL | 235.792.931 | 17,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 341,82 M€ (341.816.832 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 341.816.832 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,92 M€ (47.918.752 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 24.437.277 | 51,0 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTES | 23.481.475 | 49,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 24,87 M€ (24.865.106 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 24.865.106 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 9.430,15 M€ · 51 códigos · 41,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.371.532.091 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.228.439.108 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.394.254.493 |
| `5010` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 365.672.016 |
| `14012` | D.G. DE CARRETERAS E INFRAESTRUCTURAS | 213.017.273 |
| `11021` | D.G. DE ADMINISTRACIÓN LOCAL | 193.051.452 |
| `20017` | D.G. DE FORMACIÓN | 170.311.016 |
| `11011` | D.G. DE EMERGENCIAS | 161.933.072 |
| `26001` | CRÉDITOS CENTRALIZADOS | 144.679.108 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 115.906.409 |
| `30001` | FONDO DE CONTINGENCIA | 100.400.000 |
| `11010` | D.G. DE SEGURIDAD, PROTECCIÓN CIVIL Y FORMACIÓN | 96.532.010 |
| `5011` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 93.699.621 |
| `16010` | D.G. DE MEDIO AMBIENTE Y SOSTENIBILIDAD | 88.656.618 |
| `19001` | S.G.T. DE POLÍTICAS SOCIALES Y FAMILIA | 76.913.421 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 55.807.549 |
| `19017` | D.G. DE LA FAMILIA Y EL MENOR | 55.426.096 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 52.882.493 |
| `11001` | S.G.T. DE LA VICEPRESIDENCIA, CONSEJERÍA DE | 40.566.979 |
| `4014` | D.G. DE DEPORTES | 39.754.019 |
| `12016` | D.G. DE TRIBUTOS | 33.684.491 |
| `1001` | ASAMBLEA DE MADRID | 32.127.600 |
| `12017` | D.G. DE CONTRATACIÓN, PATRIMONIO Y TESORERÍA | 27.814.598 |
| `16001` | S.G.T. DE MEDIO AMBIENTE Y ORDENACIÓN DEL | 26.191.918 |
| `12018` | INTERVENCIÓN GENERAL | 21.196.032 |
| … | *resto: 26 códigos* | 229.700.026 |

</details>

### 2022

*Fuente: `libro_03.pdf` · 89 líneas · total extraído **25.900,85 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.759,66 M€ (8.759.661.476 €) · 4 códigos · 33,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 8.542.142.261 | 97,5 % |
| `17012` | D.G. DE SALUD PÚBLICA | 158.527.645 | 1,8 % |
| `17001` | S.G.T. DE SANIDAD | 37.211.396 | 0,4 % |
| `17011` | D.G. DE INSPECCIÓN Y ORDENACIÓN SANITARIA | 21.780.174 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 2.825,10 M€ (2.825.098.365 €) · 7 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE EDUCACIÓN CONCERTADA, BECAS Y AYUDAS AL | 1.352.252.824 | 47,9 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSEÑANZAS ARTÍSTICAS | 1.055.248.824 | 37,4 % |
| `15011` | D.G. DE EDUCACIÓN SECUNDARIA, FORMACIÓN | 159.634.075 | 5,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y ESPECIAL | 111.839.308 | 4,0 % |
| `15020` | D.G. DE BILINGÜISMO Y CALIDAD DE LA ENSEÑANZA | 73.668.052 | 2,6 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 39.911.751 | 1,4 % |
| `15001` | S.G.T. DE EDUCACIÓN, UNIVERSIDADES, CIENCIA Y | 32.543.531 | 1,2 % |

</details>

<details open><summary><b><code>soberania</code> — 59,61 M€ (59.609.524 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 59.609.524 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,58 M€ (1.577.295 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.577.295 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 292,39 M€ (292.387.981 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 151.980.711 | 52,0 % |
| `16019` | D.G. DE VIVIENDA Y REHABILITACIÓN | 102.658.078 | 35,1 % |
| `16001` | S.G.T. DE MEDIO AMBIENTE, VIVIENDA Y AGRICULTURA | 27.773.681 | 9,5 % |
| `16012` | D.G. DE URBANISMO | 9.975.511 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 427,31 M€ (427.309.249 €) · 3 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 355.681.255 | 83,2 % |
| `12001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 38.375.848 | 9,0 % |
| `20001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 33.252.146 | 7,8 % |

</details>

<details open><summary><b><code>idi</code> — 229,00 M€ (229.000.297 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN TECNOLÓGICA | 172.660.419 | 75,4 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 23.385.342 | 10,2 % |
| `17010` | D.G. DE INVESTIGACIÓN, DOCENCIA Y DOCUMENTACIÓN | 22.124.536 | 9,7 % |
| `19020` | D.G. DE EVALUACIÓN, CALIDAD E INNOVACIÓN | 10.830.000 | 4,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.468,15 M€ (1.468.148.434 €) · 3 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN AL MAYOR Y A LA DEPENDENCIA | 856.769.771 | 58,4 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 441.250.495 | 30,1 % |
| `19010` | D.G. DE SERVICIOS SOCIALES | 170.128.168 | 11,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 426,66 M€ (426.658.876 €) · 1 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 426.658.876 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 94,51 M€ (94.511.353 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 71.660.709 | 75,8 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTE | 22.850.644 | 24,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 32,81 M€ (32.807.176 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE IGUALDAD | 32.807.176 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 11.284,08 M€ · 58 códigos · 43,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.614.057.915 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.537.980.921 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.613.361.394 |
| `26001` | CRÉDITOS CENTRALIZADOS | 408.314.756 |
| `11022` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 392.146.564 |
| `7001` | S.G.T. DE ADMINISTRACIÓN LOCAL Y DIGITALIZACIÓN | 250.758.133 |
| `20017` | D.G. DE FORMACIÓN | 235.204.293 |
| `14012` | D.G. DE CARRETERAS | 218.996.960 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 186.400.887 |
| `11011` | D.G. DE EMERGENCIAS | 180.392.193 |
| `7011` | D.G. DE INVERSIONES Y DESARROLLO LOCAL | 170.724.570 |
| `30001` | FONDO DE CONTINGENCIA | 114.219.556 |
| `19017` | D.G. DE INFANCIA, FAMILIA Y FOMENTO DE LA NATALIDAD | 105.642.033 |
| `11023` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 100.864.214 |
| `14013` | D.G. DE INFRAESTRUCTURAS | 85.637.123 |
| `16017` | D.G.DE ECONOMÍA CIRCULAR | 82.442.394 |
| `15002` | VICECONSEJERÍA DE ORGANIZACIÓN EDUCATIVA | 77.898.431 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 77.117.795 |
| `12027` | D.G. DE AUTÓNOMOS Y EMPRENDIMIENTO | 72.874.455 |
| `19001` | S.G.T. DE FAMILIA, JUVENTUD Y POLÍTICA SOCIAL | 67.586.574 |
| `19019` | D.G. DE INTEGRACIÓN | 62.748.699 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 59.498.558 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA E INTERIOR | 49.189.424 |
| `4014` | D.G. DE DEPORTES | 43.742.839 |
| `16010` | D.G. DE BIODIVERSIDAD Y RECURSOS NATURALES | 42.379.809 |
| … | *resto: 33 códigos* | 433.895.396 |

</details>

### 2023

*Fuente: `libro_03.pdf` · 89 líneas · total extraído **25.900,85 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.759,66 M€ (8.759.661.476 €) · 4 códigos · 33,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 8.542.142.261 | 97,5 % |
| `17012` | D.G. DE SALUD PÚBLICA | 158.527.645 | 1,8 % |
| `17001` | S.G.T. DE SANIDAD | 37.211.396 | 0,4 % |
| `17011` | D.G. DE INSPECCIÓN Y ORDENACIÓN SANITARIA | 21.780.174 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 2.825,10 M€ (2.825.098.365 €) · 7 códigos · 10,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE EDUCACIÓN CONCERTADA, BECAS Y AYUDAS AL | 1.352.252.824 | 47,9 % |
| `15014` | D.G. DE UNIVERSIDADES Y ENSEÑANZAS ARTÍSTICAS | 1.055.248.824 | 37,4 % |
| `15011` | D.G. DE EDUCACIÓN SECUNDARIA, FORMACIÓN | 159.634.075 | 5,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y ESPECIAL | 111.839.308 | 4,0 % |
| `15020` | D.G. DE BILINGÜISMO Y CALIDAD DE LA ENSEÑANZA | 73.668.052 | 2,6 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 39.911.751 | 1,4 % |
| `15001` | S.G.T. DE EDUCACIÓN, UNIVERSIDADES, CIENCIA Y | 32.543.531 | 1,2 % |

</details>

<details open><summary><b><code>soberania</code> — 59,61 M€ (59.609.524 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 59.609.524 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 1,58 M€ (1.577.295 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.577.295 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 292,39 M€ (292.387.981 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 151.980.711 | 52,0 % |
| `16019` | D.G. DE VIVIENDA Y REHABILITACIÓN | 102.658.078 | 35,1 % |
| `16001` | S.G.T. DE MEDIO AMBIENTE, VIVIENDA Y AGRICULTURA | 27.773.681 | 9,5 % |
| `16012` | D.G. DE URBANISMO | 9.975.511 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 427,31 M€ (427.309.249 €) · 3 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 355.681.255 | 83,2 % |
| `12001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 38.375.848 | 9,0 % |
| `20001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 33.252.146 | 7,8 % |

</details>

<details open><summary><b><code>idi</code> — 229,00 M€ (229.000.297 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN TECNOLÓGICA | 172.660.419 | 75,4 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 23.385.342 | 10,2 % |
| `17010` | D.G. DE INVESTIGACIÓN, DOCENCIA Y DOCUMENTACIÓN | 22.124.536 | 9,7 % |
| `19020` | D.G. DE EVALUACIÓN, CALIDAD E INNOVACIÓN | 10.830.000 | 4,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.468,15 M€ (1.468.148.434 €) · 3 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN AL MAYOR Y A LA DEPENDENCIA | 856.769.771 | 58,4 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 441.250.495 | 30,1 % |
| `19010` | D.G. DE SERVICIOS SOCIALES | 170.128.168 | 11,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 426,66 M€ (426.658.876 €) · 1 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 426.658.876 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 94,51 M€ (94.511.353 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO | 71.660.709 | 75,8 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTE | 22.850.644 | 24,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 32,81 M€ (32.807.176 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE IGUALDAD | 32.807.176 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 11.284,08 M€ · 58 códigos · 43,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.614.057.915 |
| `15016` | D.G. DE RECURSOS HUMANOS | 2.537.980.921 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.613.361.394 |
| `26001` | CRÉDITOS CENTRALIZADOS | 408.314.756 |
| `11022` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 392.146.564 |
| `7001` | S.G.T. DE ADMINISTRACIÓN LOCAL Y DIGITALIZACIÓN | 250.758.133 |
| `20017` | D.G. DE FORMACIÓN | 235.204.293 |
| `14012` | D.G. DE CARRETERAS | 218.996.960 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 186.400.887 |
| `11011` | D.G. DE EMERGENCIAS | 180.392.193 |
| `7011` | D.G. DE INVERSIONES Y DESARROLLO LOCAL | 170.724.570 |
| `30001` | FONDO DE CONTINGENCIA | 114.219.556 |
| `19017` | D.G. DE INFANCIA, FAMILIA Y FOMENTO DE LA NATALIDAD | 105.642.033 |
| `11023` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 100.864.214 |
| `14013` | D.G. DE INFRAESTRUCTURAS | 85.637.123 |
| `16017` | D.G.DE ECONOMÍA CIRCULAR | 82.442.394 |
| `15002` | VICECONSEJERÍA DE ORGANIZACIÓN EDUCATIVA | 77.898.431 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 77.117.795 |
| `12027` | D.G. DE AUTÓNOMOS Y EMPRENDIMIENTO | 72.874.455 |
| `19001` | S.G.T. DE FAMILIA, JUVENTUD Y POLÍTICA SOCIAL | 67.586.574 |
| `19019` | D.G. DE INTEGRACIÓN | 62.748.699 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 59.498.558 |
| `11001` | S.G.T. DE PRESIDENCIA, JUSTICIA E INTERIOR | 49.189.424 |
| `4014` | D.G. DE DEPORTES | 43.742.839 |
| `16010` | D.G. DE BIODIVERSIDAD Y RECURSOS NATURALES | 42.379.809 |
| … | *resto: 33 códigos* | 433.895.396 |

</details>

### 2024

*Fuente: `libro_03.pdf` · 87 líneas · total extraído **30.446,56 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 10.211,96 M€ (10.211.960.772 €) · 5 códigos · 33,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 9.892.812.792 | 96,9 % |
| `17012` | D.G. DE SALUD PÚBLICA | 187.604.891 | 1,8 % |
| `7013` | D.G.SALUD DIGITAL | 75.507.883 | 0,7 % |
| `17001` | S.G.T. DE SANIDAD | 31.873.003 | 0,3 % |
| `17011` | D.G. DE INSPECCIÓN Y ORDENACIÓN SANITARIA | 24.162.203 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 3.071,36 M€ (3.071.356.976 €) · 8 códigos · 10,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE EDUCACIÓN CONCERTADA, BECAS Y AYUDAS AL | 1.579.209.121 | 51,4 % |
| `15014` | D.G. DE UNIVERSIDADES | 1.116.901.468 | 36,4 % |
| `15011` | D.G. DE EDUCACIÓN SECUNDARIA, FORMACIÓN | 125.620.659 | 4,1 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y ESPECIAL | 116.415.575 | 3,8 % |
| `15020` | D.G. DE BILINGÜISMO Y CALIDAD DE LA ENSEÑANZA | 45.998.236 | 1,5 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 43.227.973 | 1,4 % |
| `15001` | S.G.T. DE EDUCACIÓN, CIENCIA Y UNIVERSIDADES | 33.420.783 | 1,1 % |
| `15022` | D.G.ENSEÑANZAS ARTÍSTICAS | 10.563.161 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 98,21 M€ (98.207.107 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 63.137.611 | 64,3 % |
| `16001` | S.G.T. DE MEDIO AMBIENTE,AGRICULTURA E INTERIOR | 35.069.496 | 35,7 % |

</details>

<details open><summary><b><code>direccion</code> — 1,57 M€ (1.566.385 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.566.385 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 551,30 M€ (551.302.388 €) · 4 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 335.458.834 | 60,8 % |
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 182.012.480 | 33,0 % |
| `14001` | S.G.T. DE VIVIENDA,TRANSPORTES E | 22.425.468 | 4,1 % |
| `16012` | D.G. DE URBANISMO | 11.405.606 | 2,1 % |

</details>

<details open><summary><b><code>empleo</code> — 408,11 M€ (408.113.125 €) · 3 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 328.483.601 | 80,5 % |
| `12001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 43.320.264 | 10,6 % |
| `20001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 36.309.260 | 8,9 % |

</details>

<details open><summary><b><code>idi</code> — 220,66 M€ (220.655.159 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN TECNOLÓGICA | 160.070.998 | 72,5 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 26.037.471 | 11,8 % |
| `17010` | D.G. DE INVESTIGACIÓN Y DOCENCIA | 20.295.448 | 9,2 % |
| `19020` | D.G. DE EVALUACIÓN, CALIDAD E INNOVACIÓN | 14.251.242 | 6,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.809,83 M€ (1.809.832.916 €) · 3 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN AL MAYOR Y A LA DEPENDENCIA | 1.110.193.047 | 61,3 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 518.567.272 | 28,7 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN | 181.072.597 | 10,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 450,66 M€ (450.655.867 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 450.655.867 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 103,61 M€ (103.610.599 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO Y HOSTELERIA | 76.311.934 | 73,7 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTE | 27.298.665 | 26,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 40,54 M€ (40.535.484 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE IGUALDAD | 40.535.484 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 13.478,76 M€ · 53 códigos · 44,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.974.627.396 |
| `15016` | D.G. DE RECURSOS HUMANOS | 3.032.210.080 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.982.046.003 |
| `26001` | CRÉDITOS CENTRALIZADOS | 766.941.179 |
| `11022` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 430.917.063 |
| `16120` | AGENCIA DE SEGURIDAD Y EMERGENCIAS MADRID | 336.256.351 |
| `7001` | S.G.T. DE DIGITALIZACIÓN | 331.753.040 |
| `14013` | D.G. DE INFRAESTRUCTURAS DE TRANSPORTE | 284.224.326 |
| `20017` | D.G. DE FORMACIÓN | 269.998.950 |
| `14012` | D.G. DE CARRETERAS | 232.532.171 |
| `11021` | D.G. DE INVERSIONES Y DESARROLLO LOCAL | 206.273.149 |
| `19017` | D.G. DE INFANCIA, FAMILIA Y FOMENTO DE LA NATALIDAD | 205.835.759 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 171.438.854 |
| `11023` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 115.474.965 |
| `16015` | D.G.DE TRANSICIÓN ENERGÉTICA Y ECONOMÍA CIRCULAR | 106.970.442 |
| `7012` | D.G. DE ESTRATEGIA DIGITAL | 105.293.644 |
| `4010` | D.G. DE PROMOCIÓN CULTURAL | 86.140.589 |
| `19001` | S.G.T. DE FAMILIA,JUVENTUD Y ASUNTOS SOCIALES | 66.188.926 |
| `12027` | D.G. DE AUTÓNOMOS Y EMPRENDIMIENTO | 65.837.540 |
| `4011` | D.G. DE PATRIMONIO CULTURAL | 64.115.877 |
| `11001` | S.G.T. DE PRESIDENCIA,JUSTICIA Y ADMINISTRACIÓN | 60.918.796 |
| `4014` | D.G. DE DEPORTES | 57.712.983 |
| `14010` | D.G. DE TRANSPORTES Y MOVILIDAD | 51.449.294 |
| `16010` | D.G. DE BIODIVERSIDAD Y GESTIÓN FORESTAL | 45.152.175 |
| `1001` | ASAMBLEA DE MADRID | 40.190.190 |
| … | *resto: 28 códigos* | 388.258.810 |

</details>

### 2025

*Fuente: `libro_03.pdf` · 88 líneas · total extraído **31.453,01 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 10.542,86 M€ (10.542.858.597 €) · 6 códigos · 33,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 9.765.150.409 | 92,6 % |
| `17119` | AGENCIA DE CONTRATACIÓN SANITARIA DE LA | 411.520.871 | 3,9 % |
| `17012` | D.G. DE SALUD PÚBLICA | 198.520.952 | 1,9 % |
| `7013` | D.G.SALUD DIGITAL | 107.134.699 | 1,0 % |
| `17001` | S.G.T. DE SANIDAD | 33.199.545 | 0,3 % |
| `17011` | D.G. DE INSPECCIÓN Y ORDENACIÓN SANITARIA | 27.332.121 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 3.178,68 M€ (3.178.683.222 €) · 8 códigos · 10,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE EDUCACIÓN CONCERTADA, BECAS Y AYUDAS AL | 1.618.681.751 | 50,9 % |
| `15014` | D.G. DE UNIVERSIDADES | 1.164.369.999 | 36,6 % |
| `15011` | D.G. DE EDUCACIÓN SECUNDARIA, FORMACIÓN | 128.411.063 | 4,0 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y ESPECIAL | 121.046.715 | 3,8 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 54.919.068 | 1,7 % |
| `15020` | D.G. DE BILINGÜISMO Y CALIDAD DE LA ENSEÑANZA | 44.551.558 | 1,4 % |
| `15001` | S.G.T. DE EDUCACIÓN, CIENCIA Y UNIVERSIDADES | 34.378.171 | 1,1 % |
| `15022` | D.G.ENSEÑANZAS ARTÍSTICAS | 12.324.897 | 0,4 % |

</details>

<details open><summary><b><code>soberania</code> — 100,15 M€ (100.152.638 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 63.633.079 | 63,5 % |
| `16001` | S.G.T. DE MEDIO AMBIENTE,AGRICULTURA E INTERIOR | 36.519.559 | 36,5 % |

</details>

<details open><summary><b><code>direccion</code> — 1,69 M€ (1.690.373 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.690.373 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 766,51 M€ (766.507.303 €) · 4 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 498.858.305 | 65,1 % |
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 229.249.979 | 29,9 % |
| `14001` | S.G.T. DE VIVIENDA,TRANSPORTES E | 23.435.135 | 3,1 % |
| `16012` | D.G. DE URBANISMO | 14.963.884 | 2,0 % |

</details>

<details open><summary><b><code>empleo</code> — 439,50 M€ (439.503.747 €) · 3 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 354.460.441 | 80,7 % |
| `12001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 46.805.323 | 10,6 % |
| `20001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 38.237.983 | 8,7 % |

</details>

<details open><summary><b><code>idi</code> — 238,63 M€ (238.625.438 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN TECNOLÓGICA | 177.627.902 | 74,4 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 29.146.624 | 12,2 % |
| `17010` | D.G. DE INVESTIGACIÓN Y DOCENCIA | 21.298.248 | 8,9 % |
| `19020` | D.G. DE EVALUACIÓN, CALIDAD E INNOVACIÓN | 10.552.664 | 4,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.882,52 M€ (1.882.516.974 €) · 3 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN AL MAYOR Y A LA DEPENDENCIA | 1.193.073.490 | 63,4 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 515.212.040 | 27,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN | 174.231.444 | 9,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 450,97 M€ (450.974.972 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 450.974.972 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 87,29 M€ (87.289.160 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO Y HOSTELERIA | 58.827.686 | 67,4 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTE | 28.461.474 | 32,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 39,85 M€ (39.849.524 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE IGUALDAD | 39.849.524 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 13.724,36 M€ · 53 códigos · 43,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.930.625.195 |
| `15016` | D.G. DE RECURSOS HUMANOS | 3.224.280.869 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.982.485.688 |
| `26001` | CRÉDITOS CENTRALIZADOS | 578.016.501 |
| `11022` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 454.603.678 |
| `16120` | AGENCIA DE SEGURIDAD Y EMERGENCIAS MADRID | 359.953.576 |
| `7001` | S.G.T. DE DIGITALIZACIÓN | 354.325.729 |
| `14013` | D.G. DE INFRAESTRUCTURAS DE TRANSPORTE | 317.315.558 |
| `20017` | D.G. DE FORMACIÓN | 254.891.588 |
| `19017` | D.G. DE INFANCIA, FAMILIA Y FOMENTO DE LA NATALIDAD | 235.220.213 |
| `14012` | D.G. DE CARRETERAS | 227.723.528 |
| `11023` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 197.448.579 |
| `11021` | D.G. DE INVERSIONES Y DESARROLLO LOCAL | 194.798.588 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 154.679.573 |
| `16015` | D.G.DE TRANSICIÓN ENERGÉTICA Y ECONOMÍA CIRCULAR | 145.276.911 |
| `11001` | S.G.T. DE PRESIDENCIA,JUSTICIA Y ADMINISTRACIÓN | 135.132.158 |
| `7012` | D.G. DE ESTRATEGIA DIGITAL | 105.797.713 |
| `4010` | D.G. DE CULTURA E INDUSTRIAS CREATIVAS | 81.983.571 |
| `4011` | D.G. DE PATRIMONIO CULTURAL Y OFICINA DEL ESPAÑOL | 66.193.754 |
| `4014` | D.G. DE DEPORTES | 61.901.302 |
| `11024` | D.G.REEQUILIBRIO TERRITORIAL | 57.923.031 |
| `19001` | S.G.T. DE FAMILIA,JUVENTUD Y ASUNTOS SOCIALES | 56.411.760 |
| `16010` | D.G. DE BIODIVERSIDAD Y GESTIÓN FORESTAL | 50.612.826 |
| `14010` | D.G. DE TRANSPORTES Y MOVILIDAD | 42.355.206 |
| `12027` | D.G. DE AUTÓNOMOS Y EMPRENDIMIENTO | 41.815.400 |
| … | *resto: 28 códigos* | 412.589.824 |

</details>

### 2026

*Fuente: `libro_03.pdf` · 88 líneas · total extraído **33.271,72 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 11.093,46 M€ (11.093.460.615 €) · 6 códigos · 33,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `17118` | SERVICIO MADRILEÑO DE SALUD | 10.103.439.518 | 91,1 % |
| `17119` | AGENCIA DE CONTRATACIÓN SANITARIA DE LA | 620.288.399 | 5,6 % |
| `17012` | D.G. DE SALUD PÚBLICA | 199.117.319 | 1,8 % |
| `7013` | D.G.SALUD DIGITAL | 110.408.904 | 1,0 % |
| `17001` | S.G.T. DE SANIDAD | 33.357.303 | 0,3 % |
| `17011` | D.G. DE INSPECCIÓN Y ORDENACIÓN SANITARIA | 26.849.172 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 3.291,30 M€ (3.291.300.291 €) · 8 códigos · 9,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15012` | D.G. DE EDUCACIÓN CONCERTADA, BECAS Y AYUDAS AL | 1.658.534.043 | 50,4 % |
| `15014` | D.G. DE UNIVERSIDADES | 1.239.667.558 | 37,7 % |
| `15010` | D.G. DE EDUCACIÓN INFANTIL, PRIMARIA Y ESPECIAL | 128.714.415 | 3,9 % |
| `15011` | D.G. DE EDUCACIÓN SECUNDARIA, FORMACIÓN | 120.632.421 | 3,7 % |
| `11104` | AGENCIA C.M. PARA LA REEDUCACIÓN Y REINSERCIÓN | 55.187.698 | 1,7 % |
| `15020` | D.G. DE BILINGÜISMO Y CALIDAD DE LA ENSEÑANZA | 41.812.244 | 1,3 % |
| `15001` | S.G.T. DE EDUCACIÓN, CIENCIA Y UNIVERSIDADES | 35.016.933 | 1,1 % |
| `15022` | D.G.ENSEÑANZAS ARTÍSTICAS | 11.734.979 | 0,4 % |

</details>

<details open><summary><b><code>soberania</code> — 104,85 M€ (104.850.437 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `16014` | D.G. DE AGRICULTURA, GANADERÍA Y ALIMENTACIÓN | 67.669.165 | 64,5 % |
| `16001` | S.G.T. DE MEDIO AMBIENTE,AGRICULTURA E INTERIOR | 37.181.272 | 35,5 % |

</details>

<details open><summary><b><code>direccion</code> — 1,72 M€ (1.715.456 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `3001` | PRESIDENCIA DE LA COMUNIDAD DE MADRID | 1.715.456 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 794,13 M€ (794.130.303 €) · 4 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `14014` | D.G. DE VIVIENDA Y REHABILITACIÓN | 509.701.935 | 64,2 % |
| `14202` | AGENCIA DE VIVIENDA SOCIAL DE LA COMUNIDAD DE | 244.398.465 | 30,8 % |
| `14001` | S.G.T. DE VIVIENDA,TRANSPORTES E | 24.356.793 | 3,1 % |
| `16012` | D.G. DE URBANISMO | 15.673.110 | 2,0 % |

</details>

<details open><summary><b><code>empleo</code> — 437,51 M€ (437.514.295 €) · 3 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `20015` | D.G. DEL SERVICIO PÚBLICO DE EMPLEO | 351.803.506 | 80,4 % |
| `12001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 47.934.446 | 11,0 % |
| `20001` | S.G.T. DE ECONOMÍA, HACIENDA Y EMPLEO | 37.776.343 | 8,6 % |

</details>

<details open><summary><b><code>idi</code> — 246,70 M€ (246.701.357 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `15019` | D.G. DE INVESTIGACIÓN E INNOVACIÓN TECNOLÓGICA | 181.030.318 | 73,4 % |
| `16206` | INSTITUTO MADRILEÑO DE INVESTIGACIÓN Y | 30.366.528 | 12,3 % |
| `17010` | D.G. DE INVESTIGACIÓN Y DOCENCIA | 23.854.925 | 9,7 % |
| `19020` | D.G. DE EVALUACIÓN, CALIDAD E INNOVACIÓN | 11.449.586 | 4,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.043,28 M€ (2.043.283.812 €) · 3 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19011` | D.G. DE ATENCIÓN AL MAYOR Y A LA DEPENDENCIA | 1.344.267.636 | 65,8 % |
| `19102` | AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL | 519.654.522 | 25,4 % |
| `19010` | D.G. DE SERVICIOS SOCIALES E INTEGRACIÓN | 179.361.654 | 8,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 497,64 M€ (497.641.026 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19012` | D.G. DE ATENCIÓN A PERSONAS CON DISCAPACIDAD | 497.641.026 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 85,63 M€ (85.630.459 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `4012` | D.G. DE TURISMO Y HOSTELERIA | 57.406.038 | 67,0 % |
| `4001` | S.G.T. DE CULTURA, TURISMO Y DEPORTE | 28.224.421 | 33,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 38,27 M€ (38.265.006 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `19013` | D.G. DE LA MUJER | 38.265.006 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 14.637,23 M€ · 53 códigos · 44,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `25001` | DEUDA PÚBLICA | 3.802.922.852 |
| `15016` | D.G. DE RECURSOS HUMANOS | 3.368.330.403 |
| `14203` | CONSORCIO REGIONAL DE TRANSPORTES | 1.982.541.287 |
| `26001` | CRÉDITOS CENTRALIZADOS | 1.171.042.073 |
| `11022` | D.G. DE RECURSOS HUMANOS Y RELACIONES CON LA | 466.768.103 |
| `16120` | AGENCIA DE SEGURIDAD Y EMERGENCIAS MADRID | 409.781.567 |
| `7001` | S.G.T. DE DIGITALIZACIÓN | 370.903.289 |
| `14013` | D.G. DE INFRAESTRUCTURAS DE TRANSPORTE | 312.307.826 |
| `20017` | D.G. DE FORMACIÓN | 274.016.310 |
| `14012` | D.G. DE CARRETERAS | 246.831.725 |
| `19017` | D.G. DE INFANCIA, FAMILIA Y FOMENTO DE LA NATALIDAD | 241.717.724 |
| `11021` | D.G. DE INVERSIONES Y DESARROLLO LOCAL | 231.127.043 |
| `11023` | D.G. DE INFRAESTRUCTURAS JUDICIALES | 222.636.498 |
| `30001` | FONDO DE CONTINGENCIA | 153.285.694 |
| `15015` | D.G. DE INFRAESTRUCTURAS Y SERVICIOS | 152.782.898 |
| `16015` | D.G.DE TRANSICIÓN ENERGÉTICA Y ECONOMÍA CIRCULAR | 148.666.813 |
| `11001` | S.G.T. DE PRESIDENCIA,JUSTICIA Y ADMINISTRACIÓN | 141.623.389 |
| `4010` | D.G. DE CULTURA E INDUSTRIAS CREATIVAS | 86.464.426 |
| `12026` | D.G. DE ECONOMÍA E INDUSTRIA | 67.514.978 |
| `4011` | D.G. DE PATRIMONIO CULTURAL Y OFICINA DEL ESPAÑOL | 67.498.050 |
| `11024` | D.G.REEQUILIBRIO TERRITORIAL | 63.065.669 |
| `4014` | D.G. DE DEPORTES | 55.218.787 |
| `19001` | S.G.T. DE FAMILIA,JUVENTUD Y ASUNTOS SOCIALES | 53.898.571 |
| `7012` | D.G. DE ESTRATEGIA DIGITAL | 52.750.235 |
| `16010` | D.G. DE BIODIVERSIDAD Y GESTIÓN FORESTAL | 51.382.767 |
| … | *resto: 28 códigos* | 442.150.178 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py mad     # regenera este documento
python3 tools/auditoria_magnitud.py mad        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa mad --anio <año> \
    --input ../fuentes/raw/mad/<año>/<fichero> --output /tmp/mad.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-mad.md`](limitaciones-mad.md)

