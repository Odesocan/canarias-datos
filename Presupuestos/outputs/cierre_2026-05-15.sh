#!/usr/bin/env bash
# Cierre matinal — Noche 3 (run nocturno Cowork 2026-05-15).
# Pasaron a VERDE Python (smoke ya verificado en sandbox):
#   - can 2025  (motor=can-tomo3-resumen-programas)        141 filas / 12 conceptos
#   - lar 2026  (motor=lar-camelot-funcional-economico)     56 filas / 11 conceptos
#   - nav 2026  (motor=nav-breakdowns-functional)          167 filas / 12 conceptos
#
# Este script:
#   1) Verifica que python3 + camelot + pdftotext están disponibles localmente.
#   2) Lanza el smoke aislado de las tres nuevas CCAA para certificar reproducibilidad.
#   3) Trunca presupuestos.ced_presupuestos y lanza el maestro R con persistencia.
#   4) Reporta cobertura final por capa.
set -e

PROJ="/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"
cd "$PROJ"

# --- 1) Pre-flight local ---
command -v python3 >/dev/null || { echo "ABORT: python3 no instalado"; exit 1; }
command -v pdftotext >/dev/null || echo "WARN: pdftotext no instalado (poppler); cnt y can lo necesitan"
python3 -c 'import camelot' 2>/dev/null || echo "WARN: camelot no instalado; lar lo necesita"
command -v Rscript >/dev/null || { echo "ABORT: Rscript no encontrado"; exit 1; }
command -v psql    >/dev/null || { echo "ABORT: psql no encontrado"; exit 1; }

# --- 2) Smoke por CCAA nuevas ---
cd "$PROJ/1_extraccion"
echo "----- smoke can 2025 -----"
python3 -m ccaa --ccaa can --anio 2025 \
                --input ../fuentes/raw/can/2025/tomo_3.pdf \
                --output /tmp/test_can.csv | tail -2
echo "----- smoke lar 2026 -----"
python3 -m ccaa --ccaa lar --anio 2026 \
                --input ../fuentes/raw/lar/2025/funcional_economico.pdf \
                --output /tmp/test_lar.csv | tail -2
echo "----- smoke nav 2026 -----"
python3 -m ccaa --ccaa nav --anio 2026 \
                --input ../fuentes/raw/nav/2026/programa_csv.html \
                --output /tmp/test_nav.csv | tail -2

# --- 3) Maestro R con persistencia ---
cd "$PROJ"
export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=${USER} SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"

Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# --- 4) Verificación cobertura final ---
echo "----- cobertura por capa -----"
psql -d presupuestos_smoke -c "
SELECT capa, COUNT(*) AS filas, COUNT(DISTINCT ccaa) AS ccaas,
       MIN(periodo) AS anio_min, MAX(periodo) AS anio_max
FROM   presupuestos.ced_presupuestos
GROUP BY capa
ORDER BY capa;"

echo "----- sanidad por ccaa/periodo (B€) -----"
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo, capa,
       ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2)    AS sanidad_b,
       ROUND((COALESCE(imp_educacion,0)/1e9)::numeric,2)  AS educacion_b,
       ROUND((COALESCE(imp_direccion,0)/1e9)::numeric,2)  AS direccion_b
FROM   presupuestos.ced_presupuestos
WHERE  capa = 'autonomica'
ORDER BY ccaa, periodo;"

echo "Cierre 2026-05-15 OK."
