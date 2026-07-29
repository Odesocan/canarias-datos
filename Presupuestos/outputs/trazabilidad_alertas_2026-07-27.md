# Índice de alertas de trazabilidad — 17 CCAA · rev. 2026-07-27

> Resumen transversal generado por `tools/build_trazabilidad_md.py`. El detalle
> código-a-concepto está en `1_extraccion/ccaa/<id3>/trazabilidad-<id3>.md`.
> Importes en € NOMINALES (la BD y el D3 usan € constantes deflactados).

## 1 · Semáforo por CCAA

| CCAA | Años | Conceptos | Alertas | Cód. inestables | Cód. duplicados | M€ duplicados | Conceptos ausentes |
|---|---|---:|---:|---:|---:|---:|---|
| [`bal`](../1_extraccion/ccaa/bal/trazabilidad-bal.md) Islas Baleares | 2015-2026 | 13 | 22 | 12 | 0 | — | — |
| [`lar`](../1_extraccion/ccaa/lar/trazabilidad-lar.md) La Rioja | 2015-2026 | 13 | 14 | 26 | 0 | — | — |
| [`val`](../1_extraccion/ccaa/val/trazabilidad-val.md) Comunidad Valenciana | 2015-2026 | 13 | 10 | 4 | 0 | — | — |
| [`mur`](../1_extraccion/ccaa/mur/trazabilidad-mur.md) Región de Murcia | 2015-2026 | 13 | 8 | 2 | 0 | — | — |
| [`ara`](../1_extraccion/ccaa/ara/trazabilidad-ara.md) Aragón | 2015-2026 | 11 | 7 | 3 | 232 | 9.543,00 | dependencia, discapacidad |
| [`mad`](../1_extraccion/ccaa/mad/trazabilidad-mad.md) Comunidad de Madrid | 2015-2026 | 12 | 7 | 6 | 0 | — | salud_mental |
| [`clm`](../1_extraccion/ccaa/clm/trazabilidad-clm.md) Castilla-La Mancha | 2015-2026 | 12 | 6 | 1 | 25 | 4.091,56 | diversidad |
| [`cnt`](../1_extraccion/ccaa/cnt/trazabilidad-cnt.md) Cantabria | 2015-2026 | 12 | 6 | 5 | 0 | — | diversidad |
| [`ast`](../1_extraccion/ccaa/ast/trazabilidad-ast.md) Principado de Asturias | 2015-2026 | 11 | 5 | 1 | 0 | — | discapacidad, salud_mental |
| [`and`](../1_extraccion/ccaa/and/trazabilidad-and.md) Andalucía | 2015-2026 | 12 | 4 | 6 | 64 | 65.514,82 | direccion |
| [`cym`](../1_extraccion/ccaa/cym/trazabilidad-cym.md) Castilla y León | 2015-2026 | 13 | 3 | 4 | 0 | — | — |
| [`gal`](../1_extraccion/ccaa/gal/trazabilidad-gal.md) Galicia | 2015-2026 | 13 | 2 | 0 | 0 | — | — |
| [`can`](../1_extraccion/ccaa/can/trazabilidad-can.md) Canarias | 2015-2026 | 12 | 1 | 0 | 0 | — | salud_mental |
| [`cat`](../1_extraccion/ccaa/cat/trazabilidad-cat.md) Cataluña | 2015-2026 | 12 | 1 | 0 | 0 | — | salud_mental |
| [`ext`](../1_extraccion/ccaa/ext/trazabilidad-ext.md) Extremadura | 2015-2026 | 11 | 1 | 1 | 0 | — | discapacidad, salud_mental |
| [`nav`](../1_extraccion/ccaa/nav/trazabilidad-nav.md) Comunidad Foral de Navarra | 2015-2026 | 13 | 1 | 0 | 0 | — | — |
| [`pvc`](../1_extraccion/ccaa/pvc/trazabilidad-pvc.md) País Vasco | 2015-2026 | 10 | 1 | 2 | 0 | — | dependencia, discapacidad, salud_mental |

## 2 · Top 60 alertas por impacto absoluto (M€ nominales)

> Ordenadas por el importe en juego, no por el % — son las que más pueden distorsionar
> la visualización. `TOTAL` = salto del total extraído del ejercicio (≥ 25 %).

| # | Impacto (M€) | CCAA | Año | Concepto | Tipo | Detalle |
|---:|---:|---|---|---|---|---|
| 1 | 2.593,90 | `clm` | 2022 | `TOTAL` | **SALTO** | 9.667,09 → 12.260,99 M€ (+26,8 %) |
| 2 | 615,62 | `and` | 2020 | `empleo` | **SALTO** | 530,18 → 1.145,80 M€ (+116,1 % ⚠) |
| 3 | 460,69 | `and` | 2016 | `empleo` | **SALTO** | 1.016,66 → 555,97 M€ (−45,3 % ⚠) |
| 4 | 429,54 | `mad` | 2016 | `idi` | **SALTO** | 444,57 → 15,03 M€ (−96,6 % ⚠) |
| 5 | 419,96 | `pvc` | 2026 | `empleo` | **SALTO** | 838,17 → 418,21 M€ (−50,1 % ⚠) |
| 6 | 414,70 | `cat` | 2022 | `vivienda` | **SALTO** | 242,92 → 657,63 M€ (+170,7 % ⚠) |
| 7 | 378,79 | `val` | 2020 | `dependencia` | **SALTO** | 823,33 → 1.202,12 M€ (+46,0 % ⚠) |
| 8 | 302,97 | `mad` | 2016 | `discapacidad` | **APARECE** | 0 → 302,97 M€ |
| 9 | 258,91 | `mad` | 2024 | `vivienda` | **SALTO** | 292,39 → 551,30 M€ (+88,6 % ⚠) |
| 10 | 250,88 | `mad` | 2016 | `empleo` | **SALTO** | 206,24 → 457,12 M€ (+121,6 % ⚠) |
| 11 | 230,62 | `val` | 2020 | `discapacidad` | **SALTO** | 279,77 → 49,15 M€ (−82,4 % ⚠) |
| 12 | 230,47 | `and` | 2026 | `vivienda` | **SALTO** | 488,87 → 719,35 M€ (+47,1 % ⚠) |
| 13 | 200,43 | `val` | 2016 | `discapacidad` | **APARECE** | 0 → 200,43 M€ |
| 14 | 179,52 | `mad` | 2016 | `vivienda` | **SALTO** | 336,08 → 515,60 M€ (+53,4 % ⚠) |
| 15 | 171,83 | `and` | 2023 | `vivienda` | **SALTO** | 246,78 → 418,60 M€ (+69,6 % ⚠) |
| 16 | 164,40 | `val` | 2022 | `vivienda` | **SALTO** | 216,86 → 381,26 M€ (+75,8 % ⚠) |
| 17 | 156,42 | `bal` | 2023 | `turismo` | **SALTO** | 32,02 → 188,44 M€ (+488,5 % ⚠) |
| 18 | 135,20 | `cym` | 2023 | `idi` | **SALTO** | 303,24 → 438,44 M€ (+44,6 % ⚠) |
| 19 | 130,34 | `gal` | 2021 | `idi` | **SALTO** | 264,88 → 395,22 M€ (+49,2 % ⚠) |
| 20 | 125,29 | `bal` | 2025 | `empleo` | **SALTO** | 29,60 → 154,89 M€ (+423,3 % ⚠) |
| 21 | 116,89 | `clm` | 2023 | `vivienda` | **SALTO** | 106,60 → 223,49 M€ (+109,7 % ⚠) |
| 22 | 115,62 | `bal` | 2024 | `empleo` | **SALTO** | 145,22 → 29,60 M€ (−79,6 % ⚠) |
| 23 | 108,48 | `mad` | 2018 | `idi` | **SALTO** | 16,14 → 124,63 M€ (+671,9 % ⚠) |
| 24 | 105,89 | `val` | 2022 | `idi` | **SALTO** | 148,63 → 254,52 M€ (+71,2 % ⚠) |
| 25 | 97,54 | `val` | 2026 | `idi` | **SALTO** | 226,08 → 323,62 M€ (+43,1 % ⚠) |
| 26 | 95,26 | `val` | 2025 | `empleo` | **SALTO** | 208,25 → 303,50 M€ (+45,7 % ⚠) |
| 27 | 89,98 | `bal` | 2020 | `empleo` | **SALTO** | 111,71 → 21,73 M€ (−80,5 % ⚠) |
| 28 | 89,57 | `val` | 2021 | `empleo` | **SALTO** | 169,46 → 259,03 M€ (+52,9 % ⚠) |
| 29 | 83,32 | `bal` | 2021 | `empleo` | **SALTO** | 21,73 → 105,06 M€ (+383,4 % ⚠) |
| 30 | 75,89 | `cym` | 2023 | `vivienda` | **SALTO** | 173,26 → 249,15 M€ (+43,8 % ⚠) |
| 31 | 74,76 | `mad` | 2022 | `idi` | **SALTO** | 154,24 → 229,00 M€ (+48,5 % ⚠) |
| 32 | 69,33 | `bal` | 2026 | `vivienda` | **SALTO** | 98,03 → 28,70 M€ (−70,7 % ⚠) |
| 33 | 68,17 | `bal` | 2023 | `vivienda` | **SALTO** | 36,45 → 104,62 M€ (+187,0 % ⚠) |
| 34 | 68,13 | `gal` | 2021 | `turismo` | **SALTO** | 127,64 → 195,77 M€ (+53,4 % ⚠) |
| 35 | 67,48 | `val` | 2019 | `vivienda` | **SALTO** | 102,84 → 170,32 M€ (+65,6 % ⚠) |
| 36 | 66,50 | `clm` | 2022 | `turismo` | **SALTO** | 37,80 → 104,30 M€ (+176,0 % ⚠) |
| 37 | 66,39 | `bal` | 2023 | `salud_mental` | **SALTO** | 49,15 → 115,54 M€ (+135,1 % ⚠) |
| 38 | 59,95 | `ast` | 2025 | `vivienda` | **SALTO** | 98,36 → 158,31 M€ (+60,9 % ⚠) |
| 39 | 58,00 | `lar` | 2021 | `turismo` | **APARECE** | 0 → 58,00 M€ |
| 40 | 56,05 | `ara` | 2016 | `vivienda` | **SALTO** | 74,55 → 18,50 M€ (−75,2 % ⚠) |
| 41 | 55,35 | `cym` | 2023 | `turismo` | **SALTO** | 29,88 → 85,24 M€ (+185,2 % ⚠) |
| 42 | 53,67 | `bal` | 2019 | `turismo` | **SALTO** | 91,64 → 37,97 M€ (−58,6 % ⚠) |
| 43 | 52,48 | `lar` | 2017 | `direccion` | **SALTO** | 57,66 → 5,18 M€ (−91,0 % ⚠) |
| 44 | 51,44 | `clm` | 2021 | `vivienda` | **SALTO** | 59,40 → 110,84 M€ (+86,6 % ⚠) |
| 45 | 50,25 | `bal` | 2018 | `turismo` | **SALTO** | 41,39 → 91,64 M€ (+121,4 % ⚠) |
| 46 | 49,61 | `ara` | 2023 | `vivienda` | **SALTO** | 51,68 → 101,30 M€ (+96,0 % ⚠) |
| 47 | 49,49 | `ext` | 2023 | `vivienda` | **SALTO** | 84,77 → 134,26 M€ (+58,4 % ⚠) |
| 48 | 48,63 | `bal` | 2024 | `salud_mental` | **SALTO** | 115,54 → 66,91 M€ (−42,1 % ⚠) |
| 49 | 47,42 | `ara` | 2024 | `vivienda` | **SALTO** | 101,30 → 53,88 M€ (−46,8 % ⚠) |
| 50 | 45,27 | `lar` | 2020 | `turismo` | **DESAPARECE** | 45,27 M€ → 0 |
| 51 | 43,22 | `val` | 2021 | `idi` | **SALTO** | 105,41 → 148,63 M€ (+41,0 % ⚠) |
| 52 | 39,97 | `clm` | 2016 | `salud_mental` | **SALTO** | 61,03 → 101,00 M€ (+65,5 % ⚠) |
| 53 | 39,95 | `ast` | 2023 | `vivienda` | **SALTO** | 41,28 → 81,24 M€ (+96,8 % ⚠) |
| 54 | 36,79 | `nav` | 2022 | `vivienda` | **SALTO** | 65,78 → 102,57 M€ (+55,9 % ⚠) |
| 55 | 36,75 | `mur` | 2021 | `turismo` | **SALTO** | 23,15 → 59,90 M€ (+158,7 % ⚠) |
| 56 | 36,35 | `can` | 2019 | `vivienda` | **SALTO** | 89,63 → 125,98 M€ (+40,6 % ⚠) |
| 57 | 36,28 | `ara` | 2024 | `turismo` | **SALTO** | 52,71 → 89,00 M€ (+68,8 % ⚠) |
| 58 | 36,09 | `bal` | 2019 | `vivienda` | **SALTO** | 29,04 → 65,13 M€ (+124,3 % ⚠) |
| 59 | 35,93 | `lar` | 2016 | `empleo` | **SALTO** | 63,42 → 27,49 M€ (−56,7 % ⚠) |
| 60 | 34,54 | `clm` | 2023 | `empleo` | **SALTO** | 82,84 → 117,38 M€ (+41,7 % ⚠) |

*Total de alertas en las 17 CCAA: 99.*

