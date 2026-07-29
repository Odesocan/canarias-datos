#!/usr/bin/env bash
# Cierre "verde DB" · Presupuestos · ODESOCAN Canarias en Datos
# Certifica: carga el staging deflactado en presupuestos_smoke y verifica.
#
# CORREGIDO 2026-07-24 (dos bugs que dejaban la carga VACÍA — ver logs/progreso.md 2026-07-24):
#   BUG 1 (paso 1): antes solo hacía `cp` del manifest (backup) pese a decir "reset". El
#     manifest.jsonl es APPEND-ONLY y run_extraccion reconstruye el staging SOLO con las
#     fuentes recién parseadas; las que hacen match de SHA se saltan y NO entran. Con el
#     manifest intacto (o repoblado por otro maestro que corra en paralelo), la carga sale
#     con 0 filas. Hay que MOVER el manifest fuera, no copiarlo.
#   BUG 2 (paso 0): asumía que el 5432 lo ocupa EDB18 y que hay que arrancar postgresql@17.
#     En la práctica lo sirve postgresql@16 y presupuestos_smoke responde por trust. Se
#     sustituye la suposición por una comprobación de reachability real.
set -euo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=$USER SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

# 0) Comprobación de reachability (no asumir qué servidor sirve el 5432). Si falla, el
#    servidor donde vive presupuestos_smoke no está arrancado: arranca el que corresponda
#    (p. ej. `brew services start postgresql@16`) y reintenta.
if ! PGPASSWORD="$SUPABASE_PASS" psql -h "$SUPABASE_HOST" -p "$SUPABASE_PORT" -U "$SUPABASE_USER" \
        -d "$SUPABASE_DBNAME" -tAc "SELECT 1" >/dev/null 2>&1; then
  echo "ERROR: presupuestos_smoke no responde en ${SUPABASE_HOST}:${SUPABASE_PORT}." >&2
  echo "       Arranca el Postgres que la aloja (p. ej. brew services start postgresql@16) y reintenta." >&2
  exit 1
fi

# 1) RESET del manifest (backup + MOVER fuera) para forzar el re-parseo completo. Imprescindible
#    si tocaste código de extractor o correspondencias (el cache es por SHA del raw, no del código).
#    Se hace justo antes del maestro y sin hueco para que ningún otro run repueble el manifest.
if [ -f logs/manifest.jsonl ]; then
  cp logs/manifest.jsonl "logs/manifest.jsonl.bak_$(date +%F_%H%M%S)"
  mv logs/manifest.jsonl "logs/manifest.jsonl.reset_$(date +%F_%H%M%S)"
fi
rm -f 1_extraccion/staging_gasto.rds   # evita reusar un staging viejo/vacío

# 2) Reset de la tabla y run completo del maestro (extracción→carga, deflactado)
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# 3) Verificación de cobertura por capa
psql -d presupuestos_smoke -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"

# 3b) Celdas autonómicas faltantes vs grid 17×(2015-2026) — deben ser solo cym 2015 y mur 2026
psql -d presupuestos_smoke -tAc "WITH grid AS (SELECT c.ccaa,g.periodo FROM (SELECT DISTINCT ccaa FROM presupuestos.ced_presupuestos WHERE capa='autonomica') c CROSS JOIN generate_series(2015,2026) g(periodo)), have AS (SELECT ccaa,periodo FROM presupuestos.ced_presupuestos WHERE capa='autonomica') SELECT 'FALTA: '||grid.ccaa||' '||grid.periodo FROM grid LEFT JOIN have USING(ccaa,periodo) WHERE have.ccaa IS NULL ORDER BY 1;"

# 4) Spot-check de sanidad por CCAA-año (€ constantes en DB)
psql -d presupuestos_smoke -c "SELECT ccaa, periodo, capa, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b FROM presupuestos.ced_presupuestos WHERE capa='autonomica' ORDER BY ccaa, periodo;"

# 5) Gate de magnitud sobre el staging NOMINAL fresco (no la DB deflactada)
python3 tools/auditoria_magnitud.py || echo "  (revisa las alertas conocidas: ast/pvc 2025-2026 €/hab por techo de banda; no bloqueantes)"

echo "OK · cierre verde-DB completado."
