# Fase 4 · Carga — Sección Empleo

**Canarias en Datos · ODESOCAN** · Carga del dataset de Empleo a **Supabase**
(schema `canendatos`), para que la pieza D3 (`5_visualizacion`) y la web lean
de la base de datos en producción.

## Esquema (ya creado en Supabase)

Dos tablas, con el patrón **seguro** de Dependencia (RLS activado + política de
solo lectura para `anon`/`authenticated`, grant `SELECT`):

- `canendatos.ced_empleo_global` — CCAA · año · 10 indicadores (valor «Ambos
  géneros» / territorial) + `origen_q`, `origen_a`. PK `(ccaa, periodo)`.
- `canendatos.ced_empleo_gen` — CCAA · año · **género** · indicadores con
  desglose. PK `(ccaa, periodo, genero)`.

El DDL está en `esquema_ced_empleo.sql`. Ya aplicado; verificado que la clave
anon puede leer (HTTP 200), igual que las demás secciones.

## Carga de datos

`cargar_supabase.py` hace una **carga atómica** (§7.7): `TRUNCATE` + `INSERT` de
ambas tablas dentro de **una sola transacción**. Los lectores (la web) nunca ven
una tabla vacía o a medias — siguen viendo los datos anteriores hasta el
`COMMIT`. Se preservan RLS, políticas, grants y PK (no se recrea la tabla).

### Credenciales (por variable de entorno; nunca en el código)

```bash
export SUPABASE_DB_URL="postgresql://postgres:[PASSWORD]@db.kdpsjutsgvghdtzoskkg.supabase.co:5432/postgres"
# o el pooler (modo sesión, puerto 5432):
# export SUPABASE_DB_URL="postgresql://postgres.kdpsjutsgvghdtzoskkg:[PASSWORD]@aws-0-eu-west-1.pooler.supabase.com:5432/postgres"
```

La contraseña es la de la base de datos (secreto del pipeline, `.Renviron` /
gestor de secretos). **No** se usa la anon key aquí: la carga requiere escritura.

### Ejecutar

```bash
cd 4_carga
pip install -r requirements.txt
python cargar_supabase.py            # regenera los CSV desde 3_modelado y carga
python cargar_supabase.py --no-prep  # carga los CSV existentes sin regenerarlos
python cargar_supabase.py --dry-run  # valida y cuenta, sin escribir
```

Tras la carga, la pieza D3 leerá de Supabase automáticamente (el badge pasa de
«CSV» a «Supabase»); no hay que tocar el HTML.

## Ficheros

- `esquema_ced_empleo.sql` — DDL de las dos tablas (ya aplicado).
- `cargar_supabase.py` — carga atómica desde los CSV a Supabase.
- `requirements.txt` — `pandas`, `psycopg2-binary`.

## Nota de seguridad (RLS en el schema `canendatos`)

Las tablas de Empleo usan el patrón seguro (RLS + política). Sin embargo, **16
tablas ya existentes** en `canendatos` (Vivienda, Salud mental y varias fuentes
de Dependencia) tienen **RLS desactivado**: con la anon key cualquiera puede leer
y **modificar** sus filas. Conviene revisarlo. El SQL de remediación (activar RLS
+ añadir política de solo lectura) está en `remediacion_rls_canendatos.sql`;
no se aplica automáticamente para no bloquear accesos sin querer.
