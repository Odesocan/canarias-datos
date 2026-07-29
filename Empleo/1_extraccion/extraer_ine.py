# -*- coding: utf-8 -*-
"""
FASE 1 · EXTRACCIÓN — Fuentes INE (EPA, ETCL, EAES)
Canarias en Datos · Sección Empleo · ODESOCAN

Descarga las tablas verificadas del catálogo (catalogo.py) desde la API JSON del
INE y las vuelca en formato largo/tidy, sin transformar ni calcular indicadores
(eso corresponde a 2_transformacion). Produce, por cada tabla:

  raw/<slug>.json         → respuesta cruda de la API (traza de auditoría)
  salida/<slug>.parquet   → datos en formato largo (una fila por serie·periodo)
  salida/<slug>.csv       → misma tabla en CSV (interoperable con R/Power BI)

Y de forma global:

  salida/cobertura.csv    → reporte de cobertura por tabla (§8 hoja de ruta, paso 4)
  salida/manifiesto.json  → metadatos de la ejecución (fecha, versiones, filas)

Uso:
    python extraer_ine.py                 # extracción completa desde 2010
    python extraer_ine.py --desde 2015    # otra fecha de arranque
    python extraer_ine.py --sin-cache     # fuerza descarga (ignora cache local)

Requisitos: pandas, pyarrow  (ver requirements.txt).
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from catalogo import FuenteINE, catalogo_ine_unico
from ine_cliente import INEClient
from territorio import detecta_genero, detecta_territorio, parse_periodo

# --------------------------------------------------------------------------- #
# Rutas (relativas a la carpeta 1_extraccion)
# --------------------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"
OUT_DIR = BASE_DIR / "salida"
CACHE_DIR = BASE_DIR / ".cache_ine"

FUENTE_ETIQUETA = {
    "EPA": "INE · Encuesta de Población Activa (EPA)",
    "ETCL": "INE · Encuesta Trimestral de Coste Laboral (ETCL)",
    "EAES": "INE · Encuesta Anual de Estructura Salarial (EAES)",
}


def _tidy_desde_series(series: list[dict], fuente: FuenteINE, desde_anyo: int) -> pd.DataFrame:
    """Convierte la lista de series de una tabla en un DataFrame largo/tidy."""
    filas: list[dict] = []
    for serie in series:
        serie_cod = serie.get("COD")
        serie_nombre = serie.get("Nombre", "")
        unidad = serie.get("Unidad", {})
        unidad_nombre = unidad.get("Nombre") if isinstance(unidad, dict) else unidad
        escala = serie.get("Escala", {})
        escala_nombre = escala.get("Nombre") if isinstance(escala, dict) else escala

        cod_ter, territorio = detecta_territorio(serie_nombre)
        genero = detecta_genero(serie_nombre)
        # normaliza la denominación de género en el nombre de serie (tras la
        # detección, que necesita el texto literal "Ambos sexos" del INE)
        serie_nombre = serie_nombre.replace("Ambos sexos", "Ambos géneros")

        for punto in serie.get("Data", []):
            per = parse_periodo(punto)
            if per["anyo"] is None or per["anyo"] < desde_anyo:
                continue
            tipo_dato = punto.get("TipoDato", {})
            filas.append(
                {
                    "indicador_id": fuente.indicador_id,
                    "indicador": fuente.nombre,
                    "operacion": fuente.operacion,
                    "id_tabla": fuente.id_tabla,
                    "serie_cod": serie_cod,
                    "serie_nombre": serie_nombre,
                    "territorio_cod": cod_ter,
                    "territorio": territorio,
                    "genero": genero,
                    "anyo": per["anyo"],
                    "periodo": per["periodo"],
                    "periodicidad": per["periodicidad"],
                    "fecha": per["fecha"],
                    "valor": punto.get("Valor"),
                    "unidad": unidad_nombre,
                    "escala": escala_nombre,
                    "tipo_dato": tipo_dato.get("Nombre") if isinstance(tipo_dato, dict) else None,
                    "secreto": punto.get("Secreto", False),
                    "origen": "real",  # §7.6 bandera origen (proyección se añade en 3_modelado)
                    "fuente": FUENTE_ETIQUETA.get(fuente.operacion, f"INE · {fuente.operacion}"),
                }
            )
    df = pd.DataFrame(filas)
    return df


def extraer(desde_anyo: int = 2010, usar_cache: bool = True) -> dict:
    """Ejecuta la extracción de todas las tablas INE del catálogo."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    cliente = INEClient(cache_dir=CACHE_DIR)
    fecha_extraccion = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")

    cobertura: list[dict] = []
    manifiesto: dict = {
        "seccion": "Empleo",
        "proyecto": "Canarias en Datos · ODESOCAN",
        "fase": "1_extraccion",
        "fecha_extraccion_utc": fecha_extraccion,
        "desde_anyo": desde_anyo,
        "tablas": [],
    }

    for fuente in catalogo_ine_unico():
        etiqueta = f"[{fuente.operacion} · tabla {fuente.id_tabla}] {fuente.nombre}"
        print(f"⇣ Extrayendo {etiqueta} …")

        # La serie completa (sin nult); la cache del cliente evita redescargas.
        # El flag --sin-cache vacía la carpeta de cache antes de ejecutar.
        respuesta = cliente.datos_tabla(fuente.id_tabla, det=2)

        # volcado crudo
        raw_path = RAW_DIR / f"{fuente.slug}.json"
        with raw_path.open("w", encoding="utf-8") as fh:
            json.dump(respuesta, fh, ensure_ascii=False)

        if isinstance(respuesta, dict) and "__error__" in respuesta:
            print(f"   ✗ ERROR de descarga: {respuesta['__error__']}")
            cobertura.append(
                {"slug": fuente.slug, "id_tabla": fuente.id_tabla, "estado": "ERROR",
                 "filas": 0, "detalle": respuesta["__error__"]}
            )
            continue

        df = _tidy_desde_series(respuesta, fuente, desde_anyo)

        # salidas tidy
        parquet_path = OUT_DIR / f"{fuente.slug}.parquet"
        csv_path = OUT_DIR / f"{fuente.slug}.csv"
        df.to_parquet(parquet_path, index=False)
        df.to_csv(csv_path, index=False, encoding="utf-8")

        # métricas de cobertura
        n_filas = len(df)
        territorios = sorted(t for t in df["territorio"].dropna().unique())
        anyos = df["anyo"].dropna()
        na_valor = float(df["valor"].isna().mean()) if n_filas else 1.0
        cobertura.append(
            {
                "slug": fuente.slug,
                "operacion": fuente.operacion,
                "id_tabla": fuente.id_tabla,
                "indicador": fuente.nombre,
                "estado": "OK",
                "filas": n_filas,
                "n_series": df["serie_cod"].nunique(),
                "n_territorios": len(territorios),
                "incluye_canarias": "Canarias" in territorios,
                "anyo_min": int(anyos.min()) if n_filas else None,
                "anyo_max": int(anyos.max()) if n_filas else None,
                "periodicidad": fuente.periodicidad,
                "tasa_na_valor": round(na_valor, 4),
            }
        )
        manifiesto["tablas"].append(
            {"slug": fuente.slug, "operacion": fuente.operacion, "id_tabla": fuente.id_tabla,
             "tabla_nombre": fuente.tabla_nombre, "filas": n_filas}
        )
        print(f"   ✓ {n_filas:>7,} filas · {len(territorios)} territorios · "
              f"{cobertura[-1]['anyo_min']}–{cobertura[-1]['anyo_max']} · "
              f"Canarias={'sí' if cobertura[-1]['incluye_canarias'] else 'NO'}")

    # reportes globales
    cob_df = pd.DataFrame(cobertura)
    cob_df.to_csv(OUT_DIR / "cobertura.csv", index=False, encoding="utf-8")
    with (OUT_DIR / "manifiesto.json").open("w", encoding="utf-8") as fh:
        json.dump(manifiesto, fh, ensure_ascii=False, indent=2)

    print("\n── Resumen de cobertura ──")
    if not cob_df.empty:
        cols = ["slug", "id_tabla", "estado", "filas", "anyo_min", "anyo_max", "incluye_canarias"]
        print(cob_df[cols].to_string(index=False))
    print(f"\nArtefactos en: {OUT_DIR}")
    return {"cobertura": cobertura, "manifiesto": manifiesto}


def main() -> None:
    ap = argparse.ArgumentParser(description="Extracción INE de la sección Empleo (Canarias en Datos)")
    ap.add_argument("--desde", type=int, default=2010, help="Año de arranque de las series (def. 2010)")
    ap.add_argument("--sin-cache", action="store_true", help="Ignora la cache local y fuerza descarga")
    args = ap.parse_args()

    # si se pide sin cache, se vacía la carpeta de cache antes de ejecutar
    if args.sin_cache and CACHE_DIR.exists():
        for f in CACHE_DIR.glob("*.json"):
            f.unlink()

    extraer(desde_anyo=args.desde, usar_cache=True)


if __name__ == "__main__":
    main()
