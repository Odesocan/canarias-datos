# -*- coding: utf-8 -*-
"""
FASE 1 · EXTRACCIÓN — Alquiler desde Supabase (bd_odesocan)
Canarias en Datos · Sección Empleo · ODESOCAN

Extrae la serie de precio de alquiler (€/m²) por CCAA que ya alimenta la sección
Vivienda del proyecto, alojada en la base de datos Supabase `bd_odesocan`
(tabla `public.alquiler_historico_ccaa`, fuente Idealista). Es el insumo de
alquiler del **indicador 11** (% del salario dedicado al alquiler); el cálculo
final —y su desagregación por género vía el salario EAES— se hace en
`2_transformacion`.

CREDENCIALES (nunca se incrustan en el código):
    export SUPABASE_URL="https://kdpsjutsgvghdtzoskkg.supabase.co"
    export SUPABASE_SERVICE_KEY="<service_role_key>"   # secreto; NO lo subas al repo

  La tabla tiene RLS activado: la clave `anon`/publishable devuelve 0 filas.
  Se necesita la `service_role` (o una política SELECT para un rol dedicado).

Salidas:
    salida/alquiler_ccaa_mensual.parquet / .csv   → serie mensual cruda por CCAA
    salida/alquiler_ccaa_anual.parquet   / .csv   → media anual €/m² (alineada con
                                                    la frecuencia anual del salario)

Uso:
    python extraer_supabase.py                 # desde 2010
    python extraer_supabase.py --desde 2006    # toda la serie disponible
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

from territorio import detecta_territorio

BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "salida"

TABLA = "alquiler_historico_ccaa"
PAGINA = 1000  # PostgREST pagina por defecto; se recorre con Range


def _config() -> tuple[str, str]:
    url = os.environ.get("SUPABASE_URL", "https://kdpsjutsgvghdtzoskkg.supabase.co").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_KEY")
    if not key:
        raise SystemExit(
            "Falta la credencial. Exporta SUPABASE_SERVICE_KEY con la clave service_role "
            "(la tabla tiene RLS y la clave anon devuelve 0 filas)."
        )
    return url, key


def _descargar(url: str, key: str) -> pd.DataFrame:
    """Descarga toda la tabla vía PostgREST, paginando con cabeceras Range."""
    headers = {"apikey": key, "Authorization": f"Bearer {key}"}
    filas: list[dict] = []
    offset = 0
    while True:
        h = dict(headers)
        h["Range-Unit"] = "items"
        h["Range"] = f"{offset}-{offset + PAGINA - 1}"
        resp = requests.get(
            f"{url}/rest/v1/{TABLA}",
            params={"select": "comunidad,codigo_ccaa,periodo,mes,mes_nombre,precio_m2,"
                    "variacion_mensual,variacion_trimestral,variacion_anual,fecha_extraccion",
                    "order": "codigo_ccaa.asc,periodo.asc,mes.asc"},
            headers=h,
            timeout=60,
        )
        resp.raise_for_status()
        lote = resp.json()
        if not lote:
            break
        filas.extend(lote)
        if len(lote) < PAGINA:
            break
        offset += PAGINA
    return pd.DataFrame(filas)


def _enriquecer(df: pd.DataFrame) -> pd.DataFrame:
    """Añade territorio canónico, bandera de origen y metadatos de fuente.

    OJO: en esta tabla La Rioja llega con codigo_ccaa='26' (código de provincia),
    no '17' como en el INE. Por eso el territorio canónico se resuelve por NOMBRE
    con el diccionario de territorio.py, y el join con el salario debe hacerse por
    nombre canónico, no por el código de origen.
    """
    cod, nom = zip(*df["comunidad"].map(detecta_territorio)) if len(df) else ([], [])
    df = df.copy()
    df["territorio_cod"] = list(cod)
    df["territorio"] = list(nom)
    df["periodicidad"] = "mensual"
    df["origen"] = "real"
    df["fuente"] = "Idealista (vía Supabase bd_odesocan · sección Vivienda)"
    df["indicador_id"] = 11
    df["indicador"] = "Precio de alquiler (€/m²) — insumo del % salario en alquiler"
    return df


def extraer(desde_anyo: int = 2010) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url, key = _config()
    print(f"⇣ Descargando {TABLA} desde Supabase …")
    df = _descargar(url, key)
    df = df[df["periodo"] >= desde_anyo].reset_index(drop=True)
    df["precio_m2"] = pd.to_numeric(df["precio_m2"], errors="coerce")
    df = _enriquecer(df)

    # serie mensual cruda
    df.to_parquet(OUT_DIR / "alquiler_ccaa_mensual.parquet", index=False)
    df.to_csv(OUT_DIR / "alquiler_ccaa_mensual.csv", index=False, encoding="utf-8")

    # media anual (alineada con la frecuencia del salario EAES, anual)
    anual = (
        df.dropna(subset=["precio_m2"])
        .groupby(["territorio_cod", "territorio", "comunidad", "periodo"], as_index=False)
        .agg(precio_m2_medio_anual=("precio_m2", "mean"), n_meses=("precio_m2", "size"))
    )
    anual["precio_m2_medio_anual"] = anual["precio_m2_medio_anual"].round(2)
    anual = anual.rename(columns={"periodo": "anyo"})
    anual["origen"] = "real"
    anual["fuente"] = "Idealista (vía Supabase bd_odesocan · sección Vivienda)"
    anual.to_parquet(OUT_DIR / "alquiler_ccaa_anual.parquet", index=False)
    anual.to_csv(OUT_DIR / "alquiler_ccaa_anual.csv", index=False, encoding="utf-8")

    print(f"   ✓ mensual: {len(df):,} filas · {df['territorio'].nunique()} territorios · "
          f"{int(df['periodo'].min())}–{int(df['periodo'].max())}")
    print(f"   ✓ anual:   {len(anual):,} filas")
    print(f"Artefactos en: {OUT_DIR}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Extracción de alquiler CCAA desde Supabase (Empleo)")
    ap.add_argument("--desde", type=int, default=2010, help="Año de arranque (def. 2010)")
    args = ap.parse_args()
    extraer(desde_anyo=args.desde)


if __name__ == "__main__":
    main()
