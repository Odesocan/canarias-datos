# Limitaciones conocidas — Comunidad de Madrid (mad)

> Advertencias de la extracción de Comunidad de Madrid. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `mad-libro-03-centros` (+ `mad-transform`); fallback `mad-xlsx-adjunto` si hay `programas*.xlsx|csv`. · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~40-50 %, 10-11 conceptos).

## Perímetro / decisiones de consolidación
- **PROXY de centro presupuestario, NO programa funcional.** No existe URL canónica estable del **Libro 04** (memoria de programas), así que se trabaja con el **Libro 03 "Ingresos y Gastos"**, sección IV.3 "Resumen por tipo de centros presupuestarios, orgánica y capítulos". Se extrae cada centro (código orgánico 4-5 díg.) y su columna TOTAL; el código orgánico hace de proxy del programa.
- El parseo sólo procesa páginas que incluyen la columna TOTAL en la cabecera (gate `_page_has_total`), para no tomar el Cap.5 como total en el formato antiguo 2015-2018 (tabla partida en dos páginas).
- El mapeo a concepto es **exclusivamente por KEYWORD** sobre la denominación del centro (todos los `codigos: []` en correspondencias.yml están vacíos): p. ej. "D.G. DE SANIDAD" → sanidad.

## Conceptos NO separables (NULL estructural por diseño)
- **`salud_mental`** y **`diversidad`**: no son centro presupuestario propio en Madrid; requieren el Libro 04 para aislarse. No capturables con el Libro 03.

## Advertencias de calidad del dato
- **PARCIALMENTE ARREGLADO (FIX 2026-07-02) — doble conteo agregado+centro eliminado.** El regex `RE_CENTRO` capturaba centros (4-5 díg.) Y agregados de sección (2 díg.), y ambos recibían concepto → doble conteo (educación 2015 +46 %). Además los agregados de 2 díg. eran poco fiables (sección 17 "SANIDAD" = 86 M€ en vez de los ~7,3 B€ de sus centros). Restringido a `\d{4,5}` (solo centros; para toda sección suma(hijos)≥agregado, así que no se pierde gasto). Total 2015 32,8→20,9 B€ (más cerca del real ~18-20 B€). Añadidos keywords sociales ("del mayor", "servicios sociales", "bienestar social", "atención social"→dependencia; "infancia"/"familia"→diversidad): dependencia 2015 256 M→1,22 B, diversidad recuperada.
- **⚠️ RESIDUAL: infra-captura por keyword (ya NO doble conteo).** Tras quitar el doble conteo, la educación queda INFRA-contada (2015 ~2,1 B€ vs sección real ~4,3 B€) porque centros como "D.G. DE RECURSOS HUMANOS" (profesorado, ~2 B€) no llevan keyword de educación. Limitación del proxy-centro (Libro 03); el arreglo definitivo sigue siendo el **Libro 04** (memoria por programas) o un mapeo por sección. Antes el defecto era sobre-conteo; ahora infra-conteo — en ambos casos usar cuotas relativas con cautela.
- **Prórrogas** (mismo dato replicado): **2020 y 2021 ≡ 2019**; **2023 ≡ 2022**.

## Años faltantes / problemáticos
- Serie completa 2015-2026 (todos VERDE_PRAGM), pero 2020/2021 y 2023 son prórrogas (ver arriba).

## Notas de uso
- **Usa cuotas relativas por concepto (%), NO importes absolutos** sin depurar: el proxy de centro infla el total ~2x.
- No compares los importes absolutos de Madrid con los de otras CCAA ni con la capa Hacienda hasta resolver el Libro 04.
- Trata 2020, 2021 y 2023 como prórrogas (no ejercicios independientes) en análisis longitudinales.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py mad` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1072 16:1117 17:1146 18:1178 19:1214 20:1214 21:1214 22:1326 23:1326 24:1544 25:1595 26:1676` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** ⚠️ Sanidad €/hab OK (~1072-1676) PERO el **TOTAL está inflado ~2×** (proxy de centro, Libro 03, no Libro 04). **No usar importes absolutos del total**, solo cuotas relativas. Prórrogas 2020/21≡2019, 2023≡2022.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
