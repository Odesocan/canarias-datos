#!/usr/bin/env python3
"""Redefine el concepto `direccion` como DIRECCIÓN POLÍTICA (altos cargos del ejecutivo).

Motivo (2026-07-27): `direccion` se había convertido en un cajón de sastre que
absorbía deuda pública, justicia, gestión tributaria, transferencias a entes
locales, informática, medios de comunicación y parlamentos — hasta el 33 % del
presupuesto en val y el 29 % en cat.

Referencia conceptual: programa **912A "Dirección Política y Gobierno"** de Canarias,
replicado en cada consejería para retribuir a los altos cargos (verificado en el
Tomo 3 de 2024: 13 líneas, pp. 72-77, que suman los 30.926.843 € del resumen).

Perímetro acordado: **ejecutivo estricto** — dirección política, presidencia,
vicepresidencia, gabinetes y alta dirección. Se EXCLUYEN parlamento y actividad
legislativa, cámaras de cuentas y control externo, defensorías, consejos
consultivos, transparencia y relaciones exteriores. Todo lo demás sale de
`direccion` y queda SIN CONCEPTO (gasto no-social fuera del catálogo de 13).

El mapeo es **por código exacto y por CCAA**: el mismo código significa cosas
distintas en cada comunidad (`112A` es dirección en clm/ext/ast pero Tribunales de
Justicia en can). Se dejan las keywords VACÍAS a propósito, para que `direccion` no
vuelva a capturar por texto.

Uso:
    python3 tools/redefinir_direccion.py [--dry-run]
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

# id3 -> (nombre en el yml raíz, códigos de dirección política, nota)
MAPEO: dict[str, tuple[str, list[str], str]] = {
    "and": ("Andalucía", [],
            "NULL ESTRUCTURAL: Andalucía no publica programa de direccion politica. "
            "El unico candidato, 11A D.S.G. Presidencia, es la direccion administrativa de "
            "UN departamento y su serie es inestable (61,8 M en 2015, 620,9 M en 2025, 87,4 M "
            "en 2026, con numeros pegados a la denominacion). No es asimilable a 912A."),
    "ara": ("Aragón", ["1121"],
            "1121 PRESIDENCIA Y ORGANOS DE LA PRESIDENCIA (12/12 anios, 2,2-3,0 M). "
            "Se excluye 1211 Servicios Generales de Presidencia (D.S.G. de departamento)."),
    "ast": ("Principado de Asturias", ["112A", "112H", "112I"],
            "112A SECRETARIA GENERAL TECNICA Y GABINETE TECNICO (2015-2025), "
            "112H APOYO A LA VICEPRESIDENCIA (2020-2026), "
            "112I GABINETE Y OFICINA ECONOMICA (2026, releva a 112A). Cobertura 12/12."),
    "bal": ("Islas Baleares", ["121A"],
            "121A Serveis/Direccio generals de la Presidencia del Govern (12/12, 3,2-4,4 M). "
            "Se excluye 121B (D.S.G. de la Conselleria de Presidencia, 47 M) y 912A/912B, que "
            "en Baleares son soporte financiero a consells insulars y ajuntaments."),
    "can": ("Canarias", ["912A"],
            "912A DIRECCION POLITICA Y GOBIERNO (12/12, 12,4-33,6 M). ES LA REFERENCIA del "
            "concepto: programa horizontal replicado en cada consejeria para los altos cargos. "
            "Se excluyen 912B/C (D.S.G. Presidencia/Vicepresidencia), 912D/E (asistencia "
            "tecnica), 912G (relaciones con el Parlamento), 912H (oficina en Madrid) y "
            "912L (Parlamento y entes estatutarios)."),
    "cat": ("Cataluña", ["112"],
            "112 IMPULS I COORDINACIO DE L'ACCIO DE GOVERN (12/12, 0,1-3,5 M). "
            "Sale de direccion el 911 DEUTE PUBLIC (9.350 M), que era el 62 % del concepto."),
    "clm": ("Castilla-La Mancha", ["112A"],
            "112A DIRECCION Y SERVICIOS GENERALES DE LA PRESIDENCIA (12/12, 12,8-21,8 M). "
            "Castilla-La Mancha no separa la direccion politica del ejecutivo por debajo de "
            "este nivel: es el programa mas estrecho disponible."),
    "cnt": ("Cantabria", ["912M"],
            "912M PRESIDENCIA DEL GOBIERNO DE CANTABRIA (12/12). OJO: salto 2019->2020 "
            "(1,9 -> 8,7 M) por cambio de perimetro del programa en el origen."),
    "cym": ("Castilla y León", ["912A01", "912A02"],
            "912A01 PRESIDENCIA DE LA JUNTA (12/12, 1,0-1,8 M) y 912A02 VICEPRESIDENCIA "
            "(2023-2024). DESVIACION deliberada respecto del borrador, que proponia 921A01 "
            "Dir.y Serv.G.Presidencia (13-22 M): 921A01 es la D.S.G. del departamento, mas "
            "ancha que el perimetro acordado. 912A01/02 es el equivalente estricto."),
    "ext": ("Extremadura", ["112A"],
            "112A DIRECCION Y ADMINISTRACION DE PRESIDENCIA (12/12, 5,8-11,7 M). "
            "Sale de direccion el 121A AMORTIZACION Y GASTOS FINANCIEROS DE LA DEUDA (960 M), "
            "que era el 82 % del concepto."),
    "gal": ("Galicia", ["111A"],
            "111A PRESIDENCIA DA XUNTA DE GALICIA (12/12, 3,4-7,0 M). Sale de direccion el "
            "911A DEBEDA PUBLICA (1.511 M) y el 811B transferencias a entidades locais."),
    "lar": ("La Rioja", ["1.8.1.1", "1.1.2.1"],
            "1.8.1.1 ACTIVIDAD ALTA DIRECCION (2017-2026) y 1.1.2.1 GABINETE DEL PRESIDENTE "
            "(2015-2016, esquema funcional antiguo). Juntos dan 12/12. Codigos ENTRECOMILLADOS: "
            "sin comillas YAML los lee como float y nunca casan."),
    "mad": ("Comunidad de Madrid", ["3001"],
            "3001 PRESIDENCIA DE LA COMUNIDAD DE MADRID (12/12, 1,1-1,7 M). Se excluye 11001 "
            "S.G.T. de Presidencia (40-191 M), que es la secretaria general tecnica de un "
            "departamento entero. Madrid extrae por CENTRO, no por programa."),
    "mur": ("Región de Murcia", ["112E"],
            "112E SERVICIOS GRALES SECRETARIA GRAL DE LA PRESIDENCIA (2020-2026, 0,5-0,7 M). "
            "2015-2019 quedan NULL: antes de 2020 Murcia solo publica 112A DIRECCION Y "
            "SERVICIOS GENERALES, cuya serie es inestable (64,4 M en 2015, 6,5 M en 2017)."),
    "nav": ("Comunidad Foral de Navarra", ["91.9121"],
            "91.9121 Alta direccion / Gobierno de Navarra (12/12, 0,4-0,6 M). Se excluyen "
            "91.9112 actividad legislativa, 91.9113 control externo y 91.9122 alto asesoramiento."),
    "pvc": ("País Vasco", ["1217"],
            "1217 Retribuciones de Altos Cargos (12/12, 2,2-4,8 M). AVISO: en pvc las "
            "denominaciones estan DESALINEADAS (el extractor toma el nombre de la primera "
            "partida, no el del programa), asi que 'Retribuciones de Altos Cargos' aparece "
            "tambien en 3121 con 1.495 M y en 2223 con 753 M. Mapear SOLO por codigo."),
    "val": ("Comunidad Valenciana", ["121B00", "121.2"],
            "121B00 Alta Direccion y Servicios (2024-2026) y su codigo legacy '121.2' "
            "(2015-2023). Juntos dan 12/12. Sale de direccion el 011A00 Servicio de la Deuda "
            "(7.948 M), que era el 80 % del concepto. '121.2' ENTRECOMILLADO obligatoriamente."),
}


def bloque_direccion(indent: int, codigos: list[str], nota: str) -> list[str]:
    """Construye el bloque YAML de `direccion` con su comentario de trazabilidad."""
    p = " " * indent
    out = [f"{p}direccion:"]
    cab = [
        f"{SELLO} — Direccion politica (altos cargos del ejecutivo).",
        "Antes era un cajon de sastre: deuda, justicia, tributos, transferencias a",
        "entes locales, informatica, medios y parlamentos. Referencia: programa 912A",
        "de Canarias 'Direccion Politica y Gobierno', replicado en cada consejeria.",
        "Perimetro: ejecutivo estricto (presidencia, vicepresidencia, gabinetes, alta",
        "direccion). EXCLUIDOS parlamento, control externo, defensorias, consejos",
        "consultivos y transparencia. Keywords VACIAS a proposito: mapeo por codigo",
        "exacto para que no vuelva a capturar por texto. Ver logs/progreso.md.",
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
    out.append(f"{p}  keywords: []")
    return out


def _wrap(texto: str, ancho: int) -> list[str]:
    palabras, linea, out = texto.split(), "", []
    for w in palabras:
        if len(linea) + len(w) + 1 > ancho:
            out.append(linea)
            linea = w
        else:
            linea = f"{linea} {w}".strip()
    if linea:
        out.append(linea)
    return out


def reemplazar_bloque(lineas: list[str], inicio: int, indent: int, nuevo: list[str]) -> list[str]:
    """Sustituye el bloque que empieza en `inicio` (y sus hijos) por `nuevo`."""
    fin = inicio + 1
    while fin < len(lineas):
        ln = lineas[fin]
        if ln.strip() and not ln.startswith(" " * (indent + 1)):
            break
        fin += 1
    # arrastra los comentarios inmediatamente anteriores al bloque
    ini = inicio
    while ini > 0 and lineas[ini - 1].strip().startswith("#") and \
            len(lineas[ini - 1]) - len(lineas[ini - 1].lstrip()) >= indent:
        ini -= 1
    return lineas[:ini] + nuevo + lineas[fin:]


def procesar_local(id3: str, codigos: list[str], nota: str, dry: bool) -> str:
    f = CCAA_DIR / id3 / "correspondencias.yml"
    lineas = f.read_text(encoding="utf-8").splitlines()
    idx = [i for i, l in enumerate(lineas) if re.match(r"^  direccion:\s*$", l)]
    if not idx:
        return f"  ! {id3}: no se encontro el bloque `direccion` en el yml local"
    nuevas = reemplazar_bloque(lineas, idx[0], 2, bloque_direccion(2, codigos, nota))
    if not dry:
        shutil.copy2(f, f.with_suffix(".yml.bak_predireccion_20260727"))
        f.write_text("\n".join(nuevas) + "\n", encoding="utf-8")
    return f"  ✓ {id3}: local → {len(codigos)} codigo(s) {codigos or '(NULL estructural)'}"


def procesar_raiz(dry: bool) -> list[str]:
    lineas = RAIZ.read_text(encoding="utf-8").splitlines()
    msgs = []

    # 1 · vaciar el patrón GLOBAL de direccion (indent 2, dentro de `patrones:`)
    i_pat = next(i for i, l in enumerate(lineas) if l == "patrones:")
    idx = [i for i in range(i_pat, len(lineas))
           if re.match(r"^  direccion:\s*$", lineas[i])]
    if idx:
        vacio = bloque_direccion(2, [], (
            "PATRON GLOBAL VACIADO: el mismo codigo significa cosas distintas en cada CCAA "
            "(112A es direccion en clm/ext/ast pero Tribunales de Justicia en can), asi que "
            "direccion se define SOLO en los bloques por comunidad de la seccion `ccaa`."))
        lineas = reemplazar_bloque(lineas, idx[0], 2, vacio)
        msgs.append("  ✓ raiz: patrones.direccion vaciado (mapeo solo por CCAA)")

    # 2 · bloque por CCAA (indent 4, dentro de `ccaa:`)
    i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")
    for id3, (nombre, codigos, nota) in MAPEO.items():
        pos = [i for i in range(i_ccaa, len(lineas))
               if re.match(rf"^  {re.escape(nombre)}:\s*$", lineas[i])]
        if not pos:
            msgs.append(f"  ! raiz: no encuentro el bloque de CCAA '{nombre}' ({id3})")
            continue
        ini_ccaa = pos[0]
        fin_ccaa = ini_ccaa + 1
        while fin_ccaa < len(lineas):
            if lineas[fin_ccaa].strip() and not lineas[fin_ccaa].startswith("   "):
                break
            fin_ccaa += 1
        nuevo = bloque_direccion(4, codigos, nota)
        dentro = [i for i in range(ini_ccaa, fin_ccaa)
                  if re.match(r"^    direccion:\s*$", lineas[i])]
        if dentro:
            lineas = reemplazar_bloque(lineas, dentro[0], 4, nuevo)
            msgs.append(f"  ✓ raiz: {nombre} → direccion sustituida ({len(codigos)} cod.)")
        else:
            lineas = lineas[:fin_ccaa] + nuevo + lineas[fin_ccaa:]
            msgs.append(f"  ✓ raiz: {nombre} → direccion insertada ({len(codigos)} cod.)")
        i_ccaa = next(i for i, l in enumerate(lineas) if l == "ccaa:")
    if not dry:
        shutil.copy2(RAIZ, RAIZ.with_suffix(".yml.bak_predireccion_20260727"))
        RAIZ.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return msgs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    print("== correspondencias LOCALES ==")
    for id3, (_n, cods, nota) in MAPEO.items():
        print(procesar_local(id3, cods, nota, args.dry_run))
    print("== correspondencias RAIZ ==")
    for m in procesar_raiz(args.dry_run):
        print(m)
    if args.dry_run:
        print("\n(dry-run: no se ha escrito nada)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
