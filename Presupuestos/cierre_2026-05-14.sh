#!/usr/bin/env bash
# cierre_2026-05-14.sh — Cierre matinal del run nocturno Cowork (Noche 1).
#
# Pivot del run: en lugar de stubs sintéticos val/bal/gal (descartados por
# el usuario), esta noche descargué fuentes REALES (PDFs / CSVs canónicos)
# para 11 ejercicios CCAA × año nuevos. El total de evidencia longitudinal
# real en `fuentes/raw/` pasa de 8 → 19 archivos.
#
# Ejecutar desde la raíz del repo Presupuestos en la mañana del 2026-05-14.
set -euo pipefail

ROOT="/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"
cd "$ROOT"

# 0) Variables locales del smoke (NO Supabase producción)
export SUPABASE_HOST=localhost
export SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER="${USER}"
export SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos
unset SUPABASE_URL || true

echo "==> 1/5 Inventario de fuentes REALES descargadas"
find fuentes/raw -type f \( -name "*.pdf" -o -name "*.csv" \) -size +1k \
  | sort | while read f; do
    sz=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f")
    printf "  %-60s %10d bytes\n" "$f" "$sz"
  done

echo
echo "==> 2/5 Smoke Python — CSVs tidy y PDFs nuevos"
cd 1_extraccion
# pvc 2022, 2024, 2025 (CSVs rápidos)
for yr in 2022 2024 2025; do
  python3 -m ccaa --ccaa pvc --anio "$yr" \
    --input "../fuentes/raw/pvc/${yr}/csv_tidy.csv" \
    --output "/tmp/smoke_pvc_${yr}.csv" 2>&1 | tail -1
done
# cat: lentos (~35-50s por PDF). Cobertura 5 años.
for yr in 2020 2022 2023 2024 2026; do
  python3 -m ccaa --ccaa cat --anio "$yr" \
    --input "../fuentes/raw/cat/${yr}/vol_p_eid.pdf" \
    --output "/tmp/smoke_cat_${yr}.csv" 2>&1 | tail -1
done
# and: 2015 (CSV), 2024/2025/2026 (PDF)
python3 -m ccaa --ccaa and --anio 2015 \
  --input ../fuentes/raw/and/2015/gastos_csv.csv \
  --output /tmp/smoke_and_2015.csv 2>&1 | tail -1
for yr in 2024 2025 2026; do
  python3 -m ccaa --ccaa and --anio "$yr" \
    --input "../fuentes/raw/and/${yr}/memoria_programas.pdf" \
    --output "/tmp/smoke_and_${yr}.csv" 2>&1 | tail -1
done
# ext 2025, 2026
for yr in 2025 2026; do
  python3 -m ccaa --ccaa ext --anio "$yr" \
    --input "../fuentes/raw/ext/${yr}/tomo_II_EIG.pdf" \
    --output "/tmp/smoke_ext_${yr}.csv" 2>&1 | tail -1
done
# ara 2024, ast 2026
python3 -m ccaa --ccaa ara --anio 2024 \
  --input ../fuentes/raw/ara/2024/ingresos_gastos.pdf \
  --output /tmp/smoke_ara_2024.csv 2>&1 | tail -1
python3 -m ccaa --ccaa ast --anio 2026 \
  --input ../fuentes/raw/ast/2026/tomo_I.pdf \
  --output /tmp/smoke_ast_2026.csv 2>&1 | tail -1
cd ..

echo
echo "==> 3/5 Maestro R (extracción + transform + modelado + carga)"
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;" || true
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

echo
echo "==> 4/5 Cobertura por capa"
psql -d presupuestos_smoke -c "
SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas,
       MIN(periodo) anio_min, MAX(periodo) anio_max
FROM presupuestos.ced_presupuestos GROUP BY capa ORDER BY capa;"

echo
echo "==> 5/5 Resumen ccaa × año (capa autonomica)"
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo,
       ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2)      AS sanidad_b,
       ROUND((COALESCE(imp_educacion,0)/1e9)::numeric,2)    AS educacion_b,
       ROUND((COALESCE(imp_dependencia,0)/1e9)::numeric,2)  AS dependencia_b
FROM presupuestos.ced_presupuestos
WHERE capa='autonomica' ORDER BY ccaa, periodo;"

echo
echo "==> Done. Actualiza logs/progreso.md columna DB para los años verdes."
echo "==> Próximo run nocturno (Noche 2): escribir extractores reales para"
echo "    clm 2026, cnt 2025, mad 2026 (PDFs ya en fuentes/raw/)."
