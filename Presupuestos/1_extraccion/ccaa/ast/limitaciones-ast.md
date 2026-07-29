# Limitaciones conocidas — Principado de Asturias (ast)

> Advertencias de la extracción del Principado de Asturias. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `ast-distribucion-gasto` (PDF `tomo_I.pdf` — tabla "DISTRIBUCIÓN DEL GASTO POR SECCIONES, PROGRAMAS Y CAPÍTULOS") · Años: 2015-2026 · Estado global: 12 VERDE_PRAGM (~67-71 % concepto, 9-10 conceptos).

## Perímetro / decisiones de consolidación
- Clasificación funcional asturiana; el extractor capta las líneas de PROGRAMA (3-4 dígitos + letra: `411C`, `422A`, `313D`…) tomando el penúltimo número como importe (el último es el porcentaje). Las subdivisiones por capítulo económico se ignoran.
- Estándar (una fila por programa), sin doble conteo ni proxy.
- **Corrección de correspondencias (2026-05-21):** la versión previa usaba códigos genéricos de 3 dígitos (`311`,`312`,`421`…) que NO coinciden con la nomenclatura asturiana y forzaban asignaciones erróneas (`313A`→salud_mental, `313C` cooperación al desarrollo→discapacidad, `313G`→discapacidad). El catálogo actual solo mapea programas identificables con seguridad.

## Conceptos NO separables — envoltorio de servicios sociales `313x` (FIX 2026-07-24)

> **Cambio conceptual 2026-07-24.** Asturias NO desglosa dependencia / discapacidad /
> salud mental como programas propios: viven agregados en los programas `313*` de la
> Consejería de Bienestar. El Cuaderno Metodológico define la procedencia de `dependencia`
> como *"Sección/DG dentro de SS … SS general en otras CCAA"* (Asturias no tiene DG dedicada
> tipo SEPAD). En consecuencia, **el envoltorio de SS general se asigna a `dependencia`**
> (concepto dominante y procedencia metodológica). Mapeo en el bloque `Principado de
> Asturias` del `correspondencias.yml` RAÍZ (regla `ccaa_codigo`, gana al patrón global):

| Programa | Denominación | Concepto |
|----------|--------------|:--------:|
| `313A` | Prestaciones y programas concertados (plazas residenciales/día, prestaciones) | **dependencia** |
| `313E` | Gestión de servicios sociales (residencias públicas, SAD, teleasistencia, valoración) | **dependencia** |
| `313G` | Ayudas diversas con fines sociales (línea nueva desde 2024) | **dependencia** |
| `313D` | Pensiones no contributivas | **dependencia** |
| `313F` | Atención a la infancia, familias y adolescencia | NULL (fuera de catálogo) |
| `313C` | Cooperación al desarrollo | NULL (residual: cae en discapacidad vía patrón GLOBAL) |
| `313B` | Emigración asturiana | NULL (residual: cae en diversidad vía patrón GLOBAL) |
| `313M` | Planificación, ordenación e innovación social | NULL (residual: cae en idi por keyword "innovación") |

- **`discapacidad` y `salud_mental` siguen NULL ESTRUCTURAL**: no son separables del
  envoltorio `313x` (comparten DG con dependencia — Cuaderno: *"Misma DG que dependencia en
  muchas CCAA"*; Asturias no tiene programa propio de salud mental). Los pocos M€ que aún
  aparecen en esos conceptos son **residuales de patrones GLOBALES** no asturianos y NO
  representan gasto real de Asturias en discapacidad/salud mental (ver más abajo).
- **BUG previo corregido (hasta 2026-07-24):** el mapeo global codifica códigos `313x` con la
  semántica de OTRAS CCAA (p.ej. `313A/313E→salud_mental` es el 313A de Madrid; `313F→
  discapacidad`; `313C→discapacidad` es de Galicia). Al dejar el bloque `313x` local en NULL,
  ganaba el global y mal-asignaba: **`salud_mental` ≈ 304-462 M€ falsos** (era 313A+313E),
  **`discapacidad` ≈ 35-75 M€ falsos** (era 313F infancia + 313C), y **`dependencia` ≈
  0,3→0,8→70 M€** (solo 313G/313D, con salto espurio en 2024 al aparecer la línea 313G). Tras
  el fix, `dependencia` recorre **≈ 300 → 524 M€** (nominal), serie continua y monótona.

### Residuales conocidos (leaks de patrón GLOBAL, no anulables desde el override de ast)
El motor `asignar_concepto` no permite forzar NULL vía override; un código no listado en el
bloque de la CCAA cae al patrón global. Quedan estos residuales menores, NO tocados para no
alterar otras CCAA:
- **`313C` cooperación al desarrollo (~6,7 M€/año) → discapacidad** vía global `313C`
  (compartido con Galicia, que lo usa para 455 M€ de "servizos sociais comunitarios").
- **`313B` emigración (~1,3-3,3 M€/año) → diversidad** vía global `313B` (exclusivo de ast;
  retirable del global sin riesgo si se decide limpiar).
- **`514B` infraestructura portuaria (~9-13 M€/año) → salud_mental** vía global `514` (código
  de salud mental de Navarra filtrándose). Es el residuo que deja `salud_mental` ≠ 0.
- **Sistémico (fuera de esta CCAA):** el mismo patrón mal-asigna en gal (`313C`→discapacidad,
  455 M€) y clm (`313A` "programas sociales básicos"→salud_mental, 980 M€). Revisión aparte.

## Advertencias de calidad del dato
- **VERDE pragmático estructuralmente moderado por diseño:** el extractor solo emite programas de gasto funcional; muchos programas sociales concretos (dependencia, discapacidad, salud mental) no existen como línea propia y quedan NULL. La cobertura ~67-71 % es la esperada, no un defecto.
- Ajuste de parsing de importes (2026-07-01): `base.parse_eur` corrige los importes españoles con un único punto de miles (`852.310` → 852310, no 852,31), lo que mejora Asturias 2021-2023 y evita infravalorar programas pequeños.
- **Doble conteo 2015 — CORREGIDO (FIX 2026-07-16).** El tomo de 2015 trae, además del bloque
  "DISTRIBUCIÓN DEL GASTO POR SECCIONES" (perímetro consejerías), anexos "RESUMEN PROGRAMÁTICO"
  y "PRESUPUESTO CONSOLIDADO" que listan los programas de los ORGANISMOS (Sección 97 SESPA:
  `412B` Asistencia Sanitaria 1.434 M ≈ la transferencia `413D` 1.435 M ya contada en la
  Consejería). El extractor barría todas las páginas y el dedup por (código, denom) no salvaba
  a los programas que solo existen en el anexo. Ahora `extract` salta las páginas sin el header
  `DISTRIBUCIÓN DEL GASTO` (normalizado sin acentos) y reporta en `notes` las páginas saltadas.
  Resultado 2015: sanidad 2,92→1,48 B (1469 €/hab, en banda), total 5,13→3,36 B (continuo con
  2016: 3,54 B). 2016-2026 re-verificados: salida idéntica (0 regresión).

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos VERDE_PRAGM.
- **2022 (resuelto 2026-07-01, con cautela):** el `tomo_I.pdf` original era la Ley BOPA 6/2021 completa (606 págs), que NO contiene la tabla programa+importe+porcentaje (el motor devolvía `WARN sin filas`). Se resolvió con `proyecto_2022_tomoII.pdf` de transparencia.asturias.es (Tomo II técnico, sí contiene el bloque de distribución): 96 filas, 10 conceptos, total 4.637 M€. **Cautela metodológica:** 2022 usa el Tomo II de *proyecto* técnico, el equivalente más próximo al bloque final publicado en BOPA para 2021/2023, no la tabla agregada del articulado final. La Ley BOPA se conserva como `ley_bopa_2021_11414.pdf`.

## Notas de uso
- `dependencia` en Asturias = **envoltorio de servicios sociales generales `313x`** (313A+313E+313G+313D), NO la prestación de dependencia SAAD aislada (Asturias no la desglosa). Es una aproximación por procedencia metodológica (Cuaderno: "SS general"); interpreta el dato como "gasto en servicios sociales de atención a la dependencia y afines", no como ejecución estricta del SAAD.
- `discapacidad` y `salud_mental` de Asturias son NULL estructural (no separables del envoltorio `313x`); los pocos M€ que muestran son residuales de patrones globales, no gasto real. No los uses como serie de Asturias.
- Ten presente que 2022 procede de un documento de proyecto, no del BOPA final; puede diferir levemente de la ejecución/aprobación definitiva.
- Valida magnitudes por per cápita y contra Hacienda antes de dar el dato por bueno.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py ast` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-16, tras fix perímetro 2015): `15:1469 16:1624 17:1652 18:1683 19:1734 20:1783 21:1923 22:1968 23:2095 24:2300 25:2422 26:2524` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** 2015 **arreglado** (fix 2026-07-16: gate al bloque DISTRIBUCIÓN; antes 2888 €/hab por el 412B del SESPA). 2024-2026 rozan/superan la banda alta (2300-2524): serie monótona sin par duplicado, crecimiento real plausible (población más envejecida de España) — banda-alta estructural, NO doble conteo; el TEST 2 seguirá avisando hasta que se parametrice banda por CCAA.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
