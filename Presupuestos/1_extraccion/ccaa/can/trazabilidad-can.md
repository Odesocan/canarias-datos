# Trazabilidad de la extracción — Canarias (`can`)

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
| **2015** | 139 | `memoria_programas.pdf` | 12 | 38,8 % | 5.898,90 | — | no_aplica |
| **2016** | 140 | `memoria_programas.pdf` | 12 | 38,6 % | 5.937,01 | — | no_aplica |
| **2017** | 141 | `memoria_programas.pdf` | 12 | 38,3 % | 6.305,89 | — | no_aplica |
| **2018** | 140 | `memoria_programas.pdf` | 12 | 38,6 % | 7.000,36 | — | no_aplica |
| **2019** | 142 | `memoria_programas.pdf` | 12 | 39,4 % | 7.511,94 | — | no_aplica |
| **2020** | 144 | `memoria_programas.pdf` | 12 | 39,6 % | 7.698,73 | — | no_aplica |
| **2021** | 141 | `memoria_programas.pdf` | 12 | 39,7 % | 8.044,74 | — | no_aplica |
| **2022** | 135 | `memoria_programas.pdf` | 12 | 40,7 % | 8.608,86 | — | no_aplica |
| **2023** | 135 | `memoria_programas.pdf` | 12 | 40,7 % | 9.701,03 | — | no_aplica |
| **2024** | 140 | `memoria_programas.pdf` | 12 | 40,7 % | 10.745,72 | — | no_aplica |
| **2025** | 141 | `memoria_programas.pdf` | 12 | 41,8 % | 11.108,73 | — | no_aplica |
| **2026** | 143 | `memoria_programas.pdf` | 12 | 42,0 % | 11.910,12 | — | no_aplica |

**URL(s) de origen:**
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2015/TOMO_3_-_2015_Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2016/tomos_ley/TOMO_3_-_2016_Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2017/ley/TOMO_3_2017_Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2018/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2019/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2020/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2021/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2022/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2023/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2024/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2025/ley/TOMO-3-Resumenes.pdf>
- <https://www.gobiernodecanarias.org/cmsgob1/export/sites/hacienda/planificacionypresupuesto/galeria/Presupuestos/2026/ley/TOMO-3-Resumenes.pdf>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 2.459,74 | 2.495,72 | 2.556,57 | 2.739,54 | 2.832,79 | 2.970,65 | 3.088,47 | 3.225,42 | 3.575,65 | 4.108,18 | 4.308,66 | 4.542,05 |
| `educacion` | 1.513,86 | 1.521,04 | 1.563,62 | 1.664,74 | 1.734,25 | 1.854,29 | 1.951,01 | 2.099,97 | 2.275,41 | 2.368,75 | 2.438,48 | 2.606,33 |
| `soberania` | 55,11 | 60,48 | 66,26 | 72,19 | 81,47 | 91,12 | 97,22 | 122,37 | 142,86 | 118,71 | 119,25 | 130,68 |
| `direccion` | 12,35 | 15,49 | 16,76 | 17,80 | 22,80 | 19,65 | 21,54 | 25,17 | 24,58 | 30,93 | 32,40 | 33,60 |
| `vivienda` | 58,07 | 56,91 | 74,28 | 89,63 | 125,98 | 124,68 | 151,41 | 164,00 | 200,81 | 166,17 | 187,33 | 211,83 |
| `empleo` | 90,60 | 67,20 | 64,57 | 64,81 | 84,27 | 85,89 | 85,84 | 91,34 | 113,62 | 93,12 | 97,66 | 96,61 |
| `idi` | 82,05 | 69,97 | 50,87 | 42,45 | 48,07 | 54,72 | 47,28 | 58,64 | 76,00 | 95,07 | 88,66 | 79,70 |
| `dependencia` | 132,90 | 143,41 | 157,03 | 202,91 | 257,53 | 266,52 | 278,84 | 300,56 | 348,66 | 379,25 | 415,94 | 478,36 |
| `discapacidad` | 48,72 | 48,64 | 50,22 | 52,46 | 64,54 | 68,17 | 74,28 | 82,19 | 82,13 | 81,49 | 83,04 | 86,69 |
| `diversidad` | 1,26 | 1,51 | 1,58 | 1,84 | 1,94 | 3,15 | 4,25 | 4,69 | 5,89 | 4,55 | 4,83 | 6,91 |
| `turismo` | 47,66 | 52,72 | 52,86 | 58,80 | 74,72 | 80,11 | 95,38 | 104,77 | 127,70 | 131,14 | 134,49 | 154,80 |
| `igualdad` | 6,82 | 7,09 | 7,81 | 8,89 | 9,77 | 10,78 | 11,87 | 12,66 | 12,84 | 13,41 | 13,63 | 14,67 |
| **Σ asignado** | 4.509,15 | 4.540,17 | 4.662,42 | 5.016,04 | 5.338,13 | 5.629,73 | 5.907,40 | 6.291,79 | 6.986,14 | 7.590,79 | 7.924,37 | 8.442,22 |
| *(sin concepto)* | 1.389,75 | 1.396,84 | 1.643,46 | 1.984,32 | 2.173,81 | 2.069,00 | 2.137,34 | 2.317,08 | 2.714,89 | 3.154,93 | 3.184,36 | 3.467,90 |
| **TOTAL extraído** | 5.898,90 | 5.937,01 | 6.305,89 | 7.000,36 | 7.511,94 | 7.698,73 | 8.044,74 | 8.608,86 | 9.701,03 | 10.745,72 | 11.108,73 | 11.910,12 |

**Conceptos sin ninguna línea en toda la serie:** `salud_mental` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +1,5 % | +2,4 % | +7,2 % | +3,4 % | +4,9 % | +4,0 % | +4,4 % | +10,9 % | +14,9 % | +4,9 % | +5,4 % |
| `educacion` | +0,5 % | +2,8 % | +6,5 % | +4,2 % | +6,9 % | +5,2 % | +7,6 % | +8,4 % | +4,1 % | +2,9 % | +6,9 % |
| `soberania` | +9,7 % | +9,6 % | +8,9 % | +12,9 % | +11,9 % | +6,7 % | +25,9 % | +16,7 % | −16,9 % | +0,4 % | +9,6 % |
| `direccion` | +25,4 % | +8,2 % | +6,2 % | +28,1 % | −13,8 % | +9,6 % | +16,9 % | −2,4 % | +25,8 % | +4,8 % | +3,7 % |
| `vivienda` | −2,0 % | +30,5 % | +20,7 % | +40,6 % ⚠ | −1,0 % | +21,4 % | +8,3 % | +22,4 % | −17,2 % | +12,7 % | +13,1 % |
| `empleo` | −25,8 % | −3,9 % | +0,4 % | +30,0 % | +1,9 % | −0,1 % | +6,4 % | +24,4 % | −18,0 % | +4,9 % | −1,1 % |
| `idi` | −14,7 % | −27,3 % | −16,6 % | +13,3 % | +13,8 % | −13,6 % | +24,0 % | +29,6 % | +25,1 % | −6,7 % | −10,1 % |
| `dependencia` | +7,9 % | +9,5 % | +29,2 % | +26,9 % | +3,5 % | +4,6 % | +7,8 % | +16,0 % | +8,8 % | +9,7 % | +15,0 % |
| `discapacidad` | −0,2 % | +3,2 % | +4,5 % | +23,0 % | +5,6 % | +9,0 % | +10,6 % | −0,1 % | −0,8 % | +1,9 % | +4,4 % |
| `diversidad` | +19,8 % | +4,3 % | +16,5 % | +5,7 % | +62,5 % ⚠ | +34,8 % | +10,2 % | +25,6 % | −22,6 % | +6,0 % | +43,1 % ⚠ |
| `turismo` | +10,6 % | +0,3 % | +11,2 % | +27,1 % | +7,2 % | +19,1 % | +9,8 % | +21,9 % | +2,7 % | +2,5 % | +15,1 % |
| `igualdad` | +4,0 % | +10,2 % | +13,8 % | +9,9 % | +10,3 % | +10,2 % | +6,7 % | +1,4 % | +4,5 % | +1,6 % | +7,6 % |
| **TOTAL** | +0,6 % | +6,2 % | +11,0 % | +7,3 % | +2,5 % | +4,5 % | +7,0 % | +12,7 % | +10,8 % | +3,4 % | +7,2 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2019 | `vivienda` | **SALTO** | 89,63 → 125,98 M€ (+40,6 % ⚠) |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `memoria_programas.pdf` · 139 líneas · total extraído **5.898,90 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.459,74 M€ (2.459.743.096 €) · 4 códigos · 41,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.454.229.799 | 99,8 % |
| `312B` | Hemodonación y Hemoterapia | 2.692.025 | 0,1 % |
| `311A` | Dirección Administrativa y Servicios Generales | 2.607.574 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 213.698 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.513,86 M€ (1.513.863.136 €) · 13 códigos · 25,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 533.386.835 | 35,2 % |
| `322C` | Enseñanza Secundaria y Formación Profesional | 480.646.066 | 31,7 % |
| `322F` | Financiación de las Universidades Canarias | 209.684.437 | 13,9 % |
| `321A` | Dirección Administrativa y Servicios Generales | 163.549.229 | 10,8 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 54.079.306 | 3,6 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 36.735.790 | 2,4 % |
| `323A` | Apoyo a los Estudios Universitarios | 13.091.422 | 0,9 % |
| `421A` | Dirección Administrativa y Servicios Generales | 8.004.330 | 0,5 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 4.624.319 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 4.480.737 | 0,3 % |
| `322D` | Formación Profesional Específica | 3.579.963 | 0,2 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 1.210.702 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 790.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 55,11 M€ (55.114.206 €) · 9 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415B` | Estructuras Pesqueras | 15.330.047 | 27,8 % |
| `411A` | Dirección Administrativa y Servicios Generales | 8.971.639 | 16,3 % |
| `411B` | Coord. Cámaras Agrar. y gest. ayudas FEAGA/FEADER | 7.342.173 | 13,3 % |
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 6.532.407 | 11,9 % |
| `412B` | Ordenación y mejora de la producción agrícola | 5.053.558 | 9,2 % |
| `412C` | Desarrollo ganadero | 5.003.174 | 9,1 % |
| `413A` | Calidad Agroalimentaria | 3.265.804 | 5,9 % |
| `415A` | Desarrollo Pesquero | 2.006.066 | 3,6 % |
| `415C` | Ordenación e Inspección Pesquera | 1.609.338 | 2,9 % |

</details>

<details open><summary><b><code>direccion</code> — 12,35 M€ (12.350.493 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 12.350.493 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 58,07 M€ (58.073.671 €) · 8 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 35.350.978 | 60,9 % |
| `451A` | Dirección Administrativa y Servicios Generales | 6.793.518 | 11,7 % |
| `261E` | Ordenación del territorio | 6.685.874 | 11,5 % |
| `431B` | Comercio Interior | 4.844.629 | 8,3 % |
| `431A` | Promoción Exterior | 2.000.515 | 3,4 % |
| `451C` | Calidad de las Construcciones | 1.887.639 | 3,3 % |
| `451D` | Planificación y Programación de Infraestructuras | 418.954 | 0,7 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 91.564 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 90,60 M€ (90.600.439 €) · 1 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 90.600.439 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 82,05 M€ (82.052.180 €) · 5 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 65.168.189 | 79,4 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 8.563.779 | 10,4 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 6.252.310 | 7,6 % |
| `463B` | Capital Humano Investigador e Innovador | 1.862.027 | 2,3 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 205.875 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 132,90 M€ (132.896.162 €) · 2 códigos · 2,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 96.386.589 | 72,5 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 36.509.573 | 27,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 48,72 M€ (48.724.495 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención Personas Mayores y Personas con Discapac | 32.648.812 | 67,0 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 12.357.219 | 25,4 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 3.718.464 | 7,6 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,26 M€ (1.261.000 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 1.261.000 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 47,66 M€ (47.655.904 €) · 6 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432G` | Promoción y Apoyo a la Comercialización | 20.913.978 | 43,9 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 16.360.101 | 34,3 % |
| `432H` | Planificación Turistíca y Sistema de Información | 3.732.433 | 7,8 % |
| `322A` | Formación Profesional Turística | 3.158.669 | 6,6 % |
| `432F` | Productos Turísticos y Calidad Turística | 2.705.382 | 5,7 % |
| `432A` | Dirección Administrativa y Servicios Generales | 785.341 | 1,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 6,82 M€ (6.818.684 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 6.818.684 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.389,75 M€ · 85 códigos · 23,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 211.048.768 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 208.737.851 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 143.630.000 |
| `112A` | Tribunales de Justicia | 124.105.857 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 80.646.631 |
| `942D` | Otras Transferencias a Corporaciones Locales | 62.445.964 |
| `932A` | Gestion Tributaria | 38.914.394 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 38.184.530 |
| `452C` | Conv. Mº Medio Amb. actuaciones en mat. de aguas | 36.538.308 |
| `231I` | Fomento de la Inclusión Social | 31.250.418 |
| `441E` | Cohesión Interinsular | 29.840.000 |
| `441D` | Movilidad Interior | 24.955.000 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 22.619.913 |
| `132A` | Seguridad y Emergencia | 20.862.673 |
| `923B` | Gestión Patrimonial | 20.499.272 |
| `456G` | Calidad Ambiental | 18.538.980 |
| `454A` | Infraestructura y Mantenimiento de Puertos | 17.880.000 |
| `911A` | Actuación Legislativa y de Control | 15.376.954 |
| `433C` | Promoción Económica | 14.213.699 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 14.013.796 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 13.426.095 |
| `231B` | Coordinación y Planificación de Asuntos Sociales | 13.329.626 |
| `456L` | Parques Nacionales | 11.270.636 |
| `931A` | Control interno y Contabilidad Pública | 11.184.240 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 10.293.455 |
| … | *resto: 60 códigos* | 155.940.755 |

</details>

### 2016

*Fuente: `memoria_programas.pdf` · 140 líneas · total extraído **5.937,01 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.495,72 M€ (2.495.715.117 €) · 4 códigos · 42,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.490.468.217 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 2.753.946 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 2.288.970 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 203.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.521,04 M€ (1.521.043.552 €) · 13 códigos · 25,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 528.714.989 | 34,8 % |
| `322C` | Enseñanza Secundaria y Formación Profesional | 494.481.772 | 32,5 % |
| `322F` | Financiación de las Universidades Canarias | 211.218.220 | 13,9 % |
| `321A` | Dirección Administrativa y Servicios Generales | 156.739.023 | 10,3 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 57.707.306 | 3,8 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 37.065.442 | 2,4 % |
| `323A` | Apoyo a los Estudios Universitarios | 11.955.646 | 0,8 % |
| `421A` | Dirección Administrativa y Servicios Generales | 7.209.538 | 0,5 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 4.822.930 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 4.557.624 | 0,3 % |
| `322D` | Formación Profesional Específica | 3.803.621 | 0,3 % |
| `421B` | Seguridad Industrial y Minera | 1.672.522 | 0,1 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 1.094.919 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 60,48 M€ (60.478.490 €) · 9 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411B` | Coord. Cámaras Agrar. y gest. ayudas FEAGA/FEADER | 12.016.702 | 19,9 % |
| `415A` | Desarrollo Pesquero | 11.378.971 | 18,8 % |
| `411A` | Dirección Administrativa y Servicios Generales | 8.877.658 | 14,7 % |
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 7.772.695 | 12,9 % |
| `415B` | Estructuras Pesqueras | 5.315.174 | 8,8 % |
| `412C` | Desarrollo ganadero | 5.200.514 | 8,6 % |
| `412B` | Ordenación y mejora de la producción agrícola | 4.815.834 | 8,0 % |
| `413A` | Calidad Agroalimentaria | 3.352.529 | 5,5 % |
| `415C` | Ordenación e Inspección Pesquera | 1.748.413 | 2,9 % |

</details>

<details open><summary><b><code>direccion</code> — 15,49 M€ (15.487.547 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 15.487.547 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 56,91 M€ (56.909.628 €) · 8 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 35.587.818 | 62,5 % |
| `261E` | Ordenación del territorio | 7.701.492 | 13,5 % |
| `451A` | Dirección Administrativa y Servicios Generales | 6.314.521 | 11,1 % |
| `431B` | Comercio Interior | 2.655.474 | 4,7 % |
| `431A` | Promoción Exterior | 2.218.709 | 3,9 % |
| `451C` | Calidad de las Construcciones | 1.891.992 | 3,3 % |
| `451D` | Planificación y Programación de Infraestructuras | 448.058 | 0,8 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 91.564 | 0,2 % |

</details>

<details open><summary><b><code>empleo</code> — 67,20 M€ (67.197.270 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 67.197.270 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 69,97 M€ (69.970.661 €) · 5 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 42.467.768 | 60,7 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 14.739.736 | 21,1 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 5.366.626 | 7,7 % |
| `463B` | Capital Humano Investigador e Innovador | 4.390.656 | 6,3 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 3.005.875 | 4,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 143,41 M€ (143.405.273 €) · 2 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 104.208.377 | 72,7 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 39.196.896 | 27,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 48,64 M€ (48.636.101 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención Personas con Discapacidad | 32.854.185 | 67,6 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 12.436.952 | 25,6 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 3.344.964 | 6,9 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,51 M€ (1.511.250 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 1.511.250 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 52,72 M€ (52.724.724 €) · 6 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432G` | Promoción y Apoyo a la Comercialización | 27.459.905 | 52,1 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 17.295.004 | 32,8 % |
| `322A` | Formación Profesional Turística | 3.158.669 | 6,0 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.139.693 | 6,0 % |
| `432A` | Dirección Administrativa y Servicios Generales | 944.390 | 1,8 % |
| `432H` | Planificación Turistíca y Sistema de Información | 727.063 | 1,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,09 M€ (7.088.723 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 7.088.723 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.396,84 M€ · 86 códigos · 23,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 226.616.865 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 214.499.709 |
| `112A` | Tribunales de Justicia | 125.386.619 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 94.190.000 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 86.680.000 |
| `942D` | Otras Transferencias a Corporaciones Locales | 62.664.261 |
| `231I` | Fomento de la Inclusión Social | 48.306.502 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 48.055.841 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 34.734.344 |
| `441E` | Cohesión Interinsular | 33.641.269 |
| `932A` | Gestion Tributaria | 32.797.646 |
| `441D` | Movilidad Interior | 25.000.000 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 22.639.138 |
| `132A` | Seguridad y Emergencia | 21.660.510 |
| `923B` | Gestión Patrimonial | 20.185.498 |
| `452C` | Conv. Mº Medio Amb. actuaciones en mat. de aguas | 19.015.194 |
| `425A` | Desarrollo Energético | 16.625.642 |
| `911A` | Actuación Legislativa y de Control | 15.947.700 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 15.706.736 |
| `433C` | Promoción Económica | 15.223.417 |
| `456G` | Calidad Ambiental | 14.215.453 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 13.808.397 |
| `931A` | Control interno y Contabilidad Pública | 9.805.795 |
| `456L` | Parques Nacionales | 8.669.504 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 8.448.223 |
| … | *resto: 61 códigos* | 162.314.751 |

</details>

### 2017

*Fuente: `memoria_programas.pdf` · 141 líneas · total extraído **6.305,89 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.556,57 M€ (2.556.566.464 €) · 4 códigos · 40,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.550.676.955 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.042.677 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 2.642.848 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 203.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.563,62 M€ (1.563.618.246 €) · 13 códigos · 24,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 534.959.303 | 34,2 % |
| `322C` | Enseñanza Secundaria y Formación Profesional | 519.539.051 | 33,2 % |
| `322F` | Financiación de las Universidades Canarias | 215.642.216 | 13,8 % |
| `321A` | Dirección Administrativa y Servicios Generales | 154.548.688 | 9,9 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 63.224.202 | 4,0 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 37.312.416 | 2,4 % |
| `323A` | Apoyo a los Estudios Universitarios | 14.060.050 | 0,9 % |
| `421A` | Dirección Administrativa y Servicios Generales | 7.447.184 | 0,5 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 4.831.849 | 0,3 % |
| `322D` | Formación Profesional Específica | 4.803.621 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 4.617.747 | 0,3 % |
| `421B` | Seguridad Industrial y Minera | 1.519.000 | 0,1 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 1.112.919 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 66,26 M€ (66.258.575 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415A` | Desarrollo Pesquero | 15.848.558 | 23,9 % |
| `411A` | Dirección Administrativa y Servicios Generales | 9.289.211 | 14,0 % |
| `411B` | Coord. Cámaras Agrar. y gest. ayudas FEAGA/FEADER | 9.002.417 | 13,6 % |
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 7.950.291 | 12,0 % |
| `412B` | Ordenación y mejora de la producción agrícola | 6.279.456 | 9,5 % |
| `415B` | Estructuras Pesqueras | 6.061.170 | 9,1 % |
| `412C` | Desarrollo ganadero | 5.451.024 | 8,2 % |
| `413A` | Calidad Agroalimentaria | 4.184.073 | 6,3 % |
| `415C` | Ordenación e Inspección Pesquera | 2.192.375 | 3,3 % |

</details>

<details open><summary><b><code>direccion</code> — 16,76 M€ (16.763.340 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 16.763.340 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 74,28 M€ (74.279.189 €) · 8 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 38.502.544 | 51,8 % |
| `451D` | Planificación y Programación de Infraestructuras | 13.569.660 | 18,3 % |
| `261E` | Ordenación del territorio | 8.380.589 | 11,3 % |
| `451A` | Dirección Administrativa y Servicios Generales | 5.277.146 | 7,1 % |
| `431B` | Comercio Interior | 3.275.878 | 4,4 % |
| `431A` | Promoción Exterior | 2.518.709 | 3,4 % |
| `451C` | Calidad de las Construcciones | 1.864.663 | 2,5 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios 0 | 890.000 | 1,2 % |

</details>

<details open><summary><b><code>empleo</code> — 64,57 M€ (64.567.875 €) · 1 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 64.567.875 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 50,87 M€ (50.868.847 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 28.136.963 | 55,3 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 10.081.591 | 19,8 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 5.581.504 | 11,0 % |
| `463B` | Capital Humano Investigador e Innovador | 3.968.789 | 7,8 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 3.100.000 | 6,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 157,03 M€ (157.033.480 €) · 2 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 118.363.914 | 75,4 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 38.669.566 | 24,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 50,22 M€ (50.215.994 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 33.874.942 | 67,5 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 13.281.498 | 26,4 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 3.059.554 | 6,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,58 M€ (1.576.250 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 1.576.250 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 52,86 M€ (52.861.263 €) · 6 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432G` | Promoción y Apoyo a la Comercialización | 24.276.794 | 45,9 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 19.029.663 | 36,0 % |
| `322A` | Formación Profesional Turística | 3.518.669 | 6,7 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.085.456 | 5,8 % |
| `432H` | Planificación Turistíca y Sistema de Información | 2.790.791 | 5,3 % |
| `432A` | Dirección Administrativa y Servicios Generales | 159.890 | 0,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,81 M€ (7.813.732 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 7.813.732 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.643,46 M€ · 87 códigos · 26,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 234.427.564 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 217.538.157 |
| `943A` | Fondo de desarrollo de Canarias | 158.834.129 |
| `112A` | Tribunales de Justicia | 134.096.532 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 96.054.084 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 91.906.636 |
| `942D` | Otras Transferencias a Corporaciones Locales | 62.818.648 |
| `231I` | Fomento de la Inclusión Social | 55.306.502 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 48.327.202 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 40.300.003 |
| `932A` | Gestion Tributaria | 37.366.522 |
| `441E` | Cohesión Interinsular | 33.606.269 |
| `923C` | Gestión del Tesoro y Política Financiera | 27.130.138 |
| `441D` | Movilidad Interior | 25.048.500 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 23.303.610 |
| `132A` | Seguridad y Emergencia | 22.535.859 |
| `923B` | Gestión Patrimonial | 21.897.565 |
| `452C` | Conv. Mº Medio Amb. actuaciones en mat. de aguas | 19.015.196 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 19.000.000 |
| `425A` | Desarrollo Energético | 16.469.539 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 16.221.384 |
| `911A` | Actuación Legislativa y de Control | 15.947.700 |
| `433C` | Promoción Económica | 15.407.332 |
| `456G` | Calidad Ambiental | 13.874.371 |
| `239A` | Dirección Administrativa y Servicios Generales | 10.138.822 |
| … | *resto: 62 códigos* | 186.892.150 |

</details>

### 2018

*Fuente: `memoria_programas.pdf` · 140 líneas · total extraído **7.000,36 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.739,54 M€ (2.739.535.209 €) · 4 códigos · 39,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.733.393.582 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.123.041 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 2.814.602 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 203.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.664,74 M€ (1.664.736.166 €) · 13 códigos · 23,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 568.427.780 | 34,1 % |
| `322C` | Enseñanza Secundaria y Formación Profesional | 565.307.359 | 34,0 % |
| `322F` | Financiación de las Universidades Canarias | 228.557.109 | 13,7 % |
| `321A` | Dirección Administrativa y Servicios Generales | 157.533.579 | 9,5 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 64.224.202 | 3,9 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 39.125.738 | 2,4 % |
| `323A` | Apoyo a los Estudios Universitarios | 15.119.828 | 0,9 % |
| `421A` | Dirección Administrativa y Servicios Generales | 7.953.119 | 0,5 % |
| `322J` | Formación Profesional Marítimo Pesquera | 4.970.970 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 4.892.277 | 0,3 % |
| `322D` | Formación Profesional Específica | 4.803.621 | 0,3 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 2.301.584 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 1.519.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 72,19 M€ (72.187.990 €) · 9 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411B` | Coord. Cámaras Agrar. y gest. ayudas FEAGA/FEADER | 11.694.773 | 16,2 % |
| `415B` | Estructuras Pesqueras | 10.824.160 | 15,0 % |
| `415A` | Desarrollo Pesquero | 10.784.267 | 14,9 % |
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 9.984.040 | 13,8 % |
| `411A` | Dirección Administrativa y Servicios Generales | 9.647.219 | 13,4 % |
| `412B` | Ordenación y mejora de la producción agrícola | 6.273.289 | 8,7 % |
| `412C` | Desarrollo ganadero | 6.186.304 | 8,6 % |
| `413A` | Calidad Agroalimentaria | 4.470.738 | 6,2 % |
| `415C` | Ordenación e Inspección Pesquera | 2.323.200 | 3,2 % |

</details>

<details open><summary><b><code>direccion</code> — 17,80 M€ (17.799.301 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 17.799.301 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 89,63 M€ (89.630.513 €) · 8 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 42.385.705 | 47,3 % |
| `451D` | Planificación y Programación de Infraestructuras | 18.599.046 | 20,8 % |
| `261E` | Ordenación del territorio | 8.051.462 | 9,0 % |
| `451A` | Dirección Administrativa y Servicios Generales | 5.945.060 | 6,6 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 4.890.000 | 5,5 % |
| `431A` | Promoción Exterior | 4.019.899 | 4,5 % |
| `431B` | Comercio Interior | 3.832.357 | 4,3 % |
| `451C` | Calidad de las Construcciones | 1.906.984 | 2,1 % |

</details>

<details open><summary><b><code>empleo</code> — 64,81 M€ (64.810.392 €) · 1 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 64.810.392 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 42,45 M€ (42.445.674 €) · 5 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 18.656.358 | 44,0 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 10.637.169 | 25,1 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 5.761.498 | 13,6 % |
| `463B` | Capital Humano Investigador e Innovador | 4.290.649 | 10,1 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 3.100.000 | 7,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 202,91 M€ (202.912.218 €) · 2 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 162.215.406 | 79,9 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 40.696.812 | 20,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 52,46 M€ (52.459.748 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 35.875.372 | 68,4 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 13.815.072 | 26,3 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 2.769.304 | 5,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,84 M€ (1.836.250 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 1.836.250 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 58,80 M€ (58.797.690 €) · 6 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 25.595.424 | 43,5 % |
| `432G` | Promoción y Apoyo a la Comercialización | 23.639.493 | 40,2 % |
| `322A` | Formación Profesional Turística | 3.723.789 | 6,3 % |
| `432F` | Productos Turísticos y Calidad Turística | 2.859.246 | 4,9 % |
| `432H` | Planificación Turistíca y Sistema de Información | 2.819.848 | 4,8 % |
| `432A` | Dirección Administrativa y Servicios Generales | 159.890 | 0,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,89 M€ (8.889.380 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 8.889.380 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.984,32 M€ · 86 códigos · 28,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 280.060.126 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 246.634.111 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 218.050.000 |
| `943A` | Fondo de desarrollo de Canarias | 160.000.000 |
| `112A` | Tribunales de Justicia | 140.213.067 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 82.659.274 |
| `942D` | Otras Transferencias a Corporaciones Locales | 63.631.072 |
| `231I` | Fomento de la Inclusión Social | 60.047.807 |
| `441E` | Cohesión Interinsular | 51.020.538 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 50.461.886 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 45.412.720 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 45.378.929 |
| `932A` | Gestion Tributaria | 41.677.042 |
| `425A` | Desarrollo Energético | 30.972.810 |
| `441D` | Movilidad Interior | 27.900.000 |
| `923C` | Gestión del Tesoro y Política Financiera | 27.208.439 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 27.111.527 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 25.335.560 |
| `923B` | Gestión Patrimonial | 25.287.605 |
| `132A` | Seguridad y Emergencia | 23.643.414 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 22.956.152 |
| `433C` | Promoción Económica | 17.746.417 |
| `911A` | Actuación Legislativa y de Control | 16.222.930 |
| `456G` | Calidad Ambiental | 16.111.626 |
| `239A` | Dirección Administrativa y Servicios Generales | 11.039.984 |
| … | *resto: 61 códigos* | 227.539.333 |

</details>

### 2019

*Fuente: `memoria_programas.pdf` · 142 líneas · total extraído **7.511,94 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.832,79 M€ (2.832.787.821 €) · 5 códigos · 37,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.826.245.730 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.175.410 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 2.862.697 | 0,1 % |
| `313A` | Salud Pública 0 | 300.000 | 0,0 % |
| `311B` | Formación Sanitaria y Social | 203.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.734,25 M€ (1.734.250.398 €) · 13 códigos · 23,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 608.285.787 | 35,1 % |
| `322C` | Enseñanza Secundaria y Formación Profesional | 577.150.952 | 33,3 % |
| `322F` | Financiación de las Universidades Canarias | 234.370.739 | 13,5 % |
| `321A` | Dirección Administrativa y Servicios Generales | 160.394.845 | 9,2 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 67.954.202 | 3,9 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 42.564.556 | 2,5 % |
| `323A` | Apoyo a los Estudios Universitarios | 16.066.502 | 0,9 % |
| `421A` | Dirección Administrativa y Servicios Generales | 8.217.766 | 0,5 % |
| `322D` | Formación Profesional Específica | 5.621.593 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 5.317.929 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 5.056.713 | 0,3 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 1.789.814 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 1.459.000 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 81,47 M€ (81.466.630 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 20.755.191 | 25,5 % |
| `415B` | Estructuras Pesqueras | 11.275.277 | 13,8 % |
| `415A` | Desarrollo Pesquero | 10.858.777 | 13,3 % |
| `411A` | Dirección Administrativa y Servicios Generales | 10.123.231 | 12,4 % |
| `411B` | Coord. Cámaras Agrar. y gest. ayudas FEAGA/FEADER | 9.118.308 | 11,2 % |
| `412B` | Ordenación y mejora de la producción agrícola | 6.410.762 | 7,9 % |
| `412C` | Desarrollo ganadero | 6.089.567 | 7,5 % |
| `413A` | Calidad Agroalimentaria | 4.531.197 | 5,6 % |
| `415C` | Ordenación e Inspección Pesquera | 2.304.320 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 22,80 M€ (22.801.339 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 22.801.339 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 125,98 M€ (125.977.817 €) · 8 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 59.964.381 | 47,6 % |
| `451D` | Planificación y Programación de Infraestructuras | 33.229.608 | 26,4 % |
| `261E` | Ordenación del territorio | 11.132.255 | 8,8 % |
| `431B` | Comercio Interior | 6.853.184 | 5,4 % |
| `451A` | Dirección Administrativa y Servicios Generales | 6.025.764 | 4,8 % |
| `431A` | Promoción Exterior | 5.352.931 | 4,2 % |
| `451C` | Calidad de las Construcciones | 1.929.694 | 1,5 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 1.490.000 | 1,2 % |

</details>

<details open><summary><b><code>empleo</code> — 84,27 M€ (84.268.994 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 84.268.994 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 48,07 M€ (48.074.715 €) · 6 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 19.162.810 | 39,9 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 12.158.607 | 25,3 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 6.258.026 | 13,0 % |
| `463B` | Capital Humano Investigador e Innovador | 4.395.272 | 9,1 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 3.400.000 | 7,1 % |
| `463A` | Ciencia, Tecnología e Innovación 0 | 2.700.000 | 5,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 257,53 M€ (257.526.731 €) · 2 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 209.575.354 | 81,4 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 47.951.377 | 18,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 64,54 M€ (64.537.608 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 47.909.060 | 74,2 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 14.116.178 | 21,9 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 2.512.370 | 3,9 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,94 M€ (1.941.250 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 1.941.250 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 74,72 M€ (74.724.169 €) · 6 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 41.091.747 | 55,0 % |
| `432G` | Promoción y Apoyo a la Comercialización | 23.710.850 | 31,7 % |
| `322A` | Formación Profesional Turística | 3.826.768 | 5,1 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.115.878 | 4,2 % |
| `432H` | Planificación Turistíca y Sistema de Información | 2.819.036 | 3,8 % |
| `432A` | Dirección Administrativa y Servicios Generales | 159.890 | 0,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,77 M€ (9.768.621 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 9.768.621 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.173,81 M€ · 86 códigos · 28,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 316.639.050 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 280.289.349 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 219.050.000 |
| `943A` | Fondo de desarrollo de Canarias | 160.000.000 |
| `112A` | Tribunales de Justicia | 150.120.043 |
| `942D` | Otras Transferencias a Corporaciones Locales | 105.768.047 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 91.208.260 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 80.725.856 |
| `231I` | Fomento de la Inclusión Social | 62.536.502 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 52.161.347 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 50.391.505 |
| `932A` | Gestion Tributaria | 46.885.185 |
| `441E` | Cohesión Interinsular | 44.660.269 |
| `441D` | Movilidad Interior | 39.100.000 |
| `425A` | Desarrollo Energético | 33.316.823 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 30.473.527 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 27.102.525 |
| `923B` | Gestión Patrimonial | 25.472.839 |
| `132A` | Seguridad y Emergencia | 24.173.749 |
| `911A` | Actuación Legislativa y de Control | 20.230.814 |
| `433C` | Promoción Económica | 19.388.335 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 15.919.626 |
| `456G` | Calidad Ambiental | 14.018.507 |
| `334A` | Promoción Cultural | 12.812.045 |
| `239A` | Dirección Administrativa y Servicios Generales | 11.107.877 |
| … | *resto: 61 códigos* | 240.259.902 |

</details>

### 2020

*Fuente: `memoria_programas.pdf` · 144 líneas · total extraído **7.698,73 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.970,65 M€ (2.970.650.193 €) · 5 códigos · 38,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 2.964.111.380 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.163.733 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 2.871.096 | 0,1 % |
| `313A` | Salud Pública | 300.000 | 0,0 % |
| `311B` | Formación Sanitaria y Social | 203.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.854,29 M€ (1.854.289.572 €) · 13 códigos · 24,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 662.110.113 | 35,7 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 629.247.865 | 33,9 % |
| `322F` | Financiación de las Universidades Canarias | 240.853.745 | 13,0 % |
| `321A` | Dirección Administrativa y Servicios Generales | 167.772.952 | 9,0 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 64.350.290 | 3,5 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 46.432.874 | 2,5 % |
| `323A` | Apoyo a los Estudios Universitarios | 15.315.513 | 0,8 % |
| `421A` | Dirección Administrativa y Servicios Generales | 6.955.913 | 0,4 % |
| `322J` | Formación Profesional Marítimo Pesquera | 5.846.506 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 5.690.592 | 0,3 % |
| `322D` | Formación Profesional Específica | 4.539.500 | 0,2 % |
| `421B` | Seguridad Industrial y Minera | 3.403.939 | 0,2 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 1.769.770 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 91,12 M€ (91.123.442 €) · 9 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 24.248.174 | 26,6 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 12.064.778 | 13,2 % |
| `411A` | Dirección Administrativa y Servicios Generales | 11.140.343 | 12,2 % |
| `415A` | Desarrollo Pesquero | 10.929.222 | 12,0 % |
| `415B` | Estructuras Pesqueras | 9.354.790 | 10,3 % |
| `412B` | Ordenación y mejora de la producción agrícola | 9.332.447 | 10,2 % |
| `412C` | Desarrollo ganadero | 6.471.397 | 7,1 % |
| `413A` | Calidad Agroalimentaria | 4.967.185 | 5,5 % |
| `415C` | Ordenación e Inspección Pesquera | 2.615.106 | 2,9 % |

</details>

<details open><summary><b><code>direccion</code> — 19,65 M€ (19.647.333 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 19.647.333 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 124,68 M€ (124.680.843 €) · 8 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 75.062.932 | 60,2 % |
| `451D` | Planificación y Programación de Infraestructuras | 19.928.483 | 16,0 % |
| `431B` | Comercio Interior | 8.000.378 | 6,4 % |
| `261E` | Ordenación del territorio | 7.347.829 | 5,9 % |
| `451A` | Dirección Administrativa y Servicios Generales | 6.322.215 | 5,1 % |
| `431A` | Promoción Exterior | 4.172.919 | 3,3 % |
| `451C` | Calidad de las Construcciones | 2.056.087 | 1,6 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 1.790.000 | 1,4 % |

</details>

<details open><summary><b><code>empleo</code> — 85,89 M€ (85.890.300 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 85.890.300 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 54,72 M€ (54.723.072 €) · 6 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 20.968.363 | 38,3 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 13.671.579 | 25,0 % |
| `463B` | Capital Humano Investigador e Innovador | 7.334.646 | 13,4 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 7.290.377 | 13,3 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 2.758.107 | 5,0 % |
| `463A` | Ciencia, Tecnología e Innovación | 2.700.000 | 4,9 % |

</details>

<details open><summary><b><code>dependencia</code> — 266,52 M€ (266.517.815 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 218.911.465 | 82,1 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 47.606.350 | 17,9 % |

</details>

<details open><summary><b><code>discapacidad</code> — 68,17 M€ (68.168.451 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 51.639.790 | 75,8 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 14.248.482 | 20,9 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 2.280.179 | 3,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,15 M€ (3.154.250 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 2.609.250 | 82,7 % |
| `232C` | Planificación y Promoción de la Diversidad 0 | 545.000 | 17,3 % |

</details>

<details open><summary><b><code>turismo</code> — 80,11 M€ (80.111.061 €) · 6 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 35.697.954 | 44,6 % |
| `432G` | Promoción y Apoyo a la Comercialización | 26.710.932 | 33,3 % |
| `432H` | Planificación Turistíca y Sistema de Información | 5.844.329 | 7,3 % |
| `322A` | Formación Profesional Turística | 5.376.768 | 6,7 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.474.528 | 4,3 % |
| `432A` | Dirección Administrativa y Servicios Generales | 3.006.550 | 3,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,78 M€ (10.777.717 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 10.777.717 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.069,00 M€ · 87 códigos · 26,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 307.650.992 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 278.293.055 |
| `112A` | Tribunales de Justicia | 155.832.337 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 147.050.001 |
| `231I` | Fomento de la Inclusión Social | 88.684.502 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 86.958.260 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 83.644.033 |
| `943A` | Fondo de desarrollo de Canarias | 80.000.000 |
| `942D` | Otras Transferencias a Corporaciones Locales | 64.816.939 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 58.354.780 |
| `932A` | Gestion Tributaria | 50.924.660 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 50.430.706 |
| `441E` | Cohesión Interinsular | 46.160.269 |
| `441D` | Movilidad Interior | 39.700.000 |
| `425A` | Desarrollo Energético | 36.600.918 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 33.770.835 |
| `923B` | Gestión Patrimonial | 32.092.416 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 26.110.437 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 24.875.380 |
| `132A` | Seguridad y Emergencia | 24.334.744 |
| `433C` | Promoción Económica | 20.758.895 |
| `911A` | Actuación Legislativa y de Control | 19.777.966 |
| `239A` | Dirección Administrativa y Servicios Generales | 17.075.843 |
| `334A` | Promoción Cultural | 15.649.593 |
| `456G` | Calidad Ambiental | 12.938.934 |
| … | *resto: 62 códigos* | 266.511.310 |

</details>

### 2021

*Fuente: `memoria_programas.pdf` · 141 líneas · total extraído **8.044,74 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.088,47 M€ (3.088.468.435 €) · 5 códigos · 38,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 3.081.520.521 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.300.660 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 3.068.270 | 0,1 % |
| `313A` | Salud Pública | 300.000 | 0,0 % |
| `311B` | Formación Sanitaria y Social | 278.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.951,01 M€ (1.951.014.528 €) · 13 códigos · 24,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 729.909.972 | 37,4 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 637.675.435 | 32,7 % |
| `322F` | Financiación de las Universidades Canarias | 239.901.791 | 12,3 % |
| `321A` | Dirección Administrativa y Servicios Generales | 183.002.442 | 9,4 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 69.005.391 | 3,5 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 50.368.302 | 2,6 % |
| `323A` | Apoyo a los Estudios Universitarios | 13.385.777 | 0,7 % |
| `322J` | Formación Profesional Marítimo Pesquera | 5.807.563 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 5.792.346 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 5.632.189 | 0,3 % |
| `322D` | Formación Profesional Específica | 4.739.500 | 0,2 % |
| `421B` | Seguridad Industrial y Minera | 3.267.049 | 0,2 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 2.526.771 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 97,22 M€ (97.222.642 €) · 9 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 28.958.593 | 29,8 % |
| `415A` | Desarrollo Pesquero | 11.822.122 | 12,2 % |
| `411A` | Dirección Administrativa y Servicios Generales | 11.584.634 | 11,9 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 11.147.269 | 11,5 % |
| `412B` | Ordenación y mejora de la producción agrícola | 8.686.445 | 8,9 % |
| `415B` | Estructuras Pesqueras | 8.524.040 | 8,8 % |
| `412C` | Desarrollo ganadero | 8.125.328 | 8,4 % |
| `413A` | Calidad Agroalimentaria | 5.647.071 | 5,8 % |
| `415C` | Ordenación e Inspección Pesquera | 2.727.140 | 2,8 % |

</details>

<details open><summary><b><code>direccion</code> — 21,54 M€ (21.541.690 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 21.541.690 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 151,41 M€ (151.405.173 €) · 8 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 101.246.823 | 66,9 % |
| `431B` | Comercio Interior | 15.087.097 | 10,0 % |
| `451D` | Planificación y Programación de Infraestructuras | 13.319.904 | 8,8 % |
| `261E` | Ordenación del territorio | 7.962.179 | 5,3 % |
| `451A` | Dirección Administrativa y Servicios Generales | 5.839.811 | 3,9 % |
| `431A` | Promoción Exterior | 3.543.576 | 2,3 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 2.315.000 | 1,5 % |
| `451C` | Calidad de las Construcciones | 2.090.783 | 1,4 % |

</details>

<details open><summary><b><code>empleo</code> — 85,84 M€ (85.836.504 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 85.836.504 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 47,28 M€ (47.283.119 €) · 5 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `463C` | Apoyo a la Investigación Básica y Aplicada | 13.614.516 | 28,8 % |
| `467B` | Apoyo a la Innovación Empresarial | 12.970.892 | 27,4 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 8.653.508 | 18,3 % |
| `463B` | Capital Humano Investigador e Innovador | 7.394.203 | 15,6 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 4.650.000 | 9,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 278,84 M€ (278.835.673 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 220.830.538 | 79,2 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 58.005.135 | 20,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 74,28 M€ (74.284.157 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 57.309.854 | 77,1 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 14.861.942 | 20,0 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 2.112.361 | 2,8 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,25 M€ (4.251.626 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 3.327.650 | 78,3 % |
| `232C` | Planificación y Promoción de la Diversidad | 923.976 | 21,7 % |

</details>

<details open><summary><b><code>turismo</code> — 95,38 M€ (95.382.995 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 36.292.201 | 38,0 % |
| `432G` | Promoción y Apoyo a la Comercialización | 33.131.110 | 34,7 % |
| `432H` | Planificación Turistíca y Sistema de Información | 13.783.469 | 14,5 % |
| `322A` | Formación Profesional Turística | 5.376.768 | 5,6 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.767.742 | 4,0 % |
| `432A` | Dirección Administrativa y Servicios Generales | 3.031.705 | 3,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,87 M€ (11.873.307 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 11.873.307 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.137,34 M€ · 85 códigos · 26,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942A` | Transferencias a Cabildos traspaso de competencias | 290.128.002 |
| `942C` | Fondo Canario de Financiación Municipal | 286.834.890 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 225.199.103 |
| `112A` | Tribunales de Justicia | 158.131.439 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 82.221.244 |
| `943A` | Fondo de desarrollo de Canarias | 80.000.000 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 72.151.989 |
| `942D` | Otras Transferencias a Corporaciones Locales | 64.594.650 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 54.925.391 |
| `932A` | Gestion Tributaria | 54.671.913 |
| `231I` | Fomento de la Inclusión Social | 53.851.502 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 46.348.033 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 46.285.842 |
| `441E` | Cohesión Interinsular | 44.410.269 |
| `425A` | Desarrollo Energético | 42.420.093 |
| `441D` | Movilidad Interior | 38.500.000 |
| `923B` | Gestión Patrimonial | 33.327.341 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 31.303.475 |
| `433C` | Promoción Económica | 30.633.435 |
| `132A` | Seguridad y Emergencia | 27.639.089 |
| `911A` | Actuación Legislativa y de Control | 22.539.357 |
| `334A` | Promoción Cultural | 18.207.552 |
| `239A` | Dirección Administrativa y Servicios Generales | 16.799.613 |
| `452B` | Mejora de la Calidad del Agua | 13.156.421 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 12.378.276 |
| … | *resto: 60 códigos* | 290.682.427 |

</details>

### 2022

*Fuente: `memoria_programas.pdf` · 135 líneas · total extraído **8.608,86 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.225,42 M€ (3.225.421.670 €) · 4 códigos · 37,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 3.218.736.030 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.229.861 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 3.086.795 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 368.984 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.099,97 M€ (2.099.974.847 €) · 13 códigos · 24,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 770.158.052 | 36,7 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 716.451.506 | 34,1 % |
| `322F` | Financiación de las Universidades Canarias | 244.376.343 | 11,6 % |
| `321A` | Dirección Administrativa y Servicios Generales | 203.427.698 | 9,7 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 64.105.391 | 3,1 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 49.419.752 | 2,4 % |
| `322D` | Formación Profesional Específica | 15.674.500 | 0,7 % |
| `323A` | Apoyo a los Estudios Universitarios | 13.696.068 | 0,7 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 6.667.717 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 5.980.885 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 5.610.216 | 0,3 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 2.316.670 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 2.090.049 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 122,37 M€ (122.367.315 €) · 9 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `415B` | Estructuras Pesqueras | 31.946.889 | 26,1 % |
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 31.196.676 | 25,5 % |
| `415A` | Desarrollo Pesquero | 12.274.936 | 10,0 % |
| `411A` | Dirección Administrativa y Servicios Generales | 10.712.740 | 8,8 % |
| `412B` | Ordenación y mejora de la producción agrícola | 9.086.649 | 7,4 % |
| `412C` | Desarrollo ganadero | 9.067.721 | 7,4 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 8.447.967 | 6,9 % |
| `413A` | Calidad Agroalimentaria | 7.031.286 | 5,7 % |
| `415C` | Ordenación e Inspección Pesquera | 2.602.451 | 2,1 % |

</details>

<details open><summary><b><code>direccion</code> — 25,17 M€ (25.173.153 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 25.173.153 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 164,00 M€ (163.995.638 €) · 8 códigos · 1,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 115.354.473 | 70,3 % |
| `431B` | Comercio Interior | 14.946.812 | 9,1 % |
| `451D` | Planificación y Programación de Infraestructuras | 8.650.127 | 5,3 % |
| `261E` | Ordenación del territorio | 8.599.591 | 5,2 % |
| `451A` | Dirección Administrativa y Servicios Generales | 5.693.158 | 3,5 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 4.926.064 | 3,0 % |
| `431A` | Promoción Exterior | 3.189.206 | 1,9 % |
| `451C` | Calidad de las Construcciones | 2.636.207 | 1,6 % |

</details>

<details open><summary><b><code>empleo</code> — 91,34 M€ (91.338.493 €) · 1 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 91.338.493 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 58,64 M€ (58.640.520 €) · 5 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `463C` | Apoyo a la Investigación Básica y Aplicada | 16.065.772 | 27,4 % |
| `467B` | Apoyo a la Innovación Empresarial | 15.622.434 | 26,6 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 9.565.060 | 16,3 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 8.835.210 | 15,1 % |
| `463B` | Capital Humano Investigador e Innovador | 8.552.044 | 14,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 300,56 M€ (300.562.419 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 238.918.494 | 79,5 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 61.643.925 | 20,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 82,19 M€ (82.192.719 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 62.857.234 | 76,5 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 15.890.656 | 19,3 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 3.444.829 | 4,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,69 M€ (4.687.276 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 3.752.300 | 80,1 % |
| `232C` | Planificación y Promoción de la Diversidad | 934.976 | 19,9 % |

</details>

<details open><summary><b><code>turismo</code> — 104,77 M€ (104.769.217 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 32.162.592 | 30,7 % |
| `432G` | Promoción y Apoyo a la Comercialización | 31.897.570 | 30,4 % |
| `432H` | Planificación Turistíca y Sistema de Información | 25.737.670 | 24,6 % |
| `322A` | Formación Profesional Turística | 8.184.747 | 7,8 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.481.975 | 3,3 % |
| `432A` | Dirección Administrativa y Servicios Generales | 3.304.663 | 3,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 12,66 M€ (12.663.329 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 12.663.329 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.317,08 M€ · 80 códigos · 26,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942A` | Transferencias a Cabildos traspaso de competencias | 306.555.411 |
| `942C` | Fondo Canario de Financiación Municipal | 292.319.482 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 229.563.952 |
| `112A` | Tribunales de Justicia | 162.788.795 |
| `441D` | Movilidad Interior | 84.430.090 |
| `943A` | Fondo de desarrollo de Canarias | 80.000.000 |
| `231I` | Fomento de la Inclusión Social | 78.092.720 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 75.178.164 |
| `425A` | Desarrollo Energético | 65.547.832 |
| `942D` | Otras Transferencias a Corporaciones Locales | 64.760.704 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 63.672.424 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 60.826.390 |
| `932A` | Gestion Tributaria | 60.192.717 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 58.607.440 |
| `441E` | Cohesión Interinsular | 42.410.269 |
| `433C` | Promoción Económica | 38.302.722 |
| `923B` | Gestión Patrimonial y contratación pública | 36.882.842 |
| `912L` | Palamento y Entes de relevancia Estatutaria | 35.781.719 |
| `132A` | Seguridad y Emergencia | 34.315.967 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 32.898.494 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 22.896.845 |
| `452B` | Mejora de la Calidad del Agua | 22.599.812 |
| `334A` | Promoción Cultural | 21.294.827 |
| `456D` | Coordinación y Planificación Medioambiental | 20.588.834 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 15.380.226 |
| … | *resto: 55 códigos* | 311.188.190 |

</details>

### 2023

*Fuente: `memoria_programas.pdf` · 135 líneas · total extraído **9.701,03 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.575,65 M€ (3.575.652.999 €) · 4 códigos · 36,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 3.568.343.068 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 3.628.642 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 3.316.805 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 364.484 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.275,41 M€ (2.275.406.200 €) · 13 códigos · 23,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 853.993.843 | 37,5 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 745.092.604 | 32,7 % |
| `322F` | Financiación de las Universidades Canarias | 257.686.823 | 11,3 % |
| `321A` | Dirección Administrativa y Servicios Generales | 222.900.251 | 9,8 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 74.171.345 | 3,3 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 60.194.963 | 2,6 % |
| `322D` | Formación Profesional Específica | 25.280.979 | 1,1 % |
| `323A` | Apoyo a los Estudios Universitarios | 13.603.502 | 0,6 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 7.121.910 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 6.451.184 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 5.794.502 | 0,3 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 2.573.245 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 541.049 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 142,86 M€ (142.858.532 €) · 9 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 36.837.302 | 25,8 % |
| `415B` | Estructuras Pesqueras | 33.403.419 | 23,4 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 20.957.464 | 14,7 % |
| `415A` | Desarrollo Pesquero | 12.130.192 | 8,5 % |
| `411A` | Dirección Administrativa y Servicios Generales | 11.308.967 | 7,9 % |
| `412B` | Ordenación y mejora de la producción agrícola | 9.124.751 | 6,4 % |
| `412C` | Desarrollo ganadero | 9.077.066 | 6,4 % |
| `413A` | Calidad Agroalimentaria | 7.385.113 | 5,2 % |
| `415C` | Ordenación e Inspección Pesquera | 2.634.258 | 1,8 % |

</details>

<details open><summary><b><code>direccion</code> — 24,58 M€ (24.576.670 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 24.576.670 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 200,81 M€ (200.807.166 €) · 8 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 131.639.158 | 65,6 % |
| `451D` | Planificación y Programación de Infraestructuras | 27.443.589 | 13,7 % |
| `431B` | Comercio Interior | 19.375.533 | 9,6 % |
| `261E` | Ordenación del territorio | 9.203.516 | 4,6 % |
| `451A` | Dirección Administrativa y Servicios Generales | 6.142.276 | 3,1 % |
| `431A` | Promoción Exterior | 3.209.206 | 1,6 % |
| `451C` | Calidad de las Construcciones | 2.553.888 | 1,3 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 1.240.000 | 0,6 % |

</details>

<details open><summary><b><code>empleo</code> — 113,62 M€ (113.622.080 €) · 1 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 113.622.080 | 100,0 % |

</details>

<details open><summary><b><code>idi</code> — 76,00 M€ (75.998.230 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B` | Apoyo a la Innovación Empresarial | 20.236.237 | 26,6 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 19.979.880 | 26,3 % |
| `463B` | Capital Humano Investigador e Innovador | 13.510.677 | 17,8 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 12.091.834 | 15,9 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 10.179.602 | 13,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 348,66 M€ (348.663.128 €) · 2 códigos · 3,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 265.498.955 | 76,1 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 83.164.173 | 23,9 % |

</details>

<details open><summary><b><code>discapacidad</code> — 82,13 M€ (82.125.662 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 63.865.248 | 77,8 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 16.423.026 | 20,0 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 1.837.388 | 2,2 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,89 M€ (5.887.276 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 4.952.300 | 84,1 % |
| `232C` | Planificación y Promoción de la Diversidad | 934.976 | 15,9 % |

</details>

<details open><summary><b><code>turismo</code> — 127,70 M€ (127.704.086 €) · 6 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432H` | Planificación Turistíca y Sistema de Información | 45.338.389 | 35,5 % |
| `432G` | Promoción y Apoyo a la Comercialización | 41.096.199 | 32,2 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 24.408.389 | 19,1 % |
| `432A` | Dirección Administrativa y Servicios Generales | 6.902.677 | 5,4 % |
| `322A` | Formación Profesional Turística | 6.384.747 | 5,0 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.573.685 | 2,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 12,84 M€ (12.837.703 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 12.837.703 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.714,89 M€ · 80 códigos · 28,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942A` | Transferencias a Cabildos traspaso de competencias | 364.553.288 |
| `942C` | Fondo Canario de Financiación Municipal | 358.805.079 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 229.563.952 |
| `112A` | Tribunales de Justicia | 172.766.022 |
| `943A` | Fondo de desarrollo de Canarias | 162.311.000 |
| `231I` | Fomento de la Inclusión Social | 95.014.838 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 89.101.858 |
| `425A` | Desarrollo Energético | 79.704.991 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 77.211.258 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 72.696.834 |
| `942D` | Otras Transferencias a Corporaciones Locales | 65.893.266 |
| `932A` | Gestion Tributaria | 64.278.350 |
| `441D` | Movilidad Interior | 62.070.000 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 60.864.493 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 48.332.576 |
| `441E` | Cohesión Interinsular | 42.660.269 |
| `132A` | Seguridad y Emergencia | 42.560.273 |
| `923B` | Gestión Patrimonial y contratación pública | 41.656.156 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 40.654.899 |
| `912L` | Palamento y Entes de relevancia Estatutaria | 36.779.973 |
| `453A` | Desarrollo de Infraestructura de Carreteras | 32.453.914 |
| `433C` | Promoción Económica | 29.273.485 |
| `334A` | Promoción Cultural | 26.093.147 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 19.633.451 |
| `456E` | Biodiversidad | 19.542.792 |
| … | *resto: 55 códigos* | 380.411.815 |

</details>

### 2024

*Fuente: `memoria_programas.pdf` · 140 líneas · total extraído **10.745,72 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.108,18 M€ (4.108.181.841 €) · 4 códigos · 38,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 4.100.463.381 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 4.079.072 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 3.287.904 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 351.484 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.368,75 M€ (2.368.752.325 €) · 13 códigos · 22,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 886.909.657 | 37,4 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 783.877.967 | 33,1 % |
| `322F` | Financiación de las Universidades Canarias | 264.695.660 | 11,2 % |
| `321A` | Dirección Administrativa y Servicios Generales | 235.371.272 | 9,9 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 87.020.767 | 3,7 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 60.164.684 | 2,5 % |
| `323A` | Apoyo a los Estudios Universitarios | 13.745.599 | 0,6 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 9.502.578 | 0,4 % |
| `322D` | Formación Profesional Específica | 9.373.333 | 0,4 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 7.046.329 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 6.032.702 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 4.508.728 | 0,2 % |
| `421B` | Seguridad Industrial y Minera | 503.049 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 118,71 M€ (118.713.832 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 32.682.144 | 27,5 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 22.109.806 | 18,6 % |
| `411A` | Dirección Administrativa y Servicios Generales | 12.215.553 | 10,3 % |
| `415A` | Desarrollo Pesquero | 11.989.209 | 10,1 % |
| `415B` | Estructuras Pesqueras | 10.418.659 | 8,8 % |
| `412B` | Ordenación y mejora de la producción agrícola | 10.093.076 | 8,5 % |
| `412C` | Desarrollo ganadero | 8.963.419 | 7,6 % |
| `413A` | Calidad Agroalimentaria | 7.617.612 | 6,4 % |
| `415C` | Ordenación e Inspección Pesquera | 2.624.354 | 2,2 % |

</details>

<details open><summary><b><code>direccion</code> — 30,93 M€ (30.926.843 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 30.926.843 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 166,17 M€ (166.171.055 €) · 8 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 114.150.493 | 68,7 % |
| `431B` | Comercio Interior | 15.622.275 | 9,4 % |
| `451D` | Planificación y Programación de Infraestructuras | 10.707.590 | 6,4 % |
| `261E` | Ordenación del territorio | 8.558.949 | 5,2 % |
| `451A` | Dirección Administrativa y Servicios Generales | 7.782.799 | 4,7 % |
| `431A` | Promoción Exterior | 3.999.206 | 2,4 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 2.708.603 | 1,6 % |
| `451C` | Calidad de las Construcciones | 2.641.140 | 1,6 % |

</details>

<details open><summary><b><code>empleo</code> — 93,12 M€ (93.117.329 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 90.305.410 | 97,0 % |
| `241K` | Refuerzo de la Capacidad Empresarial 0 | 2.710.000 | 2,9 % |
| `241E` | Dirección y Gestión Administrativa del SCE 0 | 101.919 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 95,07 M€ (95.074.319 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 46.787.786 | 49,2 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 13.822.255 | 14,5 % |
| `463B` | Capital Humano Investigador e Innovador | 12.290.376 | 12,9 % |
| `467B` | Apoyo a la Innovación Empresarial | 12.135.780 | 12,8 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 10.038.122 | 10,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 379,25 M€ (379.252.645 €) · 2 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 305.199.316 | 80,5 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 74.053.329 | 19,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 81,49 M€ (81.486.916 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 62.294.180 | 76,4 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 17.215.973 | 21,1 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 1.976.763 | 2,4 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,55 M€ (4.554.614 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 3.619.638 | 79,5 % |
| `232C` | Planificación y Promoción de la Diversidad | 934.976 | 20,5 % |

</details>

<details open><summary><b><code>turismo</code> — 131,14 M€ (131.144.302 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432H` | Planificación Turistíca y Sistema de Información | 51.823.154 | 39,5 % |
| `432G` | Promoción y Apoyo a la Comercialización | 39.872.333 | 30,4 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 23.126.831 | 17,6 % |
| `322A` | Formación Profesional Turística | 6.384.747 | 4,9 % |
| `432A` | Dirección Administrativa y Servicios Generales | 6.301.003 | 4,8 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.636.234 | 2,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 13,41 M€ (13.414.120 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 13.414.120 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.154,93 M€ · 83 códigos · 29,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942A` | Transferencias a Cabildos traspaso de competencias | 395.831.883 |
| `942C` | Fondo Canario de Financiación Municipal | 393.024.983 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 354.958.595 |
| `112A` | Tribunales de Justicia | 182.200.137 |
| `943A` | Fondo de desarrollo de Canarias | 162.600.000 |
| `425A` | Desarrollo Energético | 134.785.486 |
| `231I` | Fomento de la Inclusión Social | 102.220.409 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 96.903.597 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 94.392.203 |
| `923B` | Gestión Patrimonial y contratación pública | 84.906.418 |
| `441D` | Movilidad Interior | 73.617.823 |
| `932A` | Gestion Tributaria | 72.669.844 |
| `942D` | Otras Transferencias a Corporaciones Locales | 66.565.040 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 63.683.658 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 60.891.427 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 56.839.215 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 56.361.103 |
| `929B` | Reconstrucción y recuperac econ-social de La Palma 0 | 52.215.067 |
| `452B` | Mejora de la Calidad del Agua | 43.287.999 |
| `441E` | Cohesión Interinsular | 42.660.269 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 41.945.256 |
| `912L` | Palamento y Entes de relevancia Estatutaria | 38.446.381 |
| `132A` | Seguridad y Emergencia | 37.461.977 |
| `433C` | Promoción Económica | 30.086.580 |
| `334A` | Promoción Cultural | 24.937.723 |
| … | *resto: 58 códigos* | 391.432.098 |

</details>

### 2025

*Fuente: `memoria_programas.pdf` · 141 líneas · total extraído **11.108,73 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.308,66 M€ (4.308.657.056 €) · 4 códigos · 38,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 4.300.755.755 | 99,8 % |
| `311A` | Dirección Administrativa y Servicios Generales | 4.253.302 | 0,1 % |
| `312B` | Hemodonación y Hemoterapia | 3.296.515 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 351.484 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.438,48 M€ (2.438.484.346 €) · 14 códigos · 22,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 923.636.275 | 37,9 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 810.352.536 | 33,2 % |
| `322F` | Financiación de las Universidades Canarias | 274.138.426 | 11,2 % |
| `321A` | Dirección Administrativa y Servicios Generales | 229.348.249 | 9,4 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 86.836.094 | 3,6 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 59.482.948 | 2,4 % |
| `322D` | Formación Profesional Específica | 15.592.147 | 0,6 % |
| `323A` | Apoyo a los Estudios Universitarios | 12.316.742 | 0,5 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 7.002.578 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 6.942.307 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 6.259.208 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 4.541.243 | 0,2 % |
| `321C` | Calidad y Evaluac del Sistema Educativo Canario | 1.432.544 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 603.049 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 119,25 M€ (119.247.851 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 32.414.383 | 27,2 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 17.853.365 | 15,0 % |
| `415B` | Estructuras Pesqueras | 14.708.491 | 12,3 % |
| `411A` | Dirección Administrativa y Servicios Generales | 12.721.426 | 10,7 % |
| `415A` | Desarrollo Pesquero | 11.889.053 | 10,0 % |
| `412B` | Ordenación y mejora de la producción agrícola | 10.720.040 | 9,0 % |
| `412C` | Desarrollo ganadero | 8.669.007 | 7,3 % |
| `413A` | Calidad Agroalimentaria | 7.564.964 | 6,3 % |
| `415C` | Ordenación e Inspección Pesquera | 2.707.122 | 2,3 % |

</details>

<details open><summary><b><code>direccion</code> — 32,40 M€ (32.402.518 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 32.402.518 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 187,33 M€ (187.328.703 €) · 9 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 139.898.285 | 74,7 % |
| `431B` | Comercio Interior | 14.929.925 | 8,0 % |
| `261E` | Ordenación del territorio | 8.344.969 | 4,5 % |
| `451A` | Dirección Administrativa y Servicios Generales | 7.382.200 | 3,9 % |
| `451D` | Planificación y Programación de Infraestructuras | 5.598.713 | 3,0 % |
| `431A` | Promoción Exterior | 4.184.206 | 2,2 % |
| `451C` | Calidad de las Construcciones | 4.032.859 | 2,2 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 1.957.546 | 1,0 % |
| `261B` | Promoción y Rehabilit. Parque Públ. de Viviendas 0 | 1.000.000 | 0,5 % |

</details>

<details open><summary><b><code>empleo</code> — 97,66 M€ (97.655.020 €) · 3 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 94.953.373 | 97,2 % |
| `241K` | Refuerzo de la Capacidad Empresarial | 2.590.000 | 2,7 % |
| `241E` | Dirección y Gestión Administrativa del SCE | 111.647 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 88,66 M€ (88.664.354 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 36.304.249 | 40,9 % |
| `463C` | Apoyo a la Investigación Básica y Aplicada | 16.035.422 | 18,1 % |
| `463B` | Capital Humano Investigador e Innovador | 13.618.864 | 15,4 % |
| `467B` | Apoyo a la Innovación Empresarial | 12.717.044 | 14,3 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 9.988.775 | 11,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 415,94 M€ (415.940.040 €) · 2 códigos · 3,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 350.955.290 | 84,4 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 64.984.750 | 15,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 83,04 M€ (83.043.244 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 64.159.598 | 77,3 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 18.120.606 | 21,8 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 763.040 | 0,9 % |

</details>

<details open><summary><b><code>diversidad</code> — 4,83 M€ (4.828.638 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 4.127.638 | 85,5 % |
| `232C` | Planificación y Promoción de la Diversidad | 701.000 | 14,5 % |

</details>

<details open><summary><b><code>turismo</code> — 134,49 M€ (134.487.265 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432H` | Planificación Turistíca y Sistema de Información | 48.514.441 | 36,1 % |
| `432G` | Promoción y Apoyo a la Comercialización | 44.205.831 | 32,9 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 25.504.862 | 19,0 % |
| `322A` | Formación Profesional Turística | 6.384.747 | 4,7 % |
| `432A` | Dirección Administrativa y Servicios Generales | 5.967.577 | 4,4 % |
| `432F` | Productos Turísticos y Calidad Turística | 3.909.807 | 2,9 % |

</details>

<details open><summary><b><code>igualdad</code> — 13,63 M€ (13.631.088 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 13.631.088 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.184,36 M€ · 82 códigos · 28,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 424.896.323 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 419.209.026 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 282.509.298 |
| `112A` | Tribunales de Justicia | 193.288.385 |
| `425A` | Desarrollo Energético | 176.793.201 |
| `943A` | Fondo de desarrollo de Canarias | 125.122.280 |
| `231I` | Fomento de la Inclusión Social | 121.961.335 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 105.298.934 |
| `923B` | Gestión Patrimonial y contratación pública | 92.634.787 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 88.329.454 |
| `932A` | Gestion Tributaria | 72.033.167 |
| `231B` | Coordinac y Planific de Polít Soc y atenc pers may | 67.881.787 |
| `942D` | Otras Transferencias a Corporaciones Locales | 67.084.173 |
| `441D` | Movilidad Interior | 63.221.309 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 60.900.422 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 59.489.215 |
| `929B` | Reconstrucción y recuperac econ-social de La Palma | 52.391.484 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 40.614.467 |
| `912L` | Palamento y Entes de relevancia Estatutaria | 39.918.956 |
| `441E` | Cohesión Interinsular | 38.960.269 |
| `452B` | Mejora de la Calidad del Agua | 35.843.517 |
| `456D` | Coordinación y Planificación Medioambiental | 35.733.776 |
| `433C` | Promoción Económica | 32.481.386 |
| `132A` | Seguridad y Emergencia | 30.956.661 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 26.085.370 |
| … | *resto: 57 códigos* | 430.717.371 |

</details>

### 2026

*Fuente: `memoria_programas.pdf` · 143 líneas · total extraído **11.910,12 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.542,05 M€ (4.542.045.217 €) · 3 códigos · 38,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | Asistencia Sanitaria | 4.536.754.790 | 99,9 % |
| `311A` | Dirección Administrativa y Servicios Generales | 4.814.223 | 0,1 % |
| `311B` | Formación Sanitaria y Social | 476.204 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.606,33 M€ (2.606.326.700 €) · 14 códigos · 21,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322C` | Enseñanza Secundaria y Formación Profesional | 990.687.589 | 38,0 % |
| `322B` | Educación Infantil, Primaria y 1ª Ciclo de E.S.O | 860.633.561 | 33,0 % |
| `322F` | Financiación de las Universidades Canarias | 281.903.688 | 10,8 % |
| `321A` | Dirección Administrativa y Servicios Generales | 266.198.375 | 10,2 % |
| `324C` | Servicios Complem. a la Enseñanza no Universitaria | 102.180.749 | 3,9 % |
| `322K` | Enseñanzas Régimen Especial y Educación de Adultos | 59.255.067 | 2,3 % |
| `323A` | Apoyo a los Estudios Universitarios | 12.877.071 | 0,5 % |
| `322D` | Formación Profesional Específica | 8.610.897 | 0,3 % |
| `322H` | Mejora de la Capacitación Agraria y Form. Profes | 7.202.809 | 0,3 % |
| `322J` | Formación Profesional Marítimo Pesquera | 6.765.404 | 0,3 % |
| `421A` | Dirección Administrativa y Servicios Generales | 4.752.347 | 0,2 % |
| `321B` | Form. Permanente del Profesorado e Innov. Educat | 3.202.150 | 0,1 % |
| `321C` | Calidad y Evaluac del Sistema Educativo Canario | 1.453.944 | 0,1 % |
| `421B` | Seguridad Industrial y Minera | 603.049 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 130,68 M€ (130.679.861 €) · 9 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412A` | Mejora de Estructuras Agrarias y del Medio Rural | 34.861.085 | 26,7 % |
| `415A` | Desarrollo Pesquero | 20.254.273 | 15,5 % |
| `411B` | Gestión ayudas FEAGA/FEADER | 18.480.987 | 14,1 % |
| `411A` | Dirección Administrativa y Servicios Generales | 14.201.872 | 10,9 % |
| `415B` | Estructuras Pesqueras | 12.535.744 | 9,6 % |
| `412B` | Ordenación y mejora de la producción agrícola | 10.718.021 | 8,2 % |
| `412C` | Desarrollo ganadero | 9.514.381 | 7,3 % |
| `413A` | Calidad Agroalimentaria | 7.588.858 | 5,8 % |
| `415C` | Ordenación e Inspección Pesquera | 2.524.640 | 1,9 % |

</details>

<details open><summary><b><code>direccion</code> — 33,60 M€ (33.601.026 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A` | Dirección Política y Gobierno | 33.601.026 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 211,83 M€ (211.833.521 €) · 9 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | Dirección, Promoción y Gestión en mat. de Vivienda | 161.955.034 | 76,5 % |
| `431B` | Comercio Interior | 16.109.181 | 7,6 % |
| `261E` | Ordenación del territorio | 8.278.052 | 3,9 % |
| `451A` | Dirección Administrativa y Servicios Generales | 8.257.993 | 3,9 % |
| `451D` | Planificación y Programación de Infraestructuras | 6.608.297 | 3,1 % |
| `431A` | Promoción Exterior | 4.747.087 | 2,2 % |
| `451C` | Calidad de las Construcciones | 3.585.877 | 1,7 % |
| `451E` | Ordenación y Apoyo Plan Estratég. Ttes de Canarios | 1.292.000 | 0,6 % |
| `261B` | Promoción y Rehabilit. Parque Públ. de Viviendas | 1.000.000 | 0,5 % |

</details>

<details open><summary><b><code>empleo</code> — 96,61 M€ (96.610.923 €) · 3 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241C` | Fomento del Empleo | 92.350.760 | 95,6 % |
| `241K` | Refuerzo de la Capacidad Empresarial | 4.195.000 | 4,3 % |
| `241E` | Dirección y Gestión Administrativa del SCE | 65.163 | 0,1 % |

</details>

<details open><summary><b><code>idi</code> — 79,70 M€ (79.698.924 €) · 5 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `463C` | Apoyo a la Investigación Básica y Aplicada | 27.173.117 | 34,1 % |
| `463B` | Capital Humano Investigador e Innovador | 16.100.602 | 20,2 % |
| `467B` | Apoyo a la Innovación Empresarial | 14.655.825 | 18,4 % |
| `467C` | Apoyo al Despliegue de Sociedad de la Información | 12.011.203 | 15,1 % |
| `467A` | Investigación y Desarrollo Tecnológico Agrario | 9.758.177 | 12,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 478,36 M€ (478.357.792 €) · 3 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231M` | Atención a Personas en situación de Dependencia | 396.004.122 | 82,8 % |
| `231H` | Prevenc. e Interv. en área del Menor y la Familia | 66.186.074 | 13,8 % |
| `231D` | Atención a personas mayores 0 | 16.167.596 | 3,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 86,69 M€ (86.685.508 €) · 3 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231N` | Atención a Personas con Discapacidad | 67.741.406 | 78,1 % |
| `231C` | Planificación y Apoyo a los Servicios Sociales | 18.401.602 | 21,2 % |
| `231G` | Prestaciones y otras Ayudas Sociales | 542.500 | 0,6 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,91 M€ (6.911.270 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231P` | Acciones a favor de los canarios en el exterior | 6.210.270 | 89,9 % |
| `232C` | Planificación y Promoción de la Diversidad | 701.000 | 10,1 % |

</details>

<details open><summary><b><code>turismo</code> — 154,80 M€ (154.797.203 €) · 7 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432H` | Planificación Turistíca y Sistema de Información | 63.073.132 | 40,7 % |
| `432G` | Promoción y Apoyo a la Comercialización | 50.650.222 | 32,7 % |
| `432B` | Infraestr. Turíst. y Gest. Integral Núcleos Turíst | 22.146.080 | 14,3 % |
| `322A` | Formación Profesional Turística | 8.399.747 | 5,4 % |
| `432A` | Dirección Administrativa y Servicios Generales | 6.258.318 | 4,0 % |
| `432F` | Productos Turísticos y Calidad Turística | 4.194.704 | 2,7 % |
| `432C` | Plan Sect. de Infraestr. y Calidad Turíst. de Can. 0 | 75.000 | 0,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,67 M€ (14.672.962 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | Promoción Igualdad de Oportunidades para Mujeres | 14.672.962 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.467,90 M€ · 83 códigos · 29,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `942C` | Fondo Canario de Financiación Municipal | 465.289.201 |
| `942A` | Transferencias a Cabildos traspaso de competencias | 451.958.006 |
| `425A` | Desarrollo Energético | 285.827.844 |
| `453D` | Convenio de Carreteras con Ministerio de Fomento | 214.920.000 |
| `112A` | Tribunales de Justicia | 203.277.271 |
| `943A` | Fondo de desarrollo de Canarias | 163.356.772 |
| `231I` | Fomento de la Inclusión Social | 130.289.458 |
| `951M` | Amortiz y gtos fros deuda pública moneda nacional | 104.556.413 |
| `923B` | Gestión Patrimonial y contratación pública | 101.662.084 |
| `491A` | Infraestruct. y Serv. de Comunicac. e Informática | 99.867.877 |
| `932A` | Gestion Tributaria | 83.057.336 |
| `441D` | Movilidad Interior | 75.017.623 |
| `929A` | Gastos imprevistos y funciones no clasificadas | 69.784.288 |
| `942D` | Otras Transferencias a Corporaciones Locales | 67.791.339 |
| `456J` | Desarrollo Sostenible y Cambio Climático | 65.752.464 |
| `921J` | Medios de Comunic. Social y Relaciones Informativ | 60.906.807 |
| `231B` | Coordinación y Planificación de Políticas Sociales | 53.915.251 |
| `929B` | Reconstrucción y recuperac econ-social de La Palma | 53.302.130 |
| `912L` | Palamento y Entes de relevancia Estatutaria | 41.103.378 |
| `231K` | Ejecución Medidas Judiciales Menores Infractores | 40.290.100 |
| `452B` | Mejora de la Calidad del Agua | 36.590.941 |
| `132A` | Seguridad y Emergencia | 35.514.095 |
| `433C` | Promoción Económica | 35.381.863 |
| `441E` | Cohesión Interinsular | 33.622.160 |
| `132B` | Seguridad ciudadana | 26.171.191 |
| … | *resto: 58 códigos* | 468.696.265 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py can     # regenera este documento
python3 tools/auditoria_magnitud.py can        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa can --anio <año> \
    --input ../fuentes/raw/can/<año>/<fichero> --output /tmp/can.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-can.md`](limitaciones-can.md)

