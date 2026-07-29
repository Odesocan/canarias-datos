# CLAUDE.md — Guía del proyecto *Presupuestos · ODESOCAN / Canarias en Datos*

> Documento de orientación para **Claude Code**. Resume qué es el proyecto, en qué
> fase está, cómo está construido y qué trabajo queda — para que puedas continuar la
> extracción de presupuestos autonómicos de forma autónoma y sin romper lo que ya funciona.
> **Última actualización: 2026-07-02.**

---

## 0 · TL;DR (léelo y actúa)

- **Qué construimos:** el epígrafe de *Presupuestos* de [Canarias en Datos](https://odesocan.org),
  una tabla canónica (`presupuestos.ced_presupuestos`) con el gasto de las **17 CCAA**
  desagregado en **13 conceptos de política social** por **ejercicio** y por **capa**
  (autonómica = dato oficial de cada CCAA; hacienda = serie homogénea del Ministerio).
- **Fase actual:** extracción completa y consolidada. **196 ejercicios-año, 17/17 CCAA,
  0 AMARILLO, 0 ERROR** (165 VERDE_PRAGM + 31 VERDE estricto). El 2026-07-02 se auditaron
  las 17 CCAA (origen vs tratamiento) y se aplicaron **12 fixes conceptuales + Galicia**
  (ver `outputs/auditoria_conceptual_2026-07-02.md` y `logs/progreso.md`), y se CARGÓ el
  consolidado en la DB local `presupuestos_smoke` (`ced_presupuestos`: 381 filas, 17 CCAA,
  2015-2026, valores deflactados a € constantes). Quedan huecos sueltos de años, la capa
  Hacienda completa y la validación/conciliación final.
- **Tu rol (Claude Code en el Mac):** tienes **R, `psql`, red estable y sin límite de
  45 s**. Te tocan justo las tareas que el runner nocturno (sandbox Cowork, solo `python3`)
  **no puede**: descargar raws nuevos, extraer PDFs grandes, correr el maestro R y cargar
  en Postgres. El sandbox nocturno deja `fuentes.yml` y los extractores listos; tú ejecutas.
- **Regla de oro:** *no reescribas un extractor que ya está en VERDE salvo bug crítico.*
  Si tocas una CCAA y rompe el maestro, **revierte esa CCAA y sigue** — nunca bloquees a
  las verdes.

---

## 1 · El dato que perseguimos

Cada fila final de `ced_presupuestos` es `(ccaa, periodo, capa)` con una columna
`imp_<concepto>` por cada uno de los 13 conceptos. Los **13 conceptos canónicos**
(cuaderno metodológico §1.6) son:

```
sanidad · educacion · soberania · direccion · vivienda · empleo · idi ·
dependencia · discapacidad · salud_mental · diversidad · turismo · igualdad
```
(+ `total` para la capa Hacienda).

Una CCAA-año cuenta como **VERDE** cuando, tras `extract`+`transform`:
1. el motor devuelve `filas ≥ 30`,
2. `concepto` no nulo en ≥ 80 % de filas (**VERDE estricto**) o ≥ 35 % (**VERDE_PRAGM**,
   aceptable cuando los NULL son estructuralmente fuera de catálogo),
3. aparecen **≥ 5 conceptos** distintos del catálogo.

> En la práctica casi todas las CCAA quedan en **VERDE_PRAGM ~60-70 %**: los presupuestos
> incluyen mucho gasto no-social (deuda, dirección general, etc.) que correctamente queda
> sin concepto. No fuerces el 80 %.

---

## 2 · Arquitectura (5 etapas, orquestadas por R)

```
00_maestro.R  --steps=extraccion,transformacion,modelado,carga --with-db=true
   │
   ├─ 1_extraccion/      Python. Un sub-pipeline autocontenido por CCAA.
   │     ccaa/<id3>/{extract.py, transform.py, correspondencias.yml}
   │     ccaa/_common/   dispatcher (importlib) + base + helpers
   │     → invocable suelto:  python3 -m ccaa --ccaa <id3> --anio <año> --input <raw> --output <csv>
   │
   ├─ 2_transformacion/  Normaliza, deflacta, consolida staging → modelo largo.
   ├─ 3_modelado/        Pivota a imp_<concepto>, proyecciones (Prophet, opcional).
   ├─ 4_carga/           Carga en Postgres (psql / Supabase).  Smoke local: presupuestos_smoke
   └─ 5_visualizacion/   Salidas para la web.

fuentes.yml             Catálogo CANÓNICO de URLs por CCAA → ejercicio → documento.
correspondencias.yml    (raíz) tabla global; cada CCAA tiene además la suya local.
fuentes/raw/<id3>/<año>/ Raws descargados (PDF/HTML/CSV/XLS) + sidecars *.pagetext.json.
outputs/                Catálogo vivo de regresión y tablas resumen.
logs/progreso.md        Bitácora append-only (léela: cuenta la historia noche a noche).
```

**Contrato de un extractor** (detalle en `1_extraccion/ccaa/_README.md`):

```python
def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows = [ make_row(pagina=p, codigo="412A", denominacion="…",
                      importe=12_345_678.90, anio=anio) ]      # importe en EUROS
    return ExtractionResult(rows=rows, motor="<id3>-mi-formato")

# transform.py casi siempre es el patrón estándar:
def transform(rows, anio):
    return asignar_concepto_local(rows, mapping_path=__file__)   # usa correspondencias.yml
```

`asignar_concepto_local` mapea `codigo → concepto` por (1) match exacto, (2) prefijo
(`"42*"`), (3) keyword en la denominación. El dispatcher (`ccaa/_common/dispatcher.py`)
carga la CCAA por `importlib`, aplica `transform` y escribe columnas:
`pagina,codigo,denominacion,importe_eur,ccaa_id3,anio,capitulo,concepto,fuente_path,fecha_captura`.

> ⚠️ **Unidades:** algunos tomos PDF están en **miles de euros** (multiplica ×1000 en el
> extractor, p. ej. `clm` PDF); los CSV de datos abiertos suelen estar en **euros** (no
> multipliques, p. ej. `clm` CSV). Verifica siempre con un sanity-check de magnitud
> (sanidad de una CCAA mediana ≈ 2-4 mil M€).

---

## 3 · Estado por CCAA (catálogo vivo `outputs/smoke_regresion_py.csv`)

> ⚠️ **Esta tabla es un SNAPSHOT y va por detrás del catálogo.** Al 2026-07-02 la foto real
> es **196 CCAA-año, 0 AMARILLO, 0 ERROR** (varias celdas de abajo están anticuadas: p. ej.
> `ara/2016` YA NO es ERROR, `lar` y `mur` tienen 12 años no 1, `cym` está consolidado y
> completo, `mad` ya no duplica agregado+centro, `pvc` bajó a 2 conceptos NULL). Regenera la
> foto con `python3 tools/smoke_regresion_py.py`. La verdad de calidad conceptual y de los
> fixes del 2026-07-02 está en `outputs/auditoria_conceptual_2026-07-02.md` + las fichas
> `limitaciones-<id3>.md` + `logs/progreso.md`.

| id3 | CCAA | VERDE | Años extraídos | Motor | Pendiente |
|-----|------|:---:|---|---|---|
| and | Andalucía | 12 | 2015-2026 | `and-resumen-cap-prog` / `and-ckan-csv` | — |
| ara | Aragón | 12 | 2015-2026 | `ara-pdf-program-total` | 2016 OK (ya no ERROR); **fix 2026-07-02**: educación `421*/422*` (4222 "EDUC SECUNDARIA" abreviado) + soberanía `71*/5311` (agrario). Pendiente: `3132` duplicado infla total 4,6% |
| ast | Asturias | 11 | 2015-2021, 2023-2026 | `ast-distribucion-gasto` | **2022** (falta tomo de programas) |
| bal | Baleares | 10 | 2015-2016, 2018-2025 | `bal-frameset-secciones` | **2017, 2026** (`titol*_d.pdf` son stubs de 34 B) |
| can | Canarias | 12 | 2015-2026 | `can-tomo3-resumen-programas` | — (serie completa) |
| cat | Cataluña | 9 | 2015-2017, 2019-2020, 2022-2024, 2026 | `cat-programa-totals` | 2018, 2021, 2025 (no registrados) |
| clm | Cast.-La Mancha | 12 | 2015-2026 | `clm-gastosf-csv` (2015-21) / `clm-tomo-I-resumen-secciones` (PDF 2022-26) | — (serie completa) |
| cnt | Cantabria | 12 | 2015-2026 | `cnt-total-programa-suma-servicios` / `cnt-centros-suma-capitulos` (2015-17) | — (serie completa; bug 2025↔2026 corregido) |
| cym | Cast. y León | 8 | 2016-2018, 2021, 2023-2026 | `cym-jcyl-datosabiertos` | 2019/2020/2022 sin fuente; **2016-18 CONSOLIDADO (fix 2026-07-02: filtro transferencias OOAA 400/401/700/701)**; **2025/26 recuperados (fix 2026-07-02: el `.bin` es un ZIP, `_resolve_source` lo abre)**; 2025≡2026 prórroga |
| ext | Extremadura | 12 | 2015-2026 | `ext-doe-resumen-programa` (tabla resumen Ley DOE) | — (serie completa; educación correcta vía resumen, no EIG; 2025/26 prórroga de 2024; salud_mental/discapacidad NULL estructural) |
| gal | Galicia | 12 | 2015-2026 | `gal-progr-consellerias-ruleC` (2015-21) / `gal-csv-abertos-xunta` (2022-26) | — (serie completa; 2015-21 PDF regla C 11 conc, 2022-26 CSV consolidado; sanidad 3.17→5.67B continua) |
| lar | La Rioja | 12 | 2015-2026 | `lar-camelot-funcional-economico` | **fix 2026-07-02**: 2015-16 usan clasificación funcional ANTIGUA → `correspondencias_legacy.yml` (antes 403M sanidad→soberania). Pendiente: ventana 2018 corta bloque social (9 conc) |
| mad | Madrid | 12 | 2015-2026 | `mad-libro-03-centros` | **fix 2026-07-02**: regex `\d{4,5}` quita doble conteo agregado+centro (total 33→21B) + keywords sociales. Residual: infra-captura por proxy-centro (necesita Libro 04); 2020/21≡2019, 2023≡2022 prórroga |
| mur | Murcia | 12 | 2015-2026 | `mur-html` | ORIGEN limpio (auditado 2026-07-02); mur/2026 no cargó en el pipeline (visor HTML falla) |
| nav | Navarra | 12 | 2015-2026 | `nav-breakdowns-functional` | — (serie completa; 2015-17 del mismo visor HTML multi-año, clasificación funcional) |
| pvc | País Vasco | 12 | 2015-2026 | `pvc-gastosc-funcional` (2015-21 ZIP) / `pvc-csv-tidy` (2022-26 CSV) | serie completa; fix 2026-07-01 doble conteo gasto+ingreso; **fix 2026-07-02**: `zfill(4)` (deuda 0111 fuera de direccion) + mapping estatal→vasco (empleo `321*`, igualdad 3221/3223, diversidad 3122, salud_mental 4116) → **8→11 conceptos** (solo 2 NULL estructural: dependencia/discapacidad forales). 2019/2023 = Proyecto |
| val | C. Valenciana | 11 | 2016-2026 | `val-rpc-secciones` | 2026 sec26 = 404 en GVA (hueco ~14 M€, reportado en notes) |

**Total (2026-07-02): 196 CCAA-año · 0 AMARILLO · 0 ERROR · 17/17 CCAA** (165 VERDE_PRAGM +
31 VERDE estricto), consolidado y cargado en `presupuestos_smoke`. Regenera esta foto con:
`python3 tools/smoke_regresion_py.py` (¡hace **backup+restore** del catálogo si filtras CCAA
— corre todas o respalda antes!).

---

## 4 · Trabajo pendiente — priorizado (lo que te toca a ti, Claude Code)

**A. Cerrar lo que ya tiene fuente (rápido, alto valor):**
1. ✅ **clm 2022 y 2023 — HECHO (2026-06-29).** Extraídos de `tomo_I.pdf` con
   `clm-tomo-I-resumen-secciones` (111 / 114 filas, VERDE_PRAGM ~65 %, 13 conceptos).
   Sanidad continua contra 2021/2024. **clm completo 2015-2026.** En catálogo + COMBOS.
2. ✅ **can 2015-2017 — HECHO (2026-06-29).** Raws en `fuentes/raw/can/<año>/TOMO-3-Resumenes.pdf`,
   extraídos con `can-tomo3-resumen-programas` (139-141 filas, VERDE_PRAGM ~65 %, 12 conceptos).
   Serie sanidad continua contra 2018. **Canarias completa 2015-2026.** En catálogo + COMBOS.

**B. Desbloquear candidatos conocidos (requiere encontrar el documento correcto):**
3. **ast 2022** — el `tomo_I.pdf` en disco es la Ley BOPA (texto), no el tomo de programas.
   Busca el tomo de distribución del gasto por programa en transparencia.asturias.es.
4. **ara 2016** — mismo problema (Ley BOPA). Localiza el `ingresos_gastos.pdf` real con la
   tabla programa+total.
5. **bal 2017 y 2026** — los `titol*_d.pdf` en `secciones/` son stubs de 34 B. Re-descarga
   los PDFs reales del frameset (`pressuposts.caib.es`).
6. **gal 2026** — falta el CSV de orzamentos abertos (hoy solo `portal_index.html`).

**C. Ampliar cobertura de años** en las CCAA mono-año (cnt, cym, ext, lar, mad, mur) y
   completar series (cat 2018/2021/2025, pvc/val/nav años antiguos). Patrón: añade la URL a
   `fuentes.yml`, descarga, extrae con el motor existente.

**D. Capa Hacienda (`capa: hacienda`):** procesar los XLSX SGCIEF del Ministerio
   (`fuentes/raw/hacienda/<año>/`, ya hay 2015-2025) para la serie homogénea `total`.

**E. Validación final** (cuaderno §2.6): conciliación contra totales de Hacienda, cobertura,
   test de Benford, y carga definitiva.

---

## 5 · Cómo añadir / arreglar una CCAA (patrón fijo)

```bash
# 1. Mira el formato real del raw
python3 -c "import pdfplumber; pdf=pdfplumber.open('fuentes/raw/<id3>/<año>/<f>.pdf'); \
            print(pdf.pages[120].extract_text()[:1500])"

# 2. Edita 1_extraccion/ccaa/<id3>/extract.py imitando un módulo de formato similar:
#    PDF programa+total .......... ara/extract.py
#    PDF resumen por secciones ... clm/extract.py (rama PDF)
#    PDF suma de capítulos ....... ext/extract.py
#    PDF camelot (tablas) ........ lar/extract.py
#    HTML frameset/visor ......... bal, mur, val
#    CSV tidy / datos abiertos ... pvc/extract.py, gal, clm (rama CSV gastos_articulo)
#    XLS legacy .................. cym/extract.py (necesita xlrd)

# 3. Afina ccaa/<id3>/correspondencias.yml con los códigos reales (valida contra
#    Tablas_Correspondencias_CCAA.docx). transform.py suele ser el patrón estándar.

# 4. Prueba AISLADA (criterio VERDE: motor OK, filas≥30, ≥5 conceptos):
cd 1_extraccion
python3 -m ccaa --ccaa <id3> --anio <año> --input ../fuentes/raw/<id3>/<año>/<f>.ext --output /tmp/t.csv
awk -F, 'NR>1{print $8}' /tmp/t.csv | sort | uniq -c   # ⚠️ usa csv real si la denom lleva comas

# 5. Smoke completo sin romper nada (con DB local):
cd .. && psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true

# 6. EVALUADOR POST-EXTRACCIÓN (obligatorio: el smoke certifica la extracción, NO el número):
python3 tools/auditoria_magnitud.py <id3>   # exit≠0 si hay anomalía de magnitud
```

Variables de entorno para el smoke local (no tocar Supabase de producción):
```bash
export SUPABASE_HOST=localhost SUPABASE_PORT=5432 SUPABASE_DBNAME=presupuestos_smoke \
       SUPABASE_USER=$USER SUPABASE_PASS=fake SUPABASE_SCHEMA=presupuestos
```

### 5.1 · Evaluadores post-extracción (VERDE ≠ número correcto)

**El smoke certifica la EXTRACCIÓN (filas, %concepto), NO la MAGNITUD.** Un extractor
puede estar VERDE 12/12 y devolver el gasto al doble, a la mitad o en ~0 si el documento
cambió de estructura y el patrón fijo no se adaptó — **cada año cada CCAA cambia el
formato**. Lección 2026-07-01: *Aragón* salió VERDE con la sanidad ~2× durante 12 años sin
que nadie lo viera; *Andalucía* recodificó la transferencia al SAS (`41H`→`12S`) y 2024
cayó a ~0, también en VERDE. Por eso, tras extraer, corre **`tools/auditoria_magnitud.py`**:

- **Test CONTINUIDAD** — salto de sanidad/total año-a-año > ±40% ⇒ fallo estructural en un
  año concreto (formato no manejado). Los cambios de método documentados (`SEAMS` en el
  script) se marcan `[seam ok]`, no cuentan como error.
- **Test PLAUSIBILIDAD** — sanidad €/hab fuera de banda (900-2300; España ~1600-1800) ⇒
  error SOSTENIDO en toda la serie (doble conteo o infra-extracción) que la continuidad no
  ve. `ALTO` ⇒ probable doble conteo de transferencia interna (contar UNA vista, no dos —
  ver `1_extraccion/ccaa/LIMITACIONES.md §3`). `BAJO` ⇒ infra-extracción.

```bash
python3 tools/auditoria_magnitud.py            # todas; exit≠0 si hay anomalía (útil como gate)
python3 tools/auditoria_magnitud.py <id3>      # una CCAA
python3 tools/auditoria_magnitud.py --baseline # tabla €/hab de referencia (guárdala)
```

El **baseline** de cada CCAA (sanidad €/hab por año) y sus banderas rojas concretas están
en su ficha `1_extraccion/ccaa/<id3>/limitaciones-<id3>.md §Evaluación post-extracción`. Si
una re-extracción se desvía del baseline, el formato de ese año cambió: revísalo, no lo des
por VERDE. Cola de anomalías **abiertas (2026-07-02)**: **and** rama CSV 2015/16/20/21
(perímetro inflado ~2×, sanidad 2020-22 en 2458-2881 €/hab) + 2022; **ast** doble conteo
sanidad 2015 (413D transferencia + 412B entrega, 2888 €/hab — mismo patrón que ara/cat, aún
sin excluir); **pvc** 2025/26 €/hab ~2300-2400 (alta inversión vasca real, baseline conocido,
no bug). **RESUELTAS el 2026-07-02**: `cym` 2016-18 +30% (filtro transferencias OOAA), `ara` ~2×
(excluida `4131`), y las 12 mis-asignaciones conceptuales de la auditoría
(ver `outputs/auditoria_conceptual_2026-07-02.md`).
El nuevo **TEST 3** de `auditoria_magnitud.py` (continuidad POR CONCEPTO, aviso no bloqueante)
surfacea candidatos de revisión que sanidad/total no ven.

---

## 6 · Gotchas reales (aprendidos a base de golpes)

- **`awk -F,` miente** si la `denominación` lleva comas (desplaza columnas). Para medir
  conceptos/% usa un lector CSV de verdad (`csv.DictReader`), no `awk`.
- **CSV de datos abiertos CLM** (`gastosf`): algunas líneas vienen con la **línea entera
  entre comillas** y comillas internas duplicadas (`""`). Hay un parser tolerante en
  `clm/extract.py` (`_split_csv_line`); reutiliza el patrón si ves lo mismo en otra CCAA.
- **`web_fetch` con PDF binario** devuelve cuerpo vacío (no es un fallo: es binario). Con
  **CSV/HTML sí** devuelve el texto. Si necesitas el binario, descárgalo con
  `urllib`/`requests` (tú estás en el Mac, sin restricción de provenance).
- **Importes en miles vs euros:** ver §2. Sanity-check de magnitud SIEMPRE.
- **`smoke_regresion_py.py` con filtro de CCAA sobrescribe el catálogo** con solo esas
  filas. Respalda `outputs/smoke_regresion_py.csv` antes, o corre sin filtro.
- **`_README.md` de `1_extraccion/ccaa/` está desactualizado** (lista CCAA como "stub").
  La foto buena es §3 de este documento + el catálogo vivo.
- **No** ejecutes operaciones destructivas globales (`rm -rf fuentes/raw/`, `DROP DATABASE`),
  ni `git push --force`, ni cargues en la Supabase de **producción** (`SUPABASE_URL`).

### Gotchas de correspondencias y consolidación (auditoría 2026-07-02)

- **YAML lee `313.60` como el FLOAT `313.6`, no como string** → `str(313.6)`="313.6" nunca casa
  el código emitido "313.60". **Entrecomilla SIEMPRE** los códigos con punto o puramente
  numéricos en `correspondencias.yml`: `'313.60'`, no `313.60`. (Pasó en val.)
- **Los códigos EXACTOS de 3 dígitos (`'421'`,`'712'`) NO casan un código emitido de 4
  dígitos** (`4221`): `asignar_concepto_local` solo hace prefijo con `*` explícito. Muchas
  fichas arrastran decenas de estas entradas MUERTAS (62/103 en ara, 43/109 en cat); el mapeo
  real recae en KEYWORDS, que se rompen en silencio con **abreviaturas** (ara "EDUC SECUNDARIA"),
  **renombres** (clm `324A` 2024) y **género** (cnt "sanitario"≠"sanitaria"). Prefiere prefijos
  reales (`422*`) o exactos de 4 díg. sobre confiar en el keyword.
- **Cada CCAA cambia de clasificación con los años.** Si un año usa un esquema funcional
  distinto (lar 2015-16 esquema ANTIGUO 4.1=Sanidad vs nuevo 3.1=Sanidad), el prefijo de
  código GANA al keyword y mis-asigna en silencio → usa un `correspondencias_legacy.yml`
  condicionado por año en `transform.py` (patrón lar).
- **Degradación silenciosa = patrón sistémico.** gal (dataset homónimo estratéxico vs
  funcional), bal (stubs 404 por zero-padding `titol00`≠`titol0`), cym (`.bin` que es un ZIP),
  cat (first-wins que trunca multi-servei): cuando el documento no cumple lo asumido, el código
  NO falla — degrada. Al escribir un extractor, **cuenta y reporta en `notes`** lo saltado.
- **El maestro R cachea la extracción por SHA-256 del raw (`logs/manifest.jsonl`).** Si cambias
  el CÓDIGO de un extractor pero NO el raw, el maestro **salta el re-parseo** y reconstruye el
  staging solo con lo fresco → puedes acabar con 1 CCAA (o **0 filas y DB VACÍA** si se salta
  todo). Para forzar el re-parseo tras tocar código: **respalda y MUEVE fuera `logs/manifest.jsonl`**
  (no basta `cp`: el fichero es **append-only** y `run_extraccion` lee el snapshot al arrancar) y
  corre el maestro completo. ⚠️ **Carrera (visto 2026-07-24):** si OTRO maestro corre en paralelo,
  repuebla el manifest append-only entre tu reset y tu arranque → tu run vuelve a saltar todo.
  Hazlo ATÓMICO: `rm logs/manifest.jsonl && rm 1_extraccion/staging_gasto.rds && psql TRUNCATE &&
  Rscript 00_maestro.R ...` en UN comando, con `ps` limpio de maestros. Script corregido listo:
  `outputs/cierre_2026-07-23.sh` (el original solo hacía `cp` → cargaba vacío).
- **La DB guarda € CONSTANTES (deflactados); el staging/extractores están en € NOMINALES.**
  Un spot-check de la DB dará números distintos (~×1,3 para años antiguos) — no es un bug.
  Para validar magnitudes usa `auditoria_magnitud.py` sobre el staging (nominal), no la DB.
- **Carga a la DB:** la contraseña se lee de **`SUPABASE_PASS`**, NO de `PGPASSWORD`. El paso
  `carga` crea el esquema+tabla solo (`CREATE ... IF NOT EXISTS`); basta con la DB creada.

---

## 7 · Referencias

- `Cuaderno_Metodologico_Presupuestos_v2026-05-11.docx` — metodología (los 13 conceptos §1.6,
  conciliación §2.6).
- `Tablas_Correspondencias_CCAA.docx` — códigos presupuestarios por CCAA → concepto.
- `1_extraccion/ccaa/_README.md` — contrato técnico del extractor.
- `logs/progreso.md` — bitácora noche a noche (empieza por el final).
- `fuentes.yml` — catálogo de URLs (fuente de verdad para descargas).

> Cuando termines una sesión, **anota en `logs/progreso.md`** qué dejaste VERDE (con nº de
> filas y conceptos), qué intentaste y descartaste (motivo en una línea) y los bloqueantes
> para la siguiente. Mantén la disciplina de la bitácora: es lo que hace el proyecto reanudable.
