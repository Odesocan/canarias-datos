#!/usr/bin/env bash
# Cierre 2026-07-22 — certificar "verde DB" tras MIGRAR Galicia 2022-2026 de CSV a PDF-programa.
#
# CAMBIO DE LA SESIÓN: gal 2022-2026 pasó de `gastos_orzamento: csv` (consellería×grupo,
# 7-8 conceptos) a `progr: pdf` (PROGR_I/II "Orzamentos por programas", 11 conceptos, regla C),
# homogéneo con 2015-2021. Cambiaron el alias (csv→progr) y el raw (→progr.pdf), así que el
# maestro re-parseará gal; aun así reseteamos el manifest para forzar un re-parseo limpio.
#
# PRE-REQUISITO DB: el puerto 5432 debe apuntar al homebrew `postgresql@17` (trust, donde vive
# `presupuestos_smoke`). Si escucha el EDB PostgreSQL 18 (/Library/PostgreSQL/18), páralo antes:
#     sudo launchctl bootout system /Library/LaunchDaemons/com.edb.launchd.postgresql-18.plist
#     brew services start postgresql@17
#   (verifica con:  ps aux | grep -m1 "postgres .*-D" )
set -euo pipefail
cd "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/CANARIAS EN DATOS/Presupuestos"

export SUPABASE_HOST=localhost SUPABASE_PORT=5432
export SUPABASE_DBNAME=presupuestos_smoke
export SUPABASE_USER="$USER" SUPABASE_PASS=fake
export SUPABASE_SCHEMA=presupuestos

# 1 · Forzar re-parseo (gal cambió de fuente csv→pdf; reset con backup)
if [ -f logs/manifest.jsonl ]; then
  cp logs/manifest.jsonl "logs/manifest.jsonl.bak.$(date +%Y%m%d_%H%M%S)"
  : > logs/manifest.jsonl
  echo "manifest.jsonl reseteado (backup guardado)"
fi

# 2 · Maestro completo (extracción re-parsea las 17 CCAA; gal 2022-2026 desde PROGR_*.pdf)
psql -d presupuestos_smoke -c "TRUNCATE presupuestos.ced_presupuestos;"
Rscript 00_maestro.R --steps=extraccion,transformacion,modelado,carga --with-db=true 2>&1 | tail -40

# 3 · Verificación de carga (global + Galicia: sanidad debe encadenar 4.38→…→5.43B sin salto)
psql -d presupuestos_smoke -c "SELECT capa, COUNT(*) filas, COUNT(DISTINCT ccaa) ccaas, MIN(periodo) anio_min, MAX(periodo) anio_max FROM presupuestos.ced_presupuestos GROUP BY capa;"
psql -d presupuestos_smoke -c "SELECT ccaa, periodo, ROUND((COALESCE(imp_sanidad,0)/1e9)::numeric,2) AS sanidad_b, ROUND((COALESCE(imp_vivienda,0)/1e6)::numeric,1) AS vivienda_m, ROUND((COALESCE(imp_turismo,0)/1e6)::numeric,1) AS turismo_m, ROUND((COALESCE(imp_idi,0)/1e6)::numeric,1) AS idi_m FROM presupuestos.ced_presupuestos WHERE ccaa='Galicia' ORDER BY periodo;"

# 4 · Gate de magnitud sobre el staging NOMINAL de hoy (NO sobre la DB, que va deflactada)
python3 tools/auditoria_magnitud.py --csv outputs/staging_py_2026-07-22.csv || true

# 5 · Comprobación específica del fix gal (nominal, staging): 2022-2026 deben tener 11 conceptos
echo "gal esperado tras la migración (nominal, staging PDF regla C):"
echo "  sanidad  2022=4.38B 2023=4.74B 2024=4.94B 2025=5.21B 2026=5.43B  (−4.6% vs CSV = sesgo regla C)"
echo "  vivienda/idi/turismo/igualdad/diversidad presentes en 2022-2026 (antes NULL con el CSV)"
