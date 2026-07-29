#!/usr/bin/env python3
"""Redefine el concepto `igualdad` como Instituto de la Mujer / Igualdad-VG.

Motivo (2026-07-27): auditoría línea a línea (columna `regla` de
`gasto_detalle.rds`) reveló que `igualdad` capturaba sistemáticamente
programas de JUVENTUD (código `323A`/`232A2` en el esquema funcional de
varias CCAA es "Juventud", no "Igualdad" — solo `323B`/`232A1` es mujer/
igualdad) a través de tres mecanismos: (a) el patrón GLOBAL `codigos:
['232','323','920']` actúa como PREFIJO en R (regla de frontera de dígito)
y cuela cualquier `232X`/`323X`/`920X` sin override más específico; (b)
overrides de RAÍZ mal puestos (`ast`, `bal`, `clm`, `mur` tenían '323A'
explícito); (c) comodines `232*`/`323*` en ymls LOCALES (`cym`, `mur`).
Además Cataluña usaba código completamente equivocado: `232`/`233`
("Cooperació al desenvolupament") en vez de `322` ("Polítiques de Dones",
el programa real, encontrado 12/12 años).

Referencia conceptual (Cuaderno Metodológico, tablas 4 y 14): **"Igualdad:
Ente (Instituto Mujer/Igualdad) o programa Igualdad/VG (violencia de
género)"**. Nota del propio cuaderno: Cantabria, Castilla y León, La Rioja,
Murcia y Valencia NO tienen ente independiente, así que su dato viene de
programa, no de organismo.

Uso:
    python3 tools/redefinir_igualdad.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CCAA_DIR = ROOT / "1_extraccion" / "ccaa"
RAIZ = ROOT / "correspondencias.yml"
SELLO = "REDEFINIDO 2026-07-27"

# id3 -> (codigos, keywords, nota) para el yml LOCAL. None = no tocar el local.
LOCAL: dict[str, tuple[list[str], list[str], str] | None] = {
    "can": (["232", "232B", "920"],
            ["igualdad", "igualdad de oportunidades", "mujer", "mujeres",
             "violencia de género", "violencia de genero", "promoción de la igualdad",
             "promocion de la igualdad", "instituto de la mujer"],
            "Retirado 232A 'Promoc. y Fomento Calidad de Vida personas jovenes' (5,7 M): "
            "es juventud, no igualdad. Retirados los keywords 'jóvenes'/'jovenes'/"
            "'juventud' que lo capturaban."),
    "cat": (["322"],
            ["igualdad", "igualtat", "mujer", "dona", "violencia de genero", "berdintasun"],
            "Cambiado de ['232','323','920','233'] a '322': 232 es 'Cooperacio al "
            "Desenvolupament' (47,7 M, cooperacion internacional) y 323 es 'Accio "
            "Civica i Voluntariat' (4,9 M) — NINGUNO de los dos es igualdad. El "
            "programa real es 322 'Politiques de Dones' (7,3-15,2 M/anio, 12/12 anios), "
            "que estaba mal etiquetado como empleo. Corregido tambien en la raiz."),
    "clm": (["323B"],
            ["igualdad", "mujer", "violencia de género", "violencia de genero",
             "instituto de la mujer"],
            "Retirado 323A 'Promocion y Servicios de la Juventud' (2,8 M): es "
            "juventud. Retirados los comodines '232*'/'323*' (demasiado amplios) y "
            "los codigos genericos 232/323/920 (inertes o redundantes con el global)."),
    "cym": (["232A01"],
            ["igualdad", "mujer", "violencia de genero"],
            "Retirado 232A02 'Promoc. y serv. juventud' (23,7 M, el 61% del "
            "concepto): es juventud. Retirados los comodines '232*'/'323*'/'920*'."),
    "mur": (["313P", "323B"],
            ["igualdad", "mujer", "violencia de genero", "berdintasun", "emakume",
             "instituto de la mujer"],
            "Retirado 323A 'Promocion y Servicios a la Juventud' (8,1 M, el 33% del "
            "concepto): es juventud. Retirados los comodines '232*'/'323*'/'920*'."),
    "nav": (["23.2322", "23.2323"],
            ["lgtbi", "igualdad", "igualdad de oportunidades", "mujer", "mujeres",
             "mujeres y hombres", "violencia de género", "violencia de genero"],
            "Retirado 23.2321 'Promocion y servicios a la juventud' (3,8 M, el 36% "
            "del concepto): es juventud — estaba EXPLICITO en codigos y ADEMAS en "
            "los keywords ('juventud', 'servicios a la juventud'...). Se queda "
            "23.2322 'Igualdad de oportunidades entre mujeres y hombres' y 23.2323 "
            "'Actuaciones para la prevision integral de la violencia de genero'."),
    "val": (["323A00", "323B00", "'323.1'", "'313.8'"],
            ["igualdad", "igualtat", "mujer", "violencia de genero", "violencia sobre"],
            "Retirado '323M00'/'323.99' (MRR, Mecanismo de Recuperacion — fondos "
            "europeos, no igualdad) y los comodines '323*'/'232*'/'920*' que lo "
            "capturaban junto con el resto. Codigos legacy '323.1' (Igualdad de "
            "Genero/Promocion Familias, ≤2023) y '313.8' (Igualdad en la Diversidad) "
            "explicitos, ENTRECOMILLADOS (YAML los lee como float si no)."),
    "bal": (["323C"],
            ["igualdad", "igualtat", "mujer", "dona", "violencia de genero", "berdintasun"],
            "Retirado 323A 'Proteccio i foment de la integracio... de la joventut' "
            "(3,2 M): es juventud. Retirado el comodin '323*' que lo capturaba junto "
            "con el generico '232' (inerte) y '920' (inerte)."),
    "ast": None,  # ya limpio (solo 323B), no toca el local
    "gal": None, "mad": None, "and": None, "lar": None,  # ya limpios
    "ara": None, "cnt": None, "ext": None, "pvc": None,  # fix solo en raiz o global
}

# id3 -> (nombre CCAA en raiz, codigos, keywords, nota). None = no tocar la raiz.
RAIZ_CCAA: dict[str, tuple[list[str], list[str], str] | None] = {
    "Aragón": (["3232", "3137"], [],
               "Cambiado de keywords-only ['igualdad','mujer'] a codigos explicitos: "
               "el keyword 'igualdad' tambien capturaba 3133 'Politica Integral de "
               "Apoyo a las Familias y de Igualdad' (5,9 M), un programa mixto "
               "familia+igualdad cuyo eje principal es apoyo a familias, no "
               "igualdad especificamente. Se quedan 3232 'Promocion de la Mujer' y "
               "3137 'Igualdad de Oportunidades'."),
    "Principado de Asturias": ([], [],
               "Retirado 323A 'Actividades y Servicios de la Juventud' (3,1 M): es "
               "juventud, no igualdad. El yml LOCAL ya tiene 323B correcto (14,8 M), "
               "asi que la raiz queda vacia (el local es suficiente)."),
    "Islas Baleares": ([], [],
               "Retirado 323A (mismo motivo que en el yml local, ver ahi): es "
               "juventud. El yml local ya cubre 323C correctamente."),
    "Castilla-La Mancha": ([], [],
               "Retirado 323A 'Promocion y Servicios de la Juventud': es juventud. "
               "El yml local ya cubre 323B correctamente."),
    "Cataluña": (["322"], [],
                 "Cambiado de ['232','233'] a '322' — ver nota del yml local para "
                 "el detalle completo del error."),
    "Región de Murcia": ([], [],
               "Retirado 323A 'Promocion y Servicios a la Juventud' (8,1 M, "
               "duplicado ademas en el yml local): es juventud. El yml local ya "
               "cubre 313P/323B correctamente."),
    "País Vasco": (["3221", "3223"], [],
                   "Cambiado el comodin '322*' por codigos explicitos: '322*' "
                   "capturaba tambien 3222 'Juventud' (65,5 M, el 72% del concepto "
                   "previo) junto con los 2 codigos genuinos, 3221 'Promocion de "
                   "Igualdad Oportunidades para la Mujer' y 3223 'Emakunde-Instituto "
                   "Vasco de la Mujer'."),
}


def bloque_igualdad(indent: int, codigos: list[str], keywords: list[str], nota: str) -> list[str]:
    p = " " * indent
    out = [f"{p}igualdad:"]
    cab = [
        f"{SELLO} — Igualdad: Instituto de la Mujer / programa Igualdad-VG, per",
        "Cuaderno Metodologico tablas 4/14. Antes capturaba programas de JUVENTUD",
        "(mismo prefijo 232/323 que igualdad en el esquema funcional de varias",
        "CCAA, pero '...A' es juventud y '...B' es mujer/igualdad). Ver logs/progreso.md.",
    ]
    for ln in cab:
        out.append(f"{p}  # {ln}")
    for ln in _wrap(nota, 84):
        out.append(f"{p}  # {ln}")
    if codigos:
        out.append(f"{p}  codigos:")
        for c in codigos:
            # los que ya vienen entrecomillados (p.ej. "'323.1'") se respetan tal cual
            out.append(f"{p}  - {c}" if c.startswith("'") else f"{p}  - '{c}'")
    else:
        out.append(f"{p}  codigos: []")
    if keywords:
        out.append(f"{p}  keywords:")
        for k in keywords:
            out.append(f"{p}  - '{k}'")
    else:
        out.append(f"{p}  keywords: []")
    return out


def _wrap(texto: str, ancho: int) -> list[str]:
    palabras, linea, out = texto.split(), "", []
    for w in palabras:
        if len(linea) + len(w) + 1 > ancho:
            out.append(linea); linea = w
        else:
            linea = f"{linea} {w}".strip()
    if linea:
        out.append(linea)
    return out


def reemplazar_bloque(lineas: list[str], inicio: int, indent: int, nuevo: list[str]) -> list[str]:
    fin = inicio + 1
    while fin < len(lineas):
        ln = lineas[fin]
        if ln.strip() and not ln.startswith(" " * (indent + 1)):
            break
        fin += 1
    ini = inicio
    while ini > 0 and lineas[ini - 1].strip().startswith("#") and \
            len(lineas[ini - 1]) - len(lineas[ini - 1].lstrip()) >= indent:
        ini -= 1
    return lineas[:ini] + nuevo + lineas[fin:]


def procesar_local(id3: str, cfg: tuple[list[str], list[str], str] | None, dry: bool) -> str:
    if cfg is None:
        return f"  · {id3}: local sin cambios (ya limpio)"
    codigos, keywords, nota = cfg
    f = CCAA_DIR / id3 / "correspondencias.yml"
    lineas = f.read_text(encoding="utf-8").splitlines()
    idx = [i for i, l in enumerate(lineas) if re.match(r"^  igualdad:\s*$", l)]
    if not idx:
        return f"  ! {id3}: no se encontro el bloque `igualdad` en el yml local"
    nuevas = reemplazar_bloque(lineas, idx[0], 2, bloque_igualdad(2, codigos, keywords, nota))
    if not dry:
        shutil.copy2(f, f.with_suffix(".yml.bak_preigualdad_20260727"))
        f.write_text("\n".join(nuevas) + "\n", encoding="utf-8")
    return f"  ✓ {id3}: local → {codigos}"


def procesar_raiz(dry: bool) -> list[str]:
    lineas = RAIZ.read_text(encoding="utf-8").splitlines()
    msgs = []
    i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")
    for nombre, cfg in RAIZ_CCAA.items():
        if cfg is None:
            msgs.append(f"  · raiz {nombre}: sin cambios")
            continue
        codigos, keywords, nota = cfg
        pos = [i for i in range(i_ccaa, len(lineas))
               if re.match(rf"^  {re.escape(nombre)}:\s*$", lineas[i])]
        if not pos:
            msgs.append(f"  ! raiz: no encuentro el bloque de CCAA '{nombre}'")
            continue
        ini_ccaa = pos[0]
        fin_ccaa = ini_ccaa + 1
        while fin_ccaa < len(lineas):
            if lineas[fin_ccaa].strip() and not lineas[fin_ccaa].startswith("   "):
                break
            fin_ccaa += 1
        nuevo = bloque_igualdad(4, codigos, keywords, nota)
        dentro = [i for i in range(ini_ccaa, fin_ccaa)
                  if re.match(r"^    igualdad:\s*$", lineas[i])]
        if dentro:
            lineas = reemplazar_bloque(lineas, dentro[0], 4, nuevo)
            msgs.append(f"  ✓ raiz: {nombre} → igualdad sustituida ({codigos})")
        else:
            lineas = lineas[:fin_ccaa] + nuevo + lineas[fin_ccaa:]
            msgs.append(f"  ✓ raiz: {nombre} → igualdad insertada ({codigos})")
        i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")

    # patrones GLOBAL: vaciar codigos (232/323/920 actuaban como prefijo en R,
    # colando 232A/323A/920X sin override especifico — mismo criterio que direccion)
    i_pat = next(i for i, l in enumerate(lineas) if l == "patrones:")
    idxg = [i for i in range(i_pat, len(lineas)) if re.match(r"^  igualdad:\s*$", lineas[i])]
    if idxg:
        vacio = bloque_igualdad(2, [], ["igualdad", "mujer", "violencia de genero",
                                        "berdintasun", "emakume", "instituto de la mujer"], (
            "PATRON GLOBAL: codigos vaciados. Los codigos '232'/'323'/'920' (sin "
            "sufijo) actuan como PREFIJO en R (regla de frontera de digito) y "
            "colaban 232A/323A/920X (tipicamente 'Juventud' en el esquema funcional "
            "de bastantes CCAA) para cualquier CCAA sin override mas especifico "
            "(cnt, ext). Cada CCAA define su propio codigo exacto en su bloque "
            "ccaa o en su yml local."))
        lineas = reemplazar_bloque(lineas, idxg[0], 2, vacio)
        msgs.append("  ✓ raiz: patrones.igualdad codigos vaciados (mapeo por CCAA)")

    if not dry:
        shutil.copy2(RAIZ, RAIZ.with_suffix(".yml.bak_preigualdad_20260727"))
        RAIZ.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return msgs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    print("== correspondencias LOCALES ==")
    for id3, cfg in LOCAL.items():
        print(procesar_local(id3, cfg, args.dry_run))
    print("== correspondencias RAIZ (ccaa-block + patron global) ==")
    for m in procesar_raiz(args.dry_run):
        print(m)
    if args.dry_run:
        print("\n(dry-run: no se ha escrito nada)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
