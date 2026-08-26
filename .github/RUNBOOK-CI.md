# Runbook de CI — por qué fallaba a diario y cómo evitarlo

Diagnóstico del 2026-08-26 sobre los fallos acumulados desde el 2026-08-03.

## Resumen

Ningún fallo era un bug de código de los pipelines. **Todos** venían de cuatro
causas sistémicas de configuración. La más cara no es técnica: los arreglos
existían desde el 3 de agosto, escritos y verificados, esperando en PRs sin
mergear mientras el cron repetía el mismo fallo cada semana.

## Las cuatro causas raíz

### 1. Los arreglos vivían en ramas, no en `main`

El cron ejecuta `main`. Un arreglo en una rama no arregla nada. Entre el 3 y el
24 de agosto se abrieron tres PRs correctos (#8, #13, #15) que nunca se
mergearon, así que salud-mental volvió a fallar el 10, el 17 y el 24 de agosto
con el error exacto que #8 ya resolvía.

Agravante: las ramas de #8 y #13 envejecieron y quedaron por detrás de `main`.
Mergearlas tal cual habría revertido trabajo web posterior (`capa-movil.html`,
871 líneas). Un arreglo sin mergear no solo no sirve: se pudre.

**Regla:** un arreglo de CI se mergea el mismo día o se cierra. Si no se mergea
hoy, mañana ya no es el mismo arreglo.

### 2. `repos` fijado a CRAN anulaba los binarios de RSPM

`setup-r-pipeline` pasaba `repos = "https://cloud.r-project.org"` explícitamente,
lo que anulaba el Posit Package Manager que `setup-r` acababa de configurar.
Resultado: todo el árbol de paquetes se compilaba desde fuente. `fs` no compila
sin `libuv`, y su fallo arrastraba a `sass` → `bslib` → `rmarkdown` →
`htmlwidgets` → `dygraphs` → `prophet`.

Una línea, cuatro áreas afectadas: Dependencia, Salud mental, Vivienda y Sanidad.

**Regla:** no fijar `repos` a mano cuando `use-public-rspm: true` ya lo configura.
Ver el comentario en `.github/actions/setup-r-pipeline/action.yml`.

### 3. Secretos que el código exige y el repositorio no tiene

El fallo más repetido de todos, y el que más minutos de runner ha quemado.
Un job instala R durante 16 minutos, o scrapea durante media hora, y muere al
final porque una variable venía vacía. El error real queda enterrado bajo miles
de líneas de log de compilación.

**Regla:** todo job que dependa de secretos empieza por
`./.github/actions/check-secrets`, antes de cualquier `setup-*`. Falla en
segundos y enumera de golpe todos los que faltan.

```yaml
- uses: actions/checkout@v4
- uses: ./.github/actions/check-secrets
  with:
    required: "SNS_API_TOKEN SUPABASE_HOST"
    contexto: ".Renviron del área"
```

### 4. Contrato roto entre el código y sus dependencias declaradas

`extraer.py` importaba `requests` vía `extraer_supabase`, pero el
`requirements.txt` del área solo declaraba `pandas`/`pyarrow` — escrito cuando
la descarga sí usaba solo `urllib`. El código evolucionó, el manifiesto no.

**Regla:** al añadir un `import` de terceros, se declara en el `requirements.txt`
que instala el workflow de esa área. Lo mismo para R: lo que
`require_packages()` declare tiene que estar en `extra-packages`.

## Acciones humanas pendientes

Estas **no** se pueden resolver desde el código. Hasta que estén hechas, los
jobs afectados seguirán fallando — ahora en segundos y con un mensaje claro, en
vez de a los 16 minutos.

En **Settings → Secrets and variables → Actions**:

| Secreto | Lo necesitan | De dónde sale el valor |
|---|---|---|
| `SNS_API_TOKEN` | salud-mental, sanidad-{extract,validate,deploy} | `.Renviron` local de Sanidad / Salud mental |
| `SUPABASE_HOST` `SUPABASE_PORT` `SUPABASE_DBNAME` `SUPABASE_USER` `SUPABASE_PASS` `SUPABASE_SCHEMA` | rls-audit y todos los `*-deploy` | Supabase → Project Settings → Database |

`rls-audit` falla cada lunes solo por esto.

## Cadencia de los crons

| Workflow | Cron |
|---|---|
| rls-audit | lunes 06:00 UTC |
| salud-mental | lunes 05:00 UTC |
| dependencia · vivienda | día 5, 05:00 UTC |
| educacion-extract | día 10, 05:00 UTC |
| sanidad-extract | día 15, 05:00 UTC |
| empleo-extract | día 20, 05:00 UTC |
| presupuestos-extract | día 28, 04:00 UTC |

Las extracciones están escalonadas a propósito: ninguna comparte día.

## Antes de dar por bueno un workflow nuevo

1. Lanzarlo a mano con `workflow_dispatch` **una vez**. Un workflow que nunca se
   ha ejecutado no está probado: los tres fallos de agosto llevaban meses
   latentes porque hasta el cron del día 3 ningún workflow había corrido en
   GitHub.
2. Comprobar que declara el gate de secretos si usa alguno.
3. Comprobar que lo que el código importa está en el manifiesto que el workflow
   instala.
