#!/usr/bin/env bash
# ============================================================
# load_prod_ced.sh — Carga presupuestos.ced_presupuestos en la Supabase
# de PRODUCCIÓN (bd_odesocan) desde el dump byte-exacto generado el 2026-07-24.
#
# La contraseña NUNCA se pasa por chat ni queda en el repo: se lee de la
# variable de entorno SUPABASE_DB_URL (la cadena de conexión de tu proyecto
# Supabase → Settings → Database → Connection string).
#
# USO:
#   export SUPABASE_DB_URL='postgresql://postgres.kdpsjutsgvghdtzoskkg:TU_PASSWORD@aws-0-eu-west-1.pooler.supabase.com:6543/postgres'
#   bash 4_carga/load_prod_ced.sh
#
# Es idempotente (crea la tabla si falta, la vacía y recarga las 391 filas)
# y transaccional (BEGIN/COMMIT): si algo falla, no deja la tabla a medias.
# NO toca ninguna otra tabla del schema presupuestos.
# ============================================================
set -euo pipefail
cd "$(dirname "$0")/.."

SQL="4_carga/prod_load_ced_presupuestos.sql"
[ -f "$SQL" ] || { echo "ERROR: no encuentro $SQL" >&2; exit 1; }
: "${SUPABASE_DB_URL:?Define SUPABASE_DB_URL con tu cadena de conexión de Supabase (Settings > Database)}"

# psql del homebrew 17 (compatible con el servidor 17 de Supabase)
PSQL="$(command -v psql || echo /opt/homebrew/opt/postgresql@17/bin/psql)"

echo "→ Cargando $SQL en producción (transaccional, ON_ERROR_STOP)…"
"$PSQL" "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f "$SQL"
echo "✓ Carga completada. Revisa la tabla de verificación de arriba (debe dar autonomica=204, hacienda=187)."
