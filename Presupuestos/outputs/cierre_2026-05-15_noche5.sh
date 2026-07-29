#!/usr/bin/env bash
# Cierre matinal Noche 5 (run nocturno 2026-05-15, tras 04+05).
#
# Antes de ejecutar, considera completar el raw de mur/2025 desde tu IP
# (no rate-limitada por Radware) — el script sandbox sólo bajó 24 de 67
# secciones. Comando opcional:
#
#   python3 tools/mur_download.py --anio 2025 --resume
#
# Después corre este script para lanzar el maestro y verificar la
# carga en PG local (presupuestos_smoke).

set -euo pipefail

cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost
export SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=${USER:-$(whoami)}
export SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

echo "==> 1. Vaciar tabla canónica antes de re-cargar"
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"

echo
echo "==> 2. Correr el maestro completo (extracción + transform + modelo + carga)"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -60

echo
echo "==> 3. Resumen por capa"
psql -d presupuestos_smoke -c "
SELECT capa,
       COUNT(*)                                AS filas,
       COUNT(DISTINCT ccaa)                    AS ccaas,
       MIN(periodo)                            AS anio_min,
       MAX(periodo)                            AS anio_max
FROM   presupuestos.ced_presupuestos
GROUP BY capa
ORDER BY capa;
"

echo
echo "==> 4. Comprobar nuevos ejercicios cargados esta noche"
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo, capa,
       ROUND((COALESCE(imp_sanidad,0)   /1e9)::numeric,2) AS sanidad_b,
       ROUND((COALESCE(imp_educacion,0) /1e9)::numeric,2) AS educacion_b,
       ROUND((COALESCE(imp_direccion,0) /1e9)::numeric,2) AS direccion_b
FROM   presupuestos.ced_presupuestos
WHERE  (ccaa = 'mur' AND periodo = 2025)
   OR  (ccaa = 'val' AND periodo = 2024)
   OR  (ccaa = 'bal' AND periodo IN (2022, 2023, 2024))
ORDER BY ccaa, periodo;
"

echo
echo "==> 5. Tabla cobertura completa CCAA x año (capa autonómica)"
psql -d presupuestos_smoke -c "
SELECT ccaa,
       string_agg(periodo::text, ', ' ORDER BY periodo) AS anios,
       COUNT(*) AS n_anios
FROM   presupuestos.ced_presupuestos
WHERE  capa = 'autonomica'
GROUP BY ccaa
ORDER BY ccaa;
"

echo
echo "Cierre Noche 5 completado."
