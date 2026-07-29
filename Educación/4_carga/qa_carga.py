"""
Análisis QA de la carga · pipeline Educación · Canarias en Datos.

Sobre las tablas de distribución (data/):
  · Esquema, unicidad de clave, cobertura territorial (17 CCAA) y temporal
  · Reparto real/proyección · ausencia de NA en columnas de clave
  · Checklist de preparación para publicación

Si se cargó a Supabase (--with-db), verifica además contra la BD:
  · Existencia de tabla, nº de filas, índice único y RLS activo.

Genera reports/qa_carga_<fecha>.md.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from config_carga import TABLAS, OUT_DIR, DB, db_configurada
from utils_carga import logger

QA_DIR = BASE_DIR / "reports"
QA_DIR.mkdir(parents=True, exist_ok=True)
OK, WARN, FAIL = "✅", "⚠️", "❌"
ESPERADO = {"ced_educacion_global": 204, "ced_educacion_gen": 612}
HORIZON_END = 2026   # último periodo esperado (horizonte de proyección)


def _check_tabla(nombre, indice):
    df = pd.read_csv(OUT_DIR / f"{nombre}.csv", sep=";", decimal=",", na_values=["NA"])
    per = sorted(df["periodo"].unique())
    checks = []
    esperado = ESPERADO.get(nombre)
    checks.append(("clave única", not df.duplicated(indice).any()))
    checks.append(("17 CCAA", df["ccaa"].nunique() == 17))
    checks.append((f"periodo arranca 2015 y llega a {HORIZON_END}",
                   per[0] == 2015 and per[-1] >= HORIZON_END))
    if esperado is not None:
        checks.append((f"nº filas = {esperado}", len(df) == esperado))
    clave_sin_origen = [c for c in indice if c != "origen"]
    checks.append(("sin NA en clave", not df[clave_sin_origen].isna().any().any()))
    checks.append(("columna origen presente", "origen" in df.columns))
    n_real = int((df["origen"] == "real").sum())
    n_proy = int((df["origen"] == "proyeccion").sum())
    return df, checks, (n_real, n_proy), per


def _verificar_db(nombre, indice, n_local):
    """Comprueba la tabla en Supabase: filas, índice, RLS."""
    from sqlalchemy import create_engine, text
    url = (f"postgresql+psycopg2://{DB['user']}:{DB['password']}"
           f"@{DB['host']}:{DB['port']}/{DB['dbname']}")
    eng = create_engine(url, connect_args={"sslmode": DB["sslmode"]})
    sch = DB["schema"]
    out = []
    with eng.connect() as con:
        n = con.execute(text(f'SELECT count(*) FROM "{sch}"."{nombre}"')).scalar()
        out.append((f"filas en BD = local ({n_local})", n == n_local))
        idx = con.execute(text(
            "SELECT 1 FROM pg_indexes WHERE schemaname=:s AND tablename=:t "
            "AND indexname=:i"), {"s": sch, "t": nombre, "i": f"{nombre}_pk_idx"}).first()
        out.append(("índice único presente", idx is not None))
        rls = con.execute(text(
            "SELECT relrowsecurity FROM pg_class c JOIN pg_namespace n "
            "ON n.oid=c.relnamespace WHERE n.nspname=:s AND c.relname=:t"),
            {"s": sch, "t": nombre}).scalar()
        out.append(("RLS activo", bool(rls)))
        # GRANT a anon: es el privilegio que gobierna la lectura del dashboard.
        grant = con.execute(text(
            "SELECT has_table_privilege('anon', :ft, 'SELECT')"),
            {"ft": f'"{sch}"."{nombre}"'}).scalar()
        out.append(("GRANT SELECT a anon", bool(grant)))
    return out


def run(with_db=False):
    fecha = datetime.now().strftime("%Y-%m-%d")
    L = ["# Informe QA · Carga · Educación · Canarias en Datos", ""]
    todo_ok = True
    resumen = []

    for nombre, spec in TABLAS.items():
        if not (OUT_DIR / f"{nombre}.csv").exists():
            L.append(f"## {nombre}\n\n{FAIL} No se ha exportado. Ejecuta carga.py.")
            todo_ok = False
            continue
        df, checks, (n_real, n_proy), per = _check_tabla(nombre, spec["indice"])
        db_checks = []
        if with_db and db_configurada():
            try:
                db_checks = _verificar_db(nombre, spec["indice"], len(df))
            except Exception as e:  # noqa: BLE001
                db_checks = [("verificación BD", False)]
                logger.warning("QA BD %s: %s", nombre, e)

        L.append(f"## {nombre}")
        L.append("")
        L.append(f"- Filas: **{len(df)}** · CCAA: {df['ccaa'].nunique()} · "
                 f"periodo {per[0]}-{per[-1]} · reales {n_real} / proyectadas {n_proy}")
        L.append("")
        L.append("| Comprobación | |")
        L.append("|---|:-:|")
        for etiqueta, ok in checks + db_checks:
            L.append(f"| {etiqueta} | {OK if ok else FAIL} |")
            todo_ok = todo_ok and ok
        L.append("")
        resumen.append((nombre, len(df), n_real, n_proy))

    veredicto = OK if todo_ok else FAIL
    cab = (f"> **Fecha:** {fecha}  ·  **Veredicto:** {veredicto}  ·  "
           f"**BD:** {'verificada' if with_db else 'no tocada (modo local)'}  ·  "
           f"**schema:** {DB['schema']}")
    L.insert(1, cab)
    L.insert(2, "")

    md_path = QA_DIR / f"qa_carga_{fecha}.md"
    md_path.write_text("\n".join(L), encoding="utf-8")
    logger.info("=" * 64)
    logger.info("QA carga · %s · %s", veredicto,
                " · ".join(f"{n}:{r}f" for n, r, _, _ in resumen))
    logger.info("Informe: %s", md_path)
    return {"ok": todo_ok, "md": str(md_path)}


if __name__ == "__main__":
    run()
