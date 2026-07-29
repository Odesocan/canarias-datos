#!/usr/bin/env bash
# Cierre matinal — Noche 4 (run nocturno Cowork 2026-05-15).
#
# Pasaron a VERDE Python esta noche (smoke ya verificado en sandbox):
#   - bal 2025  (motor=bal-frameset-secciones)             141 filas / 13 conceptos / 74.5% mapped
#   - val 2025  (motor=val-rpc-secciones)                  174 filas / 13 conceptos / 86.2% mapped
#   - cym 2026  (motor=cym-jcyl-xls)                       103 filas / 13 conceptos / 85.4% mapped
#
# Este script:
#   1) Verifica que python3 + Rscript + psql están disponibles localmente.
#   2) Smoke aislado de las tres nuevas CCAA (debe imprimir "OK motor=…").
#   3) Trunca presupuestos.ced_presupuestos y lanza el maestro R con persistencia.
#   4) Reporta cobertura final por capa.
set -e

PROJ="/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"
cd "$PROJ"

# --- 1) Pre-flight local ---
command -v python3 >/dev/null || { echo "ABORT: python3 no instalado"; exit 1; }
python3 -c 'import xlrd, pandas, pdfplumber, bs4, yaml' 2>/dev/null \
    || { echo "ABORT: faltan deps Python (xlrd, pandas, pdfplumber, bs4, yaml). Instalar: pip install xlrd pandas pdfplumber beautifulsoup4 pyyaml lxml requests"; exit 1; }
command -v Rscript >/dev/null || { echo "ABORT: Rscript no encontrado"; exit 1; }
command -v psql    >/dev/null || { echo "ABORT: psql no encontrado"; exit 1; }

# --- 2) Smoke por CCAA nuevas ---
cd "$PROJ/1_extraccion"
echo "----- smoke bal 2025 -----"
python3 -m ccaa --ccaa bal --anio 2025 \
                --input ../fuentes/raw/bal/2025/memoria_programas.html \
                --output /tmp/test_bal.csv | tail -2
echo "----- smoke val 2025 -----"
python3 -m ccaa --ccaa val --anio 2025 \
                --input ../fuentes/raw/val/2025/tomo_II.html \
                --output /tmp/test_val.csv | tail -2
echo "----- smoke cym 2026 -----"
python3 -m ccaa --ccaa cym --anio 2026 \
                --input ../fuentes/raw/cym/2026/datos_abiertos_csv.csv \
                --output /tmp/test_cym.csv | tail -2

# --- 3) Maestro R con persistencia ---
cd "$PROJ"
export SUPABASE_HOST=localhost
export SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER=$USER
export SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# --- 4) Cobertura por capa ---
echo ""
echo "===== COBERTURA FINAL ced_presupuestos ====="
psql -d presupuestos_smoke -c "
SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas,
       MIN(periodo) anio_min, MAX(periodo) anio_max
FROM presupuestos.ced_presupuestos
GROUP BY capa;"

echo ""
echo "===== Sanidad por CCAA × Año (B€) ====="
psql -d presupuestos_smoke -c "
SELECT ccaa, periodo, capa,
       ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b,
       ROUND((COALESCE(imp_educacion,0)/1e9)::numeric,2) AS edu_b
FROM presupuestos.ced_presupuestos
ORDER BY ccaa, periodo;"

echo ""
echo "===== Verde DB esperado para Noche 4 ====="
echo "  - bal 2025: imp_sanidad ~2 390 M€, imp_educacion ~1 419 M€, imp_dependencia ~225 M€, imp_empleo ~140 M€"
echo "  - val 2025: imp_sanidad ~8 995 M€, imp_educacion ~7 230 M€, imp_dependencia ~1 920 M€, imp_empleo ~304 M€"
echo "  - cym 2026: imp_sanidad ~4 813 M€, imp_educacion ~2 631 M€, imp_dependencia ~950 M€, imp_empleo ~388 M€"
echo "  - 12 -> 15 CCAA con datos en capa autonómica (faltan mur, nav, can-ya-verde-extender)."
