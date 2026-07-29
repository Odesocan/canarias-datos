# Trazabilidad de la extracción — Extremadura (`ext`)

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
| **2015** | 78 | `ley_doe.pdf` | 11 | 50,0 % | 5.365,70 | — | no_aplica |
| **2016** | 77 | `ley_doe.pdf` | 11 | 50,6 % | 5.197,43 | — | no_aplica |
| **2017** | 77 | `ley_doe.pdf` | 11 | 50,6 % | 5.171,63 | — | no_aplica |
| **2018** | 77 | `ley_doe.pdf` | 11 | 50,6 % | 5.433,98 | — | no_aplica |
| **2019** | 77 | `ley_doe.pdf` | 11 | 50,6 % | 5.797,95 | — | no_aplica |
| **2020** | 80 | `ley_doe.pdf` | 11 | 50,0 % | 6.006,65 | — | no_aplica |
| **2021** | 80 | `ley_doe.pdf` | 11 | 50,0 % | 6.423,89 | — | no_aplica |
| **2022** | 79 | `ley_doe.pdf` | 11 | 50,6 % | 6.984,51 | — | no_aplica |
| **2023** | 81 | `ley_doe.pdf` | 11 | 49,4 % | 7.781,09 | — | no_aplica |
| **2024** | 79 | `ley_doe.pdf` | 11 | 49,4 % | 8.127,11 | — | no_aplica |
| **2025** | 79 | `ley_doe.pdf` | 11 | 49,4 % | 8.127,11 | — | no_aplica |
| **2026** | 79 | `ley_doe.pdf` | 11 | 49,4 % | 8.127,11 | — | no_aplica |

**URL(s) de origen:**
- <https://doe.juntaex.es/pdfs/doe/2014/2510o/14010015.pdf>
- <https://doe.juntaex.es/pdfs/doe/2016/670o/16010003.pdf>
- <https://doe.juntaex.es/pdfs/doe/2017/10e/17010001.pdf>
- <https://doe.juntaex.es/pdfs/doe/2018/170o/170o.pdf>
- <https://doe.juntaex.es/pdfs/doe/2019/160o/19010002.pdf>
- <https://doe.juntaex.es/pdfs/doe/2020/220o/20010001.pdf>
- <https://doe.juntaex.es/pdfs/doe/2021/240o/21010001.pdf>
- <https://doe.juntaex.es/pdfs/doe/2021/2510o/21010004.pdf>
- <https://doe.juntaex.es/pdfs/doe/2022/30e/22010006.pdf>
- <https://doe.juntaex.es/pdfs/doe/2024/260o/24010001.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 1.376,86 | 1.550,10 | 1.539,07 | 1.603,96 | 1.691,12 | 1.742,52 | 1.876,52 | 2.008,51 | 2.204,30 | 2.282,10 | 2.282,10 | 2.282,10 |
| `educacion` | 1.026,17 | 1.021,73 | 1.022,16 | 1.047,13 | 1.078,97 | 1.110,31 | 1.200,75 | 1.240,87 | 1.316,84 | 1.384,37 | 1.384,37 | 1.384,37 |
| `soberania` | 1.008,36 | 867,73 | 909,49 | 918,23 | 940,78 | 957,92 | 1.002,34 | 1.000,41 | 1.074,52 | 1.137,03 | 1.137,03 | 1.137,03 |
| `direccion` | 7,67 | 6,78 | 6,30 | 6,24 | 6,22 | 6,03 | 6,08 | 5,85 | 7,92 | 11,67 | 11,67 | 11,67 |
| `vivienda` | 48,23 | 48,46 | 44,15 | 50,31 | 64,57 | 63,79 | 70,71 | 84,77 | 134,26 | 142,68 | 142,68 | 142,68 |
| `empleo` | 244,12 | 256,41 | 269,57 | 307,54 | 313,36 | 327,30 | 343,36 | 393,16 | 400,62 | 407,92 | 407,92 | 407,92 |
| `idi` | 107,27 | 107,59 | 108,45 | 109,95 | 120,61 | 107,12 | 117,65 | 152,26 | 172,00 | 162,08 | 162,08 | 162,08 |
| `dependencia` | 295,12 | 301,02 | 309,63 | 318,00 | 330,61 | 347,14 | 360,67 | 412,18 | 459,48 | 485,78 | 485,78 | 485,78 |
| `diversidad` | 0,85 | 0,78 | 0,78 | 0,84 | 0,80 | 0,84 | 0,84 | 0,84 | 0,86 | 0,91 | 0,91 | 0,91 |
| `turismo` | 35,57 | 23,48 | 22,43 | 23,08 | 23,69 | 25,05 | 26,43 | 27,20 | 29,69 | 41,55 | 41,55 | 41,55 |
| `igualdad` | 6,23 | 8,05 | 8,44 | 8,78 | 10,83 | 11,57 | 14,99 | 25,06 | 27,56 | 30,08 | 30,08 | 30,08 |
| **Σ asignado** | 4.156,46 | 4.192,12 | 4.240,48 | 4.394,07 | 4.581,57 | 4.699,60 | 5.020,33 | 5.351,11 | 5.828,04 | 6.086,16 | 6.086,16 | 6.086,16 |
| *(sin concepto)* | 1.209,24 | 1.005,31 | 931,15 | 1.039,91 | 1.216,37 | 1.307,05 | 1.403,56 | 1.633,41 | 1.953,05 | 2.040,95 | 2.040,95 | 2.040,95 |
| **TOTAL extraído** | 5.365,70 | 5.197,43 | 5.171,63 | 5.433,98 | 5.797,95 | 6.006,65 | 6.423,89 | 6.984,51 | 7.781,09 | 8.127,11 | 8.127,11 | 8.127,11 |

**Conceptos sin ninguna línea en toda la serie:** `discapacidad`, `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +12,6 % | −0,7 % | +4,2 % | +5,4 % | +3,0 % | +7,7 % | +7,0 % | +9,7 % | +3,5 % | +0,0 % | +0,0 % |
| `educacion` | −0,4 % | +0,0 % | +2,4 % | +3,0 % | +2,9 % | +8,1 % | +3,3 % | +6,1 % | +5,1 % | +0,0 % | +0,0 % |
| `soberania` | −13,9 % | +4,8 % | +1,0 % | +2,5 % | +1,8 % | +4,6 % | −0,2 % | +7,4 % | +5,8 % | +0,0 % | +0,0 % |
| `direccion` | −11,6 % | −7,0 % | −0,9 % | −0,3 % | −3,2 % | +0,9 % | −3,8 % | +35,5 % | +47,3 % ⚠ | +0,0 % | +0,0 % |
| `vivienda` | +0,5 % | −8,9 % | +14,0 % | +28,3 % | −1,2 % | +10,8 % | +19,9 % | +58,4 % ⚠ | +6,3 % | +0,0 % | +0,0 % |
| `empleo` | +5,0 % | +5,1 % | +14,1 % | +1,9 % | +4,4 % | +4,9 % | +14,5 % | +1,9 % | +1,8 % | +0,0 % | +0,0 % |
| `idi` | +0,3 % | +0,8 % | +1,4 % | +9,7 % | −11,2 % | +9,8 % | +29,4 % | +13,0 % | −5,8 % | +0,0 % | +0,0 % |
| `dependencia` | +2,0 % | +2,9 % | +2,7 % | +4,0 % | +5,0 % | +3,9 % | +14,3 % | +11,5 % | +5,7 % | +0,0 % | +0,0 % |
| `diversidad` | −8,1 % | +0,3 % | +8,1 % | −5,7 % | +5,9 % | −0,0 % | +0,3 % | +1,5 % | +6,1 % | +0,0 % | +0,0 % |
| `turismo` | −34,0 % | −4,5 % | +2,9 % | +2,6 % | +5,7 % | +5,5 % | +2,9 % | +9,2 % | +39,9 % | +0,0 % | +0,0 % |
| `igualdad` | +29,1 % | +4,9 % | +4,0 % | +23,4 % | +6,8 % | +29,6 % | +67,1 % ⚠ | +10,0 % | +9,1 % | +0,0 % | +0,0 % |
| **TOTAL** | −3,1 % | −0,5 % | +5,1 % | +6,7 % | +3,6 % | +6,9 % | +8,7 % | +11,4 % | +4,4 % | +0,0 % | +0,0 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2023 | `vivienda` | **SALTO** | 84,77 → 134,26 M€ (+58,4 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (1 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `321A` | 16,17 | 2015:idi, 2016:idi, 2017:idi, 2018:idi, 2019:idi, 2020:educacion, 2021:educacion, 2022:idi, 2023:idi, 2024:educacion, 2025:educacion, 2026:educacion |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `ley_doe.pdf` · 78 líneas · total extraído **5.365,70 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.376,86 M€ (1.376.856.967 €) · 6 códigos · 25,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | Atención especializada de salud | 784.476.998 | 57,0 % |
| `212B` | Atención primaria de salud | 508.455.180 | 36,9 % |
| `211A` | Dirección y administración de Sanidad | 42.709.934 | 3,1 % |
| `211B` | Formación, inspección y calidad sanitarias | 30.961.470 | 2,2 % |
| `212D` | Salud pública | 7.659.484 | 0,6 % |
| `212A` | Planificación y ordenación sanitarias | 2.593.901 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.026,17 M€ (1.026.174.925 €) · 10 códigos · 19,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | Educación secundaria y formación profesional | 353.391.049 | 34,4 % |
| `222A` | Educación infantil y primaria | 347.161.673 | 33,8 % |
| `222G` | Actividades complementar. y ayudas a la enseñanza | 110.081.824 | 10,7 % |
| `222D` | Enseñanzas universitarias | 106.178.346 | 10,3 % |
| `222C` | Educación especial, enseñanzas artístic. e idiomas | 54.134.201 | 5,3 % |
| `222E` | Educac. permanente y a distancia no universitaria | 15.736.136 | 1,5 % |
| `221A` | Dirección y administración de Educación | 15.551.585 | 1,5 % |
| `222F` | Enseñanza agraria | 11.465.011 | 1,1 % |
| `322A` | Ordenación industrial y desarrollo energético | 6.344.891 | 0,6 % |
| `221B` | Formación del profesorado de Educación | 6.130.209 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 1.008,36 M€ (1.008.359.989 €) · 7 códigos · 18,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Regulación de producciones | 601.569.742 | 59,7 % |
| `353A` | Infraestructuras agrarias | 193.035.316 | 19,1 % |
| `323C` | Empresa agroalimentaria | 83.099.360 | 8,2 % |
| `314A` | Desarrollo del medio rural | 52.007.143 | 5,2 % |
| `312A` | Sanidad vegetal y animal | 30.268.443 | 3,0 % |
| `312B` | Competitividad y calidad produc. agríc. y ganadera | 26.768.956 | 2,7 % |
| `311A` | Dirección y administración de Agricultura | 21.611.029 | 2,1 % |

</details>

<details open><summary><b><code>direccion</code> — 7,67 M€ (7.668.529 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y administración de Presidencia | 7.668.529 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 48,23 M€ (48.234.914 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Promoción y ayudas para el acceso a la vivienda | 38.809.740 | 80,5 % |
| `262A` | Urbanismo y ordenación del territorio | 9.425.174 | 19,5 % |

</details>

<details open><summary><b><code>empleo</code> — 244,12 M€ (244.119.405 €) · 4 códigos · 4,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | Fomento y calidad en el empleo | 152.335.054 | 62,4 % |
| `242B` | Formación para el empleo | 66.096.715 | 27,1 % |
| `241A` | Dirección y admón. de Empleo y Políticas Sociales | 19.637.768 | 8,0 % |
| `325A` | Relaciones laborales y condiciones de trabajo | 6.049.868 | 2,5 % |

</details>

<details open><summary><b><code>idi</code> — 107,27 M€ (107.270.160 €) · 4 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | Investigación, desarrollo tecnológico e innovación | 62.002.307 | 57,8 % |
| `332A` | Tecnologías de la información y las comunicaciones | 35.228.112 | 32,8 % |
| `331A` | Investigación y experimentación agraria | 5.677.967 | 5,3 % |
| `321A` | Dir. y admón. de Empresa e Innovación | 4.361.774 | 4,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 295,12 M€ (295.124.175 €) · 2 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | Atención a la dependencia | 291.781.137 | 98,9 % |
| `231A` | Dirección y administración de Dependencia | 3.343.038 | 1,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,85 M€ (846.674 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | Acciones en materia de emigración | 846.674 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 35,57 M€ (35.571.564 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | Ordenación y promoción del turismo | 35.571.564 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,23 M€ (6.230.830 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | Igualdad de oportunidades | 6.230.830 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.209,24 M€ · 39 códigos · 22,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | Amortizac. y gastos financ. del endeudam. público | 479.307.563 |
| `353B` | Infraestructuras de carreteras | 68.249.253 |
| `354C` | Conservación, protección y mejora de los montes | 58.913.603 |
| `252B` | Inclusión social | 57.426.651 |
| `323A` | Desarrollo empresarial | 51.234.475 |
| `354A` | Medio natural y calidad ambiental | 50.527.994 |
| `353C` | Ordenación e inspección del transporte | 46.572.263 |
| `115B` | Relaciones con la administración local | 42.735.991 |
| `354D` | Saneamiento y abastecimiento de aguas | 42.513.644 |
| `252A` | Atención a la infancia y a las familias | 39.577.290 |
| `354B` | Protección y defensa contra los incendios | 37.371.311 |
| `115A` | Relaciones institucionales e informativas | 26.725.863 |
| `341A` | Comercio de calidad y artesanía extremeña | 19.705.748 |
| `274A` | Fomento y apoyo de las actividades deportivas | 16.048.927 |
| `111A` | Actividad legislativa | 14.500.000 |
| `252C` | Cooperación al desarrollo y acción exterior | 13.132.322 |
| `272A` | Protección del patrimonio histórico-artístico | 13.071.948 |
| `273A` | Promoción y cooperación cultural | 12.260.664 |
| `113A` | Dirección de Administración y Hacienda Públicas | 11.521.688 |
| `351A` | Dirección y administración de Fomento | 10.529.388 |
| `272B` | Bibliotecas y archivos | 9.456.462 |
| `131B` | Fondo de contingencia | 9.114.267 |
| `273B` | Teatro, música y cine | 9.047.991 |
| `272C` | Museos y artes plásticas | 7.660.079 |
| `333A` | Energía renovable y eficiencia energética | 7.554.660 |
| … | *resto: 14 códigos* | 54.481.383 |

</details>

### 2016

*Fuente: `ley_doe.pdf` · 77 líneas · total extraído **5.197,43 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.550,10 M€ (1.550.101.891 €) · 6 códigos · 29,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | Atención especializada de salud | 837.681.381 | 54,0 % |
| `212B` | Atención primaria de salud | 621.196.979 | 40,1 % |
| `211A` | Dirección y administración de Sanidad | 49.242.461 | 3,2 % |
| `211B` | Formación, inspección y calidad sanitarias | 30.107.452 | 1,9 % |
| `212D` | Salud pública | 8.255.390 | 0,5 % |
| `212A` | Planificación y ordenación sanitarias | 3.618.228 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.021,73 M€ (1.021.730.086 €) · 10 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | Educación secundaria y formación profesional | 379.060.391 | 37,1 % |
| `222A` | Educación infantil y primaria | 362.282.385 | 35,5 % |
| `222D` | Enseñanzas universitarias | 102.205.943 | 10,0 % |
| `222G` | Actividades complementar. y ayudas a la enseñanza | 63.713.509 | 6,2 % |
| `222C` | Educación especial, enseñanzas artístic. e idiomas | 58.286.418 | 5,7 % |
| `221A` | Dirección y administración de Educación | 16.771.114 | 1,6 % |
| `222E` | Educac. permanente y a distancia no universitaria | 16.680.927 | 1,6 % |
| `222F` | Enseñanza agraria | 10.411.241 | 1,0 % |
| `221B` | Formación del profesorado de Educación | 6.780.253 | 0,7 % |
| `322A` | Ordenación industrial y desarrollo energético | 5.537.905 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 867,73 M€ (867.731.588 €) · 7 códigos · 16,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Regulación de producciones | 601.807.389 | 69,4 % |
| `353A` | Infraestructuras agrarias | 129.978.745 | 15,0 % |
| `312B` | Competitividad y calidad produc. agríc. y ganadera | 32.316.793 | 3,7 % |
| `312A` | Sanidad vegetal y animal | 31.980.874 | 3,7 % |
| `311A` | Dirección y administración de Agricultura | 27.687.657 | 3,2 % |
| `314A` | Desarrollo del medio rural | 22.379.643 | 2,6 % |
| `323C` | Empresa agroalimentaria | 21.580.487 | 2,5 % |

</details>

<details open><summary><b><code>direccion</code> — 6,78 M€ (6.775.405 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y administración de Presidencia | 6.775.405 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 48,46 M€ (48.458.475 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Promoción y ayudas para el acceso a la vivienda | 39.821.947 | 82,2 % |
| `262A` | Urbanismo, arquitectura y ordenac. del territorio | 8.636.528 | 17,8 % |

</details>

<details open><summary><b><code>empleo</code> — 256,41 M€ (256.405.996 €) · 4 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | Fomento y calidad en el empleo | 161.683.105 | 63,1 % |
| `242B` | Formación para el empleo | 74.506.061 | 29,1 % |
| `241A` | Dirección y administración de Empleo | 13.457.071 | 5,2 % |
| `325A` | Relaciones laborales y condiciones de trabajo | 6.759.759 | 2,6 % |

</details>

<details open><summary><b><code>idi</code> — 107,59 M€ (107.590.586 €) · 4 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | Investigación, desarrollo tecnológico e innovación | 48.709.320 | 45,3 % |
| `332A` | Tecnologías de la información y las comunicaciones | 37.241.289 | 34,6 % |
| `321A` | Dir. y admón. de Empresa e Innovación | 15.959.419 | 14,8 % |
| `331A` | Investigación y experimentación agraria | 5.680.558 | 5,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 301,02 M€ (301.023.551 €) · 2 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | Atención a la dependencia | 297.299.715 | 98,8 % |
| `231A` | Dirección y administración de Dependencia | 3.723.836 | 1,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,78 M€ (778.079 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | Acciones en materia de emigración | 778.079 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,48 M€ (23.479.376 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | Ordenación y promoción del turismo | 23.479.376 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,05 M€ (8.046.928 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | Igualdad de oportunidades | 8.046.928 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.005,31 M€ · 38 códigos · 19,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | Amortizac. y gastos financ. del endeudam. público | 380.023.696 |
| `252B` | Inclusión social | 76.104.709 |
| `353B` | Infraestructuras de carreteras | 62.861.894 |
| `115B` | Relaciones con la administración local | 45.028.056 |
| `252A` | Atención a la infancia y a las familias | 40.299.054 |
| `354B` | Protección y defensa contra los incendios | 38.383.502 |
| `323A` | Desarrollo empresarial | 38.140.736 |
| `353C` | Ordenación e inspección del transporte | 34.293.551 |
| `354C` | Conservación, protección y mejora de los montes | 33.548.816 |
| `115A` | Relaciones institucionales e informativas | 27.416.239 |
| `354A` | Medio natural y calidad ambiental | 25.910.181 |
| `354D` | Saneamiento y abastecimiento de aguas | 25.192.818 |
| `341A` | Comercio de calidad y artesanía extremeña | 17.900.218 |
| `274A` | Fomento y apoyo de las actividades deportivas | 16.410.232 |
| `111A` | Actividad legislativa | 13.594.000 |
| `252C` | Cooperación al desarrollo y acción exterior | 12.945.014 |
| `333A` | Energía renovable y eficiencia energética | 12.863.135 |
| `273A` | Promoción y cooperación cultural | 8.946.043 |
| `113A` | Dirección de Administración y Hacienda Públicas | 8.293.052 |
| `273B` | Teatro, música y cine | 7.530.581 |
| `272A` | Protección del patrimonio histórico-artístico | 7.390.046 |
| `272B` | Bibliotecas y archivos | 6.898.128 |
| `272C` | Museos y artes plásticas | 6.570.053 |
| `116A` | Protección civil e interior | 6.534.532 |
| `253B` | Promoción y servicios a la juventud | 6.456.902 |
| … | *resto: 13 códigos* | 45.770.915 |

</details>

### 2017

*Fuente: `ley_doe.pdf` · 77 líneas · total extraído **5.171,63 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.539,07 M€ (1.539.066.245 €) · 6 códigos · 29,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | Atención especializada de salud | 829.103.590 | 53,9 % |
| `212B` | Atención primaria de salud | 618.324.571 | 40,2 % |
| `211A` | Dirección y administración de Sanidad | 48.631.669 | 3,2 % |
| `211B` | Formación, inspección y calidad sanitarias | 31.493.671 | 2,0 % |
| `212D` | Salud pública | 7.711.571 | 0,5 % |
| `212A` | Planificación y ordenación sanitarias | 3.801.173 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.022,16 M€ (1.022.164.234 €) · 10 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | Educación secundaria y formación profesional | 379.577.984 | 37,1 % |
| `222A` | Educación infantil y primaria | 360.304.569 | 35,2 % |
| `222D` | Enseñanzas universitarias | 103.369.310 | 10,1 % |
| `222G` | 222G | 65.461.320 | 6,4 % |
| `222C` | 222C | 55.831.199 | 5,5 % |
| `222E` | 222E | 17.274.157 | 1,7 % |
| `221A` | Dirección y administración de Educación | 17.085.254 | 1,7 % |
| `222F` | Enseñanza agraria | 10.790.898 | 1,1 % |
| `221B` | Formación del profesorado de Educación | 6.932.592 | 0,7 % |
| `322A` | Ordenación industrial y desarrollo energético | 5.536.951 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 909,49 M€ (909.494.357 €) · 7 códigos · 17,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Regulación de producciones | 599.131.794 | 65,9 % |
| `353A` | Infraestructuras agrarias | 159.146.578 | 17,5 % |
| `312A` | Sanidad vegetal y animal | 35.241.657 | 3,9 % |
| `314A` | Desarrollo del medio rural | 32.159.979 | 3,5 % |
| `312B` | 312B | 31.071.628 | 3,4 % |
| `311A` | Dirección y administración de Agricultura | 27.626.876 | 3,0 % |
| `323C` | Empresa agroalimentaria | 25.115.845 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 6,30 M€ (6.302.011 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y administración de Presidencia | 6.302.011 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 44,15 M€ (44.149.780 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | 261A | 34.756.905 | 78,7 % |
| `262A` | 262A | 9.392.875 | 21,3 % |

</details>

<details open><summary><b><code>empleo</code> — 269,57 M€ (269.570.975 €) · 4 códigos · 5,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | Fomento y calidad en el empleo | 160.816.698 | 59,7 % |
| `242B` | Formación para el empleo | 88.251.339 | 32,7 % |
| `241A` | Dirección y administración de Empleo | 13.351.074 | 5,0 % |
| `325A` | Relaciones laborales y condiciones de trabajo | 7.151.864 | 2,7 % |

</details>

<details open><summary><b><code>idi</code> — 108,45 M€ (108.445.889 €) · 4 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | 331B | 50.954.150 | 47,0 % |
| `332A` | 332A | 35.634.165 | 32,9 % |
| `321A` | Dir. y admón. de Empresa e Innovación | 16.167.917 | 14,9 % |
| `331A` | Investigación y experimentación agraria | 5.689.657 | 5,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 309,63 M€ (309.634.440 €) · 2 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | Atención a la dependencia | 306.051.480 | 98,8 % |
| `231A` | Dirección y administración de Dependencia | 3.582.960 | 1,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,78 M€ (780.114 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | Acciones en materia de emigración | 780.114 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 22,43 M€ (22.428.519 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | Ordenación y promoción del turismo | 22.428.519 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,44 M€ (8.440.314 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | Igualdad de oportunidades | 8.440.314 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 931,15 M€ · 38 códigos · 18,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 315.271.660 |
| `252B` | Inclusión social | 76.211.096 |
| `353B` | Infraestructuras de carreteras | 51.859.467 |
| `115B` | Relaciones con la administración local | 44.814.633 |
| `252A` | Atención a la infancia y a las familias | 41.566.638 |
| `354B` | Protección y defensa contra los incendios | 39.579.016 |
| `323A` | Desarrollo empresarial | 36.857.733 |
| `353C` | Ordenación e inspección del transporte | 35.349.101 |
| `354C` | 354C | 34.991.872 |
| `115A` | Relaciones institucionales e informativas | 27.430.145 |
| `354A` | Medio natural y calidad ambiental | 25.298.647 |
| `354D` | Saneamiento y abastecimiento de aguas | 22.140.526 |
| `341A` | Comercio de calidad y artesanía extremeña | 18.063.810 |
| `274A` | 274A | 17.236.220 |
| `252C` | Cooperación al desarrollo y acción exterior | 13.924.463 |
| `111A` | Actividad legislativa | 13.594.000 |
| `333A` | Energía renovable y eficiencia energética | 12.745.862 |
| `273A` | Promoción y cooperación cultural | 8.900.566 |
| `272A` | Protección del patrimonio histórico-artístico | 8.545.286 |
| `113A` | 113A | 7.634.774 |
| `273B` | Teatro, música y cine | 7.347.495 |
| `116A` | Protección civil e interior | 6.949.238 |
| `253B` | Promoción y servicios a la juventud | 6.571.071 |
| `272C` | Museos y artes plásticas | 6.515.558 |
| `113E` | Control interno y contabilidad pública | 6.365.956 |
| … | *resto: 13 códigos* | 45.385.024 |

</details>

### 2018

*Fuente: `ley_doe.pdf` · 77 líneas · total extraído **5.433,98 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.603,96 M€ (1.603.961.004 €) · 6 códigos · 29,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | Atención especializada de salud | 879.988.025 | 54,9 % |
| `212B` | Atención primaria de salud | 626.794.918 | 39,1 % |
| `211A` | Dirección y administración de Sanidad | 54.034.222 | 3,4 % |
| `211B` | Formación, inspección y calidad sanitarias | 32.053.256 | 2,0 % |
| `212D` | Salud pública | 7.419.544 | 0,5 % |
| `212A` | Planificación y ordenación sanitarias | 3.671.039 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.047,13 M€ (1.047.130.282 €) · 10 códigos · 19,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | Educación secundaria y formación profesional | 377.448.621 | 36,0 % |
| `222A` | Educación infantil y primaria | 373.301.090 | 35,6 % |
| `222D` | Enseñanzas universitarias | 105.050.968 | 10,0 % |
| `222G` | Actividades complementar. y ayudas a la enseñanza | 68.989.071 | 6,6 % |
| `222C` | Educación especial, enseñanzas artísticas e idiomas | 58.124.795 | 5,6 % |
| `222E` | Educación permanente y a distancia no universitaria | 23.025.269 | 2,2 % |
| `221A` | Dirección y administración de Educación | 17.073.354 | 1,6 % |
| `222F` | Enseñanza agraria | 10.898.933 | 1,0 % |
| `221B` | Formación del profesorado de Educación | 7.410.637 | 0,7 % |
| `322A` | Ordenación industrial y desarrollo energético | 5.807.544 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 918,23 M€ (918.227.109 €) · 7 códigos · 16,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Regulación de producciones | 596.403.638 | 65,0 % |
| `353A` | Infraestructuras agrarias | 165.759.462 | 18,1 % |
| `312A` | Sanidad vegetal y animal | 35.473.153 | 3,9 % |
| `312B` | ganadera | 31.686.314 | 3,5 % |
| `311A` | Dirección y administración de Agricultura | 30.333.806 | 3,3 % |
| `314A` | Desarrollo del medio rural | 29.582.708 | 3,2 % |
| `323C` | Empresa agroalimentaria | 28.988.028 | 3,2 % |

</details>

<details open><summary><b><code>direccion</code> — 6,24 M€ (6.242.477 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y administración de Presidencia | 6.242.477 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 50,31 M€ (50.311.665 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Promoción y ayudas para el acceso a la vivienda | 40.016.671 | 79,5 % |
| `262A` | Urbanismo, arquitectura y ordenación del territorio | 10.294.994 | 20,5 % |

</details>

<details open><summary><b><code>empleo</code> — 307,54 M€ (307.539.563 €) · 4 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | Fomento y calidad en el empleo | 173.401.054 | 56,4 % |
| `242B` | Formación para el empleo | 112.363.738 | 36,5 % |
| `241A` | Dirección y administración de Empleo | 14.056.754 | 4,6 % |
| `325A` | Relaciones laborales y condiciones de trabajo | 7.718.017 | 2,5 % |

</details>

<details open><summary><b><code>idi</code> — 109,95 M€ (109.954.628 €) · 4 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | Investigación, desarrollo tecnológico e innovación | 55.574.007 | 50,5 % |
| `332A` | Tecnologías de la información y las comunicaciones | 32.781.213 | 29,8 % |
| `321A` | Dir. y admón. de Empresa e Innovación | 16.047.998 | 14,6 % |
| `331A` | Investigación y experimentación agraria | 5.551.410 | 5,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 318,00 M€ (317.996.579 €) · 2 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | Atención a la dependencia | 313.930.572 | 98,7 % |
| `231A` | Dirección y administración de Dependencia | 4.066.007 | 1,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,84 M€ (843.492 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | Acciones en materia de emigración | 843.492 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,08 M€ (23.083.317 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | Ordenación y promoción del turismo | 23.083.317 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,78 M€ (8.777.536 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | Igualdad de oportunidades | 8.777.536 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.039,91 M€ · 38 códigos · 19,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | Amortizac. y gastos financ. delendeudam. público | 385.964.586 |
| `252B` | Inclusión social | 90.746.417 |
| `353B` | Infraestructuras de carreteras | 57.037.541 |
| `115B` | Relaciones con la administración local | 45.118.094 |
| `353C` | Ordenación e inspección del transporte | 43.085.730 |
| `354B` | Protección y defensa contra los incendios | 42.396.331 |
| `252A` | Atención a la infancia y a las familias | 40.851.883 |
| `354C` | Conservación, protección y mejora de los montes | 34.850.665 |
| `323A` | Desarrollo empresarial | 28.335.358 |
| `354A` | Medio natural y calidad ambiental | 27.507.442 |
| `115A` | Relaciones institucionales e informativas | 27.494.493 |
| `354D` | Saneamiento y abastecimiento de aguas | 25.566.475 |
| `274A` | Fomento y apoyo de las actividades deportivas | 19.725.427 |
| `341A` | Comercio de calidad y artesanía extremeña | 19.224.760 |
| `252C` | Cooperación al desarrollo y acción exterior | 14.578.938 |
| `111A` | Actividad legislativa | 13.729.940 |
| `333A` | Energía renovable y eficiencia energética | 13.432.358 |
| `273A` | Promoción y cooperación cultural | 9.951.871 |
| `272A` | Protección del patrimonio histórico-artístico | 9.124.618 |
| `116A` | Protección civil e interior | 8.455.623 |
| `113A` | Dirección de Administración y Hacienda Públicas | 8.239.406 |
| `273B` | Teatro, música y cine | 7.197.676 |
| `272C` | Museos y artes plásticas | 6.926.708 |
| `253B` | Promoción y servicios a la juventud | 6.653.923 |
| `113E` | Control interno y contabilidad pública | 6.522.841 |
| … | *resto: 13 códigos* | 47.189.150 |

</details>

### 2019

*Fuente: `ley_doe.pdf` · 77 líneas · total extraído **5.797,95 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.691,12 M€ (1.691.119.508 €) · 6 códigos · 29,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | Atención especializada de salud | 943.170.526 | 55,8 % |
| `212B` | Atención primaria de salud | 645.812.045 | 38,2 % |
| `211A` | Dirección y administración de Sanidad | 54.979.123 | 3,3 % |
| `211B` | Formación, inspección y calidad sanitarias | 33.840.321 | 2,0 % |
| `212D` | Salud pública | 9.501.919 | 0,6 % |
| `212A` | Planificación y ordenación sanitarias | 3.815.574 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.078,97 M€ (1.078.972.561 €) · 10 códigos · 18,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222A` | Educación infantil y primaria | 396.934.942 | 36,8 % |
| `222B` | Educación secundaria y formación profesional | 379.114.065 | 35,1 % |
| `222D` | Enseñanzas universitarias | 106.075.204 | 9,8 % |
| `222G` | 222G | 69.801.182 | 6,5 % |
| `222C` | 222C | 61.609.511 | 5,7 % |
| `222E` | 222E | 21.186.504 | 2,0 % |
| `221A` | Dirección y administración de Educación | 18.806.604 | 1,7 % |
| `222F` | Enseñanza agraria | 10.955.050 | 1,0 % |
| `221B` | Formación del profesorado de Educación | 7.493.918 | 0,7 % |
| `322A` | Ordenación industrial y desarrollo energético | 6.995.581 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 940,78 M€ (940.779.570 €) · 7 códigos · 16,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Regulación de producciones | 595.131.828 | 63,3 % |
| `353A` | Infraestructuras agrarias | 185.492.999 | 19,7 % |
| `312B` | 312B | 35.884.950 | 3,8 % |
| `312A` | Sanidad vegetal y animal | 35.340.523 | 3,8 % |
| `311A` | Dirección y administración de Agricultura | 30.683.370 | 3,3 % |
| `314A` | Desarrollo del medio rural | 30.157.031 | 3,2 % |
| `323C` | Empresa agroalimentaria | 28.088.869 | 3,0 % |

</details>

<details open><summary><b><code>direccion</code> — 6,22 M€ (6.224.536 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | Dirección y administración de Presidencia | 6.224.536 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 64,57 M€ (64.571.981 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | 261A | 53.961.713 | 83,6 % |
| `262A` | 262A | 10.610.268 | 16,4 % |

</details>

<details open><summary><b><code>empleo</code> — 313,36 M€ (313.361.114 €) · 4 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | Fomento y calidad en el empleo | 193.884.803 | 61,9 % |
| `242B` | Formación para el empleo | 96.666.307 | 30,8 % |
| `241A` | Dirección y administración de Empleo | 14.925.486 | 4,8 % |
| `325A` | Relaciones laborales y condiciones de trabajo | 7.884.518 | 2,5 % |

</details>

<details open><summary><b><code>idi</code> — 120,61 M€ (120.609.777 €) · 4 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | 331B | 63.143.314 | 52,4 % |
| `332A` | 332A | 36.222.568 | 30,0 % |
| `321A` | Dir. y admón. de Empresa e Innovación | 15.900.792 | 13,2 % |
| `331A` | Investigación y experimentación agraria | 5.343.103 | 4,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 330,61 M€ (330.608.387 €) · 2 códigos · 5,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | Atención a la dependencia | 326.412.426 | 98,7 % |
| `231A` | Dirección y administración de Dependencia | 4.195.961 | 1,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,80 M€ (795.679 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | Acciones en materia de emigración | 795.679 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,69 M€ (23.694.251 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | Ordenación y promoción del turismo | 23.694.251 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,83 M€ (10.834.942 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | 253A | 10.834.942 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.216,37 M€ · 38 códigos · 21,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 535.470.827 |
| `252B` | Inclusión social | 87.930.814 |
| `353B` | Infraestructuras de carreteras | 63.615.132 |
| `115B` | Relaciones con la administración local | 44.991.641 |
| `354B` | Protección y defensa contra los incendios | 43.371.632 |
| `252A` | Atención a la infancia y a las familias | 42.086.202 |
| `353C` | Ordenación e inspección del transporte | 41.362.292 |
| `354C` | 354C | 41.013.857 |
| `354D` | Saneamiento y abastecimiento de aguas | 34.938.495 |
| `354A` | Medio natural y calidad ambiental | 29.557.825 |
| `323A` | Desarrollo empresarial | 28.052.968 |
| `115A` | Relaciones institucionales e informativas | 27.748.287 |
| `274A` | 274A | 20.433.728 |
| `341A` | Comercio de calidad y artesanía extremeña | 20.049.730 |
| `252C` | Cooperación al desarrollo y acción exterior | 15.590.324 |
| `111A` | Actividad legislativa | 13.929.940 |
| `333A` | Energía renovable y eficiencia energética | 12.368.611 |
| `113A` | 113A | 10.269.159 |
| `272A` | Protección del patrimonio histórico-artístico | 9.373.563 |
| `273A` | Promoción y cooperación cultural | 8.350.970 |
| `116A` | Protección civil e interior | 8.074.451 |
| `273B` | Teatro, música y cine | 7.922.117 |
| `272C` | Museos y artes plásticas | 7.158.717 |
| `113C` | Administración tributaria | 6.970.280 |
| `253B` | Promoción y servicios a la juventud | 6.735.797 |
| … | *resto: 13 códigos* | 49.007.358 |

</details>

### 2020

*Fuente: `ley_doe.pdf` · 80 líneas · total extraído **6.006,65 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.742,52 M€ (1.742.520.488 €) · 6 códigos · 29,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 980.736.009 | 56,3 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 648.926.790 | 37,2 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 63.562.373 | 3,6 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 35.500.140 | 2,0 % |
| `212D` | SALUD PÚBLICA | 9.661.216 | 0,6 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 4.133.960 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.110,31 M€ (1.110.313.493 €) · 11 códigos · 18,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | 222B | 425.007.375 | 38,3 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 377.250.272 | 34,0 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 111.934.207 | 10,1 % |
| `222G` | 222G | 69.375.669 | 6,2 % |
| `222C` | 222C | 63.794.081 | 5,7 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 18.794.236 | 1,7 % |
| `222E` | 222E | 15.595.704 | 1,4 % |
| `222F` | ENSEÑANZA AGRARIA | 8.153.740 | 0,7 % |
| `322A` | 322A | 7.254.570 | 0,7 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 6.926.534 | 0,6 % |
| `321A` | 321A | 6.227.105 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 957,92 M€ (957.921.474 €) · 7 códigos · 15,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 599.873.483 | 62,6 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 196.719.123 | 20,5 % |
| `312B` | 312B | 36.284.618 | 3,8 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 35.810.444 | 3,7 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 31.379.055 | 3,3 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 30.301.025 | 3,2 % |
| `323C` | EMPRESA AGROALIMENTARIA | 27.553.726 | 2,9 % |

</details>

<details open><summary><b><code>direccion</code> — 6,03 M€ (6.026.170 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 6.026.170 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 63,79 M€ (63.786.749 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | 261A | 51.585.435 | 80,9 % |
| `262A` | 262A | 12.201.314 | 19,1 % |

</details>

<details open><summary><b><code>empleo</code> — 327,30 M€ (327.303.628 €) · 4 códigos · 5,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 204.487.906 | 62,5 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 98.250.474 | 30,0 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 17.273.345 | 5,3 % |
| `325A` | 325A | 7.291.903 | 2,2 % |

</details>

<details open><summary><b><code>idi</code> — 107,12 M€ (107.121.478 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | 331B | 64.836.720 | 60,5 % |
| `332A` | 332A | 37.159.328 | 34,7 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 5.125.430 | 4,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 347,14 M€ (347.141.661 €) · 2 códigos · 5,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 342.706.817 | 98,7 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.434.844 | 1,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,84 M€ (842.770 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 842.770 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,05 M€ (25.053.164 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 25.053.164 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,57 M€ (11.567.653 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | 253A | 10.555.911 | 91,3 % |
| `253D` | DIRECCIÓN Y ADMINISTRACIÓN DE IGUALDAD | 1.011.742 | 8,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.307,05 M€ · 40 códigos · 21,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 586.931.392 |
| `252B` | INCLUSIÓN SOCIAL | 82.898.631 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 78.282.583 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 44.917.154 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 43.327.895 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 42.613.709 |
| `354C` | 354C | 41.595.664 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 40.168.536 |
| `323A` | DESARROLLO EMPRESARIAL | 33.262.513 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 32.448.633 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 32.417.687 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 28.120.840 |
| `274A` | 274A | 20.629.000 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 19.973.223 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 19.771.208 |
| `252C` | COOPERACIÓN AL DESARROLLO Y ACCIÓN EXTERIOR | 15.593.369 |
| `111A` | ACTIVIDAD LEGISLATIVA | 13.929.940 |
| `353D` | 353D | 9.982.301 |
| `272A` | 272A | 9.843.639 |
| `113A` | 113A | 9.583.040 |
| `273B` | TEATRO, MÚSICA Y CINE | 8.552.067 |
| `273A` | PROMOCIÓN Y COOPERACIÓN CULTURAL | 8.220.949 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 8.051.976 |
| `116A` | PROTECCIÓN CIVIL E INTERIOR | 7.977.743 |
| `113C` | ADMINISTRACIÓN TRIBUTARIA | 7.174.390 |
| … | *resto: 15 códigos* | 60.780.241 |

</details>

### 2021

*Fuente: `ley_doe.pdf` · 80 líneas · total extraído **6.423,89 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.876,52 M€ (1.876.516.389 €) · 6 códigos · 29,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.082.365.663 | 57,7 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 678.015.523 | 36,1 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 63.251.655 | 3,4 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 37.212.575 | 2,0 % |
| `212D` | SALUD PÚBLICA | 11.510.819 | 0,6 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 4.160.154 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.200,75 M€ (1.200.745.474 €) · 11 códigos · 18,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 464.994.398 | 38,7 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 407.490.117 | 33,9 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 116.928.835 | 9,7 % |
| `222G` | 222G | 72.421.425 | 6,0 % |
| `222C` | 222C | 70.020.174 | 5,8 % |
| `222E` | 222E | 22.365.973 | 1,9 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 18.819.198 | 1,6 % |
| `222F` | ENSEÑANZA AGRARIA | 7.496.746 | 0,6 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 7.294.726 | 0,6 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 6.947.673 | 0,6 % |
| `321A` | 321A | 5.966.209 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 1.002,34 M€ (1.002.336.789 €) · 7 códigos · 15,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.321.039 | 61,6 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 222.475.078 | 22,2 % |
| `312B` | 312B | 37.369.455 | 3,7 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 37.295.810 | 3,7 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 30.287.731 | 3,0 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 29.936.589 | 3,0 % |
| `323C` | EMPRESA AGROALIMENTARIA | 27.651.087 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 6,08 M€ (6.080.447 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 6.080.447 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 70,71 M€ (70.705.624 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 54.624.138 | 77,3 % |
| `262A` | 262A | 16.081.486 | 22,7 % |

</details>

<details open><summary><b><code>empleo</code> — 343,36 M€ (343.359.065 €) · 4 códigos · 5,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 229.664.835 | 66,9 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 87.679.777 | 25,5 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 18.425.998 | 5,4 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 7.588.455 | 2,2 % |

</details>

<details open><summary><b><code>idi</code> — 117,65 M€ (117.651.204 €) · 3 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | 331B | 67.569.493 | 57,4 % |
| `332A` | 332A | 44.740.791 | 38,0 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 5.340.920 | 4,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 360,67 M€ (360.672.739 €) · 2 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 356.009.140 | 98,7 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.663.599 | 1,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,84 M€ (842.370 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 842.370 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 26,43 M€ (26.431.175 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 26.431.175 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,99 M€ (14.993.077 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | 253A | 13.481.975 | 89,9 % |
| `253D` | DIRECCIÓN Y ADMINISTRACIÓN DE IGUALDAD | 1.511.102 | 10,1 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.403,56 M€ · 40 códigos · 21,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 647.460.073 |
| `252B` | INCLUSIÓN SOCIAL | 82.823.101 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 78.590.548 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 45.432.093 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 44.903.684 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 44.284.779 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 43.791.173 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 43.448.912 |
| `323A` | DESARROLLO EMPRESARIAL | 42.217.942 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 37.126.056 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 35.160.815 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 31.299.051 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 20.935.694 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 20.215.378 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 19.790.387 |
| `252C` | COOPERACIÓN AL DESARROLLO Y ACCIÓN EXTERIOR | 15.505.287 |
| `111A` | ACTIVIDAD LEGISLATIVA | 13.929.940 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO-ARTÍSTICO | 10.230.952 |
| `353D` | 353D | 9.465.305 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 9.390.765 |
| `273B` | TEATRO, MÚSICA Y CINE | 8.549.575 |
| `113B` | PLANIFICACIÓN, PROGRAMACIÓN Y PRESUPUESTACIÓN | 8.510.751 |
| `116A` | PROTECCIÓN CIVIL E INTERIOR | 8.370.385 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 8.209.672 |
| `273A` | PROMOCIÓN Y COOPERACIÓN CULTURAL | 7.503.946 |
| … | *resto: 15 códigos* | 66.414.203 |

</details>

### 2022

*Fuente: `ley_doe.pdf` · 79 líneas · total extraído **6.984,51 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.008,51 M€ (2.008.513.430 €) · 6 códigos · 28,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.173.067.988 | 58,4 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 706.466.680 | 35,2 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 69.171.281 | 3,4 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 43.799.752 | 2,2 % |
| `212D` | SALUD PÚBLICA | 11.851.967 | 0,6 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 4.155.762 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.240,87 M€ (1.240.872.586 €) · 10 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 470.655.980 | 37,9 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 416.508.285 | 33,6 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 125.584.278 | 10,1 % |
| `222G` | ACTIVIDADES COMPLEMENTARIAS Y AYUDAS A LA ENSEÑANZA | 84.189.170 | 6,8 % |
| `222C` | EDUCACIÓN ESPECIAL, ENSEÑANZAS ARTÍSTICAS E IDIOMAS | 74.834.383 | 6,0 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 20.921.513 | 1,7 % |
| `222E` | EDUCACIÓN PERMANENTE Y A DISTANCIA NO UNIVERSITARIA | 20.595.678 | 1,7 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 10.655.083 | 0,9 % |
| `222F` | ENSEÑANZA AGRARIA | 9.920.049 | 0,8 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 7.008.167 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 1.000,41 M€ (1.000.410.914 €) · 7 códigos · 14,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.080.682 | 61,7 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 214.542.133 | 21,4 % |
| `312B` | 312B | 42.098.754 | 4,2 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 38.176.527 | 3,8 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 30.572.361 | 3,1 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 30.553.423 | 3,1 % |
| `323C` | EMPRESA AGROALIMENTARIA | 27.387.034 | 2,7 % |

</details>

<details open><summary><b><code>direccion</code> — 5,85 M€ (5.848.033 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 5.848.033 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 84,77 M€ (84.768.631 €) · 2 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 52.555.796 | 62,0 % |
| `262A` | URBANISMO, ARQUITECTURA Y ORDENACIÓN DEL TERRITORIO | 32.212.835 | 38,0 % |

</details>

<details open><summary><b><code>empleo</code> — 393,16 M€ (393.155.595 €) · 4 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 260.983.430 | 66,4 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 104.623.000 | 26,6 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 19.680.807 | 5,0 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 7.868.358 | 2,0 % |

</details>

<details open><summary><b><code>idi</code> — 152,26 M€ (152.257.697 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | INVESTIGACIÓN, DESARROLLO TECNOLÓGICO E INNOVACIÓN | 79.382.968 | 52,1 % |
| `332A` | TECNOLOGÍAS DE LA INFORMACIÓN Y DE LAS COMUNICACIONES | 61.351.278 | 40,3 % |
| `321A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPRESA E INNOVACIÓN | 5.985.622 | 3,9 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 5.537.829 | 3,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 412,18 M€ (412.180.332 €) · 2 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 407.325.761 | 98,8 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.854.571 | 1,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,84 M€ (844.606 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 844.606 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 27,20 M€ (27.195.666 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 27.195.666 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 25,06 M€ (25.058.177 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | 253A | 23.513.253 | 93,8 % |
| `253D` | DIRECCIÓN Y ADMINISTRACIÓN DE IGUALDAD | 1.544.924 | 6,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.633,41 M€ · 39 códigos · 23,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 767.296.373 |
| `252B` | INCLUSIÓN SOCIAL | 87.777.658 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 66.833.427 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 64.015.169 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 59.723.981 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 57.313.171 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 55.524.506 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 51.869.301 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 47.073.286 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 44.939.402 |
| `323A` | DESARROLLO EMPRESARIAL | 42.840.914 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 37.666.057 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 32.397.763 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 22.561.744 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 18.802.847 |
| `252C` | COOPERACIÓN AL DESARROLLO Y ACCIÓN EXTERIOR | 16.703.241 |
| `111A` | ACTIVIDAD LEGISLATIVA | 14.429.940 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO‐ARTÍSTICO | 14.307.480 |
| `273B` | TEATRO, MÚSICA Y CINE | 11.701.184 |
| `131B` | FONDO DE CONTINGENCIA | 10.000.000 |
| `113D` | ADMINISTRACIÓN DEL PATRIMONIO | 9.944.115 |
| `353D` | 353D | 9.407.615 |
| `114A` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 9.097.537 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 8.897.130 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 8.573.517 |
| … | *resto: 14 códigos* | 63.708.122 |

</details>

### 2023

*Fuente: `ley_doe.pdf` · 81 líneas · total extraído **7.781,09 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.204,30 M€ (2.204.300.044 €) · 6 códigos · 28,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.262.467.596 | 57,3 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 781.910.861 | 35,5 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 93.220.989 | 4,2 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 49.379.983 | 2,2 % |
| `212D` | SALUD PÚBLICA | 13.655.076 | 0,6 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 3.665.539 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.316,84 M€ (1.316.837.775 €) · 10 códigos · 16,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 494.197.690 | 37,5 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 436.427.828 | 33,1 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 146.856.424 | 11,2 % |
| `222G` | ACTIVIDADES COMPLEMENTARIAS Y AYUDAS A LA ENSEÑANZA | 92.725.914 | 7,0 % |
| `222C` | EDUCACIÓN ESPECIAL, ENSEÑANZAS ARTÍSTICAS E IDIOMAS | 76.746.586 | 5,8 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 22.373.361 | 1,7 % |
| `222E` | EDUCACIÓN PERMANENTE Y A DISTANCIA NO UNIVERSITARIA | 19.853.095 | 1,5 % |
| `222F` | ENSEÑANZA AGRARIA | 11.977.240 | 0,9 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 7.889.594 | 0,6 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 7.790.043 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 1.074,52 M€ (1.074.515.804 €) · 7 códigos · 13,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.652.629 | 57,5 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 267.694.593 | 24,9 % |
| `312B` | 312B | 47.859.436 | 4,5 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 41.789.109 | 3,9 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 41.067.462 | 3,8 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 32.920.913 | 3,1 % |
| `323C` | EMPRESA AGROALIMENTARIA | 25.531.662 | 2,4 % |

</details>

<details open><summary><b><code>direccion</code> — 7,92 M€ (7.921.346 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 7.921.346 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 134,26 M€ (134.258.208 €) · 2 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 90.568.368 | 67,5 % |
| `262A` | URBANISMO, ARQUITECTURA Y ORDENACIÓN DEL TERRITORIO | 43.689.840 | 32,5 % |

</details>

<details open><summary><b><code>empleo</code> — 400,62 M€ (400.616.946 €) · 4 códigos · 5,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 245.144.916 | 61,2 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 125.226.813 | 31,3 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 21.882.242 | 5,5 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 8.362.975 | 2,1 % |

</details>

<details open><summary><b><code>idi</code> — 172,00 M€ (171.999.033 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | INVESTIGACIÓN, DESARROLLO TECNOLÓGICO E INNOVACIÓN | 86.117.893 | 50,1 % |
| `332A` | TECNOLOGÍAS DE LA INFORMACIÓN Y DE LAS COMUNICACIONES | 73.900.691 | 43,0 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 6.142.863 | 3,6 % |
| `321A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPRESA E INNOVACIÓN | 5.837.586 | 3,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 459,48 M€ (459.483.120 €) · 2 códigos · 5,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 454.125.105 | 98,8 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 5.358.015 | 1,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,86 M€ (857.009 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 857.009 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,69 M€ (29.692.255 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 29.692.255 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 27,56 M€ (27.559.491 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | 253A | 25.812.408 | 93,7 % |
| `253D` | DIRECCIÓN Y ADMINISTRACIÓN DE IGUALDAD | 1.747.083 | 6,3 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.953,05 M€ · 41 códigos · 25,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | 121A | 906.867.534 |
| `252B` | INCLUSIÓN SOCIAL | 103.928.209 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 76.571.148 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 73.042.123 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 69.812.749 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 66.367.810 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 64.369.989 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 59.989.936 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 58.620.103 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 55.289.096 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 54.950.797 |
| `323A` | DESARROLLO EMPRESARIAL | 51.788.175 |
| `113D` | ADMINISTRACIÓN DEL PATRIMONIO | 36.981.223 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 33.186.605 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 26.136.214 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 19.762.732 |
| `252C` | COOPERACIÓN AL DESARROLLO Y ACCIÓN EXTERIOR | 16.894.358 |
| `111A` | ACTIVIDAD LEGISLATIVA | 14.429.940 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO-ARTÍSTICO | 14.186.156 |
| `273B` | TEATRO, MÚSICA Y CINE | 12.311.627 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 11.757.672 |
| `353D` | 353D | 10.108.332 |
| `131B` | FONDO DE CONTINGENCIA | 10.000.000 |
| `113B` | PLANIFICACIÓN, PROGRAMACIÓN Y PRESUPUESTACIÓN | 9.987.240 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 9.349.898 |
| … | *resto: 16 códigos* | 86.362.047 |

</details>

### 2024

*Fuente: `ley_doe.pdf` · 79 líneas · total extraído **8.127,11 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.282,10 M€ (2.282.097.280 €) · 6 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.306.192.695 | 57,2 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 814.689.920 | 35,7 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 84.601.258 | 3,7 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 53.143.938 | 2,3 % |
| `212D` | SALUD PÚBLICA | 18.079.606 | 0,8 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 5.389.863 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.384,37 M€ (1.384.367.923 €) · 11 códigos · 17,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 516.757.616 | 37,3 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 446.964.466 | 32,3 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 151.663.119 | 11,0 % |
| `222G` | ACTIVIDADES COMPLEMENTARIAS Y AYUDAS A LA ENSEÑANZA | 101.014.580 | 7,3 % |
| `222C` | EDUCACIÓN ESPECIAL, ENSEÑANZAS ARTÍSTICAS E IDIOMAS | 90.040.292 | 6,5 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 23.182.980 | 1,7 % |
| `222E` | EDUCACIÓN PERMANENTE Y A DISTANCIA NO UNIVERSITARIA | 20.888.577 | 1,5 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 10.977.991 | 0,8 % |
| `222F` | ENSEÑANZA AGRARIA | 9.189.807 | 0,7 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 7.294.904 | 0,5 % |
| `321A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPRESA | 6.393.591 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 1.137,03 M€ (1.137.029.049 €) · 7 códigos · 14,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.147.759 | 54,3 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 254.607.113 | 22,4 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 110.433.702 | 9,7 % |
| `312B` | COMPETITIVIDAD Y CALIDAD DE LA PRODUCCIÓN AGRÍCOLA Y GANADERA | 50.603.990 | 4,5 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 41.456.042 | 3,6 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 31.749.974 | 2,8 % |
| `323C` | EMPRESA AGROALIMENTARIA | 31.030.469 | 2,7 % |

</details>

<details open><summary><b><code>direccion</code> — 11,67 M€ (11.665.643 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 11.665.643 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 142,68 M€ (142.682.822 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 92.920.904 | 65,1 % |
| `262A` | URBANISMO, ARQUITECTURA Y ORDENACIÓN DEL TERRITORIO | 49.761.918 | 34,9 % |

</details>

<details open><summary><b><code>empleo</code> — 407,92 M€ (407.922.127 €) · 4 códigos · 5,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 248.090.020 | 60,8 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 124.917.172 | 30,6 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 25.106.250 | 6,2 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 9.808.685 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 162,08 M€ (162.079.750 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | INVESTIGACIÓN, DESARROLLO TECNOLÓGICO E INNOVACIÓN | 89.172.558 | 55,0 % |
| `332A` | TECNOLOGÍAS DE LA INFORMACIÓN Y DE LAS COMUNICACIONES | 66.885.953 | 41,3 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 6.021.239 | 3,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 485,78 M€ (485.778.189 €) · 2 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 481.014.237 | 99,0 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.763.952 | 1,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,91 M€ (909.689 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 909.689 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 41,55 M€ (41.550.144 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 41.550.144 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 30,08 M€ (30.075.601 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | IGUALDAD DE GÉNERO Y ESTRATEGIA CONTRA LA VIOLENCIA HACIA | 30.075.601 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.040,95 M€ · 40 códigos · 25,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | AMORTIZACIÓN Y GASTOS FINANCIEROS DEL ENDEUDAMIENTO PÚBLICO | 959.799.167 |
| `252B` | INCLUSIÓN SOCIAL | 97.491.048 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 80.412.393 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 80.332.371 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 77.325.007 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 77.317.603 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 73.010.706 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 66.532.367 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 63.587.484 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 61.670.487 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 56.624.503 |
| `323A` | DESARROLLO EMPRESARIAL | 47.375.761 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 36.217.111 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 28.144.927 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 22.508.250 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 17.572.728 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO-ARTÍSTICO | 16.521.572 |
| `111A` | ACTIVIDAD LEGISLATIVA | 14.662.735 |
| `252C` | COOPERACIÓN PARA EL DESARROLLO Y ACCIÓN EXTERIOR | 14.216.882 |
| `116A` | PROTECCIÓN CIVIL E INTERIOR | 14.051.792 |
| `353D` | DIRECCIÓN Y ADMINISTRACIÓN DE INFRAESTRUCTURAS Y TRANS | 10.603.461 |
| `273B` | TEATRO, MÚSICA Y CINE | 10.233.954 |
| `113B` | PLANIFICACIÓN, PROGRAMACIÓN Y PRESUPUESTACIÓN | 10.090.407 |
| `131B` | FONDO DE CONTINGENCIA | 10.000.000 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 9.777.111 |
| … | *resto: 15 códigos* | 84.871.062 |

</details>

### 2025

*Fuente: `ley_doe.pdf` · 79 líneas · total extraído **8.127,11 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.282,10 M€ (2.282.097.280 €) · 6 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.306.192.695 | 57,2 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 814.689.920 | 35,7 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 84.601.258 | 3,7 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 53.143.938 | 2,3 % |
| `212D` | SALUD PÚBLICA | 18.079.606 | 0,8 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 5.389.863 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.384,37 M€ (1.384.367.923 €) · 11 códigos · 17,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 516.757.616 | 37,3 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 446.964.466 | 32,3 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 151.663.119 | 11,0 % |
| `222G` | ACTIVIDADES COMPLEMENTARIAS Y AYUDAS A LA ENSEÑANZA | 101.014.580 | 7,3 % |
| `222C` | EDUCACIÓN ESPECIAL, ENSEÑANZAS ARTÍSTICAS E IDIOMAS | 90.040.292 | 6,5 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 23.182.980 | 1,7 % |
| `222E` | EDUCACIÓN PERMANENTE Y A DISTANCIA NO UNIVERSITARIA | 20.888.577 | 1,5 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 10.977.991 | 0,8 % |
| `222F` | ENSEÑANZA AGRARIA | 9.189.807 | 0,7 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 7.294.904 | 0,5 % |
| `321A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPRESA | 6.393.591 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 1.137,03 M€ (1.137.029.049 €) · 7 códigos · 14,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.147.759 | 54,3 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 254.607.113 | 22,4 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 110.433.702 | 9,7 % |
| `312B` | COMPETITIVIDAD Y CALIDAD DE LA PRODUCCIÓN AGRÍCOLA Y GANADERA | 50.603.990 | 4,5 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 41.456.042 | 3,6 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 31.749.974 | 2,8 % |
| `323C` | EMPRESA AGROALIMENTARIA | 31.030.469 | 2,7 % |

</details>

<details open><summary><b><code>direccion</code> — 11,67 M€ (11.665.643 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 11.665.643 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 142,68 M€ (142.682.822 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 92.920.904 | 65,1 % |
| `262A` | URBANISMO, ARQUITECTURA Y ORDENACIÓN DEL TERRITORIO | 49.761.918 | 34,9 % |

</details>

<details open><summary><b><code>empleo</code> — 407,92 M€ (407.922.127 €) · 4 códigos · 5,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 248.090.020 | 60,8 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 124.917.172 | 30,6 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 25.106.250 | 6,2 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 9.808.685 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 162,08 M€ (162.079.750 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | INVESTIGACIÓN, DESARROLLO TECNOLÓGICO E INNOVACIÓN | 89.172.558 | 55,0 % |
| `332A` | TECNOLOGÍAS DE LA INFORMACIÓN Y DE LAS COMUNICACIONES | 66.885.953 | 41,3 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 6.021.239 | 3,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 485,78 M€ (485.778.189 €) · 2 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 481.014.237 | 99,0 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.763.952 | 1,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,91 M€ (909.689 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 909.689 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 41,55 M€ (41.550.144 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 41.550.144 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 30,08 M€ (30.075.601 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | IGUALDAD DE GÉNERO Y ESTRATEGIA CONTRA LA VIOLENCIA HACIA | 30.075.601 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.040,95 M€ · 40 códigos · 25,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | AMORTIZACIÓN Y GASTOS FINANCIEROS DEL ENDEUDAMIENTO PÚBLICO | 959.799.167 |
| `252B` | INCLUSIÓN SOCIAL | 97.491.048 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 80.412.393 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 80.332.371 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 77.325.007 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 77.317.603 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 73.010.706 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 66.532.367 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 63.587.484 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 61.670.487 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 56.624.503 |
| `323A` | DESARROLLO EMPRESARIAL | 47.375.761 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 36.217.111 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 28.144.927 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 22.508.250 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 17.572.728 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO-ARTÍSTICO | 16.521.572 |
| `111A` | ACTIVIDAD LEGISLATIVA | 14.662.735 |
| `252C` | COOPERACIÓN PARA EL DESARROLLO Y ACCIÓN EXTERIOR | 14.216.882 |
| `116A` | PROTECCIÓN CIVIL E INTERIOR | 14.051.792 |
| `353D` | DIRECCIÓN Y ADMINISTRACIÓN DE INFRAESTRUCTURAS Y TRANS | 10.603.461 |
| `273B` | TEATRO, MÚSICA Y CINE | 10.233.954 |
| `113B` | PLANIFICACIÓN, PROGRAMACIÓN Y PRESUPUESTACIÓN | 10.090.407 |
| `131B` | FONDO DE CONTINGENCIA | 10.000.000 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 9.777.111 |
| … | *resto: 15 códigos* | 84.871.062 |

</details>

### 2026

*Fuente: `ley_doe.pdf` · 79 líneas · total extraído **8.127,11 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.282,10 M€ (2.282.097.280 €) · 6 códigos · 28,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `212C` | ATENCIÓN ESPECIALIZADA DE SALUD | 1.306.192.695 | 57,2 % |
| `212B` | ATENCIÓN PRIMARIA DE SALUD | 814.689.920 | 35,7 % |
| `211A` | DIRECCIÓN Y ADMINISTRACIÓN DE SANIDAD | 84.601.258 | 3,7 % |
| `211B` | FORMACIÓN, INSPECCIÓN Y CALIDAD SANITARIAS | 53.143.938 | 2,3 % |
| `212D` | SALUD PÚBLICA | 18.079.606 | 0,8 % |
| `212A` | PLANIFICACIÓN Y ORDENACIÓN SANITARIAS | 5.389.863 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 1.384,37 M€ (1.384.367.923 €) · 11 códigos · 17,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `222B` | EDUCACIÓN SECUNDARIA Y FORMACIÓN PROFESIONAL | 516.757.616 | 37,3 % |
| `222A` | EDUCACIÓN INFANTIL Y PRIMARIA | 446.964.466 | 32,3 % |
| `222D` | ENSEÑANZAS UNIVERSITARIAS | 151.663.119 | 11,0 % |
| `222G` | ACTIVIDADES COMPLEMENTARIAS Y AYUDAS A LA ENSEÑANZA | 101.014.580 | 7,3 % |
| `222C` | EDUCACIÓN ESPECIAL, ENSEÑANZAS ARTÍSTICAS E IDIOMAS | 90.040.292 | 6,5 % |
| `221A` | DIRECCIÓN Y ADMINISTRACIÓN DE EDUCACIÓN | 23.182.980 | 1,7 % |
| `222E` | EDUCACIÓN PERMANENTE Y A DISTANCIA NO UNIVERSITARIA | 20.888.577 | 1,5 % |
| `221B` | FORMACIÓN DEL PROFESORADO DE EDUCACIÓN | 10.977.991 | 0,8 % |
| `222F` | ENSEÑANZA AGRARIA | 9.189.807 | 0,7 % |
| `322A` | ORDENACIÓN INDUSTRIAL Y DESARROLLO ENERGÉTICO | 7.294.904 | 0,5 % |
| `321A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPRESA | 6.393.591 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 1.137,03 M€ (1.137.029.049 €) · 7 códigos · 14,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | REGULACIÓN DE PRODUCCIONES | 617.147.759 | 54,3 % |
| `353A` | INFRAESTRUCTURAS AGRARIAS | 254.607.113 | 22,4 % |
| `314A` | DESARROLLO DEL MEDIO RURAL | 110.433.702 | 9,7 % |
| `312B` | COMPETITIVIDAD Y CALIDAD DE LA PRODUCCIÓN AGRÍCOLA Y GANADERA | 50.603.990 | 4,5 % |
| `312A` | SANIDAD VEGETAL Y ANIMAL | 41.456.042 | 3,6 % |
| `311A` | DIRECCIÓN Y ADMINISTRACIÓN DE AGRICULTURA | 31.749.974 | 2,8 % |
| `323C` | EMPRESA AGROALIMENTARIA | 31.030.469 | 2,7 % |

</details>

<details open><summary><b><code>direccion</code> — 11,67 M€ (11.665.643 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | DIRECCIÓN Y ADMINISTRACIÓN DE PRESIDENCIA | 11.665.643 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 142,68 M€ (142.682.822 €) · 2 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | PROMOCIÓN Y AYUDAS PARA EL ACCESO A LA VIVIENDA | 92.920.904 | 65,1 % |
| `262A` | URBANISMO, ARQUITECTURA Y ORDENACIÓN DEL TERRITORIO | 49.761.918 | 34,9 % |

</details>

<details open><summary><b><code>empleo</code> — 407,92 M€ (407.922.127 €) · 4 códigos · 5,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `242A` | FOMENTO Y CALIDAD EN EL EMPLEO | 248.090.020 | 60,8 % |
| `242B` | FORMACIÓN PARA EL EMPLEO | 124.917.172 | 30,6 % |
| `241A` | DIRECCIÓN Y ADMINISTRACIÓN DE EMPLEO | 25.106.250 | 6,2 % |
| `325A` | RELACIONES LABORALES Y CONDICIONES DE TRABAJO | 9.808.685 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 162,08 M€ (162.079.750 €) · 3 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331B` | INVESTIGACIÓN, DESARROLLO TECNOLÓGICO E INNOVACIÓN | 89.172.558 | 55,0 % |
| `332A` | TECNOLOGÍAS DE LA INFORMACIÓN Y DE LAS COMUNICACIONES | 66.885.953 | 41,3 % |
| `331A` | INVESTIGACIÓN Y EXPERIMENTACIÓN AGRARIA | 6.021.239 | 3,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 485,78 M€ (485.778.189 €) · 2 códigos · 6,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A` | ATENCIÓN A LA DEPENDENCIA | 481.014.237 | 99,0 % |
| `231A` | DIRECCIÓN Y ADMINISTRACIÓN DE DEPENDENCIA | 4.763.952 | 1,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,91 M€ (909.689 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253C` | ACCIONES EN MATERIA DE EMIGRACIÓN | 909.689 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 41,55 M€ (41.550.144 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `342A` | ORDENACIÓN Y PROMOCIÓN DEL TURISMO | 41.550.144 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 30,08 M€ (30.075.601 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `253A` | IGUALDAD DE GÉNERO Y ESTRATEGIA CONTRA LA VIOLENCIA HACIA | 30.075.601 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.040,95 M€ · 40 códigos · 25,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `121A` | AMORTIZACIÓN Y GASTOS FINANCIEROS DEL ENDEUDAMIENTO PÚBLICO | 959.799.167 |
| `252B` | INCLUSIÓN SOCIAL | 97.491.048 |
| `354C` | CONSERVACIÓN, PROTECCIÓN Y MEJORA DE LOS MONTES | 80.412.393 |
| `354D` | SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 80.332.371 |
| `354A` | MEDIO NATURAL Y CALIDAD AMBIENTAL | 77.325.007 |
| `252A` | ATENCIÓN A LA INFANCIA Y A LAS FAMILIAS | 77.317.603 |
| `333A` | ENERGÍA RENOVABLE Y EFICIENCIA ENERGÉTICA | 73.010.706 |
| `353C` | ORDENACIÓN E INSPECCIÓN DEL TRANSPORTE | 66.532.367 |
| `353B` | INFRAESTRUCTURAS DE CARRETERAS | 63.587.484 |
| `354B` | PROTECCIÓN Y DEFENSA CONTRA LOS INCENDIOS | 61.670.487 |
| `115B` | RELACIONES CON LA ADMINISTRACIÓN LOCAL | 56.624.503 |
| `323A` | DESARROLLO EMPRESARIAL | 47.375.761 |
| `115A` | RELACIONES INSTITUCIONALES E INFORMATIVAS | 36.217.111 |
| `274A` | FOMENTO Y APOYO DE LAS ACTIVIDADES DEPORTIVAS | 28.144.927 |
| `341A` | COMERCIO DE CALIDAD Y ARTESANÍA EXTREMEÑA | 22.508.250 |
| `113A` | DIRECCIÓN DE ADMINISTRACIÓN Y HACIENDA PÚBLICAS | 17.572.728 |
| `272A` | PROTECCIÓN DEL PATRIMONIO HISTÓRICO-ARTÍSTICO | 16.521.572 |
| `111A` | ACTIVIDAD LEGISLATIVA | 14.662.735 |
| `252C` | COOPERACIÓN PARA EL DESARROLLO Y ACCIÓN EXTERIOR | 14.216.882 |
| `116A` | PROTECCIÓN CIVIL E INTERIOR | 14.051.792 |
| `353D` | DIRECCIÓN Y ADMINISTRACIÓN DE INFRAESTRUCTURAS Y TRANS | 10.603.461 |
| `273B` | TEATRO, MÚSICA Y CINE | 10.233.954 |
| `113B` | PLANIFICACIÓN, PROGRAMACIÓN Y PRESUPUESTACIÓN | 10.090.407 |
| `131B` | FONDO DE CONTINGENCIA | 10.000.000 |
| `272C` | MUSEOS Y ARTES PLÁSTICAS | 9.777.111 |
| … | *resto: 15 códigos* | 84.871.062 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py ext     # regenera este documento
python3 tools/auditoria_magnitud.py ext        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa ext --anio <año> \
    --input ../fuentes/raw/ext/<año>/<fichero> --output /tmp/ext.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-ext.md`](limitaciones-ext.md)

