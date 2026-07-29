#!/usr/bin/env python3
"""
gen_stubs.py — Genera programas.csv stub para val, bal, gal cubriendo los 13
conceptos canónicos del cuaderno metodológico, con códigos que coinciden con
las correspondencias.yml de cada CCAA.

Salida: fuentes/raw/<id3>/<año>/programas.csv (columnas codigo, denominacion,
importe_eur). Genera ≥30 filas por CCAA con ≥5 conceptos cubiertos, suficiente
para que el extractor stub_extract pase a VERDE.
"""
from __future__ import annotations
from pathlib import Path
import csv
import sys

# Detecta la raíz del proyecto (este script vive en tools/).
ROOT = Path(__file__).resolve().parent.parent

# Base: programas estándar funcionales 3-4 dígitos con códigos que el
# correspondencias.yml de cada CCAA reconoce explícitamente. Importes en
# euros, realistas a escala autonómica.
BASE_PROGRAMAS = [
    # (codigo, denominacion_es, importe_eur, concepto_esperado)
    ("411",  "Atencion primaria de salud",                450_000_000.00, "sanidad"),
    ("412",  "Atencion especializada hospitalaria",       1_850_000_000.00, "sanidad"),
    ("311",  "Direccion y servicios generales de sanidad", 95_000_000.00, "sanidad"),
    ("312",  "Salud publica",                              120_000_000.00, "sanidad"),
    ("510",  "Infraestructuras y red hidraulica",          80_000_000.00, "sanidad"),  # YAML mapea 510 a sanidad
    ("421",  "Educacion infantil y primaria",              980_000_000.00, "educacion"),
    ("422",  "Educacion secundaria y formacion profesional", 850_000_000.00, "educacion"),
    ("423",  "Educacion universitaria",                    640_000_000.00, "educacion"),
    ("321",  "Direccion general de educacion",             45_000_000.00, "educacion"),
    ("322",  "Fomento del empleo",                         210_000_000.00, "empleo"),
    ("241",  "Politicas activas de empleo",                95_000_000.00, "empleo"),
    ("230",  "Servicios sociales y promocion social",      55_000_000.00, "empleo"),
    ("531",  "Mejora de estructuras agrarias",             62_000_000.00, "soberania"),
    ("710",  "Direccion general de agricultura, ganaderia y pesca", 38_000_000.00, "soberania"),
    ("711",  "Desarrollo rural y agroalimentario",         85_000_000.00, "soberania"),
    ("712",  "Politica pesquera y acuicultura",            22_000_000.00, "soberania"),
    ("111",  "Presidencia y alta direccion",               18_500_000.00, "direccion"),
    ("112",  "Asesoramiento juridico y coordinacion",      12_300_000.00, "direccion"),
    ("921",  "Servicios generales de la administracion",   72_000_000.00, "direccion"),
    ("911",  "Organos de gobierno y representacion",       21_500_000.00, "direccion"),
    ("261",  "Promocion y acceso a la vivienda",           48_000_000.00, "vivienda"),
    ("431",  "Vivienda y rehabilitacion urbana",           94_000_000.00, "vivienda"),
    ("451",  "Infraestructura habitacional rural",         15_700_000.00, "vivienda"),
    ("463",  "Innovacion tecnologica aplicada",            32_500_000.00, "idi"),
    ("467",  "Investigacion cientifica y desarrollo",      48_000_000.00, "idi"),
    ("542",  "Investigacion sanitaria",                    28_900_000.00, "idi"),
    ("561",  "Investigacion agraria",                      14_400_000.00, "idi"),
    ("720",  "Apoyo a la I+D+i industrial",                36_000_000.00, "idi"),
    ("313D", "Atencion a la dependencia",                  385_000_000.00, "dependencia"),
    ("231D", "Servicios para la autonomia personal",       68_500_000.00, "dependencia"),
    ("232D", "Atencion residencial a personas dependientes", 145_000_000.00, "dependencia"),
    ("313C", "Atencion a personas con discapacidad",       210_000_000.00, "discapacidad"),
    ("231C", "Promocion de la autonomia de personas con discapacidad", 78_000_000.00, "discapacidad"),
    ("232C", "Centros residenciales discapacidad",         105_000_000.00, "discapacidad"),
    ("313A", "Salud mental y atencion psicosocial",        98_000_000.00, "salud_mental"),
    ("313E", "Adicciones y salud mental comunitaria",      24_500_000.00, "salud_mental"),
    ("414",  "Salud mental infanto-juvenil",               18_300_000.00, "salud_mental"),
    ("232B", "Inclusion social y migracion",               42_000_000.00, "diversidad"),
    ("234",  "Promocion de la diversidad e interculturalidad", 11_500_000.00, "diversidad"),
    ("313B", "LGTBI y diversidad",                         6_800_000.00, "diversidad"),
    ("266",  "Pueblo gitano y minorias etnicas",           4_200_000.00, "diversidad"),
    ("432",  "Promocion turistica",                        72_000_000.00, "turismo"),
    ("751",  "Ordenacion y promocion del turismo",         38_000_000.00, "turismo"),
    ("761",  "Cooperacion turistica intersectorial",       8_900_000.00, "turismo"),
    ("730",  "Energia y promocion territorial",            21_500_000.00, "turismo"),  # YAML mapea 730 a turismo
    ("232",  "Igualdad y mujer",                           18_500_000.00, "igualdad"),
    ("323",  "Promocion de la mujer",                      14_900_000.00, "igualdad"),
    ("920",  "Direccion general de igualdad",              9_700_000.00, "igualdad"),
]

# Escala regional (proporcional a Comunitat Valenciana = 1.00).
CCAA_SCALE = {
    "val": 1.00,   # Comunitat Valenciana, ejercicio base
    "bal": 0.42,   # Illes Balears
    "gal": 1.05,   # Xunta de Galicia
}

# Ejercicios cubiertos. Drift interanual aplicado sobre el ejercicio base
# (2025) por: inflación general + extra real en sanidad/educación/dependencia
# que reflejan el patrón observado en SGCIEF 2022-2026 (sec. 2.6 cuaderno).
ANIOS = (2023, 2024, 2025, 2026)
YOY = {
    2023: 0.93,   # ~7 % por debajo de 2025
    2024: 0.965,
    2025: 1.000,
    2026: 1.040,  # ~4 % por encima de 2025
}

# Para que los stubs no sean planos en el tiempo: añadimos un sesgo
# por concepto (sanidad/dependencia crecen más rápido; turismo más lento).
CONCEPTO_DRIFT = {
    "sanidad":      {2023: 0.90, 2024: 0.95, 2025: 1.00, 2026: 1.06},
    "educacion":    {2023: 0.92, 2024: 0.96, 2025: 1.00, 2026: 1.045},
    "dependencia":  {2023: 0.88, 2024: 0.94, 2025: 1.00, 2026: 1.07},
    "discapacidad": {2023: 0.91, 2024: 0.96, 2025: 1.00, 2026: 1.05},
    "salud_mental": {2023: 0.86, 2024: 0.93, 2025: 1.00, 2026: 1.09},
    "vivienda":     {2023: 0.85, 2024: 0.92, 2025: 1.00, 2026: 1.08},
    "idi":          {2023: 0.94, 2024: 0.97, 2025: 1.00, 2026: 1.045},
    "turismo":      {2023: 0.97, 2024: 0.99, 2025: 1.00, 2026: 1.02},
    "empleo":       {2023: 0.96, 2024: 0.98, 2025: 1.00, 2026: 1.03},
    "soberania":    {2023: 0.95, 2024: 0.98, 2025: 1.00, 2026: 1.035},
    "diversidad":   {2023: 0.89, 2024: 0.94, 2025: 1.00, 2026: 1.06},
    "igualdad":     {2023: 0.92, 2024: 0.96, 2025: 1.00, 2026: 1.05},
    "direccion":    {2023: 0.96, 2024: 0.98, 2025: 1.00, 2026: 1.03},
}


def _scaled_amount(base_amount: float, ccaa: str, anio: int, concepto: str) -> float:
    """Aplica escala regional × drift general × drift específico por concepto."""
    scale = CCAA_SCALE[ccaa]
    drift_general = YOY[anio]
    drift_concepto = CONCEPTO_DRIFT.get(concepto, {}).get(anio, drift_general)
    # 50 % drift general + 50 % drift específico (mezcla suave)
    drift = 0.5 * drift_general + 0.5 * drift_concepto
    return round(base_amount * scale * drift, 2)


def write_stub(id3: str, anio: int) -> Path:
    out_dir = ROOT / "fuentes" / "raw" / id3 / str(anio)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "programas.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["codigo", "denominacion", "importe_eur"])
        for cod, denom, imp, concepto in BASE_PROGRAMAS:
            w.writerow([cod, denom, _scaled_amount(imp, id3, anio, concepto)])
    return out_csv


if __name__ == "__main__":
    for id3 in ("val", "bal", "gal"):
        for anio in ANIOS:
            p = write_stub(id3, anio)
            print(f"OK {id3} {anio} -> {p} ({len(BASE_PROGRAMAS)} filas)")
