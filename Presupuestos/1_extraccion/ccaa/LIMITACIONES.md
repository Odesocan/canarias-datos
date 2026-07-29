# Limitaciones transversales del pipeline de extracción

> Advertencias que aplican a **todas** las CCAA. Cada comunidad tiene además su
> propia ficha `limitaciones-<id3>.md` en su carpeta. Última revisión: 2026-07-01.

Estas limitaciones se descubrieron cargando la tabla canónica en la DB. Documentarlas
aquí evita que vuelvan a quedar invisibles (ver la retrospectiva en `logs/progreso.md`,
entradas del 2026-07-01).

## 1 · La certificación VERDE NO valida las magnitudes

El smoke (`tools/smoke_regresion_py.py`) certifica la **extracción** — filas ≥ 30, % de
concepto, nº de conceptos — pero **no comprueba**:

- los **totales / magnitudes** (un extractor puede duplicar el gasto y salir VERDE),
- la **transformación R** (re-derivación de concepto),
- los **valores finales** en `ced_presupuestos` (los `imp_<concepto>`).

**Consecuencia:** una CCAA puede estar VERDE y tener sanidad al doble, a la mitad, o en
NULL. Antes de dar por bueno un dato, valida su magnitud (p. ej. per cápita) y compáralo
con Hacienda (conciliación §2.6 del cuaderno — **pendiente**; el SGCIEF es la referencia
autoritativa y habría cazado casi todos los errores de golpe).

Rangos de sanidad razonables como guía: **~800-2200 €/habitante** (España ~1400-1800).

## 2 · Dos sistemas de concepto que pueden derivar (Python local ↔ R raíz)

- El **extractor Python** asigna concepto con el `correspondencias.yml` **LOCAL** de cada
  CCAA (`1_extraccion/ccaa/<id3>/correspondencias.yml`).
- La **transformación R** (`2_transformacion/transformacion.R`) **re-deriva** el concepto
  con el `correspondencias.yml` **RAÍZ** (`/correspondencias.yml`, sección `ccaa:`), cuyo
  matcher `.match_codigo` (`R/correspondencias.R`) exige frontera no-dígito salvo comodín `*`.

Si el raíz está desincronizado del local, R asigna NA y el concepto se pierde en la DB
aunque Python lo asignara bien. **Mitigación aplicada (2026-07-01):** fallback en la
transformación — cuando R queda NA pero Python asignó, se usa el de Python
(`regla="python_local_fallback"`; rescató 5028 filas en 148 CCAA-año). Aun así, **al añadir
o cambiar códigos, actualiza el raíz Y el local** (o el raíz quedará atrás).

## 3 · Doble conteo de transferencias internas (patrón recurrente)

El gasto sanitario/social suele financiarse en cadena: Consejería/Departament →
(transferencia interna) → Servicio de Salud (entidad aparte) → (entrega) → programas
asistenciales. Si el extractor suma **la transferencia Y la entrega**, duplica el gasto.

Casos detectados y resueltos: **pvc** (gasto + ingreso), **Cataluña** (transf. `415` +
entrega `411/412`), **Andalucía** (transf. `41H`/`12S` + entrega). **Riesgo latente:**
cualquier CCAA con Servicio de Salud como entidad separada (revisar Galicia, Madrid,
C. Valenciana…). Regla: identificar los programas de "transferencia interna / al Servicio
de Salud" y contar UNA sola vista (normalmente la transferencia = presupuesto consolidado
del ente), no las dos.

## 4 · El maestro R salta fuentes por hash (manifest)

`run_extraccion` (`1_extraccion/extraccion.R`) **salta** las fuentes cuyo sha256 ya está en
`logs/manifest.jsonl`, y esas filas **no entran al staging**. Combinado con un `TRUNCATE`
previo, produce cargas parciales (solo entran las fuentes nuevas/cambiadas). El cierre
(`outputs/cierre_*.sh`) **borra el manifest** para forzar re-parseo completo. Si cambias un
**extractor** (no el raw), el hash del raw no cambia → borra el manifest o no se re-parseará.

## 5 · Gotchas operativos

- **Locale:** el maestro R necesita locale **UTF-8** (`LANG=en_US.UTF-8`). Con `LC_ALL=C`,
  `readLines` peta al leer los acentos de `fuentes.yml` → "0 fuentes".
- **Unidades:** algunos PDF vienen en **miles de euros** (×1000), los CSV suelen estar en
  euros. Sanity-check de magnitud SIEMPRE.
- **`web_fetch` con PDF binario** devuelve cuerpo vacío (no es fallo); descarga con `urllib`.
- **No** cargar en la Supabase de **producción** (requiere `SUPABASE_URL` + `SUPABASE_SERVICE_KEY`);
  el smoke/cierre va a la DB local por PG directo.

## 6 · Cómo evitar que se repita (pendiente de implementar)

1. **Certificar la DB, no solo la extracción**: guardarraíles de magnitud (per cápita,
   continuidad interanual, NULL/0 por concepto) + conciliación §2.6 contra Hacienda.
2. **Una sola fuente de verdad de conceptos**: que R confíe en el concepto de Python por
   defecto, o generar el raíz *desde* los locales.
3. **Regla explícita de transferencias internas** en la consolidación.
4. **Baseline de regresión de valores** por `(ccaa, concepto, año)` que dispare alerta ante
   saltos ×2.
