# -*- coding: utf-8 -*-
"""
FASE 1 · EXTRACCIÓN — Afiliación a la Seguridad Social (ficheros TGSS)
Canarias en Datos · Sección Empleo · ODESOCAN · INDICADOR 5

Lee los ficheros de afiliación media que publica la Seguridad Social
(Tesorería General - TGSS) y los vuelca en formato largo/tidy, filtrando a las
dos provincias canarias (Las Palmas y Santa Cruz de Tenerife).

DÓNDE CONSEGUIR LOS FICHEROS (decisión del usuario: fuente = ficheros SS):
  Portal SS → Estadísticas → Afiliación → "Afiliación Media mensual"
  https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8/EST10/EST290/EST292
  Descargar el/los Excel de distribución POR PROVINCIAS y colocarlos en:
      1_extraccion/fuentes_seg_social/
  (nivel insular por isla NO lo da la SS; para isla habría que usar ISTAC).

IMPORTANTE — a confirmar contra un fichero real:
  El layout de los Excel de la SS varía (fila de cabecera, nombre de hoja y de
  columnas). Este lector está parametrizado (ver CONFIG y los flags de CLI) y
  usa parse_numero_es (locale español, §7.5). Cuando dispongas de un fichero de
  muestra, ajusta CONFIG['col_provincia'] / CONFIG['col_valor'] y la hoja.

Salidas:
    salida/afiliacion_provincias.parquet / .csv

Uso:
    python extraer_seg_social.py                       # lee fuentes_seg_social/*.xlsx|*.csv
    python extraer_seg_social.py --hoja "Provincias"   # nombre de hoja Excel
    python extraer_seg_social.py --fila-cabecera 5     # fila (0-based) de cabecera
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from territorio import parse_numero_es

BASE_DIR = Path(__file__).resolve().parent
FUENTES_DIR = BASE_DIR / "fuentes_seg_social"
OUT_DIR = BASE_DIR / "salida"

# Provincias canarias (código INE de provincia) y variantes ortográficas
PROVINCIAS_CANARIAS = {
    "35": ("Las Palmas", ("las palmas", "palmas, las", "palmas de gran canaria")),
    "38": ("Santa Cruz de Tenerife", ("santa cruz de tenerife", "s/c de tenerife",
                                       "s. c. de tenerife", "sta. cruz de tenerife",
                                       "sc tenerife", "tenerife")),
}

# Parámetros del layout del fichero SS (ajustar contra un fichero real)
CONFIG = {
    "col_provincia": None,   # None = autodetectar la columna que contiene los nombres de provincia
    "col_valor": None,       # None = autodetectar la columna numérica de afiliados
    "hoja": 0,               # índice o nombre de hoja Excel
    "fila_cabecera": 0,      # fila (0-based) de la cabecera
}


def _norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c)).strip()


def _detecta_provincia(texto: str) -> tuple[str, str] | None:
    n = _norm(texto)
    for cod, (nombre, variantes) in PROVINCIAS_CANARIAS.items():
        if any(v in n for v in variantes):
            return cod, nombre
    return None


def _periodo_desde_nombre(nombre_fichero: str) -> tuple[int | None, int | None]:
    """Intenta inferir año y mes del nombre del fichero (p. ej. '..._2026_03.xlsx')."""
    m = re.search(r"(20\d{2})[-_ ]?(0[1-9]|1[0-2])", nombre_fichero)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.search(r"(20\d{2})", nombre_fichero)
    return (int(m.group(1)), None) if m else (None, None)


def _leer_fichero(path: Path, cfg: dict) -> pd.DataFrame:
    if path.suffix.lower() in (".xlsx", ".xls"):
        df = pd.read_excel(path, sheet_name=cfg["hoja"], header=cfg["fila_cabecera"], dtype=str)
    else:
        df = pd.read_csv(path, sep=None, engine="python", header=cfg["fila_cabecera"], dtype=str)

    col_prov = cfg["col_provincia"]
    if col_prov is None:  # autodetectar: columna con más coincidencias de provincia
        best, best_hits = None, 0
        for c in df.columns:
            hits = df[c].map(lambda x: bool(_detecta_provincia(x)) if pd.notna(x) else False).sum()
            if hits > best_hits:
                best, best_hits = c, hits
        col_prov = best
    if col_prov is None:
        return pd.DataFrame()

    col_val = cfg["col_valor"]
    if col_val is None:  # autodetectar: primera columna con valores numéricos parseables
        for c in df.columns:
            if c == col_prov:
                continue
            parsed = df[c].map(parse_numero_es)
            if parsed.notna().mean() > 0.5:
                col_val = c
                break

    anyo, mes = _periodo_desde_nombre(path.name)
    filas = []
    for _, row in df.iterrows():
        det = _detecta_provincia(row[col_prov]) if pd.notna(row[col_prov]) else None
        if not det:
            continue
        cod, nombre = det
        filas.append({
            "indicador_id": 5,
            "indicador": "Afiliación a la Seguridad Social",
            "provincia_cod": cod,
            "provincia": nombre,
            "territorio": "Canarias",
            "anyo": anyo,
            "mes": mes,
            "periodicidad": "mensual",
            "afiliados": parse_numero_es(row[col_val]) if col_val else None,
            "origen": "real",
            "fuente": "Seguridad Social · TGSS (Afiliación media mensual)",
            "fichero": path.name,
        })
    return pd.DataFrame(filas)


def extraer(cfg: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FUENTES_DIR.mkdir(parents=True, exist_ok=True)
    ficheros = sorted([*FUENTES_DIR.glob("*.xlsx"), *FUENTES_DIR.glob("*.xls"), *FUENTES_DIR.glob("*.csv")])
    if not ficheros:
        print(f"⚠ No hay ficheros en {FUENTES_DIR}.")
        print("  Descarga los Excel de afiliación por provincias de la Seguridad Social y colócalos ahí.")
        print("  Portal: Estadísticas → Afiliación → Afiliación Media mensual (distribución por provincias).")
        return

    partes = []
    for f in ficheros:
        try:
            df = _leer_fichero(f, cfg)
            print(f"  · {f.name}: {len(df)} filas de provincias canarias")
            partes.append(df)
        except Exception as exc:  # noqa: BLE001
            print(f"  ✗ {f.name}: error de lectura ({type(exc).__name__}: {exc}). "
                  "Ajusta CONFIG (hoja/fila_cabecera/columnas).")

    if not partes or all(p.empty for p in partes):
        print("⚠ No se extrajo ninguna fila. Revisa el layout del fichero y ajusta CONFIG.")
        return

    out = pd.concat(partes, ignore_index=True)
    out.to_parquet(OUT_DIR / "afiliacion_provincias.parquet", index=False)
    out.to_csv(OUT_DIR / "afiliacion_provincias.csv", index=False, encoding="utf-8")
    print(f"✓ {len(out):,} filas · {out['provincia'].nunique()} provincias · "
          f"{out['anyo'].min()}–{out['anyo'].max()}")
    print(f"Artefactos en: {OUT_DIR}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Extracción de afiliación SS por provincias (Empleo)")
    ap.add_argument("--hoja", default=None, help="Nombre o índice de hoja Excel")
    ap.add_argument("--fila-cabecera", type=int, default=None, help="Fila (0-based) de cabecera")
    ap.add_argument("--col-provincia", default=None, help="Nombre de la columna de provincia")
    ap.add_argument("--col-valor", default=None, help="Nombre de la columna de afiliados")
    args = ap.parse_args()

    cfg = dict(CONFIG)
    if args.hoja is not None:
        cfg["hoja"] = int(args.hoja) if args.hoja.isdigit() else args.hoja
    if args.fila_cabecera is not None:
        cfg["fila_cabecera"] = args.fila_cabecera
    if args.col_provincia is not None:
        cfg["col_provincia"] = args.col_provincia
    if args.col_valor is not None:
        cfg["col_valor"] = args.col_valor
    extraer(cfg)


if __name__ == "__main__":
    main()
