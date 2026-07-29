# -*- coding: utf-8 -*-
"""
FASE 2 · ORQUESTADOR — limpieza → consolidación
Canarias en Datos · Sección Empleo · ODESOCAN

Ejecuta las dos sub-fases en orden:
  A) limpieza    (limpieza.py)    → intermedio/*_limpio.parquet
  B) consolidar  (consolidar.py)  → salida/ced_empleo.csv (+ ancho anual)

Uso:
    python transformar.py
    python transformar.py --solo limpieza     # o --solo consolidar
"""
from __future__ import annotations

import argparse

import consolidar
import limpieza


def main() -> None:
    ap = argparse.ArgumentParser(description="Transformación (limpieza + join) — Empleo")
    ap.add_argument("--solo", choices=["limpieza", "consolidar"], default=None)
    args = ap.parse_args()

    if args.solo in (None, "limpieza"):
        limpieza.ejecutar()
        print()
    if args.solo in (None, "consolidar"):
        consolidar.ejecutar()


if __name__ == "__main__":
    main()
