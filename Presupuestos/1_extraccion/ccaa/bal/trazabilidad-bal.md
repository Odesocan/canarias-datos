# Trazabilidad de la extracción — Islas Baleares (`bal`)

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
| **2015** | 131 | `memoria_programas.html` | 13 | 39,7 % | 4.011,31 | — | no_aplica |
| **2016** | 132 | `memoria_programas.html` | 13 | 39,4 % | 4.218,30 | — | no_aplica |
| **2017** | 129 | `memoria_programas.html` | 13 | 42,6 % | 4.646,73 | — | no_aplica |
| **2018** | 136 | `memoria_programas.html` | 13 | 43,4 % | 4.981,31 | — | no_aplica |
| **2019** | 141 | `memoria_programas.html` | 13 | 42,6 % | 5.436,32 | — | no_aplica |
| **2020** | 150 | `memoria_programas.html` | 13 | 46,0 % | 5.772,63 | — | no_aplica |
| **2021** | 143 | `memoria_programas.html` | 13 | 45,5 % | 5.847,62 | — | no_aplica |
| **2022** | 143 | `memoria_programas.html` | 13 | 43,4 % | 6.368,44 | — | no_aplica |
| **2023** | 150 | `memoria_programas.html` | 13 | 46,7 % | 7.087,17 | — | no_aplica |
| **2024** | 145 | `memoria_programas.html` | 13 | 48,3 % | 7.114,25 | — | no_aplica |
| **2025** | 141 | `memoria_programas.html` | 13 | 48,2 % | 6.350,11 | — | no_aplica |
| **2026** | 148 | `estats_numerics.pdf` | 13 | 48,0 % | 6.442,00 | — | prorroga |

**URL(s) de origen:**
- <https://pressuposts.caib.es/www/ant/pr2015/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2016/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2017-def/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2018/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2019/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2020/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2021/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2022/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2023/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2024/archivos/menu_tom3_d.html>
- <https://pressuposts.caib.es/www/ant/pr2025bis/archivos/menu_tom3_d.html>
- <https://www.caib.es/sites/pressuposts/es/prorroga_del_pressupuesto_para_el_aao_2026/archivopub.do?ctrl=MCRST226ZI540093&id=540093>

## 2 · Matriz concepto × año — importe total (M€ nominales)

| Concepto | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | 1.293,31 | 1.370,09 | 1.474,29 | 1.555,47 | 1.708,00 | 1.706,61 | 1.761,50 | 1.939,28 | 2.199,72 | 2.273,12 | 2.393,41 | 2.425,55 |
| `educacion` | 775,80 | 817,45 | 883,52 | 936,45 | 1.001,14 | 1.006,29 | 1.021,26 | 1.136,37 | 1.245,71 | 1.343,39 | 1.421,04 | 1.400,84 |
| `soberania` | 58,56 | 52,10 | 54,36 | 57,22 | 69,11 | 53,48 | 49,27 | 57,46 | 69,18 | 93,80 | 76,47 | 70,77 |
| `direccion` | 4,37 | 3,18 | 3,18 | 3,38 | 3,34 | 3,38 | 3,25 | 3,24 | 3,38 | 3,30 | 4,28 | 3,95 |
| `vivienda` | 14,90 | 45,25 | 53,51 | 29,04 | 65,13 | 63,78 | 35,66 | 36,45 | 104,62 | 71,88 | 98,03 | 28,70 |
| `empleo` | 49,93 | 59,78 | 85,94 | 99,22 | 111,71 | 21,73 | 105,06 | 137,93 | 145,22 | 29,60 | 154,89 | 138,73 |
| `idi` | 12,79 | 13,39 | 20,32 | 32,42 | 52,21 | 36,80 | 29,62 | 33,08 | 54,90 | 88,26 | 98,92 | 78,96 |
| `dependencia` | 120,96 | 137,52 | 145,47 | 155,63 | 146,16 | 117,80 | 127,90 | 174,17 | 202,41 | 200,33 | 225,19 | 249,51 |
| `discapacidad` | 2,18 | 2,72 | 14,05 | 13,86 | 18,04 | 24,46 | 25,41 | 26,84 | 29,26 | 32,04 | 36,75 | 37,17 |
| `salud_mental` | 7,74 | 7,57 | 2,52 | 2,32 | 2,32 | 32,56 | 29,90 | 49,15 | 115,54 | 66,91 | 64,99 | 63,31 |
| `diversidad` | 1,77 | 2,18 | 2,54 | 2,58 | 2,60 | 0,43 | 0,40 | 5,28 | 5,35 | 3,60 | 6,84 | 1,35 |
| `turismo` | 39,77 | 38,29 | 41,39 | 91,64 | 37,97 | 33,47 | 35,34 | 32,02 | 188,44 | 253,41 | 208,23 | 185,63 |
| `igualdad` | 2,54 | 2,63 | 3,11 | 3,47 | 7,26 | 16,53 | 16,40 | 17,73 | 20,74 | 9,44 | 9,48 | 8,59 |
| **Σ asignado** | 2.384,62 | 2.552,17 | 2.784,20 | 2.982,71 | 3.224,99 | 3.117,34 | 3.240,98 | 3.649,01 | 4.384,46 | 4.469,08 | 4.798,53 | 4.693,07 |
| *(sin concepto)* | 1.626,69 | 1.666,13 | 1.862,52 | 1.998,60 | 2.211,33 | 2.655,29 | 2.606,63 | 2.719,43 | 2.702,70 | 2.645,17 | 1.551,58 | 1.748,94 |
| **TOTAL extraído** | 4.011,31 | 4.218,30 | 4.646,73 | 4.981,31 | 5.436,32 | 5.772,63 | 5.847,62 | 6.368,44 | 7.087,17 | 7.114,25 | 6.350,11 | 6.442,00 |

## 3 · Variación interanual (%) — detector de saltos

| Concepto | 2015→2016 | 2016→2017 | 2017→2018 | 2018→2019 | 2019→2020 | 2020→2021 | 2021→2022 | 2022→2023 | 2023→2024 | 2024→2025 | 2025→2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `sanidad` | +5,9 % | +7,6 % | +5,5 % | +9,8 % | −0,1 % | +3,2 % | +10,1 % | +13,4 % | +3,3 % | +5,3 % | +1,3 % |
| `educacion` | +5,4 % | +8,1 % | +6,0 % | +6,9 % | +0,5 % | +1,5 % | +11,3 % | +9,6 % | +7,8 % | +5,8 % | −1,4 % |
| `soberania` | −11,0 % | +4,3 % | +5,3 % | +20,8 % | −22,6 % | −7,9 % | +16,6 % | +20,4 % | +35,6 % | −18,5 % | −7,4 % |
| `direccion` | −27,1 % | −0,0 % | +6,2 % | −1,0 % | +1,1 % | −3,7 % | −0,3 % | +4,1 % | −2,4 % | +29,6 % | −7,7 % |
| `vivienda` | +203,7 % ⚠ | +18,3 % | −45,7 % ⚠ | +124,3 % ⚠ | −2,1 % | −44,1 % ⚠ | +2,2 % | +187,0 % ⚠ | −31,3 % | +36,4 % | −70,7 % ⚠ |
| `empleo` | +19,7 % | +43,8 % ⚠ | +15,5 % | +12,6 % | −80,5 % ⚠ | +383,4 % ⚠ | +31,3 % | +5,3 % | −79,6 % ⚠ | +423,3 % ⚠ | −10,4 % |
| `idi` | +4,7 % | +51,7 % ⚠ | +59,6 % ⚠ | +61,0 % ⚠ | −29,5 % | −19,5 % | +11,7 % | +66,0 % ⚠ | +60,8 % ⚠ | +12,1 % | −20,2 % |
| `dependencia` | +13,7 % | +5,8 % | +7,0 % | −6,1 % | −19,4 % | +8,6 % | +36,2 % | +16,2 % | −1,0 % | +12,4 % | +10,8 % |
| `discapacidad` | +24,7 % | +417,1 % ⚠ | −1,3 % | +30,1 % | +35,6 % | +3,9 % | +5,6 % | +9,0 % | +9,5 % | +14,7 % | +1,1 % |
| `salud_mental` | −2,2 % | −66,7 % ⚠ | −7,8 % | +0,1 % | +1,300,8 % ⚠ | −8,2 % | +64,4 % ⚠ | +135,1 % ⚠ | −42,1 % ⚠ | −2,9 % | −2,6 % |
| `diversidad` | +22,8 % | +16,6 % | +1,8 % | +0,5 % | −83,3 % ⚠ | −7,2 % | +1,210,9 % ⚠ | +1,2 % | −32,7 % | +90,1 % ⚠ | −80,2 % ⚠ |
| `turismo` | −3,7 % | +8,1 % | +121,4 % ⚠ | −58,6 % ⚠ | −11,8 % | +5,6 % | −9,4 % | +488,5 % ⚠ | +34,5 % | −17,8 % | −10,9 % |
| `igualdad` | +3,9 % | +18,1 % | +11,6 % | +109,0 % ⚠ | +127,6 % ⚠ | −0,8 % | +8,1 % | +16,9 % | −54,5 % ⚠ | +0,4 % | −9,4 % |
| **TOTAL** | +5,2 % | +10,2 % | +7,2 % | +9,1 % | +6,2 % | +1,3 % | +8,9 % | +11,3 % | +0,4 % | −10,7 % | +1,4 % |

## 4 · Alertas automáticas (candidatos a revisión)

| Año | Concepto | Tipo | Detalle |
|---|---|---|---|
| 2016 | `vivienda` | **SALTO** | 14,90 → 45,25 M€ (+203,7 % ⚠) |
| 2017 | `empleo` | **SALTO** | 59,78 → 85,94 M€ (+43,8 % ⚠) |
| 2018 | `idi` | **SALTO** | 20,32 → 32,42 M€ (+59,6 % ⚠) |
| 2018 | `turismo` | **SALTO** | 41,39 → 91,64 M€ (+121,4 % ⚠) |
| 2018 | `vivienda` | **SALTO** | 53,51 → 29,04 M€ (−45,7 % ⚠) |
| 2019 | `idi` | **SALTO** | 32,42 → 52,21 M€ (+61,0 % ⚠) |
| 2019 | `turismo` | **SALTO** | 91,64 → 37,97 M€ (−58,6 % ⚠) |
| 2019 | `vivienda` | **SALTO** | 29,04 → 65,13 M€ (+124,3 % ⚠) |
| 2020 | `empleo` | **SALTO** | 111,71 → 21,73 M€ (−80,5 % ⚠) |
| 2020 | `salud_mental` | **SALTO** | 2,32 → 32,56 M€ (+1,300,8 % ⚠) |
| 2021 | `empleo` | **SALTO** | 21,73 → 105,06 M€ (+383,4 % ⚠) |
| 2021 | `vivienda` | **SALTO** | 63,78 → 35,66 M€ (−44,1 % ⚠) |
| 2022 | `salud_mental` | **SALTO** | 29,90 → 49,15 M€ (+64,4 % ⚠) |
| 2023 | `idi` | **SALTO** | 33,08 → 54,90 M€ (+66,0 % ⚠) |
| 2023 | `salud_mental` | **SALTO** | 49,15 → 115,54 M€ (+135,1 % ⚠) |
| 2023 | `turismo` | **SALTO** | 32,02 → 188,44 M€ (+488,5 % ⚠) |
| 2023 | `vivienda` | **SALTO** | 36,45 → 104,62 M€ (+187,0 % ⚠) |
| 2024 | `empleo` | **SALTO** | 145,22 → 29,60 M€ (−79,6 % ⚠) |
| 2024 | `idi` | **SALTO** | 54,90 → 88,26 M€ (+60,8 % ⚠) |
| 2024 | `salud_mental` | **SALTO** | 115,54 → 66,91 M€ (−42,1 % ⚠) |
| 2025 | `empleo` | **SALTO** | 29,60 → 154,89 M€ (+423,3 % ⚠) |
| 2026 | `vivienda` | **SALTO** | 98,03 → 28,70 M€ (−70,7 % ⚠) |

### 4.2 · Códigos que CAMBIAN de concepto entre años (12 casos)

> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza
> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de
> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:

| Código | Importe máx. (M€) | Concepto por año |
|---|---:|---|
| `121B` | 47,02 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:igualdad, 2021:igualdad, 2022:igualdad, 2023:igualdad, 2026:(sin concepto) |
| `571H` | 44,07 | 2018:turismo, 2019:(sin concepto), 2020:(sin concepto), 2023:turismo, 2024:turismo, 2025:turismo, 2026:turismo |
| `141A` | 31,45 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:idi, 2025:idi, 2026:idi |
| `521E` | 28,50 | 2020:(sin concepto), 2023:turismo, 2024:turismo |
| `455C` | 18,55 | 2018:turismo, 2019:(sin concepto), 2020:(sin concepto) |
| `561B` | 17,89 | 2019:idi, 2020:idi, 2021:turismo |
| `313K` | 17,66 | 2015:dependencia, 2016:dependencia, 2017:dependencia, 2018:dependencia, 2019:dependencia, 2020:dependencia, 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:dependencia |
| `721A` | 15,26 | 2015:(sin concepto), 2016:(sin concepto), 2017:(sin concepto), 2024:empleo, 2025:empleo, 2026:(sin concepto) |
| `511B` | 12,29 | 2016:(sin concepto), 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:vivienda, 2022:vivienda, 2023:vivienda, 2024:vivienda, 2025:vivienda, 2026:vivienda |
| `731B` | 11,36 | 2019:(sin concepto), 2020:(sin concepto), 2023:turismo |
| `121L` | 9,45 | 2018:(sin concepto), 2019:(sin concepto), 2020:turismo, 2021:turismo, 2022:turismo, 2023:turismo |
| `571G` | 4,69 | 2017:(sin concepto), 2018:(sin concepto), 2019:(sin concepto), 2020:(sin concepto), 2021:(sin concepto), 2022:(sin concepto), 2023:(sin concepto), 2024:(sin concepto), 2025:(sin concepto), 2026:sanidad |

## 5 · Detalle año por año — qué códigos componen cada concepto

### 2015

*Fuente: `memoria_programas.html` · 131 líneas · total extraído **4.011,31 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.293,31 M€ (1.293.305.893 €) · 9 códigos · 32,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411D` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:3)(cid:79)(cid:182)(cid:68)(cid:86)(cid:86)(cid:76)(cid:86)(cid:87)(cid:113)(cid:81)(cid:70)(cid:76)(cid:68)(cid:3)(cid:86)(cid:68)(cid:81)(cid:76)(cid:87)(cid:106)(cid:85)(cid:76)(cid:68) | 1.266.675.036 | 97,9 % |
| `411A` | Direcció i serveis generals de Salut | 7.296.763 | 0,6 % |
| `413B` | Programes de salut pública | 7.007.630 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 5.810.570 | 0,4 % |
| `315B` | Salut i prevenció de riscs laborals | 2.362.019 | 0,2 % |
| `413A` | Ordenació i inspecció dels serveis sanitaris | 1.491.021 | 0,1 % |
| `315D` | Salut i prevenció de riscs laborals a l’Administració | 1.056.111 | 0,1 % |
| `413D` | Coordinació de centres insulars | 956.070 | 0,1 % |
| `413F` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:15)(cid:3)(cid:70)(cid:82)(cid:81)(cid:87)(cid:85)(cid:82)(cid:79)(cid:3)(cid:76)(cid:3)(cid:74)(cid:72)(cid:86)(cid:87)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:72)(cid:71)(cid:76)(cid:70)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:79)(cid:86)(cid:3)(cid:86)(cid:72)(cid:85)(cid:89)(cid:72)(cid:76)(cid:86)(cid:3)(cid:73)(cid:68)(cid:85)(cid:80)(cid:68)(cid:70)(cid:113)(cid:88)(cid:87)(cid:76)(cid:70)(cid:86) | 650.673 | 0,1 % |

</details>

<details open><summary><b><code>educacion</code> — 775,80 M€ (775.802.264 €) · 15 códigos · 19,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 442.956.476 | 57,1 % |
| `422B` | Educació concertada i altres ensenyaments | 144.931.549 | 18,7 % |
| `421F` | Política i actuacions en matèria universitària | 57.333.324 | 7,4 % |
| `423B` | Altres serveis a l’ensenyament | 51.241.982 | 6,6 % |
| `421A` | Direcció i serveis generals d’Educació, Cultura i Universitats | 38.790.812 | 5,0 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 29.006.636 | 3,7 % |
| `421G` | Ordenació de la formació professional | 3.350.794 | 0,4 % |
| `421B` | Ordenació general del sistema educatiu | 2.348.149 | 0,3 % |
| `421C` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:72)(cid:71)(cid:88)(cid:70)(cid:68)(cid:87)(cid:76)(cid:89)(cid:68)(cid:3)(cid:76)(cid:3)(cid:85)(cid:113)(cid:74)(cid:76)(cid:80)(cid:3)(cid:71)(cid:72)(cid:3)(cid:70)(cid:72)(cid:81)(cid:87)(cid:85)(cid:72)(cid:86)(cid:3)(cid:72)(cid:86)(cid:70)(cid:82)(cid:79)(cid:68)(cid:85)(cid:86) | 1.633.406 | 0,2 % |
| `423A` | Beques i ajuts | 1.450.000 | 0,2 % |
| `421D` | Innovació i formació del professorat | 1.405.563 | 0,2 % |
| `422G` | Tecnologies de la informació i la comunicació | 1.123.008 | 0,1 % |
| `443M` | Educació ambiental i societat | 153.705 | 0,0 % |
| `421H` | Inspecció educativa | 58.860 | 0,0 % |
| `422H` | Suport al trilingüisme | 18.000 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 58,56 M€ (58.564.872 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agrari de les Illes Balears | 36.081.220 | 61,6 % |
| `711A` | Direcció i serveis generals C.Agricultura, Medi Ambient i Territori | 19.643.271 | 33,5 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 1.855.381 | 3,2 % |
| `531A` | Infraestructures agràries de les zones rurals | 985.000 | 1,7 % |

</details>

<details open><summary><b><code>direccion</code> — 4,37 M€ (4.366.601 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Serveis generals de la Presidència del Govern | 4.366.601 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 14,90 M€ (14.903.480 €) · 1 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 14.903.480 | 100,0 % |

</details>

<details open><summary><b><code>empleo</code> — 49,93 M€ (49.930.749 €) · 3 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació a les Illes Balears | 42.059.332 | 84,2 % |
| `322A` | (cid:50)(cid:70)(cid:88)(cid:83)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:76)(cid:81)(cid:86)(cid:72)(cid:85)(cid:70)(cid:76)(cid:121)(cid:3)(cid:79)(cid:68)(cid:69)(cid:82)(cid:85)(cid:68)(cid:79)(cid:3)(cid:72)(cid:86)(cid:83)(cid:72)(cid:70)(cid:116)(cid:191)(cid:70)(cid:86) | 6.257.771 | 12,5 % |
| `322B` | Gestió de les relacions laborals | 1.613.646 | 3,2 % |

</details>

<details open><summary><b><code>idi</code> — 12,79 M€ (12.789.633 €) · 7 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541A` | Recerca i desenvolupament tecnològic | 5.056.113 | 39,5 % |
| `542A` | Innovació tecnològica | 4.585.913 | 35,9 % |
| `463D` | Eleccions i partits polítics | 1.800.000 | 14,1 % |
| `463B` | Informació i atenció a la ciutadania | 700.000 | 5,5 % |
| `463C` | Foment de projectes de comunicació d’interès social | 317.000 | 2,5 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 295.607 | 2,3 % |
| `463E` | Foment de la participació ciutadana | 35.000 | 0,3 % |

</details>

<details open><summary><b><code>dependencia</code> — 120,96 M€ (120.964.828 €) · 4 códigos · 3,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Protecció i acció social | 58.703.399 | 48,5 % |
| `314A` | Pensions i prestacions econòmiques | 41.395.237 | 34,2 % |
| `313I` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:82)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:86)(cid:82)(cid:70)(cid:76)(cid:68)(cid:79)(cid:86) | 12.766.486 | 10,6 % |
| `313K` | Direcció i serveis generals de Família i Serveis Socials | 8.099.706 | 6,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 2,18 M€ (2.178.260 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | Família i unitats de convivència | 1.994.735 | 91,6 % |
| `313F` | Protecció i defensa dels drets dels menors | 183.525 | 8,4 % |

</details>

<details open><summary><b><code>salud_mental</code> — 7,74 M€ (7.737.937 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Centres assistencials | 5.646.774 | 73,0 % |
| `413E` | Pla autonòmic de drogues | 2.091.163 | 27,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,77 M€ (1.773.683 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Integració social d’immigrants | 1.773.683 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 39,77 M€ (39.767.443 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | (cid:50)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:86)(cid:72)(cid:70)(cid:87)(cid:82)(cid:85)(cid:3)(cid:76)(cid:3)(cid:85)(cid:72)(cid:71)(cid:72)(cid:191)(cid:81)(cid:76)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:82)(cid:71)(cid:72)(cid:79)(cid:3)(cid:87)(cid:88)(cid:85)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70) | 33.864.883 | 85,2 % |
| `751A` | Direcció i serveis generals de Turisme i Esports | 5.902.560 | 14,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,54 M€ (2.536.544 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Promoció, protecció i serveis per a la dona | 2.536.544 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.626,69 M€ · 79 códigos · 40,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deute públic | 863.761.892 |
| `912A` | Transferències a corporacions locals | 283.995.287 |
| `513C` | Ordenació i inspecció del transport terrestre | 64.000.340 |
| `441B` | Sanejament i depuració d’aigües | 59.789.957 |
| `121B` | Direcció i serveis generals de la Conselleria de Presidència | 47.023.156 |
| `441A` | Proveïment d’aigües | 30.349.641 |
| `513D` | Infraestructures bàsiques | 26.695.136 |
| `457A` | Promoció i foment de l’esport | 19.653.268 |
| `124A` | Cooperació i relacions amb els ens territorials i relacions interadministratives | 18.971.679 |
| `533A` | Conservació i millora del medi natural | 18.585.480 |
| `455A` | Cultura i política lingüística | 17.821.923 |
| `111A` | Activitat legislativa | 13.901.327 |
| `611A` | Direcció i serveis generals d’Hisenda i Pressuposts | 13.885.613 |
| `121K` | Altres actuacions d’administració general i funció pública | 12.000.000 |
| `126L` | Serveis comuns tecnològics | 10.726.634 |
| `313C` | Mesures judicials i prevenció del delicte | 10.383.591 |
| `511E` | Gestió dels transports aeri i marítim a les Illes Balears | 9.182.358 |
| `514B` | Gestió de les instal·lacions portuàries | 7.292.206 |
| `721A` | Direcció i serveis generals d’Economia i Competitivitat | 6.439.419 |
| `223A` | Emergències | 5.748.789 |
| `512A` | Domini Públic Hidràulic: Protecció i control. Directiva marc de l’aigua | 5.264.585 |
| `612C` | Gestió comptable i control intern | 4.993.019 |
| `533B` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:73)(cid:82)(cid:85)(cid:72)(cid:86)(cid:87)(cid:68)(cid:79) | 4.452.978 |
| `723A` | Promoció industrial i tecnològica | 4.414.935 |
| `612G` | Organització i gestió del patrimoni de la comunitat autònoma | 4.141.134 |
| … | *resto: 54 códigos* | 63.214.300 |

</details>

### 2016

*Fuente: `memoria_programas.html` · 132 líneas · total extraído **4.218,30 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.370,09 M€ (1.370.092.639 €) · 10 códigos · 32,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.340.922.958 | 97,9 % |
| `413B` | Programes de salut pública | 7.506.216 | 0,5 % |
| `411A` | Direcció i serveis generals de Salut | 7.286.068 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 6.001.409 | 0,4 % |
| `315B` | Salut i prevenció de riscs laborals | 2.924.305 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 1.961.253 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.035.008 | 0,1 % |
| `315D` | Salut i prevenció de riscs laborals a l’Administració | 1.028.469 | 0,1 % |
| `411D` | >$.&5,*.*589(.:.$6.*58(5(*.0'%0.(3%()%0:%5) | 791.468 | 0,1 % |
| `413F` | >$.&5,*.*589(*!&'0!$(5(A%)'58(3%$("%35*."%&'(5(3%$)()%0:%5)(B.0".*C6'5*) | 635.485 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 817,45 M€ (817.453.988 €) · 14 códigos · 19,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 461.564.525 | 56,5 % |
| `422B` | Educació concertada i altres ensenyaments | 157.497.048 | 19,3 % |
| `421F` | Política i actuacions en matèria universitària | 62.849.690 | 7,7 % |
| `423B` | Altres serveis a l’ensenyament | 53.291.277 | 6,5 % |
| `421A` | Direcció i serveis generals d’Educació i Universitat | 39.354.993 | 4,8 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 27.932.551 | 3,4 % |
| `421K` | Innovació i comunitat educativa | 6.527.440 | 0,8 % |
| `421G` | Ordenació de la formació professional | 3.198.294 | 0,4 % |
| `421B` | Ordenació general del sistema educatiu | 2.303.788 | 0,3 % |
| `421C` | A$.&5,*.*58(%36*.'5:.(5(0>C5"(3%(*%&'0%)(%)*!$.0) | 1.238.037 | 0,2 % |
| `422G` | Tecnologies de la informació i la comunicació | 959.239 | 0,1 % |
| `421D` | Formació del professorat | 369.657 | 0,0 % |
| `443M` | Educació ambiental i societat | 240.000 | 0,0 % |
| `421H` | Inspecció educativa | 127.449 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 52,10 M€ (52.104.398 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agrari de les Illes Balears | 34.501.556 | 66,2 % |
| `711A` | Direcció i serveis generals de Medi Ambient, Agricultura i Pesca | 14.661.995 | 28,1 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 1.954.847 | 3,8 % |
| `531A` | Infraestructures agràries de les zones rurals | 986.000 | 1,9 % |

</details>

<details open><summary><b><code>direccion</code> — 3,18 M€ (3.184.193 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Serveis generals de la Presidència del Govern | 3.184.193 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 45,25 M€ (45.254.455 €) · 2 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | Direcció i serveis generals de Participació, Transparència i Cultura | 32.363.368 | 71,5 % |
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 12.891.087 | 28,5 % |

</details>

<details open><summary><b><code>empleo</code> — 59,78 M€ (59.775.360 €) · 3 códigos · 1,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació a les Illes Balears | 50.900.000 | 85,2 % |
| `322A` | B*6#.*58(5(5&)%0*58($./!0.$(%)#%*+,*) | 7.115.869 | 11,9 % |
| `322B` | Gestió de les relacions laborals | 1.759.491 | 2,9 % |

</details>

<details open><summary><b><code>idi</code> — 13,39 M€ (13.392.569 €) · 6 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació tecnològica | 6.217.072 | 46,4 % |
| `541A` | Recerca i desenvolupament tecnològic | 5.698.233 | 42,5 % |
| `463C` | Projectes de comunicació d’interès social | 584.000 | 4,4 % |
| `463E` | Participació, transparència, bon govern i voluntariat | 489.000 | 3,7 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 238.264 | 1,8 % |
| `463B` | Informació i atenció a la ciutadania | 166.000 | 1,2 % |

</details>

<details open><summary><b><code>dependencia</code> — 137,52 M€ (137.523.501 €) · 4 códigos · 3,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Protecció i acció social | 62.823.734 | 45,7 % |
| `314A` | Pensions i prestacions econòmiques | 52.974.211 | 38,5 % |
| `313I` | ?$.&5,*.*58(5(!03%&.*58()!*5.$) | 13.703.784 | 10,0 % |
| `313K` | Direcció i serveis generals de Serveis Socials i Cooperació | 8.021.772 | 5,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 2,72 M€ (2.716.671 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313G` | Família i unitats de convivència | 2.396.017 | 88,2 % |
| `313F` | Protecció i defensa dels drets dels menors | 320.654 | 11,8 % |

</details>

<details open><summary><b><code>salud_mental</code> — 7,57 M€ (7.566.414 €) · 2 códigos · 0,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313A` | Centres assistencials | 5.299.251 | 70,0 % |
| `413E` | Pla autonòmic de drogues | 2.267.163 | 30,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,18 M€ (2.178.344 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Integració social d’immigrants | 2.178.344 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 38,29 M€ (38.294.520 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | =03%&.*58(3%$()%*'!0(5(0%3%,&5*58(3%$("!3%$('60+)'5* | 32.831.138 | 85,7 % |
| `751A` | Direcció i serveis generals d’Innovació, Recerca i Turisme | 5.463.382 | 14,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 2,63 M€ (2.634.590 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Promoció, protecció i serveis per a la dona | 2.634.590 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.666,13 M€ · 80 códigos · 39,5 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Deute públic | 905.516.516 |
| `912A` | Transferències a corporacions locals | 300.116.816 |
| `441B` | Sanejament i depuració d’aigües | 62.905.373 |
| `513C` | Ordenació i inspecció del transport terrestre | 60.491.645 |
| `441A` | Proveïment d’aigües | 29.168.413 |
| `513D` | Infraestructures bàsiques | 27.405.667 |
| `457A` | Promoció i foment de l’esport | 19.491.301 |
| `533A` | Conservació i millora del medi natural | 18.692.693 |
| `124A` | Cooperació i relacions amb els ens territorials i relacions interadministratives | 18.357.216 |
| `121K` | Altres actuacions d’administració general i funció pública | 17.000.000 |
| `455A` | Cultura i política lingüística | 16.397.713 |
| `611A` | Direcció i serveis generals d’Hisenda i Administracions Públiques | 15.214.093 |
| `111A` | Activitat legislativa | 14.079.100 |
| `313C` | Mesures judicials i prevenció del delicte | 11.336.762 |
| `121B` | Direcció i serveis generals de la Conselleria de Presidència | 9.516.464 |
| `511E` | Gestió dels transports aeri i marítim a les Illes Balears | 9.385.622 |
| `126L` | Serveis comuns tecnològics | 9.146.634 |
| `514B` | Gestió de les instal·lacions portuàries | 7.089.560 |
| `511B` | Direcció i serveis generals de Territori, Energia i Mobilitat | 6.494.674 |
| `521A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 6.177.421 |
| `512A` | Domini Públic Hidràulic: Protecció i control. Directiva marc de l’aigua | 5.896.006 |
| `721A` | Direcció i serveis generals de Treball, Comerç i Indústria | 5.816.159 |
| `223A` | Emergències | 5.571.105 |
| `533B` | 8$.&3,*.*3=(E!0%)'.$ | 4.850.777 |
| `612C` | Gestió comptable i control intern | 4.730.299 |
| … | *resto: 55 códigos* | 75.285.027 |

</details>

### 2017

*Fuente: `memoria_programas.html` · 129 líneas · total extraído **4.646,73 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.474,29 M€ (1.474.285.487 €) · 10 códigos · 31,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.443.159.788 | 97,9 % |
| `413B` | Programes de salut pública | 8.218.588 | 0,6 % |
| `411A` | Direcció i serveis generals de Salut | 7.612.654 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 6.472.581 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 2.935.625 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 2.189.390 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.083.435 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.037.716 | 0,1 % |
| `411D` | ?$.&5,*.*589(.:.$6.*58(5(*.0'%0.(3%()%0:%5) | 869.367 | 0,1 % |
| `413F` | ?$.&5,*.*589(*!&'0!$(5(B%)'58(3%$("%35*."%&'(5(3%$)()%0:%5)(C.0".*D6'5*) | 706.343 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 883,52 M€ (883.516.262 €) · 14 códigos · 19,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 508.924.742 | 57,6 % |
| `422B` | Educació concertada | 160.913.234 | 18,2 % |
| `421F` | Política i actuacions en matèria universitària | 67.308.160 | 7,6 % |
| `423B` | Altres serveis a l’ensenyament | 58.629.355 | 6,6 % |
| `421A` | Direcció i serveis generals d’Educació i Universitat | 39.344.842 | 4,5 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 29.831.712 | 3,4 % |
| `421K` | Innovació i comunitat educativa | 9.541.826 | 1,1 % |
| `421G` | Formació professional i aprenentatge permanent | 3.394.452 | 0,4 % |
| `421E` | Projectes lingüístics | 2.112.526 | 0,2 % |
| `421C` | A$.&5,*.*58(%36*.'5:.(5(0>C5"(3%(*%&'0%)(%)*!$.0) | 1.249.215 | 0,1 % |
| `571B` | Educació ambiental | 939.369 | 0,1 % |
| `421D` | Formació del professorat | 925.352 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 245.707 | 0,0 % |
| `421H` | Inspecció educativa | 155.770 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 54,36 M€ (54.362.916 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agrari | 36.532.786 | 67,2 % |
| `711A` | Direcció i serveis generals de Medi Ambient, Agricultura i Pesca | 14.286.158 | 26,3 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.515.851 | 4,6 % |
| `531A` | Ordenació del territori i urbanisme | 1.028.121 | 1,9 % |

</details>

<details open><summary><b><code>direccion</code> — 3,18 M€ (3.183.022 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Serveis generals de la Presidència del Govern | 3.183.022 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 53,51 M€ (53.514.942 €) · 3 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `451A` | Direcció i serveis generals de Transparència, Cultura i Esports | 34.478.661 | 64,4 % |
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 15.521.258 | 29,0 % |
| `431A` | Gestió i foment de l’habitatge social | 3.515.023 | 6,6 % |

</details>

<details open><summary><b><code>empleo</code> — 85,94 M€ (85.942.112 €) · 4 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 74.045.358 | 86,2 % |
| `322A` | B*6#.*58(5(5&)%0*58($./!0.$(%)#%*+,C6%) | 8.287.656 | 9,6 % |
| `322B` | Gestió de les relacions laborals | 3.199.382 | 3,7 % |
| `322C` | Foment de la responsabilitat social corporativa | 409.716 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 20,32 M€ (20.316.826 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació | 7.189.376 | 35,4 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 6.420.868 | 31,6 % |
| `541A` | Recerca i desenvolupament | 6.400.651 | 31,5 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 305.931 | 1,5 % |

</details>

<details open><summary><b><code>dependencia</code> — 145,47 M€ (145.471.681 €) · 4 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 61.972.769 | 42,6 % |
| `313I` | ?$.&5,*.*58(5(!03%&.*58()!*5.$) | 41.308.874 | 28,4 % |
| `314A` | Pensions i prestacions econòmiques | 33.534.120 | 23,1 % |
| `313K` | Direcció i serveis generals de Serveis Socials i Cooperació | 8.655.918 | 6,0 % |

</details>

<details open><summary><b><code>discapacidad</code> — 14,05 M€ (14.047.083 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 10.143.113 | 72,2 % |
| `313G` | Família i unitats de convivència | 3.598.190 | 25,6 % |
| `313F` | Protecció i defensa dels drets dels menors | 305.780 | 2,2 % |

</details>

<details open><summary><b><code>salud_mental</code> — 2,52 M€ (2.521.219 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413E` | Pla autonòmic de drogues | 2.521.219 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,54 M€ (2.539.256 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Integració social d’immigrants | 2.539.256 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 41,39 M€ (41.390.816 €) · 5 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | C03%&.*58(3%$()%*'!0(5(0%3%,&5*58(3%$("!3%$('60+)'5* | 27.296.898 | 65,9 % |
| `751A` | Direcció i serveis generals d’Innovació, Recerca i Turisme | 6.164.190 | 14,9 % |
| `751B` | Promoció turística | 5.005.000 | 12,1 % |
| `761A` | Ordenació i promoció comercial | 2.435.157 | 5,9 % |
| `761B` | Gestió en matèria de joc | 489.571 | 1,2 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,11 M€ (3.112.708 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Promoció, protecció i serveis per a la dona | 3.112.708 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.862,52 M€ · 74 códigos · 40,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | !"#$%$&'(%)*%*+,-.,-,-*/0'0(,#,-*+,*+,1$,*.234%( | 948.729.824 |
| `912A` | !"#$%&'()(*+$&),-&*#(-+,,-&.(-!,)$- | 327.213.020 |
| `521C` | Transport ferroviari | 78.060.549 |
| `562B` | Sanejament i depuració d’aigües | 63.221.460 |
| `562A` | Abastament d’aigua | 48.965.276 |
| `811A` | Fons de contingència | 38.396.436 |
| `121H` | Gestió de recursos humans | 37.716.579 |
| `521A` | Infraestructures bàsiques | 29.088.229 |
| `912B` | =6#!0'(,&.&*%0(.(.>6&'."%&')(5(.$'0%)(%&)($!*.$) | 24.025.426 |
| `455A` | Promoció i serveis de cultura | 21.156.324 |
| `461A` | Promoció i foment de l’esport | 21.013.832 |
| `571D` | Conservació i millora del medi natural | 20.021.665 |
| `141A` | Direcció i serveis generals d’Hisenda i Administracions Públiques | 18.801.372 |
| `522A` | Ports i transport marítim | 15.001.544 |
| `111A` | Activitat legislativa | 13.867.762 |
| `313C` | Mesures judicials i prevenció del delicte | 12.336.129 |
| `126L` | Serveis comuns tecnològics | 11.026.634 |
| `121B` | Direcció i serveis generals de la Conselleria de Presidència | 10.176.938 |
| `521D` | Transport per carretera | 7.774.521 |
| `511B` | Direcció i serveis generals de Territori, Energia i Mobilitat | 6.927.008 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 6.884.358 |
| `723A` | Promoció industrial | 6.091.321 |
| `721A` | Direcció i serveis generals de Treball, Comerç i Indústria | 5.891.692 |
| `223A` | Emergències | 5.786.615 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 5.100.704 |
| … | *resto: 49 códigos* | 79.249.345 |

</details>

### 2018

*Fuente: `memoria_programas.html` · 136 líneas · total extraído **4.981,31 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.555,47 M€ (1.555.473.300 €) · 10 códigos · 31,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.522.460.793 | 97,9 % |
| `413B` | Programes de salut pública | 9.147.925 | 0,6 % |
| `411A` | Direcció i serveis generals de Salut | 8.374.545 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 7.003.054 | 0,5 % |
| `324A` | Salut i prevenció de riscs laborals | 3.218.413 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 1.434.444 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.239.476 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.135.293 | 0,1 % |
| `413F` | D$.&5,*.*589(*!&'0!$(5(G%)'58(3%$("%35*."%&'(5(3%$)()%0:%5)(>.0".*H6'5*) | 794.025 | 0,1 % |
| `411D` | D$.&5,*.*589(.:.$6.*58(5(*.0'%0.(3%()%0:%5) | 665.332 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 936,45 M€ (936.446.757 €) · 14 códigos · 18,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 534.261.803 | 57,1 % |
| `422B` | Educació concertada | 167.916.106 | 17,9 % |
| `421F` | Política i actuacions en matèria universitària | 79.226.649 | 8,5 % |
| `423B` | Altres serveis a l’ensenyament | 61.826.248 | 6,6 % |
| `421A` | Direcció i serveis generals d’Educació i Universitat | 38.110.208 | 4,1 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 33.071.499 | 3,5 % |
| `421K` | Innovació i comunitat educativa | 11.789.404 | 1,3 % |
| `421G` | Formació professional i aprenentatge permanent | 4.003.204 | 0,4 % |
| `421E` | Projectes lingüístics | 2.302.304 | 0,2 % |
| `421C` | A$.&5,*.*58(%36*.'5:.(5(0>C5"(3%(*%&'0%)(%)*!$.0) | 1.345.469 | 0,1 % |
| `421D` | Formació del professorat | 1.177.398 | 0,1 % |
| `571B` | Educació ambiental | 1.006.436 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 246.367 | 0,0 % |
| `421H` | Inspecció educativa | 163.662 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 57,22 M€ (57.219.331 €) · 4 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 37.750.846 | 66,0 % |
| `711A` | Direcció i serveis generals de Medi Ambient, Agricultura i Pesca | 15.375.232 | 26,9 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.196.495 | 3,8 % |
| `531A` | Ordenació del territori i urbanisme | 1.896.758 | 3,3 % |

</details>

<details open><summary><b><code>direccion</code> — 3,38 M€ (3.380.027 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Serveis generals de la Presidència del Govern | 3.380.027 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 29,04 M€ (29.036.244 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 18.994.275 | 65,4 % |
| `431A` | Gestió i foment de l’habitatge social | 5.340.405 | 18,4 % |
| `451A` | Direcció i serveis generals de Cultura, Participació i Esports | 4.701.564 | 16,2 % |

</details>

<details open><summary><b><code>empleo</code> — 99,22 M€ (99.221.099 €) · 4 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 82.112.696 | 82,8 % |
| `322A` | B*6#.*58(5(5&)%0*58($./!0.$(%)#%*+,C6%) | 7.968.191 | 8,0 % |
| `322E` | Impuls del Turisme Sostenible - projectes d’ocupació | 5.659.108 | 5,7 % |
| `322B` | Gestió de les relacions laborals | 3.481.104 | 3,5 % |

</details>

<details open><summary><b><code>idi</code> — 32,42 M€ (32.422.122 €) · 5 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació | 11.896.524 | 36,7 % |
| `541B` | Impuls del Turisme Sostenible - projectes de recerca | 7.691.601 | 23,7 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 6.288.773 | 19,4 % |
| `541A` | Recerca i desenvolupament | 6.175.611 | 19,0 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 369.613 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 155,63 M€ (155.633.935 €) · 4 códigos · 3,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 68.738.373 | 44,2 % |
| `313I` | C$.&5,*.*58(5(!03%&.*58()!*5.$) | 44.216.648 | 28,4 % |
| `314A` | Pensions i prestacions econòmiques | 33.110.563 | 21,3 % |
| `313K` | Direcció i serveis generals de Serveis Socials i Cooperació | 9.568.351 | 6,1 % |

</details>

<details open><summary><b><code>discapacidad</code> — 13,86 M€ (13.858.456 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 9.732.984 | 70,2 % |
| `313G` | Família i unitats de convivència | 3.767.848 | 27,2 % |
| `313F` | Protecció i defensa dels drets dels menors | 357.624 | 2,6 % |

</details>

<details open><summary><b><code>salud_mental</code> — 2,32 M€ (2.323.372 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413E` | Pla autonòmic de drogues | 2.323.372 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,58 M€ (2.584.873 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Integració social d’immigrants | 2.584.873 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 91,64 M€ (91.637.760 €) · 8 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `571H` | Impuls del Turisme Sostenible - projectes mediambientals | 38.428.680 | 41,9 % |
| `751C` | =03%&.*58(3%$()%*'!0(5(0%3%,&5*58(3%$("!3%$('60+)'5* | 25.783.477 | 28,1 % |
| `751D` | Impuls del Turisme Sostenible - projectes turístics | 8.752.550 | 9,6 % |
| `751A` | Direcció i serveis generals d’Innovació, Recerca i Turisme | 7.116.544 | 7,8 % |
| `751B` | Promoció turística | 4.344.795 | 4,7 % |
| `455C` | Impuls del Turisme Sostenible - projectes de patrimoni cultural | 4.156.000 | 4,5 % |
| `761A` | Ordenació i promoció comercial | 2.467.782 | 2,7 % |
| `761B` | Gestió en matèria de joc | 587.932 | 0,6 % |

</details>

<details open><summary><b><code>igualdad</code> — 3,47 M€ (3.474.195 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Promoció, protecció i serveis per a la dona | 3.474.195 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.998,60 M€ · 77 códigos · 40,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | !"#$%$&'(%)*%*+,-.,-,-*/0'0(,#,-*+,*+,1$,*.234%( | 1.020.218.989 |
| `912A` | !"#$%&'()(*+$&),-&*#(-+,,-&.(-!,)$- | 361.511.559 |
| `521C` | Transport ferroviari | 71.166.423 |
| `562B` | Sanejament i depuració d’aigües | 62.348.444 |
| `121H` | Gestió de recursos humans | 40.239.559 |
| `562A` | Abastament d’aigua | 32.692.425 |
| `551C` | Mitjans de comunicació social | 31.100.000 |
| `521A` | Infraestructures bàsiques | 29.541.561 |
| `461A` | Promoció i foment de l’esport | 29.056.444 |
| `912B` | =6#!0'(,&.&*%0(.(.>6&'."%&')(5(.$'0%)(%&)($!*.$) | 28.874.785 |
| `455A` | Promoció i serveis de cultura | 23.685.144 |
| `571D` | Conservació i millora del medi natural | 21.130.148 |
| `811A` | Fons de contingència | 20.432.719 |
| `141A` | Direcció i serveis generals d’Hisenda i Administracions Públiques | 18.727.502 |
| `522A` | Ports i transport marítim | 14.903.006 |
| `111A` | Activitat legislativa | 14.322.530 |
| `521D` | Transport per carretera | 13.234.237 |
| `126L` | Serveis comuns tecnològics | 12.934.498 |
| `313C` | Mesures judicials i prevenció del delicte | 12.756.984 |
| `121B` | Direcció i serveis generals de la Conselleria de Presidència | 9.395.087 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 8.444.555 |
| `511B` | Direcció i serveis generals de Territori, Energia i Mobilitat | 7.531.795 |
| `723A` | Promoció industrial | 7.491.821 |
| `223A` | Emergències | 6.384.537 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 5.913.819 |
| … | *resto: 52 códigos* | 94.562.537 |

</details>

### 2019

*Fuente: `memoria_programas.html` · 141 líneas · total extraído **5.436,32 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.708,00 M€ (1.708.001.124 €) · 10 códigos · 31,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.672.339.390 | 97,9 % |
| `413B` | Programes de salut pública | 9.752.425 | 0,6 % |
| `411A` | Direcció i serveis generals de Salut | 8.585.789 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 7.601.526 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 4.091.572 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 1.577.531 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.332.211 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.166.858 | 0,1 % |
| `413F` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:15)(cid:3)(cid:70)(cid:82)(cid:81)(cid:87)(cid:85)(cid:82)(cid:79)(cid:3)(cid:76)(cid:3)(cid:74)(cid:72)(cid:86)(cid:87)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:72)(cid:71)(cid:76)(cid:70)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:79)(cid:86)(cid:3)(cid:86)(cid:72)(cid:85)(cid:89)(cid:72)(cid:76)(cid:86)(cid:3)(cid:73)(cid:68)(cid:85)(cid:80)(cid:68)(cid:70)(cid:113)(cid:88)(cid:87)(cid:76)(cid:70)(cid:86) | 805.682 | 0,0 % |
| `411D` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:15)(cid:3)(cid:68)(cid:89)(cid:68)(cid:79)(cid:88)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:70)(cid:68)(cid:85)(cid:87)(cid:72)(cid:85)(cid:68)(cid:3)(cid:71)(cid:72)(cid:3)(cid:86)(cid:72)(cid:85)(cid:89)(cid:72)(cid:76)(cid:86) | 748.140 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.001,14 M€ (1.001.143.014 €) · 14 códigos · 18,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 574.941.323 | 57,4 % |
| `422B` | Educació concertada | 174.966.868 | 17,5 % |
| `421F` | Política i actuacions en matèria universitària | 82.043.992 | 8,2 % |
| `423B` | Altres serveis a l’ensenyament | 66.853.557 | 6,7 % |
| `421A` | Direcció i serveis generals d’Educació i Universitat | 38.618.941 | 3,9 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 36.310.156 | 3,6 % |
| `421K` | Innovació i comunitat educativa | 16.356.547 | 1,6 % |
| `421G` | Formació professional i aprenentatge permanent | 4.252.468 | 0,4 % |
| `421E` | (cid:51)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:79)(cid:76)(cid:81)(cid:74)(cid:129)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70)(cid:86) | 2.497.597 | 0,2 % |
| `421C` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:72)(cid:71)(cid:88)(cid:70)(cid:68)(cid:87)(cid:76)(cid:89)(cid:68)(cid:3)(cid:76)(cid:3)(cid:85)(cid:113)(cid:74)(cid:76)(cid:80)(cid:3)(cid:71)(cid:72)(cid:3)(cid:70)(cid:72)(cid:81)(cid:87)(cid:85)(cid:72)(cid:86)(cid:3)(cid:72)(cid:86)(cid:70)(cid:82)(cid:79)(cid:68)(cid:85)(cid:86) | 1.548.975 | 0,2 % |
| `421D` | Formació del professorat | 1.340.631 | 0,1 % |
| `571B` | Educació ambiental | 1.035.250 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 237.146 | 0,0 % |
| `421H` | Inspecció educativa | 139.563 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 69,11 M€ (69.108.740 €) · 5 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 38.034.018 | 55,0 % |
| `711A` | Direcció i serveis generals de Medi Ambient, Agricultura i Pesca | 17.292.288 | 25,0 % |
| `714A` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:68)(cid:74)(cid:85)(cid:76)(cid:70)(cid:88)(cid:79)(cid:87)(cid:88)(cid:85)(cid:68) | 9.969.573 | 14,4 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.232.732 | 3,2 % |
| `531A` | Ordenació del territori i urbanisme | 1.580.129 | 2,3 % |

</details>

<details open><summary><b><code>direccion</code> — 3,34 M€ (3.344.591 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Serveis generals de la Presidència del Govern | 3.344.591 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 65,13 M€ (65.127.226 €) · 4 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431C` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:75)(cid:68)(cid:69)(cid:76)(cid:87)(cid:68)(cid:87)(cid:74)(cid:72) | 24.293.092 | 37,3 % |
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 23.292.365 | 35,8 % |
| `431A` | Gestió i foment de l’habitatge social | 12.678.010 | 19,5 % |
| `451A` | Direcció i serveis generals de Cultura, Participació i Esports | 4.863.759 | 7,5 % |

</details>

<details open><summary><b><code>empleo</code> — 111,71 M€ (111.709.104 €) · 4 códigos · 2,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 90.457.862 | 81,0 % |
| `322A` | (cid:50)(cid:70)(cid:88)(cid:83)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:76)(cid:81)(cid:86)(cid:72)(cid:85)(cid:70)(cid:76)(cid:121)(cid:3)(cid:79)(cid:68)(cid:69)(cid:82)(cid:85)(cid:68)(cid:79)(cid:3)(cid:72)(cid:86)(cid:83)(cid:72)(cid:70)(cid:116)(cid:191)(cid:84)(cid:88)(cid:72)(cid:86) | 8.709.222 | 7,8 % |
| `322E` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:82)(cid:70)(cid:88)(cid:83)(cid:68)(cid:70)(cid:76)(cid:121) | 8.659.941 | 7,8 % |
| `322B` | Gestió de les relacions laborals | 3.882.079 | 3,5 % |

</details>

<details open><summary><b><code>idi</code> — 52,21 M€ (52.206.548 €) · 6 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561B` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:68)(cid:76)(cid:74)(cid:88)(cid:68) | 17.894.257 | 34,3 % |
| `542A` | Innovació | 12.775.275 | 24,5 % |
| `541B` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:85)(cid:72)(cid:70)(cid:72)(cid:85)(cid:70)(cid:68) | 7.311.388 | 14,0 % |
| `541A` | Recerca i desenvolupament | 7.038.541 | 13,5 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 6.795.257 | 13,0 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 391.830 | 0,8 % |

</details>

<details open><summary><b><code>dependencia</code> — 146,16 M€ (146.164.142 €) · 4 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 55.683.847 | 38,1 % |
| `313I` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:82)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:86)(cid:82)(cid:70)(cid:76)(cid:68)(cid:79)(cid:86) | 46.804.169 | 32,0 % |
| `314A` | Pensions i prestacions econòmiques | 33.172.672 | 22,7 % |
| `313K` | Direcció i serveis generals de Serveis Socials i Cooperació | 10.503.454 | 7,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 18,04 M€ (18.035.804 €) · 3 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 13.448.087 | 74,6 % |
| `313G` | Família i unitats de convivència | 4.220.451 | 23,4 % |
| `313F` | Protecció i defensa dels drets dels menors | 367.266 | 2,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 2,32 M€ (2.324.612 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `413E` | Pla autonòmic de drogues | 2.324.612 | 100,0 % |

</details>

<details open><summary><b><code>diversidad</code> — 2,60 M€ (2.598.232 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Integració social d’immigrants | 2.598.232 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 37,97 M€ (37.965.673 €) · 6 códigos · 0,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | (cid:50)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:86)(cid:72)(cid:70)(cid:87)(cid:82)(cid:85)(cid:3)(cid:76)(cid:3)(cid:85)(cid:72)(cid:71)(cid:72)(cid:191)(cid:81)(cid:76)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:82)(cid:71)(cid:72)(cid:79)(cid:3)(cid:87)(cid:88)(cid:85)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70) | 14.654.625 | 38,6 % |
| `751D` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:87)(cid:88)(cid:85)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70)(cid:86) | 11.507.295 | 30,3 % |
| `751A` | Direcció i serveis generals d’Innovació, Recerca i Turisme | 6.617.760 | 17,4 % |
| `761A` | Ordenació i promoció comercial i empresarial | 3.454.775 | 9,1 % |
| `761B` | (cid:42)(cid:72)(cid:86)(cid:87)(cid:76)(cid:121)(cid:3)(cid:72)(cid:81)(cid:3)(cid:80)(cid:68)(cid:87)(cid:113)(cid:85)(cid:76)(cid:68)(cid:3)(cid:71)(cid:72)(cid:3)(cid:77)(cid:82)(cid:70) | 1.071.218 | 2,8 % |
| `751B` | Promoció turística | 660.000 | 1,7 % |

</details>

<details open><summary><b><code>igualdad</code> — 7,26 M€ (7.262.741 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Promoció, protecció i serveis per a la dona | 7.262.741 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.211,33 M€ · 81 códigos · 40,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | (cid:36)(cid:80)(cid:82)(cid:85)(cid:87)(cid:76)(cid:87)(cid:93)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:86)(cid:83)(cid:72)(cid:86)(cid:72)(cid:86)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:71)(cid:72)(cid:88)(cid:87)(cid:72)(cid:3)(cid:83)(cid:126)(cid:69)(cid:79)(cid:76)(cid:70) | 1.137.537.949 |
| `912A` | (cid:54)(cid:88)(cid:83)(cid:82)(cid:85)(cid:87)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:3)(cid:68)(cid:79)(cid:86)(cid:3)(cid:70)(cid:82)(cid:81)(cid:86)(cid:72)(cid:79)(cid:79)(cid:86)(cid:3)(cid:76)(cid:81)(cid:86)(cid:88)(cid:79)(cid:68)(cid:85)(cid:86) | 428.085.543 |
| `521C` | Transport ferroviari | 74.903.347 |
| `562B` | (cid:54)(cid:68)(cid:81)(cid:72)(cid:77)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:83)(cid:88)(cid:85)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:182)(cid:68)(cid:76)(cid:74)(cid:129)(cid:72)(cid:86) | 61.390.087 |
| `912B` | (cid:54)(cid:88)(cid:83)(cid:82)(cid:85)(cid:87)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:3)(cid:68)(cid:3)(cid:68)(cid:77)(cid:88)(cid:81)(cid:87)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:86)(cid:3)(cid:76)(cid:3)(cid:68)(cid:79)(cid:87)(cid:85)(cid:72)(cid:86)(cid:3)(cid:72)(cid:81)(cid:86)(cid:3)(cid:79)(cid:82)(cid:70)(cid:68)(cid:79)(cid:86) | 31.895.619 |
| `551C` | (cid:48)(cid:76)(cid:87)(cid:77)(cid:68)(cid:81)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:70)(cid:82)(cid:80)(cid:88)(cid:81)(cid:76)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:86)(cid:82)(cid:70)(cid:76)(cid:68)(cid:79) | 31.100.000 |
| `521A` | Infraestructures bàsiques | 29.740.201 |
| `562A` | Abastament d’aigua | 28.361.503 |
| `455A` | Promoció i serveis de cultura | 25.341.517 |
| `461A` | Promoció i foment de l’esport | 23.069.423 |
| `811A` | Fons de contingència | 22.170.319 |
| `521D` | Transport per carretera | 21.582.127 |
| `571D` | Conservació i millora del medi natural | 21.531.919 |
| `141A` | Direcció i serveis generals d’Hisenda i Administracions Públiques | 18.907.080 |
| `522A` | Ports i transport marítim | 15.956.002 |
| `121H` | Gestió de recursos humans | 15.090.358 |
| `571H` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:80)(cid:72)(cid:71)(cid:76)(cid:68)(cid:80)(cid:69)(cid:76)(cid:72)(cid:81)(cid:87)(cid:68)(cid:79)(cid:86) | 14.740.232 |
| `111A` | Activitat legislativa | 14.362.258 |
| `455C` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:83)(cid:68)(cid:87)(cid:85)(cid:76)(cid:80)(cid:82)(cid:81)(cid:76)(cid:3)(cid:70)(cid:88)(cid:79)(cid:87)(cid:88)(cid:85)(cid:68)(cid:79) | 14.167.686 |
| `126L` | Serveis comuns tecnològics | 14.120.572 |
| `313C` | (cid:48)(cid:72)(cid:86)(cid:88)(cid:85)(cid:72)(cid:86)(cid:3)(cid:77)(cid:88)(cid:71)(cid:76)(cid:70)(cid:76)(cid:68)(cid:79)(cid:86)(cid:3)(cid:76)(cid:3)(cid:83)(cid:85)(cid:72)(cid:89)(cid:72)(cid:81)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:71)(cid:72)(cid:79)(cid:76)(cid:70)(cid:87)(cid:72) | 13.660.667 |
| `121B` | Direcció i serveis generals de la Conselleria de Presidència | 9.437.139 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 9.132.628 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 8.165.965 |
| `223A` | Emergències | 7.147.518 |
| … | *resto: 56 códigos* | 119.729.319 |

</details>

### 2020

*Fuente: `memoria_programas.html` · 150 líneas · total extraído **5.772,63 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.706,61 M€ (1.706.612.123 €) · 10 códigos · 29,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.669.635.952 | 97,8 % |
| `413B` | Programes de salut pública | 10.816.783 | 0,6 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut i Consum | 8.484.679 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 7.551.250 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 4.203.420 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 1.695.471 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.395.236 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.175.707 | 0,1 % |
| `413F` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:15)(cid:3)(cid:70)(cid:82)(cid:81)(cid:87)(cid:85)(cid:82)(cid:79)(cid:3)(cid:76)(cid:3)(cid:74)(cid:72)(cid:86)(cid:87)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:72)(cid:71)(cid:76)(cid:70)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:79)(cid:86)(cid:3)(cid:86)(cid:72)(cid:85)(cid:89)(cid:72)(cid:76)(cid:86)(cid:3)(cid:73)(cid:68)(cid:85)(cid:80)(cid:68)(cid:70)(cid:113)(cid:88)(cid:87)(cid:76)(cid:70)(cid:86) | 836.491 | 0,0 % |
| `411D` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:15)(cid:3)(cid:68)(cid:89)(cid:68)(cid:79)(cid:88)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:70)(cid:68)(cid:85)(cid:87)(cid:72)(cid:85)(cid:68)(cid:3)(cid:71)(cid:72)(cid:3)(cid:86)(cid:72)(cid:85)(cid:89)(cid:72)(cid:76)(cid:86) | 817.134 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.006,29 M€ (1.006.286.707 €) · 15 códigos · 17,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 588.175.518 | 58,5 % |
| `422B` | Educació concertada | 177.298.729 | 17,6 % |
| `421F` | Política i actuacions en matèria universitària | 78.069.206 | 7,8 % |
| `423B` | Altres serveis a l’ensenyament | 54.176.997 | 5,4 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació,Universitat i Recerca | 41.870.231 | 4,2 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 36.256.610 | 3,6 % |
| `421K` | Innovació i comunitat educativa | 16.564.924 | 1,6 % |
| `421G` | Formació professional i aprenentatge permanent | 4.125.238 | 0,4 % |
| `421J` | Ensenyaments artístics superiors | 4.036.432 | 0,4 % |
| `421E` | (cid:47)(cid:79)(cid:72)(cid:81)(cid:74)(cid:129)(cid:72)(cid:86)(cid:3)(cid:72)(cid:86)(cid:87)(cid:85)(cid:68)(cid:81)(cid:74)(cid:72)(cid:85)(cid:72)(cid:86)(cid:3)(cid:76)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:76)(cid:81)(cid:87)(cid:72)(cid:85)(cid:81)(cid:68)(cid:70)(cid:76)(cid:82)(cid:81)(cid:68)(cid:79)(cid:86) | 2.317.505 | 0,2 % |
| `421C` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:72)(cid:71)(cid:88)(cid:70)(cid:68)(cid:87)(cid:76)(cid:89)(cid:68)(cid:3)(cid:76)(cid:3)(cid:85)(cid:113)(cid:74)(cid:76)(cid:80)(cid:3)(cid:71)(cid:72)(cid:3)(cid:73)(cid:88)(cid:81)(cid:70)(cid:76)(cid:82)(cid:81)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:71)(cid:72)(cid:3)(cid:70)(cid:72)(cid:81)(cid:87)(cid:85)(cid:72)(cid:86)(cid:3)(cid:72)(cid:86)(cid:70)(cid:82)(cid:79)(cid:68)(cid:85)(cid:86) | 1.597.709 | 0,2 % |
| `571B` | Educació ambiental | 1.012.437 | 0,1 % |
| `421D` | Formació del professorat | 465.000 | 0,0 % |
| `421B` | Ordenació general del sistema educatiu | 190.624 | 0,0 % |
| `421H` | Inspecció educativa | 129.547 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 53,48 M€ (53.484.843 €) · 8 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 36.002.718 | 67,3 % |
| `714A` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)฀(cid:68)(cid:74)(cid:85)(cid:76)(cid:70)(cid:88)(cid:79)(cid:87)(cid:88)(cid:85)(cid:68) | 9.020.943 | 16,9 % |
| `711A` | Direcció i serveis generals de Medi Ambient, Agricultura i Pesca | 4.231.142 | 7,9 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.123.060 | 4,0 % |
| `718B` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:86)(cid:72)(cid:70)(cid:87)(cid:82)(cid:85)(cid:3)(cid:83)(cid:72)(cid:86)(cid:84)(cid:88)(cid:72)(cid:85) | 1.019.520 | 1,9 % |
| `531A` | Ordenació del territori i urbanisme | 938.002 | 1,8 % |
| `714C` | Polítiques alimentàries | 109.458 | 0,2 % |
| `714D` | Promoció i regulació de mercats agraris | 40.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,38 M€ (3.380.395 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 3.380.395 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 63,78 M€ (63.782.390 €) · 3 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431C` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)฀(cid:75)(cid:68)(cid:69)(cid:76)(cid:87)(cid:68)(cid:87)(cid:74)(cid:72) | 27.628.922 | 43,3 % |
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 24.402.122 | 38,3 % |
| `431A` | Gestió i foment de l’habitatge social | 11.751.346 | 18,4 % |

</details>

<details open><summary><b><code>empleo</code> — 21,73 M€ (21.732.646 €) · 5 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322E` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:82)(cid:70)(cid:88)(cid:83)(cid:68)(cid:70)(cid:76)(cid:121) | 9.802.606 | 45,1 % |
| `322A` | (cid:50)(cid:70)(cid:88)(cid:83)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:76)(cid:81)(cid:86)(cid:72)(cid:85)(cid:70)(cid:76)(cid:121)(cid:3)(cid:79)(cid:68)(cid:69)(cid:82)(cid:85)(cid:68)(cid:79)(cid:3)(cid:72)(cid:86)(cid:83)(cid:72)(cid:70)(cid:116)(cid:191)(cid:84)(cid:88)(cid:72)(cid:86) | 5.820.000 | 26,8 % |
| `322B` | Gestió de les relacions laborals | 3.264.629 | 15,0 % |
| `322F` | Autocupació i economia social | 2.307.351 | 10,6 % |
| `322C` | Foment de la responsabilitat social corporativa | 538.060 | 2,5 % |

</details>

<details open><summary><b><code>idi</code> — 36,80 M€ (36.796.087 €) · 7 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació | 13.430.296 | 36,5 % |
| `541A` | Recerca i desenvolupament | 6.933.190 | 18,8 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 5.559.635 | 15,1 % |
| `561B` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)฀(cid:68)(cid:76)(cid:74)(cid:88)(cid:68) | 5.085.972 | 13,8 % |
| `541B` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:85)(cid:72)(cid:70)(cid:72)(cid:85)(cid:70)(cid:68) | 3.390.579 | 9,2 % |
| `542B` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:182)(cid:76)(cid:81)(cid:81)(cid:82)(cid:89)(cid:68)(cid:70)(cid:76)(cid:121) | 1.998.525 | 5,4 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 397.890 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 117,80 M€ (117.802.023 €) · 5 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 54.391.025 | 46,2 % |
| `314A` | Pensions i prestacions econòmiques | 33.284.294 | 28,3 % |
| `313I` | (cid:51)(cid:79)(cid:68)(cid:81)(cid:76)(cid:191)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:82)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:86)(cid:82)(cid:70)(cid:76)(cid:68)(cid:79)(cid:86) | 13.027.365 | 11,1 % |
| `313K` | Direcció i serveis generals de la Conselleria de Serveis Socials i Esports | 11.872.388 | 10,1 % |
| `313L` | Equipaments de serveis socials | 5.226.951 | 4,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 24,46 M€ (24.463.826 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 20.219.826 | 82,7 % |
| `313G` | Família i unitats de convivència | 3.952.204 | 16,2 % |
| `313F` | Protecció i defensa dels drets dels menors | 291.796 | 1,2 % |

</details>

<details open><summary><b><code>salud_mental</code> — 32,56 M€ (32.562.726 €) · 2 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 30.577.913 | 93,9 % |
| `413E` | Pla autonòmic de drogues | 1.984.813 | 6,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,43 M€ (434.379 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316A` | Drets i Diversitat | 434.379 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 33,47 M€ (33.472.937 €) · 7 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | (cid:50)(cid:85)(cid:71)(cid:72)(cid:81)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:86)(cid:72)(cid:70)(cid:87)(cid:82)(cid:85)(cid:3)(cid:76)(cid:3)(cid:85)(cid:72)(cid:71)(cid:72)(cid:191)(cid:81)(cid:76)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:80)(cid:82)(cid:71)(cid:72)(cid:79)(cid:3)(cid:87)(cid:88)(cid:85)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70) | 13.812.823 | 41,3 % |
| `751D` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:87)(cid:88)(cid:85)(cid:116)(cid:86)(cid:87)(cid:76)(cid:70)(cid:86) | 9.050.466 | 27,0 % |
| `121L` | Direcció i serveis generals de la Conselleria de Model Econòmic, Turisme i Treball | 6.316.371 | 18,9 % |
| `761A` | Ordenació i promoció comercial | 2.187.385 | 6,5 % |
| `761C` | Promoció empresarial i economia circular | 1.193.900 | 3,6 % |
| `761B` | (cid:42)(cid:72)(cid:86)(cid:87)(cid:76)(cid:121)(cid:3)(cid:72)(cid:81)(cid:3)(cid:80)(cid:68)(cid:87)(cid:113)(cid:85)(cid:76)(cid:68)(cid:3)(cid:71)(cid:72)(cid:3)(cid:77)(cid:82)(cid:70) | 651.992 | 1,9 % |
| `751B` | Promoció turística | 260.000 | 0,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,53 M€ (16.531.460 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B` | Direcció i serveis generals de la Conselleria de Presidència,Cultura i Igualtat | 10.803.677 | 65,4 % |
| `323C` | Polítiques públiques d’igualtat | 5.727.783 | 34,6 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.655,29 M€ · 81 códigos · 46,0 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | (cid:36)(cid:80)(cid:82)(cid:85)(cid:87)(cid:76)(cid:87)(cid:93)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:86)(cid:83)(cid:72)(cid:86)(cid:72)(cid:86)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:71)(cid:72)(cid:88)(cid:87)(cid:72)(cid:3)(cid:83)(cid:126)(cid:69)(cid:79)(cid:76)(cid:70) | 1.620.265.842 |
| `912A` | (cid:54)(cid:88)(cid:83)(cid:82)(cid:85)(cid:87)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:3)(cid:68)(cid:79)(cid:86)(cid:3)(cid:70)(cid:82)(cid:81)(cid:86)(cid:72)(cid:79)(cid:79)(cid:86)(cid:3)(cid:76)(cid:81)(cid:86)(cid:88)(cid:79)(cid:68)(cid:85)(cid:86) | 414.667.650 |
| `521C` | Transport ferroviari | 63.488.007 |
| `562B` | (cid:54)(cid:68)(cid:81)(cid:72)(cid:77)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:3)(cid:76)(cid:3)(cid:71)(cid:72)(cid:83)(cid:88)(cid:85)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:182)(cid:68)(cid:76)(cid:74)(cid:129)(cid:72)(cid:86) | 61.432.299 |
| `551C` | (cid:48)(cid:76)(cid:87)(cid:77)(cid:68)(cid:81)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:70)(cid:82)(cid:80)(cid:88)(cid:81)(cid:76)(cid:70)(cid:68)(cid:70)(cid:76)(cid:121)(cid:3)(cid:86)(cid:82)(cid:70)(cid:76)(cid:68)(cid:79) | 31.100.000 |
| `912B` | (cid:54)(cid:88)(cid:83)(cid:82)(cid:85)(cid:87)(cid:3)(cid:191)(cid:81)(cid:68)(cid:81)(cid:70)(cid:72)(cid:85)(cid:3)(cid:68)(cid:3)(cid:68)(cid:77)(cid:88)(cid:81)(cid:87)(cid:68)(cid:80)(cid:72)(cid:81)(cid:87)(cid:86)(cid:3)(cid:76)(cid:3)(cid:68)(cid:79)(cid:87)(cid:85)(cid:72)(cid:86)(cid:3)(cid:72)(cid:81)(cid:86)(cid:3)(cid:79)(cid:82)(cid:70)(cid:68)(cid:79)(cid:86) | 30.420.589 |
| `521A` | Infraestructures bàsiques | 30.113.526 |
| `562A` | Abastament d’aigua | 25.056.019 |
| `455A` | Promoció i serveis de cultura | 24.767.326 |
| `811A` | Fons de contingència | 21.919.170 |
| `571D` | Conservació i millora del medi natural | 21.686.616 |
| `461A` | Promoció i foment de l’esport | 20.276.034 |
| `455C` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)(cid:72)(cid:3)(cid:83)(cid:68)(cid:87)(cid:85)(cid:76)(cid:80)(cid:82)(cid:81)(cid:76)(cid:3)(cid:70)(cid:88)(cid:79)(cid:87)(cid:88)(cid:85)(cid:68)(cid:79) | 18.552.323 |
| `141A` | Direcció i serveis generals de la Conselleria d’Hisenda i Relacions Exteriors | 17.777.481 |
| `521D` | Transport per carretera | 15.594.741 |
| `522A` | Ports i transport marítim | 15.521.786 |
| `111A` | Activitat legislativa | 14.715.088 |
| `571J` | Direcció i serv.generals C.Medi Ambient i Territor | 14.306.418 |
| `313C` | (cid:48)(cid:72)(cid:86)(cid:88)(cid:85)(cid:72)(cid:86)(cid:3)(cid:77)(cid:88)(cid:71)(cid:76)(cid:70)(cid:76)(cid:68)(cid:79)(cid:86)(cid:3)(cid:76)(cid:3)(cid:83)(cid:85)(cid:72)(cid:89)(cid:72)(cid:81)(cid:70)(cid:76)(cid:121)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:71)(cid:72)(cid:79)(cid:76)(cid:70)(cid:87)(cid:72) | 13.866.547 |
| `121H` | Gestió de recursos humans | 13.544.690 |
| `126L` | Serveis comuns tecnològics | 12.551.769 |
| `731B` | (cid:44)(cid:80)(cid:83)(cid:88)(cid:79)(cid:86)(cid:3)(cid:71)(cid:72)(cid:79)(cid:3)(cid:55)(cid:88)(cid:85)(cid:76)(cid:86)(cid:80)(cid:72)(cid:3)(cid:54)(cid:82)(cid:86)(cid:87)(cid:72)(cid:81)(cid:76)(cid:69)(cid:79)(cid:72)(cid:3)(cid:16)(cid:3)(cid:83)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:71)฀(cid:72)(cid:81)(cid:72)(cid:85)(cid:74)(cid:76)(cid:68) | 11.360.000 |
| `521E` | (cid:44)(cid:55)(cid:54)(cid:3)(cid:51)(cid:85)(cid:82)(cid:77)(cid:72)(cid:70)(cid:87)(cid:72)(cid:86)(cid:3)(cid:87)(cid:85)(cid:68)(cid:81)(cid:86)(cid:83)(cid:82)(cid:85)(cid:87)(cid:3)(cid:87)(cid:72)(cid:85)(cid:85)(cid:72)(cid:86)(cid:87)(cid:85)(cid:72) | 10.007.321 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 9.796.380 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 7.514.504 |
| … | *resto: 56 códigos* | 114.987.475 |

</details>

### 2021

*Fuente: `memoria_programas.html` · 143 líneas · total extraído **5.847,62 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.761,50 M€ (1.761.504.096 €) · 10 códigos · 30,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.722.436.960 | 97,8 % |
| `413B` | Programes de salut pública | 12.520.369 | 0,7 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut i Consum | 8.506.791 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 7.678.501 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 4.453.926 | 0,3 % |
| `413A` | Acreditació, docència i recerca en salut | 1.581.802 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.352.209 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.181.596 | 0,1 % |
| `411D` | Planificació, avaluació i cartera de serveis | 945.934 | 0,1 % |
| `413F` | Planificació, control i gestió del medicament i dels serveis farmacèutics | 846.008 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.021,26 M€ (1.021.264.016 €) · 15 códigos · 17,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 597.290.605 | 58,5 % |
| `422B` | Educació concertada | 177.911.477 | 17,4 % |
| `421F` | Política i actuacions en matèria universitària | 80.907.305 | 7,9 % |
| `423B` | Altres serveis a l’ensenyament | 55.770.924 | 5,5 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació, Universitat i Recerca | 44.669.335 | 4,4 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 35.220.356 | 3,4 % |
| `421K` | Innovació i comunitat educativa | 16.051.148 | 1,6 % |
| `421J` | Ensenyaments artístics superiors | 4.196.000 | 0,4 % |
| `421G` | Formació professional i aprenentatge permanent | 4.059.412 | 0,4 % |
| `421E` | Llengües estrangeres i projectes internacionals | 1.628.000 | 0,2 % |
| `421C` | Planificació educativa i règim de funcionament de centres escolars | 1.601.614 | 0,2 % |
| `571B` | Educació ambiental | 1.060.454 | 0,1 % |
| `421D` | Formació del professorat | 445.100 | 0,0 % |
| `421B` | Ordenació general del sistema educatiu | 322.192 | 0,0 % |
| `421H` | Inspecció educativa | 130.094 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 49,27 M€ (49.266.969 €) · 6 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 39.840.397 | 80,9 % |
| `711A` | Direcció i serveis generals de la Conselleria d’Agricultura, Pesca i Alimentació | 5.099.807 | 10,4 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.371.209 | 4,8 % |
| `531A` | Ordenació del territori i urbanisme | 1.193.826 | 2,4 % |
| `714C` | Polítiques alimentàries | 461.730 | 0,9 % |
| `714D` | Promoció i regulació dels mercats agraris | 300.000 | 0,6 % |

</details>

<details open><summary><b><code>direccion</code> — 3,25 M€ (3.254.225 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 3.254.225 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 35,66 M€ (35.663.347 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 19.017.875 | 53,3 % |
| `431A` | Gestió i foment de l’habitatge social | 11.819.028 | 33,1 % |
| `511B` | Direcció i serveis generals de la Conselleria de Mobilitat i Habitatge | 4.826.444 | 13,5 % |

</details>

<details open><summary><b><code>empleo</code> — 105,06 M€ (105.056.584 €) · 5 códigos · 1,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 92.608.872 | 88,2 % |
| `322A` | Ocupació i inserció laboral específiques | 5.820.000 | 5,5 % |
| `322B` | Gestió de les relacions laborals | 3.658.726 | 3,5 % |
| `322F` | Autocupació i economia social | 2.428.872 | 2,3 % |
| `322C` | Foment de la responsabilitat social corporativa | 540.114 | 0,5 % |

</details>

<details open><summary><b><code>idi</code> — 29,62 M€ (29.618.317 €) · 5 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació | 12.821.321 | 43,3 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 7.893.771 | 26,7 % |
| `541A` | Recerca i desenvolupament | 6.848.099 | 23,1 % |
| `541B` | Impuls del Turisme Sostenible - projectes de recerca | 1.540.000 | 5,2 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 515.126 | 1,7 % |

</details>

<details open><summary><b><code>dependencia</code> — 127,90 M€ (127.903.857 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 56.607.884 | 44,3 % |
| `314A` | Pensions i prestacions econòmiques | 46.116.883 | 36,1 % |
| `313I` | Planificació, ordenació i formació socials | 14.693.591 | 11,5 % |
| `313L` | Equipaments de serveis socials | 10.485.499 | 8,2 % |

</details>

<details open><summary><b><code>discapacidad</code> — 25,41 M€ (25.413.028 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 20.196.255 | 79,5 % |
| `313G` | Família i unitats de convivència | 4.797.662 | 18,9 % |
| `313F` | Protecció i defensa dels drets dels menors | 419.111 | 1,6 % |

</details>

<details open><summary><b><code>salud_mental</code> — 29,90 M€ (29.895.936 €) · 2 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 27.535.336 | 92,1 % |
| `413E` | Pla autonòmic de drogues | 2.360.600 | 7,9 % |

</details>

<details open><summary><b><code>diversidad</code> — 0,40 M€ (402.942 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316A` | Drets i diversitat | 402.942 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 35,34 M€ (35.338.649 €) · 8 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `561B` | Impuls del Turisme Sostenible - projectes daigua | 7.660.805 | 21,7 % |
| `121L` | Direcció i serveis generals de la Conselleria de Model Econòmic, Turisme i Treball | 7.299.579 | 20,7 % |
| `751D` | Impuls del Turisme Sostenible - projectes turístics | 6.529.825 | 18,5 % |
| `751C` | Ordenació del sector i redefinició del model turístic | 6.212.912 | 17,6 % |
| `761A` | Ordenació i promoció comercial | 3.930.386 | 11,1 % |
| `761C` | Promoció empresarial i economia circular | 1.417.650 | 4,0 % |
| `751B` | Promoció turística | 1.400.000 | 4,0 % |
| `761B` | Gestió en matèria de joc | 887.492 | 2,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 16,40 M€ (16.401.438 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B` | Direcció i serveis generals de la Conselleria de Presidència, Cultura i Igualtat | 10.541.330 | 64,3 % |
| `323C` | Polítiques públiques d’igualtat | 5.860.108 | 35,7 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.606,63 M€ · 78 códigos · 44,6 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Amortització i despeses financeres de deute públic | 1.246.273.564 |
| `912A` | Suport financer als consells insulars | 405.957.875 |
| `413G` | Accions públiques relatives a la COVID-19 | 229.889.253 |
| `141G` | Gestió dels fons procedents de la Unió Europea | 100.829.683 |
| `521C` | Transport ferroviari | 67.556.426 |
| `562B` | Sanejament i depuració d’aigües | 63.211.247 |
| `811A` | Fons de contingència | 39.208.751 |
| `551C` | Mitjans de comunicació social | 32.900.000 |
| `521A` | Infraestructures bàsiques | 30.479.099 |
| `912B` | Suport financer a ajuntaments i altres ens locals | 26.629.178 |
| `455A` | Promoció i serveis de cultura | 25.193.835 |
| `571D` | Conservació i millora del medi natural | 21.924.156 |
| `521D` | Transport per carretera | 21.125.992 |
| `562A` | Abastament d’aigua | 20.731.926 |
| `461A` | Promoció i foment de l’esport | 20.539.381 |
| `141A` | Direcció i serveis generals de la Conselleria d’Hisenda i Relacions Exteriors | 17.857.176 |
| `522A` | Ports i transport marítim | 15.609.732 |
| `571J` | Direcció i serveis general de la Conselleria de Medi Ambient i Territori | 14.788.889 |
| `111A` | Activitat legislativa | 14.715.088 |
| `313C` | Mesures judicials i prevenció del delicte | 14.546.426 |
| `126L` | Serveis comuns tecnològics | 13.374.401 |
| `121H` | Gestió de recursos humans | 13.246.849 |
| `313K` | Direcció i serveis generals de la Conselleria d’Afers Socials i Esports | 12.088.779 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 9.492.694 |
| `521B` | Ordenació i inspecció del transport terrestre | 8.696.667 |
| … | *resto: 53 códigos* | 119.765.333 |

</details>

### 2022

*Fuente: `memoria_programas.html` · 143 líneas · total extraído **6.368,44 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 1.939,28 M€ (1.939.280.479 €) · 10 códigos · 30,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 1.884.477.450 | 97,2 % |
| `411D` | Planificació, avaluació i cartera de serveis | 14.488.115 | 0,7 % |
| `413B` | Programes de salut pública | 13.143.854 | 0,7 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut i Consum | 9.422.801 | 0,5 % |
| `413C` | Sanitat ambiental i alimentària | 7.918.432 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 4.558.739 | 0,2 % |
| `413A` | Acreditació, docència i recerca en salut | 1.655.652 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.432.867 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.231.621 | 0,1 % |
| `413F` | Planificació, control i gestió del medicament i dels serveis farmacèutics | 950.948 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.136,37 M€ (1.136.369.323 €) · 15 códigos · 17,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 635.116.279 | 55,9 % |
| `422B` | Educació concertada | 185.044.856 | 16,3 % |
| `421F` | Política i actuacions en matèria universitària | 88.373.258 | 7,8 % |
| `421K` | Innovació i comunitat educativa | 66.974.856 | 5,9 % |
| `423B` | Altres serveis a l’ensenyament | 44.454.635 | 3,9 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació i Formació Professional | 44.273.348 | 3,9 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 38.382.470 | 3,4 % |
| `421G` | Formació professional i aprenentatge permanent | 15.161.269 | 1,3 % |
| `421D` | Formació del professorat | 8.343.670 | 0,7 % |
| `421J` | Ensenyaments artístics superiors | 4.291.920 | 0,4 % |
| `421E` | Llengües estrangeres i projectes internacionals | 2.073.000 | 0,2 % |
| `421C` | Planificació educativa i règim de funcionament de centres escolars | 1.981.157 | 0,2 % |
| `571B` | Educació ambiental | 1.345.992 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 425.654 | 0,0 % |
| `421H` | Inspecció educativa | 126.959 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 57,46 M€ (57.464.096 €) · 6 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 46.805.016 | 81,5 % |
| `711A` | Direcció i serveis generals de la Conselleria d’Agricultura, Pesca i Alimentació | 5.887.274 | 10,2 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.457.998 | 4,3 % |
| `714C` | Polítiques alimentàries | 1.283.598 | 2,2 % |
| `531A` | Ordenació del territori i urbanisme | 970.210 | 1,7 % |
| `714D` | Promoció i regulació dels mercats agraris | 60.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,24 M€ (3.244.731 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 3.244.731 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 36,45 M€ (36.452.524 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 18.957.559 | 52,0 % |
| `431A` | Gestió i foment de l’habitatge social | 12.067.399 | 33,1 % |
| `511B` | Direcció i serveis generals de la Conselleria de Mobilitat i Habitatge | 5.427.566 | 14,9 % |

</details>

<details open><summary><b><code>empleo</code> — 137,93 M€ (137.930.119 €) · 5 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 121.966.990 | 88,4 % |
| `322B` | Gestió de les relacions laborals | 7.160.930 | 5,2 % |
| `322A` | Ocupació i inserció laboral específiques | 5.820.000 | 4,2 % |
| `322F` | Autocupació i economia social | 2.428.872 | 1,8 % |
| `322C` | Foment de la responsabilitat social corporativa | 553.327 | 0,4 % |

</details>

<details open><summary><b><code>idi</code> — 33,08 M€ (33.081.410 €) · 4 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `542A` | Innovació | 14.768.854 | 44,6 % |
| `541A` | Recerca i desenvolupament | 9.624.454 | 29,1 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 8.163.814 | 24,7 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 524.288 | 1,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 174,17 M€ (174.166.170 €) · 4 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 74.909.578 | 43,0 % |
| `314A` | Pensions i prestacions econòmiques | 50.000.000 | 28,7 % |
| `313L` | Equipaments de serveis socials | 29.521.168 | 17,0 % |
| `313I` | Planificació, ordenació i formació socials | 19.735.424 | 11,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 26,84 M€ (26.840.389 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 20.533.959 | 76,5 % |
| `313G` | Família i unitats de convivència | 6.025.237 | 22,4 % |
| `313F` | Protecció i defensa dels drets dels menors | 281.193 | 1,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 49,15 M€ (49.146.561 €) · 2 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 46.826.641 | 95,3 % |
| `413E` | Pla autonòmic de drogues | 2.319.920 | 4,7 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,28 M€ (5.282.172 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316A` | Drets i diversitat | 5.282.172 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 32,02 M€ (32.018.364 €) · 6 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121L` | Direcció i serveis generals de la Conselleria de Model Econòmic, Turisme i Treball | 9.445.353 | 29,5 % |
| `751C` | Ordenació del sector i redefinició del model turístic | 8.621.796 | 26,9 % |
| `761C` | Promoció empresarial i economia circular | 6.344.992 | 19,8 % |
| `761A` | Ordenació i promoció comercial | 4.846.344 | 15,1 % |
| `751B` | Promoció turística | 1.866.955 | 5,8 % |
| `761B` | Gestió en matèria de joc | 892.924 | 2,8 % |

</details>

<details open><summary><b><code>igualdad</code> — 17,73 M€ (17.730.872 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B` | Direcció i serveis generals de la Conselleria de Presidència, Funció Pública i Igualtat | 10.997.465 | 62,0 % |
| `323C` | Polítiques públiques d’igualtat | 6.733.407 | 38,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.719,43 M€ · 81 códigos · 42,7 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Amortització i despeses financeres de deute públic | 1.290.660.433 |
| `912A` | Suport financer als consells insulars | 443.311.971 |
| `592A` | Factor d’insularitat Reial Decret-llei 4/2019 | 109.661.220 |
| `811A` | Fons de contingència | 75.000.000 |
| `521C` | Transport ferroviari | 74.934.814 |
| `413G` | Accions públiques relatives a la COVID-19 | 71.656.220 |
| `562B` | Sanejament i depuració d’aigües | 70.750.841 |
| `126F` | Serveis comuns generals | 39.370.890 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 37.943.459 |
| `521A` | Infraestructures bàsiques | 33.565.915 |
| `551C` | Mitjans de comunicació social | 32.665.000 |
| `455A` | Promoció i serveis de cultura | 28.420.201 |
| `571D` | Conservació i millora del medi natural | 23.671.900 |
| `521D` | Transport per carretera | 22.549.589 |
| `461A` | Promoció i foment de l’esport | 22.169.341 |
| `562A` | Abastament d’aigua | 21.879.845 |
| `912B` | Suport financer a ajuntaments i altres ens locals | 20.427.387 |
| `141A` | Direcció i serveis generals de la Conselleria d’Hisenda i Relacions Exteriors | 19.068.857 |
| `571A` | Gestió de residus | 18.589.366 |
| `126L` | Serveis comuns tecnològics | 17.296.221 |
| `522A` | Ports i transport marítim | 15.981.039 |
| `571J` | Direcció i serveis general de la Conselleria de Medi Ambient i Territori | 15.541.057 |
| `111A` | Activitat legislativa | 15.480.572 |
| `313C` | Mesures judicials i prevenció del delicte | 15.431.597 |
| `571C` | Gestió d’espais naturals | 14.496.378 |
| … | *resto: 56 códigos* | 168.908.366 |

</details>

### 2023

*Fuente: `memoria_programas.html` · 150 líneas · total extraído **7.087,17 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.199,72 M€ (2.199.720.288 €) · 10 códigos · 31,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 2.151.618.286 | 97,8 % |
| `413B` | Prevenció de la malaltia i promoció i vigilància en salut pública | 17.510.173 | 0,8 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut i Consum | 10.118.370 | 0,5 % |
| `413C` | Protecció de la salut | 8.122.150 | 0,4 % |
| `324A` | Salut i prevenció de riscs laborals | 4.907.224 | 0,2 % |
| `411D` | Planificació, avaluació i cartera de serveis | 1.891.691 | 0,1 % |
| `413A` | Acreditació, docència i recerca en salut | 1.795.230 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.490.141 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.304.110 | 0,1 % |
| `413F` | Planificació, control i gestió del medicament i dels serveis farmacèutics | 962.913 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.245,71 M€ (1.245.709.578 €) · 15 códigos · 17,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 689.225.003 | 55,3 % |
| `422B` | Educació concertada | 198.531.974 | 15,9 % |
| `421F` | Política i actuacions en matèria universitària | 104.469.114 | 8,4 % |
| `421K` | Innovació i comunitat educativa | 81.138.964 | 6,5 % |
| `423B` | Altres serveis a l’ensenyament | 62.086.172 | 5,0 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 41.369.967 | 3,3 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació i Formació Professional | 35.956.858 | 2,9 % |
| `421G` | Formació professional i aprenentatge permanent | 20.397.895 | 1,6 % |
| `421J` | Ensenyaments artístics superiors | 4.253.012 | 0,3 % |
| `421E` | Llengües estrangeres i projectes internacionals | 2.407.821 | 0,2 % |
| `421C` | Planificació educativa i règim de funcionament de centres escolars | 2.039.004 | 0,2 % |
| `421D` | Formació del professorat | 1.963.781 | 0,2 % |
| `571B` | Educació ambiental | 1.404.983 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 331.956 | 0,0 % |
| `421H` | Inspecció educativa | 133.074 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 69,18 M€ (69.184.838 €) · 7 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 48.636.675 | 70,3 % |
| `714A` | Impuls del Turisme Sostenible - projectes dagricultura | 8.600.000 | 12,4 % |
| `711A` | Direcció i serveis generals de la Conselleria d’Agricultura, Pesca i Alimentació | 6.634.932 | 9,6 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.913.351 | 4,2 % |
| `714C` | Polítiques alimentàries | 1.414.028 | 2,0 % |
| `531A` | Ordenació del territori i urbanisme | 905.852 | 1,3 % |
| `714D` | Promoció i regulació dels mercats agraris | 80.000 | 0,1 % |

</details>

<details open><summary><b><code>direccion</code> — 3,38 M€ (3.379.312 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 3.379.312 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 104,62 M€ (104.618.883 €) · 4 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 53.106.103 | 50,8 % |
| `431C` | Impuls del Turisme Sostenible - projectes dhabitatge | 27.366.701 | 26,2 % |
| `431A` | Gestió i foment de l’habitatge social | 18.463.559 | 17,6 % |
| `511B` | Direcció i serveis generals de la Conselleria de Mobilitat i Habitatge | 5.682.520 | 5,4 % |

</details>

<details open><summary><b><code>empleo</code> — 145,22 M€ (145.218.055 €) · 6 códigos · 2,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 129.204.839 | 89,0 % |
| `322A` | Ocupació i inserció laboral específiques | 5.500.000 | 3,8 % |
| `322B` | Gestió de les relacions laborals | 4.991.492 | 3,4 % |
| `322F` | Autocupació i economia social | 3.873.745 | 2,7 % |
| `322E` | Impuls del Turisme Sostenible - projectes d’ocupació | 1.000.000 | 0,7 % |
| `322C` | Foment de la responsabilitat social corporativa | 647.979 | 0,4 % |

</details>

<details open><summary><b><code>idi</code> — 54,90 M€ (54.898.603 €) · 5 códigos · 0,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `541B` | Impuls del Turisme Sostenible - projectes de recerca | 20.975.162 | 38,2 % |
| `542A` | Innovació | 12.196.450 | 22,2 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 10.576.811 | 19,3 % |
| `541A` | Recerca i desenvolupament | 10.531.223 | 19,2 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 618.957 | 1,1 % |

</details>

<details open><summary><b><code>dependencia</code> — 202,41 M€ (202.413.664 €) · 4 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 87.483.669 | 43,2 % |
| `314A` | Pensions i prestacions econòmiques | 53.000.000 | 26,2 % |
| `313L` | Equipaments de serveis socials | 41.138.513 | 20,3 % |
| `313I` | Planificació, ordenació i formació socials | 20.791.482 | 10,3 % |

</details>

<details open><summary><b><code>discapacidad</code> — 29,26 M€ (29.258.962 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 22.084.967 | 75,5 % |
| `313G` | Família i unitats de convivència | 6.859.308 | 23,4 % |
| `313F` | Protecció i defensa dels drets dels menors | 314.687 | 1,1 % |

</details>

<details open><summary><b><code>salud_mental</code> — 115,54 M€ (115.537.986 €) · 2 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 112.880.914 | 97,7 % |
| `413E` | Pla autonòmic d’addiccions | 2.657.072 | 2,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 5,35 M€ (5.345.802 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316A` | Drets i diversitat | 5.345.802 | 100,0 % |

</details>

<details open><summary><b><code>turismo</code> — 188,44 M€ (188.442.426 €) · 10 códigos · 2,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenació del sector i redefinició del model turístic | 94.828.881 | 50,3 % |
| `521E` | Impuls del Turisme Sostenible - projectes de transport terrestre | 28.500.000 | 15,1 % |
| `571H` | Impuls del Turisme Sostenible - projectes mediambientals | 25.156.841 | 13,3 % |
| `751D` | Impuls del Turisme Sostenible - projectes turístics | 12.776.282 | 6,8 % |
| `761A` | Ordenació i promoció comercial | 8.611.482 | 4,6 % |
| `121L` | Direcció i serveis generals de la Conselleria de Model Econòmic, Turisme i Treball | 8.087.212 | 4,3 % |
| `731B` | Impuls del Turisme Sostenible - projectes denergia | 5.346.559 | 2,8 % |
| `761C` | Promoció empresarial i economia circular | 2.330.121 | 1,2 % |
| `751B` | Promoció turística | 1.896.651 | 1,0 % |
| `761B` | Gestió en matèria de joc | 908.397 | 0,5 % |

</details>

<details open><summary><b><code>igualdad</code> — 20,74 M€ (20.735.232 €) · 2 códigos · 0,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121B` | Direcció i serveis generals de la Conselleria de Presidència, Funció Pública i Igualtat | 11.622.186 | 56,1 % |
| `323C` | Polítiques públiques d’igualtat | 9.113.046 | 43,9 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.702,70 M€ · 80 códigos · 38,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Amortització i despeses financeres de deute públic | 1.264.860.025 |
| `912A` | Suport financer als consells insulars | 567.422.704 |
| `562B` | Sanejament i depuració d’aigües | 81.370.755 |
| `521C` | Transport ferroviari | 75.797.402 |
| `811A` | Fons de contingència | 60.000.000 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 57.389.266 |
| `551C` | Mitjans de comunicació social | 36.963.956 |
| `521D` | Transport per carretera | 36.328.340 |
| `521A` | Infraestructures bàsiques | 33.757.106 |
| `455A` | Promoció i serveis de cultura | 28.940.294 |
| `562A` | Abastament d’aigua | 28.749.545 |
| `141A` | Direcció i serveis generals de la Conselleria d’Hisenda i Relacions Exteriors | 27.606.323 |
| `461A` | Promoció i foment de l’esport | 25.698.272 |
| `571D` | Conservació i millora del medi natural | 25.011.836 |
| `912B` | Suport financer a ajuntaments i altres ens locals | 20.487.438 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 18.212.925 |
| `126L` | Serveis comuns tecnològics | 17.618.389 |
| `111A` | Activitat legislativa | 17.429.898 |
| `522A` | Ports i transport marítim | 17.082.225 |
| `126F` | Serveis comuns generals | 16.943.639 |
| `313C` | Mesures judicials i prevenció del delicte | 16.575.735 |
| `571J` | Direcció i serveis general de la Conselleria de Medi Ambient i Territori | 16.352.981 |
| `223A` | Emergències | 15.626.961 |
| `313K` | Direcció i serveis generals de la Conselleria d’Afers Socials i Esports | 14.247.462 |
| `571A` | Gestió de residus | 12.738.287 |
| … | *resto: 55 códigos* | 169.489.977 |

</details>

### 2024

*Fuente: `memoria_programas.html` · 145 líneas · total extraído **7.114,25 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.273,12 M€ (2.273.123.710 €) · 10 códigos · 32,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 2.238.986.269 | 98,5 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut | 16.246.266 | 0,7 % |
| `413C` | Protecció de la salut | 7.164.464 | 0,3 % |
| `413B` | Prevenció de la malaltia i promoció i vigilància en salut pública | 2.535.243 | 0,1 % |
| `413A` | Acreditació, docència i recerca en salut | 1.836.553 | 0,1 % |
| `413H` | Promoció i prevenció de la salut mental | 1.400.624 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.364.411 | 0,1 % |
| `411D` | Planificació, avaluació i cartera de serveis | 1.308.467 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.294.757 | 0,1 % |
| `413F` | Planificació, control i gestió del medicament i dels serveis farmacèutics | 986.656 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.343,39 M€ (1.343.385.180 €) · 16 códigos · 18,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 716.303.942 | 53,3 % |
| `422B` | Educació concertada | 202.023.765 | 15,0 % |
| `421F` | Política i actuacions en matèria universitària | 113.816.461 | 8,5 % |
| `423B` | Altres serveis a l’ensenyament | 83.702.012 | 6,2 % |
| `421K` | Innovació i comunitat educativa | 82.936.974 | 6,2 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació i Universitats | 43.989.943 | 3,3 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 42.596.268 | 3,2 % |
| `421L` | Serveis complementaris a l’ensenyament | 28.594.087 | 2,1 % |
| `421G` | Formació professional i aprenentatge permanent | 15.760.014 | 1,2 % |
| `421J` | Ensenyaments artístics superiors | 5.158.144 | 0,4 % |
| `421E` | Llengües estrangeres i projectes internacionals | 2.614.968 | 0,2 % |
| `421C` | Planificació educativa i règim de funcionament de centres escolars | 2.370.607 | 0,2 % |
| `421D` | Formació del professorat | 1.961.697 | 0,1 % |
| `571B` | Educació ambiental | 854.594 | 0,1 % |
| `421B` | Ordenació general del sistema educatiu | 371.243 | 0,0 % |
| `421H` | Inspecció educativa | 330.461 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 93,80 M€ (93.802.215 €) · 8 códigos · 1,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 45.544.183 | 48,6 % |
| `714A` | Impuls del Turisme Sostenible - projectes dagricultura | 25.000.000 | 26,7 % |
| `711A` | Direcció i serveis generals de la Conselleria d’Agricultura, Pesca i Medi Natural | 15.779.528 | 16,8 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.775.267 | 3,0 % |
| `531B` | Ordenació de la costa i del litoral | 1.965.889 | 2,1 % |
| `714C` | Polítiques alimentàries | 1.423.347 | 1,5 % |
| `531A` | Ordenació del territori i urbanisme | 1.027.902 | 1,1 % |
| `531C` | Desenvolupament, Simplificació i Agilitació Urbanística | 286.099 | 0,3 % |

</details>

<details open><summary><b><code>direccion</code> — 3,30 M€ (3.299.594 €) · 1 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 3.299.594 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 71,88 M€ (71.881.943 €) · 3 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 42.135.063 | 58,6 % |
| `431A` | Gestió i foment de l’habitatge social | 17.461.460 | 24,3 % |
| `511B` | Direcció i serveis generals de la Conselleria d’Habitatge, Territori i Mobilitat | 12.285.420 | 17,1 % |

</details>

<details open><summary><b><code>empleo</code> — 29,60 M€ (29.600.694 €) · 4 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322A` | Ocupació i inserció laboral específiques | 11.000.000 | 37,2 % |
| `721A` | Direcció i serveis generals de la Conselleria d’Empresa, Ocupació i Energia | 9.600.229 | 32,4 % |
| `322B` | Gestió de les relacions laborals | 5.008.253 | 16,9 % |
| `322F` | Autocupació i economia social | 3.992.212 | 13,5 % |

</details>

<details open><summary><b><code>idi</code> — 88,26 M€ (88.256.187 €) · 7 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `141A` | Direcció i serveis generals de la Conselleria d’Economia, Hisenda i Innovació | 31.450.911 | 35,6 % |
| `541A` | Recerca i desenvolupament | 22.533.214 | 25,5 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 10.058.127 | 11,4 % |
| `542A` | Innovació | 9.351.863 | 10,6 % |
| `561C` | Direcció i serveis generals Conselleria de la Mar i del Cicle de l’Aigua | 7.330.970 | 8,3 % |
| `541B` | Impuls del Turisme Sostenible - projectes de recerca | 7.000.000 | 7,9 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 531.102 | 0,6 % |

</details>

<details open><summary><b><code>dependencia</code> — 200,33 M€ (200.326.339 €) · 4 códigos · 2,8 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 96.614.696 | 48,2 % |
| `314A` | Pensions i prestacions econòmiques | 56.562.263 | 28,2 % |
| `313L` | Equipaments de serveis socials | 30.272.479 | 15,1 % |
| `313I` | Planificació, ordenació i formació socials | 16.876.901 | 8,4 % |

</details>

<details open><summary><b><code>discapacidad</code> — 32,04 M€ (32.042.963 €) · 3 códigos · 0,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 22.735.485 | 71,0 % |
| `313G` | Família i unitats de convivència | 9.056.358 | 28,3 % |
| `313F` | Protecció i defensa dels drets dels menors | 251.120 | 0,8 % |

</details>

<details open><summary><b><code>salud_mental</code> — 66,91 M€ (66.909.910 €) · 2 códigos · 0,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 64.153.030 | 95,9 % |
| `413E` | Pla autonòmic d’addiccions | 2.756.880 | 4,1 % |

</details>

<details open><summary><b><code>diversidad</code> — 3,60 M€ (3.597.243 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Atenció i integració social de la població immigrant | 3.332.996 | 92,7 % |
| `316A` | Drets i diversitat | 264.247 | 7,3 % |

</details>

<details open><summary><b><code>turismo</code> — 253,41 M€ (253.406.214 €) · 9 códigos · 3,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751C` | Ordenació del sector i redefinició del model turístic | 130.561.084 | 51,5 % |
| `751D` | Impuls del Turisme Sostenible - projectes turístics | 50.000.000 | 19,7 % |
| `571H` | Impuls del Turisme Sostenible - projectes mediambientals | 44.072.980 | 17,4 % |
| `521E` | Impuls del Turisme Sostenible - projectes de transport terrestre | 10.000.000 | 3,9 % |
| `751A` | Direccció i serveis generals de la Conselleria de Turisme, Cultura i Esports | 6.418.514 | 2,5 % |
| `761A` | Ordenació i promoció comercial | 6.395.238 | 2,5 % |
| `761C` | Promoció empresarial i economia circular | 3.161.488 | 1,2 % |
| `751B` | Promoció turística | 2.037.301 | 0,8 % |
| `761B` | Gestió en matèria de joc | 759.609 | 0,3 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,44 M€ (9.444.077 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Polítiques públiques d’igualtat | 9.444.077 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 2.645,17 M€ · 75 códigos · 37,2 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `011A` | Amortització i despeses financeres de deute públic | 1.075.320.496 |
| `912A` | Suport financer als consells insulars | 594.771.260 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 117.513.611 |
| `521C` | Transport ferroviari | 113.005.433 |
| `562B` | Sanejament i depuració d’aigües | 85.963.074 |
| `121H` | Gestió de recursos humans | 67.620.461 |
| `811A` | Fons de contingència | 45.000.000 |
| `551C` | Mitjans de comunicació social | 42.218.458 |
| `562A` | Abastament d’aigua | 41.718.346 |
| `521A` | Infraestructures bàsiques | 34.558.726 |
| `455A` | Promoció i serveis de cultura | 31.712.003 |
| `521D` | Transport per carretera | 31.307.627 |
| `571D` | Conservació i millora del medi natural | 25.931.670 |
| `461A` | Promoció i foment de l’esport | 25.088.295 |
| `126L` | Serveis comuns tecnològics | 22.829.505 |
| `912B` | Suport financer a ajuntaments i altres ens locals | 19.862.951 |
| `571A` | Gestió de residus | 18.798.461 |
| `522A` | Ports i transport marítim | 17.686.801 |
| `111A` | Activitat legislativa | 17.419.050 |
| `313C` | Mesures judicials i prevenció del delicte | 17.168.176 |
| `223A` | Emergències | 15.064.711 |
| `126F` | Serveis comuns generals | 14.967.748 |
| `313K` | Direcció i serveis generals de la Conselleria de Famílies i Afers Socials | 14.696.965 |
| `571C` | Gestió d’espais naturals | 12.391.483 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 11.512.847 |
| … | *resto: 50 códigos* | 131.043.448 |

</details>

### 2025

*Fuente: `memoria_programas.html` · 141 líneas · total extraído **6.350,11 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.393,41 M€ (2.393.412.726 €) · 10 códigos · 37,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Finançament sanitari | 2.344.803.575 | 98,0 % |
| `413B` | Prevenció de la malaltia i promoció i vigilància en salut pública | 17.957.937 | 0,8 % |
| `411A` | Direcció i serveis generals de la Conselleria de Salut | 11.562.338 | 0,5 % |
| `413C` | Protecció de la salut | 8.462.481 | 0,4 % |
| `411D` | Planificació, avaluació i cartera de serveis | 3.008.147 | 0,1 % |
| `413A` | Acreditació, docència i recerca en salut | 1.853.394 | 0,1 % |
| `413H` | Promoció i prevenció de la salut mental | 1.780.277 | 0,1 % |
| `413D` | Coordinació de centres insulars | 1.443.172 | 0,1 % |
| `121I` | Salut i prevenció de riscs laborals a l’Administració | 1.403.095 | 0,1 % |
| `413F` | Planificació, control i gestió del medicament i dels serveis farmacèutics | 1.138.310 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.421,04 M€ (1.421.043.777 €) · 16 códigos · 22,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educació pública | 777.242.287 | 54,7 % |
| `422B` | Educació concertada | 229.041.612 | 16,1 % |
| `421F` | Política i actuacions en matèria universitària | 125.877.361 | 8,9 % |
| `423B` | Altres serveis a l’ensenyament | 75.133.730 | 5,3 % |
| `421A` | Direcció i serveis generals de la Conselleria d’Educació i Universitats | 56.451.424 | 4,0 % |
| `421K` | Innovació i comunitat educativa | 47.107.719 | 3,3 % |
| `421I` | Administració i serveis de suport a l’ensenyament | 45.598.094 | 3,2 % |
| `421L` | Serveis complementaris a l’ensenyament | 31.514.029 | 2,2 % |
| `421C` | Planificació educativa i règim de funcionament de centres escolars | 13.878.195 | 1,0 % |
| `421G` | Formació professional i aprenentatge permanent | 9.072.884 | 0,6 % |
| `421J` | Ensenyaments artístics superiors | 5.070.500 | 0,4 % |
| `421E` | Llengües estrangeres i projectes internacionals | 2.346.024 | 0,2 % |
| `421D` | Formació del professorat | 1.666.205 | 0,1 % |
| `571B` | Educació ambiental | 617.500 | 0,0 % |
| `421B` | Ordenació general del sistema educatiu | 285.933 | 0,0 % |
| `421H` | Inspecció educativa | 140.280 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 76,47 M€ (76.467.547 €) · 7 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Foment del sector agropecuari | 52.063.174 | 68,1 % |
| `711A` | Direcció i serveis generals de la Conselleria d’Agricultura, Pesca i Medi Natural | 15.265.634 | 20,0 % |
| `718A` | Recursos marins i ordenació del sector pesquer | 2.897.434 | 3,8 % |
| `531B` | Ordenació de la costa i del litoral | 2.306.480 | 3,0 % |
| `531A` | Ordenació del territori i urbanisme | 2.026.862 | 2,7 % |
| `714C` | Polítiques alimentàries | 1.582.189 | 2,1 % |
| `531C` | Desenvolupament, simplificació i agilitació urbanística | 325.774 | 0,4 % |

</details>

<details open><summary><b><code>direccion</code> — 4,28 M€ (4.277.714 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Direcció i serveis generals de la Presidència del Govern | 4.277.714 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 98,03 M€ (98.034.268 €) · 3 códigos · 1,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431B` | Arquitectura, habitatge i protecció del patrimoni | 59.944.543 | 61,1 % |
| `431A` | Gestió i foment de l’habitatge social | 30.593.827 | 31,2 % |
| `511B` | Direcció i serveis generals de la Conselleria d’Habitatge, Territori i Mobilitat | 7.495.898 | 7,6 % |

</details>

<details open><summary><b><code>empleo</code> — 154,89 M€ (154.891.570 €) · 5 códigos · 2,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Foment i gestió de l’ocupació de les Illes Balears | 119.218.484 | 77,0 % |
| `721A` | Direcció i serveis generals de la Conselleria d’Empresa, Ocupació i Energia | 15.258.242 | 9,9 % |
| `322A` | Ocupació i inserció laboral específiques | 12.355.000 | 8,0 % |
| `322B` | Gestió de les relacions laborals | 5.178.844 | 3,3 % |
| `322F` | Autoocupació i economia social | 2.881.000 | 1,9 % |

</details>

<details open><summary><b><code>idi</code> — 98,92 M€ (98.924.931 €) · 6 códigos · 1,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `141A` | Direcció i serveis generals de la Conselleria d’Economia, Hisenda i Innovació | 29.876.376 | 30,2 % |
| `561A` | Domini públic hidràulic: Protecció i control. Directiva marc de l’aigua | 23.367.624 | 23,6 % |
| `541A` | Recerca i desenvolupament | 20.094.006 | 20,3 % |
| `542A` | Innovació | 17.319.344 | 17,5 % |
| `561C` | Direcció i serveis generals Conselleria de la Mar i del Cicle de l’Aigua | 7.918.293 | 8,0 % |
| `126H` | Assessorament, estudi, recerca i difusió normativa | 349.288 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 225,19 M€ (225.188.836 €) · 4 códigos · 3,5 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atenció a la dependència | 107.916.472 | 47,9 % |
| `314A` | Pensions i prestacions econòmiques | 68.271.318 | 30,3 % |
| `313L` | Equipaments de serveis socials | 31.602.421 | 14,0 % |
| `313I` | Planificació, ordenació i formació socials | 17.398.625 | 7,7 % |

</details>

<details open><summary><b><code>discapacidad</code> — 36,75 M€ (36.746.386 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atenció a la discapacitat | 23.806.864 | 64,8 % |
| `313G` | Família i unitats de convivència | 12.590.397 | 34,3 % |
| `313F` | Protecció i defensa dels drets dels menors | 349.125 | 1,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 64,99 M€ (64.992.256 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Serveis socials | 62.803.589 | 96,6 % |
| `413E` | Pla autonòmic d’addiccions | 2.188.667 | 3,4 % |

</details>

<details open><summary><b><code>diversidad</code> — 6,84 M€ (6.837.711 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `316A` | Drets i diversitat | 4.763.810 | 69,7 % |
| `313J` | Atenció i integració social de la població immigrant | 2.073.901 | 30,3 % |

</details>

<details open><summary><b><code>turismo</code> — 208,23 M€ (208.232.117 €) · 8 códigos · 3,3 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751D` | Impuls del Turisme Sostenible - projectes turístics | 150.686.495 | 72,4 % |
| `751C` | Ordenació del sector i redefinició del model turístic | 28.186.902 | 13,5 % |
| `761A` | Ordenació i promoció comercial | 11.011.574 | 5,3 % |
| `751A` | Direccció i serveis generals de la Conselleria de Turisme, Cultura i Esports | 7.302.042 | 3,5 % |
| `761C` | Promoció empresarial i economia circular | 4.255.080 | 2,0 % |
| `571H` | Impuls del Turisme Sostenible - projectes mediambientals | 4.000.000 | 1,9 % |
| `751B` | Promoció turística | 2.038.301 | 1,0 % |
| `761B` | Gestió en matèria de joc | 751.723 | 0,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 9,48 M€ (9.483.352 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Polítiques públiques d’igualtat | 9.483.352 | 100,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.551,58 M€ · 73 códigos · 24,4 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `912A` | Suport financer als consells insulars | 556.336.078 |
| `731A` | Foment de l’ús d’energies renovables i de l’estalvi energètic | 155.490.436 |
| `562B` | Sanejament i depuració d’aigües | 106.549.043 |
| `521C` | Transport ferroviari | 78.384.750 |
| `521A` | Infraestructures bàsiques | 75.567.909 |
| `551C` | Mitjans de comunicació social | 42.086.239 |
| `121H` | Gestió de recursos humans | 40.340.365 |
| `811A` | Fons de contingència | 39.335.000 |
| `455A` | Promoció i serveis de cultura | 31.262.264 |
| `461A` | Promoció i foment de l’esport | 27.692.965 |
| `571D` | Conservació i millora del medi natural | 25.299.569 |
| `126L` | Serveis comuns tecnològics | 24.690.448 |
| `562A` | Abastament d’aigua | 22.378.553 |
| `521D` | Transport per carretera | 21.832.231 |
| `522A` | Ports i transport marítim | 20.981.308 |
| `313C` | Mesures judicials i prevenció del delicte | 18.674.476 |
| `912B` | Suport financer a ajuntaments i altres ens locals | 18.181.256 |
| `111A` | Activitat legislativa | 17.883.112 |
| `313K` | Direcció i serveis generals de la Conselleria de Famílies i Afers Socials | 17.311.107 |
| `723A` | Promoció industrial | 16.619.230 |
| `571A` | Gestió de residus | 15.400.661 |
| `571C` | Gestió d’espais naturals | 15.267.851 |
| `223A` | Emergències | 15.171.131 |
| `141E` | Gestió de tresoreria i política financera | 12.496.840 |
| `551A` | Ordenació, regulació i desenvolupament de les telecomunicacions | 12.462.603 |
| … | *resto: 48 códigos* | 123.880.306 |

</details>

### 2026

*Fuente: `estats_numerics.pdf` · 148 líneas · total extraído **6.442,00 M€** (nominales)*

<details open><summary><b><code>sanidad</code> — 2.425,55 M€ (2.425.549.966 €) · 12 códigos · 37,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `411E` | Financiación sanitaria | 2.363.306.674 | 97,4 % |
| `413B` | Prevención de la enfermedad y promoción y vigilancia en salud pública | 17.251.844 | 0,7 % |
| `411A` | Dirección y servicios generales de la Consejería de Salud | 12.196.439 | 0,5 % |
| `413C` | Protección de la salud | 8.349.398 | 0,3 % |
| `411D` | Planificación, evaluación y cartera de servicios | 7.664.760 | 0,3 % |
| `324A` | Salud y prevención de riesgos laborales | 4.976.269 | 0,2 % |
| `571G` | Sanidad forestal | 3.419.937 | 0,1 % |
| `413H` | Promoción y prevención de la salud mental | 2.453.902 | 0,1 % |
| `413A` | Acreditación, docencia e investigación en salud | 1.889.267 | 0,1 % |
| `413D` | Coordinación de centros insulares | 1.543.338 | 0,1 % |
| `121I` | Salud y prevención de riesgos laborales en la Administración | 1.425.625 | 0,1 % |
| `413F` | Planificación, control y gestión del medicamento y de los servicios farmacéuticos | 1.072.513 | 0,0 % |

</details>

<details open><summary><b><code>educacion</code> — 1.400,84 M€ (1.400.836.886 €) · 16 códigos · 21,7 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `422A` | Educación pública | 798.133.802 | 57,0 % |
| `422B` | Educación concertada | 224.040.872 | 16,0 % |
| `421F` | Política y actuaciones en materia universitaria | 122.068.708 | 8,7 % |
| `423B` | Otros servicios a la enseñanza | 87.305.821 | 6,2 % |
| `421I` | Administración y servicios de apoyo a la enseñanza | 48.816.315 | 3,5 % |
| `421K` | Innovación y comunidad educativa | 35.154.185 | 2,5 % |
| `421L` | Servicios complementarios a la enseñanza | 34.591.532 | 2,5 % |
| `421A` | Dirección y servicios generales de la Consejería de Educación y Universidades | 23.578.892 | 1,7 % |
| `421C` | Planificación educativa y régimen de funcionamiento de centros escolares | 13.802.111 | 1,0 % |
| `421J` | Enseñanzas artísticas superiores | 5.070.500 | 0,4 % |
| `421G` | Formación profesional y aprendizaje permanente | 3.671.813 | 0,3 % |
| `421E` | Lenguas extranjeras y proyectos internacionales | 2.329.216 | 0,2 % |
| `421D` | Formación del profesorado | 1.204.962 | 0,1 % |
| `571B` | Educación ambiental | 617.500 | 0,0 % |
| `421B` | Ordenación general del sistema educativo | 300.306 | 0,0 % |
| `421H` | Inspección educativa | 150.351 | 0,0 % |

</details>

<details open><summary><b><code>soberania</code> — 70,77 M€ (70.774.415 €) · 7 códigos · 1,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `714B` | Fomento del sector agrario | 46.447.354 | 65,6 % |
| `711A` | Dirección y servicios generales de la Consejería de Agricultura, Pesca y Medio Natural | 14.809.608 | 20,9 % |
| `718A` | Recursos marinos y ordenación del sector pesquero | 2.951.333 | 4,2 % |
| `531B` | Ordenación de la costa y del litoral | 2.663.938 | 3,8 % |
| `531A` | Ordenación del territorio y urbanismo | 2.061.153 | 2,9 % |
| `714C` | Políticas alimentarias | 1.506.982 | 2,1 % |
| `531C` | Desarrollo, simplificacion y agilización urbanística | 334.047 | 0,5 % |

</details>

<details open><summary><b><code>direccion</code> — 3,95 M€ (3.949.752 €) · 1 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `121A` | Servicios generales de la Presidencia del Gobierno | 3.949.752 | 100,0 % |

</details>

<details open><summary><b><code>vivienda</code> — 28,70 M€ (28.701.877 €) · 3 códigos · 0,4 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `431A` | Gestión y fomento de la vivienda social | 14.759.340 | 51,4 % |
| `431B` | Arquitectura, vivienda y protección del patrimonio | 8.311.408 | 29,0 % |
| `511B` | Dirección y servicios generales de la Consejería de Vivienda, Territorio y Movilidad | 5.631.129 | 19,6 % |

</details>

<details open><summary><b><code>empleo</code> — 138,73 M€ (138.730.464 €) · 4 códigos · 2,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `322D` | Fomento y gestión del empleo a las Illes Balears | 115.905.503 | 83,5 % |
| `322A` | Empleo e inserción laboral específicos | 13.746.077 | 9,9 % |
| `322B` | Gestión de las relaciones laborales | 5.197.884 | 3,7 % |
| `322F` | Autoempleo y economía social | 3.881.000 | 2,8 % |

</details>

<details open><summary><b><code>idi</code> — 78,96 M€ (78.961.365 €) · 6 códigos · 1,2 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `141A` | Dirección y servicios generales de la Consejería de Economía, Hacienda e Innovación | 26.474.825 | 33,5 % |
| `541A` | Investigación y desarrollo | 19.315.186 | 24,5 % |
| `542A` | Innovación | 14.465.904 | 18,3 % |
| `561A` | Dominio público hidráulico: protección y control. Directiva marco del agua | 10.858.414 | 13,8 % |
| `561C` | Dirección y servicios generales de la C. del Mar y del Ciclo del Agua | 7.527.729 | 9,5 % |
| `126H` | Asesoramiento, estudio, investigación y difusión normativa | 319.307 | 0,4 % |

</details>

<details open><summary><b><code>dependencia</code> — 249,51 M€ (249.514.601 €) · 5 códigos · 3,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313D` | Atención a la dependencia | 106.820.051 | 42,8 % |
| `314A` | Pensiones y prestaciones económicas | 84.937.010 | 34,0 % |
| `313L` | Equipamientos de servicios sociales | 23.061.811 | 9,2 % |
| `313K` | Dirección y servicios generales de la Consejería de Familias, Bienestar Social y Atención a la Dependencia | 17.656.693 | 7,1 % |
| `313I` | Planificación, ordenación y formación sociales | 17.039.036 | 6,8 % |

</details>

<details open><summary><b><code>discapacidad</code> — 37,17 M€ (37.165.911 €) · 3 códigos · 0,6 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313B` | Atención a la discapacidad | 23.806.864 | 64,1 % |
| `313G` | Familia y unidades de convivencia | 13.005.114 | 35,0 % |
| `313F` | Protección y defensa de los derechos de los menores | 353.933 | 1,0 % |

</details>

<details open><summary><b><code>salud_mental</code> — 63,31 M€ (63.313.138 €) · 2 códigos · 1,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313E` | Servicios sociales | 61.213.997 | 96,7 % |
| `413E` | Plan autonómico de adicciones | 2.099.141 | 3,3 % |

</details>

<details open><summary><b><code>diversidad</code> — 1,35 M€ (1.353.429 €) · 2 códigos · 0,0 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `313J` | Atención e integración social de la población inmigrante | 1.086.895 | 80,3 % |
| `316A` | Derechos y diversidad | 266.534 | 19,7 % |

</details>

<details open><summary><b><code>turismo</code> — 185,63 M€ (185.626.005 €) · 8 códigos · 2,9 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `751D` | Impulso del turismo sostenible - proyectos turísticos | 150.686.495 | 81,2 % |
| `751C` | Ordenación del sector y redefinición del modelo turístico | 13.229.573 | 7,1 % |
| `751A` | Dirección y servicios generales C. Turismo, Cultura y Deportes | 7.200.470 | 3,9 % |
| `761A` | Ordenación y promoción comercial | 6.109.646 | 3,3 % |
| `571H` | Impulso del turismo sostenible - proyectos medioambientales | 4.000.000 | 2,2 % |
| `751B` | Promoción turística | 2.038.301 | 1,1 % |
| `761C` | Promoción empresarial y economía circular | 1.591.043 | 0,9 % |
| `761B` | Gestión en materia de juego | 770.477 | 0,4 % |

</details>

<details open><summary><b><code>igualdad</code> — 8,59 M€ (8.588.030 €) · 2 códigos · 0,1 % del año</b></summary>

| Código | Denominación | Importe (€) | % concepto |
|---|---|---:|---:|
| `323C` | Políticas públicas de igualdad | 8.503.541 | 99,0 % |
| `324B` | Conciliación e igualdad en el ámbito laboral | 84.489 | 1,0 % |

</details>

<details><summary><code>(sin concepto)</code> — 1.748,94 M€ · 77 códigos · 27,1 % del año (se listan los 25 mayores)</summary>

| Código | Denominación | Importe (€) |
|---|---|---:|
| `912A` | Apoyo financiero a los consejos insulares | 556.336.078 |
| `811A` | Fondo de contingencia | 448.720.301 |
| `562B` | Saneamiento y depuración de aguas | 104.512.991 |
| `521C` | Transporte ferroviario | 70.464.922 |
| `521A` | Infraestructuras básicas | 46.572.232 |
| `551C` | Medios de comunicación social | 41.586.239 |
| `121H` | Gestión de recursos humanos | 38.972.875 |
| `455A` | Promoción y servicios de cultura | 28.440.267 |
| `571D` | Conservación y mejora del medio natural | 24.369.061 |
| `521D` | Transporte por carretera | 24.115.976 |
| `461A` | Promoción y fomento del deporte | 20.733.558 |
| `126F` | Servicios comunes generales | 19.746.432 |
| `126L` | Servicios comunes tecnológicos | 19.166.025 |
| `313C` | Medidas judiciales y prevención del delito | 18.680.492 |
| `912B` | Apoyo financiero a ayuntamientos y otros entes locales | 18.188.318 |
| `522A` | Puertos y transporte marítimo | 17.910.356 |
| `111A` | Actividad legislativa | 17.883.113 |
| `551A` | Ordenación, regulación y desarrollo de las telecomunicaciones | 16.015.988 |
| `223A` | Emergencias | 15.212.484 |
| `126N` | Dirección y servicios generals de la Agencia Balear de Digitalización, Ciberseguridad y Telecomunicaciones | 13.837.167 |
| `721A` | Dirección y servicios generales de la Consejería de Empresa, Autónomos y Energía | 13.456.354 |
| `121B` | Dirección y servicios generales de la Consejería de Presidencia, Coord.Acción Gobierno y Coop.Local | 12.404.272 |
| `571K` | Fondo de prevención y gestión de residuos | 11.291.790 |
| `723A` | Promoción industrial | 10.419.230 |
| `731A` | Fomento de la utilización de energías renovables y del ahorro energético | 9.816.994 |
| … | *resto: 52 códigos* | 130.084.879 |

</details>

## 6 · Cómo reproducir / verificar

```bash
python3 tools/build_trazabilidad_md.py bal     # regenera este documento
python3 tools/auditoria_magnitud.py bal        # test de continuidad y per cápita
cd 1_extraccion && python3 -m ccaa --ccaa bal --anio <año> \
    --input ../fuentes/raw/bal/<año>/<fichero> --output /tmp/bal.csv
```

Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · Motor: [`extract.py`](extract.py) · Limitaciones conocidas: [`limitaciones-bal.md`](limitaciones-bal.md)

