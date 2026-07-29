# Trazabilidad de la extracción — Cataluña (`cat`)

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
| **2015** | 96 | `vol_p_eid.pdf` | 12 | 40,6 % | 32.483,09 | — | no_aplica |
| **2016** | 94 | `vol_p_eid.pdf` | 12 | 41,5 % | 33.645,40 | — | no_aplica |
| **2017** | 94 | `vol_p_eid.pdf` | 12 | 41,5 % | 33.936,97 | — | no_aplica |
| **2018** | 94 | `vol_p_eid.pdf` | 12 | 41,5 % | 33.936,97 | sí | no_aplica |
| **2019** | 97 | `vol_p_eid.pdf` | 12 | 40,2 % | 38.081,66 | — | no_aplica |
| **2020** | 97 | `vol_p_eid.pdf` | 12 | 40,2 % | 42.073,28 | — | no_aplica |
| **2021** | 97 | `vol_p_eid.pdf` | 12 | 40,2 % | 42.073,28 | sí | no_aplica |
| **2022** | 99 | `vol_p_eid.pdf` | 12 | 39,4 % | 48.752,98 | — | no_aplica |
| **2023** | 99 | `vol_p_eid.pdf` | 12 | 39,4 % | 51.526,28 | — | no_aplica |
| **2024** | 99 | `vol_p_eid.pdf` | 12 | 39,4 % | 51.537,28 | — | no_aplica |
| **2025** | 99 | `vol_p_eid.pdf` | 12 | 39,4 % | 51.537,28 | sí | no_aplica |
| **2026** | 101 | `vol_p_eid.pdf` | 12 | 38,6 % | 56.815,49 | — | no_aplica |

**URL(s) de origen:**
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2015/pdf/VOL_P_RES.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2016/pdf/VOL_P_RES.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2017/pdf/VOL_L_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2019/pdf/VOL_P_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2020/pdf/VOL_P_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2022/pdf/VOL_P_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2023/pdf/VOL_P_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2024/pdf/VOL_P_EID.pdf>
- <https://aplicacions.economia.gencat.cat/wpres/AppPHP/2026/pdf/VOL_P_EID.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 8.313,92 | 8.606,86 | 8.740,40 | 8.740,40 | 9.265,06 | 9.636,62 | 9.636,62 | 10.573,23 | 11.540,80 | 11.959,08 | 11.959,08 | 13.272,16 |
| `educacion` | 5.130,68 | 5.423,14 | 5.628,22 | 5.628,22 | 6.195,00 | 6.628,90 | 6.628,90 | 7.687,71 | 8.023,06 | 8.389,13 | 8.389,13 | 9.270,14 |
| `soberania` | 3.428,43 | 3.547,32 | 3.837,35 | 3.837,35 | 4.066,20 | 4.210,51 | 4.210,51 | 4.954,80 | 5.235,44 | 5.435,60 | 5.435,60 | 6.860,04 |
| `direccion` | 0,17 | 0,14 | 0,58 | 0,58 | 0,54 | 0,68 | 0,68 | 1,75 | 3,40 | 2,94 | 2,94 | 3,47 |
| `vivienda` | 161,71 | 182,03 | 178,15 | 178,15 | 189,02 | 242,92 | 242,92 | 657,63 | 502,09 | 436,40 | 436,40 | 527,64 |
| `empleo` | 556,53 | 761,13 | 723,03 | 723,03 | 890,95 | 921,40 | 921,40 | 885,33 | 950,06 | 894,79 | 894,79 | 927,54 |
| `idi` | 323,17 | 356,67 | 388,80 | 388,80 | 443,01 | 459,59 | 459,59 | 608,78 | 660,26 | 681,11 | 681,11 | 844,52 |
| `dependencia` | 1.440,37 | 1.482,98 | 1.491,40 | 1.491,40 | 1.531,77 | 1.594,18 | 1.594,18 | 1.749,98 | 1.969,63 | 2.163,06 | 2.163,06 | 2.484,71 |
| `discapacidad` | 9,07 | 9,07 | 9,11 | 9,11 | 11,42 | 13,09 | 13,09 | 11,89 | 16,09 | 16,09 | 16,09 | 14,71 |
| `diversidad` | 5,08 | 4,42 | 5,43 | 5,43 | 6,91 | 18,37 | 18,37 | 54,49 | 63,98 | 78,50 | 78,50 | 79,03 |
| `turismo` | 74,23 | 85,15 | 96,13 | 96,13 | 111,77 | 122,42 | 122,42 | 95,36 | 126,24 | 119,95 | 119,95 | 140,73 |
| `igualdad` | 7,45 | 7,35 | 7,95 | 7,95 | 7,92 | 10,59 | 10,59 | 10,59 | 12,39 | 15,17 | 15,17 | 14,39 |
| **Σ asignado** | 19.450,81 | 20.466,24 | 21.106,54 | 21.106,54 | 22.719,56 | 23.859,29 | 23.859,29 | 27.291,54 | 29.103,44 | 30.191,83 | 30.191,83 | 34.439,07 |
| *(sin concepto)* | 13.032,28 | 13.179,17 | 12.830,43 | 12.830,43 | 15.362,10 | 18.213,99 | 18.213,99 | 21.461,44 | 22.422,84 | 21.345,45 | 21.345,45 | 22.376,42 |
| **TOTAL extraído** | 32.483,09 | 33.645,40 | 33.936,97 | 33.936,97 | 38.081,66 | 42.073,28 | 42.073,28 | 48.752,98 | 51.526,28 | 51.537,28 | 51.537,28 | 56.815,49 |

**Conceptos sin ninguna línea en toda la serie:** `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +3,5 % | +1,6 % | +0,0 % | +6,0 % | +4,0 % | +0,0 % | +9,7 % | +9,2 % | +3,6 % | +0,0 % | +11,0 % |
| `educacion` | +5,7 % | +3,8 % | +0,0 % | +10,1 % | +7,0 % | +0,0 % | +16,0 % | +4,4 % | +4,6 % | +0,0 % | +10,5 % |
| `soberania` | +3,5 % | +8,2 % | +0,0 % | +6,0 % | +3,5 % | +0,0 % | +17,7 % | +5,7 % | +3,8 % | +0,0 % | +26,2 % |
| `direccion` | −18,2 % | +328,4 % ⚠ | +0,0 % | −6,1 % | +25,9 % | +0,0 % | +155,4 % ⚠ | +94,6 % ⚠ | −13,4 % | +0,0 % | +17,8 % |
| `vivienda` | +12,6 % | −2,1 % | +0,0 % | +6,1 % | +28,5 % | +0,0 % | +170,7 % ⚠ | −23,7 % | −13,1 % | +0,0 % | +20,9 % |
| `empleo` | +36,8 % | −5,0 % | +0,0 % | +23,2 % | +3,4 % | +0,0 % | −3,9 % | +7,3 % | −5,8 % | +0,0 % | +3,7 % |
| `idi` | +10,4 % | +9,0 % | +0,0 % | +13,9 % | +3,7 % | +0,0 % | +32,5 % | +8,5 % | +3,2 % | +0,0 % | +24,0 % |
| `dependencia` | +3,0 % | +0,6 % | +0,0 % | +2,7 % | +4,1 % | +0,0 % | +9,8 % | +12,6 % | +9,8 % | +0,0 % | +14,9 % |
| `discapacidad` | +0,0 % | +0,5 % | +0,0 % | +25,3 % | +14,7 % | +0,0 % | −9,2 % | +35,3 % | +0,0 % | +0,0 % | −8,6 % |
| `diversidad` | −13,0 % | +22,8 % | +0,0 % | +27,3 % | +165,9 % ⚠ | +0,0 % | +196,6 % ⚠ | +17,4 % | +22,7 % | +0,0 % | +0,7 % |
| `turismo` | +14,7 % | +12,9 % | +0,0 % | +16,3 % | +9,5 % | +0,0 % | −22,1 % | +32,4 % | −5,0 % | +0,0 % | +17,3 % |
| `igualdad` | −1,4 % | +8,2 % | +0,0 % | −0,3 % | +33,7 % | +0,0 % | +0,0 % | +17,0 % | +22,4 % | +0,0 % | −5,1 % |
| **TOTAL** | +3,6 % | +0,9 % | +0,0 % | +12,2 % | +10,5 % | +0,0 % | +15,9 % | +5,7 % | +0,0 % | +0,0 % | +10,2 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2022 | `vivienda` | **SALTO** | 242,92 → 657,63 M€ (+170,7 % ⚠) |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `vol_p_eid.pdf` · 96 líneas · total extraído **32.483,09 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.313,92 M€ (8.313.924.579 €) · 3 códigos · 25,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` |  | 8.220.878.564 | 98,9 % |
| `414` |  | 55.376.488 | 0,7 % |
| `419` |  | 37.669.526 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 5.130,68 M€ (5.130.679.427 €) · 6 códigos · 15,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` |  | 4.199.610.181 | 81,9 % |
| `422` |  | 785.155.470 | 15,3 % |
| `424` |  | 118.514.056 | 2,3 % |
| `321` |  | 14.535.936 | 0,3 % |
| `425` |  | 12.682.784 | 0,2 % |
| `426` |  | 181.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 3.428,43 M€ (3.428.434.583 €) · 9 códigos · 10,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` |  | 3.158.017.891 | 92,1 % |
| `711` |  | 152.744.298 | 4,5 % |
| `614` |  | 48.714.881 | 1,4 % |
| `613` |  | 24.211.676 | 0,7 % |
| `612` |  | 16.611.054 | 0,5 % |
| `616` |  | 11.593.827 | 0,3 % |
| `531` |  | 10.108.877 | 0,3 % |
| `611` |  | 4.876.784 | 0,1 % |
| `335` |  | 1.555.296 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,17 M€ (165.020 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` |  | 165.020 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 161,71 M€ (161.709.895 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` |  | 138.252.084 | 85,5 % |
| `451` |  | 23.457.811 | 14,5 % |

</details>

<details open><summary><b><code>empleo</code> — 556,53 M€ (556.525.479 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` |  | 323.842.948 | 58,2 % |
| `333` |  | 232.682.531 | 41,8 % |

</details>

<details open><summary><b><code>idi</code> — 323,17 M€ (323.171.211 €) · 9 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` |  | 126.568.220 | 39,2 % |
| `661` |  | 52.635.761 | 16,3 % |
| `573` |  | 51.335.464 | 15,9 % |
| `562` |  | 33.887.560 | 10,5 % |
| `574` |  | 22.626.053 | 7,0 % |
| `572` |  | 17.691.524 | 5,5 % |
| `532` |  | 12.503.420 | 3,9 % |
| `542` |  | 5.908.088 | 1,8 % |
| `561` |  | 15.120 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.440,37 M€ (1.440.365.938 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` |  | 1.421.651.020 | 98,7 % |
| `313` |  | 18.714.918 | 1,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 9,07 M€ (9.065.264 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` |  | 9.065.264 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,08 M€ (5.077.720 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` |  | 5.077.720 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 74,23 M€ (74.233.946 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` |  | 51.468.207 | 69,3 % |
| `432` |  | 22.765.739 | 30,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,45 M€ (7.454.958 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` |  | 7.454.958 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 13.032,28 M€ · 57 códigos · 40,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` |  | 7.004.764.606 |
| `121` |  | 1.271.144.538 |
| `221` |  | 927.717.205 |
| `522` |  | 532.343.678 |
| `211` |  | 454.113.237 |
| `521` |  | 402.030.876 |
| `213` |  | 313.091.348 |
| `523` |  | 309.040.767 |
| `533` |  | 245.891.544 |
| `811` |  | 200.000.000 |
| `317` |  | 196.813.562 |
| `318` |  | 187.075.211 |
| `223` |  | 167.603.004 |
| `111` |  | 90.166.367 |
| `441` |  | 67.078.474 |
| `125` |  | 60.280.328 |
| `552` |  | 55.287.862 |
| `551` |  | 54.006.477 |
| `622` |  | 53.975.882 |
| `471` |  | 52.969.886 |
| `445` |  | 48.136.767 |
| `443` |  | 44.185.837 |
| `641` |  | 34.490.424 |
| `212` |  | 28.241.848 |
| `323` |  | 26.947.118 |
| … | *resto: 32 códigos* | 204.881.079 |

</details>

### 2016

*Fuente: `vol_p_eid.pdf` · 94 líneas · total extraído **33.645,40 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.606,86 M€ (8.606.859.146 €) · 3 códigos · 25,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 8.496.150.430 | 98,7 % |
| `414` | SALUT PÚBLICA | 74.881.966 | 0,9 % |
| `419` | ALTRES SERVEIS DE SALUT | 35.826.750 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 5.423,14 M€ (5.423.136.304 €) · 6 códigos · 16,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 4.346.966.980 | 80,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 826.344.526 | 15,2 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 139.390.333 | 2,6 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 92.695.284 | 1,7 % |
| `321` | POLÍTIQUES DE JOVENTUT | 15.339.180 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 2.400.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 3.547,32 M€ (3.547.319.084 €) · 9 códigos · 10,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.268.548.000 | 92,1 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 153.948.754 | 4,3 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 60.443.735 | 1,7 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 27.140.573 | 0,8 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 17.604.642 | 0,5 % |
| `531` | E-INFRAESTRUCTURES | 10.829.333 | 0,3 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 5.587.832 | 0,2 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 1.630.296 | 0,0 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 1.585.920 | 0,0 % |

</details>

<details open><summary><b><code>direccion</code> — 0,14 M€ (135.020 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 135.020 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 182,03 M€ (182.028.060 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 157.485.664 | 86,5 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 24.542.396 | 13,5 % |

</details>

<details open><summary><b><code>empleo</code> — 761,13 M€ (761.131.819 €) · 2 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT | 422.278.220 | 55,5 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 338.853.599 | 44,5 % |

</details>

<details open><summary><b><code>idi</code> — 356,67 M€ (356.673.042 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 132.799.903 | 37,2 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 58.918.313 | 16,5 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 52.721.821 | 14,8 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 38.904.851 | 10,9 % |
| `574` | INNOVACIÓ | 37.510.912 | 10,5 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 17.919.608 | 5,0 % |
| `532` | SOCIETAT DIGITAL | 13.097.238 | 3,7 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.785.278 | 1,3 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 15.120 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.482,98 M€ (1.482.975.719 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.463.991.259 | 98,7 % |
| `313` | SUPORT A LES FAMÍLIES | 18.984.460 | 1,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 9,07 M€ (9.065.264 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 9.065.264 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,42 M€ (4.419.610 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 4.419.610 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 85,15 M€ (85.146.541 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 53.226.979 | 62,5 % |
| `432` | BARRIS I NUCLIS ANTICS | 31.919.562 | 37,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,35 M€ (7.349.185 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 7.349.185 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 13.179,17 M€ · 55 códigos · 39,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 6.790.553.916 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.367.088.652 |
| `221` | SEGURETAT CIUTADANA | 940.713.964 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 585.003.325 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 493.687.996 |
| `521` | CARRETERES | 398.128.814 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 364.941.874 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 349.892.181 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 247.196.329 |
| `811` | FONS DE CONTINGÈNCIA | 240.000.000 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 205.007.624 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 193.256.781 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 173.129.919 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 87.963.956 |
| `441` | CREADORS I EMPRESES CULTURALS | 75.911.066 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 66.432.694 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 61.287.862 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 60.517.097 |
| `443` | PATRIMONI CULTURAL | 51.249.923 |
| `445` | GRANS INSTITUCIONS CULTURALS | 51.031.686 |
| `622` | SUPORT A LA INDÚSTRIA | 48.133.786 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 36.118.862 |
| `323` | ACCIÓ CÍVICA I VOLUNTARIAT | 27.163.940 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 26.818.778 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 22.221.145 |
| … | *resto: 30 códigos* | 215.713.291 |

</details>

### 2017

*Fuente: `vol_p_eid.pdf` · 94 líneas · total extraído **33.936,97 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 8.740,40 M€ (8.740.399.288 €) · 3 códigos · 25,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 8.563.714.525 | 98,0 % |
| `414` | SALUT PÚBLICA | 123.823.424 | 1,4 % |
| `419` | ALTRES SERVEIS DE SALUT | 52.861.339 | 0,6 % |

</details>

<details open><summary><b><code>educacion</code> — 5.628,22 M€ (5.628.219.106 €) · 6 códigos · 16,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 4.511.643.682 | 80,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 831.816.011 | 14,8 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 132.977.000 | 2,4 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 132.695.284 | 2,4 % |
| `321` | POLÍTIQUES DE JOVENTUT | 15.617.129 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 3.470.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 3.837,35 M€ (3.837.349.914 €) · 9 códigos · 11,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.268.548.000 | 85,2 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 254.310.392 | 6,6 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 155.411.026 | 4,0 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 70.827.750 | 1,8 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 57.476.549 | 1,5 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 10.369.517 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 8.297.467 | 0,2 % |
| `531` | E-INFRAESTRUCTURES | 6.986.333 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 5.122.880 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,58 M€ (578.468 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 578.468 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 178,15 M€ (178.147.546 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 152.255.150 | 85,5 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 25.892.396 | 14,5 % |

</details>

<details open><summary><b><code>empleo</code> — 723,03 M€ (723.031.947 €) · 2 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT | 395.587.678 | 54,7 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 327.444.270 | 45,3 % |

</details>

<details open><summary><b><code>idi</code> — 388,80 M€ (388.801.186 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 139.034.727 | 35,8 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 79.124.040 | 20,4 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 58.096.607 | 14,9 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 46.972.479 | 12,1 % |
| `574` | INNOVACIÓ | 24.568.306 | 6,3 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 19.255.036 | 5,0 % |
| `532` | SOCIETAT DIGITAL | 17.706.593 | 4,6 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.028.278 | 1,0 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 15.120 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.491,40 M€ (1.491.396.034 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.471.174.018 | 98,6 % |
| `313` | SUPORT A LES FAMÍLIES | 20.222.016 | 1,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 9,11 M€ (9.113.720 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 9.113.720 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,43 M€ (5.427.539 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 5.427.539 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 96,13 M€ (96.127.946 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 58.377.947 | 60,7 % |
| `432` | BARRIS I NUCLIS ANTICS | 37.749.999 | 39,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,95 M€ (7.948.185 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 7.948.185 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.830,43 M€ · 55 códigos · 37,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 5.996.140.815 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.482.884.294 |
| `221` | SEGURETAT CIUTADANA | 946.115.262 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 638.624.956 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 494.280.379 |
| `521` | CARRETERES | 420.327.091 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 357.719.429 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 356.390.526 |
| `811` | FONS DE CONTINGÈNCIA | 330.000.000 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 243.943.263 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 237.530.472 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 212.896.524 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 191.908.607 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 144.419.584 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 76.508.012 |
| `441` | CREADORS I EMPRESES CULTURALS | 74.904.887 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 72.749.371 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 61.517.097 |
| `622` | SUPORT A LA INDÚSTRIA | 54.015.439 |
| `445` | GRANS INSTITUCIONS CULTURALS | 49.456.981 |
| `443` | PATRIMONI CULTURAL | 48.626.094 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 31.408.000 |
| `323` | ACCIÓ CÍVICA I VOLUNTARIAT | 31.354.585 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 28.240.538 |
| `581` | CARTOGRAFIA, GEOLOGIA I GEOFÍSICA | 19.857.545 |
| … | *resto: 30 códigos* | 228.613.723 |

</details>

### 2018

*Fuente: `vol_p_eid.pdf` · 94 líneas · total extraído **33.936,97 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 8.740,40 M€ (8.740.399.288 €) · 3 códigos · 25,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 8.563.714.525 | 98,0 % |
| `414` | SALUT PÚBLICA | 123.823.424 | 1,4 % |
| `419` | ALTRES SERVEIS DE SALUT | 52.861.339 | 0,6 % |

</details>

<details open><summary><b><code>educacion</code> — 5.628,22 M€ (5.628.219.106 €) · 6 códigos · 16,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 4.511.643.682 | 80,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 831.816.011 | 14,8 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 132.977.000 | 2,4 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 132.695.284 | 2,4 % |
| `321` | POLÍTIQUES DE JOVENTUT | 15.617.129 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 3.470.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 3.837,35 M€ (3.837.349.914 €) · 9 códigos · 11,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.268.548.000 | 85,2 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 254.310.392 | 6,6 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 155.411.026 | 4,0 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 70.827.750 | 1,8 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 57.476.549 | 1,5 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 10.369.517 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 8.297.467 | 0,2 % |
| `531` | E-INFRAESTRUCTURES | 6.986.333 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 5.122.880 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,58 M€ (578.468 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 578.468 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 178,15 M€ (178.147.546 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 152.255.150 | 85,5 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 25.892.396 | 14,5 % |

</details>

<details open><summary><b><code>empleo</code> — 723,03 M€ (723.031.947 €) · 2 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT | 395.587.678 | 54,7 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 327.444.270 | 45,3 % |

</details>

<details open><summary><b><code>idi</code> — 388,80 M€ (388.801.186 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 139.034.727 | 35,8 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 79.124.040 | 20,4 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 58.096.607 | 14,9 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 46.972.479 | 12,1 % |
| `574` | INNOVACIÓ | 24.568.306 | 6,3 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 19.255.036 | 5,0 % |
| `532` | SOCIETAT DIGITAL | 17.706.593 | 4,6 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.028.278 | 1,0 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 15.120 | 0,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.491,40 M€ (1.491.396.034 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.471.174.018 | 98,6 % |
| `313` | SUPORT A LES FAMÍLIES | 20.222.016 | 1,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 9,11 M€ (9.113.720 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 9.113.720 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,43 M€ (5.427.539 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 5.427.539 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 96,13 M€ (96.127.946 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 58.377.947 | 60,7 % |
| `432` | BARRIS I NUCLIS ANTICS | 37.749.999 | 39,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,95 M€ (7.948.185 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 7.948.185 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 12.830,43 M€ · 55 códigos · 37,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 5.996.140.815 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.482.884.294 |
| `221` | SEGURETAT CIUTADANA | 946.115.262 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 638.624.956 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 494.280.379 |
| `521` | CARRETERES | 420.327.091 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 357.719.429 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 356.390.526 |
| `811` | FONS DE CONTINGÈNCIA | 330.000.000 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 243.943.263 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 237.530.472 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 212.896.524 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 191.908.607 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 144.419.584 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 76.508.012 |
| `441` | CREADORS I EMPRESES CULTURALS | 74.904.887 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 72.749.371 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 61.517.097 |
| `622` | SUPORT A LA INDÚSTRIA | 54.015.439 |
| `445` | GRANS INSTITUCIONS CULTURALS | 49.456.981 |
| `443` | PATRIMONI CULTURAL | 48.626.094 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 31.408.000 |
| `323` | ACCIÓ CÍVICA I VOLUNTARIAT | 31.354.585 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 28.240.538 |
| `581` | CARTOGRAFIA, GEOLOGIA I GEOFÍSICA | 19.857.545 |
| … | *resto: 30 códigos* | 228.613.723 |

</details>

### 2019

*Fuente: `vol_p_eid.pdf` · 97 líneas · total extraído **38.081,66 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.265,06 M€ (9.265.055.639 €) · 3 códigos · 24,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 9.092.525.303 | 98,1 % |
| `414` | SALUT PÚBLICA | 130.893.304 | 1,4 % |
| `419` | ALTRES SERVEIS DE SALUT | 41.637.032 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 6.195,00 M€ (6.195.003.669 €) · 6 códigos · 16,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 4.966.325.754 | 80,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 882.561.698 | 14,2 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 185.195.284 | 3,0 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 139.209.660 | 2,2 % |
| `321` | POLÍTIQUES DE JOVENTUT | 17.911.274 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 3.800.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 4.066,20 M€ (4.066.200.005 €) · 9 códigos · 10,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.405.827.016 | 83,8 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 295.941.070 | 7,3 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 160.353.054 | 3,9 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 82.118.072 | 2,0 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 74.677.588 | 1,8 % |
| `531` | E-INFRAESTRUCTURES | 24.222.799 | 0,6 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 10.376.667 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 7.898.630 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 4.785.108 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,54 M€ (543.458 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 543.458 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 189,02 M€ (189.017.634 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 160.240.239 | 84,8 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 28.777.396 | 15,2 % |

</details>

<details open><summary><b><code>empleo</code> — 890,95 M€ (890.947.322 €) · 2 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 498.945.745 | 56,0 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 392.001.578 | 44,0 % |

</details>

<details open><summary><b><code>idi</code> — 443,01 M€ (443.006.886 €) · 9 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 170.880.259 | 38,6 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 84.681.305 | 19,1 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 57.304.143 | 12,9 % |
| `532` | SOCIETAT DIGITAL | 37.669.737 | 8,5 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 35.526.442 | 8,0 % |
| `574` | INNOVACIÓ | 32.697.485 | 7,4 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 18.449.432 | 4,2 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.282.963 | 1,0 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 1.515.120 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.531,77 M€ (1.531.771.267 €) · 2 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.510.552.872 | 98,6 % |
| `313` | SUPORT A LES FAMÍLIES | 21.218.395 | 1,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 11,42 M€ (11.417.511 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 11.417.511 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,91 M€ (6.908.849 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 6.908.849 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 111,77 M€ (111.766.211 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 70.122.607 | 62,7 % |
| `432` | BARRIS I NUCLIS ANTICS | 41.643.604 | 37,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,92 M€ (7.922.235 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 7.922.235 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 15.362,10 M€ · 58 códigos · 40,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 8.009.184.346 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.672.223.974 |
| `221` | SEGURETAT CIUTADANA | 1.043.509.056 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 651.514.936 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 509.710.195 |
| `521` | CARRETERES | 435.083.199 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 434.354.746 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 370.221.469 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 287.775.331 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 274.579.056 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 264.285.052 |
| `811` | FONS DE CONTINGÈNCIA | 220.000.000 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 212.535.084 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 141.652.551 |
| `441` | CREADORS I EMPRESES CULTURALS | 79.686.453 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 79.609.510 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 75.558.100 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 73.086.964 |
| `445` | GRANS INSTITUCIONS CULTURALS | 53.175.002 |
| `443` | PATRIMONI CULTURAL | 51.732.766 |
| `622` | SUPORT A LA INDÚSTRIA | 46.891.436 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 33.608.000 |
| `310` | ALTRES PROGRAMES SOCIALS | 31.200.000 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 31.090.457 |
| `232` | COOPERACIÓ AL DESENVOLUPAMENT | 23.882.200 |
| … | *resto: 33 códigos* | 255.954.108 |

</details>

### 2020

*Fuente: `vol_p_eid.pdf` · 97 líneas · total extraído **42.073,28 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 9.636,62 M€ (9.636.622.207 €) · 3 códigos · 22,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 9.449.516.886 | 98,1 % |
| `414` | SALUT PÚBLICA | 142.380.605 | 1,5 % |
| `419` | ALTRES SERVEIS DE SALUT | 44.724.717 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 6.628,90 M€ (6.628.901.871 €) · 6 códigos · 15,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 5.284.046.786 | 79,7 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 973.972.763 | 14,7 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 185.695.284 | 2,8 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 158.607.202 | 2,4 % |
| `321` | POLÍTIQUES DE JOVENTUT | 18.414.637 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 8.165.200 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 4.210,51 M€ (4.210.510.791 €) · 9 códigos · 10,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.528.436.789 | 83,8 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 299.559.914 | 7,1 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 164.092.465 | 3,9 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 83.254.036 | 2,0 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 72.190.375 | 1,7 % |
| `531` | E-INFRAESTRUCTURES | 37.661.033 | 0,9 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 10.535.539 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 9.178.057 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 5.602.582 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,68 M€ (684.007 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 684.007 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 242,92 M€ (242.922.701 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 211.737.005 | 87,2 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 31.185.696 | 12,8 % |

</details>

<details open><summary><b><code>empleo</code> — 921,40 M€ (921.396.630 €) · 2 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 471.659.209 | 51,2 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 449.737.422 | 48,8 % |

</details>

<details open><summary><b><code>idi</code> — 459,59 M€ (459.593.955 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 166.210.654 | 36,2 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 88.024.293 | 19,2 % |
| `532` | SOCIETAT DIGITAL | 56.761.321 | 12,4 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 55.182.865 | 12,0 % |
| `574` | INNOVACIÓ | 33.275.327 | 7,2 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 31.917.085 | 6,9 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 20.214.763 | 4,4 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.489.907 | 1,0 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 3.517.739 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.594,18 M€ (1.594.179.040 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.583.364.253 | 99,3 % |
| `313` | SUPORT A LES FAMÍLIES | 10.814.786 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 13,09 M€ (13.092.933 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 13.092.933 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 18,37 M€ (18.370.367 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 18.370.367 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 122,42 M€ (122.419.935 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 83.216.207 | 68,0 % |
| `432` | BARRIS I NUCLIS ANTICS | 39.203.728 | 32,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,59 M€ (10.592.235 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 10.592.235 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 18.213,99 M€ · 58 códigos · 43,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 10.539.663.492 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.682.301.945 |
| `221` | SEGURETAT CIUTADANA | 1.099.785.668 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 668.389.008 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 537.753.798 |
| `521` | CARRETERES | 439.706.816 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 432.577.722 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 394.053.830 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 345.388.534 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 305.728.817 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 253.399.475 |
| `811` | FONS DE CONTINGÈNCIA | 250.000.000 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 242.542.711 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 145.307.930 |
| `441` | CREADORS I EMPRESES CULTURALS | 85.718.013 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 85.609.510 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 78.058.342 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 68.300.802 |
| `445` | GRANS INSTITUCIONS CULTURALS | 59.482.069 |
| `443` | PATRIMONI CULTURAL | 53.924.604 |
| `622` | SUPORT A LA INDÚSTRIA | 51.174.305 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 35.670.626 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 35.176.380 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 32.326.641 |
| `310` | ALTRES PROGRAMES SOCIALS | 31.910.000 |
| … | *resto: 33 códigos* | 260.037.825 |

</details>

### 2021

*Fuente: `vol_p_eid.pdf` · 97 líneas · total extraído **42.073,28 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 9.636,62 M€ (9.636.622.207 €) · 3 códigos · 22,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 9.449.516.886 | 98,1 % |
| `414` | SALUT PÚBLICA | 142.380.605 | 1,5 % |
| `419` | ALTRES SERVEIS DE SALUT | 44.724.717 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 6.628,90 M€ (6.628.901.871 €) · 6 códigos · 15,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 5.284.046.786 | 79,7 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 973.972.763 | 14,7 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 185.695.284 | 2,8 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 158.607.202 | 2,4 % |
| `321` | POLÍTIQUES DE JOVENTUT | 18.414.637 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 8.165.200 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 4.210,51 M€ (4.210.510.791 €) · 9 códigos · 10,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 3.528.436.789 | 83,8 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 299.559.914 | 7,1 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 164.092.465 | 3,9 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 83.254.036 | 2,0 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 72.190.375 | 1,7 % |
| `531` | E-INFRAESTRUCTURES | 37.661.033 | 0,9 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 10.535.539 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 9.178.057 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 5.602.582 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 0,68 M€ (684.007 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 684.007 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 242,92 M€ (242.922.701 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 211.737.005 | 87,2 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 31.185.696 | 12,8 % |

</details>

<details open><summary><b><code>empleo</code> — 921,40 M€ (921.396.630 €) · 2 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 471.659.209 | 51,2 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 449.737.422 | 48,8 % |

</details>

<details open><summary><b><code>idi</code> — 459,59 M€ (459.593.955 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 166.210.654 | 36,2 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 88.024.293 | 19,2 % |
| `532` | SOCIETAT DIGITAL | 56.761.321 | 12,4 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 55.182.865 | 12,0 % |
| `574` | INNOVACIÓ | 33.275.327 | 7,2 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 31.917.085 | 6,9 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 20.214.763 | 4,4 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 4.489.907 | 1,0 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 3.517.739 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.594,18 M€ (1.594.179.040 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.583.364.253 | 99,3 % |
| `313` | SUPORT A LES FAMÍLIES | 10.814.786 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 13,09 M€ (13.092.933 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 13.092.933 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 18,37 M€ (18.370.367 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 18.370.367 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 122,42 M€ (122.419.935 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 83.216.207 | 68,0 % |
| `432` | BARRIS I NUCLIS ANTICS | 39.203.728 | 32,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,59 M€ (10.592.235 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 10.592.235 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 18.213,99 M€ · 58 códigos · 43,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 10.539.663.492 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.682.301.945 |
| `221` | SEGURETAT CIUTADANA | 1.099.785.668 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 668.389.008 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 537.753.798 |
| `521` | CARRETERES | 439.706.816 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 432.577.722 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 394.053.830 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 345.388.534 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 305.728.817 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 253.399.475 |
| `811` | FONS DE CONTINGÈNCIA | 250.000.000 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 242.542.711 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 145.307.930 |
| `441` | CREADORS I EMPRESES CULTURALS | 85.718.013 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 85.609.510 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 78.058.342 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 68.300.802 |
| `445` | GRANS INSTITUCIONS CULTURALS | 59.482.069 |
| `443` | PATRIMONI CULTURAL | 53.924.604 |
| `622` | SUPORT A LA INDÚSTRIA | 51.174.305 |
| `641` | ORDENACIÓ I PROMOCIÓ DEL COMERÇ I L'ARTESANIA | 35.670.626 |
| `212` | SERVEIS DE JUSTÍCIA JUVENIL I ATENCIÓ A LES PERSON | 35.176.380 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 32.326.641 |
| `310` | ALTRES PROGRAMES SOCIALS | 31.910.000 |
| … | *resto: 33 códigos* | 260.037.825 |

</details>

### 2022

*Fuente: `vol_p_eid.pdf` · 99 líneas · total extraído **48.752,98 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 10.573,23 M€ (10.573.225.268 €) · 3 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 10.308.236.980 | 97,5 % |
| `414` | SALUT PÚBLICA | 218.468.457 | 2,1 % |
| `419` | ALTRES SERVEIS DE SALUT | 46.519.831 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 7.687,71 M€ (7.687.714.793 €) · 6 códigos · 15,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 6.114.745.225 | 79,5 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 1.046.243.046 | 13,6 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 287.220.000 | 3,7 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 213.411.061 | 2,8 % |
| `321` | POLÍTIQUES DE JOVENTUT | 18.995.461 | 0,2 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 7.100.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 4.954,80 M€ (4.954.802.029 €) · 9 códigos · 10,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 4.123.960.425 | 83,2 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 305.644.747 | 6,2 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 175.617.437 | 3,5 % |
| `531` | E-INFRAESTRUCTURES | 163.906.045 | 3,3 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 78.758.860 | 1,6 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 78.267.912 | 1,6 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 12.721.497 | 0,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 9.284.607 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 6.640.500 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 1,75 M€ (1.747.118 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 1.747.118 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 657,63 M€ (657.626.713 €) · 2 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 618.981.017 | 94,1 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 38.645.696 | 5,9 % |

</details>

<details open><summary><b><code>empleo</code> — 885,33 M€ (885.325.362 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 661.624.120 | 74,7 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 223.701.242 | 25,3 % |

</details>

<details open><summary><b><code>idi</code> — 608,78 M€ (608.782.714 €) · 9 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 249.732.522 | 41,0 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 93.153.819 | 15,3 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 78.757.622 | 12,9 % |
| `532` | SOCIETAT DIGITAL | 61.130.248 | 10,0 % |
| `574` | INNOVACIÓ | 48.395.057 | 7,9 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 25.893.499 | 4,3 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 25.839.347 | 4,2 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 19.362.862 | 3,2 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 6.517.739 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.749,98 M€ (1.749.979.173 €) · 2 códigos · 3,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.739.641.929 | 99,4 % |
| `313` | SUPORT A LES FAMÍLIES | 10.337.244 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 11,89 M€ (11.890.552 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 11.890.552 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 54,49 M€ (54.494.927 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 54.494.927 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 95,36 M€ (95.355.900 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 78.805.900 | 82,6 % |
| `432` | BARRIS I NUCLIS ANTICS | 16.550.000 | 17,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,59 M€ (10.592.285 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 10.592.285 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 21.461,44 M€ · 60 códigos · 44,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 11.389.583.314 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 1.841.996.020 |
| `221` | SEGURETAT CIUTADANA | 1.190.910.612 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 743.079.285 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 735.994.066 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 657.691.427 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 631.461.042 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 558.062.038 |
| `521` | CARRETERES | 456.451.304 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 408.925.275 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 356.008.392 |
| `811` | FONS DE CONTINGÈNCIA | 300.000.000 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 266.700.105 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 264.865.703 |
| `310` | ALTRES PROGRAMES SOCIALS | 229.185.759 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 172.430.716 |
| `631` | ENERGIA | 130.739.432 |
| `441` | CREADORS I EMPRESES CULTURALS | 123.142.227 |
| `554` | PREVENCIÓ I CONTROL AMBIENTAL | 81.347.208 |
| `124` | REGULACIÓ, CONTROL I GESTIÓ DEL JOC | 81.135.640 |
| `443` | PATRIMONI CULTURAL | 78.850.243 |
| `672` | CRÈDIT OFICIAL | 77.477.975 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 70.762.726 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 68.379.091 |
| `445` | GRANS INSTITUCIONS CULTURALS | 66.185.094 |
| … | *resto: 35 códigos* | 480.075.595 |

</details>

### 2023

*Fuente: `vol_p_eid.pdf` · 99 líneas · total extraído **51.526,28 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 11.540,80 M€ (11.540.801.007 €) · 3 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 11.286.546.568 | 97,8 % |
| `414` | SALUT PÚBLICA | 205.499.066 | 1,8 % |
| `419` | ALTRES SERVEIS DE SALUT | 48.755.373 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 8.023,06 M€ (8.023.063.296 €) · 6 códigos · 15,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 6.433.911.230 | 80,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 1.162.131.993 | 14,5 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 243.220.000 | 3,0 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 152.513.146 | 1,9 % |
| `321` | POLÍTIQUES DE JOVENTUT | 24.916.727 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 6.370.200 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 5.235,44 M€ (5.235.440.412 €) · 9 códigos · 10,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 4.346.654.288 | 83,0 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 352.105.452 | 6,7 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 196.535.348 | 3,8 % |
| `531` | E-INFRAESTRUCTURES | 111.833.513 | 2,1 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 111.403.834 | 2,1 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 89.516.541 | 1,7 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 11.251.667 | 0,2 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 9.585.092 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 6.554.677 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,40 M€ (3.399.406 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 3.399.406 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 502,09 M€ (502.086.405 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 449.776.659 | 89,6 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 52.309.746 | 10,4 % |

</details>

<details open><summary><b><code>empleo</code> — 950,06 M€ (950.063.832 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 730.778.795 | 76,9 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 219.285.037 | 23,1 % |

</details>

<details open><summary><b><code>idi</code> — 660,26 M€ (660.263.758 €) · 9 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 242.753.324 | 36,8 % |
| `532` | SOCIETAT DIGITAL | 100.515.132 | 15,2 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 97.773.642 | 14,8 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 75.284.299 | 11,4 % |
| `574` | INNOVACIÓ | 55.445.760 | 8,4 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 29.485.343 | 4,5 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 28.365.946 | 4,3 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 24.640.311 | 3,7 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 6.000.000 | 0,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 1.969,63 M€ (1.969.629.181 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 1.957.489.070 | 99,4 % |
| `313` | SUPORT A LES FAMÍLIES | 12.140.111 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 16,09 M€ (16.089.100 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 16.089.100 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 63,98 M€ (63.977.512 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 63.977.512 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 126,24 M€ (126.236.675 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 123.186.675 | 97,6 % |
| `432` | BARRIS I NUCLIS ANTICS | 3.050.000 | 2,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 12,39 M€ (12.391.009 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 12.391.009 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 22.422,84 M€ · 60 códigos · 43,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 11.417.994.424 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 2.350.185.990 |
| `221` | SEGURETAT CIUTADANA | 1.356.984.124 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 818.915.001 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 787.664.548 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 626.118.243 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 544.549.936 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 498.621.784 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 446.634.784 |
| `521` | CARRETERES | 441.763.407 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 398.655.089 |
| `811` | FONS DE CONTINGÈNCIA | 300.000.000 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 295.641.232 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 294.607.504 |
| `631` | ENERGIA | 175.566.165 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 169.496.601 |
| `441` | CREADORS I EMPRESES CULTURALS | 148.732.108 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 113.754.733 |
| `310` | ALTRES PROGRAMES SOCIALS | 105.801.460 |
| `622` | SUPORT A LA INDÚSTRIA | 101.545.330 |
| `443` | PATRIMONI CULTURAL | 97.833.094 |
| `124` | REGULACIÓ, CONTROL I GESTIÓ DEL JOC | 91.399.567 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 89.829.357 |
| `445` | GRANS INSTITUCIONS CULTURALS | 79.148.336 |
| `554` | PREVENCIÓ I CONTROL AMBIENTAL | 77.852.580 |
| … | *resto: 35 códigos* | 593.545.139 |

</details>

### 2024

*Fuente: `vol_p_eid.pdf` · 99 líneas · total extraído **51.537,28 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 11.959,08 M€ (11.959.082.591 €) · 3 códigos · 23,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 11.699.726.952 | 97,8 % |
| `414` | SALUT PÚBLICA | 212.076.043 | 1,8 % |
| `419` | ALTRES SERVEIS DE SALUT | 47.279.596 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 8.389,13 M€ (8.389.127.301 €) · 6 códigos · 16,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 6.644.716.996 | 79,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 1.242.893.385 | 14,8 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 243.868.000 | 2,9 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 229.514.304 | 2,7 % |
| `321` | POLÍTIQUES DE JOVENTUT | 25.087.616 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 3.047.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 5.435,60 M€ (5.435.604.695 €) · 9 códigos · 10,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 4.603.269.770 | 84,7 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 392.052.500 | 7,2 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 213.138.024 | 3,9 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 86.734.878 | 1,6 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 82.279.785 | 1,5 % |
| `531` | E-INFRAESTRUCTURES | 28.637.620 | 0,5 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 11.995.009 | 0,2 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 10.694.220 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 6.802.891 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,94 M€ (2.942.839 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 2.942.839 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 436,40 M€ (436.402.658 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 373.215.073 | 85,5 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 63.187.585 | 14,5 % |

</details>

<details open><summary><b><code>empleo</code> — 894,79 M€ (894.794.343 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 675.676.372 | 75,5 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 219.117.971 | 24,5 % |

</details>

<details open><summary><b><code>idi</code> — 681,11 M€ (681.107.521 €) · 9 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 248.470.936 | 36,5 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 106.233.527 | 15,6 % |
| `532` | SOCIETAT DIGITAL | 83.901.227 | 12,3 % |
| `574` | INNOVACIÓ | 72.783.563 | 10,7 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 72.004.843 | 10,6 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 33.590.711 | 4,9 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 30.608.831 | 4,5 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 28.013.883 | 4,1 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 5.500.000 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.163,06 M€ (2.163.059.091 €) · 2 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 2.151.006.572 | 99,4 % |
| `313` | SUPORT A LES FAMÍLIES | 12.052.519 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 16,09 M€ (16.089.948 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 16.089.948 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 78,50 M€ (78.502.515 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 78.502.515 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 119,95 M€ (119.952.908 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 116.902.908 | 97,5 % |
| `432` | BARRIS I NUCLIS ANTICS | 3.050.000 | 2,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 15,17 M€ (15.166.403 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 15.166.403 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 21.345,45 M€ · 60 códigos · 41,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 9.350.348.301 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 2.525.512.435 |
| `221` | SEGURETAT CIUTADANA | 1.429.621.480 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 1.121.059.261 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 857.328.762 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 820.585.525 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 626.790.032 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 565.988.995 |
| `521` | CARRETERES | 470.649.074 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 457.617.070 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 400.293.986 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 350.746.907 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 314.873.436 |
| `811` | FONS DE CONTINGÈNCIA | 300.000.000 |
| `441` | CREADORS I EMPRESES CULTURALS | 207.438.049 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 173.872.020 |
| `622` | SUPORT A LA INDÚSTRIA | 148.082.940 |
| `443` | PATRIMONI CULTURAL | 98.947.184 |
| `124` | REGULACIÓ, CONTROL I GESTIÓ DEL JOC | 91.516.410 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 88.559.694 |
| `445` | GRANS INSTITUCIONS CULTURALS | 86.633.638 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 80.794.294 |
| `631` | ENERGIA | 76.794.871 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 65.440.759 |
| `672` | CRÈDIT OFICIAL | 64.696.964 |
| … | *resto: 35 códigos* | 571.255.105 |

</details>

### 2025

*Fuente: `vol_p_eid.pdf` · 99 líneas · total extraído **51.537,28 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 11.959,08 M€ (11.959.082.591 €) · 3 códigos · 23,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 11.699.726.952 | 97,8 % |
| `414` | SALUT PÚBLICA | 212.076.043 | 1,8 % |
| `419` | ALTRES SERVEIS DE SALUT | 47.279.596 | 0,4 % |

</details>

<details open><summary><b><code>educacion</code> — 8.389,13 M€ (8.389.127.301 €) · 6 códigos · 16,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 6.644.716.996 | 79,2 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 1.242.893.385 | 14,8 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 243.868.000 | 2,9 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 229.514.304 | 2,7 % |
| `321` | POLÍTIQUES DE JOVENTUT | 25.087.616 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 3.047.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 5.435,60 M€ (5.435.604.695 €) · 9 códigos · 10,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L | 4.603.269.770 | 84,7 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 392.052.500 | 7,2 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 213.138.024 | 3,9 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 86.734.878 | 1,6 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 82.279.785 | 1,5 % |
| `531` | E-INFRAESTRUCTURES | 28.637.620 | 0,5 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 11.995.009 | 0,2 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 10.694.220 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 6.802.891 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 2,94 M€ (2.942.839 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 2.942.839 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 436,40 M€ (436.402.658 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 373.215.073 | 85,5 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 63.187.585 | 14,5 % |

</details>

<details open><summary><b><code>empleo</code> — 894,79 M€ (894.794.343 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 675.676.372 | 75,5 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 219.117.971 | 24,5 % |

</details>

<details open><summary><b><code>idi</code> — 681,11 M€ (681.107.521 €) · 9 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 248.470.936 | 36,5 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 106.233.527 | 15,6 % |
| `532` | SOCIETAT DIGITAL | 83.901.227 | 12,3 % |
| `574` | INNOVACIÓ | 72.783.563 | 10,7 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 72.004.843 | 10,6 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 33.590.711 | 4,9 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 30.608.831 | 4,5 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 28.013.883 | 4,1 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 5.500.000 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.163,06 M€ (2.163.059.091 €) · 2 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 2.151.006.572 | 99,4 % |
| `313` | SUPORT A LES FAMÍLIES | 12.052.519 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 16,09 M€ (16.089.948 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 16.089.948 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 78,50 M€ (78.502.515 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 78.502.515 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 119,95 M€ (119.952.908 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 116.902.908 | 97,5 % |
| `432` | BARRIS I NUCLIS ANTICS | 3.050.000 | 2,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 15,17 M€ (15.166.403 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 15.166.403 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 21.345,45 M€ · 60 códigos · 41,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 9.350.348.301 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 2.525.512.435 |
| `221` | SEGURETAT CIUTADANA | 1.429.621.480 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 1.121.059.261 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 857.328.762 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 820.585.525 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 626.790.032 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 565.988.995 |
| `521` | CARRETERES | 470.649.074 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 457.617.070 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 400.293.986 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 350.746.907 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 314.873.436 |
| `811` | FONS DE CONTINGÈNCIA | 300.000.000 |
| `441` | CREADORS I EMPRESES CULTURALS | 207.438.049 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 173.872.020 |
| `622` | SUPORT A LA INDÚSTRIA | 148.082.940 |
| `443` | PATRIMONI CULTURAL | 98.947.184 |
| `124` | REGULACIÓ, CONTROL I GESTIÓ DEL JOC | 91.516.410 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 88.559.694 |
| `445` | GRANS INSTITUCIONS CULTURALS | 86.633.638 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 80.794.294 |
| `631` | ENERGIA | 76.794.871 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 65.440.759 |
| `672` | CRÈDIT OFICIAL | 64.696.964 |
| … | *resto: 35 códigos* | 571.255.105 |

</details>

### 2026

*Fuente: `vol_p_eid.pdf` · 101 líneas · total extraído **56.815,49 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 13.272,16 M€ (13.272.158.515 €) · 3 códigos · 23,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415` | TRANSFERÈNCIES INTERNES PER SERVEIS DE SALUT | 12.969.257.319 | 97,7 % |
| `414` | SALUT PÚBLICA | 267.551.321 | 2,0 % |
| `419` | ALTRES SERVEIS DE SALUT | 35.349.876 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 9.270,14 M€ (9.270.136.188 €) · 6 códigos · 16,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `421` | EDUCACIÓ GENERAL | 7.318.327.759 | 78,9 % |
| `422` | EDUCACIÓ UNIVERSITÀRIA | 1.292.270.085 | 13,9 % |
| `424` | SERVEIS COMPLEMENTARIS A L'EDUCACIÓ | 311.252.633 | 3,4 % |
| `425` | BEQUES I AJUTS A L'ESTUDI | 309.420.064 | 3,3 % |
| `321` | POLÍTIQUES DE JOVENTUT | 30.504.011 | 0,3 % |
| `426` | FORMACIÓ DEL PERSONAL DOCENT | 8.361.636 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 6.860,04 M€ (6.860.043.304 €) · 9 códigos · 12,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712` | PARTICIPACIÓ DELS ENS LOCALS EN ELS INGRESSOS DE L’ESTAT | 4.992.457.588 | 72,8 % |
| `531` | E-INFRAESTRUCTURES | 990.294.115 | 14,4 % |
| `612` | ORDENACIÓ, RECONVERSIÓ I SUPORT ALS SUBSECTORS AGR | 385.828.389 | 5,6 % |
| `711` | SUPORT FINANCER DE LA GENERALITAT ALS ENS LOCALS | 245.015.151 | 3,6 % |
| `613` | SUPORT A L'AGROINDÚSTRIA, LA COMERCIALITZACIÓ I LA | 118.291.697 | 1,7 % |
| `614` | MODERNITZACIÓ I MILLORA DE LES ESTRUCTURES EMPRESA | 91.744.992 | 1,3 % |
| `335` | FORMACIÓ PROFESSIONAL AGRÀRIA I PESQUERA | 14.830.910 | 0,2 % |
| `616` | DIVERSIFICACIÓ ECONÒMICA I QUALITAT DE VIDA AL MÓN | 12.141.777 | 0,2 % |
| `611` | SANITAT VEGETAL, ANIMAL I CONTROL DE PRODUCCIONS | 9.438.685 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,47 M€ (3.466.288 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112` | IMPULS I COORDINACIÓ DE L'ACCIÓ DE GOVERN | 3.466.288 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 527,64 M€ (527.641.332 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431` | HABITATGE | 453.815.450 | 86,0 % |
| `451` | PROMOCIÓ DE LA LLENGUA CATALANA | 73.825.882 | 14,0 % |

</details>

<details open><summary><b><code>empleo</code> — 927,54 M€ (927.537.916 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331` | OCUPABILITAT I AUTOOCUPACIÓ | 693.582.629 | 74,8 % |
| `333` | IGUALTAT, QUALITAT I INTEGRACIÓ LABORAL | 233.955.286 | 25,2 % |

</details>

<details open><summary><b><code>idi</code> — 844,52 M€ (844.523.683 €) · 9 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571` | RECERCA I DESENVOLUPAMENT | 381.985.080 | 45,2 % |
| `573` | R+D BIOMÈDICS I EN CIÈNCIES DE LA SALUT | 111.112.182 | 13,2 % |
| `562` | INFRAESTRUCTURES DE REGADIUS I ORDENACIÓ PARCEL.LÀ | 89.673.714 | 10,6 % |
| `532` | SOCIETAT DIGITAL | 85.076.886 | 10,1 % |
| `574` | INNOVACIÓ | 73.365.899 | 8,7 % |
| `572` | R+D EN CIÈNCIA I TECNOLOGIA AGROALIMENTÀRIA | 38.448.800 | 4,6 % |
| `661` | EMPRENEDORIA I FOMENT EMPRESARIAL | 32.854.311 | 3,9 % |
| `542` | ORDENACIÓ DEL TERRITORI I URBANISME | 24.006.811 | 2,8 % |
| `561` | INFRAESTRUCTURES PER AL DESENVOLUPAMENT RURAL | 8.000.000 | 0,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 2.484,71 M€ (2.484.712.971 €) · 2 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `315` | PROMOCIÓ DE L'AUTONOMIA PERSONAL | 2.472.374.689 | 99,5 % |
| `313` | SUPORT A LES FAMÍLIES | 12.338.283 | 0,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,71 M€ (14.706.386 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `314` | ATENCIÓ A LA IMMIGRACIÓ | 14.706.386 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 79,03 M€ (79.025.753 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316` | IGUALTAT I RESPECTE A LA DIVERSITAT | 79.025.753 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 140,73 M€ (140.733.040 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `651` | ORDENACIÓ, FOMENT I PROMOCIÓ TURÍSTICA | 123.149.654 | 87,5 % |
| `432` | BARRIS I NUCLIS ANTICS | 17.583.387 | 12,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,39 M€ (14.387.057 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322` | POLÍTIQUES DE DONES | 14.387.057 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 22.376,42 M€ · 62 códigos · 39,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911` | DEUTE PÚBLIC | 9.395.147.300 |
| `121` | DIRECCIÓ I ADMINISTRACIÓ GENERALS | 3.238.237.271 |
| `221` | SEGURETAT CIUTADANA | 1.641.363.281 |
| `522` | INFRAESTRUCTURES FERROVIÀRIES | 1.191.119.964 |
| `317` | INCLUSIÓ SOCIAL I LLUITA CONTRA POBRESA | 864.138.536 |
| `211` | ADMINISTRACIÓ DE JUSTÍCIA I MINISTERI FISCAL | 648.849.747 |
| `523` | SUPORT AL TRANSPORT PÚBLIC DE VIATGERS | 622.701.398 |
| `213` | SERVEIS PENITENCIARIS I MESURES PENALS ALTERNATIVE | 534.786.594 |
| `521` | CARRETERES | 527.343.056 |
| `318` | ATENCIÓ A LA INFÀNCIA I L'ADOLESCÈNCIA | 460.586.164 |
| `223` | PREVENCIÓ, EXTINCIÓ D'INCENDIS I SALVAMENTS | 388.443.797 |
| `533` | MITJANS DE COMUNICACIÓ SOCIAL | 369.564.694 |
| `125` | ADMINISTRACIÓ DE LES FINANCES DE LA GENERALITAT | 326.157.914 |
| `811` | FONS DE CONTINGÈNCIA | 300.000.000 |
| `441` | CREADORS I EMPRESES CULTURALS | 184.610.564 |
| `551` | PROTECCIÓ I CONSERVACIÓ DEL MEDI NATURAL I LA BIOD | 168.255.919 |
| `622` | SUPORT A LA INDÚSTRIA | 145.874.375 |
| `443` | PATRIMONI CULTURAL | 125.425.440 |
| `471` | ACTIVITAT FÍSICA I ESPORT | 125.257.513 |
| `552` | INFRAESTRUCTURA I GESTIÓ DE TRACTAMENT DE RESIDUS | 112.195.596 |
| `445` | GRANS INSTITUCIONS CULTURALS | 103.690.292 |
| `232` | COOPERACIÓ AL DESENVOLUPAMENT | 88.044.913 |
| `713` | SUPORT A OBRES I SERVEIS DELS ENS LOCALS | 85.950.000 |
| `631` | ENERGIA | 71.958.301 |
| `124` | REGULACIÓ, CONTROL I GESTIÓ DEL JOC | 49.871.744 |
| … | *resto: 37 códigos* | 606.843.818 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py cat     # regenera este documento
python3 tools/auditoria_magnitud.py cat        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa cat --anio <año> \
    --input ../fuentes/raw/cat/<año>/<fichero> --output /tmp/cat.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-cat.md`](limitaciones-cat.md)

