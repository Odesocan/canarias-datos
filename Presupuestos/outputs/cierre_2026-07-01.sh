#!/usr/bin/env bash
# Cierre 2026-07-01 — certificar VERDE DB tras completar pvc (País Vasco) 2015-2026
# y corregir el doble conteo gasto+ingreso del motor tidy.
#
# USO:
#   export SUPABASE_PASS='tu_contraseña_de_postgres'   # obligatorio
#   bash outputs/cierre_2026-07-01.sh
#
# (Opcional) si tu usuario/host/puerto difieren, expórtalos antes:
#   export SUPABASE_USER=otro  SUPABASE_HOST=localhost  SUPABASE_PORT=5432
set -uo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

# --- BLINDAJE ANTI-PRODUCCIÓN -------------------------------------------------
# Esta rutina carga SOLO en la DB LOCAL de smoke. carga.R usa la REST API de
# Supabase (PRODUCCIÓN) cuando SUPABASE_URL + SUPABASE_SERVICE_KEY están
# definidas; las desactivamos para forzar PG directo a localhost.
unset SUPABASE_URL SUPABASE_SERVICE_KEY SUPABASE_KEY SUPABASE_ANON_KEY

# --- Credenciales (con defaults; la contraseña la pones tú) ---------------
export SUPABASE_HOST="${SUPABASE_HOST:-localhost}"
export SUPABASE_PORT="${SUPABASE_PORT:-5432}"
export SUPABASE_DBNAME="${SUPABASE_DBNAME:-presupuestos_smoke}"
export SUPABASE_USER="${SUPABASE_USER:-$USER}"
export SUPABASE_SCHEMA="${SUPABASE_SCHEMA:-presupuestos}"

if [ -z "${SUPABASE_PASS:-}" ]; then
  echo "ERROR: exporta primero tu contraseña:  export SUPABASE_PASS='...'" >&2
  exit 1
fi
export PGPASSWORD="$SUPABASE_PASS"          # para los psql de abajo
PSQL=(psql -h "$SUPABASE_HOST" -p "$SUPABASE_PORT" -U "$SUPABASE_USER")

echo "== 0. Crear la DB $SUPABASE_DBNAME si no existe =="
if "${PSQL[@]}" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$SUPABASE_DBNAME'" | grep -q 1; then
  echo "   ya existe (ok)"
else
  createdb -h "$SUPABASE_HOST" -p "$SUPABASE_PORT" -U "$SUPABASE_USER" "$SUPABASE_DBNAME" \
    && echo "   creada" || { echo "   ERROR creando la DB"; exit 1; }
fi

echo "== 1. TRUNCATE tabla canónica (si ya existe; si no, la crea la carga) =="
"${PSQL[@]}" -d "$SUPABASE_DBNAME" -c "TRUNCATE presupuestos.ced_presupuestos;" 2>/dev/null \
  && echo "   truncada" || echo "   (tabla aún no existe — la crea carga.R)"

echo "== 1b. Forzar re-parseo completo (el maestro SALTA fuentes con hash en manifest;"
echo "        como el paso 1 hace TRUNCATE, hay que reconstruir TODO el staging) =="
if [ -f logs/manifest.jsonl ]; then
  cp logs/manifest.jsonl "logs/manifest.jsonl.bak.cierre" && rm -f logs/manifest.jsonl \
    && echo "   manifest borrado (respaldo en logs/manifest.jsonl.bak.cierre)"
else
  echo "   sin manifest (re-parseo completo asegurado)"
fi

echo "== 2. Maestro R (extracción → transformación → modelado → carga) =="
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

echo "== 3. Cobertura global por capa =="
"${PSQL[@]}" -d "$SUPABASE_DBNAME" -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"

echo "== 4. VERIFICACIÓN pvc: total corregido ~11-17 B€ (NO ~38); sanidad 3,4→5,3 B€ =="
"${PSQL[@]}" -d "$SUPABASE_DBNAME" -c "
  SELECT periodo,
         ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2)   AS sanidad_b,
         ROUND((COALESCE(imp_educacion,0)/1e9)::numeric,2)  AS educacion_b,
         ROUND((COALESCE(imp_direccion,0)/1e9)::numeric,2)  AS direccion_b
  FROM presupuestos.ced_presupuestos
  WHERE ccaa='pvc' AND capa='autonomica'
  ORDER BY periodo;"

echo "== 5. Sanidad de todas las CCAA (sanity global) =="
"${PSQL[@]}" -d "$SUPABASE_DBNAME" -c "SELECT ccaa, periodo, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b FROM presupuestos.ced_presupuestos WHERE capa='autonomica' AND periodo IN (2021,2022,2026) ORDER BY ccaa, periodo;"

echo "== FIN cierre 2026-07-01 =="
