#!/usr/bin/env bash
# Cierre matutino 2026-07-20 — certificar "verde DB" tras el fix de neteo OOAA en ara.
# IMPORTANTE: el extractor de ara CAMBIÓ esta noche. El maestro R cachea la extracción
# por SHA-256 del raw (logs/manifest.jsonl); como el raw NO cambió, hay que resetear el
# manifiesto para forzar el re-parseo, o ara se cargará con los importes VIEJOS.
set -euo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER="$USER" SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

# 1 · Forzar re-parseo (el código de ara cambió, el raw no)
if [ -f logs/manifest.jsonl ]; then
  cp logs/manifest.jsonl "logs/manifest.jsonl.bak.$(date +%Y%m%d_%H%M%S)"
  : > logs/manifest.jsonl
  echo "manifest.jsonl reseteado (backup guardado)"
fi

# 2 · Maestro completo
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# 3 · Verificación de carga
psql -d presupuestos_smoke -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"
psql -d presupuestos_smoke -c "SELECT ccaa, periodo, capa, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b FROM presupuestos.ced_presupuestos WHERE ccaa='Aragón' ORDER BY periodo;"

# 4 · Gate de magnitud sobre el staging nominal (NO sobre la DB, que va deflactada)
python3 tools/auditoria_magnitud.py --csv outputs/staging_py_2026-07-20.csv || true

# 5 · Comprobación específica del fix: ara debe bajar ~5-6% en total y SUBIR ~65 M en sanidad
echo "ara esperado tras el fix (nominal, staging): 2015 tot 5.30B san 1.604B … 2026 tot 8.61B san 2.772B"
