#!/usr/bin/env python3
"""
docx_a_correspondencias.py — Convierte Tablas_Correspondencias_CCAA.docx
en un bloque YAML que se inyecta en correspondencias.yml bajo la sección `ccaa:`.

Cada CCAA del Word es una tabla 14×5 con columnas:
  Concepto | Localizador (código) | Denominación | Variaciones | Procedencia

Salida: 1_extraccion/correspondencias_ccaa_dump.yml (consumible por
extracción manual o por el operador que mantenga correspondencias.yml).
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import OrderedDict

import yaml
from docx import Document

PROJECT = Path(__file__).resolve().parent.parent
DOCX = PROJECT / "1_extraccion" / "Tablas_Correspondencias_CCAA.docx"
OUT = PROJECT / "1_extraccion" / "correspondencias_ccaa_dump.yml"

# Mapeo Concepto-Texto → clave canónica usada en correspondencias.yml
CONCEPTO_KEY = {
    "Sanidad": "sanidad",
    "Educación": "educacion",
    "Educacion": "educacion",
    "Soberanía alimentaria": "soberania",
    "Soberania alimentaria": "soberania",
    "Soberanía": "soberania",
    "Dirección política": "direccion",
    "Direccion politica": "direccion",
    "Dirección": "direccion",
    "Vivienda": "vivienda",
    "Empleo": "empleo",
    "I+D+i": "idi",
    "I+D+I": "idi",
    "Dependencia": "dependencia",
    "Discapacidad": "discapacidad",
    "Salud mental": "salud_mental",
    "Diversidad": "diversidad",
    "Turismo": "turismo",
    "Igualdad": "igualdad",
}

# Mapeo Nombre largo CCAA → nombre canónico (debe coincidir con el lookup
# del pipeline R / R/ccaa_dictionary.R).
CCAA_KEY = {
    "Andalucía": "Andalucía",
    "Aragón": "Aragón",
    "Principado de Asturias": "Principado de Asturias",
    "Illes Balears": "Islas Baleares",
    "Canarias": "Canarias",
    "Cantabria": "Cantabria",
    "Castilla y León": "Castilla y León",
    "Castilla-La Mancha": "Castilla-La Mancha",
    "Cataluña / Catalunya": "Cataluña",
    "Cataluña": "Cataluña",
    "Extremadura": "Extremadura",
    "Galicia": "Galicia",
    "La Rioja": "La Rioja",
    "Comunidad de Madrid": "Comunidad de Madrid",
    "Región de Murcia": "Región de Murcia",
    "Comunidad Foral de Navarra": "Comunidad Foral de Navarra",
    "Euskadi / País Vasco": "País Vasco",
    "País Vasco": "País Vasco",
    "Comunitat Valenciana": "Comunidad Valenciana",
    "Comunidad Valenciana": "Comunidad Valenciana",
}

# Regex de códigos: capta tokens tipo "41A", "41A-41D", "010-110", "313.70",
# "412I", "31P", "75", "313", "010", "232E", etc.
CODIGO_TOKEN = re.compile(
    r"\b\d{2,3}[A-Z]?(?:\.\d{1,3})?\b"
)


def _expand_range(tok: str) -> list[str]:
    """Expande rangos del estilo '41A-41D' o '232C-232E' a [41A,41B,41C,41D]."""
    if "-" not in tok:
        return [tok]
    a, b = tok.split("-", 1)
    a, b = a.strip(), b.strip()
    m1 = re.match(r"^(\d+)([A-Z])$", a)
    m2 = re.match(r"^(\d+)([A-Z])$", b)
    if m1 and m2 and m1.group(1) == m2.group(1):
        n = m1.group(1)
        ca, cb = ord(m1.group(2)), ord(m2.group(2))
        return [f"{n}{chr(c)}" for c in range(ca, cb + 1)]
    return [a, b]


def parse_localizador(cell_text: str) -> list[str]:
    """Extrae lista limpia de códigos a partir del texto de la celda."""
    if not cell_text:
        return []
    # Normaliza separadores
    txt = cell_text.replace(",", " ").replace("/", " ").replace(";", " ")
    out = []
    # Primero capta secuencias con guion (rangos)
    for rng in re.findall(r"\d+[A-Z]?-\d+[A-Z]?", txt):
        out.extend(_expand_range(rng))
        txt = txt.replace(rng, " ")
    # Luego los tokens sueltos
    for tok in CODIGO_TOKEN.findall(txt):
        out.append(tok)
    # Dedupe preservando orden
    seen = set(); dedup = []
    for c in out:
        if c not in seen:
            seen.add(c); dedup.append(c)
    return dedup


def extract_keywords(denominacion: str, concepto_key: str) -> list[str]:
    """Heurística mínima de keywords: nombres propios de entes en la denominación
    (mayúsculas internas) + lemas frecuentes por concepto."""
    if not denominacion:
        return []
    txt = denominacion.lower()
    out = []
    # Tokens "Servicio X de Salud", "Instituto Y", "AGENCIA Z" detectables
    for ent in re.findall(r"servicio [a-z\s]{3,30} salud", txt):
        out.append(ent.strip())
    for ent in re.findall(r"instituto [a-z\s]{3,30}", txt):
        out.append(ent.strip())
    for ent in re.findall(r"agencia [a-z\s]{3,30}", txt):
        out.append(ent.strip())
    # Lemas obvios por concepto
    obvios = {
        "sanidad": ["sanidad","salud","sanitaria"],
        "educacion": ["educacion","ensenanza"],
        "salud_mental": ["salud mental"],
        "dependencia": ["dependencia"],
        "discapacidad": ["discapacidad","diversidad funcional"],
        "vivienda": ["vivienda"],
        "empleo": ["empleo","ocupacion"],
        "turismo": ["turismo"],
        "igualdad": ["igualdad","mujer"],
        "diversidad": ["lgtbi","migracion"],
        "soberania": ["agricultura","ganaderia","pesca"],
        "idi": ["investigacion","innovacion"],
        "direccion": ["presidencia","gobierno"],
    }
    for kw in obvios.get(concepto_key, []):
        if kw in txt and kw not in out:
            out.append(kw)
    return out[:6]


def parse_ccaa_table(header_text: str, content_table) -> tuple[str, dict] | None:
    ccaa_canon = CCAA_KEY.get(header_text.strip())
    if not ccaa_canon:
        return None
    if len(content_table.rows) < 2:
        return None
    # Asumimos header en row 0 y datos a partir de row 1
    bloque: dict[str, dict] = {}
    for row in content_table.rows[1:]:
        cells = [c.text.strip() for c in row.cells]
        if len(cells) < 5:
            continue
        concepto_txt, localizador, denominacion, _variaciones, _procedencia = cells[:5]
        concepto_key = CONCEPTO_KEY.get(concepto_txt.strip())
        if not concepto_key:
            continue
        codigos = parse_localizador(localizador)
        keywords = extract_keywords(denominacion, concepto_key)
        if not codigos and not keywords:
            continue
        entry = {}
        if codigos:
            entry["codigos"] = codigos
        if keywords:
            entry["keywords"] = keywords
        bloque[concepto_key] = entry
    return ccaa_canon, bloque


def main() -> int:
    if not DOCX.exists():
        print(f"ERROR: no existe {DOCX}", file=sys.stderr)
        return 1
    doc = Document(str(DOCX))
    out: "OrderedDict[str, dict]" = OrderedDict()

    tables = doc.tables
    i = 0
    while i < len(tables):
        if len(tables[i].rows) == 1 and len(tables[i].columns) == 1:
            header = tables[i].rows[0].cells[0].text.strip()
            if i + 1 < len(tables):
                parsed = parse_ccaa_table(header, tables[i + 1])
                if parsed:
                    ccaa, bloque = parsed
                    out[ccaa] = bloque
                i += 2
                continue
        i += 1

    payload = {"ccaa": {k: dict(v) for k, v in out.items()}}
    OUT.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True,
                                   default_flow_style=False, width=120),
                   encoding="utf-8")
    print(f"OK escrito {OUT} con {len(out)} CCAA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
