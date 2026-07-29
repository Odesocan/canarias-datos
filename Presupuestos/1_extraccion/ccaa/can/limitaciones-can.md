# Limitaciones conocidas — Canarias (can)

> Advertencias de la extracción de Canarias. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `can-tomo3-resumen-programas` (parseo PDF; rama `can-csv-seflogic` si hay CSV adjunto, hoy inactiva) · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~65-67 % concepto, 12-13 conceptos).

## Perímetro / decisiones de consolidación
- Fuente: `TOMO 3 - Resúmenes`, sección **2.10 "RESUMEN DE GASTOS POR PROGRAMAS — COMUNIDAD AUTÓNOMA"** (consolidado por programa, importes en euros).
- Se **excluyen** deliberadamente las secciones 2.15/2.16 ("POR PROGRAMAS Y CAPÍTULOS" / "POR SECCIONES, PROGRAMAS Y CAPÍTULOS"): son desgloses por capítulo cuyos "Total" repiten los mismos códigos → evita doble conteo.
- Códigos canarios = 3 dígitos + letra (`312A`, `412A`, `231M`…). Un mismo código repetido (p. ej. cabildos en secciones posteriores) se queda con la primera aparición (2.10 va antes que 2.11+).
- Selección de importe: la sección 2.10 es bianual (columnas año-1 ajustado / año objetivo); `_pick_importe` toma el **2º importe sin coma decimal** como el del año objetivo. Sanidad verificada monótona contra 2018 (2.460→2.739 mil M€), columna de año confirmada correcta.

## Conceptos NO separables (NULL estructural por diseño)
- `salud_mental`: **NULL estructural en toda la serie (FIX 2026-07-16).** Los 3 años que
  aparentaban dato (2019-21) eran `313A` "Salud Pública" (0,3 M) mal mapeado — salud pública es
  sanidad, no salud mental, y 0,3 M es implausible como programa autonómico. `313A` retirado del
  catálogo. El gasto real de salud mental canario va dentro del programa del SCS (`412*`) sin
  desagregar; pendiente verificar en el Tomo 3 si algún subprograma lo separa. Los ~33-35 % de
  filas sin concepto son gasto no-social fuera de catálogo (deuda, servicios generales,
  dirección) → esperado.

## Advertencias de calidad del dato
- **FIX 2026-07-16:** retirado `313A`→salud_mental (fabricaba el concepto, ver arriba). Canarias
  pasa de 12-13 a 12 conceptos uniformes en toda la serie. Sin otras incidencias conocidas.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos.

## Notas de uso
- Serie **autonómica** consolidada por programa; comparable año a año dentro de Canarias sin ajustes.
- `salud_mental` no es una serie continua: no lo trates como cero implícito fuera de 2019-2021, sino como no desagregado en 2.10.
- Es la CCAA-foco del proyecto; serie de referencia. Antes de comparar niveles absolutos con otras CCAA, recuerda que aquí el perímetro es programa consolidado (no centro, no capítulo).

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py can` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1098 16:1114 17:1141 18:1223 19:1265 20:1326 21:1379 22:1440 23:1596 24:1834 25:1924 26:2028` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible y continua (1098-2028 €/hab). Sin banderas rojas.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
