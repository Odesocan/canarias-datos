# Limitaciones conocidas — Andalucía (and)

> Advertencias de la extracción de Andalucía. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `and-resumen-cap-prog` (PDF tomo de programas, 2017-2019 y 2022-2026) + `and-ckan-csv` (CSV de líneas de gasto del portal datosabiertos CKAN, 2015/2016/2020/2021) · Años: 2015-2026 · Estado global: 12 VERDE_PRAGM (~66-75 % concepto, 12 conceptos).

## Perímetro / decisiones de consolidación
- Clasificación funcional Junta de Andalucía (códigos 2-3 dígitos + letra: `41H`, `41C`, `12S`, …). Rama PDF: se captan las líneas `codigo denom … total` en las páginas `RESUMEN CAPÍTULOS-PROGRAMAS`; el último número es el total del programa. Rama CSV: se agrega `IMPORTE` por código `FUNCIONAL` (= programa) para reproducir las mismas filas programa+total.
- **Recodificación section-aware de la transferencia al SAS (fix 2026-07-01):** la transferencia al Servicio Andaluz de Salud —el grueso del gasto sanitario, ~13 B€— se recodificó en los presupuestos oficiales de programa `41H` "Planificación y Financiación" (función 41, ≤2022) a `12S` "Dirección y Servicios Generales" (función 12, ≥2024). El motor mapea `41*`→sanidad pero no `12S`, así que 2024-2026 caían a ~0,14 B. El extractor PDF ahora rastrea `SECCIÓN:` y, dentro de la CONSEJERÍA DE SALUD/SANIDAD, recodifica los programas de dirección `12x` a `41H` para que mapeen a sanidad y la serie sea continua con 2022.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido (los 13 conceptos disponen de códigos funcionales en `correspondencias.yml`; en la práctica aparecen 12 conceptos por año, sin `salud_mental` separable de forma estable). Nota: `41M` está en `salud_mental` pero la denominación de la familia `41x` la absorbe mayoritariamente sanidad.

## Advertencias de calidad del dato
- **FIX 2026-07-02 (conceptual, ambas ramas):** `31G` "Acción comunitaria e inserción" (210-238 M), `31P` "Apoyo a familias" (184-330 M) y `32E` "Proyectos de interés social" (46-58 M) iban a NULL → mapeados a `diversidad` (que estaba en 1 fila de 4-11 M, implausible; ahora 380-659 M/año). `31B` "Plan sobre adicciones" (34-41 M) movido de sanidad a `salud_mental` (antes 0). Aplica a rama CSV y PDF. Sanidad y total casi intactos (31B ~35 M). 13 conceptos en toda la serie salvo 2022 (anomalía aparte).
- **Rama CSV inflada (2015/2016/2020/2021) — CORREGIDA (FIX 2026-07-16).** El doble conteo era
  transferencia + ejecución simultáneas: el CSV CKAN incluye las líneas de la Consejería
  (`41H` = transferencia al SAS) Y las del propio SAS como centro gestor (`41C`/`41G`, dígitos
  3-4 del CENTRO GESTOR = "31"). `_extract_csv` ahora excluye las filas cuyo CENTRO GESTOR no
  es consejería (`cg[2:4] != "00"`), consolidando el perímetro igual que la rama PDF. Resultado:
  sanidad 2015: 16,13→8,39 B (993 €/hab) · 2016: 16,77→8,66 B · 2020: 20,82→10,77 B ·
  2021: 22,91→11,45 B; totales cuadran con el presupuesto publicado de la Junta (2020: 38,28 B
  ≈ 38,5 B oficial; 2021: 39,75 ≈ 40,2 B) y la serie CSV↔PDF es continua (TEST 1 limpio, seams
  `and` retirados de `auditoria_magnitud.py`). Las líneas excluidas se reportan en `notes`.
- **Rama PDF (2017-2019, 2022-2026) verificada tras el fix.** El fix section-aware corrige a la vez el hueco 2023-2026 (2024 pasó de 0,14 B roto a 14,09 B; 2026 de 0,11 a 15,99 B) y la inflación previa 2020-2022 de la rama PDF (2022 pasó de 24,37 B inflado ~2x a 12,25 B; el `41C`=8,8 B que inflaba 2022 era un fantasma de una extracción vieja, no está en el PDF). Per cápita resultante coherente (2022: 1441 €; 2024: 1657 €; 2026: 1881 €, pobl. ~8,5 M).
- Doble conteo de transferencia interna al Servicio de Salud: es uno de los tres casos detectados y (para la rama PDF) resuelto vía la recodificación `41H`/`12S`.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos VERDE_PRAGM. Ningún año en ERROR.
- Salvedad: 2015/2016/2020/2021 (rama CSV) están VERDE en extracción pero con magnitud inflada (ver arriba); no son directamente comparables con los años PDF hasta revisar la rama CSV.

## Notas de uso
- Compara los totales por magnitud (per cápita) y contra Hacienda antes de darlos por buenos; la certificación VERDE no valida magnitudes.
- Para series de sanidad, prioriza los años de rama PDF (2017-2019, 2022-2026) ya consolidados; los años de rama CSV requieren corrección de doble conteo.
- No fuerces el 80 % de cobertura: mucho gasto no-social (deuda, dirección general) queda correctamente sin concepto.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py and` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-16, tras consolidar rama CSV): `15:993 16:1025 17:1082 18:1141 19:1139 20:1274 21:1355 22:1445 23:1615 24:1663 25:1780 26:1888` — serie monótona continua; si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Rama PDF 2023-2026 **arreglada** (fix section-aware 12S→41H). Rama CSV 2015/16/20/21 **arreglada** (fix 2026-07-16 perímetro CENTRO GESTOR). Si sanidad >2300 o <900 en un año, o el total CSV vuelve a ~50 B, volvió el doble conteo.
- **Seams documentados**: ninguno (retirados 2026-07-16 — la alternancia CSV↔PDF ya no produce salto de magnitud; a nivel de CONCEPTO fino sigue habiendo diferencias de perímetro entre ramas, visibles como avisos TEST 3: igualdad, empleo, soberania).

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
