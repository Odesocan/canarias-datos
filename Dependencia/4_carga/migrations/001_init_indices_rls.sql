-- ===========================================================================
-- 001_init_indices_rls.sql -- Indices unicos + RLS para hub D3 Dependencia
-- ===========================================================================
-- Cuaderno metodologico v2 §11.6:
--   * Indice unico sobre (ccaa, fecha, origen) en ced_dependencia_global.
--   * Indice unico sobre (ccaa, fecha, genero, origen) en ced_dependencia_gen.
--   * Activar Row Level Security con politica SELECT abierta para 'anon'.
--
-- Pre-requisitos:
--   * Las tablas ya existen y han sido pobladas por el pipeline (carga.R).
--   * El schema por defecto es el indicado en la variable :"schema" (psql -v).
--
-- Uso:
--   psql "$DATABASE_URL" -v schema=saad -f 001_init_indices_rls.sql
-- ===========================================================================

\set ON_ERROR_STOP on

\if :{?schema}
\else
  \set schema saad
\endif

BEGIN;

-- ----------------------------------------------------------------------------
-- 1. ced_dependencia_global  (CCAA x fecha x origen)
-- ----------------------------------------------------------------------------

CREATE UNIQUE INDEX IF NOT EXISTS ced_dependencia_global_pk_idx
  ON :"schema".ced_dependencia_global (ccaa, fecha, origen);

ALTER TABLE :"schema".ced_dependencia_global ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS ced_dependencia_global_select_anon
  ON :"schema".ced_dependencia_global;

CREATE POLICY ced_dependencia_global_select_anon
  ON :"schema".ced_dependencia_global
  FOR SELECT
  TO anon, authenticated
  USING (TRUE);

GRANT SELECT ON :"schema".ced_dependencia_global TO anon, authenticated;

-- ----------------------------------------------------------------------------
-- 2. ced_dependencia_gen  (CCAA x fecha x genero x origen)
-- ----------------------------------------------------------------------------

CREATE UNIQUE INDEX IF NOT EXISTS ced_dependencia_gen_pk_idx
  ON :"schema".ced_dependencia_gen (ccaa, fecha, genero, origen);

ALTER TABLE :"schema".ced_dependencia_gen ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS ced_dependencia_gen_select_anon
  ON :"schema".ced_dependencia_gen;

CREATE POLICY ced_dependencia_gen_select_anon
  ON :"schema".ced_dependencia_gen
  FOR SELECT
  TO anon, authenticated
  USING (TRUE);

GRANT SELECT ON :"schema".ced_dependencia_gen TO anon, authenticated;

COMMIT;

-- ===========================================================================
-- Notas operativas
-- ===========================================================================
-- * carga.R hace DROP + RENAME atomico: tras cada ejecucion del pipeline,
--   esta migracion debe re-aplicarse para reinstalar indices y RLS sobre las
--   nuevas tablas. Patron recomendado: anadir un step "post-load SQL" en el
--   workflow GH Actions (ver hoja de ruta).
-- * El indice unico actua tambien como anti-duplicado: si compute_dashboard_-
--   indicators emitiera dos filas para la misma (ccaa, fecha, origen), la
--   carga fallaria con violacion de unicidad y el dashboard no se contaminaria.
