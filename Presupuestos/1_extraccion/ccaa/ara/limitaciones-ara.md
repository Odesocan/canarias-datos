# Limitaciones conocidas — Aragón (ara)

> Advertencias de la extracción de Aragón. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `ara-pdf-program-total` (PDF `ingresos_gastos.pdf` / equivalente, una página por programa con `PROGRAMA <cod>` + `TOTAL PROGRAMA <importe>`) · Años: 2015-2026 · Estado global: 12 VERDE_PRAGM (~56-61 % concepto, 9-11 conceptos).

## Perímetro / decisiones de consolidación
- Clasificación funcional aragonesa; el extractor empareja la cabecera `PROGRAMA <codigo> <denom>` con su `TOTAL PROGRAMA <importe>` (una fila por programa). Códigos de 4 dígitos (o 4d + letra).
- Estándar (suma por programa), sin ajustes de doble conteo ni proxy. Muchos códigos funcionales de 4 dígitos se añadieron a mano al `correspondencias.yml` (38 a `direccion` para órganos institucionales 11xx-13xx, hacienda 61xx, transferencias `9111`…; `4211`/`4229` a educación) para subir la cobertura de 19,2 % a ~58 % sin tocar el extractor.

## Conceptos NO separables (NULL estructural por diseño)
- `dependencia`, `discapacidad`: sin códigos funcionales propios en el catálogo de Aragón (listas de códigos genéricas heredadas; no aparecen de forma estable en la serie). Solo emergen vía keyword si la denominación lo permite.
- `salud_mental` y `diversidad` solo aparecen cuando existen los programas funcionales reales: `4133` "SALUD MENTAL" (match exacto que gana al prefijo `41`→sanidad; separado el 2026-06-05) y `3241` "APOYO A LA INMIGRACIÓN" (diversidad). Por eso `salud_mental` solo figura desde 2024.

## Advertencias de calidad del dato
- **Doble conteo de sanidad — DETECTADO y CORREGIDO (2026-07-01).** El presupuesto sanitario se financia en dos secciones: el Departamento (sec 16 SANIDAD) presupuesta `4131` "Protección y promoción de la salud" (~2,1 B€) = la **transferencia** al Servicio Aragonés de Salud, y el SALUD (sec 52) presupuesta `4121` "Asistencia sanitaria" (~2,1 B€) = la **entrega**. El motor sumaba ambos → sanidad ~2× (3247 €/hab vs ~1600 reales), VERDE 12/12 sin detectarse (lo cazó la auditoría de magnitud). Fix: `extract.py` excluye `4131` (`_ARA_TRANSFER_SALUD`) y cuenta la entrega del SALUD + los programas propios del Departamento. Resultado: 1146-2015 €/hab, en banda.
- **FIX 2026-07-02 — educación y soberanía infra-extraídas por keyword-miss.** Los códigos del `correspondencias.yml` eran exactos de 3 díg. (`'421'`,`'712'`…) que NUNCA casan el código emitido de 4 díg., así que el mapeo dependía del keyword y se rompía con abreviaturas: `4222 "EDUC SECUNDARIA"` (526 M€/año, ~40 % de educación) iba a NULL desde 2020, y todo lo agrario (`7121/7123` "PRODUCCIÓN AGRARIA" 465 M, `5311`, `7161`) también. Corregido con prefijos reales `421*`+`422*`→educacion y `71*`+`5311`→soberania (+`4124/4132`→sanidad). Resultado: %concepto ~59→66 %; educación 2024 ~1,0→1,52 B, soberanía ~0,05→0,74 B. Sanidad intacta (baseline).
- **Pendiente (magnitud, no concepto):** el programa `3132` "Gestión y desarrollo de los SS" aparece DUPLICADO (sec-20 Departamento 456 M + sec-53 IASS 432 M = transferencia+entrega, mismo patrón que 4131) → infla el `total` ~4,6 %. Ambos quedan NULL (SS generales), no contamina conceptos; excluir la transferencia sec-20→IASS queda pendiente.
- Cobertura de concepto estructuralmente en la banda pragmática (~66 %): el presupuesto incluye mucho gasto no-social (deuda, dirección, industria, cultura) que queda correctamente sin concepto.
- Reclasificación aplicada (2026-06-05): el programa `4133` "SALUD MENTAL" estaba absorbido por sanidad (prefijo `41`) y ocultaba el concepto canónico propio; se movió a `salud_mental` (match exacto).

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos VERDE_PRAGM.
- **2016 (resuelto 2026-07-01):** el raw canónico `ingresos_gastos.pdf` apuntaba antes a la Ley de Presupuestos publicada en el BOA (texto legislativo, sin líneas `TOTAL PROGRAMA`) y el motor devolvía 0 filas (ERROR). Se sustituyó por `Presupuesto de ingresos 2016.pdf` del ZIP histórico (pese al nombre, contiene el detalle por programa): 162 filas, 10 conceptos, total 7.216 M€. La Ley BOA se conserva como `ley_presupuestos_boa22.pdf`.

## Notas de uso
- Valida magnitudes por per cápita y contra Hacienda; la certificación VERDE no comprueba totales.
- No esperes desglose de dependencia/discapacidad como programas propios en Aragón: son NULL estructural (van dentro de programas genéricos de servicios sociales).
- Al añadir códigos, actualiza también el `correspondencias.yml` RAÍZ (que usa R), no solo el local.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py ara` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, post-fix 2026-07-01): `15:1146 16:1310 17:1379 18:1452 19:1452 20:1503 21:1716 22:1633 23:1850 24:2015 25:2015 26:2015` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE. (2024-2026 repiten valor = prórroga.)
- **Bandera(s) roja(s):** ✅ **ARREGLADO 2026-07-01** — era ~2× (3247-3995 €/hab) por doble conteo `4131` (transferencia Departamento→SALUD) + `4121` (entrega SALUD). Se excluye `4131` en extract.py. Vigilar: si vuelve a subir >2300 €/hab, se recoló la transferencia.
- **Seams documentados** (salto esperado, NO error): ninguno (estructura estable 2015-2026).

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
