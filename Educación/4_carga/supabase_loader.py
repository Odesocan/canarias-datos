"""
Carga atómica a Supabase (staging + swap) para el pipeline Educación.

Replica el patrón robusto de Dependencia/Salud Mental (Cuaderno §8.7):
  1. Se escribe la tabla en un staging `{tabla}_staging_YYYYMMDDHHMMSS`.
  2. En la MISMA transacción: DROP de la tabla destino + RENAME del staging.
  3. Tras el swap se re-aplican índice único, RLS y GRANT SELECT para `anon`.
El dashboard nunca lee una tabla a medio escribir.

Conexión Postgres directa vía SQLAlchemy/psycopg2 (no REST): necesaria para el
DDL (CREATE/DROP/RENAME/POLICY).
"""

from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text

from config_carga import DB
from utils_carga import logger


def _engine():
    url = (f"postgresql+psycopg2://{DB['user']}:{DB['password']}"
           f"@{DB['host']}:{DB['port']}/{DB['dbname']}")
    return create_engine(url, connect_args={"sslmode": DB["sslmode"]}, pool_pre_ping=True)


def _timestamp():
    # Sin Date.now prohibido: datetime normal (no es workflow)
    return datetime.now().strftime("%Y%m%d%H%M%S")


def cargar_tablas(tablas: dict, schema: str) -> None:
    """tablas = {nombre: {'df': DataFrame, 'indice': [cols]}}.

    Publicación ATÓMICA de todo el lote: los swaps de las N tablas y la fase de
    índices/RLS ocurren en UNA sola transacción (`eng.begin()`). Si algo falla en
    cualquier punto, se hace rollback completo y el dashboard sigue viendo la
    versión anterior íntegra — nunca un estado a medias (global-nueva + gen-vieja,
    o tablas sin GRANT/RLS). El DDL de Postgres es transaccional, y pandas reutiliza
    la transacción abierta al pasarle la conexión.
    """
    eng = _engine()
    ts = _timestamp()
    try:
        with eng.begin() as con:                       # una transacción para todo
            # Lock de nivel transacción: evita que dos cargas simultáneas se pisen
            # en el DROP/RENAME. Se libera solo al confirmar/revertir la transacción.
            con.execute(text("SELECT pg_advisory_xact_lock(4801532)"))
            con.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
            for nombre, spec in tablas.items():
                df = spec["df"]
                staging = f"{nombre}_staging_{ts}"
                df.to_sql(staging, con, schema=schema, index=False,
                          if_exists="replace", method="multi", chunksize=500)
                con.execute(text(f'DROP TABLE IF EXISTS "{schema}"."{nombre}"'))
                con.execute(text(
                    f'ALTER TABLE "{schema}"."{staging}" RENAME TO "{nombre}"'))
                logger.info("  DB: %s.%s en staging+swap (%d filas)", schema, nombre, len(df))
            _indices_y_rls(con, schema, tablas)
        logger.info("  DB: transacción confirmada (swaps + índices/RLS atómicos)")
    except Exception as e:  # noqa: BLE001
        logger.error("  DB: fallo en la carga (%s) — rollback completo, BD intacta", e)
        raise


def _indices_y_rls(con, schema: str, tablas: dict) -> None:
    """Índice único + RLS + GRANT SELECT para anon/authenticated (hub D3)."""
    con.execute(text(f'GRANT USAGE ON SCHEMA "{schema}" TO anon, authenticated'))
    for nombre, spec in tablas.items():
        cols = ", ".join(spec["indice"])
        idx = f"{nombre}_pk_idx"
        pol = f"{nombre}_select_anon"
        con.execute(text(
            f'CREATE UNIQUE INDEX IF NOT EXISTS "{idx}" '
            f'ON "{schema}"."{nombre}" ({cols})'))
        con.execute(text(
            f'ALTER TABLE "{schema}"."{nombre}" ENABLE ROW LEVEL SECURITY'))
        con.execute(text(f'DROP POLICY IF EXISTS "{pol}" ON "{schema}"."{nombre}"'))
        con.execute(text(
            f'CREATE POLICY "{pol}" ON "{schema}"."{nombre}" FOR SELECT '
            f'TO anon, authenticated USING (TRUE)'))
        con.execute(text(
            f'GRANT SELECT ON "{schema}"."{nombre}" TO anon, authenticated'))
        logger.info("  DB: índice único + RLS aplicados a %s.%s", schema, nombre)
    # Sin commit: la transacción la confirma el `eng.begin()` de cargar_tablas.
