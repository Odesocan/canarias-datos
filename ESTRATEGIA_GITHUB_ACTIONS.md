# Canarias en Datos — Estrategia de organización estructural en GitHub

**Para:** ODESOCAN · Observatorio de Derechos Sociales de Canarias
**Ámbito:** monorepo `CANARIAS EN DATOS` — 7 áreas temáticas activas + `canarias-en-datos-web`
(Comunicación y Migraciones quedan fuera de alcance por ahora, ver nota en §1.1)
**Objetivo:** diseñar cómo debe organizarse el flujo completo en GitHub (repo, carpetas, workflows, secretos, despliegue) para que cada área se actualice sola vía GitHub Actions y alimente la web sin intervención manual.
**Fecha del diagnóstico:** 2026-07-24

---

## 0 · Resumen ejecutivo

Ya tienes, sin habértelo propuesto como tal, un **patrón de referencia que funciona**: el
pipeline de *Presupuestos* (`extract.yml` → `validate.yml` → `deploy.yml`) es más maduro que
cualquier framework que yo te propondría desde cero. El problema no es de diseño, es de
**consistencia y ubicación**: cada área ha ido resolviendo su propia automatización de forma
aislada, con tres niveles de madurez distintos conviviendo en el mismo repo, y el workflow
mejor diseñado de todos (el de Presupuestos) **no se está ejecutando en GitHub** porque vive en
`Presupuestos/.github/workflows/` en lugar de `.github/workflows/` en la raíz.

La estrategia que propongo no es "reescribir todo", es:

1. **Adoptar el patrón de 3 workflows de Presupuestos como estándar** para las 7 áreas activas,
   con una versión simplificada para las áreas menos complejas.
2. **Extraer la parte duplicada** (setup de R, setup de Python, instalación de dependencias del
   sistema) a *composite actions* reutilizables, para no mantener una copia del mismo bloque
   por cada área.
3. **Separar limpiamente tres ciclos de vida independientes**: dato (pipeline por área) →
   validación (gate antes de tocar producción) → publicación (Supabase + web), cada uno con su
   propio disparador.
4. **Cerrar el hueco de seguridad ya detectado** (16 tablas en Supabase sin RLS) como parte del
   propio gate de validación, no como tarea aparte.
5. **Desacoplar el despliegue de la web** del de los datos: la web lee directamente de Supabase,
   así que solo necesita re-desplegarse cuando cambia su código, no cuando cambia un dato.

---

## 1 · Diagnóstico: qué hay hoy

### 1.1 · Estructura ya establecida (y que hay que respetar)

> **Nota de alcance:** de las 9 carpetas de área que existen en el repositorio, **Comunicación
> y Migraciones son áreas que todavía no se van a trabajar** — no es que les falte automatizar
> algo, es que no hay pipeline que construir hasta que ODESOCAN lo indique. Por eso todo este
> documento (diagnóstico, matrices, hoja de ruta) se centra en las **7 áreas activas**
> (Dependencia, Educación, Empleo, Presupuestos, Salud mental, Sanidad, Vivienda). Comunicación
> y Migraciones se mencionan solo para dejar constancia de su estado actual, no como trabajo
> pendiente.

Las áreas activas ya comparten una convención de carpetas que nace del "Cuaderno Metodológico"
de cada una — **esto ya es tu estándar interno, no hace falta inventarlo**:

```
<Área>/
├── 00_maestro.R              (o main.py)     orquestador con --steps= / --with-db=
├── Cuaderno_metodologico_<área>.docx
├── 1_extraccion/       descarga fuentes crudas → raw
├── 2_transformacion/   limpieza, normalización, indicadores
├── 3_modelado/         proyecciones (competición de algoritmos: ARIMA/ETS/Theta/Prophet)
├── 4_carga/            carga atómica (TRUNCATE+INSERT en una transacción) a Supabase
└── 5_visualizacion/    prepara los CSV/artefactos que consume la pieza D3 de la web
```

Esta convención se mantiene incluso cuando cambia el lenguaje — y ese es un hallazgo
importante: **el proyecto ya eligió pragmáticamente R o Python según la tarea**, no por área:

| Área | Lenguaje del pipeline | Notas |
|---|---|---|
| Dependencia | R | + carpetas `_analisis`/`_legacy` con series históricas |
| Sanidad | R | el más limpio: `qa/` en cada etapa, `R/imputacion_bootstrap.R` |
| Salud mental | R | pipeline pequeño, ya con `.claude/settings.local.json` local |
| Vivienda | R (orquestador) + Python (scraping) | sub-proyecto ETL propio en `fuentes/scrapings/alquiler_historico_ccaa/` (Playwright/BeautifulSoup, muy completo) |
| Educación | Python | `main.py` orquesta `extract/`, `qa/`, `config/`; logs por ejecución |
| Empleo | Python | el **mejor documentado**: README por fase, banderas `origen`/`proyección` explícitas |
| Presupuestos | R (orquestador) + Python (17 sub-pipelines, uno por CCAA) | el más complejo: `1_extraccion/ccaa/<id3>/{extract.py,transform.py,correspondencias.yml}` con dispatcher por `importlib` |
| *Comunicación* | — | *fuera de alcance por ahora* — solo `.pbix` + CSV crudos, no se va a trabajar todavía |
| *Migraciones* | — | *fuera de alcance por ahora* — solo el esqueleto de carpetas `1_..5_`, vacío, no se va a trabajar todavía |

No recomiendo forzar un único lenguaje: R te da acceso a `ineapir`/`forecast`/`prophet` con
menos fricción, y Python es mejor para scraping/PDF (`pdfplumber`, `camelot`, Playwright). La
estrategia de GitHub Actions tiene que **admitir ambos por diseño**, no intentar unificarlos.

### 1.2 · Estado real de automatización (la parte que hay que arreglar)

| Área | Pipeline listo | Workflow en `.github/workflows/` raíz | Wireado en la web (`topics/*.js`) |
|---|:--:|:--:|:--:|
| Dependencia | ✅ | ✅ `dependencia-pipeline.yml` | ✅ |
| Vivienda | ✅ | ✅ `vivienda-pipeline.yml` | ✅ |
| Salud mental | ✅ | ✅ `salud-mental-pipeline.yml` | ❌ |
| Educación | ✅ | ❌ | ✅ |
| Empleo | ✅ (falta solo `4_carga` a producción) | ❌ | ✅ |
| Presupuestos | ✅ (204/204 celdas VERDE) | ⚠️ **existe pero está mal ubicado** (`Presupuestos/.github/workflows/`, GitHub no lo ve) | ✅ |
| Sanidad | ✅ | ❌ | ❌ |
| *Comunicación* | *— (fuera de alcance, no se trabaja aún)* | — | — |
| *Migraciones* | *— (fuera de alcance, no se trabaja aún)* | — | — |

Es decir: de las **7 áreas activas**, solo **2 están realmente automatizadas de punta a punta**
(Dependencia, Vivienda). Presupuestos — el pipeline técnicamente más sofisticado del proyecto —
está a un `git mv` de estarlo también.

### 1.3 · Problemas estructurales concretos

1. **Workflows de Presupuestos inertes.** GitHub Actions solo lee `.github/workflows/` en la
   **raíz del repo**. La carpeta `Presupuestos/.github/workflows/` con `extract.yml`,
   `validate.yml`, `deploy.yml` no se ejecuta nunca. Es el hallazgo más urgente: hay un patrón
   de CI/CD ya diseñado (PR automático con el manifiesto, validación con Postgres efímero,
   purga de CDN) que simplemente nunca se ha activado.

2. **Duplicación de boilerplate.** Los 4 workflows que sí existen repiten, casi carácter a
   carácter, el mismo bloque: `actions/checkout` → `setup-r` → `apt-get install
   libcurl4-openssl-dev libssl-dev libxml2-dev libpq-dev` → lista de paquetes R. Cada área que
   se añada va a copiar y pegar este bloque una vez más. Es mantenimiento que crece
   linealmente con el número de áreas.

3. **Dos patrones de CI compitiendo.** El patrón "flat" (`dependencia-pipeline.yml`: un solo
   job que extrae, transforma, modela y **carga a producción** en la misma ejecución
   programada, sin validación previa) convive con el patrón de 3 fases de Presupuestos
   (extract → validate-con-Postgres-efímero → deploy-con-`environment: production`). El
   patrón flat no tiene ningún gate antes de escribir en la Supabase de producción — si un
   extractor rompe, el error se detecta en producción, no antes.

4. **Brecha de seguridad ya diagnosticada por vosotros mismos.** El README de
   `Empleo/4_carga` documenta que **16 tablas** de `canendatos` (Vivienda, Salud mental, varias
   de Dependencia) tienen **RLS desactivado**: con la anon key pública, cualquiera puede no solo
   leer sino **escribir** sobre esas tablas. Ya existe el SQL de remediación
   (`remediacion_rls_canendatos.sql`) pero no se aplica porque no hay ningún proceso
   automático que lo fuerce.

5. **Desfase entre carpetas de área y slugs de la web.** Las carpetas usan nombres en español
   con mayúsculas y espacios (`Salud mental`, `Educación`), mientras que
   `canarias-en-datos-web/topics/` usa slugs kebab-case (`salud-mental`, `educacion`). No hay
   que renombrar las carpetas (rompería scripts y rutas locales ya probadas), pero conviene
   fijar la tabla de equivalencia como parte del estándar, porque los nombres de los workflows
   y de los artefactos de CI deberían usar el slug, no el nombre de carpeta con espacios
   (GitHub Actions maneja mal los espacios en `working-directory`/`paths`).

6. **Datos huérfanos.** `Comunicación/Salud mental/` contiene una copia de los CSV de Salud
   mental dentro de la carpeta de Comunicación — probablemente un extracto de Power BI mal
   ubicado. No afecta al diseño de CI, pero conviene limpiarlo antes de dar por buena la
   estructura de carpetas.

---

## 2 · Principios de la estrategia recomendada

**Monorepo, no polyrepo.** Ya lo es, y es la decisión correcta a este tamaño de equipo: todas
las áreas comparten Supabase, comparten la web, y comparten utilidades (`ccaa_dictionary.R`,
`pipeline_utils.R` están casi duplicados letra a letra en Dependencia/Sanidad/Salud
mental/Vivienda — otro candidato a centralizar en `_shared/R/`). Separar en repos por área solo
multiplicaría la gestión de secretos y la fricción de CI sin ganar nada a cambio.

**CI por área, no CI monolítico.** Dentro del monorepo, cada área tiene su propio workflow (o
trío de workflows) con `paths:` filtrado a su propia carpeta, exactamente como ya hace
`validate.yml` de Presupuestos. Un cambio en `Vivienda/` no debe disparar ni bloquear el
pipeline de `Sanidad/`.

**Tres fases con responsabilidades distintas, no tres tamaños de esfuerzo distintos.** El
patrón de Presupuestos (extraer → validar → desplegar) no es "sobre-ingeniería para un caso
complejo": es la separación mínima correcta entre "¿hay datos nuevos?", "¿son correctos?" y
"¿los publico?". Lo que sí debe variar por complejidad es **cuánto vive dentro de cada fase**,
no si las fases existen.

**La web es un consumidor, no un paso del pipeline.** `canarias-en-datos-web` lee Supabase en
tiempo real (`core/config.js` + `topics/<slug>.js`); no necesita rebuild cuando cambia un dato.
Su despliegue es un cuarto flujo, totalmente independiente, disparado solo por cambios en
`canarias-en-datos-web/**`.

---

## 3 · Estructura de carpetas objetivo

No se mueve ninguna carpeta de área. Los cambios son solo en `.github/`:

```
CANARIAS EN DATOS/
├── .github/
│   ├── actions/                          # NUEVO — composite actions reutilizables
│   │   ├── setup-r-pipeline/action.yml   # checkout ya lo hace el workflow; esto = setup-r + apt deps + paquetes core
│   │   └── setup-python-pipeline/action.yml
│   ├── workflows/
│   │   ├── _reusable-pipeline.yml        # NUEVO — workflow_call parametrizado (area, lenguaje, steps, cron)
│   │   ├── dependencia-extract.yml       # llama al reusable con inputs de Dependencia
│   │   ├── dependencia-validate.yml
│   │   ├── dependencia-deploy.yml
│   │   ├── vivienda-extract.yml
│   │   ├── vivienda-validate.yml
│   │   ├── vivienda-deploy.yml
│   │   ├── salud-mental-extract.yml
│   │   ├── salud-mental-validate.yml
│   │   ├── salud-mental-deploy.yml
│   │   ├── educacion-extract.yml         # NUEVO
│   │   ├── educacion-validate.yml        # NUEVO
│   │   ├── educacion-deploy.yml          # NUEVO
│   │   ├── empleo-extract.yml            # NUEVO
│   │   ├── empleo-validate.yml           # NUEVO
│   │   ├── empleo-deploy.yml             # NUEVO
│   │   ├── sanidad-extract.yml           # NUEVO
│   │   ├── sanidad-validate.yml          # NUEVO
│   │   ├── sanidad-deploy.yml            # NUEVO
│   │   ├── presupuestos-extract.yml      # MOVIDO desde Presupuestos/.github/
│   │   ├── presupuestos-validate.yml     # MOVIDO
│   │   ├── presupuestos-deploy.yml       # MOVIDO
│   │   └── web-deploy.yml                # NUEVO — GitHub Pages
│   └── CODEOWNERS                        # opcional, útil si se suma alguien al equipo
├── Dependencia/  Educación/  Empleo/  Presupuestos/  Sanidad/  ...   # sin cambios
└── canarias-en-datos-web/                                            # sin cambios
```

Con las 7 áreas activas × 3 workflows serían 21 archivos — parece mucho, pero cada uno pasa de
~60 líneas (como los actuales) a ~15-20, porque el bloque de *setup* se delega a la composite
action. Para las áreas más simples (Salud mental, Educación) se puede colapsar
extract+validate+deploy en un único archivo `<area>-pipeline.yml` con tres `jobs:` encadenados
por `needs:` — ver §4.2. (Comunicación y Migraciones no entran en esta cuenta: no se planifica
ningún workflow para ellas mientras sigan fuera de alcance.)

---

## 4 · El patrón de workflow estándar

### 4.1 · Composite action reutilizable (elimina la duplicación de R/Python setup)

```yaml
# .github/actions/setup-r-pipeline/action.yml
name: "Setup R pipeline"
description: "R + deps de sistema + paquetes core comunes a todas las áreas"
inputs:
  extra-packages:
    description: "Paquetes R adicionales, espacio-separados (p. ej. forecast prophet ranger)"
    required: false
    default: ""
runs:
  using: "composite"
  steps:
    - uses: r-lib/actions/setup-r@v2
      with: { use-public-rspm: true }
    - name: System deps
      shell: bash
      run: |
        sudo apt-get update
        sudo apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev libpq-dev
    - name: R packages (núcleo + extras del área)
      shell: bash
      run: |
        Rscript -e 'install.packages(c(
          "DBI","RPostgres","dplyr","glue","purrr","readr","readxl","stringr",
          "tibble","tidyr","lubridate","writexl","${{ inputs.extra-packages }}"
        ), repos = "https://cloud.r-project.org")'
```

Cada workflow de área pasa solo lo que le sobra sobre el núcleo (`extra-packages:
"forecast prophet ranger xgboost"` para Dependencia; `"ineapir"` para Salud mental/Vivienda).
Lo mismo aplica a un `setup-python-pipeline` equivalente para Educación/Empleo/Presupuestos
(pandas, pyarrow, pdfplumber, camelot cuando aplique).

### 4.2 · Las tres fases, con el criterio de cuándo fundirlas

**`<area>-extract.yml`** — descarga y transforma, sin tocar producción.
- Disparador: `schedule` (cadencia = publicación de la fuente, ver tabla §5) + `workflow_dispatch`.
- `Rscript 00_maestro.R --steps=extraccion,transformacion --with-db=false`.
- Sube artefactos (`upload-artifact`) para poder inspeccionar sin re-ejecutar.
- Patrón Presupuestos (recomendado también para áreas con fuentes inestables — PDFs, scraping):
  abrir un PR con el manifiesto/salida en lugar de commitear directo a `main`. Da un punto de
  revisión humana barato antes de que el dato entre al repo.

**`<area>-validate.yml`** — el gate. Esto es lo que **falta hoy en Dependencia, Salud mental y
Vivienda**, y es la pieza de mayor valor de toda esta propuesta.
- Disparador: `pull_request` y `push a main` con `paths: ["<Área>/**"]`.
- Levanta un servicio `postgres:16` efímero (ya resuelto en `presupuestos-validate.yml`),
  aplica el schema, corre un smoke test.
- **Añadir aquí el chequeo de RLS** que hoy no existe en ningún workflow:
  ```yaml
  - name: RLS gate — ninguna tabla ced_* sin política de solo lectura para anon
    run: |
      psql "$POSTGRES_URL" -t -c "
        SELECT tablename FROM pg_tables
        WHERE schemaname='canendatos' AND tablename LIKE 'ced_%'
          AND NOT rowsecurity;" | grep -q . && \
        { echo '::error::Tablas sin RLS detectadas'; exit 1; } || echo 'OK: RLS activo en todas'
  ```
  (Sobre la producción real, este mismo chequeo se puede correr como workflow programado
  aparte usando `mcp__Supabase__get_advisors` / la vista `pg_policies`, para las 16 tablas que
  ya están desplegadas sin este gate.)

**`<area>-deploy.yml`** — el único que escribe en Supabase de producción.
- Disparador: `push a main` con `paths` sobre `4_carga/**` (o `db/**`), + `workflow_dispatch`.
- **`environment: production`** en el job (ya lo hace Presupuestos; hay que añadirlo también a
  Dependencia/Salud mental/Vivienda). Esto permite exigir un *required reviewer* en GitHub antes
  de que cualquier ejecución programada escriba en producción sin supervisión — hoy esas tres
  áreas escriben en producción directamente desde un cron sin ningún control.
- `--with-db=true`.

**Cuándo fundir las tres en un solo archivo:** para áreas de una sola fuente y un solo script
(Salud mental es el caso hoy), un único `<area>-pipeline.yml` con tres `jobs` encadenados (`validate` → `needs: extract`, `deploy` → `needs: validate`) da la
misma seguridad con menos archivos. Reserva los tres archivos separados para áreas donde
`extract` es lento/costoso y no quieres re-ejecutarlo solo porque cambió el schema de validación
(Presupuestos: 17 sub-pipelines, timeout de 60 min ya declarado).

### 4.3 · Ejemplo de área nueva usando el reusable (Educación, hoy sin workflow)

```yaml
# .github/workflows/educacion-extract.yml
name: educacion-extract
on:
  schedule:
    - cron: "0 5 15 * *"     # ajustar a la cadencia real de INE/Educabase
  workflow_dispatch:
jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r Educación/1_extraccion/requirements.txt
      - working-directory: Educación/1_extraccion
        run: python main.py
      - uses: actions/upload-artifact@v4
        with:
          name: educacion-raw
          path: Educación/1_extraccion/data/raw/*.csv
```

(Nota: `working-directory` con espacio en `Educación` funciona bien entre comillas de YAML;
el problema de nombres con espacio aparece sobre todo en `paths:` de disparadores y en rutas
pasadas a scripts de shell sin comillas — hay que ser explícito con comillas en todos los
`run:` que toquen `Educación/`, `Salud mental/` o `Empleo/`.)

---

## 5 · Matriz de disparadores recomendada

| Área | Cadencia de `extract` | Justificación | Aprobación manual en `deploy` |
|---|---|---|---|
| Presupuestos | día 28, mensual | SGCIEF publica con retraso variable | Ya la tiene (`environment: production`) |
| Dependencia | día 5, mensual | IMSERSO publica SAAD 6-8 semanas tras cierre de mes | **Añadir** |
| Vivienda | día 5, mensual | ventana de publicación mensual de Idealista | **Añadir** |
| Salud mental | lunes, semanal | fuente INE de baja frecuencia, margen amplio | **Añadir** |
| Educación | mensual (a fijar) | Educabase/Eurostat, cadencia variable por indicador | Nueva — incluir desde el inicio |
| Empleo | trimestral + mensual (mixto) | EPA/ETCL trimestral, EAES/alquiler anual — replicar cadencia mixta ya modelada en el propio dataset (`origen_q`/`origen_a`) | Nueva — incluir desde el inicio |
| Sanidad | a fijar (revisar Cuaderno metodológico) | pipeline ya construido, solo falta decidir cadencia | Nueva — incluir desde el inicio |

*Comunicación y Migraciones no aparecen en esta matriz a propósito: son áreas que aún no se van
a trabajar, así que no hay cadencia ni disparador que definir por el momento.*

Todas las áreas activas mantienen `workflow_dispatch` para reruns manuales — ya es la práctica
actual y es correcta.

---

## 6 · Despliegue de la web (flujo independiente)

```yaml
# .github/workflows/web-deploy.yml
name: web-deploy
on:
  push:
    branches: [main]
    paths: ["canarias-en-datos-web/**"]
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions: { pages: write, id-token: write }
    environment: { name: github-pages }
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with: { path: canarias-en-datos-web }
      - uses: actions/deploy-pages@v4
```

Esto cierra la **Fase 6** que el propio `README.md` de `canarias-en-datos-web` ya tiene
pendiente. No depende de ningún pipeline de datos: cuando se publique un dato nuevo en
Supabase, la web lo muestra en la siguiente carga de página sin necesidad de redeploy — la
única razón para re-desplegar la web es un cambio en `core/` o `topics/`.

Antes de activar Fase 6, quedan pendientes (según el propio README): `core/engine.js` (Fase 2,
"en construcción"), botonera dinámica con estado en URL (Fase 3, aunque el `index.html` que ya
existe apunta a que esto está más avanzado de lo que indica el README — conviene actualizar ese
README con el estado real antes de tocar el deploy).

---

## 7 · Hoja de ruta de implementación (orden recomendado)

1. **Reubicar los workflows de Presupuestos** de `Presupuestos/.github/workflows/` a
   `.github/workflows/`. Es un `git mv`, cero riesgo, y activa de golpe el pipeline más maduro
   del proyecto. *(máxima prioridad, mínimo esfuerzo)*
2. **Construir las composite actions** (`setup-r-pipeline`, `setup-python-pipeline`) y
   migrar Dependencia/Salud mental/Vivienda a usarlas — reduce cada workflow existente a una
   fracción de su tamaño sin cambiar su comportamiento.
3. **Añadir `<area>-validate.yml` con el gate de RLS** a Dependencia, Salud mental y Vivienda
   (hoy escriben a producción sin ningún control previo) y aplicar
   `remediacion_rls_canendatos.sql` a las 16 tablas ya expuestas. *(prioridad de seguridad)*
4. **Dar workflow a Educación y Empleo** — sus pipelines ya están completos y ya están
   "ready" en la web; es la automatización con mayor retorno inmediato. Empleo necesita
   además terminar su `4_carga` a producción (marcado como pendiente en su propio README).
5. **Dar workflow a Sanidad y wirearla en la web** (`topics/sanidad.js`) — el pipeline ya
   existe y es, de hecho, el mejor estructurado en R (`qa/` en cada etapa). Esto además
   coincide con la prioridad institucional: en `Mapa de proceso.docx`, salud/sanidad es una de
   las tres áreas propuestas para informe sectorial junto con dependencia y vivienda.
6. **Wirear Salud mental en la web** (`topics/salud-mental.js`) — su pipeline ya está
   automatizado, solo falta el archivo de configuración de la temática.
7. **Activar `web-deploy.yml`** una vez `core/engine.js` esté estable (Fase 2 de su propio plan).
8. **Limpieza de higiene**: mover/eliminar `Comunicación/Salud mental/` (datos huérfanos),
   centralizar `ccaa_dictionary.R`/`pipeline_utils.R` duplicados en un `_shared/R/` común,
   y decidir si `master/` (los dos HTML de storytelling consolidado) sigue vigente o es
   candidato a archivar ahora que existe `canarias-en-datos-web`.

**Fuera de esta hoja de ruta, a propósito:** Comunicación y Migraciones no tienen ningún paso
asignado. Son áreas que ODESOCAN todavía no va a trabajar, así que no se planifica pipeline,
workflow ni wireado a la web para ellas hasta que se indique lo contrario. Cuando llegue ese
momento, el checklist de §8 es el punto de partida.

---

## 8 · Checklist para añadir una nueva área al estándar

1. Confirmar que existe `Cuaderno_metodologico_<área>.docx` con los indicadores objetivo.
2. Crear `1_extraccion → 5_visualizacion` siguiendo el contrato ya usado (ver `extraer.py` de
   Empleo o `extraccion.R` de Sanidad como plantilla, según lenguaje).
3. Definir el slug kebab-case (para workflow, artefactos y `topics/<slug>.js>`).
4. Añadir `<slug>-extract.yml` / `-validate.yml` / `-deploy.yml` (o el `-pipeline.yml`
   fusionado si es una fuente simple) usando las composite actions.
5. Aplicar el esquema seguro en Supabase: `ced_<área>_global` (+ `_gen` si aplica), con RLS +
   política `SELECT` para `anon` desde el primer commit — no después.
6. Añadir `environment: production` al job de `deploy`.
7. Crear `topics/<slug>.js` siguiendo `_schema.md` y marcar `ready: true` en el `MANIFEST` de
   `index.html` solo cuando `4_carga` ya esté escribiendo en producción.

---

*Documento de estrategia · elaborado tras inspección directa del repositorio local
`CANARIAS EN DATOS` (carpetas, workflows existentes, READMEs por fase, `AGENTS.md`/`CLAUDE.md`
de Presupuestos y `Mapa de proceso.docx`). No se ha modificado ningún archivo del proyecto.*
