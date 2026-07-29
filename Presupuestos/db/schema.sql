-- =============================================================
--  ODESOCAN — Canarias en Datos
--  Esquema PostgreSQL: presupuestos autonómicos
--  Versión: 2026-05-11 (refactor pipeline)
--
--  Decisiones (frente al schema anterior):
--   * pct_pib_nacional usa PIB nominal NACIONAL (en dim_ejercicio),
--     coherente con la fórmula del cuaderno.
--   * pct_pib_regional (2026-07-16): % del PIB REGIONAL de cada CCAA
--     (dim_ccaa_ejercicio.pib_regional_eur). Indicador comparable de
--     prioridad política — pivotado a pibreg_<concepto> en ced_presupuestos.
--     Los años sin dato del INE (p.ej. 2025-2026) se completan por bootstrap
--     en el modelado; pib_origen marca 'real'|'proyeccion'.
--   * poblacion se modela por (ccaa, ejercicio) → tabla
--     `dim_ccaa_ejercicio`, evitando per cápita con población congelada.
--   * fact_gasto incluye `capa` para distinguir Hacienda vs autonómica.
--   * Se mantiene fase=ejecucion para el roadmap Q3 2026.
-- =============================================================

CREATE SCHEMA IF NOT EXISTS presupuestos;

-- ------- Dimensiones ----------------------------------------

CREATE TABLE IF NOT EXISTS presupuestos.dim_ccaa (
    id_ccaa   CHAR(3)  PRIMARY KEY,            -- and, ara, ast, bal, can, ...
    nombre    TEXT     NOT NULL,
    regimen   TEXT     CHECK (regimen IN ('comun','foral')) DEFAULT 'comun',
    cod_ine   CHAR(2)
);

CREATE TABLE IF NOT EXISTS presupuestos.dim_concepto (
    id_concepto SERIAL PRIMARY KEY,
    clave       TEXT UNIQUE NOT NULL,
    nombre      TEXT NOT NULL,
    procedencia TEXT NOT NULL CHECK (procedencia IN ('funcion','seccion','programa','ente'))
);

CREATE TABLE IF NOT EXISTS presupuestos.dim_ejercicio (
    ejercicio       INTEGER PRIMARY KEY,
    estado          TEXT NOT NULL CHECK (estado IN ('proyecto','aprobado','prorrogado')) DEFAULT 'aprobado',
    pib_nominal_eur NUMERIC(20,2),
    ipc_indice      NUMERIC(8,4)
);

CREATE TABLE IF NOT EXISTS presupuestos.dim_capitulo (
    capitulo INTEGER PRIMARY KEY,
    nombre   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS presupuestos.dim_ccaa_ejercicio (
    id_ccaa     CHAR(3)  REFERENCES presupuestos.dim_ccaa(id_ccaa),
    ejercicio   INTEGER  REFERENCES presupuestos.dim_ejercicio(ejercicio),
    poblacion   NUMERIC(14,0),
    pib_regional_eur NUMERIC(20,2),
    PRIMARY KEY (id_ccaa, ejercicio)
);

-- ------- Manifiesto de fuentes ------------------------------

CREATE TABLE IF NOT EXISTS presupuestos.manifest (
    id              BIGSERIAL PRIMARY KEY,
    id_ccaa         CHAR(3)   REFERENCES presupuestos.dim_ccaa(id_ccaa),
    ejercicio       INTEGER   REFERENCES presupuestos.dim_ejercicio(ejercicio),
    capa            TEXT      CHECK (capa IN ('hacienda','autonomica')) NOT NULL DEFAULT 'autonomica',
    alias           TEXT      NOT NULL,
    tipo            TEXT      CHECK (tipo IN ('pdf','csv','xlsx','html','zip')),
    url             TEXT      NOT NULL,
    path_local      TEXT,
    sha256          CHAR(64),
    size_bytes      BIGINT,
    fecha_captura   TIMESTAMP DEFAULT NOW(),
    UNIQUE (id_ccaa, ejercicio, capa, alias)
);

-- ------- Hecho: gasto por concepto y CCAA -------------------

CREATE TABLE IF NOT EXISTS presupuestos.fact_gasto (
    id                BIGSERIAL PRIMARY KEY,
    id_ccaa           CHAR(3)  REFERENCES presupuestos.dim_ccaa(id_ccaa),
    id_concepto       INTEGER  REFERENCES presupuestos.dim_concepto(id_concepto),
    ejercicio         INTEGER  REFERENCES presupuestos.dim_ejercicio(ejercicio),
    capa              TEXT     CHECK (capa IN ('hacienda','autonomica')) NOT NULL DEFAULT 'autonomica',
    capitulo          INTEGER  REFERENCES presupuestos.dim_capitulo(capitulo),
    codigo_origen     TEXT,
    denominacion_origen TEXT,
    importe_eur       NUMERIC(20,2) NOT NULL,
    fase              TEXT CHECK (fase IN ('aprobado','prorrogado','proyecto','liquidacion','ejecucion')) DEFAULT 'aprobado',
    consolidacion     TEXT CHECK (consolidacion IN ('consolidado','sin_consolidar','no_aplica')) DEFAULT 'no_aplica',
    es_prorroga       BOOLEAN DEFAULT FALSE,
    estimado          BOOLEAN DEFAULT FALSE,
    fuente_id         BIGINT  REFERENCES presupuestos.manifest(id),
    origen            TEXT CHECK (origen IN ('real','imputado','proyeccion')) DEFAULT 'real',
    fecha_carga       TIMESTAMP DEFAULT NOW(),
    UNIQUE (id_ccaa, id_concepto, ejercicio, capa, capitulo, codigo_origen, fase)
);

CREATE INDEX IF NOT EXISTS idx_fg_ccaa_ej     ON presupuestos.fact_gasto (id_ccaa, ejercicio);
CREATE INDEX IF NOT EXISTS idx_fg_concepto_ej ON presupuestos.fact_gasto (id_concepto, ejercicio);
CREATE INDEX IF NOT EXISTS idx_fg_fase        ON presupuestos.fact_gasto (fase, ejercicio);
CREATE INDEX IF NOT EXISTS idx_fg_capa        ON presupuestos.fact_gasto (capa, ejercicio);

-- ------- Tabla canónica para el front ------------------------
-- Replicada con el shape común de la viz 3D (ced_<tema>).

CREATE TABLE IF NOT EXISTS presupuestos.ced_presupuestos (
    ccaa        TEXT NOT NULL,
    periodo     INTEGER NOT NULL,
    genero      TEXT NOT NULL DEFAULT 'total',
    origen      TEXT NOT NULL DEFAULT 'real',
    capa        TEXT NOT NULL DEFAULT 'autonomica',
    es_prorroga BOOLEAN DEFAULT FALSE,
    estimado    BOOLEAN DEFAULT FALSE,
    pib_regional_eur DOUBLE PRECISION,   -- PIB regional de la CCAA (nominal)
    pib_origen  TEXT                     -- 'real' | 'proyeccion' (bootstrap)
    -- Las columnas pivotadas (imp_*, pib_*, pibreg_*, pc_*, var_*) se crean por
    -- carga.R/ensure_supabase_table con tipo double precision. No las
    -- declaramos aquí para no congelar la lista de conceptos.
    --   imp_<c>    = importe nominal €        pib_<c>    = % PIB NACIONAL
    --   pibreg_<c> = % PIB REGIONAL (objetivo) pc_<c>     = € per cápita
);

CREATE UNIQUE INDEX IF NOT EXISTS ced_presupuestos_key_idx
    ON presupuestos.ced_presupuestos (ccaa, periodo, genero, origen, capa);

-- ------- Vistas materializadas (capa de comparación) ---------
-- mv_indicadores: 13 conceptos × 17 CCAA × ejercicios × capa
-- Indicadores ya unidos a dim_ejercicio (PIB nacional) y dim_ccaa_ejercicio (población).

DROP MATERIALIZED VIEW IF EXISTS presupuestos.mv_indicadores CASCADE;
CREATE MATERIALIZED VIEW presupuestos.mv_indicadores AS
SELECT
    c.id_ccaa,
    c.nombre AS ccaa,
    e.ejercicio,
    g.capa,
    k.clave        AS concepto_clave,
    k.nombre       AS concepto,
    k.procedencia,
    SUM(g.importe_eur)                                                              AS importe_eur,
    SUM(g.importe_eur) / NULLIF(e.pib_nominal_eur, 0) * 100                          AS pct_pib_nacional,
    SUM(g.importe_eur) / NULLIF(ce.poblacion, 0)                                     AS eur_per_capita,
    BOOL_OR(g.es_prorroga) AS prorrogado,
    BOOL_OR(g.estimado)    AS estimado
FROM presupuestos.fact_gasto      g
JOIN presupuestos.dim_ccaa        c USING (id_ccaa)
JOIN presupuestos.dim_concepto    k USING (id_concepto)
JOIN presupuestos.dim_ejercicio   e USING (ejercicio)
LEFT JOIN presupuestos.dim_ccaa_ejercicio ce
       ON ce.id_ccaa = c.id_ccaa AND ce.ejercicio = e.ejercicio
WHERE g.fase = 'aprobado'
GROUP BY c.id_ccaa, c.nombre, e.ejercicio, e.pib_nominal_eur,
         ce.poblacion, g.capa, k.clave, k.nombre, k.procedencia;

CREATE UNIQUE INDEX IF NOT EXISTS idx_mv_ind_ccaa_ej_concepto_capa
    ON presupuestos.mv_indicadores (id_ccaa, ejercicio, concepto_clave, capa);

DROP MATERIALIZED VIEW IF EXISTS presupuestos.mv_variacion CASCADE;
CREATE MATERIALIZED VIEW presupuestos.mv_variacion AS
SELECT
    a.id_ccaa, a.capa, a.concepto_clave, a.concepto, a.ejercicio,
    a.importe_eur AS importe_actual,
    b.importe_eur AS importe_anterior,
    (a.importe_eur - b.importe_eur) / NULLIF(b.importe_eur, 0) * 100 AS var_nominal_pct,
    a.pct_pib_nacional, a.eur_per_capita, a.prorrogado, a.estimado
FROM presupuestos.mv_indicadores a
LEFT JOIN presupuestos.mv_indicadores b
       ON  b.id_ccaa = a.id_ccaa
       AND b.capa = a.capa
       AND b.concepto_clave = a.concepto_clave
       AND b.ejercicio = a.ejercicio - 1;

CREATE UNIQUE INDEX IF NOT EXISTS idx_mv_var_ccaa_ej_concepto_capa
    ON presupuestos.mv_variacion (id_ccaa, ejercicio, concepto_clave, capa);
