# Trazabilidad de la extracción — Cantabria (`cnt`)

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
| **2015** | 83 | `desarrollo_centros.pdf` | 12 | 48,2 % | 2.514,33 | — | no_aplica |
| **2016** | 84 | `desarrollo_centros.pdf` | 12 | 48,8 % | 2.479,37 | — | no_aplica |
| **2017** | 84 | `desarrollo_centros.pdf` | 12 | 48,8 % | 2.617,26 | — | no_aplica |
| **2018** | 84 | `ingresos_gastos.pdf` | 11 | 47,6 % | 2.741,70 | — | no_aplica |
| **2019** | 85 | `ingresos_gastos.pdf` | 11 | 48,2 % | 2.867,94 | — | no_aplica |
| **2020** | 85 | `ingresos_gastos.pdf` | 11 | 47,1 % | 2.902,81 | — | no_aplica |
| **2021** | 85 | `ingresos_gastos.pdf` | 11 | 47,1 % | 3.094,64 | — | no_aplica |
| **2022** | 91 | `ingresos_gastos.pdf` | 11 | 48,4 % | 3.360,61 | — | no_aplica |
| **2023** | 91 | `ingresos_gastos.pdf` | 11 | 48,4 % | 3.524,79 | — | no_aplica |
| **2024** | 89 | `ingresos_gastos.pdf` | 11 | 47,2 % | 3.568,56 | — | no_aplica |
| **2025** | 88 | `ingresos_gastos.pdf` | 11 | 47,7 % | 3.790,88 | — | no_aplica |
| **2026** | 91 | `ingresos_gastos.pdf` | 11 | 49,5 % | 3.972,74 | — | no_aplica |

**URL(s) de origen:**
- <https://www.cantabria.es/documents/16870/0/1.-+Estado+de+Ingresos+y+Gastos.pdf/d491a6f2-65a3-c763-3272-501dfb3b07e3?t=1672303614487>
- <https://www.cantabria.es/documents/16870/10159872/ESTADO+DE+INGRESOS+Y+GASTOS.pdf/59354366-4acb-cb35-a66c-16962c88e8c1?t=1610370000924>
- <https://www.cantabria.es/documents/16870/124906248/2-+2%C2%BA+INGRESOS+Y+GASTOS+DEFINITIVA.pdf>
- <https://www.cantabria.es/documents/16870/17593766/Anexo+de+Ingresos+y+Gastos.pdf/b1b3a49c-38fd-c441-5e90-50478af0ed1e?t=1641208054180>
- <https://www.cantabria.es/documents/16870/3151201/Anexo+de+DESARROLLO+ECON%C3%93MICO+DE+GASTO+POR+CENTROS+GESTORES.pdf/42efe732-e9b1-476c-b1a2-7e4b55cf3edf?t=1421084127747>
- <https://www.cantabria.es/documents/16870/34175817/3.+Estado+de+Ingresos+y+Gastos.pdf/6591a91d-b21f-00cc-75e9-a4cc544308c9?t=1703853508972>
- <https://www.cantabria.es/documents/16870/3601314/Anexo+DESARROLLO+ECON%C3%93MICO+DE+GASTO+POR+CENTROS+GESTORES.pdf/54d07522-0f15-46c6-a1d4-ba3fc7b24d54?t=1451904183021>
- <https://www.cantabria.es/documents/16870/4625307/Anexo+de+DESARROLLO+ECON%C3%93MICO+DE+GASTO+POR+CENTROS+GESTORES.pdf/f6bf7256-f48c-fd12-a8f3-ba0ea02fbf3b?t=1488439779828>
- <https://www.cantabria.es/documents/16870/51252291/02.-+ESTADO+DE+INGRESOS+Y+GASTOS.pdf/6ffdbd50-989b-b540-1261-55c41a8290ed?t=1745912072331>
- <https://www.cantabria.es/documents/16870/5673777/ESTADO+DE+INGRESOS+Y+GASTOS.pdf/aa2ea856-315d-72c4-8afd-1318c2c24a6b?t=1514542759019>
- <https://www.cantabria.es/documents/16870/6784591/3.-+ESTADO+DE+INGRESOS+Y+GASTOS.pdf/c0c6f12a-6860-4801-6b22-8eb5bfb1e66f>
- <https://www.cantabria.es/documents/16870/8498099/Estado+Ingresos+y+Gastos+2020.pdf/bc93be69-9a69-943e-6ccb-a9adbe6920ea?t=1577967585034>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 813,67 | 831,45 | 852,35 | 870,67 | 894,11 | 952,69 | 1.031,45 | 1.041,18 | 1.099,33 | 1.168,05 | 1.240,70 | 1.341,86 |
| `educacion` | 513,39 | 536,38 | 552,22 | 587,78 | 612,60 | 581,07 | 612,29 | 633,98 | 686,86 | 723,84 | 746,61 | 793,19 |
| `soberania` | 21,05 | 19,20 | 20,30 | 21,05 | 21,24 | 15,57 | 16,95 | 16,87 | 17,83 | 17,98 | 17,79 | 19,25 |
| `direccion` | 1,86 | 1,86 | 1,95 | 1,97 | 1,91 | 8,70 | 8,71 | 9,17 | 8,80 | 7,07 | 7,32 | 7,56 |
| `vivienda` | 25,32 | 27,86 | 28,29 | 29,85 | 30,84 | 41,81 | 44,59 | 26,71 | 30,47 | 30,84 | 31,61 | 46,01 |
| `empleo` | 107,34 | 108,62 | 105,98 | 110,42 | 112,35 | 101,87 | 103,70 | 103,94 | 106,26 | 108,75 | 112,75 | 112,75 |
| `idi` | 24,66 | 14,34 | 19,00 | 19,50 | 20,48 | 42,74 | 42,97 | 49,66 | 51,59 | 49,60 | 77,31 | 83,49 |
| `dependencia` | 138,93 | 139,66 | 134,20 | 134,83 | 136,95 | 144,41 | 150,78 | 154,84 | 170,77 | 182,38 | 191,34 | 211,63 |
| `discapacidad` | 10,84 | 11,44 | 11,88 | 12,60 | 14,63 | 14,53 | 14,41 | 14,22 | 15,30 | 14,48 | 17,08 | 19,25 |
| `salud_mental` | 7,15 | 6,17 | 8,13 | — | — | — | — | — | — | — | — | — |
| `turismo` | 12,88 | 14,83 | 21,29 | 23,48 | 23,63 | 23,57 | 26,23 | 26,91 | 32,56 | 30,15 | 29,69 | 29,21 |
| `igualdad` | 1,52 | 1,71 | 1,77 | 1,86 | 3,41 | 10,16 | 9,02 | 8,83 | 11,84 | 7,52 | 7,69 | 8,26 |
| **Σ asignado** | 1.678,61 | 1.713,52 | 1.757,37 | 1.813,99 | 1.872,15 | 1.937,12 | 2.061,07 | 2.086,31 | 2.231,61 | 2.340,66 | 2.479,89 | 2.672,46 |
| *(sin concepto)* | 835,72 | 765,85 | 859,89 | 927,71 | 995,78 | 965,69 | 1.033,57 | 1.274,30 | 1.293,18 | 1.227,90 | 1.310,99 | 1.300,28 |
| **TOTAL extraído** | 2.514,33 | 2.479,37 | 2.617,26 | 2.741,70 | 2.867,94 | 2.902,81 | 3.094,64 | 3.360,61 | 3.524,79 | 3.568,56 | 3.790,88 | 3.972,74 |

**Conceptos sin ninguna línea en toda la serie:** `diversidad` — revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) o un hueco de `correspondencias.yml`.

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +2,2 % | +2,5 % | +2,1 % | +2,7 % | +6,6 % | +8,3 % | +0,9 % | +5,6 % | +6,3 % | +6,2 % | +8,2 % |
| `educacion` | +4,5 % | +3,0 % | +6,4 % | +4,2 % | −5,1 % | +5,4 % | +3,5 % | +8,3 % | +5,4 % | +3,1 % | +6,2 % |
| `soberania` | −8,8 % | +5,7 % | +3,7 % | +0,9 % | −26,7 % | +8,9 % | −0,4 % | +5,7 % | +0,8 % | −1,1 % | +8,2 % |
| `direccion` | +0,1 % | +5,1 % | +1,1 % | −3,1 % | +355,0 % ⚠ | +0,0 % | +5,3 % | −4,0 % | −19,7 % | +3,6 % | +3,2 % |
| `vivienda` | +10,0 % | +1,5 % | +5,5 % | +3,3 % | +35,5 % | +6,7 % | −40,1 % ⚠ | +14,1 % | +1,2 % | +2,5 % | +45,6 % ⚠ |
| `empleo` | +1,2 % | −2,4 % | +4,2 % | +1,7 % | −9,3 % | +1,8 % | +0,2 % | +2,2 % | +2,3 % | +3,7 % | +0,0 % |
| `idi` | −41,9 % ⚠ | +32,5 % | +2,6 % | +5,0 % | +108,7 % ⚠ | +0,5 % | +15,6 % | +3,9 % | −3,9 % | +55,8 % ⚠ | +8,0 % |
| `dependencia` | +0,5 % | −3,9 % | +0,5 % | +1,6 % | +5,5 % | +4,4 % | +2,7 % | +10,3 % | +6,8 % | +4,9 % | +10,6 % |
| `discapacidad` | +5,5 % | +3,9 % | +6,1 % | +16,1 % | −0,7 % | −0,8 % | −1,3 % | +7,5 % | −5,4 % | +18,0 % | +12,7 % |
| `salud_mental` | −13,8 % | +31,8 % | **a 0** ⛔ | · | · | · | · | · | · | · | · |
| `turismo` | +15,1 % | +43,6 % ⚠ | +10,3 % | +0,7 % | −0,3 % | +11,3 % | +2,6 % | +21,0 % | −7,4 % | −1,5 % | −1,6 % |
| `igualdad` | +12,5 % | +3,4 % | +5,1 % | +84,0 % ⚠ | +197,7 % ⚠ | −11,3 % | −2,0 % | +34,1 % | −36,5 % | +2,2 % | +7,4 % |
| **TOTAL** | −1,4 % | +5,6 % | +4,8 % | +4,6 % | +1,2 % | +6,6 % | +8,6 % | +4,9 % | +1,2 % | +6,2 % | +4,8 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `idi` | **SALTO** | 24,66 → 14,34 M€ (−41,9 % ⚠) |
| 2017 | `turismo` | **SALTO** | 14,83 → 21,29 M€ (+43,6 % ⚠) |
| 2020 | `idi` | **SALTO** | 20,48 → 42,74 M€ (+108,7 % ⚠) |
| 2022 | `vivienda` | **SALTO** | 44,59 → 26,71 M€ (−40,1 % ⚠) |
| 2025 | `idi` | **SALTO** | 49,60 → 77,31 M€ (+55,8 % ⚠) |
| 2026 | `vivienda` | **SALTO** | 31,61 → 46,01 M€ (+45,6 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (5 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `923M` | 21,65 | 2015:empleo, 2016:empleo, 2017:empleo, 2018:empleo, 2019:empleo, 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto) |
| `323A` | 14,99 | 2015:idi, 2016:idi, 2017:idi, 2018:idi, 2019:idi, 2020:idi, 2021:idi, 2022:idi, 2023:idi, 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `414B` | 8,13 | 2015:salud_mental, 2016:salud_mental, 2017:salud_mental, 2020:idi, 2021:idi, 2022:idi, 2023:idi, 2024:idi, 2025:idi, 2026:idi |
| `331M` | 5,31 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2022:igualdad, 2023:igualdad, 2024:turismo, 2025:turismo, 2026:turismo |
| `231E` | 4,58 | 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:dependencia, 2025:dependencia, 2026:dependencia |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `desarrollo_centros.pdf` · 83 líneas · total extraído **2.514,33 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 813,67 M€ (813.671.798 €) · 9 códigos · 32,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 753.067.288 | 92,6 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 19.444.495 | 2,4 % |
| `313A` | SALUD PÚBLICA | 8.370.102 | 1,0 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LAS PRODUCCIONES | 7.975.835 | 1,0 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 7.490.862 | 0,9 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 5.369.272 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD Y SERVICIOS SOCIALES | 4.965.228 | 0,6 % |
| `311N` | ORDENACIÓN SANITARIA | 4.636.393 | 0,6 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.352.323 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 513,39 M€ (513.386.490 €) · 7 códigos · 20,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 249.868.929 | 48,7 % |
| `322A` | PERSONAL NO DOCENTE Y GESTIÓN DE CENTROS | 143.550.975 | 28,0 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 67.964.234 | 13,2 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 28.573.154 | 5,6 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 16.082.152 | 3,1 % |
| `322C` | PROYECTO COMILLAS | 4.245.138 | 0,8 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 3.101.908 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 21,05 M€ (21.049.003 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | DESARROLLO RURAL Y ESTRUCTURAS AGRARIAS | 12.490.305 | 59,3 % |
| `411M` | DIRECCIÓN Y SERVICIOS GENERALES DE GANADERÍA, PESCA Y DESARROLLO RURAL | 8.558.698 | 40,7 % |

</details>

<details open><summary><b><code>direccion</code> — 1,86 M€ (1.855.297 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 1.855.297 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 25,32 M€ (25.322.423 €) · 5 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 15.482.564 | 61,1 % |
| `451N` | DIRECCIÓN Y SERVICIOS GENERALES DE OBRAS PÚBLICAS Y VIVIENDA | 3.859.543 | 15,2 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 2.762.433 | 10,9 % |
| `431A` | COMERCIO | 2.069.584 | 8,2 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.148.299 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 107,34 M€ (107.341.952 €) · 5 códigos · 4,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 61.239.589 | 57,1 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 19.079.098 | 17,8 % |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y EMPLEO | 14.085.117 | 13,1 % |
| `241N` | INTERMEDIACIÓN LABORAL | 7.268.783 | 6,8 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.669.365 | 5,3 % |

</details>

<details open><summary><b><code>idi</code> — 24,66 M€ (24.662.333 €) · 4 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN | 13.592.475 | 55,1 % |
| `323A` | ORDENACIÓN E INNOVACIÓN EDUCATIVA | 7.078.502 | 28,7 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 3.370.390 | 13,7 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 620.966 | 2,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 138,93 M€ (138.925.482 €) · 3 códigos · 5,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 136.230.567 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.865.000 | 1,3 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 829.915 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 10,84 M€ (10.838.358 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 10.838.358 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 7,15 M€ (7.154.009 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414B` | MEJORA DE LA ACTIVIDAD AGRARIA | 7.154.009 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 12,88 M€ (12.882.424 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 12.882.424 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,52 M€ (1.517.729 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 1.517.729 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 835,72 M€ · 43 códigos · 33,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 400.242.795 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 57.038.509 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 55.066.159 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 51.750.509 |
| `456B` | CALIDAD AMBIENTAL | 35.949.128 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 28.603.900 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 26.054.998 |
| `494M` | RELACIONES LABORALES | 20.202.645 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 18.401.281 |
| `931P` | PLANIFICACIÓN DE LA ACTIVIDAD FINANCIERA | 12.262.223 |
| `134M` | PROTECCIÓN CIVIL | 11.952.248 |
| `458A` | ACTUACIONES EN EL ÁMBITO LOCAL | 11.321.787 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 8.293.589 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 8.056.528 |
| `921O` | MANTENIMIENTO | 8.045.570 |
| `921M` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 7.968.081 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 7.525.296 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 7.299.422 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 6.971.545 |
| `911M` | ACTIVIDAD LEGISLATIVA | 6.965.369 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 6.753.136 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 6.198.524 |
| `332A` | CENTROS CULTURALES | 5.830.986 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 3.449.024 |
| `931N` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 3.399.571 |
| … | *resto: 18 códigos* | 20.119.515 |

</details>

### 2016

*Fuente: `desarrollo_centros.pdf` · 84 líneas · total extraído **2.479,37 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 831,45 M€ (831.449.140 €) · 9 códigos · 33,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 773.205.141 | 93,0 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 19.567.542 | 2,4 % |
| `313A` | SALUD PÚBLICA | 8.519.570 | 1,0 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 7.744.407 | 0,9 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LAS PRODUCCIONES | 6.000.128 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.151.262 | 0,6 % |
| `311N` | ORDENACIÓN SANITARIA | 4.928.641 | 0,6 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 4.251.570 | 0,5 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.080.879 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 536,38 M€ (536.376.717 €) · 8 códigos · 21,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 265.879.237 | 49,6 % |
| `322A` | GESTIÓN DE CENTROS | 139.212.962 | 26,0 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 88.508.425 | 16,5 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 16.609.845 | 3,1 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 16.485.740 | 3,1 % |
| `322C` | PROYECTO COMILLAS | 4.245.138 | 0,8 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 3.150.196 | 0,6 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 2.285.174 | 0,4 % |

</details>

<details open><summary><b><code>soberania</code> — 19,20 M€ (19.203.374 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | DESARROLLO RURAL Y ESTRUCTURAS AGRARIAS | 9.949.872 | 51,8 % |
| `411M` | DIRECCIÓN Y SERVICIOS GENERALES DE MEDIO RURAL, PESCA Y ALIMENTACIÓN | 9.253.502 | 48,2 % |

</details>

<details open><summary><b><code>direccion</code> — 1,86 M€ (1.857.507 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 1.857.507 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 27,86 M€ (27.862.476 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 17.543.532 | 63,0 % |
| `451N` | DIRECCIÓN Y SERVICIOS GENERALES DE OBRAS PÚBLICAS Y VIVIENDA | 4.023.388 | 14,4 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 3.079.255 | 11,1 % |
| `431A` | COMERCIO | 1.958.298 | 7,0 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.258.003 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 108,62 M€ (108.622.841 €) · 5 códigos · 4,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 61.757.933 | 56,9 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 19.464.275 | 17,9 % |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y EMPLEO | 14.931.472 | 13,7 % |
| `241N` | INTERMEDIACIÓN LABORAL | 7.087.707 | 6,5 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.381.454 | 5,0 % |

</details>

<details open><summary><b><code>idi</code> — 14,34 M€ (14.337.798 €) · 4 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | INNOVACIÓN | 7.661.469 | 53,4 % |
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 3.447.476 | 24,0 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.605.698 | 18,2 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 623.155 | 4,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 139,66 M€ (139.664.656 €) · 3 códigos · 5,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 137.045.241 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.765.000 | 1,3 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 854.415 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 11,44 M€ (11.437.096 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 11.437.096 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 6,17 M€ (6.168.598 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414B` | MEJORA DE LA ACTIVIDAD AGRARIA | 6.168.598 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 14,83 M€ (14.829.474 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 14.829.474 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,71 M€ (1.706.773 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 1.706.773 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 765,85 M€ · 43 códigos · 30,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 329.892.000 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 61.288.592 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 40.561.963 |
| `456B` | CALIDAD AMBIENTAL | 37.918.143 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 35.070.463 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 29.252.353 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 26.033.239 |
| `458A` | ACTUACIONES EN EL ÁMBITO LOCAL | 25.477.321 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 21.477.507 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 17.131.362 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 12.677.944 |
| `134M` | PROTECCIÓN CIVIL Y EMERGENCIAS | 12.306.027 |
| `494M` | RELACIONES LABORALES | 11.932.156 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 10.051.708 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 9.028.877 |
| `921O` | MANTENIMIENTO | 7.873.512 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 7.551.718 |
| `911M` | ACTIVIDAD LEGISLATIVA | 7.445.399 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 7.413.269 |
| `921M` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 7.116.353 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 6.672.969 |
| `332A` | CENTROS CULTURALES | 5.772.547 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 5.366.850 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 3.636.625 |
| `931N` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 3.614.383 |
| … | *resto: 18 códigos* | 23.290.297 |

</details>

### 2017

*Fuente: `desarrollo_centros.pdf` · 84 líneas · total extraído **2.617,26 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 852,35 M€ (852.348.270 €) · 9 códigos · 32,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 792.398.164 | 93,0 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 19.763.216 | 2,3 % |
| `313A` | SALUD PÚBLICA | 9.118.188 | 1,1 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 8.834.340 | 1,0 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LAS PRODUCCIONES | 6.379.731 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.232.821 | 0,6 % |
| `311N` | ORDENACIÓN SANITARIA | 4.940.451 | 0,6 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 3.502.111 | 0,4 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.179.248 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 552,22 M€ (552.223.348 €) · 8 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 276.751.826 | 50,1 % |
| `322A` | GESTIÓN DE CENTROS | 137.112.756 | 24,8 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 87.755.743 | 15,9 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 22.299.388 | 4,0 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 16.688.587 | 3,0 % |
| `322C` | PROYECTO COMILLAS | 5.345.138 | 1,0 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 3.532.739 | 0,6 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 2.737.171 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 20,30 M€ (20.301.447 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | DESARROLLO RURAL Y ESTRUCTURAS AGRARIAS | 10.787.393 | 53,1 % |
| `411M` | DIRECCIÓN Y SERVICIOS GENERALES DE MEDIO RURAL, PESCA Y ALIMENTACIÓN | 9.514.054 | 46,9 % |

</details>

<details open><summary><b><code>direccion</code> — 1,95 M€ (1.953.093 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 1.953.093 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 28,29 M€ (28.287.681 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 18.141.335 | 64,1 % |
| `451N` | DIRECCIÓN Y SERVICIOS GENERALES DE OBRAS PÚBLICAS Y VIVIENDA | 4.163.177 | 14,7 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 2.841.611 | 10,0 % |
| `431A` | COMERCIO | 1.864.044 | 6,6 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.277.514 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 105,98 M€ (105.980.816 €) · 5 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 53.501.353 | 50,5 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 26.363.744 | 24,9 % |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y EMPLEO | 14.289.447 | 13,5 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.989.944 | 5,7 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 5.836.328 | 5,5 % |

</details>

<details open><summary><b><code>idi</code> — 19,00 M€ (19.000.371 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | INNOVACIÓN | 8.000.065 | 42,1 % |
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 7.495.514 | 39,4 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.877.601 | 15,1 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 627.191 | 3,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 134,20 M€ (134.204.538 €) · 3 códigos · 5,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 131.645.780 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.675.000 | 1,2 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 883.758 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 11,88 M€ (11.881.158 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 11.881.158 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,13 M€ (8.129.154 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414B` | MEJORA DE LA ACTIVIDAD AGRARIA | 8.129.154 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 21,29 M€ (21.292.996 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 21.292.996 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,77 M€ (1.765.645 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 1.765.645 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 859,89 M€ · 43 códigos · 32,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 386.230.212 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 69.370.460 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 41.490.279 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 41.156.489 |
| `456B` | CALIDAD AMBIENTAL | 39.904.031 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 31.981.384 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 30.123.498 |
| `458A` | ACTUACIONES EN EL ÁMBITO LOCAL | 28.986.651 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 23.155.767 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 18.792.360 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 14.924.804 |
| `134M` | PROTECCIÓN CIVIL Y EMERGENCIAS | 13.909.692 |
| `494M` | RELACIONES LABORALES | 10.112.978 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 9.521.585 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 9.081.715 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.521.219 |
| `921O` | MANTENIMIENTO | 7.804.770 |
| `911M` | ACTIVIDAD LEGISLATIVA | 7.445.399 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 7.007.348 |
| `332A` | CENTROS CULTURALES | 6.998.165 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 6.888.695 |
| `921M` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 6.762.572 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 6.646.711 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 3.986.878 |
| `931N` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 3.632.631 |
| … | *resto: 18 códigos* | 25.451.417 |

</details>

### 2018

*Fuente: `ingresos_gastos.pdf` · 84 líneas · total extraído **2.741,70 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 870,67 M€ (870.665.092 €) · 8 códigos · 31,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 810.259.420 | 93,1 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 20.551.777 | 2,4 % |
| `313A` | SALUD PÚBLICA | 9.521.066 | 1,1 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 8.839.850 | 1,0 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 8.435.862 | 1,0 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.387.641 | 0,6 % |
| `311N` | ORDENACIÓN SANITARIA | 5.077.069 | 0,6 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.592.407 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 587,78 M€ (587.781.378 €) · 9 códigos · 21,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 285.088.488 | 48,5 % |
| `322A` | GESTIÓN DE CENTROS | 139.872.469 | 23,8 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 92.610.375 | 15,8 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 28.761.577 | 4,9 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 17.075.515 | 2,9 % |
| `421M` | DIRECCIÓN Y SERVICIOS GENERALES DE INNOVACIÓN, INDUSTRIA, TURISMO Y COMERCIO | 10.489.068 | 1,8 % |
| `322C` | PROYECTO COMILLAS | 6.160.283 | 1,0 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.353.917 | 0,7 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 3.369.686 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 21,05 M€ (21.045.344 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | DESARROLLO RURAL Y ESTRUCTURAS AGRARIAS | 11.402.455 | 54,2 % |
| `411M` | DIRECCIÓN Y SERVICIOS GENERALES DE MEDIO RURAL, PESCA Y ALIMENTACIÓN | 9.642.889 | 45,8 % |

</details>

<details open><summary><b><code>direccion</code> — 1,97 M€ (1.974.781 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 1.974.781 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 29,85 M€ (29.846.073 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 18.981.202 | 63,6 % |
| `451N` | DIRECCIÓN Y SERVICIOS GENERALES DE OBRAS PÚBLICAS Y VIVIENDA | 4.622.419 | 15,5 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 3.235.154 | 10,8 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.534.359 | 5,1 % |
| `431A` | COMERCIO | 1.472.939 | 4,9 % |

</details>

<details open><summary><b><code>empleo</code> — 110,42 M€ (110.416.013 €) · 5 códigos · 4,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 63.214.312 | 57,3 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 20.768.546 | 18,8 % |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y EMPLEO | 14.181.981 | 12,8 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 6.421.345 | 5,8 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 5.829.829 | 5,3 % |

</details>

<details open><summary><b><code>idi</code> — 19,50 M€ (19.497.531 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | INNOVACIÓN | 8.233.378 | 42,2 % |
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 7.623.612 | 39,1 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 3.002.793 | 15,4 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 637.748 | 3,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 134,83 M€ (134.832.316 €) · 3 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 132.271.856 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.675.000 | 1,2 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 885.460 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 12,60 M€ (12.600.670 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 12.600.670 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,48 M€ (23.477.508 €) · 1 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 23.477.508 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 1,86 M€ (1.855.723 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 1.855.723 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 927,71 M€ · 44 códigos · 33,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 426.140.404 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 75.728.641 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 45.541.933 |
| `456B` | CALIDAD AMBIENTAL | 41.403.657 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 36.632.998 |
| `458A` | ACTUACIONES EN EL ÁMBITO LOCAL | 34.638.225 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 34.048.513 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 31.443.571 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 21.724.272 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 19.940.647 |
| `134M` | PROTECCIÓN CIVIL Y EMERGENCIAS | 14.327.392 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 12.686.611 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 11.989.202 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 9.721.085 |
| `494M` | RELACIONES LABORALES | 9.323.203 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.827.951 |
| `332A` | CENTROS CULTURALES | 8.533.996 |
| `921O` | MANTENIMIENTO | 7.944.274 |
| `911M` | ACTIVIDAD LEGISLATIVA | 7.543.200 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 7.282.749 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 7.102.476 |
| `921M` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 7.043.043 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 6.100.383 |
| `413A` | DESARROLLO DE LA INDUSTRIALIZACIÓN, COMERCIALIZACIÓN Y COOPERACIÓN AGRARIA | 5.990.163 |
| `931N` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 4.120.214 |
| … | *resto: 19 códigos* | 31.928.282 |

</details>

### 2019

*Fuente: `ingresos_gastos.pdf` · 85 líneas · total extraído **2.867,94 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 894,11 M€ (894.106.775 €) · 9 códigos · 31,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 827.565.160 | 92,6 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 20.869.533 | 2,3 % |
| `313A` | SALUD PÚBLICA | 9.803.830 | 1,1 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 9.482.185 | 1,1 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 7.745.017 | 0,9 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 5.378.263 | 0,6 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.344.008 | 0,6 % |
| `311N` | ORDENACIÓN SANITARIA | 5.266.746 | 0,6 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.652.033 | 0,3 % |

</details>

<details open><summary><b><code>educacion</code> — 612,60 M€ (612.600.404 €) · 9 códigos · 21,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 291.230.284 | 47,5 % |
| `322A` | GESTIÓN DE CENTROS | 142.587.189 | 23,3 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 108.631.721 | 17,7 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 29.183.861 | 4,8 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 18.943.519 | 3,1 % |
| `421M` | DIRECCIÓN Y SERVICIOS GENERALES DE INNOVACIÓN, INDUSTRIA, TURISMO Y COMERCIO | 10.638.300 | 1,7 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.367.906 | 0,7 % |
| `322C` | PROYECTO COMILLAS | 3.971.000 | 0,6 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 3.046.624 | 0,5 % |

</details>

<details open><summary><b><code>soberania</code> — 21,24 M€ (21.241.225 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | DESARROLLO RURAL Y ESTRUCTURAS AGRARIAS | 11.822.250 | 55,7 % |
| `411M` | DIRECCIÓN Y SERVICIOS GENERALES DE MEDIO RURAL, PESCA Y ALIMENTACIÓN | 9.418.975 | 44,3 % |

</details>

<details open><summary><b><code>direccion</code> — 1,91 M€ (1.912.806 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 1.912.806 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 30,84 M€ (30.841.472 €) · 5 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 16.542.803 | 53,6 % |
| `451N` | DIRECCIÓN Y SERVICIOS GENERALES DE OBRAS PÚBLICAS Y VIVIENDA | 8.111.075 | 26,3 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 3.331.223 | 10,8 % |
| `431A` | COMERCIO | 1.537.371 | 5,0 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.319.000 | 4,3 % |

</details>

<details open><summary><b><code>empleo</code> — 112,35 M€ (112.345.707 €) · 5 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 57.573.236 | 51,2 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 28.405.142 | 25,3 % |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y EMPLEO | 13.902.377 | 12,4 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 6.477.840 | 5,8 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 5.987.112 | 5,3 % |

</details>

<details open><summary><b><code>idi</code> — 20,48 M€ (20.481.355 €) · 4 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323A` | INNOVACIÓN | 8.689.718 | 42,4 % |
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 8.047.844 | 39,3 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 3.093.892 | 15,1 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 649.901 | 3,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 136,95 M€ (136.947.079 €) · 3 códigos · 4,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 134.362.751 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.675.000 | 1,2 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 909.328 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,63 M€ (14.629.432 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 14.629.432 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,63 M€ (23.631.802 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 23.631.802 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,41 M€ (3.413.851 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 3.413.851 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 995,78 M€ · 44 códigos · 34,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 467.149.570 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 76.681.044 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 44.883.997 |
| `456B` | CALIDAD AMBIENTAL | 42.815.035 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 38.822.625 |
| `458A` | ACTUACIONES EN EL ÁMBITO LOCAL | 37.762.506 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 34.742.265 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 32.306.214 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 23.581.396 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 20.727.409 |
| `134M` | PROTECCIÓN CIVIL Y EMERGENCIAS | 15.060.394 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 14.300.206 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 12.800.010 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 9.966.700 |
| `494M` | RELACIONES LABORALES | 9.537.566 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.949.505 |
| `929N` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 8.851.534 |
| `332A` | CENTROS CULTURALES | 8.799.390 |
| `921O` | MANTENIMIENTO | 8.286.984 |
| `921M` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA Y JUSTICIA | 7.864.372 |
| `911M` | ACTIVIDAD LEGISLATIVA | 7.765.838 |
| `413A` | DESARROLLO DE LA INDUSTRIALIZACIÓN, COMERCIALIZACIÓN Y COOPERACIÓN AGRARIA | 7.437.517 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 7.359.280 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 6.770.400 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 6.035.956 |
| … | *resto: 19 códigos* | 36.526.663 |

</details>

### 2020

*Fuente: `ingresos_gastos.pdf` · 85 líneas · total extraído **2.902,81 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 952,69 M€ (952.686.411 €) · 10 códigos · 32,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 886.411.689 | 93,0 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 22.291.513 | 2,3 % |
| `313A` | SALUD PÚBLICA | 9.741.470 | 1,0 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 7.653.651 | 0,8 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 6.770.765 | 0,7 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 5.538.954 | 0,6 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.399.100 | 0,6 % |
| `311N` | ORDENACIÓN, FARMACIA E INSPECCIÓN SANITARIA | 4.773.296 | 0,5 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.687.033 | 0,3 % |
| `311A` | TRANSFORMACIÓN DIGITAL Y RELACIONES CON LOS USUARIS | 1.418.940 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 581,07 M€ (581.071.798 €) · 7 códigos · 20,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 311.455.772 | 53,6 % |
| `322A` | GESTIÓN DE CENTROS | 147.585.741 | 25,4 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 82.489.642 | 14,2 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 27.914.756 | 4,8 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.375.048 | 0,8 % |
| `322C` | PROYECTO COMILLAS | 3.971.000 | 0,7 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 3.279.839 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 15,57 M€ (15.567.926 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 15.567.926 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 8,70 M€ (8.702.338 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 8.702.338 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 41,81 M€ (41.805.547 €) · 4 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA | 34.530.727 | 82,6 % |
| `261M` | ACTUACIONES EN MATERIA DE ORDENACIÓN DEL TERRITORIO | 3.381.272 | 8,1 % |
| `261N` | ACTUACIONES EN MATERIA DE URBANISMO Y ARQUITECTURA | 2.023.480 | 4,8 % |
| `431A` | COMERCIO | 1.870.068 | 4,5 % |

</details>

<details open><summary><b><code>empleo</code> — 101,87 M€ (101.865.279 €) · 5 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 55.968.041 | 54,9 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 29.003.870 | 28,5 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 7.749.568 | 7,6 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 5.721.851 | 5,6 % |
| `231M` | DIRECCIÓN Y SERVICIOS GENERALES DE EMPLEO Y POLÍTICAS SOCIALES | 3.421.949 | 3,4 % |

</details>

<details open><summary><b><code>idi</code> — 42,74 M€ (42.743.819 €) · 5 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 27.683.144 | 64,8 % |
| `323A` | INNOVACIÓN | 8.708.716 | 20,4 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.891.892 | 6,8 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 2.842.907 | 6,7 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 617.160 | 1,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 144,41 M€ (144.411.558 €) · 3 códigos · 5,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 141.827.730 | 98,2 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.675.000 | 1,2 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 908.828 | 0,6 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,53 M€ (14.529.632 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 14.529.632 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,57 M€ (23.569.169 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 23.569.169 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,16 M€ (10.164.005 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451M` | DIRECCIÓN Y SERVICIOS GENERALES DE UNIVERSIDADES,IGUALDAD, CULTURA Y DEPORTE | 6.715.265 | 66,1 % |
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 3.448.740 | 33,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 965,69 M€ · 45 códigos · 33,3 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 431.458.226 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 73.281.365 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 54.437.311 |
| `456B` | CALIDAD AMBIENTAL | 44.737.833 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 39.668.491 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 34.049.058 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 33.412.778 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 21.057.459 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 19.657.747 |
| `232A` | PROMOCIÓN Y SERVICIOS A LA JUVENTUD | 19.497.418 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCION EXTERIOR | 18.762.398 |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA Y HACIENDA | 14.285.873 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 10.102.861 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 9.892.610 |
| `494M` | RELACIONES LABORALES | 9.588.097 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 9.137.646 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 8.646.877 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.568.972 |
| `332A` | CENTROS CULTURALES | 8.546.155 |
| `921O` | MANTENIMIENTO | 8.405.938 |
| `911M` | ACTIVIDAD LEGISLATIVA | 8.071.428 |
| `134M` | PROTECCIÓN CIVIL | 7.855.866 |
| `134N` | EMERGENCIAS | 7.851.301 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 7.437.816 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 7.363.882 |
| … | *resto: 20 códigos* | 49.914.996 |

</details>

### 2021

*Fuente: `ingresos_gastos.pdf` · 85 líneas · total extraído **3.094,64 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.031,45 M€ (1.031.448.121 €) · 10 códigos · 33,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 960.114.468 | 93,1 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 22.082.711 | 2,1 % |
| `313A` | SALUD PÚBLICA | 12.655.892 | 1,2 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 7.909.728 | 0,8 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 6.899.841 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.988.977 | 0,6 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 5.652.534 | 0,5 % |
| `311N` | ORDENACIÓN, FARMACIA E INSPECCIÓN SANITARIA | 4.967.711 | 0,5 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.887.033 | 0,3 % |
| `311A` | TRANSFORMACIÓN DIGITAL Y RELACIONES CON LAS PERSONAS USUARIAS | 2.289.226 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 612,29 M€ (612.286.337 €) · 7 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 331.455.772 | 54,1 % |
| `322A` | GESTIÓN DE CENTROS | 152.790.883 | 25,0 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS E INVESTIGACIÓN CIENTÍFICA | 86.203.267 | 14,1 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 28.200.547 | 4,6 % |
| `322C` | PROYECTO COMILLAS | 5.595.000 | 0,9 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.665.970 | 0,8 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 3.374.898 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 16,95 M€ (16.947.571 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 16.947.571 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 8,71 M€ (8.705.210 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 8.705.210 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 44,59 M€ (44.586.274 €) · 4 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA | 36.400.108 | 81,6 % |
| `261M` | ACTUACIONES EN MATERIA DE ORDENACIÓN DEL TERRITORIO | 3.175.637 | 7,1 % |
| `261N` | ACTUACIONES EN MATERIA DE URBANISMO Y ARQUITECTURA | 3.047.431 | 6,8 % |
| `431A` | COMERCIO | 1.963.098 | 4,4 % |

</details>

<details open><summary><b><code>empleo</code> — 103,70 M€ (103.698.258 €) · 5 códigos · 3,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 56.962.934 | 54,9 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 27.278.563 | 26,3 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 8.820.867 | 8,5 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 6.993.966 | 6,7 % |
| `231M` | DIRECCIÓN Y SERVICIOS GENERALES DE EMPLEO Y POLÍTICAS SOCIALES | 3.641.928 | 3,5 % |

</details>

<details open><summary><b><code>idi</code> — 42,97 M€ (42.967.168 €) · 5 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 27.695.432 | 64,5 % |
| `323A` | INNOVACIÓN | 8.532.921 | 19,9 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.167.439 | 7,4 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.891.892 | 6,7 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 679.484 | 1,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 150,78 M€ (150.775.265 €) · 3 códigos · 4,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 147.853.365 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.675.000 | 1,1 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.246.900 | 0,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,41 M€ (14.412.201 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 14.412.201 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 26,23 M€ (26.230.083 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 26.230.083 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,02 M€ (9.017.657 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451M` | DIRECCIÓN Y SERVICIOS GENERALES DE UNIVERSIDADES,IGUALDAD, CULTURA Y DEPORTE | 5.523.777 | 61,3 % |
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 3.493.880 | 38,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.033,57 M€ · 45 códigos · 33,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 474.902.476 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 75.025.089 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 55.999.673 |
| `456B` | CALIDAD AMBIENTAL | 44.461.821 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 41.324.706 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 37.206.666 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 34.560.810 |
| `232A` | PROMOCIÓN Y SERVICIOS A LA JUVENTUD | 25.632.939 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 22.163.646 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCION EXTERIOR | 19.502.109 |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA Y HACIENDA | 16.289.329 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 13.666.928 |
| `332A` | CENTROS CULTURALES | 11.663.131 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 11.383.572 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 10.455.956 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 9.786.408 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 9.719.939 |
| `494M` | RELACIONES LABORALES | 9.579.101 |
| `134N` | EMERGENCIAS | 9.368.301 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.610.088 |
| `921O` | MANTENIMIENTO | 8.488.630 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 8.388.958 |
| `911M` | ACTIVIDAD LEGISLATIVA | 8.025.970 |
| `134M` | PROTECCIÓN CIVIL | 7.974.380 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 7.225.744 |
| … | *resto: 20 códigos* | 52.159.912 |

</details>

### 2022

*Fuente: `ingresos_gastos.pdf` · 91 líneas · total extraído **3.360,61 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.041,18 M€ (1.041.181.743 €) · 11 códigos · 31,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 967.325.891 | 92,9 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 22.077.320 | 2,1 % |
| `313A` | SALUD PÚBLICA | 14.042.068 | 1,3 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 8.291.747 | 0,8 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 7.091.273 | 0,7 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 6.553.729 | 0,6 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 6.285.259 | 0,6 % |
| `311N` | ORDENACIÓN, FARMACIA E INSPECCIÓN SANITARIA | 2.995.500 | 0,3 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 2.914.255 | 0,3 % |
| `461C` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN SANITARIA | 2.019.000 | 0,2 % |
| `311A` | TRANSFORMACIÓN DIGITAL Y RELACIONES CON LAS PERSONAS USUARIAS | 1.585.701 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 633,98 M€ (633.984.499 €) · 8 códigos · 18,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 336.137.309 | 53,0 % |
| `322A` | GESTIÓN DE CENTROS | 151.014.071 | 23,8 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS | 83.111.053 | 13,1 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 29.005.229 | 4,6 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN Y FORMACIÓN PROFESIONAL | 20.924.518 | 3,3 % |
| `322C` | PROYECTO COMILLAS | 5.595.000 | 0,9 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.186.091 | 0,7 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 4.011.228 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 16,87 M€ (16.873.139 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 16.873.139 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 9,17 M€ (9.166.814 €) · 1 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 9.166.814 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 26,71 M€ (26.705.133 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA | 16.654.121 | 62,4 % |
| `261N` | ACTUACIONES EN MATERIA DE URBANISMO Y ARQUITECTURA | 3.717.580 | 13,9 % |
| `261M` | ACTUACIONES EN MATERIA DE ORDENACIÓN DEL TERRITORIO | 3.361.927 | 12,6 % |
| `431A` | COMERCIO | 2.971.505 | 11,1 % |

</details>

<details open><summary><b><code>empleo</code> — 103,94 M€ (103.942.441 €) · 5 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 57.616.391 | 55,4 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 29.433.825 | 28,3 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 7.653.991 | 7,4 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 5.539.392 | 5,3 % |
| `231M` | DIRECCIÓN Y SERVICIOS GENERALES DE EMPLEO Y POLÍTICAS SOCIALES | 3.698.842 | 3,6 % |

</details>

<details open><summary><b><code>idi</code> — 49,66 M€ (49.656.475 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 28.513.707 | 57,4 % |
| `323A` | INNOVACIÓN | 9.135.901 | 18,4 % |
| `461B` | INVESTIGACIÓN CIENTÍFICA Y TRANSFERENCIA DEL CONOCIMIENTO | 5.366.348 | 10,8 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.219.393 | 6,5 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.917.569 | 5,9 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 503.557 | 1,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 154,84 M€ (154.836.701 €) · 3 códigos · 4,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 151.913.201 | 98,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.671.500 | 1,1 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.252.000 | 0,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,22 M€ (14.222.435 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 14.192.435 | 99,8 % |
| `232C` | FOMENTO DE LAS ACTIVIDADES JUVENILES | 30.000 | 0,2 % |

</details>

<details open><summary><b><code>turismo</code> — 26,91 M€ (26.907.677 €) · 1 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 26.907.677 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,83 M€ (8.832.976 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `331M` | DIRECCIÓN Y SERVICIOS GENERALES DE UNIVERSIDADES, IGUALDAD, CULTURA Y DEPORTE | 5.313.002 | 60,1 % |
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 3.519.974 | 39,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.274,30 M€ · 47 códigos · 37,9 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 517.533.200 |
| `140A` | MECANISMO DE RECUPERACIÓN Y RESILIENCIA (MRR) | 139.433.413 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 72.032.265 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 57.178.186 |
| `140B` | REACT-UE | 49.026.588 |
| `456B` | CALIDAD AMBIENTAL | 44.862.518 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 42.744.547 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 39.106.851 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 36.026.128 |
| `232A` | PROMOCIÓN Y SERVICIOS A LA JUVENTUD | 28.188.106 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 23.896.513 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCION EXTERIOR | 19.928.704 |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA Y HACIENDA | 17.448.944 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 13.401.867 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 12.391.243 |
| `332A` | CENTROS CULTURALES | 11.404.803 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 10.367.636 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 9.712.086 |
| `494M` | RELACIONES LABORALES | 9.575.778 |
| `134N` | EMERGENCIAS | 9.368.301 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 9.066.380 |
| `921O` | MANTENIMIENTO | 9.056.538 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 8.935.360 |
| `911M` | ACTIVIDAD LEGISLATIVA | 8.359.335 |
| `134M` | PROTECCIÓN CIVIL | 8.358.746 |
| … | *resto: 22 códigos* | 66.891.660 |

</details>

### 2023

*Fuente: `ingresos_gastos.pdf` · 91 líneas · total extraído **3.524,79 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.099,33 M€ (1.099.328.181 €) · 11 códigos · 31,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 1.018.720.565 | 92,7 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 24.683.670 | 2,2 % |
| `313A` | SALUD PÚBLICA | 16.078.926 | 1,5 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 9.326.933 | 0,8 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 7.513.068 | 0,7 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 7.037.021 | 0,6 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 5.406.080 | 0,5 % |
| `311N` | ORDENACIÓN, FARMACIA E INSPECCIÓN SANITARIA | 3.636.380 | 0,3 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 3.078.222 | 0,3 % |
| `461C` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN SANITARIA | 2.019.000 | 0,2 % |
| `311A` | TRANSFORMACIÓN DIGITAL Y RELACIONES CON LAS PERSONAS USUARIAS | 1.828.316 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 686,86 M€ (686.857.723 €) · 8 códigos · 19,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 371.485.749 | 54,1 % |
| `322A` | GESTIÓN DE CENTROS | 171.210.760 | 24,9 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS | 86.899.531 | 12,7 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 35.014.932 | 5,1 % |
| `321M` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN Y FORMACIÓN PROFESIONAL | 7.434.099 | 1,1 % |
| `322C` | PROYECTO COMILLAS | 6.120.000 | 0,9 % |
| `321N` | PERSONAL NO DOCENTE Y ORDENACIÓN ACADÉMICA | 4.363.254 | 0,6 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.329.398 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 17,83 M€ (17.829.646 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 17.829.646 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 8,80 M€ (8.799.351 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 8.799.351 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 30,47 M€ (30.474.540 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA | 21.161.907 | 69,4 % |
| `261M` | ACTUACIONES EN MATERIA DE ORDENACIÓN DEL TERRITORIO | 3.474.267 | 11,4 % |
| `431A` | COMERCIO | 3.180.772 | 10,4 % |
| `261N` | ACTUACIONES EN MATERIA DE URBANISMO Y ARQUITECTURA | 2.657.594 | 8,7 % |

</details>

<details open><summary><b><code>empleo</code> — 106,26 M€ (106.262.018 €) · 5 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 61.535.475 | 57,9 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 28.685.377 | 27,0 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 8.207.087 | 7,7 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.136.061 | 4,8 % |
| `231M` | DIRECCIÓN Y SERVICIOS GENERALES DE EMPLEO Y POLÍTICAS SOCIALES | 2.698.018 | 2,5 % |

</details>

<details open><summary><b><code>idi</code> — 51,59 M€ (51.590.872 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 28.683.908 | 55,6 % |
| `323A` | INNOVACIÓN | 8.999.846 | 17,4 % |
| `461B` | INVESTIGACIÓN CIENTÍFICA Y TRANSFERENCIA DEL CONOCIMIENTO | 6.749.919 | 13,1 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.688.657 | 7,1 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.972.071 | 5,8 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 496.471 | 1,0 % |

</details>

<details open><summary><b><code>dependencia</code> — 170,77 M€ (170.767.283 €) · 3 códigos · 4,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 167.821.783 | 98,3 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.671.500 | 1,0 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.274.000 | 0,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 15,30 M€ (15.296.220 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 15.266.220 | 99,8 % |
| `232C` | FOMENTO DE LAS ACTIVIDADES JUVENILES | 30.000 | 0,2 % |

</details>

<details open><summary><b><code>turismo</code> — 32,56 M€ (32.559.773 €) · 1 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 32.559.773 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,84 M€ (11.844.900 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | FOMENTO DE LA IGUALDAD DE OPORTUNIDADES ENTRE MUJERES Y HOMBRES | 7.325.860 | 61,8 % |
| `331M` | DIRECCIÓN Y SERVICIOS GENERALES DE UNIVERSIDADES, IGUALDAD, CULTURA Y DEPORTE | 4.519.040 | 38,2 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.293,18 M€ · 47 códigos · 36,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 480.802.000 |
| `140A` | MECANISMO DE RECUPERACIÓN Y RESILIENCIA (MRR) | 167.565.250 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 69.185.135 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 61.608.089 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 46.262.374 |
| `456B` | CALIDAD AMBIENTAL | 45.998.360 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 41.418.515 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 41.259.154 |
| `232A` | PROMOCIÓN Y SERVICIOS A LA JUVENTUD | 27.828.254 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 27.155.424 |
| `140B` | REACT-UE | 26.864.510 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCION EXTERIOR | 21.933.170 |
| `332A` | CENTROS CULTURALES | 17.792.028 |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA Y HACIENDA | 17.658.252 |
| `929N` | FONDO DE CONTINGENCIA DE EJECUCIÓN PRESUPUESTARIA | 14.200.000 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 13.119.141 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 11.529.690 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 11.345.235 |
| `134N` | EMERGENCIAS | 10.765.872 |
| `494M` | RELACIONES LABORALES | 10.321.858 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 10.051.979 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 9.645.669 |
| `134M` | PROTECCIÓN CIVIL | 9.543.801 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 9.044.602 |
| `929M` | IMPREVISTOS Y FUNCIONES NO CLASIFICADAS | 9.000.000 |
| … | *resto: 22 códigos* | 81.284.443 |

</details>

### 2024

*Fuente: `ingresos_gastos.pdf` · 89 líneas · total extraído **3.568,56 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.168,05 M€ (1.168.051.162 €) · 11 códigos · 32,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 1.081.053.293 | 92,6 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 27.333.781 | 2,3 % |
| `313A` | SALUD PÚBLICA | 17.263.165 | 1,5 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 9.953.030 | 0,9 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 8.436.477 | 0,7 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 7.852.121 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SALUD | 4.415.863 | 0,4 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 3.899.295 | 0,3 % |
| `311N` | PLANIFICACIÓN, ORDENACIÓN, GESTIÓN DEL CONOCIMIENTO Y SALUD DIGITAL | 3.822.217 | 0,3 % |
| `461C` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN SANITARIA | 2.129.000 | 0,2 % |
| `311P` | FARMACIA, HUMANIZACIÓN Y COORDINACIÓN SOCIOSANITARIA | 1.892.920 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 723,84 M€ (723.842.463 €) · 8 códigos · 20,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 402.809.446 | 55,6 % |
| `322A` | GESTIÓN DE CENTROS E INFRAESTRUCTURAS EDUCATIVAS | 179.064.552 | 24,7 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS | 90.684.033 | 12,5 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 32.058.230 | 4,4 % |
| `322C` | PROYECTO COMILLAS | 5.210.000 | 0,7 % |
| `321N` | DIRECCIÓN Y RECURSOS HUMANOS | 5.174.132 | 0,7 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 4.502.609 | 0,6 % |
| `421M` | DIRECCIÓN Y SERVICIOS GENERALES DE INDUSTRIA, EMPLEO, INNOVACIÓN Y COMERCIO | 4.339.461 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 17,98 M€ (17.980.803 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 17.980.803 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 7,07 M€ (7.068.889 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 7.068.889 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 30,84 M€ (30.836.033 €) · 4 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 21.601.340 | 70,1 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 4.140.382 | 13,4 % |
| `431A` | COMERCIO | 3.524.347 | 11,4 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.569.964 | 5,1 % |

</details>

<details open><summary><b><code>empleo</code> — 108,75 M€ (108.749.736 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 63.042.050 | 58,0 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 30.527.557 | 28,1 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 9.291.864 | 8,5 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.888.265 | 5,4 % |

</details>

<details open><summary><b><code>idi</code> — 49,60 M€ (49.604.154 €) · 5 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 35.529.984 | 71,6 % |
| `461B` | INVESTIGACIÓN Y POLÍTICA UNIVERSITARIA | 6.723.181 | 13,6 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.820.294 | 7,7 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 2.972.059 | 6,0 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 558.636 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 182,38 M€ (182.382.497 €) · 4 códigos · 5,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 175.715.491 | 96,3 % |
| `231E` | DEPENDENCIA, ATENCIÓN SOCIOSANITARIA Y SOLEDAD NO DESEADA | 3.458.306 | 1,9 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.689.500 | 0,9 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.519.200 | 0,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,48 M€ (14.475.355 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 14.475.355 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 30,15 M€ (30.145.610 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 25.466.443 | 84,5 % |
| `331M` | DIRECCIÓN Y SERVICIOS GENERALES DE CULTURA, TURISMO Y DEPORTE | 4.679.167 | 15,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,52 M€ (7.522.267 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | INCLUSIÓN SOCIAL, FAMILIAS E IGUALDAD | 7.522.267 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.227,90 M€ · 47 códigos · 34,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 417.937.000 |
| `140A` | MECANISMO DE RECUPERACIÓN Y RESILIENCIA (MRR) | 158.890.854 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 71.708.172 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 59.604.882 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCION EXTERIOR | 46.050.304 |
| `456B` | CALIDAD AMBIENTAL | 45.727.097 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 45.393.799 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 43.402.156 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 41.693.219 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 29.556.081 |
| `923M` | DIRECCIÓN Y SERVICIOS GENERALES DE ECONOMÍA, HACIENDA Y FONDOS EUROPEOS | 21.649.879 |
| `332A` | CENTROS CULTURALES | 18.285.288 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 16.128.002 |
| `494M` | RELACIONES LABORALES | 14.767.397 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 14.221.438 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 13.984.420 |
| `134N` | EMERGENCIAS | 12.686.630 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 12.328.258 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 10.341.186 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 10.316.176 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 10.302.805 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 10.277.417 |
| `134M` | SEGURIDAD Y PROTECCIÓN CIUDADANA | 9.984.230 |
| `323A` | CALIDAD Y EQUIDAD EDUCATIVA | 9.883.534 |
| `911M` | ACTIVIDAD LEGISLATIVA | 8.988.032 |
| … | *resto: 22 códigos* | 73.790.699 |

</details>

### 2025

*Fuente: `ingresos_gastos.pdf` · 88 líneas · total extraído **3.790,88 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.240,70 M€ (1.240.702.721 €) · 11 códigos · 32,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 1.134.341.707 | 91,4 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 31.072.964 | 2,5 % |
| `313A` | SALUD PÚBLICA | 19.395.168 | 1,6 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 16.120.825 | 1,3 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 10.908.574 | 0,9 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 8.540.503 | 0,7 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SALUD | 5.349.777 | 0,4 % |
| `461C` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN SANITARIA | 4.779.000 | 0,4 % |
| `311N` | PLANIFICACIÓN, ORDENACIÓN, GESTIÓN DEL CONOCIMIENTO Y SALUD DIGITAL | 4.264.858 | 0,3 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 3.921.447 | 0,3 % |
| `311P` | FARMACIA, HUMANIZACIÓN Y COORDINACIÓN SOCIOSANITARIA | 2.007.898 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 746,61 M€ (746.611.006 €) · 8 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 415.519.589 | 55,7 % |
| `322A` | GESTIÓN DE CENTROS E INFRAESTRUCTURAS EDUCATIVAS | 190.134.165 | 25,5 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS | 66.858.975 | 9,0 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 33.011.213 | 4,4 % |
| `322C` | PROYECTO COMILLAS | 26.885.437 | 3,6 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 5.024.456 | 0,7 % |
| `321N` | DIRECCIÓN Y RECURSOS HUMANOS | 4.814.535 | 0,6 % |
| `421M` | DIRECCIÓN Y SERVICIOS GENERALES DE INDUSTRIA, EMPLEO, INNOVACIÓN Y COMERCIO | 4.362.636 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 17,79 M€ (17.790.064 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 17.790.064 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 7,32 M€ (7.324.587 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 7.324.587 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 31,61 M€ (31.611.589 €) · 4 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 23.480.991 | 74,3 % |
| `431A` | COMERCIO | 4.030.926 | 12,8 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 2.490.454 | 7,9 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.609.218 | 5,1 % |

</details>

<details open><summary><b><code>empleo</code> — 112,75 M€ (112.749.736 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 61.218.508 | 54,3 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 35.691.923 | 31,7 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 10.413.568 | 9,2 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.425.737 | 4,8 % |

</details>

<details open><summary><b><code>idi</code> — 77,31 M€ (77.307.482 €) · 5 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 34.401.809 | 44,5 % |
| `461B` | INVESTIGACIÓN Y POLÍTICA UNIVERSITARIA | 34.101.822 | 44,1 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 4.265.497 | 5,5 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.969.355 | 5,1 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 568.999 | 0,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 191,34 M€ (191.340.914 €) · 4 códigos · 5,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 184.013.077 | 96,2 % |
| `231E` | DEPENDENCIA, ATENCIÓN SOCIOSANITARIA Y SOLEDAD NO DESEADA | 4.054.837 | 2,1 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.671.500 | 0,9 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.601.500 | 0,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 17,08 M€ (17.077.855 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 17.077.855 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,69 M€ (29.686.481 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 25.121.524 | 84,6 % |
| `331M` | DIRECCIÓN Y SERVICIOS GENERALES DE CULTURA, TURISMO Y DEPORTE | 4.564.957 | 15,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,69 M€ (7.690.961 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | INCLUSIÓN SOCIAL, FAMILIAS E IGUALDAD | 7.690.961 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.310,99 M€ · 46 códigos · 34,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 461.433.287 |
| `140A` | MECANISMO DE RECUPERACIÓN Y RESILIENCIA (MRR) | 155.528.398 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 78.388.124 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 67.785.035 |
| `456B` | CALIDAD AMBIENTAL | 55.629.400 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 47.150.292 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 47.034.633 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 43.205.067 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCIÓN EXTERIOR | 40.052.414 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 38.468.249 |
| `134M` | SEGURIDAD Y PROTECCIÓN CIUDADANA | 22.939.383 |
| `332A` | CENTROS CULTURALES | 20.233.504 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 17.543.669 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 16.820.293 |
| `494M` | RELACIONES LABORALES | 15.110.096 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 14.715.592 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 13.983.491 |
| `323A` | CALIDAD Y EQUIDAD EDUCATIVA | 13.602.960 |
| `134N` | EMERGENCIAS | 13.581.542 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 12.262.632 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 11.014.833 |
| `911M` | ACTIVIDAD LEGISLATIVA | 9.056.733 |
| `454A` | GESTIÓN E INFRAESTRUCTURA PORTUARIA | 8.956.120 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 8.819.456 |
| `413A` | DESARROLLO DE LA INDUSTRIALIZACIÓN, COMERCIALIZACIÓN Y COOPERACIÓN AGRARIA | 8.497.505 |
| … | *resto: 21 códigos* | 69.174.924 |

</details>

### 2026

*Fuente: `ingresos_gastos.pdf` · 91 líneas · total extraído **3.972,74 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.341,86 M€ (1.341.857.644 €) · 11 códigos · 33,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A` | ASISTENCIA SANITARIA | 1.225.951.460 | 91,4 % |
| `311O` | FORMACIÓN DE PERSONAL SANITARIO | 32.101.229 | 2,4 % |
| `313A` | SALUD PÚBLICA | 22.631.293 | 1,7 % |
| `461C` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN SANITARIA | 12.255.806 | 0,9 % |
| `412B` | REORIENTACIÓN, PROMOCIÓN Y DIVERSIFICACIÓN DE LA PRODUCCIÓN AGRARIA | 11.772.648 | 0,9 % |
| `412A` | ERRADICACIÓN, LUCHA Y CONTROL DE ENFERMEDADES | 10.583.331 | 0,8 % |
| `312M` | DIRECCIÓN Y SERVICIOS GENERALES DEL SERVICIO CÁNTABRO DE SALUD | 10.395.804 | 0,8 % |
| `311M` | DIRECCIÓN Y SERVICIOS GENERALES DE SALUD | 5.169.895 | 0,4 % |
| `311N` | PLANIFICACIÓN, ORDENACIÓN, GESTIÓN DEL CONOCIMIENTO Y SALUD DIGITAL | 4.814.589 | 0,4 % |
| `494N` | SEGURIDAD Y SALUD EN EL TRABAJO | 4.161.665 | 0,3 % |
| `311P` | FARMACIA, HUMANIZACIÓN Y COORDINACIÓN SOCIOSANITARIA | 2.019.924 | 0,2 % |

</details>

<details open><summary><b><code>educacion</code> — 793,19 M€ (793.193.442 €) · 8 códigos · 20,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `321O` | PERSONAL DOCENTE | 432.617.274 | 54,5 % |
| `322A` | GESTIÓN DE CENTROS E INFRAESTRUCTURAS EDUCATIVAS | 205.320.218 | 25,9 % |
| `322B` | ENSEÑANZAS UNIVERSITARIAS | 72.543.291 | 9,1 % |
| `422A` | APOYO Y ACTUACIONES ADMINISTRATIVAS EN LA INDUSTRIA | 41.323.547 | 5,2 % |
| `322C` | PROYECTO COMILLAS | 24.794.446 | 3,1 % |
| `324A` | FORMACIÓN PROFESIONAL Y EDUCACIÓN PERMANENTE | 6.913.569 | 0,9 % |
| `321N` | DIRECCIÓN Y RECURSOS HUMANOS | 5.290.138 | 0,7 % |
| `421M` | DIRECCIÓN Y SERVICIOS GENERALES DE INDUSTRIA, EMPLEO, INNOVACIÓN Y COMERCIO | 4.390.959 | 0,6 % |

</details>

<details open><summary><b><code>soberania</code> — 19,25 M€ (19.247.162 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `414A` | AYUDAS Y OTRAS ACTUACIONES PARA EL DESARROLLO RURAL | 19.247.162 | 100,0 % |

</details>

<details open><summary><b><code>direccion</code> — 7,56 M€ (7.555.911 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912M` | PRESIDENCIA DEL GOBIERNO DE CANTABRIA | 7.555.911 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 46,01 M€ (46.014.536 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A` | ACTUACIONES EN MATERIA DE VIVIENDA Y ARQUITECTURA | 36.435.161 | 79,2 % |
| `431A` | COMERCIO | 4.652.260 | 10,1 % |
| `261M` | ORDENACIÓN DEL TERRITORIO | 3.307.788 | 7,2 % |
| `261N` | PLANEAMIENTO URBANÍSTICO | 1.619.327 | 3,5 % |

</details>

<details open><summary><b><code>empleo</code> — 112,75 M€ (112.749.736 €) · 4 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241M` | PROMOCIÓN DEL EMPLEO Y LA INSERCIÓN LABORAL | 61.105.043 | 54,2 % |
| `241A` | FORMACIÓN E INSERCIÓN PROFESIONAL | 32.807.929 | 29,1 % |
| `241N` | INTERMEDIACIÓN LABORAL Y ORIENTACIÓN PROFESIONAL | 13.119.196 | 11,6 % |
| `241O` | PLANIFICACIÓN, GESTIÓN Y CONTROL | 5.717.568 | 5,1 % |

</details>

<details open><summary><b><code>idi</code> — 83,49 M€ (83.491.279 €) · 8 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `461A` | INNOVACIÓN, DESARROLLO TECNOLÓGICO Y EMPRENDIMIENTO INDUSTRIAL | 38.287.140 | 45,9 % |
| `461B` | INVESTIGACIÓN Y POLÍTICA UNIVERSITARIA | 34.541.207 | 41,4 % |
| `456D` | CENTRO DE INVESTIGACIÓN DEL MEDIO AMBIENTE | 3.939.959 | 4,7 % |
| `414B` | PROMOCIÓN DE LA INNOVACIÓN Y FORMACIÓN EN EL SECTOR AGRARIO | 3.247.969 | 3,9 % |
| `462A` | INNOVACIÓN Y CALIDAD DE LOS SERVICIOS | 1.185.226 | 1,4 % |
| `461F` | INVESTIGACIÓN, DESARROLLO Y MEDIO AMBIENTE | 1.094.778 | 1,3 % |
| `461E` | INVESTIGACIÓN, DESARROLLO E INNOVACIÓN DEL SECTOR AGRARIO | 695.000 | 0,8 % |
| `461G` | INNOVACIÓN DIGITAL EN MATERIA DE TURISMO | 500.000 | 0,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 211,63 M€ (211.628.366 €) · 4 códigos · 5,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B` | PROMOCIÓN DE LA AUTONOMÍA PERSONAL Y ATENCIÓN A LA DEPENDENCIA | 203.559.889 | 96,2 % |
| `231E` | DEPENDENCIA, ATENCIÓN SOCIOSANITARIA Y SOLEDAD NO DESEADA | 4.575.717 | 2,2 % |
| `232D` | FOMENTO DE LA NATALIDAD | 1.819.260 | 0,9 % |
| `231D` | ATENCIÓN A PERSONAS MAYORES | 1.673.500 | 0,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 19,25 M€ (19.250.355 €) · 1 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231C` | ATENCIÓN A LA INFANCIA, ADOLESCENCIA Y FAMILIA | 19.250.355 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,21 M€ (29.209.446 €) · 2 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A` | COORDINACIÓN Y PROMOCIÓN DEL TURISMO | 24.653.291 | 84,4 % |
| `331M` | DIRECCIÓN Y SERVICIOS GENERALES DE CULTURA, TURISMO Y DEPORTE | 4.556.155 | 15,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,26 M€ (8.259.262 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232B` | INCLUSIÓN SOCIAL, FAMILIAS E IGUALDAD | 8.259.262 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.300,28 M€ · 46 códigos · 32,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `951M` | DEUDA PÚBLICA | 447.055.000 |
| `140A` | MECANISMO DE RECUPERACIÓN Y RESILIENCIA (MRR) | 116.599.866 |
| `231A` | PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES | 81.538.518 |
| `453B` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA DE CARRETERAS AUTONÓMICAS | 70.207.287 |
| `456B` | CALIDAD AMBIENTAL | 54.825.043 |
| `452A` | GESTIÓN E INFRAESTRUCTURA HIDRÁULICA Y DE SANEAMIENTO | 50.314.125 |
| `112M` | ADMINISTRACIÓN DE JUSTICIA | 47.739.988 |
| `496M` | ACTUACIONES EN EL ÁMBITO LOCAL Y ACCIÓN EXTERIOR | 45.657.796 |
| `456C` | PROTECCIÓN DEL MEDIO NATURAL Y APROVECHAMIENTOS FORESTALES | 44.757.579 |
| `491M` | TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIONES | 35.301.498 |
| `332A` | CENTROS CULTURALES | 26.336.013 |
| `134M` | SEGURIDAD Y PROTECCIÓN CIUDADANA | 25.831.860 |
| `336A` | FOMENTO Y APOYO A LAS ACTIVIDADES DEPORTIVAS | 18.622.343 |
| `134N` | EMERGENCIAS | 18.273.639 |
| `453C` | ORDENACIÓN Y PROMOCIÓN DEL TRANSPORTE Y LAS TELECOMUNICACIONES | 16.195.996 |
| `323A` | CALIDAD Y EQUIDAD EDUCATIVA | 14.988.129 |
| `494M` | RELACIONES LABORALES | 14.855.381 |
| `932A` | APLICACIÓN SISTEMA TRIBUTARIO Y GESTIÓN DE INGRESOS PRESUPUESTARIOS | 14.717.364 |
| `453A` | ACTUACIONES EN MATERIA DE INFRAESTRUCTURA MUNICIPAL | 14.405.785 |
| `931O` | GESTIÓN DE TESORERÍA, PRESUPUESTOS Y POLÍTICA FINANCIERA | 14.399.537 |
| `334A` | GESTIÓN Y PROMOCIÓN CULTURAL | 12.830.104 |
| `415A` | DESARROLLO DE LOS SECTORES PESQUERO Y ALIMENTARIO | 12.132.604 |
| `911M` | ACTIVIDAD LEGISLATIVA | 9.327.289 |
| `921N` | DIRECCIÓN Y ORGANIZACIÓN DE LA FUNCIÓN PÚBLICA | 9.299.087 |
| `413A` | DESARROLLO DE LA INDUSTRIALIZACIÓN, COMERCIALIZACIÓN Y COOPERACIÓN AGRARIA | 8.619.114 |
| … | *resto: 21 códigos* | 75.448.043 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py cnt     # regenera este documento
python3 tools/auditoria_magnitud.py cnt        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa cnt --anio <año> \
    --input ../fuentes/raw/cnt/<año>/<fichero> --output /tmp/cnt.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-cnt.md`](limitaciones-cnt.md)

