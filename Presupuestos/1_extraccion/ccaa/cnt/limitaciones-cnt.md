# Limitaciones conocidas — Cantabria (cnt)

> Advertencias de la extracción de Cantabria. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `cnt-total-programa-suma-servicios` (suma `TOTAL PROGRAMA:` por código, 2018-2026) · `cnt-centros-suma-capitulos` (Anexo Desarrollo Económico por Centros Gestores, suma `TOTAL CAPÍTULO:` por programa, 2015-2017) · Fallback `cnt-politica-gastos-boc` (tabla "POLÍTICA DE GASTOS" del Art. 2 de la Ley BOC, disponible pero hoy inactivo) · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~52-55 % concepto, 12 conceptos).

## Perímetro / decisiones de consolidación
- Importes en euros enteros (es-ES). Un mismo programa se reparte entre varios servicios (p. ej. `140A` "PERSONAL" aparece en ~20 servicios), por lo que se **SUMAN todos los `TOTAL PROGRAMA` por código** para obtener el total consolidado del programa.
- **2015-2017 usan otra fuente y otro motor:** el "Anexo de Desarrollo Económico de Gasto por Centros Gestores" NO trae `TOTAL PROGRAMA`, sino `TOTAL CAPÍTULO:` por capítulo dentro de cada programa → el total del programa = suma de sus capítulos. Selección automática por umbral (≥20 códigos): `TOTAL PROGRAMA` si existe, si no suma de capítulos. Serie sanidad continua y monótona cruzando ambos motores: 0.766 (2015) → 0.823 (2018) → 1.269 (2026) mil M€.
- Uso de `pdftotext -layout` (poppler) por rendimiento; fallback a pdfplumber (~450-540 págs, 15 MB).

## Conceptos NO separables (NULL estructural por diseño)
- **`diversidad`: nunca aparece** en la serie 2015-2026 (Cantabria no publica programa etiquetable como LGTBI / migración / interculturalidad en su catálogo por programa). Es NULL estructural en las 12 filas.
- **`discapacidad`: NULL estructural desde el FIX 2026-07-16.** El fix 2026-07-02 lo declaró NULL
  pero `232C` "FOMENTO DE LAS ACTIVIDADES JUVENILES" (0,03 M) seguía en el YAML y fabricaba el
  concepto en 2022-23 (juventud ≠ discapacidad). Retirado; el gasto real está en `231B`
  "Autonomía Personal y Atención a la Dependencia" (176 M) → dependencia.
- El ~45-48 % de filas sin concepto es gasto no-social fuera de catálogo: carreteras (`451N`, `453B`), deuda (`951M`), función pública (`921N-Q`), telecomunicaciones (`491M`) → esperado y correcto.

## Advertencias de calidad del dato
- **FIX 2026-07-02 — códigos exactos de OTRA añada del plan presupuestario mal asignados.** Contaminaban los conceptos pequeños: `313A` "SALUD PÚBLICA" (9,7 M) iba a salud_mental (era el 100 % del concepto → fabricado) y ahora va a sanidad (keyword); `231C` "INFANCIA, ADOLESCENCIA Y FAMILIA" (14,5 M) iba a discapacidad (100 % → fabricado) y ahora a diversidad; `232D` "FOMENTO DE LA NATALIDAD" fuera de dependencia; los prefijos `232*`/`323*` arrastraban `232A` "JUVENTUD" (19,5 M) y `323A` "INNOVACIÓN" (8,7 M→idi) a igualdad → igualdad 32→3-8 M (real). Añadido keyword "sanitario" (`311O` "Formación de personal sanitario", 22 M, iba a NULL). Efecto: `salud_mental` y `discapacidad` pasan a NULL (Cantabria no los desglosa en programa propio — honesto, no fabricado); igualdad y sanidad correctas.
- **Bug corregido (2026-06-29): el slot 2025 contenía datos de 2026.** `fuentes.yml` tenía cnt 2025 apuntando a la URL del 2026 ("2º INGRESOS Y GASTOS DEFINITIVA"); el raw en disco era el Proyecto 2026 (total 3,97). La fila VERDE de 2025 estaba sobre datos de 2026. Corregido: URL de 2025 correcta, raw sustituido (el erróneo → `_ERRONEO_era_2026_*.bak`), 2025 re-extraído (88 filas, total 3,79, encaja entre 2024=3,56 y 2026=3,97). **Usa la serie posterior a esa fecha.**
- `salud_mental` sí aparece pero con cobertura fina (a menudo 1 programa); trátalo con cautela en años delgados.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos. (Nota histórica: 2015-2017 pasaron por un estado AMARILLO transitorio con el fallback política-de-gasto —granularidad de área 2-díg, ~19 filas, área "23 Servicios Sociales" agrupa dependencia+discapacidad+igualdad+salud_mental— antes de subir a VERDE con el Anexo de Centros Gestores. El fallback político queda disponible pero NO está en uso.)

## Notas de uso
- No esperes `diversidad` en Cantabria: su ausencia es estructural, no un fallo de extracción.
- 2015-2017 provienen de suma de capítulos (motor distinto): son consolidados por programa y comparables con 2018-2026, pero si depuras diferencias finas ten presente el cambio de motor.
- Verifica que trabajas con el 2025 corregido (post 2026-06-29), no con el raw antiguo que era 2026.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py cnt` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1328 16:1361 17:1394 18:1420 19:1459 20:1560 21:1689 22:1704 23:1793 24:1912 25:2026 26:2189` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible (1328-2189 €/hab). Sin banderas rojas.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
