"""
Etapa 4 · Carga · pipeline Educación · Canarias en Datos.

Toma las tablas modeladas (3_modelado), hace la validación final de publicación,
exporta la copia de distribución (CSV/XLSX) y, opcionalmente, carga a Supabase
con el patrón atómico staging+swap (Cuaderno §8.7).

Por seguridad, la escritura en base de datos está DESACTIVADA por defecto: hay
que pasar --with-db explícitamente (y tener las credenciales en el entorno o en
Educación/.Renviron). Sin --with-db solo valida y exporta localmente.

Uso:
    python carga.py                 # valida + exporta (sin tocar la BD)
    python carga.py --with-db       # además carga a Supabase (staging+swap)
    python carga.py --qa            # ejecuta el QA de carga al terminar
"""

import argparse
import sys

import pandas as pd

from config_carga import TABLAS, OUT_DIR, DB, db_configurada
from utils_carga import logger


def _leer(fuente):
    return pd.read_csv(fuente, sep=";", decimal=",", na_values=["NA"])


def _validar(nombre, df, indice):
    """Validación de publicación. Devuelve lista de incidencias (vacía = OK)."""
    inc = []
    faltan = [c for c in indice if c not in df.columns]
    if faltan:
        inc.append(f"{nombre}: faltan columnas clave {faltan}")
        return inc
    dup = int(df.duplicated(indice).sum())
    if dup:
        inc.append(f"{nombre}: {dup} filas duplicadas en clave {tuple(indice)}")
    if df[[c for c in indice if c != 'origen']].isna().any().any():
        inc.append(f"{nombre}: hay NA en columnas de clave")
    # 'origen' forma parte del índice ÚNICO; en Postgres los NULL se consideran
    # distintos, así que un NULL rompería la unicidad. Debe estar siempre presente.
    if "origen" in indice and (df["origen"].isna().any() or (df["origen"].astype(str).str.strip() == "").any()):
        inc.append(f"{nombre}: 'origen' con NULL/vacío (rompe el índice único)")
    ncc = df["ccaa"].nunique()
    if ncc != 17:
        inc.append(f"{nombre}: {ncc}/17 CCAA")
    return inc


def _exportar(nombre, df):
    df.to_csv(OUT_DIR / f"{nombre}.csv", sep=";", decimal=",", na_rep="NA", index=False)
    try:
        df.to_excel(OUT_DIR / f"{nombre}.xlsx", index=False)
    except Exception as e:  # noqa: BLE001
        logger.warning("xlsx %s: %s", nombre, e)


def ejecutar(with_db=False):
    logger.info("=" * 64)
    logger.info("CARGA · Educación · with_db=%s · schema=%s", with_db, DB["schema"])
    logger.info("=" * 64)

    preparadas, incidencias = {}, []
    for nombre, spec in TABLAS.items():
        if not spec["fuente"].exists():
            incidencias.append(f"{nombre}: no existe la fuente {spec['fuente'].name} "
                               "(ejecuta antes el modelado)")
            continue
        df = _leer(spec["fuente"])
        incidencias += _validar(nombre, df, spec["indice"])
        _exportar(nombre, df)
        preparadas[nombre] = {"df": df, "indice": spec["indice"]}
        logger.info("  %s: %d filas · %d cols · exportada a data/",
                    nombre, len(df), df.shape[1])

    if incidencias:
        for x in incidencias:
            logger.error("  VALIDACIÓN: %s", x)
        logger.error("Validación con %d incidencias: NO se carga a BD.", len(incidencias))
        return {"incidencias": incidencias, "cargado": False}

    logger.info("Validación de publicación: OK (%d tablas)", len(preparadas))

    if with_db:
        if not db_configurada():
            logger.error("--with-db activo pero faltan credenciales Supabase "
                         "(SUPABASE_HOST/USER/PASS en entorno o Educación/.Renviron). "
                         "No se carga.")
            return {"incidencias": ["sin credenciales"], "cargado": False}
        from supabase_loader import cargar_tablas
        cargar_tablas(preparadas, DB["schema"])
        logger.info("Carga a Supabase completada (staging+swap + índices/RLS).")
        return {"incidencias": [], "cargado": True}

    logger.info("Modo local (sin --with-db): tablas validadas y exportadas, BD intacta.")
    return {"incidencias": [], "cargado": False}


def main():
    p = argparse.ArgumentParser(description="Carga · pipeline Educación")
    p.add_argument("--with-db", action="store_true",
                   help="Cargar a Supabase (staging+swap). Requiere credenciales.")
    p.add_argument("--qa", action="store_true", help="Ejecutar el QA de carga")
    args = p.parse_args()
    res = ejecutar(args.with_db)
    if args.qa:
        import qa_carga
        qa_carga.run(with_db=args.with_db and res["cargado"])


if __name__ == "__main__":
    main()
