#!/usr/bin/env bash
# Cierre matinal Noche 13 (2026-05-26)
# Resultado nocturno: 12 ejercicios-CCAA nuevos VERDE Python
#   ara/2024, ast/2024-26, clm/2024-26, cnt/2025, ext/2025-26,
#   lar/2025, mad/2026
# Cambios de código: 3 YAML de correspondencias (ara, ast, ext) sólo ADD.
# Sidecars nuevos: ara/2024, ast/2024-26, clm/2024-26, cnt/2025, ext/2025.
#
# Pre-requisitos: Rscript >= 4.x con el proyecto cargado; PostgreSQL local
# levantado con la base `presupuestos_smoke`; xlrd>=2.0 instalado (cym).

set -euo pipefail

cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost
export SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=${USER}
export SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

echo "=== 1) TRUNCATE tabla canónica ==="
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"

echo
echo "=== 2) Maestro R: extraccion + transformacion + modelado + carga ==="
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -60

echo
echo "=== 3) Cobertura por capa ==="
psql -d presupuestos_smoke -c "
SELECT capa,
       COUNT(*) AS filas,
       COUNT(DISTINCT ccaa) AS ccaas,
       MIN(periodo) AS anio_min,
       MAX(periodo) AS anio_max
FROM presupuestos.ced_presupuestos
GROUP BY capa
ORDER BY capa;"

echo
echo "=== 4) Sanidad por CCAA-año (capa autonómica, en B€) ==="
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo, capa,
       ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric, 2) AS sanidad_b,
       ROUND((COALESCE(imp_educacion,0)/1e9)::numeric, 2) AS educ_b,
       ROUND((COALESCE(imp_dependencia,0)/1e9)::numeric, 2) AS depend_b
FROM presupuestos.ced_presupuestos
WHERE capa = 'autonomica'
ORDER BY ccaa, periodo;"

echo
echo "=== 5) Conteo de conceptos no NULL por CCAA-año (capa autonómica) ==="
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo,
       (CASE WHEN imp_sanidad      IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_educacion    IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_soberania    IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_direccion    IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_vivienda     IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_empleo       IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_idi          IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_dependencia  IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_discapacidad IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_salud_mental IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_diversidad   IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_turismo      IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN imp_igualdad     IS NOT NULL THEN 1 ELSE 0 END) AS n_conceptos
FROM presupuestos.ced_presupuestos
WHERE capa = 'autonomica'
ORDER BY ccaa, periodo;"

echo
echo "=== DONE. Anota en logs/progreso.md la columna 'DB' tras revisar el output ==="
