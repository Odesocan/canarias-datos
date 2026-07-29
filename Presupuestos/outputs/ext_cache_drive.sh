#!/usr/bin/env bash
# Driver resumable para cachear los sidecars pagetext de ext (Ley DOE, ~700-950
# págs./año, 27MB). Procesa años NO completos en secuencia (secuencial rinde más
# que paralelo por contención de CPU en el sandbox) hasta agotar ~36s de budget.
# Reanuda solo: cada llamada avanza donde quedó. Uso: bash outputs/ext_cache_drive.sh
set -u
cd "$(dirname "$0")/.."
BUDGET=${1:-36}
CHUNK=${2:-140}
T0=$SECONDS
for y in 2015 2016 2017 2018 2019 2020 2021 2022 2023 2025 2026; do
  f="fuentes/raw/ext/$y/ley_doe.pdf"
  sc="$f.pagetext.json"
  [ -f "$f" ] || continue
  # saltar si ya completo
  if [ -f "$sc" ] && python3 -c "import json,sys;sys.exit(0 if json.load(open('$sc')).get('complete') else 1)" 2>/dev/null; then
    continue
  fi
  while [ $((SECONDS - T0)) -lt "$BUDGET" ]; do
    out=$(python3 outputs/ext_cache_fast.py "$f" "$CHUNK" 2>&1 | tail -1)
    echo "$y :: $out"
    # completo o sin avance -> siguiente año
    echo "$out" | grep -q "complete=True" && break
    echo "$out" | grep -q "ya completo" && break
    echo "$out" | grep -q "^OK" || break
    [ $((SECONDS - T0)) -ge "$BUDGET" ] && break
  done
  [ $((SECONDS - T0)) -ge "$BUDGET" ] && break
done
echo "=== elapsed $((SECONDS - T0))s ==="
