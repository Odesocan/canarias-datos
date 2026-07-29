#!/usr/bin/env bash
# Cierre matutino 2026-07-06 — certifica "verde DB" y refresca la magnitud
# deflactada de las CCAA que el sandbox nocturno dejó como '·' en la tabla resumen
# (ara, can, lar, mad, ext + años PDF sueltos). Ejecútalo tú en el Mac (con R+psql).
set -euo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER="$USER" SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

# 1) Run completo del maestro (extracción→carga) sobre la DB smoke local.
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# 2) Cobertura por capa.
psql -d presupuestos_smoke -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"

# 3) Sanidad €B por CCAA×año (deflactado) — completa las celdas '·' de la tabla resumen.
psql -d presupuestos_smoke -c "SELECT ccaa, periodo, capa, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b FROM presupuestos.ced_presupuestos WHERE capa='autonomica' ORDER BY ccaa, periodo;"

# 4) (opcional) Gate de magnitud sobre el staging nominal recién generado por el maestro.
python3 tools/auditoria_magnitud.py || echo "auditoria_magnitud: revisa anomalías (ver salida)"

echo "OK cierre 2026-07-06. La tabla resumen de la noche está en outputs/tabla_resumen_2026-07-06.{md,csv,xlsx}"
