# Limitaciones conocidas — Cataluña (cat)

> Advertencias de la extracción de Cataluña. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor: `cat-programa-generalitat-suma` (FIX 2026-07-02) — suma la línea `PROGRAMA <cod> <denom> <importe>` de todas las páginas de detalle (cabecera `Servei:`) del `Àmbit: Subsector GENERALITAT` del PDF `vol_p_eid`. Maneja formato con denominación (2016+) y sin ella (2015). Años registrados: 2015-2017, 2019-2020, 2022-2024, 2026 (9 ejercicios) · Estado global: 9 VERDE_PRAGM (~63-67 % concepto, 13/13 conceptos).

## Perímetro / decisiones de consolidación
- **Sanidad = consolidada evitando doble conteo de la cadena de transferencias internas (fix 2026-07-01).** La sanidad catalana se financia en cadena: Generalitat —(prog `415` "Al Servei Català de la Salut", ≈8,23 B)→ CatSalut (entitat 5100, ≈presupuesto sanitario consolidado) —(415 "A l'ICS")→ ICS —(ejecuta `411` primària + `412` especialitzada). El PDF lista los programas de TODAS las entidades, así que sumar `415` (la transferencia = presupuesto de CatSalut) MÁS `411`/`412` (la entrega del ICS que esa transferencia ya financia) **duplicaba** el gasto (~2x: ~2220 €/hab vs ~1340 real).
- **Decisión:** sanidad = `415` (CatSalut consolidado) + `414`/`419` (salut pública, aparte). Se **EXCLUYEN `411` y `412`** (entrega ICS, subconjunto ya dentro de 415). El extractor los filtra en ambos motores (`_SALUT_DOBLE_CONTEO = {"411","412"}`) y el `correspondencias.yml` los quita de `sanidad` por coherencia. Verificado: staging `415` (8.476 B) ≈ CatSalut total (8.475 B, entitat 5100, 2016). Per cápita 2022 resultante ≈1338 €/hab (en línea con Madrid ~1327).
- **Perímetro GENERALITAT + suma por servei (FIX 2026-07-02).** El EID detallado lista cada programa UNA VEZ POR SERVEI y lo repite en otros subsectores (entitats autònomes, consorcis, societats) financiados por transferencia interna. El motor suma la línea PROGRAMA de las páginas `Servei:` del `Subsector GENERALITAT` → total consolidado sin doble conteo. Verificado 2015/2016/2026: dentro de GENERALITAT NO hay líneas PROGRAMA a nivel agregado (Secció/Àmbit), así que sumar los serveis es exacto; excluir los demás subsectores evita contar dos veces las transferencias internas (mismo criterio que la cadena SALUT).
- **Bug histórico corregido (first-wins → suma):** hasta 2026-07-02 el motor se quedaba con la PRIMERA aparición de cada programa, truncando los multi-servei: educació ×3,3 (2016 1,5→5,4 B; 2026 2,6→9,3 B), universitats ×87, dependència ×15,7 (2026 0,16→2,49 B). Sanidad se salvaba por accidente (415 es mono-servei → suma ≈ first-wins). El seam 2015→2016 (total ×0,54) era artefacto del first-wins en 2016, no de la fuente: tras el fix 2015=32,5 B ≈ 2016=33,7 B.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido (los 13 conceptos aparecen en la serie). El ~36 % de filas sin concepto es gasto no-social fuera de catálogo → esperado.

## Advertencias de calidad del dato
- **Bug corregido (2026-07-01):** el programa `412` estaba mapeado a `soberania` en `correspondencias.yml` — era un error: `412` es atenció especialitzada de SALUT, no soberanía alimentaria. Retirado de `soberania`. Datos previos a la corrección sobreestimaban soberanía e (por el doble conteo) sanidad.
- La corrección de sanidad afecta a toda la serie: valores de sanidad anteriores a 2026-07-01 estaban inflados ~2x. Verificado tras el fix: 2016 ≈8,50 B, 2022 ≈10,35 B (solo 415/419).

## Años faltantes / problemáticos
- **2018, 2021, 2025 no registrados** (no hay VERDE en catálogo). 2025 documentado como hueco sin raw en `fuentes/raw/cat/`. Falta localizar/descargar el `vol_p_eid` de esos ejercicios.

## Notas de uso
- Para sanidad usa SIEMPRE la versión post-fix (excluye 411/412). No re-incluyas 411/412 ni sumes CatSalut + ICS: duplicarías el gasto asistencial.
- Serie con huecos (2018, 2021, 2025): no interpoles sin marcarlo; no hay dato oficial cargado para esos años.
- Comparabilidad de sanidad per cápita con Madrid/Canarias validada solo con el perímetro consolidado 415+414/419.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py cat` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1060 16:1092 17:1105 19:1171 20:1218 22:1328 23:1454 24:1507 26:1668` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** **Arreglada** (fix: excluir `411`/`412` entrega ICS, contar `415` = CatSalut). Baseline ~1333-1675 €/hab. Si supera ~2000, volvieron a colarse 411/412.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
