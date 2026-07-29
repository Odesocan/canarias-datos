"""
Configuración de la etapa de carga · pipeline Educación · Canarias en Datos.

Credenciales de Supabase (Postgres directo, para carga atómica staging+swap).
Se leen de variables de entorno o de un fichero .Renviron en la carpeta Educación
(mismo patrón que el resto de áreas: SUPABASE_HOST/PORT/DBNAME/USER/PASS/SCHEMA).
NO se guardan credenciales en el repo.

Las tablas se cargan al schema compartido `canendatos` (el que lee el hub D3),
igual que Salud Mental, Dependencia y Vivienda.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent            # 4_carga
EDUCACION_DIR = BASE_DIR.parent
MODELADO_DIR = EDUCACION_DIR / "3_modelado" / "data"
OUT_DIR = BASE_DIR / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def _cargar_renviron() -> None:
    """Vuelca un .Renviron (KEY=VALUE) de la carpeta Educación al entorno si existe."""
    for ruta in (EDUCACION_DIR / ".Renviron", BASE_DIR / ".env"):
        if ruta.exists():
            for linea in ruta.read_text(encoding="utf-8", errors="ignore").splitlines():
                linea = linea.strip()
                if not linea or linea.startswith("#") or "=" not in linea:
                    continue
                k, v = linea.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_cargar_renviron()

# ── Conexión ────────────────────────────────────────────────────────────────
DB = {
    "host": os.getenv("SUPABASE_HOST", ""),
    "port": os.getenv("SUPABASE_PORT", "5432"),
    "dbname": os.getenv("SUPABASE_DBNAME", "postgres"),
    "user": os.getenv("SUPABASE_USER", ""),
    "password": os.getenv("SUPABASE_PASS", ""),
    "schema": os.getenv("SUPABASE_SCHEMA", "canendatos"),
    "sslmode": os.getenv("SUPABASE_SSLMODE", "require"),
}


def db_configurada() -> bool:
    return bool(DB["host"] and DB["user"] and DB["password"])


# ── Tablas destino e índices únicos (clave del hub D3) ──────────────────────
TABLAS = {
    "ced_educacion_global": {
        "fuente": MODELADO_DIR / "ced_educacion_global.csv",
        "indice": ["ccaa", "periodo", "origen"],
    },
    "ced_educacion_gen": {
        "fuente": MODELADO_DIR / "ced_educacion_gen.csv",
        "indice": ["ccaa", "periodo", "genero", "origen"],
    },
}
