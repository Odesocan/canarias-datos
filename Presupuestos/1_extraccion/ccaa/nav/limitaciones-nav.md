# Limitaciones conocidas — Comunidad Foral de Navarra (nav)

> Advertencias de la extracción de Comunidad Foral de Navarra. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `nav-breakdowns-functional` (+ `nav-transform`); si el operador adjunta un CSV/XLSX limpio gana `nav-csv-adjunto`. · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~75-78 %, 12-13 conceptos).

## Perímetro / decisiones de consolidación
- Fuente: el visor SPA de `presupuesto.navarra.es` embebe todos los datos en `var breakdowns = {…}` dentro de un `<script>`. Se lee `breakdowns.functional.sub[<función>].sub[<programa>]` y su gasto del ejercicio.
- Código canónico = `<función 2 díg>.<programa 4 caracteres>` (p. ej. `31.3122` = Sanidad / Atención primaria; `32.322D` = Educación / Ed. primaria). Mapeo a concepto por prefijo de función (`31.*`→sanidad, `32.*`→educacion, …) más keywords.
- **Importes en CÉNTIMOS**: el extractor divide entre 100 para pasar a euros.
- El JS no es JSON estricto (claves con comillas simples, comas finales); se normaliza antes de `json.loads`.
- 2015-2017 se obtienen del **mismo visor HTML multi-año** (clasificación funcional), no de fuentes separadas por año.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno declarado en correspondencias.yml: los 13 conceptos tienen códigos funcionales asignados. En la práctica **`discapacidad` no aparece de 2019 en adelante** (la serie pasa de 13 a 12 conceptos), por lo que su cobertura no está garantizada todos los años.

## Advertencias de calidad del dato
- La cobertura de concepto se queda en ~75-78 % (VERDE_PRAGM): el resto es gasto fuera del catálogo §1.6 (deuda, servicios generales, etc.), correctamente sin concepto.
- Depende de que el HTML servido siga embebiendo `var breakdowns`; si el portal cambia de versión el motor cae a `nav-pendiente` (0 filas).

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos. Único matiz: `discapacidad` deja de mapearse desde 2019 (12 conceptos en vez de 13).

## Notas de uso
- Serie homogénea 2015-2026 con clasificación funcional; apta para comparación longitudinal.
- No asumas presencia de `discapacidad` en 2019+; compruébalo antes de series de ese concepto.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py nav` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1351 16:1418 17:1502 18:1529 19:1564 20:1675 21:1808 22:1818 23:1919 24:2113 25:2179 26:2251` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Importes en **céntimos ÷100**: si sale ×100, error de unidad. `discapacidad` deja de mapearse desde 2019.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
