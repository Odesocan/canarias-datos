-- ===========================================================================
-- 001_init_indices_rls.sql — Índices únicos + RLS para el hub D3 (Educación)
-- ===========================================================================
-- Cuaderno metodológico §8.7:
--   * Índice único (ccaa, periodo, origen)          en ced_educacion_global.
--   * Índice único (ccaa, periodo, genero, origen)  en ced_educacion_gen.
--   * Row Level Security con política SELECT abierta para 'anon'/'authenticated'.
--
-- carga.py aplica esto automáticamente tras el swap; este fichero permite
-- reaplicarlo a mano con psql si hiciera falta.
--
-- Uso:  psql "$DATABASE_URL" -v schema=canendatos -f 001_init_indices_rls.sql
-- ===========================================================================

\set ON_ERROR_STOP on
\if :{?schema}
\else
  \set schema canendatos
\endif

BEGIN;

GRANT USAGE ON SCHEMA :"schema" TO anon, authenticated;

-- 1. ced_educacion_global  (CCAA × periodo × origen) --------------------------
CREATE UNIQUE INDEX IF NOT EXISTS ced_educacion_global_pk_idx
  ON :"schema".ced_educacion_global (ccaa, periodo, origen);

ALTER TABLE :"schema".ced_educacion_global ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS ced_educacion_global_select_anon
  ON :"schema".ced_educacion_global;
CREATE POLICY ced_educacion_global_select_anon
  ON :"schema".ced_educacion_global
  FOR SELECT TO anon, authenticated USING (TRUE);
GRANT SELECT ON :"schema".ced_educacion_global TO anon, authenticated;

-- 2. ced_educacion_gen  (CCAA × periodo × género × origen) --------------------
CREATE UNIQUE INDEX IF NOT EXISTS ced_educacion_gen_pk_idx
  ON :"schema".ced_educacion_gen (ccaa, periodo, genero, origen);

ALTER TABLE :"schema".ced_educacion_gen ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS ced_educacion_gen_select_anon
  ON :"schema".ced_educacion_gen;
CREATE POLICY ced_educacion_gen_select_anon
  ON :"schema".ced_educacion_gen
  FOR SELECT TO anon, authenticated USING (TRUE);
GRANT SELECT ON :"schema".ced_educacion_gen TO anon, authenticated;

COMMIT;
