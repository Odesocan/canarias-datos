# -*- coding: utf-8 -*-
"""
FASE 4 · CARGA — Volcado de ced_empleo a Supabase (canendatos)
Canarias en Datos · Sección Empleo · ODESOCAN

Carga las tablas de distribución que consume la pieza D3:
  · canendatos.ced_empleo_global   (CCAA · año · indicadores "Ambos géneros"/territorial)
  · canendatos.ced_empleo_gen      (CCAA · año · género · indicadores con desglose)

desde los CSV generados por 5_visualizacion/preparar_datos_viz.py.

CARGA ATÓMICA (§7.7 del cuaderno): TRUNCATE + INSERT de ambas tablas dentro de
UNA sola transacción. Los lectores (la web) nunca ven una tabla vacía o a medias:
siguen viendo los datos anteriores hasta el COMMIT. Se preservan RLS, políticas,
grants y claves primarias (el objeto tabla no se recrea).

CREDENCIALES (nunca se incrustan; se leen del entorno):
    export SUPABASE_DB_URL="postgresql://postgres:[PASSWORD]@db.kdpsjutsgvghdtzoskkg.supabase.co:5432/postgres"
  o el pooler en modo sesión (puerto 5432):
    export SUPABASE_DB_URL="postgresql://postgres.kdpsjutsgvghdtzoskkg:[PASSWORD]@aws-0-eu-west-1.pooler.supabase.com:5432/postgres"

  La contraseña es la de la base de datos (secreto del pipeline). NO usar la
  anon key aquí: la carga requiere permisos de escritura.

Uso:
    python cargar_supabase.py            # regenera los CSV y carga
    python cargar_supabase.py --no-prep  # carga los CSV existentes sin regenerarlos
    python cargar_supabase.py --dry-run  # valida y muestra recuento, sin escribir
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

BASE = Path(__file__).resolve().parent
VIZ = BASE.parent / "5_visualizacion"
TABLAS = [
    ("canendatos.ced_empleo_global", VIZ / "ced_empleo_global.csv"),
    ("canendatos.ced_empleo_gen",    VIZ / "ced_empleo_gen.csv"),
]


def _native(v):
    """numpy/NaN → tipos nativos de Python / None (NULL en SQL)."""
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    if hasattr(v, "item"):        # numpy scalar
        v = v.item()
    if isinstance(v, float) and math.isnan(v):
        return None
    return v


def _leer(csv: Path) -> tuple[list[str], list[tuple]]:
    if not csv.exists():
        raise SystemExit(f"No existe {csv}. Ejecuta antes: "
                         f"python ../5_visualizacion/preparar_datos_viz.py")
    df = pd.read_csv(csv, sep=";")
    cols = list(df.columns)
    filas = [tuple(_native(v) for v in row) for row in df.itertuples(index=False, name=None)]
    return cols, filas


def cargar(dry_run: bool = False) -> None:
    datos = {tabla: _leer(csv) for tabla, csv in TABLAS}
    for tabla, (cols, filas) in datos.items():
        print(f"  {tabla}: {len(filas)} filas · {len(cols)} columnas")
    if dry_run:
        print("(--dry-run) No se escribe nada.")
        return

    dburl = os.environ.get("SUPABASE_DB_URL")
    if not dburl:
        raise SystemExit("Falta SUPABASE_DB_URL (cadena de conexión Postgres de Supabase).")

    conn = psycopg2.connect(dburl)
    conn.autocommit = False        # una sola transacción para ambas tablas
    try:
        with conn.cursor() as cur:
            for tabla, (cols, filas) in datos.items():
                cur.execute(f"TRUNCATE {tabla};")
                execute_values(
                    cur,
                    f"INSERT INTO {tabla} ({', '.join(cols)}) VALUES %s",
                    filas, page_size=1000,
                )
        conn.commit()
        # verificación post-commit
        with conn.cursor() as cur:
            for tabla, _ in TABLAS:
                cur.execute(f"SELECT count(*) FROM {tabla};")
                print(f"  ✓ {tabla}: {cur.fetchone()[0]} filas en BD")
        print("✓ Carga atómica completada (COMMIT).")
    except Exception:
        conn.rollback()
        print("✗ Error en la carga; ROLLBACK (los datos anteriores quedan intactos).", file=sys.stderr)
        raise
    finally:
        conn.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="Carga de ced_empleo a Supabase (Empleo)")
    ap.add_argument("--no-prep", action="store_true", help="No regenerar los CSV antes de cargar")
    ap.add_argument("--dry-run", action="store_true", help="Validar y contar sin escribir")
    args = ap.parse_args()

    if not args.no_prep:
        sys.path.insert(0, str(VIZ))
        import preparar_datos_viz          # regenera los CSV desde 3_modelado
        preparar_datos_viz.main()

    cargar(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
