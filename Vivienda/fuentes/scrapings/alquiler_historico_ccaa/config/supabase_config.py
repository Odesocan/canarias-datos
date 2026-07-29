"""
Configuración de conexión a Supabase y esquema de tabla.
Credenciales cargadas desde .env con python-dotenv.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Cargar .env desde la raíz del proyecto
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# ── Credenciales de Supabase ────────────────────────────────────────────────

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# ── Nombre de la tabla destino ──────────────────────────────────────────────

TABLE_NAME = "alquiler_historico_ccaa"

# ── Esquema SQL para crear la tabla en Supabase ─────────────────────────────

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS alquiler_historico_ccaa (
    id                      BIGSERIAL PRIMARY KEY,
    comunidad               TEXT NOT NULL,
    codigo_ccaa             CHAR(2),
    mes                     SMALLINT NOT NULL,
    periodo                 SMALLINT NOT NULL,
    mes_nombre              TEXT,
    precio_m2               NUMERIC(8, 2),
    variacion_mensual       NUMERIC(6, 2),
    variacion_trimestral    NUMERIC(6, 2),
    variacion_anual         NUMERIC(6, 2),
    fecha_extraccion        TIMESTAMPTZ DEFAULT NOW(),
    created_at              TIMESTAMPTZ DEFAULT NOW(),
    updated_at              TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(comunidad, mes, periodo)
);

-- Índices para consultas frecuentes
CREATE INDEX IF NOT EXISTS idx_hist_ccaa_comunidad ON alquiler_historico_ccaa (comunidad);
CREATE INDEX IF NOT EXISTS idx_hist_ccaa_periodo   ON alquiler_historico_ccaa (periodo);
CREATE INDEX IF NOT EXISTS idx_hist_ccaa_combined  ON alquiler_historico_ccaa (comunidad, periodo);
CREATE INDEX IF NOT EXISTS idx_hist_ccaa_codigo    ON alquiler_historico_ccaa (codigo_ccaa);

COMMENT ON TABLE alquiler_historico_ccaa IS
    'Evolución histórica del precio de alquiler por m² en las comunidades
     autónomas de España (17 CCAA + Ceuta + Melilla).
     Fuente: Idealista sala de prensa. Datos mensuales con variaciones.';
"""

# ── Configuración de batch para carga ───────────────────────────────────────

BATCH_SIZE = 200
UPSERT_ON_CONFLICT = "comunidad,mes,periodo"
