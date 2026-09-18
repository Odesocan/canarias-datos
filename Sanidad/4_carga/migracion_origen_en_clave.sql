-- =============================================================================
-- Sanidad · migración: el origen (real/proyección) pasa a formar parte de la
-- clave primaria de global_sanidad y gen_sanidad.
--
-- Antes: una fila por (ccaa, periodo[, genero]) con un único origen, marcada
-- entera como proyección en cuanto un indicador lo era. Ahora lo real y lo
-- proyectado de un mismo año van en filas distintas (4_carga/carga.R).
--
-- Se aplica una vez sobre las tablas existentes, ANTES de la primera carga con
-- el código nuevo. Las filas actuales ya son únicas por la clave nueva.
-- Idempotente: si la clave ya incluye origen, se reconstruye igual.
-- =============================================================================
begin;
alter table canendatos.global_sanidad drop constraint if exists global_sanidad_pkey;
alter table canendatos.global_sanidad add primary key (ccaa, periodo, origen);
alter table canendatos.gen_sanidad drop constraint if exists gen_sanidad_pkey;
alter table canendatos.gen_sanidad add primary key (ccaa, periodo, genero, origen);
commit;
