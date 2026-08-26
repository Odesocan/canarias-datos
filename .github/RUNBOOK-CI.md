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

## Dos avisos que vienen de otros repositorios del Observatorio

Salieron al revisar el resto de repos el 2026-08-26 y afectan a la planificación
de este, aunque su origen esté fuera.

### GitHub no dispara los crons de forma fiable

En `transparencia-gobcan` se midió el cumplimiento real de `schedule` durante
cuatro días: **24%**, y **0%** en la franja 07:00–08:00 UTC. Ninguna hora pasaba
del 25%, así que no era cuestión de mover el horario.

La solución que ya está en producción allí: el reloj lo lleva `pg_cron` en
Supabase, que llama al API de GitHub para lanzar el workflow por
`workflow_dispatch` — ese camino sí se ejecuta siempre, porque la
depriorización solo afecta a `schedule`. El cron de GitHub se queda como red de
seguridad. Está documentado en `docs/programacion-fiable.md` de ese repositorio.

Encaja con la nota del 2026-08-05 en `medios-odesocan`, que avisaba de que
ningún cron programado se disparaba desde el 28 de julio.

**Consecuencia para este repo:** si una extracción mensual se salta su día, antes
de buscar un bug hay que comprobar si el cron llegó a dispararse. Y si el
problema se repite, la solución no hay que diseñarla: ya está escrita.

### Una credencial con fecha de caducidad

El token que dispara las extracciones de `transparencia-gobcan` **caduca el
2026-09-28**. Cuando lo haga, parará la automatización sin ningún aviso previo.

Regla general: toda credencial con caducidad va a un calendario el día que se
crea. Una credencial que expira es un fallo con fecha conocida.

## La carga a producción es explícita

Dependencia, Vivienda y Salud mental decidían si escribir en producción así:

```bash
if [ -n "${SUPABASE_HOST}" ] && [ -n "${SUPABASE_USER}" ] && ... ; then
  WITH_DB=true
fi
```

Es decir: **la mera existencia de los secretos activaba la escritura**. Dar de
alta las credenciales para que `rls-audit` pudiera hacer su trabajo habría
encendido, de rebote, la carga automática de tres pipelines que llevaban todo
agosto ejecutándose en seco y que nunca han completado una carga en CI. La
primera habría sido desatendida, un lunes a las 5:00 UTC.

Ahora la decisión es explícita:

| Cómo se lanza | Quién decide |
|---|---|
| A mano (`workflow_dispatch`) | la casilla del formulario, desmarcada por defecto |
| Cron | la variable de repositorio `CED_CRON_ESCRIBE`; si no existe, no escribe |

`CED_CRON_ESCRIBE` es una **variable**, no un secreto (Settings → Secrets and
variables → Actions → pestaña *Variables*): su valor no es sensible y conviene
poder consultarlo.

Si se pide escribir y faltan credenciales, el job falla de inmediato con un
mensaje claro, en vez de ejecutar el pipeline entero y dejar la carga a medias.

### Cómo activarlo cuando se quiera

1. Dar de alta los secretos de Supabase.
2. Lanzar el pipeline a mano **con la casilla marcada** y comprobar el
   resultado en la base de datos.
3. Solo entonces crear `CED_CRON_ESCRIBE = true` para que el cron escriba solo.

Ese orden importa: ninguno de los tres ha completado nunca una carga en CI, y
la primera conviene mirarla.
