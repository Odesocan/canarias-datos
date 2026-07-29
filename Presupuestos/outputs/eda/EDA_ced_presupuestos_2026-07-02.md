# EDA · `ced_presupuestos` — missings y outliers

> Generado por `outputs/eda/eda_ced_presupuestos.py` sobre `4_carga/ced_presupuestos.csv`.
> Rev. 2026-07-02. Valores `imp_` en euros CONSTANTES (deflactados).

**Datos:** 381 filas (194 autonómica + 187 hacienda) · 17 CCAA · 2015-2026. El análisis de conceptos es sobre la **capa autonómica**; la hacienda solo trae `total`.

## 1 · Missings

### 1.1 · Combinaciones CCAA-año ausentes (10 de 204 posibles)

| CCAA | años ausentes |
|------|---------------|
| cat | 2018, 2021, 2025 |
| cym | 2015, 2019, 2020, 2022 |
| lar | 2023 |
| mur | 2026 |
| val | 2015 |

> Nota: muchos son años sin fuente publicada (cym 2019/2020/2022, cat 2018/2021/2025, val ≤2015) o fuente que falló en el pipeline (mur 2026). No confundir con NULL de concepto.

### 1.2 · NULL por concepto (capa autonómica)

| concepto | % filas NULL | filas con dato | ¿estructural? |
|----------|:---:|:---:|---|
| salud_mental | 54% | 89 | sí en 7 CCAA: ast, clm, cnt, ext, gal, mad, pvc |
| discapacidad | 26% | 143 | sí en 5 CCAA: ara, ast, ext, gal, pvc |
| diversidad | 18% | 160 |  |
| dependencia | 13% | 169 | sí en 3 CCAA: ara, ast, pvc |
| empleo | 10% | 175 |  |
| igualdad | 9% | 177 |  |
| soberania | 7% | 181 |  |
| turismo | 3% | 189 |  |
| idi | 2% | 190 |  |
| vivienda | 2% | 191 |  |
| sanidad | 0% | 194 |  |
| educacion | 0% | 194 |  |
| direccion | 0% | 194 |  |

### 1.3 · Cobertura CCAA × concepto (nº de años con dato / años presentes)

| CCAA | años | sanidad | educacion | soberania | direccion | vivienda | empleo | idi | dependencia | discapacidad | salud_mental | diversidad | turismo | igualdad |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| and | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8 | ✓ | ✓ | ✓ |
| ara | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · | 8 | ✓ | ✓ |
| ast | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| bal | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| can | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ |
| cat | 9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ |
| clm | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ |
| cnt | 12 | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ |
| cym | 8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ext | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | ✓ | ✓ | ✓ |
| gal | 12 | ✓ | ✓ | ✓ | ✓ | 9 | ✓ | 8 | ✓ | 7 | · | 9 | 8 | 7 |
| lar | 11 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10 | 10 | 3 | 8 | 10 | 9 |
| mad | 12 | ✓ | ✓ | 11 | ✓ | ✓ | ✓ | ✓ | ✓ | 11 | · | ✓ | ✓ | ✓ |
| mur | 11 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| nav | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4 | · | ✓ | ✓ | ✓ |
| pvc | 12 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · | ✓ | ✓ | 2 |
| val | 11 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

> `✓` = todos los años; `·` = 0 años (NULL total); número = años parciales.

### 1.4 · ⚠️ Divergencia Python (staging) vs modelado (R) — concepto

El modelado R re-deriva el concepto desde el `correspondencias.yml` **RAÍZ (global)**, NO desde los `1_extraccion/ccaa/*/correspondencias.yml` (Python) donde viven los fixes 2026-07-02. Donde R mapea a un concepto distinto, R gana (el fallback solo actúa si R es NA). Resultado: la tabla entregada NO refleja del todo los fixes conceptuales.

**(a) En el staging (Python, correcto) pero NULL en la tabla (R lo pierde) — 8:**

| CCAA | concepto |
|------|----------|
| ara | salud_mental |
| can | salud_mental |
| cat | salud_mental |
| clm | diversidad |
| cnt | diversidad |
| cnt | soberania |
| nav | salud_mental |
| pvc | salud_mental |

**(b) En la tabla (R) pero NO en el staging — concepto FABRICADO por el mapping viejo — 6:**

| CCAA | concepto |
|------|----------|
| ast | dependencia |
| ast | discapacidad |
| ast | salud_mental |
| clm | salud_mental |
| cnt | salud_mental |
| gal | discapacidad |

> **Acción:** propagar los fixes 2026-07-02 al `correspondencias.yml` RAÍZ (o hacer que la transformación prefiera el concepto Python) y re-modelar + recargar. Sin eso, `clm/cnt` diversidad, 5×`salud_mental`, etc. faltan, y `ast/gal/clm/cnt` arrastran salud_mental/discapacidad FABRICADOS que los fixes ya eliminaron en el staging.


## 2 · Outliers

> ⚠️ **Aviso metodológico:** los `imp_` de esta tabla están **deflactados a € constantes**, así que el per-cápita calculado aquí sale ~20-30 % por encima del nominal en los años recientes. La banda de sanidad 900-2300 está calibrada en €/hab NOMINALES → aquí sobre-marca. El chequeo de banda AUTORITATIVO (nominal, sobre el staging) es `tools/auditoria_magnitud.py`; abajo se anota qué anomalías son reales (documentadas en nominal) y cuáles son artefacto de la deflación.

### 2.1 · Per-cápita €/hab por concepto — outliers (IQR 1.5× sobre todas las CCAA-año)

| concepto | mediana €/hab | banda IQR | nº outliers | CCAA-año atípicos (top) |
|----------|:---:|:---:|:---:|---|
| sanidad | 1642 | 545–2753 | 2 | ast2015=2899, and2022=2881 |
| educacion | 1016 | 344–1688 | 8 | bal2020=9, mad2017=36, mad2016=37, bal2021=79 |
| soberania | 146 | 0–787 | 13 | ext2024=1039, ext2025=1039, ext2026=1039, ext2023=980 |
| direccion | 649 | 0–2172 | 4 | nav2026=2877, nav2025=2680, nav2024=2599, nav2023=2184 |
| vivienda | 51 | 0–151 | 10 | nav2026=229, nav2025=224, nav2024=221, gal2026=208 |
| empleo | 92 | 0–386 | 3 | pvc2021=412, pvc2020=398, pvc2022=396 |
| idi | 59 | 0–220 | 11 | lar2025=355, lar2026=353, lar2024=334, lar2022=331 |
| dependencia | 198 | 0–513 | 1 | gal2026=515 |
| discapacidad | 42 | 0–133 | 11 | mur2025=280, mur2024=266, mur2023=244, mur2022=212 |
| salud_mental | 33 | 0–132 | 12 | ast2026=457, ast2025=451, ast2023=433, ast2024=413 |
| diversidad | 35 | 0–203 | 22 | nav2026=497, nav2025=451, nav2024=444, nav2023=407 |
| turismo | 22 | 0–80 | 15 | lar2024=247, lar2021=225, bal2024=221, lar2026=195 |
| igualdad | 10 | 0–32 | 20 | pvc2024=233, cnt2023=84, cnt2022=80, ext2023=75 |

### 2.2 · Sanidad €/hab alto (per-cápita en € CONSTANTES; banda nominal 900–2300)

| CCAA | año | €/hab (const.) | ¿anomalía real (nominal)? |
|------|:---:|:---:|---|
| ast | 2015 | 2899 | 🔴 SÍ — documentada (ver ficha) |
| and | 2022 | 2881 | 🔴 SÍ — documentada (ver ficha) |
| and | 2021 | 2705 | 🔴 SÍ — documentada (ver ficha) |
| cym | 2024 | 2584 | 🟢 no — en banda en nominal; artefacto de € constantes |
| cym | 2025 | 2584 | 🟢 no — en banda en nominal; artefacto de € constantes |
| cym | 2026 | 2584 | 🟢 no — en banda en nominal; artefacto de € constantes |
| ast | 2026 | 2529 | 🔴 SÍ — documentada (ver ficha) |
| cym | 2023 | 2521 | 🟢 no — en banda en nominal; artefacto de € constantes |
| and | 2020 | 2458 | 🔴 SÍ — documentada (ver ficha) |
| ast | 2025 | 2426 | 🔴 SÍ — documentada (ver ficha) |
| pvc | 2026 | 2408 | 🔴 SÍ — documentada (ver ficha) |
| cym | 2021 | 2354 | 🟢 no — en banda en nominal; artefacto de € constantes |
| nav | 2026 | 2331 | 🟢 no — en banda en nominal; artefacto de € constantes |
| cnt | 2026 | 2314 | 🟢 no — en banda en nominal; artefacto de € constantes |
| pvc | 2025 | 2313 | 🔴 SÍ — documentada (ver ficha) |
| ast | 2024 | 2304 | 🟢 no — en banda en nominal; artefacto de € constantes |

> De los 16 marcados, **8 son anomalías reales** (documentadas: `and` perímetro rama CSV, `ast` 2015 doble conteo 413D+412B, `pvc` 2025-26 alta inversión vasca) y **8 son artefacto de la deflación** (en banda al medirse en nominal: cym, nav, cnt, etc.). Confirmar siempre con `auditoria_magnitud.py` (nominal).

### 2.3 · Saltos año-a-año (concepto ≥ 50 M€)

**(a) Saltos de magnitud reales** (±40–200 %, entre dos valores no triviales): 95. Candidatos a revisar contra la ficha (seam de método, cambio de fuente).

| concepto | CCAA | año | var % |
|----------|------|:---:|:---:|
| vivienda | bal | 2023 | +187% |
| turismo | cym | 2023 | +185% |
| vivienda | cat | 2022 | +171% |
| turismo | mur | 2021 | +159% |
| igualdad | and | 2017 | +156% |
| idi | bal | 2024 | +142% |
| salud_mental | bal | 2023 | +135% |
| turismo | clm | 2022 | +128% |
| vivienda | clm | 2023 | +124% |
| vivienda | bal | 2019 | +124% |
| empleo | mad | 2016 | +122% |
| diversidad | cat | 2022 | +117% |
| sanidad | and | 2020 | +117% |
| empleo | pvc | 2025 | +116% |
| direccion | mad | 2022 | +108% |
| dependencia | val | 2024 | +106% |
| dependencia | and | 2021 | +100% |
| turismo | mad | 2022 | +97% |
| vivienda | ast | 2023 | +97% |
| vivienda | clm | 2021 | +96% |
| … | | | (+75 más) |

**(b) Apariciones / cambios de escala** (>200 %, base ~0): 11. NO son anomalías de magnitud: son conceptos que empiezan a mapearse (muchos por los fixes 2026-07-02: pvc igualdad, val salud_mental, and diversidad…) o cambios de perímetro.

| concepto | CCAA | año | var % |
|----------|------|:---:|:---:|
| dependencia | ast | 2024 | +9522% |
| igualdad | pvc | 2024 | +7022% |
| educacion | bal | 2022 | +1260% |
| educacion | mad | 2018 | +860% |
| educacion | bal | 2021 | +766% |
| turismo | bal | 2023 | +554% |
| salud_mental | val | 2024 | +423% |
| vivienda | gal | 2025 | +401% |
| empleo | and | 2020 | +237% |
| turismo | gal | 2022 | +213% |
| soberania | and | 2020 | +211% |

## 3 · Figuras

- `fig_missings_heatmap.png` — cobertura de concepto por CCAA (verde=completo, rojo=NULL).
- `fig_percapita_boxplots.png` — distribución per-cápita por concepto (outliers marcados).
- `fig_sanidad_percapita.png` — sanidad €/hab por CCAA con la banda de plausibilidad.

## 4 · Síntesis

- **🚩 Lo más importante — la tabla entregada no refleja del todo los fixes 2026-07-02:** 8 concepto-CCAA están bien en el staging (Python) pero se pierden en el modelado R, y 6 conceptos FABRICADOS por el mapping viejo siguen en la tabla. Causa: el modelado R usa el `correspondencias.yml` RAÍZ, no los per-CCAA de Python (§1.4). **Requiere propagar los fixes al raíz + re-modelar + recargar.**
- **Missings de concepto:** los 3 más difíciles son **salud_mental, discapacidad, diversidad** — servicios sociales especializados que muchas CCAA no presupuestan como programa propio (NULL estructural, no fallo de extracción; ver STRUCTURAL en el script y las fichas).
- **Combinaciones ausentes:** 10 CCAA-año, casi todas por falta de fuente publicada o prórroga, no por error.
- **Outliers per-cápita (en € constantes):** los de sanidad se concentran en `and` (perímetro rama CSV), `ast` 2015 y `pvc` 2025-26 (documentados); el resto de flags de banda son artefacto de la deflación. Por concepto, los altos son legítimos por perfil (soberanía alta en `ext`; dirección/diversidad altas en `nav` foral; empleo alto en `pvc`).
- **Saltos de magnitud reales:** 95 (±40-200 %); las 11 'apariciones' (>200 %) son conceptos recién mapeados por los fixes 2026-07-02, no anomalías.
- **🔎 Hallazgo a revisar (nuevo):** `educacion` de **Baleares se desploma en 2020-2021** (bal 2020 ≈ 9 €/hab vs ~96 en 2019) y en Madrid queda infra-capturada (proxy-centro). Ninguna es de los 12 fixes: son candidatas para la siguiente iteración (bal 2020-21 parece un año con secciones incompletas, como 2015-16).
