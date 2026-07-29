# -*- coding: utf-8 -*-
"""
FASE 1 · EXTRACCIÓN — Orquestador
Canarias en Datos · Sección Empleo · ODESOCAN

Ejecuta las tres vías de extracción en orden:
  1) INE  (EPA, ETCL, EAES)     → extraer_ine.py        [siempre disponible]
  2) Supabase (alquiler CCAA)   → extraer_supabase.py   [requiere SUPABASE_SERVICE_KEY]
  3) Seguridad Social (afiliac.)→ extraer_seg_social.py [requiere ficheros locales]

Cada vía es independiente: si una no tiene sus prerequisitos (credencial o
ficheros), se omite con un aviso y las demás continúan.

Uso:
    python extraer.py                 # todo lo disponible, desde 2010
    python extraer.py --desde 2015
    python extraer.py --solo ine      # ine | supabase | seg_social
"""
from __future__ import annotations

import argparse
import os
import traceback

import extraer_ine
import extraer_seg_social
import extraer_supabase


def _sep(titulo: str) -> None:
    print("\n" + "═" * 70)
    print(f"  {titulo}")
    print("═" * 70)


def run(desde: int, solo: str | None) -> None:
    # 1) INE
    if solo in (None, "ine"):
        _sep("1/3 · INE (EPA · ETCL · EAES)")
        extraer_ine.extraer(desde_anyo=desde, usar_cache=True)

    # 2) Supabase (alquiler)
    if solo in (None, "supabase"):
        _sep("2/3 · Supabase (alquiler CCAA — indicador 11)")
        if not (os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_KEY")):
            print("⚠ Omitido: falta SUPABASE_SERVICE_KEY en el entorno.")
        else:
            try:
                extraer_supabase.extraer(desde_anyo=desde)
            except Exception:  # noqa: BLE001
                print("✗ Error en la extracción de Supabase:")
                traceback.print_exc()

    # 3) Seguridad Social (afiliación)
    if solo in (None, "seg_social"):
        _sep("3/3 · Seguridad Social (afiliación — indicador 5)")
        extraer_seg_social.extraer(dict(extraer_seg_social.CONFIG))


def main() -> None:
    ap = argparse.ArgumentParser(description="Orquestador de la fase de extracción (Empleo)")
    ap.add_argument("--desde", type=int, default=2010, help="Año de arranque (def. 2010)")
    ap.add_argument("--solo", choices=["ine", "supabase", "seg_social"], default=None,
                    help="Ejecutar sólo una vía")
    args = ap.parse_args()
    run(desde=args.desde, solo=args.solo)


if __name__ == "__main__":
    main()
