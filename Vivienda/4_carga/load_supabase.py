"""
Carga a Supabase (schema canendatos) los outputs del pipeline R:
  - 4_carga/ced_vivienda_global.csv  -> canendatos.ced_vivienda_global
  - 4_carga/ced_vivienda_gen.csv     -> canendatos.ced_vivienda_gen

Replica el comportamiento de DBI::dbWriteTable(overwrite=TRUE) del
pipeline R: DROP TABLE + CREATE TABLE + INSERT.

Uso:
    python 4_carga/load_supabase.py

Credenciales: lee ../.Renviron con las variables CED_DB_*.
"""

import sys
from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

ROOT = Path(__file__).resolve().parent.parent
LOAD_DIR = ROOT / "4_carga"
RENVIRON = ROOT / ".Renviron"


def load_renviron(path: Path) -> dict:
    """Lee un .Renviron estilo KEY=VALUE (sin comillas, sin export)."""
    env = {}
    if not path.exists():
        sys.exit(f".Renviron no encontrado: {path}")
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


SCHEMA_DEFINITIONS = {
    "ced_vivienda_global": {
        "columns": [
            ("ccaa", "text"),
            ("periodo", "integer"),
            ("origen", "text"),
            ("dif_finmes", "double precision"),
            ("espacio_insuf", "double precision"),
            ("gasto_elevado", "double precision"),
            ("hogares_mono", "double precision"),
            ("precio_alquiler_periodo_label", "text"),
            ("precio_alquiler", "double precision"),
            ("precio_venta_periodo_label", "text"),
            ("precio_venta", "double precision"),
            ("retrasos_pagos", "double precision"),
            ("salario_destinado", "double precision"),
        ],
        "csv": "ced_vivienda_global.csv",
    },
    "ced_vivienda_gen": {
        "columns": [
            ("ccaa", "text"),
            ("periodo", "integer"),
            ("genero", "text"),
            ("origen", "text"),
            ("dif_finmes", "double precision"),
            ("espacio_insuf", "double precision"),
            ("gasto_elevado", "double precision"),
            ("hogares_mono", "double precision"),
            ("retrasos_pagos", "double precision"),
            ("salario_destinado", "double precision"),
        ],
        "csv": "ced_vivienda_gen.csv",
    },
}


def read_csv_es(path: Path) -> pd.DataFrame:
    """CSV en formato español: separador ';' y decimal ','."""
    return pd.read_csv(path, sep=";", decimal=",", encoding="utf-8")


def rebuild_table(cur, schema: str, table: str, columns: list[tuple]) -> None:
    cols_sql = ",\n    ".join(f'"{c}" {t}' for c, t in columns)
    cur.execute(f'DROP TABLE IF EXISTS "{schema}"."{table}"')
    cur.execute(f'CREATE TABLE "{schema}"."{table}" (\n    {cols_sql}\n)')


def insert_df(cur, schema: str, table: str, df: pd.DataFrame, columns: list[tuple]) -> int:
    col_names = [c for c, _ in columns]
    missing = [c for c in col_names if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas en CSV para {table}: {missing}")

    df = df[col_names].copy().where(pd.notna, None)
    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]
    # Reemplazar NaN residual por None (por si where no atrapó float nan)
    rows = [tuple(None if (isinstance(v, float) and pd.isna(v)) else v for v in r) for r in rows]

    placeholders = f'({",".join(["%s"] * len(col_names))})'
    cols_sql = ", ".join(f'"{c}"' for c in col_names)
    sql = f'INSERT INTO "{schema}"."{table}" ({cols_sql}) VALUES %s'
    execute_values(cur, sql, rows, template=placeholders, page_size=500)
    return len(rows)


def main() -> None:
    env = load_renviron(RENVIRON)
    required = ["CED_DB_NAME", "CED_DB_HOST", "CED_DB_PORT",
                "CED_DB_USER", "CED_DB_PASSWORD", "CED_DB_SCHEMA"]
    missing = [k for k in required if not env.get(k)]
    if missing:
        sys.exit(f"Faltan variables en .Renviron: {missing}")

    schema = env["CED_DB_SCHEMA"]
    print(f"Schema destino: {schema}")

    conn = psycopg2.connect(
        dbname=env["CED_DB_NAME"],
        host=env["CED_DB_HOST"],
        port=int(env["CED_DB_PORT"]),
        user=env["CED_DB_USER"],
        password=env["CED_DB_PASSWORD"],
        sslmode="require",
    )
    conn.autocommit = False
    try:
        with conn.cursor() as cur:
            cur.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema}"')

            for table, spec in SCHEMA_DEFINITIONS.items():
                csv_path = LOAD_DIR / spec["csv"]
                if not csv_path.exists():
                    raise FileNotFoundError(csv_path)
                df = read_csv_es(csv_path)
                print(f"\n=== {schema}.{table} ===")
                print(f"  CSV: {csv_path.name} ({len(df)} filas)")
                rebuild_table(cur, schema, table, spec["columns"])
                n = insert_df(cur, schema, table, df, spec["columns"])
                print(f"  Insertadas: {n}")

        conn.commit()
        print("\nCommit OK")
    except Exception as e:
        conn.rollback()
        print(f"\nERROR: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
