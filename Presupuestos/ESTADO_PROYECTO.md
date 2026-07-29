<!--
  Documento de ESTADO vivo del epígrafe de Presupuestos (ODESOCAN · Canarias en Datos).
  Es una FOTO del estado + instrucciones para regenerarla. Actualízalo tras cada hito
  (nueva CCAA-año, fix conceptual, cierre de capa). Ver §7 "Cómo actualizar".
-->

# 📊 Estado del proyecto · Presupuestos autonómicos

> **ODESOCAN · Canarias en Datos** — extracción del gasto de las 17 CCAA desagregado en
> **13 conceptos de política social**, por ejercicio y por capa.
>
> | | |
> |---|---|
> | **Última actualización** | 2026-07-16 |
> | **Fase** | Capa autonómica **cerrada** · capa Hacienda 2015-2025 · validación final en curso |
> | **Fuente de esta foto** | `outputs/staging_py_2026-07-16.csv` (23.078 filas, € nominales) |
> | **Cómo se regeneró** | ver [§7 · Cómo actualizar este documento](#7--cómo-actualizar-este-documento) |

---

## 1 · Resumen ejecutivo

La **capa autonómica está completa y consolidada**: las **204 celdas** posibles
(17 CCAA × 12 ejercicios, 2015-2026) están extraídas, transformadas y en estado **VERDE**.
No queda ningún hueco de año en el rango objetivo.

| Métrica | Valor |
|---|---:|
| Celdas CCAA-año extraídas | **204 / 204** |
| Comunidades autónomas | **17 / 17** |
| Ejercicios cubiertos | **2015 – 2026** (12) |
| Celdas VERDE estricto (≥80 % filas clasificadas) | **38** |
| Celdas VERDE pragmático (35-80 %) | **166** |
| Celdas bajo umbral | **0** |
| Media de conceptos captados (de 13) por CCAA | **≈ 11,7** |
| Filas de detalle en el staging | **23.078** |

> **VERDE estricto vs. pragmático:** casi todas las CCAA quedan en pragmático (~60-70 % de
> filas con concepto). Es lo esperado y correcto: los presupuestos incluyen mucho gasto
> **no-social** (deuda, dirección general, carreteras…) que legítimamente queda sin concepto.
> No es un déficit de extracción.

---

## 2 · Estado por capas

| Capa | Descripción | Estado |
|---|---|---|
| **Autonómica** | Dato oficial de cada CCAA, 13 conceptos | ✅ **204/204 VERDE** (2015-2026) |
| **Hacienda** (SGCIEF) | Serie homogénea `total` del Ministerio | 🟡 **2015-2025** cargada · **2026 pendiente** (sin publicar) |
| **Conciliación §2.6** | Cuadre contra totales de Hacienda | ✅ **Superada a nivel TOTAL** (187/187 OK) |
| **Benford** | Test de dígitos sobre importes | ✅ Conforme |
| **Carga en DB deflactada** | € constantes en `ced_presupuestos` | 🟡 Pendiente cierre certificado (requiere R+psql) |
| **Indicador % PIB regional** | `pibreg_<concepto>` en `ced_presupuestos` | ✅ Integrado en `modelado.R` (PIB INE 2015-2024 + bootstrap 2025-2026) |

> **Indicador objetivo `pct_pib_regional`** (2026-07-16): gasto de cada área ÷ **PIB regional de la
> propia CCAA** × 100 — comparable entre territorios de tamaño distinto (mide prioridad política, no
> volumen). PIB regional real del INE (Contabilidad Regional op. 30679, `fuentes/externos/pib_regional_ccaa.csv`),
> con 2025-2026 completados por **bootstrap** de las tasas de crecimiento (`pib_origen`='proyeccion').
> Extremadura dedica el 8,6 % de su PIB a sanidad vs Madrid 3,2 % — invierte el ranking absoluto.

---

## 3 · Tabla 1 · Cobertura y calidad — CCAA × ejercicio

Cada celda = **clasificación** + **nº de conceptos** (de 13) con importe > 0.
`V` = VERDE estricto (≥80 %) · `v` = VERDE pragmático (35-80 %).

| CCAA | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | Media |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Andalucía | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | **13.0** |
| Aragón | v9 | v10 | v10 | v10 | v10 | v10 | v10 | v10 | v10 | v11 | v11 | v11 | 10.2 |
| Asturias | v9 | v9 | v9 | v9 | v9 | v9 | v10 | v10 | v10 | v10 | v10 | v10 | 9.5 |
| Baleares | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | **13.0** |
| Canarias | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | 12.0 |
| Cataluña | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | **13.0** |
| Cast.-La Mancha | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | 12.0 |
| Cantabria | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | 11.0 |
| Cast. y León | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **13.0** |
| Extremadura | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | **V11** | 11.0 |
| Galicia | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v8 | v7 | v7 | v8 | **V8** | 9.6 |
| La Rioja | v9 | v9 | v12 | v9 | v12 | v11 | v12 | v12 | v12 | v13 | **V13** | v13 | 11.4 |
| Madrid | v10 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | 11.8 |
| Murcia | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | v13 | **13.0** |
| Navarra | v13 | v13 | v13 | v13 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | v12 | 12.3 |
| País Vasco | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | v11 | 11.0 |
| C. Valenciana | **V12** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | **V13** | 12.9 |

**Global:** 204 celdas · 38 VERDE estricto + 166 VERDE pragmático · 0 bajo umbral.

---

## 4 · Tabla 2 · Cobertura por concepto (nº de años con dato, de 12)

Explica por qué algunas celdas no llegan a 13: los huecos son casi siempre **nulos
estructurales** (gasto fuera del catálogo funcional de esa CCAA), no fallos de extracción.
`0` = concepto sin ningún año con dato.

| Concepto | and | ara | ast | bal | can | cat | clm | cnt | cym | ext | gal | lar | mad | mur | nav | pvc | val | ΣCCAA |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| sanidad | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| educacion | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| soberania | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 11 | 12 | 12 | 12 | 12 | 17/17 |
| direccion | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| vivienda | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 9 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| empleo | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| idi | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 8 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| dependencia | 12 | **0** | **0** | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | **0** | 12 | 14/17 |
| discapacidad | 12 | **0** | **0** | 12 | 12 | 12 | 12 | **0**¹ | 12 | **0** | **0** | 9 | 11 | 12 | 4 | **0** | 11 | 11/17 |
| salud_mental | 12 | 3² | **0** | 12 | **0**¹ | 12 | **0** | **0** | 12 | **0** | **0** | 3² | **0** | 12 | 12 | 12 | 12 | 10/17 |
| diversidad | 12 | 11 | 6 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 11 | 9 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| turismo | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 8 | 11 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| igualdad | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 7 | 9 | 12 | 12 | 12 | 12 | 12 | 17/17 |

**Lectura:**
- **7 conceptos con serie completa** en las 17 CCAA (sanidad, educación, soberanía, dirección, empleo, vivienda, idi — salvo huecos puntuales de Galicia y Madrid).
- **Conceptos con menor cobertura:** `salud_mental` (10/17), `discapacidad` (11/17), `dependencia` (14/17). Partidas que muchas CCAA no desagregan como línea propia (salud mental dentro de sanidad; dependencia/discapacidad dentro de servicios sociales). En pvc son además competencia **foral** (diputaciones, fuera del presupuesto de la CAE).
- **Nulos estructurales confirmados:** Aragón, Asturias y País Vasco no tienen dependencia/discapacidad como programa funcional propio; Galicia 2022-26 (CSV consolidado) baja a 7-8 conceptos.
- ¹ **FIX 2026-07-16 (falsos positivos retirados):** cnt·discapacidad (era `232C` "Actividades Juveniles", 0,03 M) y can·salud_mental (era `313A` "Salud Pública", 0,3 M) pasan a NULL estructural honesto.
- ² **Programas de nueva creación 2024** (ara `4133`, lar `3.1.3.3` "Salud Mental"): cobertura parcial legítima — el concepto nace en 2024 en el origen, no retropolar.

---

## 5 · Anomalías de magnitud (afectan a € , no a cobertura)

La cobertura conceptual y la corrección del importe son ejes distintos. Estado tras los
**fixes del 2026-07-16** (`tools/auditoria_magnitud.py`: **9 → 4 anomalías, TEST 1 continuidad LIMPIO**):

| CCAA | Ejercicios | Problema | Estado |
|---|---|---|---|
| Andalucía | 2015/16/20/21 (rama CSV) | Doble conteo transferencia (`41H`) + ejecución SAS (`41C`/`41G`) | ✅ **RESUELTA 2026-07-16** (filtro CENTRO GESTOR consejería; sanidad 2021: 22,9→11,45 B; serie monótona continua) |
| Asturias | 2015 | Doble conteo SESPA: par `413D` 1,435 B + `412B` 1,434 B de los anexos del tomo | ✅ **RESUELTA 2026-07-16** (gate al bloque DISTRIBUCIÓN; sanidad 2,92→1,48 B) |
| Asturias | 2025-2026 | €/hab 2422-2524 (banda alta) | Banda-alta **estructural** — serie monótona sin par duplicado, crecimiento real (no bug) |
| País Vasco | 2025-2026 | €/hab ~2300-2400 | Inversión real alta (baseline conocido, **no** bug) |

Pendientes menores identificados en la auditoría del 2026-07-16: dedup ara `3132` (~-4,6 % total),
revisión ast `313E`→direccion, seams de origen a documentar (val discapacidad 2020, nav 2019).

---

## 6 · Trabajo pendiente

- [ ] **Capa Hacienda 2026** — SGCIEF del Ministerio aún sin publicar; no hay `fuentes/raw/hacienda/2026/`.
- [ ] **Carga definitiva certificada** en la DB deflactada (€ constantes) — `bash outputs/cierre_2026-07-06.sh` en el Mac (requiere R + psql).
- [ ] **Conciliación funcional §2.6 por concepto** — requiere la liquidación funcional BDGEL del Ministerio (no publicada en el SGCIEF descargado).
- [x] ~~**Anomalías de magnitud** and CSV / ast 2015~~ — **resueltas 2026-07-16** (ver §5).
- [ ] Dedup ara `3132` (duplicado sistemático, ~-4,6 % del total aragonés).
- [ ] Revisar asignación ast `313E` "Gestión de Servicios Sociales" (252 M/año) → `direccion`.
- [ ] Galicia 2022-26: comprobar si existen los tomos `PROGR_I/II` (recuperaría vivienda/igualdad/diversidad).
- [ ] Mejora conceptual menor: `art.10 → direccion`.

---

## 7 · Cómo actualizar este documento

Este `.md` es una **foto**. Para regenerar las cifras tras nuevos extractores, fixes o cierres:

```bash
cd "CANARIAS EN DATOS/Presupuestos"

# 1. Regenerar el staging del día (extracción + transformación de las 17 CCAA)
#    — opción A: pipeline completo con R (necesita R+psql en el Mac)
Rscript 00_maestro.R --steps=extraccion,transformacion --with-db=false
#    — opción B: build directo en Python (sin R)
python3 outputs/build_staging_py.py            # → outputs/staging_py_<fecha>.csv

# 2. Recomputar cobertura y calidad por CCAA×año (Tabla 1)
python3 outputs/build_tabla_resumen.py          # → outputs/tabla_resumen_<fecha>.{md,csv}

# 3. Recomputar cobertura por concepto (Tabla 2)
python3 outputs/cobertura_concepto_2026-07-10.py   # → cobertura_concepto_<fecha>.md

# 4. Auditar magnitudes (gate de anomalías €, §5)
python3 tools/auditoria_magnitud.py --csv outputs/staging_py_<fecha>.csv

# 5. Volcar las nuevas tablas en las §3, §4 y §5 de este documento,
#    actualizar la fecha del encabezado y añadir una fila al registro de la §8.
```

**Criterio VERDE** (para clasificar una celda nueva): motor OK · filas ≥ 30 ·
≥ 5 conceptos distintos · concepto no nulo en ≥ 80 % (estricto `V`) o ≥ 35 % (pragmático `v`).

**Definiciones fijas** (no cambian entre versiones):
- **13 conceptos canónicos:** `sanidad · educacion · soberania · direccion · vivienda · empleo · idi · dependencia · discapacidad · salud_mental · diversidad · turismo · igualdad`.
- **Celda** = tupla `(ccaa, ejercicio)`. **Capa** = `autonomica` (oficial CCAA) | `hacienda` (serie homogénea Ministerio).
- € del staging = **nominales**; la DB guarda € **constantes** (deflactados, ~×1,3 en años antiguos).

---

## 8 · Registro de actualizaciones

> Añade una fila por cada actualización de esta foto. La bitácora detallada noche-a-noche
> vive en `logs/progreso.md`; aquí solo el resumen de hitos de estado.

| Fecha | Celdas VERDE | Cambio principal |
|---|:--:|---|
| 2026-07-16 (tarde) | 204/204 | **Indicador % PIB regional** integrado en el pipeline R (`modelado.R`): PIB INE por CCAA 2015-2024 + bootstrap 2025-2026, columnas `pibreg_<concepto>`. |
| 2026-07-16 (tarde) | 204/204 | **Fixes de magnitud y catálogo** (auditoría 3 frentes): and rama CSV consolidada (sanidad ~×2 → serie continua), ast 2015 sin doble conteo SESPA, falsos positivos cnt `232C`/can `313A` retirados. Auditoría 9→4 anomalías, TEST 1 limpio. |
| 2026-07-16 | 204/204 | Foto inicial de este documento. Spot-check VERDE (val, bal, nav, cym, mur 2024) · sin regresiones. |
| 2026-07-02 | 196/196 | Auditoría conceptual de las 17 CCAA: 12 fixes conceptuales + Galicia. Carga en `presupuestos_smoke`. |

---

*Documento de estado · ODESOCAN · Canarias en Datos · Presupuestos. Mantener junto a `CLAUDE.md` (guía técnica) y `logs/progreso.md` (bitácora).*
