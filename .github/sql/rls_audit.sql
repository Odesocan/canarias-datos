-- ===========================================================================
-- rls_audit.sql — auditoría de Row Level Security sobre la Supabase real
-- ===========================================================================
-- Devuelve UNA FILA POR HALLAZGO, o ninguna si todo está correcto. Lo consume
-- .github/workflows/rls-audit.yml, que falla el job si aparece algún CRITICO.
--
-- Uso:
--   psql -v ON_ERROR_STOP=1 -v esquemas="canendatos" -t -A -F'|' -f rls_audit.sql
--
-- Formato de salida:  severidad|esquema.tabla|privilegios_de_anon
--
-- Qué se considera hallazgo: una tabla con permisos concedidos a anon o
-- authenticated Y con RLS desactivado.
--   CRITICO  incluye INSERT/UPDATE/DELETE/TRUNCATE -> escritura abierta con la
--            anon key, que es pública.
--   AVISO    solo SELECT -> lectura abierta. Los datos son públicos por diseño,
--            pero se aparta del estándar del proyecto (RLS + política SELECT).
--
-- Una tabla con RLS ACTIVO no se marca aunque tenga permisos de escritura: con
-- RLS activo manda la política y, si ninguna la permite, la escritura se deniega.
-- Es el caso de las tablas de `public` en este proyecto (RLS activo, 0 políticas).
--
-- Solo lee catálogos del sistema. No modifica nada.
-- ===========================================================================

with concedido as (
  select table_schema,
         table_name,
         array_agg(distinct privilege_type::text) as privs
  from information_schema.role_table_grants
  where grantee in ('anon', 'authenticated')
    and table_schema = any (string_to_array(:'esquemas', ','))
  group by table_schema, table_name
)
select case
         when g.privs && array['INSERT','UPDATE','DELETE','TRUNCATE']
         then 'CRITICO'
         else 'AVISO'
       end                                        as severidad,
       g.table_schema || '.' || g.table_name      as tabla,
       array_to_string(g.privs, ',')              as privilegios_anon
from concedido g
join pg_namespace n on n.nspname = g.table_schema
join pg_class     c on c.relnamespace = n.oid
                   and c.relname = g.table_name
                   and c.relkind = 'r'
where c.relrowsecurity = false
order by severidad, tabla;
