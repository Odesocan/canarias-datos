#!/usr/bin/env python3
"""Redefine el concepto `diversidad` como LGTBI + migraciones + etnias.

Motivo (2026-07-27): `diversidad` se había convertido en un segundo cajón de
sastre, absorbiendo inclusión social genérica, atención a la infancia y
familia, cooperación internacional/desarrollo, e incluso deporte, cultura,
patrimonio histórico y promoción del idioma gallego (ext, gal) — hasta el
92 % del concepto en cat (820 M€ de "Inclusió Social i Lluita contra la
Pobresa") y el 100 % en clm/cnt/mad (ningún código real de diversidad).

Referencia conceptual (Cuaderno Metodológico, tablas 4 y 14): **"Diversidad
(LGTBI, migraciones, etnias)"**. Perímetro acordado: programas específicos y
explícitos de estos tres ejes. EXCLUIDOS: inclusión social genérica, atención
a la infancia/familia/juventud, dependencia, cooperación internacional /
ayuda al desarrollo genérica (no es migración de personas), deporte, cultura,
patrimonio, idioma. Emigración/apoyo a la diaspora SÍ cuenta (es "migraciones").

Mapeo por código exacto y por CCAA (mismo criterio que `redefinir_direccion.py`):
el código 313B, por ejemplo, es "Atención a la discapacidad" en Baleares y
"Emigración Asturiana" en Asturias — nunca por texto genérico.

Uso:
    python3 tools/redefinir_diversidad.py [--dry-run]
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

KEYWORDS_BASE = ["lgtbi", "lgbti", "migracion", "migración", "interculturalidad", "gitano"]

# id3 -> (codigos, keywords, nota)
LOCAL: dict[str, tuple[list[str], list[str], str]] = {
    "and": (["232B", "234", "313B", "266", "31J"], KEYWORDS_BASE,
            "Retirados 31G (Accion Comunitaria e Insercion, 210 M), 31P (Apoyo a "
            "Familias, 184 M) y 32E (Proyectos de Interes Social, 58 M): inclusion "
            "social generica, no LGTBI/migracion/etnias. Se queda 31J Coordinacion "
            "de Politicas Migratorias (10-11 M/anio, 2015-2026)."),
    "cat": (["232B", "234", "313B", "266", "316"], KEYWORDS_BASE,
            "Retirado 317 'Inclusio Social i Lluita contra Pobresa' (820 M, 92% del "
            "concepto): lucha contra la pobreza generica, no diversidad. Se queda "
            "316 'Igualtat i Respecte a la Diversitat' (78 M/anio)."),
    "val": (["313H00"], ["lgtbi", "lgbti", "migracion", "migración", "interculturalidad"],
            "Retirados 313C00 (Familia/Infancia, 73 M), 313E00 (Inclusion Social, "
            "348 M), 313K00 ('Instituto Valenciano de...', denominacion truncada en "
            "origen, no identificable con certeza), 313M00 (MRR, fondos europeos de "
            "recuperacion, no diversidad), '313.30' (legacy de 313C00), 134A00 "
            "(Cooperacion Internacional: ayuda al desarrollo, no migracion de "
            "personas). Se queda 313H00 'Diversidad' (18-22 M/anio, explicito)."),
    "can": (["232C", "313B", "234", "266", "231P"],
            ["lgtbi", "lgbti", "migración", "migracion", "interculturalidad", "gitano",
             "canarios en el exterior"],
            "Retirado 231I 'Fomento de la Inclusion Social' (102 M): inclusion "
            "generica. Retirado el keyword generico 'diversidad' (capturaba 456E "
            "'Biodiversidad', 14 M, por substring literal — el matcher Python no usa "
            "frontera de palabra). Se quedan 232C 'Planificacion y Promocion de la "
            "Diversidad' (explicito) y 231P 'Canarios en el exterior' (emigracion, "
            "mismo criterio que el 313B de Asturias)."),
    "mad": (["19015"],
            ["lgtbi", "lgbti", "migración", "migracion", "migrante", "interculturalidad", "gitano"],
            "Retirados los keywords 'infancia'/'familia'/'convivencia': capturaban "
            "19017 'D.G. Infancia, Familia y Fomento de la Natalidad' (206 M) y 19001 "
            "'S.G.T. Familia,Juventud y Asuntos Sociales' (66 M) — el 100% de "
            "diversidad en Madrid era esto, ningun codigo real. Anadido codigo "
            "explicito 19015 'D.G. de Inmigracion' (solo existe en 2015, 6 M; sin "
            "sucesor identificable en anios posteriores por el proxy-centro de "
            "Madrid — ver limitaciones-mad.md). 2016+ queda NULL estructural."),
    "clm": (["232B", "234", "313B", "266"], KEYWORDS_BASE,
            "Retirado 313E 'Atencion y Acompanamiento al Menor' (era el 100% del "
            "concepto, 59 M): atencion a la infancia, no diversidad. Castilla-La "
            "Mancha no tiene programa propio de LGTBI/migracion/etnias identificable "
            "— NULL estructural."),
    "cnt": (["234", "313B", "266"],
            ["lgtbi", "lgbti", "migración", "migracion", "interculturalidad", "gitano"],
            "Retirado 231C 'Atencion a la Infancia, Adolescencia y Familia' (era el "
            "100% del concepto, 14 M) y los keywords 'infancia'/'adolescencia' que lo "
            "capturaban. Cantabria no tiene programa propio de LGTBI/migracion/"
            "etnias identificable — NULL estructural."),
    "nav": (["23.2319"],
            ["lgtbi", "lgbti", "migración", "migracion", "inmigrantes",
             "integración de los inmigrantes", "integracion de los inmigrantes",
             "interculturalidad", "gitano"],
            "Retirados 23.2315 (Proteccion a la familia, 194 M), 23.2317 (Atencion a "
            "la infancia, 46 M), 23.2310 (Programacion general, 20 M), 23.2316 "
            "(Reinsercion social, 12 M), 23.2331 (Direccion y servicios, 10 M), "
            "23.2325 (Memoria y convivencia, 8 M) y sus keywords genericos "
            "('proteccion a la familia', 'servicios sociales', 'reinsercion social', "
            "'memoria y convivencia', etc.): eran el 98% del concepto, servicios "
            "sociales generales sin relacion con diversidad. Se queda 23.2319 "
            "'Integracion de los inmigrantes' (6-7 M/anio)."),
    "lar": (["2.3.2.1"],
            ["lgtbi", "lgbti", "migración", "migracion", "interculturalidad", "gitano",
             "exclusión social", "exclusion social"],
            "Retirados 2.3.2.4 (Infancia y Menores), 2.3.2.5 (PRESTACIONES DE LA "
            "DEPENDENCIA — literalmente el concepto dependencia, mal ubicado aqui) y "
            "2.3.2.6 (Servicios Comunitarios). Se queda 2.3.2.1 'Exclusion Social e "
            "Inmigracion' (8-10 M/anio; combina exclusion social con inmigracion en "
            "el mismo programa, es el mas cercano al perimetro acordado)."),
    "cym": (["231B08"], ["lgtbi", "lgbti", "migracion", "migración", "cooperación al desarrollo"],
            "Retirados 231B05 (Atencion a la infancia, 77 M) y 232A02 (Promocion y "
            "servicios juventud, 24 M). Se queda 231B08 'Migracion y Cooperacion al "
            "Desarrollo' (9 M/anio; combina migracion en el nombre del programa)."),
    "bal": (["313J", "316A", "232B", "234", "266"],
            ["lgtbi", "lgbti", "migracion", "migració", "immigrant", "interculturalidad",
             "diversitat", "drets civils"],
            "Retirado 232A 'Cooperacio internacional' (7,6 M): ayuda al desarrollo "
            "generica, no migracion de personas. Se quedan 313J 'Integracio social "
            "d'immigrants' y 316A 'Drets i diversitat'."),
}

# ext y gal usan override en la RAIZ (bloque ccaa), no yml local
RAIZ_CCAA: dict[str, tuple[list[str], list[str], str]] = {
    "Extremadura": (["253C"], ["lgtbi", "migracion", "interculturalidad", "gitano", "emigracion"],
                    "Retirados 252C (Cooperacion para el Desarrollo, 14 M, ayuda "
                    "generica), 253B (Promocion y Servicios a la Juventud, 7 M) y "
                    "271/272/273/274 (direccion de cultura, bibliotecas, museos, "
                    "promocion cultural, deporte — 78 M en total, NADA que ver con "
                    "diversidad). Se queda 253C 'Acciones en materia de Emigracion' "
                    "(0,9 M/anio)."),
    "Galicia": (["312C"], ["lgtbi", "migrac", "interculturalidad", "gitano"],
                "Retirados 313A (Servizos a xuventude, 17 M), 151 (Fomento da lingua "
                "galega, 11 M), 431/432/433/441 (direccion de cultura, bibliotecas/"
                "museos, patrimonio, deporte — 162 M en total, NADA que ver con "
                "diversidad). Se queda 312C 'Servizos sociais relativos as "
                "migracions' (22-25 M/anio, unico programa realmente de diversidad)."),
}


def bloque_diversidad(indent: int, codigos: list[str], keywords: list[str], nota: str) -> list[str]:
    p = " " * indent
    out = [f"{p}diversidad:"]
    cab = [
        f"{SELLO} — Diversidad (LGTBI, migraciones, etnias), per Cuaderno",
        "Metodologico tablas 4/14. Antes cajon de sastre: inclusion social",
        "generica, infancia/familia, cooperacion al desarrollo, deporte, cultura,",
        "patrimonio, idioma. Ver logs/progreso.md.",
    ]
    for ln in cab:
        out.append(f"{p}  # {ln}")
    for ln in _wrap(nota, 84):
        out.append(f"{p}  # {ln}")
    if codigos:
        out.append(f"{p}  codigos:")
        for c in codigos:
            out.append(f"{p}  - '{c}'")
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


def procesar_local(id3: str, codigos: list[str], keywords: list[str], nota: str, dry: bool) -> str:
    f = CCAA_DIR / id3 / "correspondencias.yml"
    lineas = f.read_text(encoding="utf-8").splitlines()
    idx = [i for i, l in enumerate(lineas) if re.match(r"^  diversidad:\s*$", l)]
    if not idx:
        return f"  ! {id3}: no se encontro el bloque `diversidad` en el yml local"
    nuevas = reemplazar_bloque(lineas, idx[0], 2, bloque_diversidad(2, codigos, keywords, nota))
    if not dry:
        shutil.copy2(f, f.with_suffix(".yml.bak_prediversidad_20260727"))
        f.write_text("\n".join(nuevas) + "\n", encoding="utf-8")
    return f"  ✓ {id3}: local → {codigos}"


def procesar_raiz(dry: bool) -> list[str]:
    lineas = RAIZ.read_text(encoding="utf-8").splitlines()
    msgs = []
    i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")
    for nombre, (codigos, keywords, nota) in RAIZ_CCAA.items():
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
        nuevo = bloque_diversidad(4, codigos, keywords, nota)
        dentro = [i for i in range(ini_ccaa, fin_ccaa)
                  if re.match(r"^    diversidad:\s*$", lineas[i])]
        if dentro:
            lineas = reemplazar_bloque(lineas, dentro[0], 4, nuevo)
            msgs.append(f"  ✓ raiz: {nombre} → diversidad sustituida ({codigos})")
        else:
            lineas = lineas[:fin_ccaa] + nuevo + lineas[fin_ccaa:]
            msgs.append(f"  ✓ raiz: {nombre} → diversidad insertada ({codigos})")
        i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")
    if not dry:
        shutil.copy2(RAIZ, RAIZ.with_suffix(".yml.bak_prediversidad_20260727"))
        RAIZ.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return msgs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    print("== correspondencias LOCALES ==")
    for id3, (cods, kws, nota) in LOCAL.items():
        print(procesar_local(id3, cods, kws, nota, args.dry_run))
    print("== correspondencias RAIZ (ccaa-block) ==")
    for m in procesar_raiz(args.dry_run):
        print(m)
    if args.dry_run:
        print("\n(dry-run: no se ha escrito nada)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
