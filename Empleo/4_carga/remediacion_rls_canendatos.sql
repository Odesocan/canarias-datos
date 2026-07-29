-- ============================================================================
-- REMEDIACIÓN RLS · schema canendatos  (REVISAR antes de ejecutar)
-- 16 tablas preexistentes tienen RLS desactivado: con la anon key cualquiera
-- puede LEER y MODIFICAR sus filas. Este script activa RLS y añade una política
-- de SOLO LECTURA (anon/authenticated), como en ced_empleo_* y ced_dependencia_*.
-- NO ejecutar a ciegas: revisa que ninguna app dependa de escritura vía anon.
-- ============================================================================
do $$
declare t text;
begin
  foreach t in array array[
    'ccaa_ref','ced_vivienda_global','ced_vivienda_gen','ced_saludmental',
    'all_forecasts','benefect_full','benpresaad_all','censo_ppd',
    'dashboard_indicators','dictsaad_all','pend_grado','pend_pia',
    'perf_ccaa_genero','perf_genero','solsaad_all','tiempo_espera'
  ] loop
    execute format('alter table canendatos.%I enable row level security;', t);
    execute format('drop policy if exists %I on canendatos.%I;', t||'_select_anon', t);
    execute format('create policy %I on canendatos.%I for select to anon, authenticated using (true);', t||'_select_anon', t);
  end loop;
end $$;
