-- ============================================================================
-- Sanidad · esquema de distribución en canendatos (Canarias en Datos)
-- Tablas global_sanidad (género 'total') y gen_sanidad (hombres/mujeres).
-- Patrón seguro de la plataforma: RLS ON + policy SELECT para anon/authenticated.
-- Ejecutar UNA vez antes de la primera carga (run_carga usa DELETE+INSERT).
-- ============================================================================

create schema if not exists canendatos;

-- 1) GLOBAL — 1 fila por CCAA·año (género total; incluye indicadores de sistema)
create table if not exists canendatos.global_sanidad (
  ccaa                     text    not null,
  ccaa_cod                 text,
  periodo                  integer not null,          -- año
  origen                   text,                       -- real / proyeccion (fila con ≥1 celda proyectada)
  avs_65                   double precision,           -- años de vida saludable a los 65
  mort_cancer              double precision,           -- mortalidad prematura cáncer (tasa aj. /100k)
  mort_cardio              double precision,           -- mortalidad prematura cardiopatía isquémica
  mort_diabetes            double precision,           -- mortalidad prematura diabetes
  mort_ictus               double precision,           -- mortalidad prematura enf. vascular cerebral
  mort_epoc                double precision,           -- mortalidad prematura EPOC
  mort_evitable_idx        double precision,           -- índice mort. evitable (ratio; media histórica=1)
  mort_evitable_idx_0_100  double precision,           -- índice mort. evitable reescalado 0-100
  med_ae                   double precision,           -- médicos atención especializada /1000
  med_ap                   double precision,           -- médicos atención primaria /1000
  enf_ae                   double precision,           -- enfermería atención especializada /1000
  enf_ap                   double precision,           -- enfermería atención primaria /1000
  camas                    double precision,           -- camas hospitalarias en funcionamiento /1000
  gasto_farmacia_pct       double precision,           -- % del gasto sanitario en farmacia
  pct_pib_sanidad          double precision,           -- gasto sanitario autonómico / PIB (Presupuestos)
  imp_sanidad_eur          double precision,           -- importe gasto Sanidad presupuestado (€)
  pib_regional_eur         double precision,           -- PIB regional (€)
  espera_quir              double precision,           -- días de espera intervención quirúrgica
  espera_ae                double precision,           -- días de espera 1ª consulta atención especializada
  reingresos_psiq          double precision,           -- % reingresos urgentes psiquiátricos
  poblacion_total          double precision,           -- población total (denominador)
  -- El origen va en la clave: un año puede tener una fila real y otra
  -- proyectada, y cada indicador sólo tiene valor en la de su origen.
  primary key (ccaa, periodo, origen)
);

-- 2) GEN — 1 fila por CCAA·año·género (solo indicadores con desglose por género)
create table if not exists canendatos.gen_sanidad (
  ccaa                     text    not null,
  ccaa_cod                 text,
  periodo                  integer not null,
  genero                   text    not null,          -- hombres / mujeres
  origen                   text,
  avs_65                   double precision,
  mort_cancer              double precision,
  mort_cardio              double precision,
  mort_diabetes            double precision,
  mort_ictus               double precision,
  mort_epoc                double precision,
  mort_evitable_idx        double precision,
  mort_evitable_idx_0_100  double precision,
  reingresos_psiq          double precision,
  poblacion_total          double precision,
  primary key (ccaa, periodo, genero, origen)
);

-- 3) Lectura pública para el cliente web (anon key) — SOLO SELECT
grant select on canendatos.global_sanidad to anon, authenticated;
grant select on canendatos.gen_sanidad    to anon, authenticated;

-- 4) RLS activado + política de solo lectura (idéntico al resto de áreas)
alter table canendatos.global_sanidad enable row level security;
alter table canendatos.gen_sanidad    enable row level security;

drop policy if exists global_sanidad_select_anon on canendatos.global_sanidad;
create policy global_sanidad_select_anon
  on canendatos.global_sanidad for select to anon, authenticated using (true);

drop policy if exists gen_sanidad_select_anon on canendatos.gen_sanidad;
create policy gen_sanidad_select_anon
  on canendatos.gen_sanidad for select to anon, authenticated using (true);
