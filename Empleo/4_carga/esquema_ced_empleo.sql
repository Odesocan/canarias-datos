-- ============================================================================
-- ced_empleo · esquema de distribución en canendatos (Canarias en Datos)
-- Alimenta la pieza D3 de Empleo (ced_empleo_global / ced_empleo_gen).
-- Patrón seguro de Dependencia: RLS ON + policy SELECT para anon/authenticated.
-- Aplicado el 2026-07-21 (migración create_ced_empleo_canendatos).
-- ============================================================================

-- 1) GLOBAL — 1 fila por CCAA·año (valor "Ambos géneros" / indicadores territoriales)
create table if not exists canendatos.ced_empleo_global (
  ccaa                  text    not null,
  ccaa_cod              text,
  periodo               integer not null,          -- año
  origen_q              text,                       -- real/proyeccion (indic. trimestrales EPA/ETCL)
  origen_a              text,                       -- real/proyeccion (indic. anuales EAES/alquiler)
  tasa_paro             double precision,
  tasa_actividad        double precision,
  tasa_empleo           double precision,
  horas_servicios       double precision,
  paro_juvenil          double precision,
  paro_larga_duracion   double precision,
  temporalidad          double precision,
  parcialidad           double precision,
  brecha_salarial       double precision,
  pct_alquiler_salario  double precision,
  primary key (ccaa, periodo)
);

-- 2) GEN — 1 fila por CCAA·año·género (indicadores con desglose por género)
create table if not exists canendatos.ced_empleo_gen (
  ccaa                  text    not null,
  ccaa_cod              text,
  periodo               integer not null,          -- año
  genero                text    not null,          -- hombre / mujer
  origen_q              text,
  origen_a              text,
  tasa_paro             double precision,
  tasa_actividad        double precision,
  tasa_empleo           double precision,
  paro_juvenil          double precision,
  paro_larga_duracion   double precision,
  temporalidad          double precision,
  parcialidad           double precision,
  pct_alquiler_salario  double precision,
  primary key (ccaa, periodo, genero)
);

-- 3) Lectura pública para el cliente web (anon key) — SOLO SELECT
grant select on canendatos.ced_empleo_global to anon, authenticated;
grant select on canendatos.ced_empleo_gen    to anon, authenticated;

-- 4) RLS activado + política de solo lectura (idéntico a ced_dependencia_*)
alter table canendatos.ced_empleo_global enable row level security;
alter table canendatos.ced_empleo_gen    enable row level security;

drop policy if exists ced_empleo_global_select_anon on canendatos.ced_empleo_global;
create policy ced_empleo_global_select_anon
  on canendatos.ced_empleo_global for select to anon, authenticated using (true);

drop policy if exists ced_empleo_gen_select_anon on canendatos.ced_empleo_gen;
create policy ced_empleo_gen_select_anon
  on canendatos.ced_empleo_gen for select to anon, authenticated using (true);
