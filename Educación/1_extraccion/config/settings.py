"""
Configuración central del pipeline de extracción de Educación · Canarias en Datos.

Rutas del proyecto, ventana temporal y endpoints de las fuentes.
Sigue la convención del resto de áreas (Vivienda, Salud Mental, Dependencia).
"""

from pathlib import Path

# ── Rutas del proyecto ──────────────────────────────────────────────────────
# config/settings.py -> 1_extraccion/ -> Educación/ -> CANARIAS EN DATOS/
BASE_DIR = Path(__file__).resolve().parents[1]          # Educación/1_extraccion
EDUCACION_DIR = BASE_DIR.parent                          # Educación
PROJECT_DIR = EDUCACION_DIR.parent                       # CANARIAS EN DATOS

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
LOGS_DIR = DATA_DIR / "logs"
QA_DIR = BASE_DIR / "qa" / "reports"

# Enlace inter-área: el gasto en educación / PIB se toma del área de Presupuestos.
PRESUPUESTOS_OUTPUTS = PROJECT_DIR / "Presupuestos" / "outputs"

for _d in (RAW_DIR, LOGS_DIR, QA_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# ── Ventana temporal ────────────────────────────────────────────────────────
# Año base del período activo (coherente con Presupuestos y CNED-2014). Ver
# Cuaderno_metodologico_educacion.docx §2.
YEAR_START = 2015

# ── Endpoints ───────────────────────────────────────────────────────────────
# Eurostat · API de difusión (JSON-stat 2.0), sin clave. Republica los datos
# regionales (NUTS-2 = CCAA) de la EPA española, desagregados por sexo.
EUROSTAT_BASE = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
)

# ── Parámetros de red ───────────────────────────────────────────────────────
HTTP_TIMEOUT = 60
HTTP_RETRIES = 3
HTTP_BACKOFF = 3          # segundos entre reintentos
USER_AGENT = "odesocan-canarias-en-datos/educacion-extraccion (investigacion@odesocan.org)"

# ── Esquema canónico de salida (formato largo/tidy) ─────────────────────────
SCHEMA = [
    "indicador",     # clave del indicador (p. ej. abandono_temprano)
    "bloque",        # A/B/C/D del cuaderno
    "fuente",        # Eurostat · <dataset> | Presupuestos · <archivo>
    "dataset",       # código de dataset/tabla de origen
    "ccaa",          # nombre canónico de la CCAA / territorio
    "ccaa_id",       # código INE 2 dígitos (00 = nacional)
    "nuts2",         # código NUTS-2 (ES70 = Canarias)
    "anio",          # año natural
    "sexo",          # total | hombres | mujeres
    "valor",         # valor numérico del indicador
    "unidad",        # % | %PIB | EUR ...
    "origen",        # real | proyeccion
    "extraido_en",   # timestamp ISO de la extracción
    "url_fuente",    # URL/fichero exacto de origen (trazabilidad auditable)
]
