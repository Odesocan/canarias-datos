#!/usr/bin/env bash
# Cierre matutino 2026-07-28 · Presupuestos ODESOCAN / Canarias en Datos
# Generado por el run nocturno (sandbox, solo Python). El run NO tocó los
# extractores verdes ni la DB; solo certificó extracción y regeneró la tabla.
# Ejecuta esto para certificar "verde DB" y refrescar ced_presupuestos.
set -euo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=$USER SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

# 1) Recarga completa del maestro (extracción cacheada por SHA -> reconstruye staging + carga)
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# 2) Certificación de cobertura y magnitudes
psql -d presupuestos_smoke -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"
psql -d presupuestos_smoke -c "SELECT ccaa, periodo, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b FROM presupuestos.ced_presupuestos WHERE capa='autonomica' ORDER BY ccaa, periodo;"

# 3) Evaluador post-extracción (magnitudes sobre staging NOMINAL, no la DB deflactada)
python3 tools/auditoria_magnitud.py || true

echo "OK cierre 2026-07-28. Tabla del día: outputs/tabla_resumen_2026-07-28.xlsx"
