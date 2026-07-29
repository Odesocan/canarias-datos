# AGENTS.md — Guía del proyecto *Presupuestos · ODESOCAN / Canarias en Datos*

> Documento de orientación para **Codex**. Resume qué es el proyecto, en qué
> fase está, cómo está construido y qué trabajo queda — para que puedas continuar la
> extracción de presupuestos autonómicos de forma autónoma y sin romper lo que ya funciona.
> **Última actualización: 2026-06-29.**

---

## 0 · TL;DR (léelo y actúa)

- **Qué construimos:** el epígrafe de *Presupuestos* de [Canarias en Datos](https://odesocan.org),
  una tabla canónica (`presupuestos.ced_presupuestos`) con el gasto de las **17 CCAA**
  desagregado en **13 conceptos de política social** por **ejercicio** y por **capa**
  (autonómica = dato oficial de cada CCAA; hacienda = serie homogénea del Ministerio).
- **Fase actual:** extracción casi completa. **138 ejercicios-año en VERDE, 17/17 CCAA,
  1 ERROR (ara/2016).** Quedan huecos de años y la capa Hacienda + validación final.
- **Tu rol (Codex en el Mac):** tienes **R, `psql`, red estable y sin límite de
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

| id3 | CCAA | VERDE | Años extraídos | Motor | Pendiente |
|-----|------|:---:|---|---|---|
| and | Andalucía | 12 | 2015-2026 | `and-resumen-cap-prog` / `and-ckan-csv` | — |
| ara | Aragón | 11 | 2015, 2017-2026 | `ara-pdf-program-total` | **2016 ❌** (raw es Ley BOPA, no programa+total) |
| ast | Asturias | 11 | 2015-2021, 2023-2026 | `ast-distribucion-gasto` | **2022** (falta tomo de programas) |
| bal | Baleares | 10 | 2015-2016, 2018-2025 | `bal-frameset-secciones` | **2017, 2026** (`titol*_d.pdf` son stubs de 34 B) |
| can | Canarias | 12 | 2015-2026 | `can-tomo3-resumen-programas` | — (serie completa) |
| cat | Cataluña | 9 | 2015-2017, 2019-2020, 2022-2024, 2026 | `cat-programa-totals` | 2018, 2021, 2025 (no registrados) |
| clm | Cast.-La Mancha | 12 | 2015-2026 | `clm-gastosf-csv` (2015-21) / `clm-tomo-I-resumen-secciones` (PDF 2022-26) | — (serie completa) |
| cnt | Cantabria | 12 | 2015-2026 | `cnt-total-programa-suma-servicios` / `cnt-centros-suma-capitulos` (2015-17) | — (serie completa; bug 2025↔2026 corregido) |
| cym | Cast. y León | 8 | 2016-2018, 2021, 2023-2026 | `cym-jcyl-datosabiertos` | 2019/2020/2022 sin fuente; 2016-18 sin consolidar (~+30%); 2025≡2026 prórroga |
| ext | Extremadura | 2 | 2025-2026 | `ext-tomo-eig-suma-capitulos` | ampliar años |
| gal | Galicia | 12 | 2015-2026 | `gal-progr-consellerias-ruleC` (2015-21) / `gal-csv-abertos-xunta` (2022-26) | — (serie completa; 2015-21 PDF regla C 11 conc, 2022-26 CSV consolidado; sanidad 3.17→5.67B continua) |
| lar | La Rioja | 1 | 2025 | `lar-camelot-funcional-economico` | ampliar años |
| mad | Madrid | 12 | 2015-2026 | `mad-libro-03-centros` | ⚠️ totales inflados ~2x (proxy centro, no Libro 04); 2020/21≡2019, 2023≡2022 prórroga |
| mur | Murcia | 1 | 2025 | `mur-html` | ampliar años |
| nav | Navarra | 9 | 2018-2026 | `nav-breakdowns-functional` | ampliar años antiguos |
| pvc | País Vasco | 4 | 2022, 2024-2026 | `pvc-csv-tidy` | 2023 y anteriores |
| val | C. Valenciana | 11 | 2016-2026 | `val-rpc-secciones` | 2026 sec26 = 404 en GVA (hueco ~14 M€, reportado en notes) |

**Total: 138 VERDE + 1 ERROR · 17/17 CCAA.** (📥 = fuente ya en `fuentes.yml`/raw, falta
extraer.) Regenera esta foto con: `python3 tools/smoke_regresion_py.py` (¡hace **backup+
restore** del catálogo si filtras CCAA — corre todas o respalda antes!).

---

## 4 · Trabajo pendiente — priorizado (lo que te toca a ti, Codex)

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
```

Variables de entorno para el smoke local (no tocar Supabase de producción):
```bash
export SUPABASE_HOST=localhost SUPABASE_PORT=5432 SUPABASE_DBNAME=presupuestos_smoke \
       SUPABASE_USER=$USER SUPABASE_PASS=fake SUPABASE_SCHEMA=presupuestos
```

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
