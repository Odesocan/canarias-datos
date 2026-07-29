#!/usr/bin/env bash
# tests/bench_extractors.sh — Ejecuta cada extractor contra el raw local
# correspondiente y reporta cuántas filas extrae.
set -e
cd "$(dirname "$0")/.."

declare -a SOURCES=(
  "and:2026:fuentes/raw/and/2026/memoria_programas.pdf"
  "ara:2024:fuentes/raw/ara/2024/ingresos_gastos.pdf"
  "ast:2026:fuentes/raw/ast/2026/tomo_I.pdf"
  "bal:2025:fuentes/raw/bal/2025/memoria_programas.html"
  "can:2025:fuentes/raw/can/2025/memoria_programas.pdf"
  "cnt:2025:fuentes/raw/cnt/2025/ingresos_gastos.pdf"
  "cym:2026:fuentes/raw/cym/2026/datos_abiertos_csv.csv"
  "clm:2026:fuentes/raw/clm/2026/tomo_I.pdf"
  "cat:2026:fuentes/raw/cat/2026/vol_p_eid.pdf"
  "ext:2025:fuentes/raw/ext/2025/tomo_II_EIG.pdf"
  "gal:2026:fuentes/raw/gal/2026/portal_index.html"
  "lar:2025:fuentes/raw/lar/2025/funcional_economico.pdf"
  "mad:2026:fuentes/raw/mad/2026/libro_03.pdf"
  "mur:2025:fuentes/raw/mur/2025/portal_movil.html"
  "nav:2026:fuentes/raw/nav/2026/programa_csv.csv"
  "pvc:2025:fuentes/raw/pvc/2025/csv_tidy.csv"
  "val:2025:fuentes/raw/val/2025/tomo_II.html"
)

cd 1_extraccion

printf "%-6s %-6s %-30s %s\n" "CCAA" "AÑO" "MOTOR" "FILAS"
printf "%-6s %-6s %-30s %s\n" "----" "---" "-----" "-----"

for entry in "${SOURCES[@]}"; do
  IFS=":" read ccaa anio src <<< "$entry"
  src="../$src"
  if [ ! -f "$src" ] || [ ! -s "$src" ]; then
    printf "%-6s %-6s %-30s %s\n" "$ccaa" "$anio" "(sin raw)" "-"
    continue
  fi
  out="/tmp/bench_${ccaa}_${anio}.csv"
  result=$(python3 -m extractors --ccaa "$ccaa" --anio "$anio" --input "$src" --output "$out" 2>&1 | head -1)
  filas=$(echo "$result" | grep -oE 'filas=[0-9]+' | head -1)
  motor=$(echo "$result" | grep -oE 'motor=[a-z\-]+' | head -1 | sed 's/motor=//')
  if [ -z "$filas" ]; then filas="warn"; fi
  if [ -z "$motor" ]; then motor="(sin motor)"; fi
  printf "%-6s %-6s %-30s %s\n" "$ccaa" "$anio" "$motor" "$filas"
done
