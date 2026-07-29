# Trazabilidad de la extracción — Galicia (`gal`)

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
| **2015** | 107 | `progr.pdf` | 13 | 60,7 % | 9.548,70 | — | no_aplica |
| **2016** | 108 | `progr.pdf` | 13 | 60,2 % | 10.097,37 | — | no_aplica |
| **2017** | 108 | `progr.pdf` | 13 | 60,2 % | 10.607,67 | — | no_aplica |
| **2018** | 108 | `progr.pdf` | 13 | 60,2 % | 10.520,62 | — | no_aplica |
| **2019** | 107 | `progr.pdf` | 13 | 59,8 % | 11.337,35 | — | no_aplica |
| **2020** | 107 | `progr.pdf` | 13 | 59,8 % | 11.594,12 | — | no_aplica |
| **2021** | 107 | `progr.pdf` | 13 | 59,8 % | 13.183,47 | — | no_aplica |
| **2022** | 107 | `progr.pdf` | 13 | 59,8 % | 12.843,40 | — | no_aplica |
| **2023** | 107 | `progr.pdf` | 13 | 59,8 % | 13.916,28 | — | no_aplica |
| **2024** | 107 | `progr.pdf` | 13 | 59,8 % | 14.519,61 | — | no_aplica |
| **2025** | 108 | `progr.pdf` | 13 | 60,2 % | 15.462,69 | — | no_aplica |
| **2026** | 108 | `progr.pdf` | 13 | 60,2 % | 16.044,89 | — | no_aplica |

**URL(s) de origen:**
- <https://orzamentos.xunta.gal/orzamentos/2018/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2019/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2020/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2021/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2022/DE/PROGR_I.pdf>
- <https://orzamentos.xunta.gal/orzamentos/2023/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2024/DE/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2025/DE/LIBROS/PROGR_I.PDF>
- <https://orzamentos.xunta.gal/orzamentos/2026/DE/LIBROS/PROGR_I.PDF>
- <https://www.conselleriadefacenda.gal/orzamentos/2015/DE/PROGR_I.PDF>
- <https://www.conselleriadefacenda.gal/orzamentos/2016/DE/PROGR_I.PDF>
- <https://www.conselleriadefacenda.gal/orzamentos/2017/DE/PROGR_I.PDF>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 3.365,53 | 3.541,66 | 3.652,33 | 3.917,82 | 4.055,16 | 4.191,36 | 4.712,92 | 4.708,01 | 5.170,56 | 5.379,51 | 5.675,37 | 5.840,97 |
| `educacion` | 2.097,39 | 2.198,19 | 2.261,26 | 2.337,68 | 2.412,87 | 2.520,44 | 2.689,45 | 2.763,44 | 2.873,38 | 2.951,53 | 3.065,99 | 3.125,91 |
| `soberania` | 523,02 | 584,45 | 604,93 | 583,68 | 603,13 | 634,64 | 690,52 | 738,57 | 780,05 | 794,89 | 844,48 | 859,68 |
| `direccion` | 3,38 | 3,64 | 3,47 | 3,55 | 3,61 | 3,72 | 3,73 | 3,76 | 6,03 | 6,26 | 6,71 | 6,97 |
| `vivienda` | 98,60 | 95,58 | 92,14 | 102,52 | 105,66 | 94,88 | 109,51 | 135,45 | 154,27 | 189,96 | 236,49 | 287,55 |
| `empleo` | 194,12 | 210,93 | 242,97 | 246,97 | 263,83 | 275,66 | 372,57 | 396,45 | 444,52 | 449,79 | 447,69 | 445,73 |
| `idi` | 182,30 | 213,80 | 218,08 | 238,41 | 242,74 | 264,88 | 395,22 | 411,20 | 438,22 | 421,99 | 411,41 | 369,02 |
| `dependencia` | 327,05 | 352,45 | 366,13 | 404,57 | 419,34 | 441,58 | 519,01 | 553,17 | 599,47 | 715,95 | 797,67 | 910,93 |
| `discapacidad` | 16,63 | 22,23 | 25,26 | 29,13 | 30,90 | 32,25 | 33,87 | 42,15 | 57,82 | 55,16 | 55,91 | 53,47 |
| `salud_mental` | 12,95 | 14,36 | 14,25 | 15,11 | 15,26 | 16,32 | 16,22 | 16,15 | 16,80 | 17,25 | 22,15 | 24,89 |
| `diversidad` | 8,30 | 9,43 | 9,87 | 11,60 | 13,31 | 14,24 | 17,16 | 16,85 | 20,45 | 22,40 | 24,02 | 25,35 |
| `turismo` | 84,57 | 97,41 | 105,58 | 121,66 | 125,93 | 127,64 | 195,77 | 201,59 | 229,15 | 235,11 | 241,00 | 221,48 |
| `igualdad` | 9,26 | 10,96 | 12,19 | 12,65 | 21,48 | 23,16 | 24,94 | 29,49 | 31,94 | 40,00 | 44,04 | 43,96 |
| **Σ asignado** | 6.923,10 | 7.355,10 | 7.608,47 | 8.025,37 | 8.313,21 | 8.640,75 | 9.780,90 | 10.016,28 | 10.822,65 | 11.279,79 | 11.872,94 | 12.215,91 |
| *(sin concepto)* | 2.625,60 | 2.742,27 | 2.999,20 | 2.495,25 | 3.024,14 | 2.953,37 | 3.402,57 | 2.827,12 | 3.093,63 | 3.239,83 | 3.589,74 | 3.828,99 |
| **TOTAL extraído** | 9.548,70 | 10.097,37 | 10.607,67 | 10.520,62 | 11.337,35 | 11.594,12 | 13.183,47 | 12.843,40 | 13.916,28 | 14.519,61 | 15.462,69 | 16.044,89 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +5,2 % | +3,1 % | +7,3 % | +3,5 % | +3,4 % | +12,4 % | −0,1 % | +9,8 % | +4,0 % | +5,5 % | +2,9 % |
| `educacion` | +4,8 % | +2,9 % | +3,4 % | +3,2 % | +4,5 % | +6,7 % | +2,8 % | +4,0 % | +2,7 % | +3,9 % | +2,0 % |
| `soberania` | +11,7 % | +3,5 % | −3,5 % | +3,3 % | +5,2 % | +8,8 % | +7,0 % | +5,6 % | +1,9 % | +6,2 % | +1,8 % |
| `direccion` | +7,7 % | −4,5 % | +2,3 % | +1,6 % | +3,0 % | +0,4 % | +0,7 % | +60,2 % ⚠ | +3,9 % | +7,1 % | +3,9 % |
| `vivienda` | −3,1 % | −3,6 % | +11,3 % | +3,1 % | −10,2 % | +15,4 % | +23,7 % | +13,9 % | +23,1 % | +24,5 % | +21,6 % |
| `empleo` | +8,7 % | +15,2 % | +1,6 % | +6,8 % | +4,5 % | +35,2 % | +6,4 % | +12,1 % | +1,2 % | −0,5 % | −0,4 % |
| `idi` | +17,3 % | +2,0 % | +9,3 % | +1,8 % | +9,1 % | +49,2 % ⚠ | +4,0 % | +6,6 % | −3,7 % | −2,5 % | −10,3 % |
| `dependencia` | +7,8 % | +3,9 % | +10,5 % | +3,7 % | +5,3 % | +17,5 % | +6,6 % | +8,4 % | +19,4 % | +11,4 % | +14,2 % |
| `discapacidad` | +33,7 % | +13,6 % | +15,3 % | +6,1 % | +4,4 % | +5,0 % | +24,5 % | +37,2 % | −4,6 % | +1,4 % | −4,4 % |
| `salud_mental` | +10,9 % | −0,8 % | +6,0 % | +1,0 % | +6,9 % | −0,6 % | −0,4 % | +4,1 % | +2,7 % | +28,4 % | +12,3 % |
| `diversidad` | +13,6 % | +4,7 % | +17,5 % | +14,7 % | +7,0 % | +20,6 % | −1,8 % | +21,4 % | +9,5 % | +7,3 % | +5,5 % |
| `turismo` | +15,2 % | +8,4 % | +15,2 % | +3,5 % | +1,4 % | +53,4 % ⚠ | +3,0 % | +13,7 % | +2,6 % | +2,5 % | −8,1 % |
| `igualdad` | +18,3 % | +11,2 % | +3,8 % | +69,7 % ⚠ | +7,8 % | +7,7 % | +18,2 % | +8,3 % | +25,3 % | +10,1 % | −0,2 % |
| **TOTAL** | +5,7 % | +5,1 % | −0,8 % | +7,8 % | +2,3 % | +13,7 % | −2,6 % | +8,4 % | +4,3 % | +6,5 % | +3,8 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2021 | `idi` | **SALTO** | 264,88 → 395,22 M€ (+49,2 % ⚠) |
| 2021 | `turismo` | **SALTO** | 127,64 → 195,77 M€ (+53,4 % ⚠) |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `progr.pdf` · 107 líneas · total extraído **9.548,70 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.365,53 M€ (3.365.526.487 €) · 7 códigos · 35,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.121.607.282 | 92,8 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 76.928.672 | 2,3 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 63.926.695 | 1,9 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 52.147.164 | 1,5 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 48.419.179 | 1,4 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.295.292 | 0,0 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PR | 1.202.203 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.097,39 M€ (2.097.391.793 €) · 14 códigos · 22,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 732.688.362 | 34,9 % |
| `422M` | ENSINANZA SECUNDARIA E FORMACIÓN PROFESIONAL | 671.220.969 | 32,0 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 322.748.446 | 15,4 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 183.454.590 | 8,7 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 49.173.397 | 2,3 % |
| `422D` | EDUCACIÓN ESPECIAL | 33.758.218 | 1,6 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 33.254.002 | 1,6 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 23.661.908 | 1,1 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 17.247.970 | 0,8 % |
| `422G` | ENSINANZAS ESPECIAIS | 15.475.587 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 6.969.541 | 0,3 % |
| `422L` | CAPACITACIÓN E EXTENSIÓN AGROFORESTAL | 6.015.799 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 1.378.892 | 0,1 % |
| `422H` | OUTRAS ENSINANZAS | 344.112 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 523,02 M€ (523.023.071 €) · 18 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 108.873.015 | 20,8 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 74.157.799 | 14,2 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 49.481.059 | 9,5 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 47.903.359 | 9,2 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 43.091.442 | 8,2 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 41.616.655 | 8,0 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 28.274.265 | 5,4 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 28.218.428 | 5,4 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 24.639.393 | 4,7 % |
| `541C` | PROTECCIÓN E MELLORA DO MEDIO NATURAL MARÍTIMO | 19.579.738 | 3,7 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 13.809.997 | 2,6 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 13.176.774 | 2,5 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 10.942.656 | 2,1 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 6.433.217 | 1,2 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 4.373.071 | 0,8 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 3.860.531 | 0,7 % |
| `713A` | MOBILIDADE DE TERRAS AGRARIAS IMPRODUTIVAS | 3.089.608 | 0,6 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 1.502.064 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 3,38 M€ (3.376.671 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.376.671 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 98,60 M€ (98.603.367 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451B` | ACCESO Á VIVENDA | 70.235.090 | 71,2 % |
| `521A` | URBANISMO | 16.340.441 | 16,6 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 12.027.836 | 12,2 % |

</details>

<details open><summary><b><code>empleo</code> — 194,12 M€ (194.115.762 €) · 7 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 68.200.948 | 35,1 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 50.731.732 | 26,1 % |
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INC | 37.867.081 | 19,5 % |
| `324A` | MELLORA DA ORGANIZ. E ADM. DAS RELACIÓNS LABORAIS E DA ECONOMÍA SOCIAL | 15.630.138 | 8,1 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 8.633.635 | 4,4 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 7.052.228 | 3,6 % |
| `323B` | MELLORA DA CUALIFICACIÓN NO EMPREGO | 6.000.000 | 3,1 % |

</details>

<details open><summary><b><code>idi</code> — 182,30 M€ (182.304.336 €) · 3 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 85.667.685 | 47,0 % |
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXI | 70.893.238 | 38,9 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 25.743.413 | 14,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 327,05 M€ (327.047.917 €) · 2 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | SERVIZOS SOCIAIS DE ATENCIÓN ÁS PERSOAS DEPENDENTES | 298.430.435 | 91,2 % |
| `312E` | SERVIZOS SOCIAIS DE ATENCIÓN A PERSOAS MAIORES E CON DISCAPACIDADE | 28.617.482 | 8,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 16,63 M€ (16.625.753 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 16.625.753 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 12,95 M€ (12.951.703 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 12.951.703 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 8,30 M€ (8.297.491 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 8.297.491 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 84,57 M€ (84.572.732 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | COORDINACIÓN E PROMOCIÓN DO TURISMO | 39.133.184 | 46,3 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 17.511.094 | 20,7 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 14.361.204 | 17,0 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 13.407.250 | 15,9 % |
| `432C` | FOMENTO DO AUDIOVISUAL | 160.000 | 0,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,26 M€ (9.263.920 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 5.848.020 | 63,1 % |
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNE RO | 3.415.900 | 36,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.625,60 M€ · 42 códigos · 27,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.515.100.598 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 229.919.220 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 114.183.620 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDAD | 112.972.806 |
| `461B` | RADIODIFUSIÓN E TVG | 98.735.480 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE | 89.138.893 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 52.877.913 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 50.648.291 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 40.324.898 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 39.645.029 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 33.507.697 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 27.585.212 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 25.094.187 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 18.548.149 |
| `111B` | ACTIVIDADE LEXISLATIVA | 18.025.925 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 17.899.066 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 16.433.177 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO E CULTURAL | 13.683.366 |
| `141A` | ADMINISTRACIÓN LOCAL | 12.348.805 |
| `613A` | ORDENACIÓN , INFORMACIÓN E DEFENSA DO CONSUMIDOR E DA COMPETENCIA | 11.294.950 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 8.539.253 |
| `151A` | FOMENTO DA LINGUA GALEGA | 6.740.182 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 6.622.704 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 6.484.978 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 6.422.539 |
| … | *resto: 17 códigos* | 52.825.997 |

</details>

### 2016

*Fuente: `progr.pdf` · 108 líneas · total extraído **10.097,37 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.541,66 M€ (3.541.657.595 €) · 7 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.249.975.690 | 91,8 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 113.358.038 | 3,2 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 74.467.427 | 2,1 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 59.959.606 | 1,7 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 41.477.854 | 1,2 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.216.777 | 0,0 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PR | 1.202.203 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.198,19 M€ (2.198.190.396 €) · 13 códigos · 21,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 744.476.375 | 33,9 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 696.503.769 | 31,7 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 338.516.198 | 15,4 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 186.598.074 | 8,5 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 61.752.543 | 2,8 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 50.034.780 | 2,3 % |
| `422D` | EDUCACIÓN ESPECIAL | 35.411.402 | 1,6 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 33.600.786 | 1,5 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 17.519.649 | 0,8 % |
| `422G` | ENSINANZAS ESPECIAIS | 16.048.251 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 8.340.399 | 0,4 % |
| `422L` | CAPACITACIÓN E EXTENSIÓN AGROFORESTAL | 7.549.985 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 1.838.185 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 584,45 M€ (584.454.250 €) · 18 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 99.883.310 | 17,1 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 90.939.750 | 15,6 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 73.354.984 | 12,6 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 55.389.011 | 9,5 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 50.681.421 | 8,7 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 46.738.566 | 8,0 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 35.216.926 | 6,0 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 32.297.504 | 5,5 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR, MELLORA DO | 28.912.322 | 4,9 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 22.027.943 | 3,8 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 11.066.157 | 1,9 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 9.143.302 | 1,6 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 8.811.746 | 1,5 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 5.900.000 | 1,0 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 5.503.418 | 0,9 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 4.055.557 | 0,7 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.145.398 | 0,5 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 1.386.935 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 3,64 M€ (3.636.325 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.636.325 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 95,58 M€ (95.580.618 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451B` | ACCESO Á VIVENDA | 59.634.421 | 62,4 % |
| `521A` | URBANISMO | 15.595.219 | 16,3 % |
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 15.223.547 | 15,9 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 5.127.431 | 5,4 % |

</details>

<details open><summary><b><code>empleo</code> — 210,93 M€ (210.933.016 €) · 8 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 71.606.501 | 33,9 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 53.546.538 | 25,4 % |
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INC | 45.046.765 | 21,4 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA P | 17.904.825 | 8,5 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 6.648.059 | 3,2 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 6.500.000 | 3,1 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 5.403.620 | 2,6 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 4.276.708 | 2,0 % |

</details>

<details open><summary><b><code>idi</code> — 213,80 M€ (213.803.009 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 96.389.590 | 45,1 % |
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 77.538.389 | 36,3 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 39.875.030 | 18,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 352,45 M€ (352.447.241 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 324.181.183 | 92,0 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOA | 28.266.058 | 8,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 22,23 M€ (22.230.923 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 22.230.923 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 14,36 M€ (14.361.231 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 14.361.231 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,43 M€ (9.427.880 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 9.427.880 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 97,41 M€ (97.414.896 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 40.252.422 | 41,3 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 26.311.995 | 27,0 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 17.708.421 | 18,2 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 13.142.058 | 13,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,96 M€ (10.963.616 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 6.994.875 | 63,8 % |
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 3.968.741 | 36,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.742,27 M€ · 43 códigos · 27,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.598.200.386 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 241.915.331 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 128.243.751 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDAD | 116.138.255 |
| `461B` | RADIODIFUSIÓN E TVG | 94.753.203 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE | 77.710.289 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 72.845.412 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 55.354.523 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 40.233.960 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 30.812.310 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 27.913.098 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 23.941.038 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 19.611.207 |
| `111B` | ACTIVIDADE LEXISLATIVA | 18.339.725 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 17.795.190 |
| `141A` | ADMINISTRACIÓN LOCAL | 15.628.986 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 14.947.084 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 13.474.664 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 13.398.783 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO E CULTURAL | 12.834.588 |
| `613A` | ORDENACIÓN , INFORMACIÓN E DEFENSA DO CONSUMIDOR E DA COMPETENCIA | 10.726.848 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 9.599.730 |
| `161A` | ELECCIÓNS E PARTIDOS POLÍTICOS | 7.995.218 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 7.989.690 |
| `151A` | FOMENTO DA LINGUA GALEGA | 6.756.815 |
| … | *resto: 18 códigos* | 65.106.562 |

</details>

### 2017

*Fuente: `progr.pdf` · 108 líneas · total extraído **10.607,67 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.652,33 M€ (3.652.332.091 €) · 7 códigos · 34,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.353.335.002 | 91,8 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 122.773.813 | 3,4 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 72.907.146 | 2,0 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 58.820.655 | 1,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 42.131.902 | 1,2 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PR | 1.202.203 | 0,0 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.161.370 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.261,26 M€ (2.261.255.143 €) · 13 códigos · 21,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 790.063.939 | 34,9 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 728.157.472 | 32,2 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 348.378.846 | 15,4 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 189.308.620 | 8,4 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 51.808.910 | 2,3 % |
| `422D` | EDUCACIÓN ESPECIAL | 37.452.246 | 1,7 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 35.649.608 | 1,6 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 25.053.024 | 1,1 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 19.701.062 | 0,9 % |
| `422G` | ENSINANZAS ESPECIAIS | 17.054.229 | 0,8 % |
| `422K` | ENSINANZAS PESQUEIRAS | 8.750.754 | 0,4 % |
| `422L` | CAPACITACIÓN E EXTENSIÓN AGROFORESTAL | 7.626.092 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 2.250.341 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 604,93 M€ (604.934.345 €) · 18 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 101.215.264 | 16,7 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 95.262.485 | 15,7 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 72.516.793 | 12,0 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 61.015.022 | 10,1 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 54.004.229 | 8,9 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 49.056.895 | 8,1 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 36.434.827 | 6,0 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 36.199.933 | 6,0 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO | 29.036.695 | 4,8 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 18.366.163 | 3,0 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 14.602.441 | 2,4 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 10.317.003 | 1,7 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 8.225.481 | 1,4 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 6.407.863 | 1,1 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 5.147.224 | 0,9 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 3.302.302 | 0,5 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.262.915 | 0,5 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 560.810 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,47 M€ (3.474.031 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.474.031 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 92,14 M€ (92.137.126 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 66.560.523 | 72,2 % |
| `521A` | URBANISMO | 16.937.304 | 18,4 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 5.149.699 | 5,6 % |
| `451B` | ACCESO Á VIVENDA | 3.489.600 | 3,8 % |

</details>

<details open><summary><b><code>empleo</code> — 242,97 M€ (242.973.137 €) · 8 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 80.456.030 | 33,1 % |
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INC | 77.320.372 | 31,8 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 43.402.945 | 17,9 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA P | 18.064.863 | 7,4 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 11.288.891 | 4,6 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 6.273.377 | 2,6 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 5.411.139 | 2,2 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 218,08 M€ (218.078.014 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 99.262.466 | 45,5 % |
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 79.918.839 | 36,6 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 38.896.709 | 17,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 366,13 M€ (366.132.154 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 338.238.420 | 92,4 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOA | 27.893.734 | 7,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 25,26 M€ (25.264.423 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 25.264.423 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 14,25 M€ (14.245.060 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 14.245.060 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,87 M€ (9.874.953 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 9.874.953 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 105,58 M€ (105.579.724 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 43.198.184 | 40,9 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 27.716.995 | 26,3 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 18.129.685 | 17,2 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 16.534.860 | 15,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 12,19 M€ (12.188.542 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 6.983.875 | 57,3 % |
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 5.204.667 | 42,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.999,20 M€ · 43 códigos · 28,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.822.264.186 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 246.975.118 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 134.575.697 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDAD | 119.764.132 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE | 100.427.692 |
| `461B` | RADIODIFUSIÓN E TVG | 96.453.203 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 62.449.789 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 55.345.096 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 41.899.571 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 34.295.816 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 28.952.865 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 25.472.751 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 19.316.978 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 19.218.550 |
| `111B` | ACTIVIDADE LEXISLATIVA | 18.705.488 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 15.544.718 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 14.793.491 |
| `141A` | ADMINISTRACIÓN LOCAL | 13.265.541 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 12.910.804 |
| `613A` | ORDENACIÓN , INFORMACIÓN E DEFENSA DO CONSUMIDOR E DA COMPETENCIA | 12.232.398 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 10.165.063 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 6.937.054 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 6.886.824 |
| `151A` | FOMENTO DA LINGUA GALEGA | 6.819.086 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 6.164.644 |
| … | *resto: 18 códigos* | 67.363.207 |

</details>

### 2018

*Fuente: `progr.pdf` · 108 líneas · total extraído **10.520,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.917,82 M€ (3.917.820.182 €) · 7 códigos · 37,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.603.123.640 | 92,0 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 131.258.666 | 3,4 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 77.045.078 | 2,0 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 61.811.029 | 1,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 41.954.579 | 1,1 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.424.987 | 0,0 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 1.202.203 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.337,68 M€ (2.337.684.996 €) · 13 códigos · 22,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 819.703.101 | 35,1 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 752.363.799 | 32,2 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 359.865.775 | 15,4 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 185.977.141 | 8,0 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 57.006.073 | 2,4 % |
| `422D` | EDUCACIÓN ESPECIAL | 39.674.079 | 1,7 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 36.932.324 | 1,6 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 25.758.800 | 1,1 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 23.121.879 | 1,0 % |
| `422G` | ENSINANZAS ESPECIAIS | 17.147.136 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 8.973.191 | 0,4 % |
| `422L` | CAPACITACIÓN E EXTENSIÓN AGROFORESTAL | 7.919.178 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.242.520 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 583,68 M€ (583.679.346 €) · 18 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 102.920.151 | 17,6 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 100.750.425 | 17,3 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 77.241.448 | 13,2 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 63.470.636 | 10,9 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 49.982.737 | 8,6 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 43.573.183 | 7,5 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 34.496.880 | 5,9 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 30.298.118 | 5,2 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 18.316.035 | 3,1 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 15.223.059 | 2,6 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 10.177.342 | 1,7 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 8.835.000 | 1,5 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 8.430.806 | 1,4 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 6.761.170 | 1,2 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 5.147.223 | 0,9 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 3.955.048 | 0,7 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.382.673 | 0,6 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 717.412 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,55 M€ (3.553.525 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.553.525 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 102,52 M€ (102.524.662 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 73.239.810 | 71,4 % |
| `521A` | URBANISMO | 19.184.779 | 18,7 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 5.626.299 | 5,5 % |
| `451B` | ACCESO Á VIVENDA | 4.473.774 | 4,4 % |

</details>

<details open><summary><b><code>empleo</code> — 246,97 M€ (246.971.190 €) · 8 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 81.331.317 | 32,9 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 76.321.459 | 30,9 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 45.067.597 | 18,2 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 18.790.823 | 7,6 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 14.432.958 | 5,8 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 6.126.655 | 2,5 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 4.144.861 | 1,7 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 238,41 M€ (238.413.533 €) · 3 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 102.606.080 | 43,0 % |
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 97.379.767 | 40,8 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 38.427.686 | 16,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 404,57 M€ (404.565.100 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 368.973.951 | 91,2 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 35.591.149 | 8,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 29,13 M€ (29.128.495 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 29.128.495 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 15,11 M€ (15.105.652 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 15.105.652 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 11,60 M€ (11.602.427 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 11.602.427 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 121,66 M€ (121.664.794 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 55.164.376 | 45,3 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 29.421.478 | 24,2 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 18.836.988 | 15,5 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 18.241.952 | 15,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 12,65 M€ (12.653.752 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 7.226.427 | 57,1 % |
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 5.427.325 | 42,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.495,25 M€ · 43 códigos · 23,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.222.143.484 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 273.720.878 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 146.115.252 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 125.594.165 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 123.003.362 |
| `461B` | RADIODIFUSIÓN E TVG | 99.578.033 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 61.824.578 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 45.064.483 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 41.750.212 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 38.047.123 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 34.545.323 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 31.552.517 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 24.934.189 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 21.946.159 |
| `111B` | ACTIVIDADE LEXISLATIVA | 19.284.399 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 17.755.740 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 15.457.581 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 15.131.945 |
| `141A` | ADMINISTRACIÓN LOCAL | 13.803.228 |
| `613A` | ORDENACIÓN , INFORMACIÓN E DEFENSA DO CONSUMIDOR E DA COMPETENCIA | 11.093.024 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 10.154.626 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 9.404.156 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 9.222.081 |
| `151A` | FOMENTO DA LINGUA GALEGA | 7.623.085 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 7.098.583 |
| … | *resto: 18 códigos* | 69.405.797 |

</details>

### 2019

*Fuente: `progr.pdf` · 107 líneas · total extraído **11.337,35 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.055,16 M€ (4.055.163.402 €) · 7 códigos · 35,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.718.885.556 | 91,7 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 142.116.338 | 3,5 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 78.500.072 | 1,9 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 63.449.669 | 1,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 49.182.570 | 1,2 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 1.620.525 | 0,0 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.408.672 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.412,87 M€ (2.412.867.739 €) · 12 códigos · 21,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 838.676.792 | 34,8 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 783.849.405 | 32,5 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 367.994.329 | 15,3 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 188.155.066 | 7,8 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 61.291.000 | 2,5 % |
| `422D` | EDUCACIÓN ESPECIAL | 43.798.238 | 1,8 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 38.638.485 | 1,6 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 33.523.640 | 1,4 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 25.429.420 | 1,1 % |
| `422G` | ENSINANZAS ESPECIAIS | 18.835.690 | 0,8 % |
| `422K` | ENSINANZAS PESQUEIRAS | 9.375.674 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.300.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 603,13 M€ (603.130.896 €) · 18 códigos · 5,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 113.893.016 | 18,9 % |
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 110.725.930 | 18,4 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 66.620.226 | 11,0 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 65.151.691 | 10,8 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 50.685.450 | 8,4 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 49.020.237 | 8,1 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 33.649.637 | 5,6 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 31.554.620 | 5,2 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 18.990.972 | 3,1 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 15.388.320 | 2,6 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 8.768.334 | 1,5 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 8.623.965 | 1,4 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 8.251.988 | 1,4 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 7.385.771 | 1,2 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 6.108.286 | 1,0 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 4.269.931 | 0,7 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.434.729 | 0,6 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 607.793 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,61 M€ (3.611.860 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.611.860 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 105,66 M€ (105.656.547 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 72.914.117 | 69,0 % |
| `521A` | URBANISMO | 15.779.913 | 14,9 % |
| `451B` | ACCESO Á VIVENDA | 10.604.700 | 10,0 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 6.357.817 | 6,0 % |

</details>

<details open><summary><b><code>empleo</code> — 263,83 M€ (263.825.058 €) · 8 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 86.738.984 | 32,9 % |
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 71.009.591 | 26,9 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 50.604.121 | 19,2 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 20.413.467 | 7,7 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 20.252.043 | 7,7 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 7.624.967 | 2,9 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 6.426.365 | 2,4 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 242,74 M€ (242.736.721 €) · 3 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 121.984.554 | 50,3 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 91.108.513 | 37,5 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 29.643.654 | 12,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 419,34 M€ (419.338.223 €) · 2 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 382.872.359 | 91,3 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 36.465.864 | 8,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 30,90 M€ (30.901.757 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 30.901.757 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 15,26 M€ (15.258.685 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 15.258.685 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 13,31 M€ (13.310.196 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 13.310.196 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 125,93 M€ (125.930.862 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 60.944.672 | 48,4 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 30.087.428 | 23,9 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 19.063.465 | 15,1 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 15.835.297 | 12,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 21,48 M€ (21.477.595 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 14.113.342 | 65,7 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 7.364.253 | 34,3 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.024,14 M€ · 43 códigos · 26,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.675.915.745 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 266.643.929 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 158.696.789 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 148.223.702 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 128.744.353 |
| `461B` | RADIODIFUSIÓN E TVG | 102.923.844 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 64.229.119 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 53.274.320 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 51.241.639 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 48.205.603 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 35.894.447 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 33.669.123 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 29.554.780 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 24.259.027 |
| `111B` | ACTIVIDADE LEXISLATIVA | 19.804.604 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 17.562.035 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 16.480.955 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 15.249.298 |
| `141A` | ADMINISTRACIÓN LOCAL | 15.141.134 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 10.154.626 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 8.837.702 |
| `151A` | FOMENTO DA LINGUA GALEGA | 8.078.959 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 7.625.450 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 7.485.379 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 7.288.943 |
| … | *resto: 18 códigos* | 68.956.279 |

</details>

### 2020

*Fuente: `progr.pdf` · 107 líneas · total extraído **11.594,12 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.191,36 M€ (4.191.355.776 €) · 7 códigos · 36,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 3.832.289.158 | 91,4 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 160.334.745 | 3,8 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 78.415.877 | 1,9 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 65.471.910 | 1,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 51.588.312 | 1,2 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 1.893.738 | 0,0 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.362.036 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.520,44 M€ (2.520.437.222 €) · 12 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 867.375.471 | 34,4 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 810.446.317 | 32,2 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 376.650.751 | 14,9 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 215.657.698 | 8,6 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 63.908.501 | 2,5 % |
| `422D` | EDUCACIÓN ESPECIAL | 48.128.971 | 1,9 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 39.878.149 | 1,6 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 39.852.380 | 1,6 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 26.247.320 | 1,0 % |
| `422G` | ENSINANZAS ESPECIAIS | 19.200.625 | 0,8 % |
| `422K` | ENSINANZAS PESQUEIRAS | 9.775.462 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.315.577 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 634,64 M€ (634.635.466 €) · 18 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 127.272.148 | 20,1 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 123.068.104 | 19,4 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 76.355.504 | 12,0 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 67.661.519 | 10,7 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 52.650.205 | 8,3 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 45.896.107 | 7,2 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 32.590.274 | 5,1 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 20.947.045 | 3,3 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 20.194.539 | 3,2 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 16.845.507 | 2,7 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 11.703.916 | 1,8 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 9.302.513 | 1,5 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 8.273.793 | 1,3 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 6.649.617 | 1,0 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 6.595.685 | 1,0 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 4.997.199 | 0,8 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.217.830 | 0,5 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 413.961 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,72 M€ (3.718.663 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.718.663 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 94,88 M€ (94.882.923 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 61.470.518 | 64,8 % |
| `521A` | URBANISMO | 15.665.517 | 16,5 % |
| `451B` | ACCESO Á VIVENDA | 10.748.000 | 11,3 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 6.998.888 | 7,4 % |

</details>

<details open><summary><b><code>empleo</code> — 275,66 M€ (275.655.389 €) · 8 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 84.310.960 | 30,6 % |
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 70.733.222 | 25,7 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 53.229.663 | 19,3 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 27.051.801 | 9,8 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 23.134.925 | 8,4 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 10.435.913 | 3,8 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 6.003.385 | 2,2 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,3 % |

</details>

<details open><summary><b><code>idi</code> — 264,88 M€ (264.879.109 €) · 3 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 133.996.145 | 50,6 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 92.136.944 | 34,8 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 38.746.020 | 14,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 441,58 M€ (441.575.398 €) · 2 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 404.086.794 | 91,5 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 37.488.604 | 8,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 32,25 M€ (32.250.649 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 32.250.649 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,32 M€ (16.317.089 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 16.317.089 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 14,24 M€ (14.236.313 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 14.236.313 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 127,64 M€ (127.641.907 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 60.556.034 | 47,4 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 31.410.290 | 24,6 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 19.788.645 | 15,5 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 15.886.938 | 12,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 23,16 M€ (23.163.164 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 14.281.985 | 61,7 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 8.881.179 | 38,3 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.953,37 M€ · 43 códigos · 25,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.642.102.187 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 228.494.497 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 156.314.058 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 135.797.955 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 130.022.421 |
| `461B` | RADIODIFUSIÓN E TVG | 105.919.984 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 60.523.335 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 56.600.857 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 54.493.103 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 47.521.780 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 36.410.401 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 35.122.809 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 28.947.195 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 25.257.216 |
| `111B` | ACTIVIDADE LEXISLATIVA | 20.378.900 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 17.514.571 |
| `141A` | ADMINISTRACIÓN LOCAL | 17.281.586 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 16.537.161 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 14.604.795 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 9.452.443 |
| `161A` | ELECCIÓNS E PARTIDOS POLÍTICOS | 8.683.120 |
| `151A` | FOMENTO DA LINGUA GALEGA | 8.507.074 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 7.910.216 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 7.754.626 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 7.673.000 |
| … | *resto: 18 códigos* | 73.544.958 |

</details>

### 2021

*Fuente: `progr.pdf` · 107 líneas · total extraído **13.183,47 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.712,92 M€ (4.712.923.613 €) · 7 códigos · 35,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 4.294.883.986 | 91,1 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 182.072.137 | 3,9 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 83.396.146 | 1,8 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 81.812.840 | 1,7 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 66.706.149 | 1,4 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 2.673.737 | 0,1 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.378.618 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.689,45 M€ (2.689.451.194 €) · 12 códigos · 20,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 909.141.190 | 33,8 % |
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 908.907.567 | 33,8 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 383.510.312 | 14,3 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 222.846.948 | 8,3 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 67.888.787 | 2,5 % |
| `422D` | EDUCACIÓN ESPECIAL | 49.849.666 | 1,9 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 45.952.010 | 1,7 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 41.504.567 | 1,5 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 26.807.565 | 1,0 % |
| `422G` | ENSINANZAS ESPECIAIS | 19.996.683 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 9.550.774 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.495.125 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 690,52 M€ (690.517.653 €) · 18 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 145.579.441 | 21,1 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 120.791.061 | 17,5 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 84.817.628 | 12,3 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 79.827.369 | 11,6 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 55.570.933 | 8,0 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 41.032.736 | 5,9 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 33.384.452 | 4,8 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 26.138.386 | 3,8 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 23.918.476 | 3,5 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 19.913.398 | 2,9 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 13.631.332 | 2,0 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 9.539.724 | 1,4 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 9.163.857 | 1,3 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 8.469.664 | 1,2 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 8.248.271 | 1,2 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 6.495.966 | 0,9 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.268.458 | 0,5 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 726.501 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,73 M€ (3.734.804 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.734.804 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 109,51 M€ (109.512.182 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 73.950.268 | 67,5 % |
| `521A` | URBANISMO | 16.648.826 | 15,2 % |
| `451B` | ACCESO Á VIVENDA | 11.860.974 | 10,8 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 7.052.114 | 6,4 % |

</details>

<details open><summary><b><code>empleo</code> — 372,57 M€ (372.567.704 €) · 8 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 151.553.202 | 40,7 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 85.354.000 | 22,9 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 54.785.174 | 14,7 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 33.013.588 | 8,9 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 28.269.794 | 7,6 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 11.747.500 | 3,2 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 7.088.926 | 1,9 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 395,22 M€ (395.218.063 €) · 3 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 171.252.130 | 43,3 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 155.039.335 | 39,2 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 68.926.598 | 17,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 519,01 M€ (519.013.879 €) · 2 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 442.629.086 | 85,3 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 76.384.793 | 14,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 33,87 M€ (33.868.603 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 33.868.603 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,22 M€ (16.215.502 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 16.215.502 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 17,16 M€ (17.163.964 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 17.163.964 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 195,77 M€ (195.767.880 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 104.770.454 | 53,5 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 44.724.748 | 22,8 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 23.744.605 | 12,1 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 22.528.073 | 11,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 24,94 M€ (24.941.328 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 14.712.529 | 59,0 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 10.228.799 | 41,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.402,57 M€ · 43 códigos · 25,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.671.784.382 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 284.026.237 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 240.668.223 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 171.131.227 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 161.278.080 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 127.057.910 |
| `461B` | RADIODIFUSIÓN E TVG | 106.385.440 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 80.007.843 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 71.661.760 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 64.337.828 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 61.323.219 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 48.522.672 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 36.989.376 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 32.474.216 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 30.283.875 |
| `111B` | ACTIVIDADE LEXISLATIVA | 20.583.700 |
| `141A` | ADMINISTRACIÓN LOCAL | 17.259.490 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 17.113.709 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 16.710.349 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 16.146.701 |
| `151A` | FOMENTO DA LINGUA GALEGA | 13.062.113 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 12.361.102 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 10.751.448 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 8.211.607 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 7.847.453 |
| … | *resto: 18 códigos* | 74.593.825 |

</details>

### 2022

*Fuente: `progr.pdf` · 107 líneas · total extraído **12.843,40 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.708,01 M€ (4.708.013.386 €) · 7 códigos · 36,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 4.302.888.242 | 91,4 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 168.332.509 | 3,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 89.697.400 | 1,9 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 76.730.216 | 1,6 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 66.047.606 | 1,4 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 2.318.924 | 0,0 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 1.998.489 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.763,44 M€ (2.763.441.230 €) · 12 códigos · 21,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 913.564.517 | 33,1 % |
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 904.223.596 | 32,7 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 387.038.772 | 14,0 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 212.507.083 | 7,7 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 105.629.693 | 3,8 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 78.956.048 | 2,9 % |
| `422D` | EDUCACIÓN ESPECIAL | 52.450.500 | 1,9 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 43.203.120 | 1,6 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 33.748.287 | 1,2 % |
| `422G` | ENSINANZAS ESPECIAIS | 19.956.432 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 9.518.057 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 2.645.125 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 738,57 M€ (738.573.543 €) · 18 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 154.515.526 | 20,9 % |
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 142.446.318 | 19,3 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 90.574.350 | 12,3 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 83.957.129 | 11,4 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 55.003.339 | 7,4 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 47.854.170 | 6,5 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 33.465.271 | 4,5 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 27.352.515 | 3,7 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 23.883.895 | 3,2 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 16.378.309 | 2,2 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 13.735.684 | 1,9 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 11.463.000 | 1,6 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 10.942.274 | 1,5 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 8.365.150 | 1,1 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 7.303.856 | 1,0 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 6.822.534 | 0,9 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.234.913 | 0,4 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 1.275.310 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 3,76 M€ (3.762.034 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 3.762.034 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 135,45 M€ (135.454.306 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 90.198.170 | 66,6 % |
| `451B` | ACCESO Á VIVENDA | 19.635.974 | 14,5 % |
| `521A` | URBANISMO | 16.474.877 | 12,2 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 9.145.285 | 6,8 % |

</details>

<details open><summary><b><code>empleo</code> — 396,45 M€ (396.446.745 €) · 8 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 115.029.459 | 29,0 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 105.882.187 | 26,7 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 98.321.692 | 24,8 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 35.027.787 | 8,8 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 26.542.576 | 6,7 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 7.845.762 | 2,0 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 7.041.762 | 1,8 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 411,20 M€ (411.198.306 €) · 3 códigos · 3,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 197.216.544 | 48,0 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 146.677.320 | 35,7 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 67.304.442 | 16,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 553,17 M€ (553.166.639 €) · 2 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 487.913.369 | 88,2 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 65.253.270 | 11,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 42,15 M€ (42.149.804 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 42.149.804 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,15 M€ (16.146.151 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 16.146.151 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 16,85 M€ (16.847.451 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 16.847.451 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 201,59 M€ (201.592.114 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 115.320.835 | 57,2 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 45.160.557 | 22,4 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 22.735.111 | 11,3 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 18.375.611 | 9,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 29,49 M€ (29.487.315 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 17.915.189 | 60,8 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 11.572.126 | 39,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.827,12 M€ · 43 códigos · 22,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.326.565.439 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 254.371.616 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 161.993.976 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 146.563.623 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 135.713.928 |
| `461B` | RADIODIFUSIÓN E TVG | 117.385.440 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 112.189.612 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 63.169.635 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 57.138.820 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 57.092.051 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 49.704.707 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 44.110.877 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 32.489.463 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 29.314.625 |
| `111B` | ACTIVIDADE LEXISLATIVA | 20.753.000 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 19.222.936 |
| `141A` | ADMINISTRACIÓN LOCAL | 17.322.882 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 17.314.885 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 16.245.405 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 14.473.301 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 13.500.000 |
| `511A` | DIRECCIÓN E SERVIZOS XERAIS DE TERRITORIO E INFRAESTRUTURAS | 13.193.826 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 10.351.448 |
| `151A` | FOMENTO DA LINGUA GALEGA | 10.105.395 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 8.734.296 |
| … | *resto: 18 códigos* | 78.097.121 |

</details>

### 2023

*Fuente: `progr.pdf` · 107 líneas · total extraído **13.916,28 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.170,56 M€ (5.170.564.504 €) · 7 códigos · 37,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 4.651.795.969 | 90,0 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 229.330.457 | 4,4 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 96.748.368 | 1,9 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 90.393.706 | 1,7 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 86.763.013 | 1,7 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 12.596.848 | 0,2 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 2.936.143 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 2.873,38 M€ (2.873.380.743 €) · 12 códigos · 20,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 967.422.724 | 33,7 % |
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 939.048.552 | 32,7 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 399.601.085 | 13,9 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 227.990.050 | 7,9 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 89.794.122 | 3,1 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 83.248.208 | 2,9 % |
| `422D` | EDUCACIÓN ESPECIAL | 55.783.883 | 1,9 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 44.434.398 | 1,5 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 32.303.339 | 1,1 % |
| `422G` | ENSINANZAS ESPECIAIS | 20.812.162 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 9.938.935 | 0,3 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.003.285 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 780,05 M€ (780.046.044 €) · 18 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 160.470.685 | 20,6 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 128.030.405 | 16,4 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 86.718.653 | 11,1 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 86.068.675 | 11,0 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 57.690.407 | 7,4 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 57.062.044 | 7,3 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 35.040.030 | 4,5 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 32.415.381 | 4,2 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 31.854.565 | 4,1 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 27.402.304 | 3,5 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 15.849.185 | 2,0 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 13.935.243 | 1,8 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 13.085.695 | 1,7 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 12.107.792 | 1,6 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 8.850.647 | 1,1 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 8.719.485 | 1,1 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.386.698 | 0,4 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 1.358.150 | 0,2 % |

</details>

<details open><summary><b><code>direccion</code> — 6,03 M€ (6.027.722 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 6.027.722 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 154,27 M€ (154.266.820 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 90.371.523 | 58,6 % |
| `451B` | ACCESO Á VIVENDA | 35.255.580 | 22,9 % |
| `521A` | URBANISMO | 18.125.640 | 11,7 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 10.514.077 | 6,8 % |

</details>

<details open><summary><b><code>empleo</code> — 444,52 M€ (444.518.895 €) · 8 códigos · 3,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 138.709.132 | 31,2 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 127.333.383 | 28,6 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 94.539.738 | 21,3 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 42.337.271 | 9,5 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 22.781.725 | 5,1 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 9.439.937 | 2,1 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 8.622.189 | 1,9 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 438,22 M€ (438.217.629 €) · 3 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 212.936.801 | 48,6 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 159.624.357 | 36,4 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 65.656.471 | 15,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 599,47 M€ (599.469.409 €) · 2 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 524.471.094 | 87,5 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 74.998.315 | 12,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 57,82 M€ (57.817.595 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 57.817.595 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 16,80 M€ (16.803.325 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 16.803.325 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 20,45 M€ (20.447.147 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 20.447.147 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 229,15 M€ (229.152.090 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 131.820.132 | 57,5 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 44.175.514 | 19,3 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 27.671.084 | 12,1 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 25.485.360 | 11,1 % |

</details>

<details open><summary><b><code>igualdad</code> — 31,94 M€ (31.937.149 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 20.550.822 | 64,3 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 11.386.327 | 35,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.093,63 M€ · 43 códigos · 22,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.414.754.328 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 260.237.239 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 174.073.340 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 172.289.395 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 168.374.065 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 148.924.139 |
| `461B` | RADIODIFUSIÓN E TVG | 121.920.456 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 71.615.469 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 69.866.799 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 57.098.719 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 57.062.253 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 51.413.350 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 44.071.633 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 29.008.970 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 22.098.341 |
| `111B` | ACTIVIDADE LEXISLATIVA | 21.476.000 |
| `141A` | ADMINISTRACIÓN LOCAL | 20.063.728 |
| `511A` | DIRECCIÓN E SERVIZOS XERAIS DE TERRITORIO E INFRAESTRUTURAS | 19.983.980 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 16.048.315 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 15.300.301 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 14.317.039 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 13.500.000 |
| `151A` | FOMENTO DA LINGUA GALEGA | 10.907.619 |
| `331A` | COOPERACIÓN EXTERIOR E AO DESENVOLVEMENTO | 8.915.485 |
| `731A` | DIRECCIÓN E SERVIZOS XERAIS DE INDUSTRIA | 8.687.022 |
| … | *resto: 18 códigos* | 81.619.834 |

</details>

### 2024

*Fuente: `progr.pdf` · 107 líneas · total extraído **14.519,61 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.379,51 M€ (5.379.507.186 €) · 7 códigos · 37,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 4.836.550.669 | 89,9 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 242.235.814 | 4,5 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 99.567.998 | 1,9 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 95.519.281 | 1,8 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 93.243.521 | 1,7 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 10.545.094 | 0,2 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 1.844.809 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.951,53 M€ (2.951.527.495 €) · 12 códigos · 20,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 1.002.312.571 | 34,0 % |
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 970.012.702 | 32,9 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 409.452.056 | 13,9 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 237.298.505 | 8,0 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 104.117.980 | 3,5 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 60.924.561 | 2,1 % |
| `422D` | EDUCACIÓN ESPECIAL | 57.480.972 | 1,9 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 44.812.781 | 1,5 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 29.807.234 | 1,0 % |
| `422G` | ENSINANZAS ESPECIAIS | 21.298.195 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 10.582.421 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.427.517 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 794,89 M€ (794.886.909 €) · 18 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 159.319.147 | 20,0 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 127.644.855 | 16,1 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 87.855.683 | 11,1 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 71.681.077 | 9,0 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 64.175.620 | 8,1 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 61.925.479 | 7,8 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 41.668.572 | 5,2 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 40.399.119 | 5,1 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 32.902.803 | 4,1 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 31.704.060 | 4,0 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 20.766.667 | 2,6 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 11.810.877 | 1,5 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 11.270.500 | 1,4 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 9.740.439 | 1,2 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 9.060.614 | 1,1 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 8.604.600 | 1,1 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.236.797 | 0,4 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 1.120.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 6,26 M€ (6.262.890 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 6.262.890 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 189,96 M€ (189.958.097 €) · 4 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 117.158.158 | 61,7 % |
| `451B` | ACCESO Á VIVENDA | 43.540.682 | 22,9 % |
| `521A` | URBANISMO | 18.361.646 | 9,7 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 10.897.611 | 5,7 % |

</details>

<details open><summary><b><code>empleo</code> — 449,79 M€ (449.785.825 €) · 8 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 138.352.338 | 30,8 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 136.997.508 | 30,5 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 82.866.808 | 18,4 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 43.645.333 | 9,7 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 24.887.296 | 5,5 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 12.601.857 | 2,8 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 9.679.165 | 2,2 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 421,99 M€ (421.986.307 €) · 3 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 213.920.597 | 50,7 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 155.428.678 | 36,8 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 52.637.032 | 12,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 715,95 M€ (715.948.712 €) · 2 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 655.478.910 | 91,6 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 60.469.802 | 8,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 55,16 M€ (55.159.820 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 55.159.820 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 17,25 M€ (17.254.574 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 17.254.574 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 22,40 M€ (22.396.775 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 22.396.775 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 235,11 M€ (235.111.676 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 141.030.605 | 60,0 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 43.183.813 | 18,4 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 29.005.963 | 12,3 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 21.891.295 | 9,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 40,00 M€ (40.003.586 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 23.521.894 | 58,8 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 16.481.692 | 41,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.239,83 M€ · 43 códigos · 22,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.511.235.389 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 257.261.901 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 179.754.339 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 170.440.919 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 162.108.874 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 158.127.792 |
| `461B` | RADIODIFUSIÓN E TVG | 125.490.819 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 87.695.295 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 76.817.965 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMINISTRACIÓN XERAL | 71.122.666 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 56.225.913 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 49.289.103 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 42.894.467 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 30.447.067 |
| `111B` | ACTIVIDADE LEXISLATIVA | 22.693.000 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 22.347.764 |
| `141A` | ADMINISTRACIÓN LOCAL | 20.093.598 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 17.502.033 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 16.327.607 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 14.954.289 |
| `161A` | ELECCIÓNS E PARTIDOS POLÍTICOS | 14.142.356 |
| `151A` | FOMENTO DA LINGUA GALEGA | 11.049.009 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 11.000.000 |
| `124A` | DIRECCIÓN, MODERNIZACIÓN E XESTIÓN DA FUNCIÓN PUBLICA | 9.473.629 |
| `331A` | COOPERACIÓN EXTERIOR E AO DESENVOLVEMENTO | 8.939.434 |
| … | *resto: 18 códigos* | 92.389.901 |

</details>

### 2025

*Fuente: `progr.pdf` · 108 líneas · total extraído **15.462,69 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.675,37 M€ (5.675.373.515 €) · 7 códigos · 36,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 5.109.379.633 | 90,0 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 262.725.432 | 4,6 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 104.086.547 | 1,8 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 97.993.788 | 1,7 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 89.046.511 | 1,6 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 9.510.410 | 0,2 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 2.631.194 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 3.065,99 M€ (3.065.989.649 €) · 12 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 1.045.647.295 | 34,1 % |
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 1.029.286.030 | 33,6 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 432.181.810 | 14,1 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 239.979.324 | 7,8 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 106.363.145 | 3,5 % |
| `422D` | EDUCACIÓN ESPECIAL | 60.288.757 | 2,0 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 46.026.584 | 1,5 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 39.420.700 | 1,3 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 30.247.218 | 1,0 % |
| `422G` | ENSINANZAS ESPECIAIS | 21.953.505 | 0,7 % |
| `422K` | ENSINANZAS PESQUEIRAS | 11.312.915 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.282.366 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 844,48 M€ (844.475.573 €) · 19 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 181.588.385 | 21,5 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 137.500.331 | 16,3 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 86.570.314 | 10,3 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 76.366.985 | 9,0 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 66.744.590 | 7,9 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 55.652.279 | 6,6 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 41.293.847 | 4,9 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 40.993.454 | 4,9 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 35.451.465 | 4,2 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 25.911.659 | 3,1 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 20.420.000 | 2,4 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 15.177.628 | 1,8 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 12.242.396 | 1,4 % |
| `531A` | PROMOCIÓN DE SOLO PARA ACTIVIDADES ECONÓMICAS | 11.161.022 | 1,3 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 11.150.000 | 1,3 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 11.125.517 | 1,3 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 11.006.876 | 1,3 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.418.825 | 0,4 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 700.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 6,71 M€ (6.709.836 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 6.709.836 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 236,49 M€ (236.492.482 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 143.920.704 | 60,9 % |
| `451B` | ACCESO Á VIVENDA | 60.959.804 | 25,8 % |
| `521A` | URBANISMO | 20.007.107 | 8,5 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 11.604.867 | 4,9 % |

</details>

<details open><summary><b><code>empleo</code> — 447,69 M€ (447.693.569 €) · 8 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 137.924.248 | 30,8 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 134.901.345 | 30,1 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 72.232.081 | 16,1 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 44.853.618 | 10,0 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 25.885.970 | 5,8 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 19.827.346 | 4,4 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 11.313.441 | 2,5 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 755.520 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 411,41 M€ (411.410.747 €) · 3 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 206.700.423 | 50,2 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 155.756.808 | 37,9 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 48.953.516 | 11,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 797,67 M€ (797.667.697 €) · 2 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 728.316.051 | 91,3 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 69.351.646 | 8,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 55,91 M€ (55.914.419 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 55.914.419 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 22,15 M€ (22.154.490 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 22.154.490 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 24,02 M€ (24.023.714 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 24.023.714 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 241,00 M€ (240.999.890 €) · 4 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 143.183.803 | 59,4 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 45.449.994 | 18,9 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 30.638.248 | 12,7 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 21.727.845 | 9,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 44,04 M€ (44.039.145 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 26.467.046 | 60,1 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 17.572.099 | 39,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.589,74 M€ · 43 códigos · 23,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.763.489.507 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 240.699.429 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 195.807.107 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 192.521.425 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 175.903.858 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 168.056.605 |
| `461B` | RADIODIFUSIÓN E TVG | 129.811.800 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 98.788.191 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 87.096.450 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMON XERAL E PERIFERICA DA XUNTA DE GALICIA | 74.486.646 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 52.683.420 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 48.541.866 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 40.153.725 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 39.144.901 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 30.885.771 |
| `111B` | ACTIVIDADE LEXISLATIVA | 25.097.000 |
| `141A` | ADMINISTRACIÓN LOCAL | 22.692.362 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 22.159.824 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 19.517.921 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 18.085.022 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 12.292.038 |
| `151A` | FOMENTO DA LINGUA GALEGA | 11.964.171 |
| `541A` | DIRECCIÓN E SERVIZOS XERAIS DE MEDIO AMBIENTE | 11.421.174 |
| `111C` | CONTROL EXTERNO DO SECTOR PÚBLICO | 9.921.639 |
| `124A` | DIRECCIÓN, MODERNIZACIÓN E XESTIÓN DA FUNCIÓN PUBLICA | 9.866.678 |
| … | *resto: 18 códigos* | 88.653.811 |

</details>

### 2026

*Fuente: `progr.pdf` · 108 líneas · total extraído **16.044,89 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 5.840,97 M€ (5.840.969.114 €) · 7 códigos · 36,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411A` | DIRECCIÓN E SERVIZOS XERAIS DE SANIDADE | 5.314.043.791 | 91,0 % |
| `312B` | PROGRAMAS DE PRESTACIÓNS ÁS FAMILIAS E Á INFANCIA | 253.379.935 | 4,3 % |
| `413A` | PROTECCIÓN E PROMOCIÓN DA SAÚDE PÚBLICA | 112.444.512 | 1,9 % |
| `312A` | PROTECCIÓN E INSERCIÓN SOCIAL | 91.279.929 | 1,6 % |
| `311A` | DIRECCIÓN E SERVIZOS XERAIS DE PROMOCIÓN SOCIAL | 58.299.598 | 1,0 % |
| `312G` | APOIO Á CONCILIACIÓN DA VIDA LABORAL E PERSOAL E OUTROS SERVIZOS DE PROTECCIÓN | 9.481.499 | 0,2 % |
| `312F` | PROGRAMAS DE SOLIDARIEDADE | 2.039.850 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 3.125,91 M€ (3.125.909.375 €) · 12 códigos · 19,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422M` | ENSINANZA SECUNDARIA , FORMACIÓN PROFESIONAL E OUTRAS ENSINANZAS | 1.053.006.153 | 33,7 % |
| `422A` | EDUCACIÓN INFANTIL, PRIMARIA E ESO | 1.045.584.339 | 33,4 % |
| `422C` | ENSINANZAS UNIVERSITARIAS | 440.367.764 | 14,1 % |
| `423A` | SERVIZOS E AXUDAS COMPLEMENTARIAS DA ENSINANZA | 249.982.383 | 8,0 % |
| `561B` | INVESTIGACIÓN UNIVERSITARIA | 118.576.744 | 3,8 % |
| `422D` | EDUCACIÓN ESPECIAL | 61.925.276 | 2,0 % |
| `422E` | ENSINANZAS ARTÍSTICAS | 46.594.398 | 1,5 % |
| `421A` | DIRECCIÓN E SERVIZOS XERAIS DE EDUCACIÓN | 41.542.173 | 1,3 % |
| `423B` | PREVENCIÓN DO ABANDONO ESCOLAR | 28.966.412 | 0,9 % |
| `422G` | ENSINANZAS ESPECIAIS | 23.705.919 | 0,8 % |
| `422K` | ENSINANZAS PESQUEIRAS | 12.384.249 | 0,4 % |
| `422I` | FORMACIÓN E PERFECCIONAMENTO DO PROFESORADO | 3.273.565 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 859,68 M€ (859.679.318 €) · 19 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `551B` | ACCIÓNS PREVENTIVAS E INFRAESTRUTURA FORESTAL | 213.845.611 | 24,9 % |
| `712B` | MODERNIZACIÓN E DIVERSIFICACIÓN DO TECIDO PRODUTIVO RURAL | 129.169.081 | 15,0 % |
| `713B` | ORDENACIÓN DAS PRODUCIÓNS FORESTAIS | 85.710.980 | 10,0 % |
| `723A` | COMPETITIV. E MELLORA DA CALIDADE DA PROD. PESQUEIRA E DA ACUICULTURA | 72.477.617 | 8,4 % |
| `713E` | BENESTAR ANIMAL E SANIDADE VEXETAL | 63.185.487 | 7,3 % |
| `712A` | FIXACIÓN DE POBOACIÓN NO MEDIO RURAL | 54.185.205 | 6,3 % |
| `541C` | PROTECCIÓN, CONTROL TÉCNICO- SANITARIO DOS PRODUTOS DO MAR,MELLORA DO MEDIO | 42.056.904 | 4,9 % |
| `723B` | REGULACIÓN DAS PRODUCIÓNS E DOS MERCADOS DA PESCA | 38.081.815 | 4,4 % |
| `551A` | INFRAESTRUTURAS E EQUIPAMENTOS NO MEDIO RURAL | 37.083.808 | 4,3 % |
| `711A` | DIRECCIÓN E SERVIZOS XERAIS DO MEDIO RURAL | 34.450.189 | 4,0 % |
| `723C` | DESENVOLVEMENTO SOSTIBLE DAS ZOAS DE PESCA | 22.925.310 | 2,7 % |
| `721A` | DIRECCIÓN E SERVIZOS XERAIS DE POLÍTICAS PESQUEIRAS | 12.902.982 | 1,5 % |
| `713F` | REGULACIÓNS DAS PRODUCIÓNS AGRARIAS E APOIO Á RENDA DOS AGRICULTORES | 10.634.322 | 1,2 % |
| `531A` | PROMOCIÓN DE SOLO PARA ACTIVIDADES ECONÓMICAS | 10.521.283 | 1,2 % |
| `713D` | MELLORA DA CALIDADE NA PRODUCIÓN AGROALIMENTARIA | 9.618.669 | 1,1 % |
| `514A` | INFRAESTRUTURAS PESQUEIRAS | 9.500.000 | 1,1 % |
| `713C` | IMPLANTACIÓN DE SISTEMAS PRODUTIVOS AGRARIOS SUSTENTABLES | 8.691.122 | 1,0 % |
| `722A` | PROMOCIÓN SOCIAL E DIVULGACIÓN DA TECNOLOXÍA PESQUEIRA. | 3.766.288 | 0,4 % |
| `712C` | FOMENTO DO ASOCIACIONISMO AGRARIO E DIVULGACIÓN DA TECNOLOXÍA AGRARIA | 872.645 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 6,97 M€ (6.968.374 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `111A` | PRESIDENCIA DA XUNTA DE GALICIA | 6.968.374 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 287,55 M€ (287.554.167 €) · 4 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | FOMENTO DA REHABILITACIÓN E DA CALIDADE DA VIVENDA | 179.375.736 | 62,4 % |
| `451B` | ACCESO Á VIVENDA | 76.527.052 | 26,6 % |
| `521A` | URBANISMO | 19.810.328 | 6,9 % |
| `431A` | DIRECCIÓN E SERVIZOS XERAIS DE CULTURA | 11.841.051 | 4,1 % |

</details>

<details open><summary><b><code>empleo</code> — 445,73 M€ (445.727.681 €) · 8 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | PROMOCIÓN DO EMPREGO, DO EMPREGO AUTÓNOMO E DO MERCADO DE TRABALLO INCLUSIVO | 138.683.776 | 31,1 % |
| `323A` | FORMACIÓN PROFESIONAL DESEMPREGADOS | 131.990.145 | 29,6 % |
| `322A` | MELLORA E FOMENTO DA EMPREGABILIDADE | 71.916.628 | 16,1 % |
| `324C` | PROMOCIÓN DA ECONOMIA SOCIAL | 44.714.562 | 10,0 % |
| `324A` | MELLORA DA ORGANIZACIÓN E ADMINISTRACIÓN DAS RELACIÓNS LABORAIS E DA PREVENCIÓN | 26.191.934 | 5,9 % |
| `323B` | FORMACIÓN PROFESIONAL DE OCUPADOS | 20.660.745 | 4,6 % |
| `321A` | DIRECCIÓN E SERVIZOS XERAIS DE EMPREGO | 10.777.432 | 2,4 % |
| `324B` | MELLORA DOS SISTEMAS DE SAÚDE E SEGURIDADE NO TRABALLO | 792.459 | 0,2 % |

</details>

<details open><summary><b><code>idi</code> — 369,02 M€ (369.020.937 €) · 3 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561A` | PLAN GALEGO DE INVESTIGACIÓN, DESENVOLVEMENTO E INNOVACIÓN TECNOLÓXICA | 181.886.255 | 49,3 % |
| `571A` | FOMENTO DA SOCIEDADE DA INFORMACIÓN E DO COÑECEMENTO | 136.099.365 | 36,9 % |
| `542A` | PLANIFICACIÓN E XESTIÓN HIDROLÓXICA | 51.035.317 | 13,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 910,93 M€ (910.929.100 €) · 2 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312D` | PROGRAMA DE ATENCIÓN Á DEPENDENCIA | 844.928.975 | 92,8 % |
| `312E` | PROMOCIÓN DA AUTONOMÍA PERSOAL E PREVENCION DA DEPENDENCIA PARA PERSOAS CON | 66.000.125 | 7,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 53,47 M€ (53.470.252 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313C` | SERVIZOS SOCIAIS COMUNITARIOS | 53.470.252 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 24,89 M€ (24.889.913 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | SERVIZOS Á XUVENTUDE | 24.889.913 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 25,35 M€ (25.350.060 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312C` | SERVIZOS SOCIAIS RELATIVOS ÁS MIGRACIÓNS | 25.350.060 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 221,48 M€ (221.476.344 €) · 4 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `761A` | POTENCIACIÓN E PROMOCIÓN DO TURISMO | 122.750.028 | 55,4 % |
| `432B` | FOMENTO DAS ACTIVIDADES CULTURAIS | 44.623.908 | 20,1 % |
| `432A` | BIBLIOTECAS, ARQUIVOS, MUSEOS E EQUIPAMENTOS CULTURAIS | 31.390.158 | 14,2 % |
| `751A` | ORDENACIÓN, REGULACIÓN E PROMOCIÓN DO COMERCIO INTERIOR DE GALICIA | 22.712.250 | 10,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 43,96 M€ (43.963.956 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | PROTECCIÓN E APOIO ÁS MULLERES QUE SOFREN VIOLENCIA DE XÉNERO | 25.320.082 | 57,6 % |
| `313B` | ACCIÓNS PARA A IGUALDADE, PROTECCIÓN E PROMOCIÓN DA MULLER | 18.643.874 | 42,4 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.828,99 M€ · 43 códigos · 23,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `911A` | AMORTIZACIÓN E GASTOS FINANCEIROS DA DÉBEDA PÚBLICA | 1.858.585.440 |
| `512B` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN DE ESTRADAS | 243.857.578 |
| `741A` | APOIO Á MODERNIZACIÓN, INTERNACIONALIZACIÓN E MELLORA DA COMPETITIVADE, | 207.199.486 |
| `131A` | ADMINISTRACIÓN DE XUSTIZA | 197.058.395 |
| `811B` | TRANSF. A ENTIDADES LOCAIS POR PARTICIPACIÓN NOS INGRESOS DA COMUNIDADE AUTÓNOMA | 187.314.115 |
| `621B` | IMPREVISTOS E FUNCIÓNS NON CLASIFICADAS | 171.171.018 |
| `461B` | RADIODIFUSIÓN E TVG | 134.571.800 |
| `733A` | EFICIENCIA ENERXÉTICA E ENERXÍAS RENOVABLES | 128.201.188 |
| `621A` | ADMINISTRACIÓN FINANCEIRA, TRIBUTARIA, PATRIMONIAL E DE CONTROL. | 97.699.899 |
| `121A` | DIRECCIÓN E SERVIZOS XERAIS DE ADMON XERAL E PERIFERICA DA XUNTA DE GALICIA | 73.221.776 |
| `512A` | ORDENACIÓN E INSPECCIÓN DO TRANSPORTE | 64.093.374 |
| `541B` | CONSERVACIÓN DA BIODIVERSIDADE E POSTA EN VALOR DO MEDIO NATURAL | 48.684.387 |
| `212A` | PROTECCIÓN CIVIL E SEGURIDADE DA COMUNIDADE AUTÓNOMA | 42.837.818 |
| `441A` | PROMOCIÓN DA ACTIVIDADE DEPORTIVA | 41.807.420 |
| `541E` | COÑECEMENTO DO MEDIO AMBIENTE E FOMENTO DA SUSTENTABILIDADE | 33.846.596 |
| `541D` | CONTROL AMBIENTAL E XESTIÓN DE RESIDUOS | 32.231.268 |
| `141A` | ADMINISTRACIÓN LOCAL | 26.546.087 |
| `111B` | ACTIVIDADE LEXISLATIVA | 25.901.000 |
| `433A` | PROTECCIÓN E PROMOCIÓN DO PATRIMONIO HISTÓRICO, ARTÍSTICO ECULTURAL | 22.194.912 |
| `732A` | REGULACIÓN E SOPORTE DA ACTIVIDADE INDUSTRIAL | 21.032.649 |
| `611A` | DIRECCIÓN E SERVIZOS XERAIS DE FACENDA | 19.439.384 |
| `151A` | FOMENTO DA LINGUA GALEGA | 13.008.030 |
| `811C` | OUTROS SOPORTES FINANCEIROS ÁS ENTIDADES LOCAIS | 13.000.000 |
| `513A` | CONSTRUCIÓN, CONSERVACIÓN E EXPLOTACIÓN PORTUARIA | 12.408.573 |
| `124A` | DIRECCIÓN, MODERNIZACIÓN E XESTIÓN DA FUNCIÓN PUBLICA | 10.648.235 |
| … | *resto: 18 códigos* | 102.425.299 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py gal     # regenera este documento
python3 tools/auditoria_magnitud.py gal        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa gal --anio <año> \
    --input ../fuentes/raw/gal/<año>/<fichero> --output /tmp/gal.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-gal.md`](limitaciones-gal.md)

