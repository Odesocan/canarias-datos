# Trazabilidad de la extracción — Castilla y León (`cym`)

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
| **2015** | 104 | `bocyl_ley11_2014.pdf` | 13 | 61,5 % | 9.920,81 | — | no_aplica |
| **2016** | 103 | `gastos.csv` | 13 | 57,3 % | 9.843,70 | — | no_aplica |
| **2017** | 102 | `gastos.csv` | 13 | 57,8 % | 10.293,19 | — | no_aplica |
| **2018** | 102 | `gastos.csv` | 13 | 57,8 % | 10.859,22 | — | no_aplica |
| **2019** | 102 | `gastos.csv` | 13 | 57,8 % | 10.859,22 | sí | no_aplica |
| **2020** | 102 | `gastos.csv` | 13 | 57,8 % | 10.859,22 | sí | no_aplica |
| **2021** | 104 | `gastos.csv` | 13 | 56,7 % | 12.291,44 | — | no_aplica |
| **2022** | 104 | `gastos.csv` | 13 | 56,7 % | 12.291,44 | sí | no_aplica |
| **2023** | 107 | `gastos.xlsx` | 13 | 57,9 % | 13.809,84 | — | no_aplica |
| **2024** | 104 | `gastos.xlsx` | 13 | 57,7 % | 14.562,49 | — | no_aplica |
| **2025** | 103 | `gastos.bin` | 13 | 57,3 % | 14.562,49 | — | no_aplica |
| **2026** | 103 | `gastos.bin` | 13 | 57,3 % | 14.562,49 | — | no_aplica |

**URL(s) de origen:**
- <https://bocyl.jcyl.es/boletines/2014/12/29/pdf/BOCYL-D-29122014-2.pdf>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-1.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-2.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-3.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-4.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-5.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-6.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-7.csv>
- <https://datosabiertos.jcyl.es/web/jcyl/risp/es/hacienda/presupuestos/1284548037482-8.csv>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 3.252,49 | 3.285,03 | 3.446,72 | 3.544,93 | 3.544,93 | 3.544,93 | 4.316,97 | 4.316,97 | 4.690,05 | 4.812,77 | 4.812,77 | 4.812,77 |
| `educacion` | 2.094,97 | 2.015,50 | 2.172,39 | 2.145,64 | 2.145,64 | 2.145,64 | 2.452,59 | 2.452,59 | 2.735,04 | 2.865,00 | 2.865,00 | 2.865,00 |
| `soberania` | 1.443,88 | 1.318,54 | 1.346,49 | 1.382,18 | 1.382,18 | 1.382,18 | 1.419,45 | 1.419,45 | 1.460,96 | 1.497,09 | 1.497,09 | 1.497,09 |
| `direccion` | 1,10 | 1,10 | 1,03 | 0,99 | 0,99 | 0,99 | 1,65 | 1,65 | 3,09 | 3,37 | 1,84 | 1,84 |
| `vivienda` | 135,79 | 145,27 | 152,39 | 166,81 | 166,81 | 166,81 | 173,26 | 173,26 | 249,15 | 244,46 | 244,46 | 244,46 |
| `empleo` | 248,95 | 264,60 | 292,72 | 304,47 | 304,47 | 304,47 | 344,46 | 344,46 | 426,63 | 436,91 | 436,91 | 436,91 |
| `idi` | 178,46 | 166,95 | 224,63 | 242,18 | 242,18 | 242,18 | 303,24 | 303,24 | 438,44 | 379,19 | 379,19 | 379,19 |
| `dependencia` | 611,78 | 618,90 | 661,20 | 696,81 | 696,81 | 696,81 | 744,74 | 744,74 | 865,31 | 950,48 | 950,48 | 950,48 |
| `discapacidad` | 128,87 | 130,29 | 135,94 | 140,09 | 140,09 | 140,09 | 172,60 | 172,60 | 191,66 | 204,46 | 204,46 | 204,46 |
| `salud_mental` | 8,31 | 8,33 | 8,72 | 8,98 | 8,98 | 8,98 | 10,26 | 10,26 | 10,31 | 12,63 | 12,63 | 12,63 |
| `diversidad` | 5,60 | 5,73 | 5,82 | 5,95 | 5,95 | 5,95 | 7,05 | 7,05 | 8,48 | 9,01 | 9,01 | 9,01 |
| `turismo` | 38,97 | 22,46 | 23,98 | 25,34 | 25,34 | 25,34 | 29,88 | 29,88 | 85,24 | 61,33 | 61,33 | 61,33 |
| `igualdad` | 13,28 | 7,46 | 8,02 | 8,54 | 8,54 | 8,54 | 10,84 | 10,84 | 11,89 | 14,84 | 14,84 | 14,84 |
| **Σ asignado** | 8.162,44 | 7.990,16 | 8.480,05 | 8.672,91 | 8.672,91 | 8.672,91 | 9.986,97 | 9.986,97 | 11.176,22 | 11.491,54 | 11.490,01 | 11.490,01 |
| *(sin concepto)* | 1.758,37 | 1.853,54 | 1.813,13 | 2.186,31 | 2.186,31 | 2.186,31 | 2.304,47 | 2.304,47 | 2.633,62 | 3.070,95 | 3.072,49 | 3.072,49 |
| **TOTAL extraído** | 9.920,81 | 9.843,70 | 10.293,19 | 10.859,22 | 10.859,22 | 10.859,22 | 12.291,44 | 12.291,44 | 13.809,84 | 14.562,49 | 14.562,49 | 14.562,49 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +1,0 % | +4,9 % | +2,8 % | +0,0 % | +0,0 % | +21,8 % | +0,0 % | +8,6 % | +2,6 % | +0,0 % | +0,0 % |
| `educacion` | −3,8 % | +7,8 % | −1,2 % | +0,0 % | +0,0 % | +14,3 % | +0,0 % | +11,5 % | +4,8 % | +0,0 % | +0,0 % |
| `soberania` | −8,7 % | +2,1 % | +2,7 % | +0,0 % | +0,0 % | +2,7 % | +0,0 % | +2,9 % | +2,5 % | +0,0 % | +0,0 % |
| `direccion` | +0,2 % | −6,3 % | −4,3 % | +0,0 % | +0,0 % | +67,2 % ⚠ | +0,0 % | +87,2 % ⚠ | +9,1 % | −45,5 % ⚠ | +0,0 % |
| `vivienda` | +7,0 % | +4,9 % | +9,5 % | +0,0 % | +0,0 % | +3,9 % | +0,0 % | +43,8 % ⚠ | −1,9 % | +0,0 % | +0,0 % |
| `empleo` | +6,3 % | +10,6 % | +4,0 % | +0,0 % | +0,0 % | +13,1 % | +0,0 % | +23,9 % | +2,4 % | +0,0 % | +0,0 % |
| `idi` | −6,4 % | +34,5 % | +7,8 % | +0,0 % | +0,0 % | +25,2 % | +0,0 % | +44,6 % ⚠ | −13,5 % | +0,0 % | +0,0 % |
| `dependencia` | +1,2 % | +6,8 % | +5,4 % | +0,0 % | +0,0 % | +6,9 % | +0,0 % | +16,2 % | +9,8 % | +0,0 % | +0,0 % |
| `discapacidad` | +1,1 % | +4,3 % | +3,1 % | +0,0 % | +0,0 % | +23,2 % | +0,0 % | +11,0 % | +6,7 % | +0,0 % | +0,0 % |
| `salud_mental` | +0,1 % | +4,8 % | +2,9 % | +0,0 % | +0,0 % | +14,3 % | +0,0 % | +0,4 % | +22,6 % | +0,0 % | +0,0 % |
| `diversidad` | +2,3 % | +1,6 % | +2,3 % | +0,0 % | +0,0 % | +18,4 % | +0,0 % | +20,3 % | +6,3 % | +0,0 % | +0,0 % |
| `turismo` | −42,4 % ⚠ | +6,8 % | +5,7 % | +0,0 % | +0,0 % | +17,9 % | +0,0 % | +185,2 % ⚠ | −28,0 % | +0,0 % | +0,0 % |
| `igualdad` | −43,8 % ⚠ | +7,5 % | +6,5 % | +0,0 % | +0,0 % | +26,9 % | +0,0 % | +9,7 % | +24,9 % | +0,0 % | +0,0 % |
| **TOTAL** | −0,8 % | +4,6 % | +5,5 % | +0,0 % | +0,0 % | +13,2 % | +0,0 % | +12,4 % | +5,5 % | +0,0 % | +0,0 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2023 | `idi` | **SALTO** | 303,24 → 438,44 M€ (+44,6 % ⚠) |
| 2023 | `turismo` | **SALTO** | 29,88 → 85,24 M€ (+185,2 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 173,26 → 249,15 M€ (+43,8 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (4 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `456B01` | 64,98 | 2015:educacion, 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `231B01` | 61,89 | 2015:dependencia, 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `331A01` | 20,82 | 2015:turismo, 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |
| `231A01` | 6,14 | 2015:igualdad, 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:(sin concepto) |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `bocyl_ley11_2014.pdf` · 104 líneas · total extraído **9.920,81 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.252,49 M€ (3.252.486.438 €) · 7 códigos · 32,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | ATENCIÓN ESPECIALIZADA | 1.967.461.072 | 60,5 % |
| `312A01` | ATENCIÓN PRIMARIA | 1.057.250.504 | 32,5 % |
| `313B01` | SALUD PÚBLICA | 68.579.206 | 2,1 % |
| `312A03` | FORMACIÓN INTERNOS RESIDENTES | 56.507.758 | 1,7 % |
| `311B01` | ADMÓN. GENERAL DE LA GERENCIA REGIONAL DE SALUD | 44.490.075 | 1,4 % |
| `312A04` | EMERGENCIAS SANITARIAS | 39.522.562 | 1,2 % |
| `311A01` | DIRECCIÓN Y SERVICIOS GENERALES DE SANIDAD | 18.675.261 | 0,6 % |

</details>

<details open><summary><b><code>educacion</code> — 2.094,97 M€ (2.094.966.245 €) · 14 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | EDUC.SECUNDARIA,F.P.,EDUC.ESP.,ENS.ART.E IDIOMAS | 725.167.466 | 34,6 % |
| `322A01` | EDUCACIÓN INFANTIL Y PRIMARIA | 568.923.784 | 27,2 % |
| `322B01` | ENSEÑANZAS UNIVERSITARIAS | 329.881.313 | 15,7 % |
| `422A02` | COMPETITIVIDAD | 206.805.787 | 9,9 % |
| `322A04` | SERVICIOS COMPLEMENTARIOS A LA ENSEÑANZA | 84.108.422 | 4,0 % |
| `321A01` | DIRECCIÓN Y SERVICIOS GENERALES DE EDUCACIÓN | 43.171.584 | 2,1 % |
| `421A02` | ADM.Y SERV.GEN.AGENCIA INNOV.,FINANC.E INTERN.EMP. | 40.751.155 | 1,9 % |
| `322A05` | MEJORA CALIDAD ENSEÑANZA | 28.894.265 | 1,4 % |
| `322A03` | EDUC.COMPENSAT.,PERMAN.Y A DISTANCIA NO UNIVERSIT. | 26.692.807 | 1,3 % |
| `422A01` | CREACIÓN DE EMPRESAS | 17.388.734 | 0,8 % |
| `456B01` | PROTECCIÓN Y EDUCACIÓN AMBIENTAL | 11.665.082 | 0,6 % |
| `423A01` | APROVECHAMIENTO DE RECURSOS MINEROS | 5.195.466 | 0,2 % |
| `421A03` | INSPECCIÓN, NORMATIVA Y CALIDAD INDUSTRIAL | 3.839.399 | 0,2 % |
| `322C01` | ENSEÑANZA AGRARIA | 2.480.981 | 0,1 % |

</details>

<details open><summary><b><code>soberania</code> — 1.443,88 M€ (1.443.880.658 €) · 8 códigos · 14,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. REGULARIZACIÓN DE MERCADOS | 923.844.069 | 64,0 % |
| `412A01` | APOYO EMPRESA AGRARIA | 185.661.168 | 12,9 % |
| `413A01` | COMERCIALIZ.,INDUSTR.Y CONTROL CALIDAD AGROALIMENT | 155.290.407 | 10,8 % |
| `414A01` | REFORMA AGRARIA | 62.455.880 | 4,3 % |
| `412C01` | PRODUCCIÓN AGRARIA | 55.329.242 | 3,8 % |
| `411A01` | ADMINISTRACIÓN GENERAL AGRARIA | 47.666.828 | 3,3 % |
| `412B02` | GESTIÓN DE AYUDAS AGRARIAS DEL FEAGA | 8.604.736 | 0,6 % |
| `411A02` | ADMINIST.Y SERV. GEN.INSTITUTO TECNOLÓGICO AGRARIO | 5.028.328 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 1,10 M€ (1.098.791 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | PRESIDENCIA DE LA JUNTA | 1.098.791 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 135,79 M€ (135.785.844 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` | DIR. Y SERV.GENERALES DE FOMENTO Y MEDIO AMB. | 87.841.262 | 64,7 % |
| `261A02` | VIVIENDA | 30.088.467 | 22,2 % |
| `261A01` | ARQUITECTURA | 6.714.352 | 4,9 % |
| `431B01` | ORDENACIÓN Y PROMOCIÓN COMERCIAL | 5.331.811 | 3,9 % |
| `431A01` | INTERNACIONALIZACIÓN | 3.260.110 | 2,4 % |
| `261B01` | ORDENACIÓN DEL TERRITORIO Y URBANISMO | 2.549.842 | 1,9 % |

</details>

<details open><summary><b><code>empleo</code> — 248,95 M€ (248.945.164 €) · 8 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | FORMACIÓN OCUPACIONAL | 82.405.251 | 33,1 % |
| `241B01` | GESTIÓN DEL EMPLEO | 47.610.292 | 19,1 % |
| `241B04` | INTERMEDIACIÓN LABORAL | 26.317.460 | 10,6 % |
| `241C02` | SEGURIDAD Y SALUD LABORAL Y RELACIONES LABORALES | 25.710.124 | 10,3 % |
| `241C01` | ECONOMÍA SOCIAL Y DISCAPACITADOS | 25.322.581 | 10,2 % |
| `421A01` | DIR. Y SERV. GRALES.DE ECONOMÍA Y EMPLEO | 18.712.191 | 7,5 % |
| `241A01` | DIR. Y SERV. GEN. DEL SERVICIO PÚBLICO DE EMPLEO | 17.822.104 | 7,2 % |
| `241B03` | EMPLEO Y FORM.PERS.CON DISCAP.O RIESGO EXCL.SOCIAL | 5.045.161 | 2,0 % |

</details>

<details open><summary><b><code>idi</code> — 178,46 M€ (178.457.014 €) · 8 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` | INVESTIGAC.APLICADA Y DESARROLLO EN OTROS SECTORES | 59.478.621 | 33,3 % |
| `491A02` | PROMOCIÓN DE TELECOM. Y SOCIEDAD DE LA INFORMACIÓN | 44.941.038 | 25,2 % |
| `467B04` | INVESTIGACIÓN CIENTÍFICA O NO ORIENTADA | 27.664.403 | 15,5 % |
| `491A01` | TECNOLOGÍAS INFORMAC.Y COMUNICACIONES ADM. REG. | 19.059.829 | 10,7 % |
| `467B05` | INNOVACIÓN | 18.582.229 | 10,4 % |
| `467B02` | EFICIENCIA ENERGÉTICA Y ENERGÍAS RENOVABLES | 7.301.943 | 4,1 % |
| `467B06` | COORDINACIÓN EN CIENCIA Y TECNOLOGÍA | 765.691 | 0,4 % |
| `467B03` | ESTUDIOS E INVESTIG.ESTADÍSTICOS,ECONÓMICOS Y SOC. | 663.260 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 611,78 M€ (611.784.431 €) · 5 códigos · 6,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | SERVICIOS SOCIALES BÁSICOS E INTEGRACIÓN SOCIAL | 193.257.133 | 31,6 % |
| `212A01` | PENSIONES Y OTRAS PRESTACIONES ECONÓMICAS | 186.976.350 | 30,6 % |
| `231B04` | ATENCIÓN A PERSONAS MAYORES | 184.110.694 | 30,1 % |
| `231B01` | ADMINISTRACIÓN GENERAL DE SERVICIOS SOCIALES | 27.554.208 | 4,5 % |
| `231B06` | PROMOCIÓN Y APOYO A LA FAMILIA | 19.886.046 | 3,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 128,87 M€ (128.871.699 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | ATENCIÓN A PERSONAS CON DISCAPACIDAD | 128.871.699 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,31 M€ (8.314.980 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | INTERVENCIÓN EN DROGODEPENDENCIAS | 8.314.980 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,60 M€ (5.598.719 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | MIGRACIÓN Y COOPERACIÓN AL DESARROLLO | 5.598.719 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 38,97 M€ (38.973.762 €) · 2 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | ORDENACIÓN, PROMOCIÓN Y GESTIÓN DEL TURISMO | 22.502.178 | 57,7 % |
| `331A01` | DIRECCIÓN Y SERVICIOS GRALES. DE CULTURA Y TURISMO | 16.471.584 | 42,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 13,28 M€ (13.276.250 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | PROMOCIÓN Y APOYO A LA MUJER | 7.448.896 | 56,1 % |
| `231A01` | DIR.Y SERV.GEN.DE FAMILIA E IGUALDAD DE OPORTUNID. | 5.827.354 | 43,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.758,37 M€ · 40 códigos · 17,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | AMORTIZACIÓN Y GASTOS FINANCIEROS DEUDA COMUNIDAD | 1.079.035.956 |
| `453A01` | CARRETERAS Y FERROCARRILES | 160.769.453 |
| `456A01` | ORDENACIÓN Y MEJORA DEL MEDIO NATURAL | 98.877.944 |
| `941A02` | COOPERACIÓN ECONÓMICA LOCAL | 73.855.766 |
| `231B05` | ATENCIÓN A LA INFANCIA | 51.452.016 |
| `334A01` | PROMOCIÓN, FOMENTO Y APOYO A LA ACCIÓN CULTURAL | 44.061.088 |
| `923C01` | DIRECCIÓN Y SERVICIOS GENERALES DE HACIENDA | 39.850.200 |
| `931A03` | CONTROL INTERNO Y CONTABILIDAD PÚBLICA | 17.977.098 |
| `453A04` | PROMOCIÓN Y ORDENACIÓN DEL TRANSPORTE | 16.659.856 |
| `911A01` | ACTIVIDAD LEGISLATIVA | 16.421.564 |
| `452A01` | ABASTECIMIENTO Y SANEAMIENTO DE AGUAS | 14.865.062 |
| `337A01` | PROMOCIÓN, FOMENTO Y APOYO AL PATRIMONIO HISTÓRICO | 14.684.228 |
| `232A02` | PROMOCIÓN Y SERVICIOS A LA JUVENTUD | 14.281.797 |
| `921A01` | DIRECCIÓN Y SERVICIOS GENERALES DE PRESIDENCIA | 12.764.204 |
| `336A01` | FOMENTO Y APOYO A LA ACTIVIDAD DEPORTIVA | 12.453.212 |
| `131A01` | PROTECCIÓN CIVIL, POLICÍAS LOCALES E INTERIOR | 11.459.896 |
| `932A01` | TRIBUTOS Y FINANCIACIÓN AUTONÓMICA | 10.323.806 |
| `941A01` | DELEG. Y TRANSF. COMPETENCIAS A ENTIDADES LOCALES | 9.166.504 |
| `921B01` | DIRECCIÓN Y ADMINISTRACIÓN DE LA FUNCIÓN PÚBLICA | 8.675.634 |
| `921A02` | INSTALACIONES Y COBERTURA DE LOS SERVICIOS | 5.661.941 |
| `911B01` | CONTROL EXTERNO DEL SECTOR PÚBLICO | 4.435.407 |
| `924A01` | ELECCIONES A CORTES DE CASTILLA Y LEÓN | 4.154.392 |
| `492A01` | ORDENACIÓN, CONTROL E INFORMACIÓN SOBRE EL CONSUMO | 3.654.762 |
| `931A02` | PRESUPUESTAC. Y SEGUIMIENTO DE FONDOS COMUNITARIOS | 3.380.025 |
| `923A01` | GESTIÓN DEL PATRIMONIO Y EDIFICIOS ADMINISTRATIVOS | 3.208.686 |
| … | *resto: 15 códigos* | 26.241.264 |

</details>

### 2016

*Fuente: `gastos.csv` · 103 líneas · total extraído **9.843,70 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.285,03 M€ (3.285.027.920 €) · 7 códigos · 33,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` |  | 1.988.294.063 | 60,5 % |
| `312A01` |  | 1.065.489.593 | 32,4 % |
| `313B01` |  | 70.260.878 | 2,1 % |
| `312A03` |  | 57.339.062 | 1,7 % |
| `311B01` |  | 45.025.919 | 1,4 % |
| `312A04` |  | 40.133.729 | 1,2 % |
| `311A01` |  | 18.484.676 | 0,6 % |

</details>

<details open><summary><b><code>educacion</code> — 2.015,50 M€ (2.015.501.372 €) · 13 códigos · 20,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` |  | 754.364.855 | 37,4 % |
| `322A01` |  | 583.248.612 | 28,9 % |
| `322B01` |  | 352.031.720 | 17,5 % |
| `422A02` |  | 86.313.530 | 4,3 % |
| `322A04` |  | 81.596.614 | 4,0 % |
| `321A01` |  | 46.376.635 | 2,3 % |
| `322A05` |  | 27.567.086 | 1,4 % |
| `322A03` |  | 27.556.662 | 1,4 % |
| `421A02` |  | 23.425.683 | 1,2 % |
| `422A01` |  | 20.840.000 | 1,0 % |
| `423A01` |  | 5.048.706 | 0,3 % |
| `421A03` |  | 3.907.589 | 0,2 % |
| `322C01` |  | 3.223.680 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.318,54 M€ (1.318.536.495 €) · 8 códigos · 13,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` |  | 923.844.069 | 70,1 % |
| `412A01` |  | 151.559.678 | 11,5 % |
| `414A01` |  | 62.856.584 | 4,8 % |
| `412C01` |  | 60.987.111 | 4,6 % |
| `413A01` |  | 57.514.377 | 4,4 % |
| `411A01` |  | 47.771.536 | 3,6 % |
| `412B02` |  | 8.908.152 | 0,7 % |
| `411A02` |  | 5.094.988 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 1,10 M€ (1.100.523 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` |  | 1.100.523 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 145,27 M€ (145.271.044 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` |  | 90.627.348 | 62,4 % |
| `261A02` |  | 27.284.313 | 18,8 % |
| `431A01` |  | 10.000.000 | 6,9 % |
| `261A01` |  | 9.344.752 | 6,4 % |
| `431B01` |  | 5.604.694 | 3,9 % |
| `261B01` |  | 2.409.937 | 1,7 % |

</details>

<details open><summary><b><code>empleo</code> — 264,60 M€ (264.604.359 €) · 7 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` |  | 84.523.176 | 31,9 % |
| `241B01` |  | 55.551.485 | 21,0 % |
| `241B04` |  | 35.055.254 | 13,2 % |
| `241A01` |  | 30.899.731 | 11,7 % |
| `241C01` |  | 27.683.357 | 10,5 % |
| `241C02` |  | 24.855.916 | 9,4 % |
| `241B03` |  | 6.035.440 | 2,3 % |

</details>

<details open><summary><b><code>idi</code> — 166,95 M€ (166.951.996 €) · 8 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` |  | 67.911.270 | 40,7 % |
| `491A02` |  | 39.922.120 | 23,9 % |
| `467B04` |  | 22.584.012 | 13,5 % |
| `491A01` |  | 15.034.598 | 9,0 % |
| `467B02` |  | 10.216.487 | 6,1 % |
| `467B05` |  | 9.468.005 | 5,7 % |
| `467B06` |  | 1.052.244 | 0,6 % |
| `467B03` |  | 763.260 | 0,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 618,90 M€ (618.898.555 €) · 4 códigos · 6,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` |  | 208.838.382 | 33,7 % |
| `212A01` |  | 201.093.949 | 32,5 % |
| `231B04` |  | 188.341.168 | 30,4 % |
| `231B06` |  | 20.625.056 | 3,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 130,29 M€ (130.292.035 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` |  | 130.292.035 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,33 M€ (8.325.168 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` |  | 8.325.168 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,73 M€ (5.728.341 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` |  | 5.728.341 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 22,46 M€ (22.460.969 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` |  | 22.460.969 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,46 M€ (7.458.583 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` |  | 7.458.583 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.853,54 M€ · 44 códigos · 18,8 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` |  | 1.083.012.940 |
| `453A01` |  | 165.886.120 |
| `456A01` |  | 101.227.191 |
| `941A02` |  | 74.327.816 |
| `923C01` |  | 52.332.031 |
| `231B05` |  | 51.319.678 |
| `334A01` |  | 44.621.181 |
| `231B01` |  | 27.885.168 |
| `931A03` |  | 18.749.824 |
| `453A04` |  | 18.039.551 |
| `911A01` |  | 17.018.079 |
| `337A01` |  | 17.002.504 |
| `331A01` |  | 16.744.318 |
| `232A02` |  | 15.192.054 |
| `456B01` |  | 14.493.419 |
| `921A01` |  | 14.130.915 |
| `336A01` |  | 13.562.342 |
| `131A01` |  | 11.774.492 |
| `452A01` |  | 11.590.136 |
| `932A01` |  | 11.021.463 |
| `941A01` |  | 9.166.504 |
| `921B01` |  | 9.157.650 |
| `923A01` |  | 5.533.904 |
| `231A01` |  | 5.461.705 |
| `921A02` |  | 4.999.231 |
| … | *resto: 19 códigos* | 39.291.667 |

</details>

### 2017

*Fuente: `gastos.csv` · 102 líneas · total extraído **10.293,19 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.446,72 M€ (3.446.716.392 €) · 7 códigos · 33,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` |  | 2.062.337.300 | 59,8 % |
| `312A01` |  | 1.152.338.413 | 33,4 % |
| `313B01` |  | 71.557.075 | 2,1 % |
| `312A03` |  | 58.787.195 | 1,7 % |
| `311B01` |  | 41.585.522 | 1,2 % |
| `312A04` |  | 41.372.597 | 1,2 % |
| `311A01` |  | 18.738.290 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.172,39 M€ (2.172.387.431 €) · 13 códigos · 21,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` |  | 792.938.397 | 36,5 % |
| `322A01` |  | 595.091.290 | 27,4 % |
| `322B01` |  | 355.449.827 | 16,4 % |
| `422A02` |  | 173.104.325 | 8,0 % |
| `322A04` |  | 83.779.697 | 3,9 % |
| `321A01` |  | 44.551.954 | 2,1 % |
| `322A05` |  | 41.865.941 | 1,9 % |
| `322A03` |  | 27.330.580 | 1,3 % |
| `421A02` |  | 23.699.328 | 1,1 % |
| `422A01` |  | 20.861.812 | 1,0 % |
| `423A01` |  | 5.030.762 | 0,2 % |
| `421A03` |  | 4.573.842 | 0,2 % |
| `322C01` |  | 4.109.676 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.346,49 M€ (1.346.493.414 €) · 8 códigos · 13,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` |  | 923.844.069 | 68,6 % |
| `412A01` |  | 160.275.596 | 11,9 % |
| `413A01` |  | 71.707.161 | 5,3 % |
| `414A01` |  | 66.924.785 | 5,0 % |
| `412C01` |  | 62.863.224 | 4,7 % |
| `411A01` |  | 46.985.693 | 3,5 % |
| `412B02` |  | 8.773.266 | 0,7 % |
| `411A02` |  | 5.119.620 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 1,03 M€ (1.031.150 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` |  | 1.031.150 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 152,39 M€ (152.388.567 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` |  | 84.082.785 | 55,2 % |
| `261A02` |  | 34.733.591 | 22,8 % |
| `431A01` |  | 10.018.176 | 6,6 % |
| `261A01` |  | 9.419.717 | 6,2 % |
| `261B01` |  | 7.880.385 | 5,2 % |
| `431B01` |  | 6.253.913 | 4,1 % |

</details>

<details open><summary><b><code>empleo</code> — 292,72 M€ (292.720.497 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` |  | 92.275.256 | 31,5 % |
| `241B01` |  | 66.712.154 | 22,8 % |
| `241B04` |  | 41.487.519 | 14,2 % |
| `241C01` |  | 31.798.578 | 10,9 % |
| `241A01` |  | 31.258.657 | 10,7 % |
| `241C02` |  | 23.370.427 | 8,0 % |
| `241B03` |  | 5.817.906 | 2,0 % |

</details>

<details open><summary><b><code>idi</code> — 224,63 M€ (224.628.906 €) · 8 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` |  | 100.303.916 | 44,7 % |
| `491A02` |  | 63.509.819 | 28,3 % |
| `467B04` |  | 27.203.013 | 12,1 % |
| `491A01` |  | 15.085.058 | 6,7 % |
| `467B05` |  | 12.528.135 | 5,6 % |
| `467B02` |  | 4.310.169 | 1,9 % |
| `467B03` |  | 847.000 | 0,4 % |
| `467B06` |  | 841.796 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 661,20 M€ (661.201.402 €) · 4 códigos · 6,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` |  | 235.800.720 | 35,7 % |
| `212A01` |  | 208.584.886 | 31,5 % |
| `231B04` |  | 195.362.212 | 29,5 % |
| `231B06` |  | 21.453.584 | 3,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 135,94 M€ (135.944.676 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` |  | 135.944.676 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,72 M€ (8.722.181 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` |  | 8.722.181 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,82 M€ (5.818.726 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` |  | 5.818.726 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 23,98 M€ (23.983.830 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` |  | 23.983.830 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,02 M€ (8.015.947 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` |  | 8.015.947 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.813,13 M€ · 43 códigos · 17,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` |  | 1.018.801.455 |
| `453A01` |  | 165.882.121 |
| `456A01` |  | 110.746.781 |
| `941A02` |  | 77.735.686 |
| `231B05` |  | 53.639.301 |
| `923C01` |  | 49.310.509 |
| `334A01` |  | 45.718.859 |
| `231B01` |  | 28.371.663 |
| `911A01` |  | 19.390.419 |
| `337A01` |  | 19.163.404 |
| `931A03` |  | 18.365.280 |
| `453A04` |  | 17.681.385 |
| `331A01` |  | 16.473.914 |
| `232A02` |  | 15.722.732 |
| `456B01` |  | 14.884.952 |
| `336A01` |  | 14.466.227 |
| `921A01` |  | 14.183.635 |
| `131A01` |  | 11.964.970 |
| `921B01` |  | 10.740.370 |
| `452A01` |  | 10.573.487 |
| `932A01` |  | 10.559.791 |
| `941A01` |  | 9.192.995 |
| `923A01` |  | 7.325.424 |
| `425A01` |  | 6.521.825 |
| `231A01` |  | 5.287.374 |
| … | *resto: 18 códigos* | 40.428.680 |

</details>

### 2018

*Fuente: `gastos.csv` · 102 líneas · total extraído **10.859,22 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 3.544,93 M€ (3.544.930.466 €) · 7 códigos · 32,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` |  | 2.120.443.225 | 59,8 % |
| `312A01` |  | 1.188.572.593 | 33,5 % |
| `313B01` |  | 73.875.584 | 2,1 % |
| `312A03` |  | 59.672.183 | 1,7 % |
| `312A04` |  | 49.358.476 | 1,4 % |
| `311B01` |  | 34.627.718 | 1,0 % |
| `311A01` |  | 18.380.687 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.145,64 M€ (2.145.638.780 €) · 13 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` |  | 814.839.922 | 38,0 % |
| `322A01` |  | 603.746.621 | 28,1 % |
| `322B01` |  | 373.649.289 | 17,4 % |
| `422A02` |  | 83.461.063 | 3,9 % |
| `322A04` |  | 82.195.523 | 3,8 % |
| `322A05` |  | 47.946.715 | 2,2 % |
| `321A01` |  | 47.213.295 | 2,2 % |
| `322A03` |  | 27.084.339 | 1,3 % |
| `421A02` |  | 25.946.496 | 1,2 % |
| `422A01` |  | 20.998.131 | 1,0 % |
| `423A01` |  | 9.536.679 | 0,4 % |
| `322C01` |  | 4.576.481 | 0,2 % |
| `421A03` |  | 4.444.226 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.382,18 M€ (1.382.181.385 €) · 8 códigos · 12,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` |  | 924.421.069 | 66,9 % |
| `412A01` |  | 164.283.464 | 11,9 % |
| `414A01` |  | 84.335.891 | 6,1 % |
| `413A01` |  | 80.791.531 | 5,8 % |
| `412C01` |  | 67.659.889 | 4,9 % |
| `411A01` |  | 46.868.424 | 3,4 % |
| `412B02` |  | 8.636.511 | 0,6 % |
| `411A02` |  | 5.184.606 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,99 M€ (986.574 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` |  | 986.574 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 166,81 M€ (166.810.280 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` |  | 85.807.060 | 51,4 % |
| `261A02` |  | 41.498.504 | 24,9 % |
| `261A01` |  | 11.545.714 | 6,9 % |
| `261B01` |  | 10.636.191 | 6,4 % |
| `431A01` |  | 10.113.764 | 6,1 % |
| `431B01` |  | 7.209.047 | 4,3 % |

</details>

<details open><summary><b><code>empleo</code> — 304,47 M€ (304.469.214 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` |  | 98.192.599 | 32,3 % |
| `241B01` |  | 68.739.020 | 22,6 % |
| `241B04` |  | 41.064.682 | 13,5 % |
| `241A01` |  | 32.592.058 | 10,7 % |
| `241C01` |  | 32.505.073 | 10,7 % |
| `241C02` |  | 24.174.576 | 7,9 % |
| `241B03` |  | 7.201.206 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 242,18 M€ (242.182.633 €) · 8 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` |  | 81.761.899 | 33,8 % |
| `491A02` |  | 77.471.232 | 32,0 % |
| `467B04` |  | 40.662.291 | 16,8 % |
| `467B02` |  | 16.461.389 | 6,8 % |
| `491A01` |  | 15.520.040 | 6,4 % |
| `467B05` |  | 8.415.212 | 3,5 % |
| `467B06` |  | 1.103.570 | 0,5 % |
| `467B03` |  | 787.000 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 696,81 M€ (696.811.366 €) · 4 códigos · 6,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` |  | 262.822.986 | 37,7 % |
| `212A01` |  | 211.188.557 | 30,3 % |
| `231B04` |  | 199.362.143 | 28,6 % |
| `231B06` |  | 23.437.680 | 3,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 140,09 M€ (140.093.908 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` |  | 140.093.908 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,98 M€ (8.978.860 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` |  | 8.978.860 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,95 M€ (5.949.666 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` |  | 5.949.666 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,34 M€ (25.339.532 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` |  | 25.339.532 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,54 M€ (8.537.700 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` |  | 8.537.700 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.186,31 M€ · 43 códigos · 20,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` |  | 1.391.494.043 |
| `453A01` |  | 147.094.801 |
| `456A01` |  | 112.410.993 |
| `941A02` |  | 80.080.588 |
| `231B05` |  | 56.962.485 |
| `923C01` |  | 49.765.108 |
| `334A01` |  | 47.739.884 |
| `231B01` |  | 29.114.978 |
| `337A01` |  | 20.515.664 |
| `911A01` |  | 19.910.212 |
| `453A04` |  | 18.797.679 |
| `931A03` |  | 18.404.686 |
| `232A02` |  | 18.097.259 |
| `331A01` |  | 16.324.353 |
| `456B01` |  | 15.748.261 |
| `336A01` |  | 15.338.938 |
| `921A01` |  | 14.677.748 |
| `131A01` |  | 12.163.942 |
| `452A01` |  | 10.758.188 |
| `921B01` |  | 10.531.952 |
| `932A01` |  | 10.038.593 |
| `941A01` |  | 9.371.592 |
| `923A01` |  | 8.098.001 |
| `425A01` |  | 6.187.291 |
| `921A02` |  | 5.227.214 |
| … | *resto: 18 códigos* | 41.453.806 |

</details>

### 2019

*Fuente: `gastos.csv` · 102 líneas · total extraído **10.859,22 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 3.544,93 M€ (3.544.930.466 €) · 7 códigos · 32,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` |  | 2.120.443.225 | 59,8 % |
| `312A01` |  | 1.188.572.593 | 33,5 % |
| `313B01` |  | 73.875.584 | 2,1 % |
| `312A03` |  | 59.672.183 | 1,7 % |
| `312A04` |  | 49.358.476 | 1,4 % |
| `311B01` |  | 34.627.718 | 1,0 % |
| `311A01` |  | 18.380.687 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.145,64 M€ (2.145.638.780 €) · 13 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` |  | 814.839.922 | 38,0 % |
| `322A01` |  | 603.746.621 | 28,1 % |
| `322B01` |  | 373.649.289 | 17,4 % |
| `422A02` |  | 83.461.063 | 3,9 % |
| `322A04` |  | 82.195.523 | 3,8 % |
| `322A05` |  | 47.946.715 | 2,2 % |
| `321A01` |  | 47.213.295 | 2,2 % |
| `322A03` |  | 27.084.339 | 1,3 % |
| `421A02` |  | 25.946.496 | 1,2 % |
| `422A01` |  | 20.998.131 | 1,0 % |
| `423A01` |  | 9.536.679 | 0,4 % |
| `322C01` |  | 4.576.481 | 0,2 % |
| `421A03` |  | 4.444.226 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.382,18 M€ (1.382.181.385 €) · 8 códigos · 12,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` |  | 924.421.069 | 66,9 % |
| `412A01` |  | 164.283.464 | 11,9 % |
| `414A01` |  | 84.335.891 | 6,1 % |
| `413A01` |  | 80.791.531 | 5,8 % |
| `412C01` |  | 67.659.889 | 4,9 % |
| `411A01` |  | 46.868.424 | 3,4 % |
| `412B02` |  | 8.636.511 | 0,6 % |
| `411A02` |  | 5.184.606 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,99 M€ (986.574 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` |  | 986.574 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 166,81 M€ (166.810.280 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` |  | 85.807.060 | 51,4 % |
| `261A02` |  | 41.498.504 | 24,9 % |
| `261A01` |  | 11.545.714 | 6,9 % |
| `261B01` |  | 10.636.191 | 6,4 % |
| `431A01` |  | 10.113.764 | 6,1 % |
| `431B01` |  | 7.209.047 | 4,3 % |

</details>

<details open><summary><b><code>empleo</code> — 304,47 M€ (304.469.214 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` |  | 98.192.599 | 32,3 % |
| `241B01` |  | 68.739.020 | 22,6 % |
| `241B04` |  | 41.064.682 | 13,5 % |
| `241A01` |  | 32.592.058 | 10,7 % |
| `241C01` |  | 32.505.073 | 10,7 % |
| `241C02` |  | 24.174.576 | 7,9 % |
| `241B03` |  | 7.201.206 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 242,18 M€ (242.182.633 €) · 8 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` |  | 81.761.899 | 33,8 % |
| `491A02` |  | 77.471.232 | 32,0 % |
| `467B04` |  | 40.662.291 | 16,8 % |
| `467B02` |  | 16.461.389 | 6,8 % |
| `491A01` |  | 15.520.040 | 6,4 % |
| `467B05` |  | 8.415.212 | 3,5 % |
| `467B06` |  | 1.103.570 | 0,5 % |
| `467B03` |  | 787.000 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 696,81 M€ (696.811.366 €) · 4 códigos · 6,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` |  | 262.822.986 | 37,7 % |
| `212A01` |  | 211.188.557 | 30,3 % |
| `231B04` |  | 199.362.143 | 28,6 % |
| `231B06` |  | 23.437.680 | 3,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 140,09 M€ (140.093.908 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` |  | 140.093.908 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,98 M€ (8.978.860 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` |  | 8.978.860 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,95 M€ (5.949.666 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` |  | 5.949.666 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,34 M€ (25.339.532 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` |  | 25.339.532 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,54 M€ (8.537.700 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` |  | 8.537.700 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.186,31 M€ · 43 códigos · 20,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` |  | 1.391.494.043 |
| `453A01` |  | 147.094.801 |
| `456A01` |  | 112.410.993 |
| `941A02` |  | 80.080.588 |
| `231B05` |  | 56.962.485 |
| `923C01` |  | 49.765.108 |
| `334A01` |  | 47.739.884 |
| `231B01` |  | 29.114.978 |
| `337A01` |  | 20.515.664 |
| `911A01` |  | 19.910.212 |
| `453A04` |  | 18.797.679 |
| `931A03` |  | 18.404.686 |
| `232A02` |  | 18.097.259 |
| `331A01` |  | 16.324.353 |
| `456B01` |  | 15.748.261 |
| `336A01` |  | 15.338.938 |
| `921A01` |  | 14.677.748 |
| `131A01` |  | 12.163.942 |
| `452A01` |  | 10.758.188 |
| `921B01` |  | 10.531.952 |
| `932A01` |  | 10.038.593 |
| `941A01` |  | 9.371.592 |
| `923A01` |  | 8.098.001 |
| `425A01` |  | 6.187.291 |
| `921A02` |  | 5.227.214 |
| … | *resto: 18 códigos* | 41.453.806 |

</details>

### 2020

*Fuente: `gastos.csv` · 102 líneas · total extraído **10.859,22 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 3.544,93 M€ (3.544.930.466 €) · 7 códigos · 32,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` |  | 2.120.443.225 | 59,8 % |
| `312A01` |  | 1.188.572.593 | 33,5 % |
| `313B01` |  | 73.875.584 | 2,1 % |
| `312A03` |  | 59.672.183 | 1,7 % |
| `312A04` |  | 49.358.476 | 1,4 % |
| `311B01` |  | 34.627.718 | 1,0 % |
| `311A01` |  | 18.380.687 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.145,64 M€ (2.145.638.780 €) · 13 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` |  | 814.839.922 | 38,0 % |
| `322A01` |  | 603.746.621 | 28,1 % |
| `322B01` |  | 373.649.289 | 17,4 % |
| `422A02` |  | 83.461.063 | 3,9 % |
| `322A04` |  | 82.195.523 | 3,8 % |
| `322A05` |  | 47.946.715 | 2,2 % |
| `321A01` |  | 47.213.295 | 2,2 % |
| `322A03` |  | 27.084.339 | 1,3 % |
| `421A02` |  | 25.946.496 | 1,2 % |
| `422A01` |  | 20.998.131 | 1,0 % |
| `423A01` |  | 9.536.679 | 0,4 % |
| `322C01` |  | 4.576.481 | 0,2 % |
| `421A03` |  | 4.444.226 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.382,18 M€ (1.382.181.385 €) · 8 códigos · 12,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` |  | 924.421.069 | 66,9 % |
| `412A01` |  | 164.283.464 | 11,9 % |
| `414A01` |  | 84.335.891 | 6,1 % |
| `413A01` |  | 80.791.531 | 5,8 % |
| `412C01` |  | 67.659.889 | 4,9 % |
| `411A01` |  | 46.868.424 | 3,4 % |
| `412B02` |  | 8.636.511 | 0,6 % |
| `411A02` |  | 5.184.606 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 0,99 M€ (986.574 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` |  | 986.574 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 166,81 M€ (166.810.280 €) · 6 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` |  | 85.807.060 | 51,4 % |
| `261A02` |  | 41.498.504 | 24,9 % |
| `261A01` |  | 11.545.714 | 6,9 % |
| `261B01` |  | 10.636.191 | 6,4 % |
| `431A01` |  | 10.113.764 | 6,1 % |
| `431B01` |  | 7.209.047 | 4,3 % |

</details>

<details open><summary><b><code>empleo</code> — 304,47 M€ (304.469.214 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` |  | 98.192.599 | 32,3 % |
| `241B01` |  | 68.739.020 | 22,6 % |
| `241B04` |  | 41.064.682 | 13,5 % |
| `241A01` |  | 32.592.058 | 10,7 % |
| `241C01` |  | 32.505.073 | 10,7 % |
| `241C02` |  | 24.174.576 | 7,9 % |
| `241B03` |  | 7.201.206 | 2,4 % |

</details>

<details open><summary><b><code>idi</code> — 242,18 M€ (242.182.633 €) · 8 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `467B01` |  | 81.761.899 | 33,8 % |
| `491A02` |  | 77.471.232 | 32,0 % |
| `467B04` |  | 40.662.291 | 16,8 % |
| `467B02` |  | 16.461.389 | 6,8 % |
| `491A01` |  | 15.520.040 | 6,4 % |
| `467B05` |  | 8.415.212 | 3,5 % |
| `467B06` |  | 1.103.570 | 0,5 % |
| `467B03` |  | 787.000 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 696,81 M€ (696.811.366 €) · 4 códigos · 6,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` |  | 262.822.986 | 37,7 % |
| `212A01` |  | 211.188.557 | 30,3 % |
| `231B04` |  | 199.362.143 | 28,6 % |
| `231B06` |  | 23.437.680 | 3,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 140,09 M€ (140.093.908 €) · 1 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` |  | 140.093.908 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 8,98 M€ (8.978.860 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` |  | 8.978.860 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,95 M€ (5.949.666 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` |  | 5.949.666 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 25,34 M€ (25.339.532 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` |  | 25.339.532 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,54 M€ (8.537.700 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` |  | 8.537.700 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.186,31 M€ · 43 códigos · 20,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` |  | 1.391.494.043 |
| `453A01` |  | 147.094.801 |
| `456A01` |  | 112.410.993 |
| `941A02` |  | 80.080.588 |
| `231B05` |  | 56.962.485 |
| `923C01` |  | 49.765.108 |
| `334A01` |  | 47.739.884 |
| `231B01` |  | 29.114.978 |
| `337A01` |  | 20.515.664 |
| `911A01` |  | 19.910.212 |
| `453A04` |  | 18.797.679 |
| `931A03` |  | 18.404.686 |
| `232A02` |  | 18.097.259 |
| `331A01` |  | 16.324.353 |
| `456B01` |  | 15.748.261 |
| `336A01` |  | 15.338.938 |
| `921A01` |  | 14.677.748 |
| `131A01` |  | 12.163.942 |
| `452A01` |  | 10.758.188 |
| `921B01` |  | 10.531.952 |
| `932A01` |  | 10.038.593 |
| `941A01` |  | 9.371.592 |
| `923A01` |  | 8.098.001 |
| `425A01` |  | 6.187.291 |
| `921A02` |  | 5.227.214 |
| … | *resto: 18 códigos* | 41.453.806 |

</details>

### 2021

*Fuente: `gastos.csv` · 104 líneas · total extraído **12.291,44 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.316,97 M€ (4.316.967.631 €) · 7 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.621.352.094 | 60,7 % |
| `312A01` | Atención primaria | 1.419.427.617 | 32,9 % |
| `313B01` | Salud pública | 86.150.051 | 2,0 % |
| `312A03` | Formac. internos resident | 75.684.923 | 1,8 % |
| `312A04` | Emergencias sanitarias | 65.698.350 | 1,5 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 27.284.673 | 0,6 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 21.369.923 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.452,59 M€ (2.452.586.140 €) · 13 códigos · 20,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 974.365.757 | 39,7 % |
| `322A01` | Educ. infantil y primaria | 679.182.477 | 27,7 % |
| `322B01` | Enseñanzas universitarias | 412.214.325 | 16,8 % |
| `422A02` | Competitividad | 101.594.739 | 4,1 % |
| `322A04` | Serv.complement. enseñ. | 97.898.060 | 4,0 % |
| `321A01` | Dir.y Serv.Gen. Educación | 51.232.477 | 2,1 % |
| `322A05` | Mejora calidad enseñanza | 45.993.128 | 1,9 % |
| `322A03` | Educ.comp.perma.y a dist. | 26.019.238 | 1,1 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 25.459.550 | 1,0 % |
| `322C01` | Enseñanza agraria | 13.048.531 | 0,5 % |
| `423A01` | Aprovech.recursos mineros | 10.098.161 | 0,4 % |
| `422A01` | Creación de empresas | 8.752.500 | 0,4 % |
| `421A03` | Inspec.y calidad indust. | 6.727.197 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 1.419,45 M€ (1.419.449.800 €) · 8 códigos · 11,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 65,1 % |
| `412A01` | Apoyo empresa agraria | 181.162.988 | 12,8 % |
| `414A01` | Reforma agraria | 98.773.886 | 7,0 % |
| `413A01` | Comerc.indust.y cont.c.a. | 78.106.345 | 5,5 % |
| `412C01` | Producción agraria | 72.425.285 | 5,1 % |
| `411A01` | Adm.General Agraria | 48.868.277 | 3,4 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 9.952.855 | 0,7 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 5.739.095 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 1,65 M€ (1.649.097 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.649.097 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 173,26 M€ (173.261.426 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` | Dir.y S.G.Fomento y M.A. | 90.201.592 | 52,1 % |
| `261A02` | Vivienda | 42.869.998 | 24,7 % |
| `431B01` | Ordenac.y prom. comercial | 13.314.289 | 7,7 % |
| `261B01` | Ord.territ.y urbanismo | 11.521.239 | 6,6 % |
| `261A01` | Arquitectura | 9.535.308 | 5,5 % |
| `431A01` | Internacionalización | 5.819.000 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 344,46 M€ (344.456.453 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 106.159.143 | 30,8 % |
| `241B01` | Gestión del empleo | 66.931.552 | 19,4 % |
| `241A01` | Dir.y Serv.G.Empleo e Ind | 43.564.422 | 12,6 % |
| `241C02` | Seg.y salud lab.y rel.lab | 43.178.619 | 12,5 % |
| `241B04` | Intermediación laboral | 39.907.855 | 11,6 % |
| `241C01` | Econ.social y discapacit. | 34.602.838 | 10,0 % |
| `241B03` | Empl.y form.pers.discapac | 10.112.024 | 2,9 % |

</details>

<details open><summary><b><code>idi</code> — 303,24 M€ (303.237.083 €) · 8 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A02` | Prom.telecom.y soc.inform | 110.604.413 | 36,5 % |
| `467B01` | Invest.aplic.y desar.sect | 97.498.673 | 32,2 % |
| `467B04` | Invest.científ.o no orien | 52.076.131 | 17,2 % |
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 20.652.417 | 6,8 % |
| `467B05` | Innovación | 14.732.201 | 4,9 % |
| `467B02` | Efic.energ.y energ.renov. | 5.823.925 | 1,9 % |
| `467B03` | Estud.invest.estad.econ. | 935.753 | 0,3 % |
| `467B06` | Coord.ciencia y tecnolog. | 913.570 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 744,74 M€ (744.737.627 €) · 4 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e int.social | 319.871.092 | 43,0 % |
| `231B04` | Atencion personas mayores | 228.594.221 | 30,7 % |
| `212A01` | Pens.y otras presta.econo | 179.853.259 | 24,1 % |
| `231B06` | Promoción y apoyo familia | 16.419.055 | 2,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 172,60 M€ (172.600.101 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 172.600.101 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 10,26 M€ (10.261.322 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 10.261.322 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 7,05 M€ (7.047.038 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 7.047.038 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,88 M€ (29.882.122 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 29.882.122 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,84 M€ (10.835.846 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 10.835.846 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.304,47 M€ · 45 códigos · 18,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.423.378.499 |
| `456A01` | Ord.y mejora medio natur. | 139.147.717 |
| `453A01` | Carreteras y ferrocar. | 119.688.265 |
| `941A02` | Coop. Econ.Local | 105.413.941 |
| `231B05` | Atención a la infancia | 60.732.133 |
| `334A01` | Prom.fom.y ap.acc.cult. | 51.485.214 |
| `231B01` | Adm.Gen.serv.sociales | 45.149.962 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 43.468.964 |
| `337A01` | Prom.fom.y ap.patr.hist. | 24.102.443 |
| `932A01` | Tributos y finac.autonóm. | 22.747.376 |
| `911A01` | Actividad legislativa | 21.886.000 |
| `931A03` | Control int.y Contab.Púb. | 20.501.227 |
| `232A02` | Promoc. y serv. juventud | 19.896.979 |
| `331A01` | Dir.y Serv.G.de Cult.y T. | 19.025.569 |
| `453A04` | Promoc.y orden.transporte | 19.008.891 |
| `452A01` | Abastec.y saneam. aguas | 16.173.219 |
| `336A01` | Fom.y apoyo act.deportiva | 15.498.303 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 14.512.216 |
| `456B01` | Protec.y educac.ambiental | 13.792.579 |
| `921A01` | Dir.y Serv.G.Presidencia | 13.030.201 |
| `923A01` | Gest.Patrim.y edif.adm. | 9.461.185 |
| `941A01` | Deleg.y transf.comp.E.L. | 9.405.829 |
| `921B01` | Dir.y Adm.Función Pública | 9.224.568 |
| `425A01` | Infr.eléct.y ahorro energ | 7.953.356 |
| `921A02` | Inst.y cobert.servicios | 5.444.064 |
| … | *resto: 20 códigos* | 54.344.137 |

</details>

### 2022

*Fuente: `gastos.csv` · 104 líneas · total extraído **12.291,44 M€** (nominales) · PRÓRROGA*

<details open><summary><b><code>sanidad</code> — 4.316,97 M€ (4.316.967.631 €) · 7 códigos · 35,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.621.352.094 | 60,7 % |
| `312A01` | Atención primaria | 1.419.427.617 | 32,9 % |
| `313B01` | Salud pública | 86.150.051 | 2,0 % |
| `312A03` | Formac. internos resident | 75.684.923 | 1,8 % |
| `312A04` | Emergencias sanitarias | 65.698.350 | 1,5 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 27.284.673 | 0,6 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 21.369.923 | 0,5 % |

</details>

<details open><summary><b><code>educacion</code> — 2.452,59 M€ (2.452.586.140 €) · 13 códigos · 20,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 974.365.757 | 39,7 % |
| `322A01` | Educ. infantil y primaria | 679.182.477 | 27,7 % |
| `322B01` | Enseñanzas universitarias | 412.214.325 | 16,8 % |
| `422A02` | Competitividad | 101.594.739 | 4,1 % |
| `322A04` | Serv.complement. enseñ. | 97.898.060 | 4,0 % |
| `321A01` | Dir.y Serv.Gen. Educación | 51.232.477 | 2,1 % |
| `322A05` | Mejora calidad enseñanza | 45.993.128 | 1,9 % |
| `322A03` | Educ.comp.perma.y a dist. | 26.019.238 | 1,1 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 25.459.550 | 1,0 % |
| `322C01` | Enseñanza agraria | 13.048.531 | 0,5 % |
| `423A01` | Aprovech.recursos mineros | 10.098.161 | 0,4 % |
| `422A01` | Creación de empresas | 8.752.500 | 0,4 % |
| `421A03` | Inspec.y calidad indust. | 6.727.197 | 0,3 % |

</details>

<details open><summary><b><code>soberania</code> — 1.419,45 M€ (1.419.449.800 €) · 8 códigos · 11,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 65,1 % |
| `412A01` | Apoyo empresa agraria | 181.162.988 | 12,8 % |
| `414A01` | Reforma agraria | 98.773.886 | 7,0 % |
| `413A01` | Comerc.indust.y cont.c.a. | 78.106.345 | 5,5 % |
| `412C01` | Producción agraria | 72.425.285 | 5,1 % |
| `411A01` | Adm.General Agraria | 48.868.277 | 3,4 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 9.952.855 | 0,7 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 5.739.095 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 1,65 M€ (1.649.097 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.649.097 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 173,26 M€ (173.261.426 €) · 6 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A01` | Dir.y S.G.Fomento y M.A. | 90.201.592 | 52,1 % |
| `261A02` | Vivienda | 42.869.998 | 24,7 % |
| `431B01` | Ordenac.y prom. comercial | 13.314.289 | 7,7 % |
| `261B01` | Ord.territ.y urbanismo | 11.521.239 | 6,6 % |
| `261A01` | Arquitectura | 9.535.308 | 5,5 % |
| `431A01` | Internacionalización | 5.819.000 | 3,4 % |

</details>

<details open><summary><b><code>empleo</code> — 344,46 M€ (344.456.453 €) · 7 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 106.159.143 | 30,8 % |
| `241B01` | Gestión del empleo | 66.931.552 | 19,4 % |
| `241A01` | Dir.y Serv.G.Empleo e Ind | 43.564.422 | 12,6 % |
| `241C02` | Seg.y salud lab.y rel.lab | 43.178.619 | 12,5 % |
| `241B04` | Intermediación laboral | 39.907.855 | 11,6 % |
| `241C01` | Econ.social y discapacit. | 34.602.838 | 10,0 % |
| `241B03` | Empl.y form.pers.discapac | 10.112.024 | 2,9 % |

</details>

<details open><summary><b><code>idi</code> — 303,24 M€ (303.237.083 €) · 8 códigos · 2,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A02` | Prom.telecom.y soc.inform | 110.604.413 | 36,5 % |
| `467B01` | Invest.aplic.y desar.sect | 97.498.673 | 32,2 % |
| `467B04` | Invest.científ.o no orien | 52.076.131 | 17,2 % |
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 20.652.417 | 6,8 % |
| `467B05` | Innovación | 14.732.201 | 4,9 % |
| `467B02` | Efic.energ.y energ.renov. | 5.823.925 | 1,9 % |
| `467B03` | Estud.invest.estad.econ. | 935.753 | 0,3 % |
| `467B06` | Coord.ciencia y tecnolog. | 913.570 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 744,74 M€ (744.737.627 €) · 4 códigos · 6,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e int.social | 319.871.092 | 43,0 % |
| `231B04` | Atencion personas mayores | 228.594.221 | 30,7 % |
| `212A01` | Pens.y otras presta.econo | 179.853.259 | 24,1 % |
| `231B06` | Promoción y apoyo familia | 16.419.055 | 2,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 172,60 M€ (172.600.101 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 172.600.101 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 10,26 M€ (10.261.322 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 10.261.322 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 7,05 M€ (7.047.038 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 7.047.038 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 29,88 M€ (29.882.122 €) · 1 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 29.882.122 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 10,84 M€ (10.835.846 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 10.835.846 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.304,47 M€ · 45 códigos · 18,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.423.378.499 |
| `456A01` | Ord.y mejora medio natur. | 139.147.717 |
| `453A01` | Carreteras y ferrocar. | 119.688.265 |
| `941A02` | Coop. Econ.Local | 105.413.941 |
| `231B05` | Atención a la infancia | 60.732.133 |
| `334A01` | Prom.fom.y ap.acc.cult. | 51.485.214 |
| `231B01` | Adm.Gen.serv.sociales | 45.149.962 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 43.468.964 |
| `337A01` | Prom.fom.y ap.patr.hist. | 24.102.443 |
| `932A01` | Tributos y finac.autonóm. | 22.747.376 |
| `911A01` | Actividad legislativa | 21.886.000 |
| `931A03` | Control int.y Contab.Púb. | 20.501.227 |
| `232A02` | Promoc. y serv. juventud | 19.896.979 |
| `331A01` | Dir.y Serv.G.de Cult.y T. | 19.025.569 |
| `453A04` | Promoc.y orden.transporte | 19.008.891 |
| `452A01` | Abastec.y saneam. aguas | 16.173.219 |
| `336A01` | Fom.y apoyo act.deportiva | 15.498.303 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 14.512.216 |
| `456B01` | Protec.y educac.ambiental | 13.792.579 |
| `921A01` | Dir.y Serv.G.Presidencia | 13.030.201 |
| `923A01` | Gest.Patrim.y edif.adm. | 9.461.185 |
| `941A01` | Deleg.y transf.comp.E.L. | 9.405.829 |
| `921B01` | Dir.y Adm.Función Pública | 9.224.568 |
| `425A01` | Infr.eléct.y ahorro energ | 7.953.356 |
| `921A02` | Inst.y cobert.servicios | 5.444.064 |
| … | *resto: 20 códigos* | 54.344.137 |

</details>

### 2023

*Fuente: `gastos.xlsx` · 107 líneas · total extraído **13.809,84 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.690,05 M€ (4.690.046.743 €) · 8 códigos · 34,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.783.174.370 | 59,3 % |
| `312A01` | Atención primaria | 1.538.336.277 | 32,8 % |
| `313B01` | Salud pública | 107.408.236 | 2,3 % |
| `312A04` | Emergencias sanitarias | 106.188.232 | 2,3 % |
| `312A03` | Formac. internos resident | 97.377.311 | 2,1 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 28.967.310 | 0,6 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 26.529.306 | 0,6 % |
| `313A01` | Planific. y desarrollo | 2.065.701 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.735,04 M€ (2.735.035.519 €) · 13 códigos · 19,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 1.090.549.910 | 39,9 % |
| `322A01` | Educ. infantil y primaria | 768.113.135 | 28,1 % |
| `322B01` | Enseñanzas universitarias | 433.601.659 | 15,9 % |
| `422A02` | Competitividad | 133.557.548 | 4,9 % |
| `322A04` | Serv.complement. enseñ. | 97.171.497 | 3,6 % |
| `321A01` | Dir.y Serv.Gen. Educación | 57.117.206 | 2,1 % |
| `322A05` | Mejora calidad enseñanza | 49.303.016 | 1,8 % |
| `322A03` | Educ.comp.perma.y a dist. | 28.494.824 | 1,0 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 26.338.072 | 1,0 % |
| `422A01` | Creación de empresas | 16.313.003 | 0,6 % |
| `322C01` | Enseñanza agraria | 14.512.603 | 0,5 % |
| `421A03` | Inspec.y calidad indust. | 10.111.582 | 0,4 % |
| `423A01` | Aprovech.recursos mineros | 9.851.464 | 0,4 % |

</details>

<details open><summary><b><code>soberania</code> — 1.460,96 M€ (1.460.955.044 €) · 8 códigos · 10,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 63,3 % |
| `412A01` | Apoyo empresa agraria | 207.690.937 | 14,2 % |
| `414A01` | Reforma agraria | 110.436.539 | 7,6 % |
| `412C01` | Producción agraria | 79.793.087 | 5,5 % |
| `413A01` | Comerc.indust.y cont.c.a. | 66.943.701 | 4,6 % |
| `411A01` | Adm.General Agraria | 52.737.816 | 3,6 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 10.290.443 | 0,7 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 8.641.452 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 3,09 M€ (3.087.311 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.652.437 | 53,5 % |
| `912A02` | Vicepresidencia Junta | 1.434.874 | 46,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 249,15 M€ (249.148.898 €) · 7 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `261A02` | Vivienda | 94.236.121 | 37,8 % |
| `451B01` | Dir.y Serv.G.M.A,Viv.O.T. | 82.699.869 | 33,2 % |
| `451A02` | Dir.y Serv.G.Movil.y T.D. | 21.480.968 | 8,6 % |
| `431B01` | Ordenac.y prom. comercial | 15.826.846 | 6,4 % |
| `261A01` | Arquitectura | 15.082.849 | 6,1 % |
| `261B01` | Ord.territ.y urbanismo | 13.903.245 | 5,6 % |
| `431A01` | Internacionalización | 5.919.000 | 2,4 % |

</details>

<details open><summary><b><code>empleo</code> — 426,63 M€ (426.628.015 €) · 7 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 167.768.182 | 39,3 % |
| `241B01` | Gestión del empleo | 85.457.744 | 20,0 % |
| `241A01` | Dir.y Serv.G.Ind.Com.Empl | 51.166.117 | 12,0 % |
| `241C01` | Econ.social y discapacit. | 49.516.828 | 11,6 % |
| `241B04` | Intermediación laboral | 30.405.365 | 7,1 % |
| `241C02` | Seg.y salud lab.y rel.lab | 26.351.445 | 6,2 % |
| `241B03` | Empl.y form.pers.discapac | 15.962.334 | 3,7 % |

</details>

<details open><summary><b><code>idi</code> — 438,44 M€ (438.440.387 €) · 8 códigos · 3,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A02` | Prom.telecom.y soc.inform | 173.380.072 | 39,5 % |
| `467B01` | Invest.aplic.y desar.sect | 112.684.351 | 25,7 % |
| `467B02` | Efic.energ.y energ.renov. | 57.304.159 | 13,1 % |
| `467B04` | Invest.científ.o no orien | 45.994.392 | 10,5 % |
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 30.823.863 | 7,0 % |
| `467B05` | Innovación | 16.339.980 | 3,7 % |
| `467B03` | Estud.invest.estad.econ. | 1.000.000 | 0,2 % |
| `467B06` | Coord.ciencia y tecnolog. | 913.570 | 0,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 865,31 M€ (865.314.063 €) · 4 códigos · 6,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e int.social | 392.850.090 | 45,4 % |
| `231B04` | Atencion personas mayores | 275.354.210 | 31,8 % |
| `212A01` | Pens.y otras presta.econo | 146.369.277 | 16,9 % |
| `231B06` | Promoción y apoyo familia | 50.740.486 | 5,9 % |

</details>

<details open><summary><b><code>discapacidad</code> — 191,66 M€ (191.657.715 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 191.657.715 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 10,31 M€ (10.306.603 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 10.306.603 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 8,48 M€ (8.476.266 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 8.476.266 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 85,24 M€ (85.235.574 €) · 1 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 85.235.574 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 11,89 M€ (11.886.698 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 11.886.698 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.633,62 M€ · 45 códigos · 19,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.469.363.540 |
| `456A01` | Ord.y mejora medio natur. | 186.242.303 |
| `453A01` | Carreteras y ferrocar. | 127.499.246 |
| `941A02` | Coop. Econ.Local | 111.368.463 |
| `231B05` | Atención a la infancia | 76.079.853 |
| `456B01` | Protec.y educac.ambiental | 64.984.316 |
| `231B01` | Adm.Gen.serv.sociales | 60.762.579 |
| `334A01` | Prom.fom.y ap.acc.cult. | 56.014.506 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 50.954.140 |
| `425A01` | Infr.eléct.y ahorro energ | 42.674.922 |
| `453A04` | Promoc.y orden.transporte | 40.211.199 |
| `452A01` | Abastec.y saneam. aguas | 31.387.180 |
| `337A01` | Prom.fom.y ap.patr.cult. | 27.686.189 |
| `232A02` | Promoc. y serv. juventud | 23.966.892 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 23.835.269 |
| `932A01` | Tributos y finac.autonóm. | 23.725.114 |
| `911A01` | Actividad legislativa | 23.039.160 |
| `931A03` | Control int.y Contab.Púb. | 22.372.244 |
| `336A01` | Fom.y apoyo act.deportiva | 21.773.310 |
| `331A01` | Dir.y Serv.G.Cult.Tur.Dep | 20.819.883 |
| `921A01` | Dir.y Serv.G.Presidencia | 19.368.793 |
| `453A03` | Infraest.compl.transporte | 15.163.494 |
| `923A01` | Gest.Patrim.y edif.adm. | 13.979.056 |
| `941A01` | Deleg.y transf.comp.E.L. | 9.996.643 |
| `921B01` | Dir.y Adm.Función Pública | 9.240.469 |
| … | *resto: 20 códigos* | 61.109.292 |

</details>

### 2024

*Fuente: `gastos.xlsx` · 104 líneas · total extraído **14.562,49 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.812,77 M€ (4.812.765.002 €) · 8 códigos · 33,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.848.775.970 | 59,2 % |
| `312A01` | Atención primaria | 1.554.905.872 | 32,3 % |
| `312A03` | Formac. internos resident | 126.973.760 | 2,6 % |
| `312A04` | Emergencias sanitarias | 111.722.998 | 2,3 % |
| `313B01` | Salud pública | 110.298.777 | 2,3 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 31.539.763 | 0,7 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 27.233.007 | 0,6 % |
| `313A01` | Planific. y desarrollo | 1.314.855 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.865,00 M€ (2.865.004.829 €) · 13 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 1.175.949.339 | 41,0 % |
| `322A01` | Educ. infantil y primaria | 809.343.181 | 28,2 % |
| `322B01` | Enseñanzas universitarias | 459.014.382 | 16,0 % |
| `422A02` | Competitividad | 128.943.101 | 4,5 % |
| `322A04` | Serv.complement. enseñ. | 97.223.237 | 3,4 % |
| `321A01` | Dir.y Serv.Gen. Educación | 57.937.478 | 2,0 % |
| `322A05` | Mejora calidad enseñanza | 50.545.473 | 1,8 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 27.106.209 | 0,9 % |
| `322A03` | Educ.comp.perma.y a dist. | 23.801.616 | 0,8 % |
| `322C01` | Enseñanza agraria | 14.834.296 | 0,5 % |
| `421A03` | Inspec.y calidad indust. | 10.344.720 | 0,4 % |
| `422A01` | Creación de empresas | 5.606.000 | 0,2 % |
| `423A01` | Aprovech.recursos mineros | 4.355.797 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.497,09 M€ (1.497.089.801 €) · 8 códigos · 10,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 61,7 % |
| `412A01` | Apoyo empresa agraria | 230.545.953 | 15,4 % |
| `414A01` | Reforma agraria | 112.556.091 | 7,5 % |
| `412C01` | Producción agraria | 83.254.419 | 5,6 % |
| `413A01` | Comerc.indust.y cont.c.a. | 72.755.794 | 4,9 % |
| `411A01` | Adm.General Agraria | 52.887.940 | 3,5 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 11.717.916 | 0,8 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 8.950.619 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 3,37 M€ (3.368.729 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.836.823 | 54,5 % |
| `912A02` | Vicepresidencia Junta | 1.531.906 | 45,5 % |

</details>

<details open><summary><b><code>vivienda</code> — 244,46 M€ (244.456.073 €) · 7 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451B01` | Dir.y Serv.G.M.A,Viv.O.T. | 89.748.087 | 36,7 % |
| `261A02` | Vivienda | 79.683.141 | 32,6 % |
| `451A02` | Dir.y Serv.G.Movil.y T.D. | 21.641.462 | 8,9 % |
| `261A01` | Arquitectura | 18.201.669 | 7,4 % |
| `261B01` | Ord.territ.y urbanismo | 14.294.190 | 5,8 % |
| `431B01` | Ordenac.y prom. comercial | 13.693.678 | 5,6 % |
| `431A01` | Internacionalización | 7.193.846 | 2,9 % |

</details>

<details open><summary><b><code>empleo</code> — 436,91 M€ (436.913.059 €) · 7 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 173.612.519 | 39,7 % |
| `241B01` | Gestión del empleo | 95.401.886 | 21,8 % |
| `241C01` | Econ.social y discapacit. | 49.229.527 | 11,3 % |
| `241A01` | Dir.y Serv.G.Ind.Com.Empl | 48.774.419 | 11,2 % |
| `241B04` | Intermediación laboral | 30.017.586 | 6,9 % |
| `241C02` | Seg.y salud lab.y rel.lab | 25.146.788 | 5,8 % |
| `241B03` | Empl.y form.pers.discapac | 14.730.334 | 3,4 % |

</details>

<details open><summary><b><code>idi</code> — 379,19 M€ (379.187.952 €) · 6 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 120.753.211 | 31,8 % |
| `467B01` | Invest.aplic.y desar.sect | 104.264.166 | 27,5 % |
| `491A02` | Prom.telecom.y soc.inform | 48.396.872 | 12,8 % |
| `467B02` | Efic.energ.y energ.renov. | 47.809.049 | 12,6 % |
| `467B04` | Invest.científ.o no orien | 42.566.586 | 11,2 % |
| `467B05` | Innovación | 15.398.068 | 4,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 950,48 M€ (950.482.061 €) · 4 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e int.social | 422.891.149 | 44,5 % |
| `231B04` | Atencion personas mayores | 309.370.047 | 32,5 % |
| `212A01` | Pens.y otras presta.econo | 166.124.339 | 17,5 % |
| `231B06` | Promoción y apoyo familia | 52.096.526 | 5,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 204,46 M€ (204.458.058 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 204.458.058 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 12,63 M€ (12.633.520 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 12.633.520 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,01 M€ (9.008.511 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 9.008.511 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 61,33 M€ (61.329.866 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 61.329.866 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,84 M€ (14.842.204 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 14.842.204 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.070,95 M€ · 44 códigos · 21,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.784.512.335 |
| `456A01` | Mejora medio natural | 249.224.473 |
| `453A01` | Carreteras y ferrocar. | 140.560.527 |
| `941A02` | Coop. Econ.Local | 116.483.148 |
| `231B05` | Atención a la infancia | 77.135.533 |
| `231B01` | Adm.Gen.serv.sociales | 61.889.487 |
| `334A01` | Prom.fom.y ap.acc.cult. | 56.890.571 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 54.243.821 |
| `456B01` | Protec.y educac.ambiental | 52.408.097 |
| `425A01` | Infr.eléct.y ahorro energ | 52.272.417 |
| `337A01` | Prom.fom.y ap.patr.cult. | 49.612.092 |
| `453A04` | Promoc.y orden.transporte | 45.248.436 |
| `453A03` | Infraest.compl.transporte | 27.270.691 |
| `336A01` | Fom.y apoyo act.deportiva | 25.763.203 |
| `232A02` | Promoc. y serv. juventud | 23.700.343 |
| `911A01` | Actividad legislativa | 23.491.070 |
| `932A01` | Tributos y finac.autonóm. | 23.256.572 |
| `452A01` | Abastec.y saneam. aguas | 23.200.336 |
| `931A03` | Control int.y Contab.Púb. | 22.785.431 |
| `921A01` | Dir.y Serv.G.Presidencia | 21.541.538 |
| `331A01` | Dir.y Serv.G.Cult.Tur.Dep | 20.553.664 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 19.032.513 |
| `923A01` | Gest.Patrim.y edif.adm. | 17.197.204 |
| `921B01` | Dir.y Adm.Función Pública | 11.279.333 |
| `941A01` | Deleg.y transf.comp.E.L. | 10.549.380 |
| … | *resto: 19 códigos* | 60.852.237 |

</details>

### 2025

*Fuente: `gastos.bin` · 103 líneas · total extraído **14.562,49 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.812,77 M€ (4.812.765.002 €) · 8 códigos · 33,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.848.775.970 | 59,2 % |
| `312A01` | Atención primaria | 1.554.905.872 | 32,3 % |
| `312A03` | Formac. internos resident | 126.973.760 | 2,6 % |
| `312A04` | Emergencias sanitarias | 111.722.998 | 2,3 % |
| `313B01` | Salud pública | 110.298.777 | 2,3 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 31.539.763 | 0,7 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 27.233.007 | 0,6 % |
| `313A01` | Planific. y desarrollo | 1.314.855 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.865,00 M€ (2.865.004.829 €) · 13 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 1.175.949.339 | 41,0 % |
| `322A01` | Educ. infantil y primaria | 809.343.181 | 28,2 % |
| `322B01` | Enseñanzas universitarias | 459.014.382 | 16,0 % |
| `422A02` | Competitividad | 128.943.101 | 4,5 % |
| `322A04` | Serv.complement. enseñ. | 97.223.237 | 3,4 % |
| `321A01` | Dir.y Serv.Gen. Educación | 57.937.478 | 2,0 % |
| `322A05` | Mejora calidad enseñanza | 50.545.473 | 1,8 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 27.106.209 | 0,9 % |
| `322A03` | Educ.comp.perma.y a dist. | 23.801.616 | 0,8 % |
| `322C01` | Enseñanza agraria | 14.834.296 | 0,5 % |
| `421A03` | Inspec.y calidad indust. | 10.344.720 | 0,4 % |
| `422A01` | Creación de empresas | 5.606.000 | 0,2 % |
| `423A01` | Aprovech.recursos mineros | 4.355.797 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.497,09 M€ (1.497.089.801 €) · 8 códigos · 10,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 61,7 % |
| `412A01` | Apoyo empresa agraria | 230.545.953 | 15,4 % |
| `414A01` | Reforma agraria | 112.556.091 | 7,5 % |
| `412C01` | Producción agraria | 83.254.419 | 5,6 % |
| `413A01` | Comerc.indust.y cont.c.a. | 72.755.794 | 4,9 % |
| `411A01` | Adm.General Agraria | 52.887.940 | 3,5 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 11.717.916 | 0,8 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 8.950.619 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 1,84 M€ (1.836.823 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.836.823 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 244,46 M€ (244.456.073 €) · 7 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451B01` | Dir.y Serv.G.M.A,Viv.O.T. | 89.748.087 | 36,7 % |
| `261A02` | Vivienda | 79.683.141 | 32,6 % |
| `451A02` | Dir.y Serv.G.Movil.y T.D. | 21.641.462 | 8,9 % |
| `261A01` | Arquitectura | 18.201.669 | 7,4 % |
| `261B01` | Ord.territ.y urbanismo | 14.294.190 | 5,8 % |
| `431B01` | Ordenac.y prom. comercial | 13.693.678 | 5,6 % |
| `431A01` | Internacionalización | 7.193.846 | 2,9 % |

</details>

<details open><summary><b><code>empleo</code> — 436,91 M€ (436.913.059 €) · 7 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 173.612.519 | 39,7 % |
| `241B01` | Gestión del empleo | 95.401.886 | 21,8 % |
| `241C01` | Econ.social y discapacit. | 49.229.527 | 11,3 % |
| `241A01` | Dir.y Serv.G.Ind.Com.Empl | 48.774.419 | 11,2 % |
| `241B04` | Intermediación laboral | 30.017.586 | 6,9 % |
| `241C02` | Seg.y salud lab.y rel.lab | 25.146.788 | 5,8 % |
| `241B03` | Empl.y form.pers.discapac | 14.730.334 | 3,4 % |

</details>

<details open><summary><b><code>idi</code> — 379,19 M€ (379.187.952 €) · 6 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 120.753.211 | 31,8 % |
| `467B01` | Invest.aplic.y desar.sect | 104.264.166 | 27,5 % |
| `491A02` | Prom.telecom.y soc.inform | 48.396.872 | 12,8 % |
| `467B02` | Efic.energ.y energ.renov. | 47.809.049 | 12,6 % |
| `467B04` | Invest.científ.o no orien | 42.566.586 | 11,2 % |
| `467B05` | Innovación | 15.398.068 | 4,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 950,48 M€ (950.482.061 €) · 4 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e int.social | 422.891.149 | 44,5 % |
| `231B04` | Atencion personas mayores | 309.370.047 | 32,5 % |
| `212A01` | Pens.y otras presta.econo | 166.124.339 | 17,5 % |
| `231B06` | Promoción y apoyo familia | 52.096.526 | 5,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 204,46 M€ (204.458.058 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 204.458.058 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 12,63 M€ (12.633.520 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 12.633.520 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,01 M€ (9.008.511 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 9.008.511 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 61,33 M€ (61.329.866 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 61.329.866 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,84 M€ (14.842.204 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 14.842.204 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.072,49 M€ · 44 códigos · 21,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.784.512.335 |
| `456A01` | Mejora medio natural | 249.224.473 |
| `453A01` | Carreteras y ferrocar. | 140.560.527 |
| `941A02` | Coop. Econ.Local | 116.483.148 |
| `231B05` | Atención a la infancia | 77.135.533 |
| `231B01` | Adm.Gen.serv.sociales | 61.889.487 |
| `334A01` | Prom.fom.y ap.acc.cult. | 56.890.571 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 54.243.821 |
| `456B01` | Protec.y educac.ambiental | 52.408.097 |
| `425A01` | Infr.eléct.y ahorro energ | 52.272.417 |
| `337A01` | Prom.fom.y ap.patr.cult. | 49.612.092 |
| `453A04` | Promoc.y orden.transporte | 45.248.436 |
| `453A03` | Infraest.compl.transporte | 27.270.691 |
| `336A01` | Fom.y apoyo act.deportiva | 25.763.203 |
| `232A02` | Promoc. y serv. juventud | 23.700.343 |
| `911A01` | Actividad legislativa | 23.491.070 |
| `932A01` | Tributos y finac.autonóm. | 23.256.572 |
| `452A01` | Abastec.y saneam. aguas | 23.200.336 |
| `931A03` | Control int.y Contab.Púb. | 22.785.431 |
| `921A01` | Dir.y Serv.G.Presidencia | 22.137.606 |
| `331A01` | Dir.y Serv.G.Cult.Tur.Dep | 20.553.664 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 19.032.513 |
| `923A01` | Gest.Patrim.y edif.adm. | 17.197.204 |
| `921B01` | Dir.y Adm.Función Pública | 11.279.333 |
| `941A01` | Deleg.y transf.comp.E.L. | 10.549.380 |
| … | *resto: 19 códigos* | 61.788.075 |

</details>

### 2026

*Fuente: `gastos.bin` · 103 líneas · total extraído **14.562,49 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 4.812,77 M€ (4.812.765.002 €) · 8 códigos · 33,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `312A02` | Atención especializada | 2.848.775.970 | 59,2 % |
| `312A01` | Atención primaria | 1.554.905.872 | 32,3 % |
| `312A03` | Formac. internos resident | 126.973.760 | 2,6 % |
| `312A04` | Emergencias sanitarias | 111.722.998 | 2,3 % |
| `313B01` | Salud pública | 110.298.777 | 2,3 % |
| `311B01` | Adm.G.Gerencia Reg.Salud | 31.539.763 | 0,7 % |
| `311A01` | Dir.y Serv.Gen.de Sanidad | 27.233.007 | 0,6 % |
| `313A01` | Planific. y desarrollo | 1.314.855 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 2.865,00 M€ (2.865.004.829 €) · 13 códigos · 19,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A02` | Educ.secund.F.P.ed.espec. | 1.175.949.339 | 41,0 % |
| `322A01` | Educ. infantil y primaria | 809.343.181 | 28,2 % |
| `322B01` | Enseñanzas universitarias | 459.014.382 | 16,0 % |
| `422A02` | Competitividad | 128.943.101 | 4,5 % |
| `322A04` | Serv.complement. enseñ. | 97.223.237 | 3,4 % |
| `321A01` | Dir.y Serv.Gen. Educación | 57.937.478 | 2,0 % |
| `322A05` | Mejora calidad enseñanza | 50.545.473 | 1,8 % |
| `421A02` | Adm.y Serv.Gen.de ICE | 27.106.209 | 0,9 % |
| `322A03` | Educ.comp.perma.y a dist. | 23.801.616 | 0,8 % |
| `322C01` | Enseñanza agraria | 14.834.296 | 0,5 % |
| `421A03` | Inspec.y calidad indust. | 10.344.720 | 0,4 % |
| `422A01` | Creación de empresas | 5.606.000 | 0,2 % |
| `423A01` | Aprovech.recursos mineros | 4.355.797 | 0,2 % |

</details>

<details open><summary><b><code>soberania</code> — 1.497,09 M€ (1.497.089.801 €) · 8 códigos · 10,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `412B01` | FEAGA. Reg. mercados | 924.421.069 | 61,7 % |
| `412A01` | Apoyo empresa agraria | 230.545.953 | 15,4 % |
| `414A01` | Reforma agraria | 112.556.091 | 7,5 % |
| `412C01` | Producción agraria | 83.254.419 | 5,6 % |
| `413A01` | Comerc.indust.y cont.c.a. | 72.755.794 | 4,9 % |
| `411A01` | Adm.General Agraria | 52.887.940 | 3,5 % |
| `412B02` | Gest.ayudas agrar.FEAGA | 11.717.916 | 0,8 % |
| `411A02` | Adm.y Serv.Gen.I.T.A. | 8.950.619 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 1,84 M€ (1.836.823 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `912A01` | Presidencia de la Junta | 1.836.823 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 244,46 M€ (244.456.073 €) · 7 códigos · 1,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451B01` | Dir.y Serv.G.M.A,Viv.O.T. | 89.748.087 | 36,7 % |
| `261A02` | Vivienda | 79.683.141 | 32,6 % |
| `451A02` | Dir.y Serv.G.Movil.y T.D. | 21.641.462 | 8,9 % |
| `261A01` | Arquitectura | 18.201.669 | 7,4 % |
| `261B01` | Ord.territ.y urbanismo | 14.294.190 | 5,8 % |
| `431B01` | Ordenac.y prom. comercial | 13.693.678 | 5,6 % |
| `431A01` | Internacionalización | 7.193.846 | 2,9 % |

</details>

<details open><summary><b><code>empleo</code> — 436,91 M€ (436.913.059 €) · 7 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `241B02` | Formación ocupacional | 173.612.519 | 39,7 % |
| `241B01` | Gestión del empleo | 95.401.886 | 21,8 % |
| `241C01` | Econ.social y pers.discap | 49.229.527 | 11,3 % |
| `241A01` | Dir.y Serv.G.Ind.Com.Empl | 48.774.419 | 11,2 % |
| `241B04` | Intermediación laboral | 30.017.586 | 6,9 % |
| `241C02` | Seg.y salud lab.y rel.lab | 25.146.788 | 5,8 % |
| `241B03` | Empl.y form.pers.discapac | 14.730.334 | 3,4 % |

</details>

<details open><summary><b><code>idi</code> — 379,19 M€ (379.187.952 €) · 6 códigos · 2,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `491A01` | Tecn.inf.y comun.Adm.Reg. | 120.753.211 | 31,8 % |
| `467B01` | Invest.aplic.y desar.sect | 104.264.166 | 27,5 % |
| `491A02` | Prom.telecom.y soc.inform | 48.396.872 | 12,8 % |
| `467B02` | Efic.energ.y energ.renov. | 47.809.049 | 12,6 % |
| `467B04` | Invest.científ.o no orien | 42.566.586 | 11,2 % |
| `467B05` | Innovación | 15.398.068 | 4,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 950,48 M€ (950.482.061 €) · 4 códigos · 6,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B02` | Serv.soc.bás.e inc.social | 422.891.149 | 44,5 % |
| `231B04` | Atencion personas mayores | 309.370.047 | 32,5 % |
| `212A01` | Pens.y otras presta.econo | 166.124.339 | 17,5 % |
| `231B06` | Promoción y apoyo familia | 52.096.526 | 5,5 % |

</details>

<details open><summary><b><code>discapacidad</code> — 204,46 M€ (204.458.058 €) · 1 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B03` | Atenc.pers.con discapacid | 204.458.058 | 100,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 12,63 M€ (12.633.520 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B07` | Intervención drogodepend. | 12.633.520 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 9,01 M€ (9.008.511 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `231B08` | Migrac.y coop. desarrollo | 9.008.511 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 61,33 M€ (61.329.866 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `432A01` | Ord.,prom.y gest. turismo | 61.329.866 | 100,0 % |

</details>

<details open><summary><b><code>igualdad</code> — 14,84 M€ (14.842.204 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `232A01` | Promoción y apoyo mujer | 14.842.204 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 3.072,49 M€ · 44 códigos · 21,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A01` | Amort.y g.fin.deuda Comun | 1.784.512.335 |
| `456A01` | Mejora medio natural | 249.224.473 |
| `453A01` | Carreteras y ferrocar. | 140.560.527 |
| `941A02` | Coop. Econ.Local | 116.483.148 |
| `231B05` | Atención a la infancia | 77.135.533 |
| `231B01` | Adm.Gen.serv.sociales | 61.889.487 |
| `334A01` | Prom.fom.y ap.acc.cult. | 56.890.571 |
| `923C01` | Dir.y Serv.Gen.E.Hacienda | 54.243.821 |
| `456B01` | Protec.y educac.ambiental | 52.408.097 |
| `425A01` | Infr.eléct.y ahorro energ | 52.272.417 |
| `337A01` | Prom.fom.y ap.patr.cult. | 49.612.092 |
| `453A04` | Promoc.y orden.transporte | 45.248.436 |
| `453A03` | Infraest.compl.transporte | 27.270.691 |
| `336A01` | Fom.y apoyo act.deportiva | 25.763.203 |
| `232A02` | Promoc. y serv. juventud | 23.700.343 |
| `911A01` | Actividad legislativa | 23.491.070 |
| `932A01` | Tributos y finac.autonóm. | 23.256.572 |
| `452A01` | Abastec.y saneam. aguas | 23.200.336 |
| `931A03` | Control int.y Contab.Púb. | 22.785.431 |
| `921A01` | Dir.y Serv.G.Presidencia | 22.137.606 |
| `331A01` | Dir.y Serv.G.Cult.Tur.Dep | 20.553.664 |
| `131A01` | P.Civil, Pol. Loc. e Int. | 19.032.513 |
| `923A01` | Gest.Patrim.y edif.adm. | 17.197.204 |
| `921B01` | Dir.y Adm.Función Pública | 11.279.333 |
| `941A01` | Deleg.y transf.comp.E.L. | 10.549.380 |
| … | *resto: 19 códigos* | 61.788.075 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py cym     # regenera este documento
python3 tools/auditoria_magnitud.py cym        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa cym --anio <año> \
    --input ../fuentes/raw/cym/<año>/<fichero> --output /tmp/cym.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-cym.md`](limitaciones-cym.md)

