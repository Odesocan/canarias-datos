"""
SIMULACRO · Extracción de un indicador MEFP desde EDUCAbase.

Prueba de concepto para verificar la viabilidad de capturar los 4 indicadores
que faltaban (idoneidad, graduación ESO, escolarización 0-2, gasto/alumno).

Resultado del sondeo: EDUCAbase es PC-Axis (Jaxi) y expone descargas directas
`csv_bd` (tidy) → NO se necesita nodriver/Playwright, basta `requests`.

Este simulacro extrae `idoneidad_15` de extremo a extremo y ejecuta unas
comprobaciones QA mínimas (cobertura CCAA, sexos, años, sondeo Canarias).

Uso:
    python simulacro_educabase.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pandas as pd

from config.settings import RAW_DIR
from config.comunidades import CCAA_OFICIALES
from extract import educabase
from utils.logger import setup_logger

logger = setup_logger()

OUT_DIR = RAW_DIR / "_simulacro"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    logger.info("=" * 64)
    logger.info("SIMULACRO EDUCAbase · indicador = idoneidad_15 (bloque C)")
    logger.info("=" * 64)

    filas = educabase.extraer("idoneidad_15", bloque="C")
    df = pd.DataFrame(filas)
    out = OUT_DIR / "simulacro_idoneidad_15.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    logger.info("Guardado: %s (%d filas)", out, len(df))

    # ── QA mínimo ────────────────────────────────────────────────────────────
    print("\n" + "─" * 64)
    print("VERIFICACIÓN QA DEL SIMULACRO")
    print("─" * 64)
    ccaa_of = df[df["ccaa"].isin(CCAA_OFICIALES)]["ccaa"].nunique()
    sexos = sorted(df["sexo"].unique())
    anios = sorted(df["anio"].dropna().unique())
    na = int(df["valor"].isna().sum())
    fuera = int(((df["valor"] < 0) | (df["valor"] > 100)).sum())
    dup = int(df.duplicated(["ccaa_id", "anio", "sexo"]).sum())
    print(f"Filas totales ............ {len(df)}")
    print(f"CCAA oficiales presentes . {ccaa_of}/17")
    print(f"Territorios distintos .... {df['ccaa'].nunique()} (incluye España/ciudades)")
    print(f"Sexos .................... {sexos}")
    print(f"Rango de años ............ {int(anios[0])}-{int(anios[-1])} ({len(anios)} cursos)")
    print(f"Valores NA ............... {na}")
    print(f"Valores fuera de [0,100] . {fuera}")
    print(f"Duplicados de clave ...... {dup}")

    print("\nSondeo Canarias · idoneidad a los 15 años (AMBOS SEXOS, últimos años):")
    can = df[(df["ccaa"] == "Canarias") & (df["sexo"] == "total")].sort_values("anio")
    for _, r in can[can["anio"] >= 2020].iterrows():
        print(f"   {int(r['anio'])}: {r['valor']:g} %")

    print("\nBrecha de género · Canarias, último año (esperado: mujeres > hombres):")
    ultimo = int(can["anio"].max())
    g = df[(df["ccaa"] == "Canarias") & (df["anio"] == ultimo)].set_index("sexo")["valor"]
    if {"hombres", "mujeres"}.issubset(g.index):
        print(f"   {ultimo}: hombres {g['hombres']:g} % · mujeres {g['mujeres']:g} % "
              f"· brecha {g['mujeres'] - g['hombres']:+.1f} pp")

    ok = (ccaa_of == 17 and set(sexos) >= {"total"} and na == 0 and fuera == 0 and dup == 0)
    print("\nVEREDICTO SIMULACRO:", "✅ VIABLE — csv_bd directo, sin navegador"
          if ok else "⚠️ revisar incidencias")
    print("url_fuente:", df["url_fuente"].iloc[0])


if __name__ == "__main__":
    main()
