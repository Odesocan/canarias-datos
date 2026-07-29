# Trazabilidad de la extracción — Principado de Asturias (`ast`)

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
| **2015** | 91 | `tomo_I.pdf` | 11 | 37,4 % | 3.834,45 | — | no_aplica |
| **2016** | 92 | `tomo_I.pdf` | 11 | 38,0 % | 3.991,59 | — | no_aplica |
| **2017** | 92 | `tomo_I.pdf` | 11 | 38,0 % | 4.096,15 | — | no_aplica |
| **2018** | 91 | `tomo_I.pdf` | 11 | 38,5 % | 4.355,21 | — | no_aplica |
| **2019** | 91 | `tomo_I.pdf` | 11 | 38,5 % | 4.394,57 | — | no_aplica |
| **2020** | 96 | `tomo_I.pdf` | 11 | 40,6 % | 4.610,31 | — | no_aplica |
| **2021** | 97 | `tomo_I.pdf` | 11 | 41,2 % | 5.095,10 | — | no_aplica |
| **2022** | 97 | `tomo_I.pdf` | 11 | 41,2 % | 5.239,75 | — | no_aplica |
| **2023** | 97 | `tomo_I.pdf` | 11 | 41,2 % | 5.846,19 | — | no_aplica |
| **2024** | 106 | `tomo_I.pdf` | 11 | 40,6 % | 6.237,36 | — | no_aplica |
| **2025** | 107 | `tomo_I.pdf` | 11 | 41,1 % | 6.557,90 | — | no_aplica |
| **2026** | 106 | `tomo_I.pdf` | 11 | 40,6 % | 6.872,66 | — | no_aplica |

**URL(s) de origen:**
- <https://miprincipado.asturias.es/bopa/2020/12/31/2020-11546.pdf>
- <https://miprincipado.asturias.es/bopa/2022/12/30/20221230Su1.pdf>
- <https://miprincipado.asturias.es/bopa/2023/12/29/20231229Su1.pdf>
- <https://miprincipado.asturias.es/bopa/2024/12/31/2024-11573.pdf>
- <https://miprincipado.asturias.es/bopa/2025/12/31/20251231Su1.pdf>
- <https://transparencia.asturias.es/documents/2213862/2215811/tomo_II.pdf/dbca73d3-0d92-8196-e455-0d258949eff8?t=1662374192441>
- <https://transparencia.asturias.es/documents/2213862/2215814/t2.pdf/cc1c5f0e-7e07-3df0-c346-2b3f8dc2790d?t=1662376205922>
- <https://transparencia.asturias.es/documents/2213862/2215817/t2.pdf/576c290b-fbe0-e9c2-64b8-498e465ac6aa?t=1662377486916>
- <https://transparencia.asturias.es/documents/2213862/2215820/t2.pdf/2c4f7866-0955-d920-14ab-6ee398a57610?t=1662377980800>
- <https://transparencia.asturias.es/documents/2213862/2215823/t2.pdf/151086eb-3f8d-db4f-b049-6bd5dc948bef?t=1662378989411>
- <https://transparencia.asturias.es/documents/2213862/2215826/PROYECTO_PRESUPUESTOS_2015.pdf/80d50681-2aa0-0756-3f16-9547d3c46fb9?t=1662389991930>
- <https://transparencia.asturias.es/documents/2213862/2895782/proyecto_2022_tomoII.pdf/cb468a76-aed1-b8f3-f4f1-61ae829f379a?t=1716376923444>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 1.486,19 | 1.642,75 | 1.671,75 | 1.702,24 | 1.754,62 | 1.804,31 | 1.946,22 | 1.991,08 | 2.119,65 | 2.326,99 | 2.450,66 | 2.554,18 |
| `educacion` | 722,33 | 740,88 | 749,56 | 773,96 | 803,25 | 845,30 | 894,35 | 942,70 | 999,12 | 1.042,25 | 1.093,29 | 1.178,92 |
| `soberania` | 144,72 | 147,06 | 181,32 | 204,19 | 201,09 | 200,87 | 230,81 | 233,28 | 245,49 | 238,68 | 244,91 | 253,89 |
| `direccion` | 1,34 | 1,35 | 1,34 | 1,32 | 1,17 | 2,44 | 3,02 | 3,09 | 3,05 | 3,27 | 2,93 | 3,18 |
| `vivienda` | 29,15 | 30,15 | 29,12 | 33,34 | 33,43 | 34,75 | 38,39 | 41,28 | 81,24 | 98,36 | 158,31 | 189,07 |
| `empleo` | 104,74 | 96,17 | 100,97 | 115,09 | 118,34 | 118,58 | 133,48 | 142,37 | 167,23 | 178,97 | 177,68 | 179,20 |
| `idi` | 17,95 | 18,20 | 18,30 | 18,96 | 19,63 | 27,79 | 34,38 | 40,56 | 56,87 | 59,80 | 75,41 | 67,41 |
| `dependencia` | 300,24 | 312,30 | 328,09 | 355,96 | 367,26 | 369,94 | 384,50 | 387,39 | 424,81 | 477,48 | 516,22 | 524,31 |
| `diversidad` | 1,29 | 1,21 | 1,30 | 1,57 | 1,47 | 1,38 | 1,41 | 1,50 | 1,88 | 5,76 | 6,53 | 6,72 |
| `turismo` | 8,46 | 8,23 | 10,16 | 11,72 | 10,01 | 10,32 | 12,23 | 12,86 | 30,35 | 40,59 | 46,16 | 49,64 |
| `igualdad` | 2,20 | 2,25 | 2,24 | 2,52 | 4,09 | 5,07 | 6,91 | 11,53 | 13,22 | 14,84 | 14,03 | 15,88 |
| **Σ asignado** | 2.818,62 | 3.000,55 | 3.094,15 | 3.220,87 | 3.314,36 | 3.420,75 | 3.685,71 | 3.807,64 | 4.142,90 | 4.487,01 | 4.786,13 | 5.022,40 |
| *(sin concepto)* | 1.015,83 | 991,04 | 1.002,00 | 1.134,34 | 1.080,21 | 1.189,56 | 1.409,39 | 1.432,11 | 1.703,30 | 1.750,36 | 1.771,77 | 1.850,26 |
| **TOTAL extraído** | 3.834,45 | 3.991,59 | 4.096,15 | 4.355,21 | 4.394,57 | 4.610,31 | 5.095,10 | 5.239,75 | 5.846,19 | 6.237,36 | 6.557,90 | 6.872,66 |

**Conceptos sin ninguna línea en toda la serie:** `discapacidad`, `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +10,5 % | +1,8 % | +1,8 % | +3,1 % | +2,8 % | +7,9 % | +2,3 % | +6,5 % | +9,8 % | +5,3 % | +4,2 % |
| `educacion` | +2,6 % | +1,2 % | +3,3 % | +3,8 % | +5,2 % | +5,8 % | +5,4 % | +6,0 % | +4,3 % | +4,9 % | +7,8 % |
| `soberania` | +1,6 % | +23,3 % | +12,6 % | −1,5 % | −0,1 % | +14,9 % | +1,1 % | +5,2 % | −2,8 % | +2,6 % | +3,7 % |
| `direccion` | +0,5 % | −1,0 % | −1,4 % | −11,1 % | +108,3 % ⚠ | +24,0 % | +2,2 % | −1,4 % | +7,5 % | −10,5 % | +8,6 % |
| `vivienda` | +3,4 % | −3,4 % | +14,5 % | +0,3 % | +3,9 % | +10,5 % | +7,5 % | +96,8 % ⚠ | +21,1 % | +60,9 % ⚠ | +19,4 % |
| `empleo` | −8,2 % | +5,0 % | +14,0 % | +2,8 % | +0,2 % | +12,6 % | +6,7 % | +17,5 % | +7,0 % | −0,7 % | +0,9 % |
| `idi` | +1,4 % | +0,5 % | +3,6 % | +3,5 % | +41,6 % ⚠ | +23,7 % | +18,0 % | +40,2 % ⚠ | +5,2 % | +26,1 % | −10,6 % |
| `dependencia` | +4,0 % | +5,1 % | +8,5 % | +3,2 % | +0,7 % | +3,9 % | +0,8 % | +9,7 % | +12,4 % | +8,1 % | +1,6 % |
| `diversidad` | −6,1 % | +7,8 % | +20,2 % | −6,1 % | −6,4 % | +2,7 % | +5,8 % | +25,8 % | +206,5 % ⚠ | +13,3 % | +2,9 % |
| `turismo` | −2,8 % | +23,6 % | +15,3 % | −14,6 % | +3,2 % | +18,5 % | +5,1 % | +136,0 % ⚠ | +33,7 % | +13,7 % | +7,5 % |
| `igualdad` | +2,2 % | −0,4 % | +12,3 % | +62,4 % ⚠ | +24,0 % | +36,2 % | +67,0 % ⚠ | +14,6 % | +12,3 % | −5,5 % | +13,3 % |
| **TOTAL** | +4,1 % | +2,6 % | +6,3 % | +0,9 % | +4,9 % | +10,5 % | +2,8 % | +11,6 % | +6,7 % | +5,1 % | +4,8 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2020 | `idi` | **SALTO** | 19,63 → 27,79 M€ (+41,6 % ⚠) |
| 2023 | `idi` | **SALTO** | 40,56 → 56,87 M€ (+40,2 % ⚠) |
| 2023 | `turismo` | **SALTO** | 12,86 → 30,35 M€ (+136,0 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 41,28 → 81,24 M€ (+96,8 % ⚠) |
| 2025 | `vivienda` | **SALTO** | 98,36 → 158,31 M€ (+60,9 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (1 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `121B` | 7,56 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:empleo, 2025:empleo, 2026:empleo |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `tomo_I.pdf` · 91 líneas · total extraído **3.834,45 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.486,19 M€ (1.486.192.547 €) · 5 códigos · 38,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.435.486.876 | 96,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 28.266.548 | 1,9 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 13.957.339 | 0,9 % |
| `412P` | SALUD PÚBLICA | 5.623.000 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 2.858.784 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 722,33 M€ (722.331.717 €) · 12 códigos · 18,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 225.256.325 | 31,2 % |
| `422C` | EDUCACIÓN SECUNDARIA | 195.290.126 | 27,0 % |
| `422D` | UNIVERSIDADES | 129.912.076 | 18,0 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 61.661.503 | 8,5 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 40.748.253 | 5,6 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 30.292.419 | 4,2 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.658.457 | 2,0 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 14.547.064 | 2,0 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 5.672.076 | 0,8 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.552.684 | 0,2 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.391.784 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.348.950 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 144,72 M€ (144.724.327 €) · 6 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 71.854.980 | 49,6 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 20.485.964 | 14,2 % |
| `711B` | DESARROLLO RURAL | 19.747.285 | 13,6 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 16.460.130 | 11,4 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 9.038.518 | 6,2 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.137.450 | 4,9 % |

</details>

<details open><summary><b><code>direccion</code> — 1,34 M€ (1.341.768 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.341.768 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 29,15 M€ (29.149.040 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 29.149.040 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 104,74 M€ (104.743.563 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 99.299.984 | 94,8 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 5.443.579 | 5,2 % |

</details>

<details open><summary><b><code>idi</code> — 17,95 M€ (17.946.722 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 17.946.722 | 100,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 300,24 M€ (300.238.092 €) · 3 códigos · 7,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 164.666.109 | 54,8 % |
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 135.306.906 | 45,1 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 265.077 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,29 M€ (1.287.623 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.287.623 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 8,46 M€ (8.464.428 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 8.464.428 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,20 M€ (2.204.598 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 2.204.598 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.015,83 M€ · 57 códigos · 26,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 473.980.000 |
| `513H` | CARRETERAS | 59.967.840 |
| `513G` | TRANSPORTES | 46.433.721 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 45.869.512 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 30.335.039 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 29.676.065 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 28.715.050 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 23.206.290 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 21.283.270 |
| `612G` | GESTIÓN SECTOR PÚBLICO EMPRESARIAL | 20.417.564 |
| `612F` | GESTIÓN DEL PATRIMONIO | 19.394.876 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 17.494.681 |
| `443F` | RECURSOS NATURALES | 13.897.211 |
| `111B` | ACTIVIDAD LEGISLATIVA | 13.449.000 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 12.798.200 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 9.674.003 |
| `443E` | PROTECCIÓN DE LA SALUD | 7.867.990 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 7.388.595 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 7.281.693 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 7.100.000 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 6.901.930 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 6.837.655 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.367.085 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 6.238.900 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.108.331 |
| … | *resto: 32 códigos* | 87.140.502 |

</details>

### 2016

*Fuente: `tomo_I.pdf` · 92 líneas · total extraído **3.991,59 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.642,75 M€ (1.642.753.590 €) · 5 códigos · 41,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.616.930.305 | 98,4 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 10.964.918 | 0,7 % |
| `412P` | SALUD PÚBLICA | 7.220.423 | 0,4 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 4.733.990 | 0,3 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 2.903.954 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 740,88 M€ (740.875.925 €) · 12 códigos · 18,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 226.993.683 | 30,6 % |
| `422C` | EDUCACIÓN SECUNDARIA | 201.281.680 | 27,2 % |
| `422D` | UNIVERSIDADES | 131.792.692 | 17,8 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 66.739.297 | 9,0 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 41.364.403 | 5,6 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 30.737.073 | 4,1 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 17.112.421 | 2,3 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.834.857 | 2,0 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 5.651.786 | 0,8 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.570.664 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.523.610 | 0,2 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.273.759 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 147,06 M€ (147.056.925 €) · 6 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 73.148.600 | 49,7 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 21.137.775 | 14,4 % |
| `711B` | DESARROLLO RURAL | 19.419.840 | 13,2 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 16.906.295 | 11,5 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 8.848.864 | 6,0 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.595.551 | 5,2 % |

</details>

<details open><summary><b><code>direccion</code> — 1,35 M€ (1.348.928 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.348.928 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 30,15 M€ (30.152.620 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 30.152.620 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 96,17 M€ (96.170.390 €) · 2 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 91.303.131 | 94,9 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 4.867.259 | 5,1 % |

</details>

<details open><summary><b><code>idi</code> — 18,20 M€ (18.201.032 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 17.829.782 | 98,0 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 371.250 | 2,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 312,30 M€ (312.302.926 €) · 3 códigos · 7,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 164.343.529 | 52,6 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 147.690.580 | 47,3 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 268.817 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,21 M€ (1.209.343 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.209.343 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 8,23 M€ (8.225.653 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 8.225.653 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,25 M€ (2.253.168 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 2.253.168 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 991,04 M€ · 57 códigos · 24,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 455.000.000 |
| `513H` | CARRETERAS | 63.115.656 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 48.944.838 |
| `513G` | TRANSPORTES | 43.891.010 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 35.304.720 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 31.663.410 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 25.795.975 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 24.130.910 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.746.980 |
| `612F` | GESTIÓN DEL PATRIMONIO | 19.795.160 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 17.064.962 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 16.992.752 |
| `443F` | RECURSOS NATURALES | 15.639.799 |
| `111B` | ACTIVIDAD LEGISLATIVA | 14.237.000 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 12.688.500 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 9.297.225 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 8.954.341 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 7.423.278 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 6.670.980 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.347.233 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 6.335.985 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.123.095 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 5.975.517 |
| `121B` | DIRECCIÓN DE LA FUNCIÓN PÚBLICA | 5.395.925 |
| `632D` | POLÍTICA FINANCIERA | 4.917.280 |
| … | *resto: 32 códigos* | 76.584.983 |

</details>

### 2017

*Fuente: `tomo_I.pdf` · 92 líneas · total extraído **4.096,15 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.671,75 M€ (1.671.749.925 €) · 5 códigos · 40,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.643.653.834 | 98,3 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 11.984.029 | 0,7 % |
| `412P` | SALUD PÚBLICA | 7.321.001 | 0,4 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.995.807 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 2.795.254 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 749,56 M€ (749.559.459 €) · 12 códigos · 18,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 230.105.389 | 30,7 % |
| `422C` | EDUCACIÓN SECUNDARIA | 205.621.897 | 27,4 % |
| `422D` | UNIVERSIDADES | 132.134.424 | 17,6 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 67.402.529 | 9,0 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 40.839.306 | 5,4 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 32.282.782 | 4,3 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 15.619.451 | 2,1 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.758.607 | 2,0 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 5.711.274 | 0,8 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.963.536 | 0,3 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.570.664 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.549.600 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 181,32 M€ (181.323.431 €) · 6 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 106.606.950 | 58,8 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 22.373.910 | 12,3 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 21.087.155 | 11,6 % |
| `711B` | DESARROLLO RURAL | 15.081.100 | 8,3 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 8.644.085 | 4,8 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.530.231 | 4,2 % |

</details>

<details open><summary><b><code>direccion</code> — 1,34 M€ (1.335.138 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.335.138 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 29,12 M€ (29.118.540 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 29.118.540 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 100,97 M€ (100.967.817 €) · 2 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 95.983.655 | 95,1 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 4.984.162 | 4,9 % |

</details>

<details open><summary><b><code>idi</code> — 18,30 M€ (18.296.955 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 17.846.760 | 97,5 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 450.195 | 2,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 328,09 M€ (328.087.583 €) · 3 códigos · 8,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 173.189.901 | 52,8 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 154.636.425 | 47,1 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 261.257 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,30 M€ (1.303.303 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.303.303 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 10,16 M€ (10.164.720 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 10.164.720 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,24 M€ (2.244.818 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 2.244.818 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.002,00 M€ · 57 códigos · 24,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 440.020.000 |
| `513H` | CARRETERAS | 63.359.425 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 48.930.150 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 42.489.831 |
| `513G` | TRANSPORTES | 41.848.746 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 31.557.420 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 27.294.646 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 26.416.680 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.785.830 |
| `612F` | GESTIÓN DEL PATRIMONIO | 20.860.077 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 19.747.333 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 17.517.503 |
| `443F` | RECURSOS NATURALES | 16.150.553 |
| `111B` | ACTIVIDAD LEGISLATIVA | 14.615.000 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 13.550.220 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 12.897.988 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 9.371.220 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 8.943.656 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 7.592.150 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.897.637 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 6.757.490 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 6.610.264 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.082.765 |
| `121B` | DIRECCIÓN DE LA FUNCIÓN PÚBLICA | 5.304.660 |
| `632D` | POLÍTICA FINANCIERA | 4.919.570 |
| … | *resto: 32 códigos* | 79.476.724 |

</details>

### 2018

*Fuente: `tomo_I.pdf` · 91 líneas · total extraído **4.355,21 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.702,24 M€ (1.702.237.431 €) · 5 códigos · 39,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.670.716.390 | 98,1 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 11.718.026 | 0,7 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 9.543.996 | 0,6 % |
| `412P` | SALUD PÚBLICA | 7.505.519 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 2.753.500 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 773,96 M€ (773.957.382 €) · 12 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 233.931.861 | 30,2 % |
| `422C` | EDUCACIÓN SECUNDARIA | 214.424.007 | 27,7 % |
| `422D` | UNIVERSIDADES | 136.110.168 | 17,6 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 68.205.118 | 8,8 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 41.359.790 | 5,3 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 38.392.251 | 5,0 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 16.009.754 | 2,1 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.865.009 | 1,9 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 5.920.926 | 0,8 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.667.041 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.568.540 | 0,2 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.502.917 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 204,19 M€ (204.193.205 €) · 6 códigos · 4,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 110.895.150 | 54,3 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 27.661.348 | 13,5 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 26.231.445 | 12,8 % |
| `711B` | DESARROLLO RURAL | 22.808.360 | 11,2 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 8.822.124 | 4,3 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.774.778 | 3,8 % |

</details>

<details open><summary><b><code>direccion</code> — 1,32 M€ (1.316.678 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.316.678 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 33,34 M€ (33.338.517 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 33.338.517 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 115,09 M€ (115.091.779 €) · 2 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 108.972.709 | 94,7 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 6.119.070 | 5,3 % |

</details>

<details open><summary><b><code>idi</code> — 18,96 M€ (18.964.058 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 18.294.788 | 96,5 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 669.270 | 3,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 355,96 M€ (355.957.031 €) · 3 códigos · 8,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 183.346.171 | 51,5 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 172.346.780 | 48,4 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 264.080 | 0,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,57 M€ (1.566.783 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.566.783 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 11,72 M€ (11.722.048 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 11.722.048 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,52 M€ (2.520.649 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 2.520.649 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.134,34 M€ · 56 códigos · 26,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 533.460.000 |
| `513H` | CARRETERAS | 69.739.949 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 53.274.180 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 41.264.571 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 40.149.958 |
| `513G` | TRANSPORTES | 36.200.237 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 34.300.100 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 26.118.915 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 23.640.290 |
| `612F` | GESTIÓN DEL PATRIMONIO | 22.593.333 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 18.650.000 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 18.580.753 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 18.402.075 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 18.280.000 |
| `443F` | RECURSOS NATURALES | 16.932.521 |
| `111B` | ACTIVIDAD LEGISLATIVA | 14.613.000 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 9.575.420 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 8.544.001 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 8.273.060 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 6.910.729 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.841.635 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.696.175 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 6.525.230 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 6.054.590 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 5.718.129 |
| … | *resto: 31 códigos* | 83.001.155 |

</details>

### 2019

*Fuente: `tomo_I.pdf` · 91 líneas · total extraído **4.394,57 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.754,62 M€ (1.754.622.875 €) · 5 códigos · 39,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.716.071.717 | 97,8 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 16.637.500 | 0,9 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 11.171.025 | 0,6 % |
| `412P` | SALUD PÚBLICA | 7.629.729 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 3.112.904 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 803,25 M€ (803.249.554 €) · 12 códigos · 18,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 243.688.779 | 30,3 % |
| `422C` | EDUCACIÓN SECUNDARIA | 221.334.312 | 27,6 % |
| `422D` | UNIVERSIDADES | 140.612.743 | 17,5 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 70.406.004 | 8,8 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 42.432.790 | 5,3 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 42.384.091 | 5,3 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 16.004.111 | 2,0 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 15.123.440 | 1,9 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 5.882.712 | 0,7 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.977.552 | 0,2 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.703.630 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.699.390 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 201,09 M€ (201.089.264 €) · 6 códigos · 4,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 111.217.190 | 55,3 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 28.866.586 | 14,4 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 26.305.945 | 13,1 % |
| `711B` | DESARROLLO RURAL | 18.131.130 | 9,0 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 8.862.563 | 4,4 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.705.850 | 3,8 % |

</details>

<details open><summary><b><code>direccion</code> — 1,17 M€ (1.170.788 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.170.788 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 33,43 M€ (33.433.490 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 33.433.490 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 118,34 M€ (118.335.912 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 112.753.082 | 95,3 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 5.582.830 | 4,7 % |

</details>

<details open><summary><b><code>idi</code> — 19,63 M€ (19.626.220 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 19.042.320 | 97,0 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 583.900 | 3,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 367,26 M€ (367.258.757 €) · 3 códigos · 8,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 191.585.147 | 52,2 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 174.941.810 | 47,6 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 731.800 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,47 M€ (1.471.660 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.471.660 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 10,01 M€ (10.006.430 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 10.006.430 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 4,09 M€ (4.092.550 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 4.092.550 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.080,21 M€ · 56 códigos · 24,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 478.611.000 |
| `513H` | CARRETERAS | 65.183.540 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 54.338.909 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 40.033.663 |
| `513G` | TRANSPORTES | 35.586.430 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 35.425.872 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 35.065.846 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 27.093.584 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 25.212.390 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 22.537.200 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 20.620.000 |
| `612F` | GESTIÓN DEL PATRIMONIO | 20.565.181 |
| `443F` | RECURSOS NATURALES | 18.037.366 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 18.004.857 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 17.911.221 |
| `111B` | ACTIVIDAD LEGISLATIVA | 14.783.000 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 9.635.730 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 9.326.826 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 8.558.810 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 7.018.493 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.847.960 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 6.497.475 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.293.705 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 5.882.139 |
| `121B` | DIRECCIÓN DE LA FUNCIÓN PÚBLICA | 5.830.460 |
| … | *resto: 31 códigos* | 85.309.690 |

</details>

### 2020

*Fuente: `tomo_I.pdf` · 96 líneas · total extraído **4.610,31 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.804,31 M€ (1.804.307.655 €) · 6 códigos · 39,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.769.573.081 | 98,1 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 12.609.860 | 0,7 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 10.916.271 | 0,6 % |
| `412P` | SALUD PÚBLICA | 7.173.330 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 3.123.943 | 0,2 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 911.170 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 845,30 M€ (845.304.215 €) · 12 códigos · 18,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 250.709.687 | 29,7 % |
| `422C` | EDUCACIÓN SECUNDARIA | 238.120.885 | 28,2 % |
| `422D` | UNIVERSIDADES | 149.268.217 | 17,7 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 74.171.771 | 8,8 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 47.071.005 | 5,6 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 42.678.791 | 5,0 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 16.511.440 | 2,0 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.822.100 | 1,8 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 6.126.133 | 0,7 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 2.228.902 | 0,3 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 1.904.630 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.690.654 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 200,87 M€ (200.868.212 €) · 6 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 100.624.600 | 50,1 % |
| `711B` | DESARROLLO RURAL | 30.657.055 | 15,3 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 26.955.953 | 13,4 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 26.658.895 | 13,3 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 8.368.489 | 4,2 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 7.603.220 | 3,8 % |

</details>

<details open><summary><b><code>direccion</code> — 2,44 M€ (2.439.133 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.840.953 | 75,5 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 598.180 | 24,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 34,75 M€ (34.749.348 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 33.687.548 | 96,9 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.061.800 | 3,1 % |

</details>

<details open><summary><b><code>empleo</code> — 118,58 M€ (118.580.815 €) · 2 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 113.772.615 | 95,9 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 4.808.200 | 4,1 % |

</details>

<details open><summary><b><code>idi</code> — 27,79 M€ (27.787.023 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 26.498.513 | 95,4 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 649.010 | 2,3 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 639.500 | 2,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 369,94 M€ (369.942.822 €) · 3 códigos · 8,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 201.135.877 | 54,4 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 168.051.405 | 45,4 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 755.540 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,38 M€ (1.377.070 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.377.070 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 10,32 M€ (10.322.743 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 10.322.743 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 5,07 M€ (5.073.031 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 5.073.031 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.189,56 M€ · 57 códigos · 25,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 569.466.340 |
| `513H` | CARRETERAS | 72.164.706 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 57.829.614 |
| `511A` | DIRECCIÓN Y SERVICIOS GENERALES | 46.398.993 |
| `513G` | TRANSPORTES | 40.851.996 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 39.319.092 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 37.601.410 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 28.235.323 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 27.727.070 |
| `441A` | INFRAESTRUCTURA URBANA EN SANEAMIENTO Y ABASTECIMIENTO DE AGUAS | 22.697.273 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 22.156.580 |
| `443F` | RECURSOS NATURALES | 18.788.707 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 17.689.514 |
| `612F` | GESTIÓN DEL PATRIMONIO | 16.790.020 |
| `111B` | ACTIVIDAD LEGISLATIVA | 15.119.000 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 10.204.533 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 10.018.367 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 9.323.930 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 8.981.997 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 8.380.410 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 7.257.305 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 6.843.825 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 6.834.138 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 6.583.469 |
| `121B` | DIRECCIÓN DE LA FUNCIÓN PÚBLICA | 5.987.730 |
| … | *resto: 32 códigos* | 76.303.812 |

</details>

### 2021

*Fuente: `tomo_I.pdf` · 97 líneas · total extraído **5.095,10 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.946,22 M€ (1.946.219.173 €) · 6 códigos · 38,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.899.929.251 | 97,6 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 19.396.404 | 1,0 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 12.517.062 | 0,6 % |
| `412P` | SALUD PÚBLICA | 8.057.056 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 4.189.404 | 0,2 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 2.129.996 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 894,35 M€ (894.354.551 €) · 12 códigos · 17,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 269.858.613 | 30,2 % |
| `422C` | EDUCACIÓN SECUNDARIA | 247.291.932 | 27,7 % |
| `422D` | UNIVERSIDADES | 155.665.988 | 17,4 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 80.261.358 | 9,0 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 48.765.056 | 5,5 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 43.674.171 | 4,9 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 16.896.152 | 1,9 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 14.793.860 | 1,7 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 6.941.654 | 0,8 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 6.409.953 | 0,7 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 2.077.271 | 0,2 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 1.718.543 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 230,81 M€ (230.805.182 €) · 6 códigos · 4,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 134.298.590 | 58,2 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 27.220.540 | 11,8 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 25.633.432 | 11,1 % |
| `711B` | DESARROLLO RURAL | 24.485.687 | 10,6 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 10.443.873 | 4,5 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 8.723.060 | 3,8 % |

</details>

<details open><summary><b><code>direccion</code> — 3,02 M€ (3.023.635 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.941.565 | 64,2 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 1.082.070 | 35,8 % |

</details>

<details open><summary><b><code>vivienda</code> — 38,39 M€ (38.394.597 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 36.725.415 | 95,7 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.669.182 | 4,3 % |

</details>

<details open><summary><b><code>empleo</code> — 133,48 M€ (133.483.253 €) · 2 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 129.292.755 | 96,9 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 4.190.498 | 3,1 % |

</details>

<details open><summary><b><code>idi</code> — 34,38 M€ (34.376.141 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 32.405.941 | 94,3 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 1.004.100 | 2,9 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 966.100 | 2,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 384,50 M€ (384.496.606 €) · 3 códigos · 7,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 225.883.108 | 58,7 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 157.824.350 | 41,0 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 789.148 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,41 M€ (1.414.020 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.349.020 | 95,4 % |
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 65.000 | 4,6 % |

</details>

<details open><summary><b><code>turismo</code> — 12,23 M€ (12.233.440 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 12.233.440 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,91 M€ (6.907.500 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | PROMOCIÓN DE LA MUJER. IGUALDAD DE OPORTUNIDADES | 6.907.500 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.409,39 M€ · 57 códigos · 27,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 625.133.500 |
| `633A` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 107.050.000 |
| `513H` | CARRETERAS | 84.123.213 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 61.540.990 |
| `513G` | TRANSPORTES | 53.265.665 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 45.053.730 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 41.381.646 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 37.794.133 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 30.948.460 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 24.178.222 |
| `443F` | RECURSOS NATURALES | 22.709.727 |
| `632D` | POLÍTICA FINANCIERA | 21.256.863 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 20.730.390 |
| `612F` | GESTIÓN DEL PATRIMONIO | 18.319.847 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 15.795.750 |
| `111B` | ACTIVIDAD LEGISLATIVA | 15.326.000 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 15.175.100 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 10.668.507 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 10.477.309 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 9.575.270 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 9.312.040 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 8.901.821 |
| `457C` | ESTACIÓN INVERNAL Y DE MONTAÑA DE PAJARES | 7.732.316 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 7.547.066 |
| `126C` | POLICÍA Y PROTECCIÓN DE EDIFICIOS | 7.437.936 |
| … | *resto: 32 códigos* | 97.955.161 |

</details>

### 2022

*Fuente: `tomo_I.pdf` · 97 líneas · total extraído **5.239,75 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.991,08 M€ (1.991.084.581 €) · 6 códigos · 38,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 1.937.755.019 | 97,3 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 26.082.340 | 1,3 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 13.667.240 | 0,7 % |
| `412P` | SALUD PÚBLICA | 7.764.927 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 3.701.034 | 0,2 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 2.114.021 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 942,70 M€ (942.696.580 €) · 12 códigos · 18,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 276.395.899 | 29,3 % |
| `422C` | EDUCACIÓN SECUNDARIA | 262.656.459 | 27,9 % |
| `422D` | UNIVERSIDADES | 159.602.188 | 16,9 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 91.116.362 | 9,7 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 55.848.251 | 5,9 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 44.703.921 | 4,7 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 16.885.062 | 1,8 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 15.689.950 | 1,7 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 8.422.918 | 0,9 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 6.688.892 | 0,7 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 2.481.237 | 0,3 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 2.205.441 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 233,28 M€ (233.277.063 €) · 6 códigos · 4,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 134.558.682 | 57,7 % |
| `711B` | DESARROLLO RURAL | 27.342.186 | 11,7 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 25.956.285 | 11,1 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 25.088.690 | 10,8 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 14.532.480 | 6,2 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 5.798.740 | 2,5 % |

</details>

<details open><summary><b><code>direccion</code> — 3,09 M€ (3.089.828 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.971.118 | 63,8 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 1.118.710 | 36,2 % |

</details>

<details open><summary><b><code>vivienda</code> — 41,28 M€ (41.281.152 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 39.465.130 | 95,6 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.816.022 | 4,4 % |

</details>

<details open><summary><b><code>empleo</code> — 142,37 M€ (142.372.110 €) · 2 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 132.219.540 | 92,9 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 10.152.570 | 7,1 % |

</details>

<details open><summary><b><code>idi</code> — 40,56 M€ (40.562.078 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 36.724.638 | 90,5 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 2.810.690 | 6,9 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 1.026.750 | 2,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 387,39 M€ (387.390.363 €) · 3 códigos · 7,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 242.984.268 | 62,7 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 143.586.015 | 37,1 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 820.080 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,50 M€ (1.495.375 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.420.375 | 95,0 % |
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 75.000 | 5,0 % |

</details>

<details open><summary><b><code>turismo</code> — 12,86 M€ (12.859.884 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 12.859.884 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,53 M€ (11.532.497 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | IGUALDAD ENTRE MUJERES Y HOMBRES | 11.532.497 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.432,11 M€ · 57 códigos · 27,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 602.791.476 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 86.091.233 |
| `513H` | CARRETERAS | 78.584.154 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 67.813.819 |
| `513G` | TRANSPORTES | 58.677.816 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 58.516.290 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 52.174.121 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 49.328.993 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 31.336.430 |
| `443F` | RECURSOS NATURALES | 27.067.238 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 24.502.749 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 22.642.093 |
| `632D` | POLÍTICA FINANCIERA | 22.126.342 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 20.117.327 |
| `612F` | GESTIÓN DEL PATRIMONIO | 19.053.851 |
| `111B` | ACTIVIDAD LEGISLATIVA | 15.854.000 |
| `443D` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 14.735.223 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 14.291.275 |
| `457C` | ESTACIÓN INVERNAL Y DE MONTAÑA DE PAJARES | 12.860.173 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 12.379.153 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 10.973.020 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 9.732.870 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 8.224.475 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 7.983.097 |
| `514B` | INFRAESTRUCTURA Y EXPLOTACIÓN PORTUARIA | 7.961.491 |
| … | *resto: 32 códigos* | 96.292.688 |

</details>

### 2023

*Fuente: `tomo_I.pdf` · 97 líneas · total extraído **5.846,19 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.119,65 M€ (2.119.645.347 €) · 6 códigos · 36,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 2.035.518.742 | 96,0 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 58.335.083 | 2,8 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 11.018.420 | 0,5 % |
| `412P` | SALUD PÚBLICA | 8.225.102 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 4.161.924 | 0,2 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 2.386.076 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 999,12 M€ (999.121.164 €) · 12 códigos · 17,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 288.589.870 | 28,9 % |
| `422C` | EDUCACIÓN SECUNDARIA | 281.206.786 | 28,1 % |
| `422D` | UNIVERSIDADES | 172.776.885 | 17,3 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 99.299.060 | 9,9 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 58.276.139 | 5,8 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 47.354.803 | 4,7 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 18.768.688 | 1,9 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 16.297.450 | 1,6 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 7.127.029 | 0,7 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 5.162.602 | 0,5 % |
| `422R` | PROMOCIÓN DEL ASTURIANO | 2.535.701 | 0,3 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.726.151 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 245,49 M€ (245.492.124 €) · 6 códigos · 4,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 139.489.442 | 56,8 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 27.843.262 | 11,3 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 27.710.388 | 11,3 % |
| `711B` | DESARROLLO RURAL | 27.638.286 | 11,3 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 16.548.356 | 6,7 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 6.262.390 | 2,6 % |

</details>

<details open><summary><b><code>direccion</code> — 3,05 M€ (3.045.108 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 1.920.118 | 63,1 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 1.124.990 | 36,9 % |

</details>

<details open><summary><b><code>vivienda</code> — 81,24 M€ (81.235.132 €) · 2 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 79.339.082 | 97,7 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.896.050 | 2,3 % |

</details>

<details open><summary><b><code>empleo</code> — 167,23 M€ (167.228.333 €) · 2 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 153.654.249 | 91,9 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 13.574.084 | 8,1 % |

</details>

<details open><summary><b><code>idi</code> — 56,87 M€ (56.866.955 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 36.681.111 | 64,5 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 19.115.834 | 33,6 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 1.070.010 | 1,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 424,81 M€ (424.813.308 €) · 3 códigos · 7,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 284.374.827 | 66,9 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 139.710.781 | 32,9 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 727.700 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,88 M€ (1.880.600 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 1.790.600 | 95,2 % |
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 90.000 | 4,8 % |

</details>

<details open><summary><b><code>turismo</code> — 30,35 M€ (30.351.673 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 30.351.673 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 13,22 M€ (13.215.572 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | POLÍTICAS DE IGUALDAD ENTRE MUJERES Y HOMBRES | 13.215.572 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.703,30 M€ · 57 códigos · 29,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 643.953.671 |
| `513H` | CARRETERAS | 108.810.929 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 105.645.335 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 100.442.397 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 99.995.227 |
| `513G` | TRANSPORTES | 76.974.397 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 73.105.460 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 50.661.837 |
| `443F` | RECURSOS NATURALES | 42.978.525 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 33.983.080 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 26.637.103 |
| `455E` | PROMOCIÓN CULTURAL,BIBLIOTECAS,ARCHIVOS Y MUSEOS | 26.541.506 |
| `612F` | GESTIÓN DEL PATRIMONIO | 26.461.546 |
| `443D` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 26.109.699 |
| `723A` | APOYO FINANCIERO Y PARTICIPACIÓN EN EMPRESAS PÚBLICAS | 22.416.264 |
| `632D` | POLÍTICA FINANCIERA | 21.904.708 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 17.566.241 |
| `111B` | ACTIVIDAD LEGISLATIVA | 16.964.000 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 15.097.288 |
| `514B` | INFRAESTRUCTURA Y EXPLOTACIÓN PORTUARIA | 12.861.600 |
| `443E` | PROTECCIÓN DE LA SALUD Y DEFENSA DEL CONSUMIDOR | 10.738.150 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 10.494.535 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 10.461.089 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 8.236.195 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 7.979.261 |
| … | *resto: 32 códigos* | 106.279.451 |

</details>

### 2024

*Fuente: `tomo_I.pdf` · 106 líneas · total extraído **6.237,36 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.326,99 M€ (2.326.987.285 €) · 8 códigos · 37,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 2.235.598.332 | 96,1 % |
| `411C` | INFRAESTRUCTURAS SANITARIAS Y SISTEMAS INFORMACIÓN | 54.934.640 | 2,4 % |
| `443C` | PROTECCIÓN DE LA SALUD | 9.582.750 | 0,4 % |
| `412P` | SALUD PÚBLICA | 9.385.043 | 0,4 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 7.560.131 | 0,3 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 4.130.914 | 0,2 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 3.039.025 | 0,1 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.756.450 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.042,25 M€ (1.042.251.593 €) · 12 códigos · 16,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 309.031.135 | 29,7 % |
| `422C` | EDUCACIÓN SECUNDARIA | 296.929.822 | 28,5 % |
| `422D` | UNIVERSIDADES | 181.971.460 | 17,5 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 89.009.790 | 8,5 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 58.480.201 | 5,6 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 49.716.147 | 4,8 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 19.226.504 | 1,8 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 17.044.600 | 1,6 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 7.149.745 | 0,7 % |
| `422H` | PLANIFICACIÓN FORMACIÓN PROFESIONAL | 6.614.257 | 0,6 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 5.216.222 | 0,5 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 1.861.710 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 238,68 M€ (238.684.549 €) · 6 códigos · 3,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADERAS | 145.170.390 | 60,8 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 31.939.178 | 13,4 % |
| `711B` | DESARROLLO RURAL | 26.829.910 | 11,2 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 15.458.234 | 6,5 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 14.479.887 | 6,1 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 4.806.950 | 2,0 % |

</details>

<details open><summary><b><code>direccion</code> — 3,27 M€ (3.272.450 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 2.166.100 | 66,2 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 1.106.350 | 33,8 % |

</details>

<details open><summary><b><code>vivienda</code> — 98,36 M€ (98.362.253 €) · 1 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 98.362.253 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 178,97 M€ (178.971.000 €) · 3 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 159.891.640 | 89,3 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 12.374.210 | 6,9 % |
| `121B` | DIRECCIÓN EMPLEO PÚBLICO | 6.705.150 | 3,7 % |

</details>

<details open><summary><b><code>idi</code> — 59,80 M€ (59.804.421 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 53.475.165 | 89,4 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 5.138.446 | 8,6 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 1.190.810 | 2,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 477,48 M€ (477.484.711 €) · 4 códigos · 7,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 252.208.041 | 52,8 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 155.254.736 | 32,5 % |
| `313G` | AYUDAS DIVERSAS CON FINES SOCIALES | 69.257.580 | 14,5 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 764.354 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,76 M€ (5.763.130 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 2.947.640 | 51,1 % |
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 2.815.490 | 48,9 % |

</details>

<details open><summary><b><code>turismo</code> — 40,59 M€ (40.587.909 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 40.587.909 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,84 M€ (14.837.739 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | POLÍTICAS DE IGUALDAD ENTRE MUJERES Y HOMBRES | 14.837.739 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.750,36 M€ · 63 códigos · 28,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 652.641.000 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 135.720.382 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 115.847.564 |
| `513H` | CARRETERAS | 102.182.200 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 96.588.852 |
| `513G` | TRANSPORTES | 81.082.604 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 79.428.765 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 51.433.163 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 39.153.160 |
| `443A` | CUSTODIA TERRITORIO | 31.873.010 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 28.613.722 |
| `612F` | GESTIÓN DEL PATRIMONIO | 26.559.372 |
| `443D` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 26.134.403 |
| `111B` | ACTIVIDAD LEGISLATIVA | 19.195.000 |
| `455E` | INSTITUCIONES CULTURALES | 17.131.979 |
| `723D` | APOYO AL DESARROLLO ECONÓMICO SOSTENIBLE | 15.923.375 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 15.836.360 |
| `443B` | VIDA SILVESTRE | 15.777.629 |
| `455G` | ACCIÓN CULTURAL Y POLÍTICA LLINGÜÍSTICA | 14.358.276 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 11.899.455 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 10.591.518 |
| `632D` | POLÍTICA FINANCIERA | 10.141.405 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 9.706.763 |
| `126G` | GASTOS CENTRALES DE DIVERSAS CONSEJERÍAS | 9.653.000 |
| `514B` | INFRAESTRUCTURA Y EXPLOTACIÓN PORTUARIA | 9.197.062 |
| … | *resto: 38 códigos* | 123.685.955 |

</details>

### 2025

*Fuente: `tomo_I.pdf` · 107 líneas · total extraído **6.557,90 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.450,66 M€ (2.450.660.157 €) · 8 códigos · 37,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 2.346.169.778 | 95,7 % |
| `411C` | INFRAESTRUCTURAS SANITARIAS Y SISTEMAS INFORMACIÓN | 65.253.483 | 2,7 % |
| `443C` | PROTECCIÓN DE LA SALUD | 10.132.950 | 0,4 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 9.671.304 | 0,4 % |
| `412P` | SALUD PÚBLICA | 9.634.006 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 4.019.274 | 0,2 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 2.959.370 | 0,1 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.819.992 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.093,29 M€ (1.093.294.252 €) · 12 códigos · 16,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 326.868.769 | 29,9 % |
| `422C` | EDUCACIÓN SECUNDARIA | 293.759.057 | 26,9 % |
| `422D` | UNIVERSIDADES | 189.055.393 | 17,3 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 101.791.671 | 9,3 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 67.680.476 | 6,2 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 54.666.708 | 5,0 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 19.486.312 | 1,8 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 18.411.840 | 1,7 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 7.304.309 | 0,7 % |
| `422H` | PLANIFICACIÓN FORMACIÓN PROFESIONAL | 7.166.573 | 0,7 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 4.955.612 | 0,5 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 2.147.532 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 244,91 M€ (244.910.353 €) · 6 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADE- RAS | 148.847.770 | 60,8 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 31.264.116 | 12,8 % |
| `711B` | DESARROLLO RURAL | 29.690.571 | 12,1 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 16.581.687 | 6,8 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 14.679.709 | 6,0 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 3.846.500 | 1,6 % |

</details>

<details open><summary><b><code>direccion</code> — 2,93 M€ (2.927.760 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112A` | SECRETARÍA GENERAL TÉCNICA Y GABINETE TÉCNICO | 2.230.310 | 76,2 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 697.450 | 23,8 % |

</details>

<details open><summary><b><code>vivienda</code> — 158,31 M€ (158.308.659 €) · 2 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 156.632.049 | 98,9 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.676.610 | 1,1 % |

</details>

<details open><summary><b><code>empleo</code> — 177,68 M€ (177.681.916 €) · 3 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 158.126.446 | 89,0 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 12.389.790 | 7,0 % |
| `121B` | DIRECCIÓN EMPLEO PÚBLICO | 7.165.680 | 4,0 % |

</details>

<details open><summary><b><code>idi</code> — 75,41 M€ (75.406.417 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 64.945.626 | 86,1 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 8.684.561 | 11,5 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 1.776.230 | 2,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 516,22 M€ (516.222.251 €) · 4 códigos · 7,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 287.479.349 | 55,7 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 158.655.887 | 30,7 % |
| `313G` | AYUDAS DIVERSAS CON FINES SOCIALES | 69.275.549 | 13,4 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 811.466 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,53 M€ (6.528.430 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 3.429.620 | 52,5 % |
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 3.098.810 | 47,5 % |

</details>

<details open><summary><b><code>turismo</code> — 46,16 M€ (46.161.143 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 46.161.143 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,03 M€ (14.025.107 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | POLÍTICAS DE IGUALDAD ENTRE MUJERES Y HOMBRES | 14.025.107 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.771,77 M€ · 63 códigos · 27,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 656.242.373 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA Y ENERGÍA | 121.608.487 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 108.492.773 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 102.951.298 |
| `513H` | CARRETERAS | 97.418.856 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 88.807.715 |
| `513G` | TRANSPORTES | 78.462.621 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 62.379.580 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 42.881.083 |
| `443D` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 34.830.802 |
| `443A` | CUSTODIA TERRITORIO | 31.577.162 |
| `612F` | GESTIÓN DEL PATRIMONIO | 31.525.143 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 30.045.934 |
| `723D` | APOYO AL DESARROLLO ECONÓMICO SOSTENIBLE | 19.264.985 |
| `111B` | ACTIVIDAD LEGISLATIVA | 18.992.000 |
| `443B` | VIDA SILVESTRE | 18.517.990 |
| `455E` | INSTITUCIONES CULTURALES | 16.435.147 |
| `455G` | ACCIÓN CULTURAL Y POLÍTICA LLINGÜÍSTICA | 16.027.235 |
| `511F` | OBRAS, SERVICIOS Y COOPERACIÓN LOCAL | 14.355.924 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 13.749.350 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 12.299.918 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 9.208.220 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 9.000.481 |
| `514B` | INFRAESTRUCTURA Y EXPLOTACIÓN PORTUARIA | 8.957.882 |
| `521A` | TELECOMUNICACIONES Y SOCIEDAD DE LA INFORMACIÓN | 7.827.517 |
| … | *resto: 38 códigos* | 119.911.193 |

</details>

### 2026

*Fuente: `tomo_I.pdf` · 106 líneas · total extraído **6.872,66 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.554,18 M€ (2.554.175.605 €) · 8 códigos · 37,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413D` | PRESTACIONES SANITARIAS Y PLANIFICACIÓN | 2.474.376.013 | 96,9 % |
| `411C` | INFRAESTRUCTURAS SANITARIAS Y SISTEMAS INFORMACIÓN | 38.154.094 | 1,5 % |
| `443C` | PROTECCIÓN DE LA SALUD | 10.366.400 | 0,4 % |
| `412P` | SALUD PÚBLICA | 10.177.559 | 0,4 % |
| `413E` | CUIDADOS, HUMANIZACIÓN Y ATENCIÓN SOCIOSANITARIA | 9.394.506 | 0,4 % |
| `311B` | DIRECCIÓN Y SERVICIOS GENERALES | 4.861.653 | 0,2 % |
| `413C` | CALIDAD Y SISTEMAS DE INFORMACIÓN | 3.969.673 | 0,2 % |
| `411A` | DIRECCIÓN Y SERVICIOS GENERALES | 2.875.707 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 1.178,92 M€ (1.178.921.574 €) · 11 códigos · 17,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | EDUCACIÓN INFANTIL Y PRIMARIA | 351.308.421 | 29,8 % |
| `422C` | EDUCACIÓN SECUNDARIA | 302.502.221 | 25,7 % |
| `422D` | UNIVERSIDADES | 198.115.212 | 16,8 % |
| `422B` | FORMACIÓN PROFESIONAL INICIAL Y PROYECTOS INNOVADORES | 124.656.972 | 10,6 % |
| `422E` | EDUCACIÓN ESPECIAL Y NECESIDADES EDUCATIVAS ESPECÍFICAS | 85.970.651 | 7,3 % |
| `423B` | SERVICIOS COMPLEMENTARIOS | 60.575.593 | 5,1 % |
| `422G` | ENSEÑANZAS ARTÍSTICAS | 23.875.761 | 2,0 % |
| `421A` | DIRECCIÓN Y ADMINISTRACIÓN EDUCATIVA | 19.132.230 | 1,6 % |
| `422F` | ESCUELAS OFICIALES DE IDIOMAS | 7.586.075 | 0,6 % |
| `421B` | FORMACIÓN PERMANENTE DEL PROFESORADO | 2.878.162 | 0,2 % |
| `422P` | APOYO A LA ACCIÓN EDUCATIVA | 2.320.276 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 253,89 M€ (253.892.390 €) · 6 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `712F` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES GANADE- RAS | 155.224.302 | 61,1 % |
| `531B` | DESARROLLO FORESTAL Y MEJORA ESTRUCTURAS AGRARIAS | 35.579.260 | 14,0 % |
| `711B` | DESARROLLO RURAL | 25.730.000 | 10,1 % |
| `712C` | ORDENACIÓN, REESTRUCTURACIÓN Y MEJORA PRODUCCIONES AGRÍCOLAS | 20.294.267 | 8,0 % |
| `712D` | ORDENACIÓN, FOMENTO Y MEJORA DE LAS PRODUCCIONES PESQUERAS | 13.145.701 | 5,2 % |
| `711A` | DIRECCIÓN Y SERVICIOS GENERALES | 3.918.860 | 1,5 % |

</details>

<details open><summary><b><code>direccion</code> — 3,18 M€ (3.178.680 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `112I` | GABINETE Y OFICINA ECONÓMICA | 2.475.260 | 77,9 % |
| `112H` | APOYO A LA VICEPRESIDENCIA | 703.420 | 22,1 % |

</details>

<details open><summary><b><code>vivienda</code> — 189,07 M€ (189.066.730 €) · 2 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | PROMOCIÓN Y ADMINISTRACIÓN DE LA VIVIENDA | 187.209.040 | 99,0 % |
| `451A` | DIRECCIÓN Y SERVICIOS GENERALES | 1.857.690 | 1,0 % |

</details>

<details open><summary><b><code>empleo</code> — 179,20 M€ (179.198.319 €) · 3 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | TRABAJO Y ORDENACIÓN DE LAS RELACIONES LABORALES | 164.105.359 | 91,6 % |
| `121B` | DIRECCIÓN EMPLEO PÚBLICO | 7.564.630 | 4,2 % |
| `322L` | FOMENTO DEL AUTOEMPLEO Y ECONOMÍA SOCIAL | 7.528.330 | 4,2 % |

</details>

<details open><summary><b><code>idi</code> — 67,41 M€ (67.412.864 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO | 63.424.737 | 94,1 % |
| `541B` | DIRECCIÓN Y SERVICIOS GENERALES | 2.512.438 | 3,7 % |
| `313M` | PLANIFICACIÓN, ORDENACIÓN E INNOVACIÓN SOCIAL | 1.475.689 | 2,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 524,31 M€ (524.305.061 €) · 4 códigos · 7,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | GESTIÓN DE SERVICIOS SOCIALES | 297.709.002 | 56,8 % |
| `313A` | PRESTACIONES Y PROGRAMAS CONCERTADOS | 155.860.970 | 29,7 % |
| `313G` | AYUDAS DIVERSAS CON FINES SOCIALES | 69.925.853 | 13,3 % |
| `313D` | PENSIONES NO CONTRIBUTIVAS | 809.236 | 0,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,72 M€ (6.718.940 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323D` | DIVERSIDAD SEXUAL Y DERECHOS LGTBI | 3.406.440 | 50,7 % |
| `313B` | PROGRAMA DE EMIGRACIÓN ASTURIANA | 3.312.500 | 49,3 % |

</details>

<details open><summary><b><code>turismo</code> — 49,64 M€ (49.644.246 €) · 1 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 49.644.246 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 15,88 M€ (15.884.896 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323B` | POLÍTICAS DE IGUALDAD ENTRE MUJERES Y HOMBRES | 15.884.896 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.850,26 M€ · 63 códigos · 26,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011C` | AMORTIZACIÓN Y GASTOS FINANCIEROS DE LA DEUDA DEL PRINCIPADO DE ASTURIAS | 687.792.420 |
| `441A` | INFRAESTRUCTURAS HIDRÁULICAS Y GESTIÓN DEL AGUA | 109.218.593 |
| `731A` | FOMENTO Y GESTIÓN ENERGÉTICA | 108.975.411 |
| `513H` | CARRETERAS | 97.282.395 |
| `121D` | SISTEMAS DE INFORMACIÓN Y COMUNICACIONES | 93.860.245 |
| `141B` | RELACIONES ADMINISTRACIÓN DE JUSTICIA | 91.810.677 |
| `513G` | TRANSPORTES | 70.544.196 |
| `313F` | ATENCIÓN A LA INFANCIA, FAMILIAS Y ADOLESCENCIA | 66.297.740 |
| `223A` | PROTECCIÓN CIVIL Y SEGURIDAD PÚBLICA | 48.088.271 |
| `443D` | PROTECCIÓN Y MEJORA DEL MEDIO AMBIENTE | 36.175.176 |
| `741G` | ACTUACIONES EN MATERIA DE MINERÍA | 34.054.200 |
| `121A` | DIRECCIÓN Y SERVICIOS GENERALES | 32.720.380 |
| `443A` | CUSTODIA TERRITORIO | 30.778.070 |
| `612F` | GESTIÓN DEL PATRIMONIO | 26.930.480 |
| `111B` | ACTIVIDAD LEGISLATIVA | 20.095.500 |
| `443B` | VIDA SILVESTRE | 18.717.537 |
| `455E` | INSTITUCIONES CULTURALES | 18.660.847 |
| `455G` | ACCIÓN CULTURAL Y POLÍTICA LLINGÜÍSTICA | 18.545.277 |
| `723D` | APOYO AL DESARROLLO ECONÓMICO SOSTENIBLE | 15.661.953 |
| `125A` | COLABORACIÓN CON LAS ENTIDADES LOCALES | 14.138.061 |
| `632D` | POLÍTICA FINANCIERA | 12.858.190 |
| `457D` | INSTALACIONES DEPORTIVAS DEL PRINCIPADO DE ASTURIAS | 11.554.683 |
| `142M` | GESTIÓN DE SERVICIOS DE JUSTICIA DEL MENOR | 11.546.887 |
| `612C` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 10.657.252 |
| `433C` | ORDENACIÓN DEL TERRITORIO | 9.827.302 |
| … | *resto: 38 códigos* | 153.466.251 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py ast     # regenera este documento
python3 tools/auditoria_magnitud.py ast        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa ast --anio <año> \
    --input ../fuentes/raw/ast/<año>/<fichero> --output /tmp/ast.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-ast.md`](limitaciones-ast.md)

