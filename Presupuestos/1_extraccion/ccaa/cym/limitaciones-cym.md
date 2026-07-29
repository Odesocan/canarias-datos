# Limitaciones conocidas — Castilla y León (cym)

> Advertencias de la extracción de Castilla y León. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `cym-jcyl-datosabiertos` (+ `cym-transform`) para 2016-2026 · `cym-bocyl-territorial` (rama PDF, + `cym-transform`) para **2015** · Años: 2015-2026 (12 ejercicios) · Estado global: 12 VERDE estricto (85.3-87.5 % concepto, 13/13 conceptos).

## Perímetro / decisiones de consolidación
- Fuente: recursos CKAN de datosabiertos.jcyl.es (`1284548037482-<N>.csv`, que en realidad son ZIP). El identificador `<N>` NO es el año: cada recurso se data por la etiqueta de la columna de importe o por la fecha interna del ZIP (mapa verificado: `-1=2016 -2=2017 -3=2018 -4=2021 -5=2023 -6=2024 -7=2025 -8=2026`).
- El extractor normaliza TRES formatos de origen a `(subprograma → importe del ejercicio)`: Excel consolidado (.xls/.xlsx, 2023-2026), "WEB Datos csv gastos.csv" (2021) y "Dotaciones Presupuesto de Gastos.csv" (2016-2018).
- Granularidad: subprograma (código de 6 caracteres, p.ej. `312A01`, `322A01`), sumando capítulos/económicas. En el formato "Dotaciones" (2016-2018) no hay descripción de subprograma → el concepto se asigna solo por código.
- Importes en euros (los CSV vienen en formato es-ES: punto de miles, coma decimal). Sin factor ×1000.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido. Las 8 series presentan los 13 conceptos del catálogo.

## Advertencias de calidad del dato
- **2016-2018 CONSOLIDADO (FIX 2026-07-02).** El formato "Dotaciones" incluía las transferencias internas a OOAA (Gerencia Regional de Salud, Gerencia de SS, ECYL) como líneas propias (concepto económico 400/401 corrientes, 700/701 capital) MIENTRAS el OOAA figura APARTE con su gasto ejecutado en el mismo fichero → doble conteo ~+30 % (total 2017 14,30→10,29 B; sanidad 2017 ~6,67→3,45 B). El extractor (`_records_from_csv`) ahora descarta las líneas con esos conceptos económicos (auto-detecta la columna `Concepto`; no-op en el CSV consolidado 2021 y en los Excel 2023-26, que ya vienen sin ellas). Tras el fix la serie es continua: total 2016=9,84B → 2021=12,29B → 2024=14,56B; sanidad 1379→2020 €/hab, toda en banda.
- **FIX 2026-07-02 (ZIP): 2025/2026 no cargaban.** La URL de datos abiertos JCyL es un `.csv` que en realidad es un ZIP; el pipeline lo guarda como `gastos.bin` y se lo pasaba al extractor, que lo rechazaba (caía a la rama CSV) → cym 2025/2026 fuera de la tabla pese a existir el `.xls` correcto al lado. `extract.py` ahora detecta el ZIP (`_resolve_source`, firma `PK`) y extrae de dentro el fichero de gastos (.xls/.xlsx/.csv, descartando "ingreso"). cym completo 8/8 años.
- **2015 desde el PDF BOCYL (motor `cym-bocyl-territorial`, 2026-07-03).** `datosabiertos.jcyl` no publica distribución 2015. Única fuente = Ley 11/2014 (BOCYL, 576 pp), cuyo estado de gastos figura SOLO como "9.- Detalle económico territorial por secciones y subprogramas", repetido por cada entidad del grupo (Administración General + cada OOAA: Gerencia Regional de Salud, Gerencia de Servicios Sociales, ECYL, ITA, ADE, EREN). La rama PDF (`_records_from_pdf_bocyl`) agrega por SUBPROGRAMA sumando las líneas de CAPÍTULO (económico de 1 dígito, columna TOTAL) y RESTANDO las transferencias internas a OOAA (concepto 400/401/700/701 — mismo criterio de consolidación que la rama CSV). El neto **reconcilia AL EURO** con el "Estado de gastos consolidado" oficial (p56: total 9.920.811.756; sanidad sección 3,27B, educación 1,84B). Resultado: 104 subprogramas, 87.5 % concepto, 13 conceptos, total 9,92B. Continuidad vs 2016: total +0.8 %, sanidad −1.0 %, educación −2.8 %, y los 13 conceptos <±10 % salvo soberania +9.5 % (variación agraria/PAC real). Sanidad 1316 €/hab (nominal), continua con 2016 (1342 nominal). **cym completo 12/12 años (2015-2026).**
- **2025 ≡ 2026 (prórroga):** idénticos a nivel de subprograma (prórroga del presupuesto de 2024, que difiere en solo 3 subprogramas). Son datos reales pero NO independientes; no los trates como dos observaciones distintas.
- La certificación VERDE no valida magnitudes (ver `LIMITACIONES.md` §1): estos totales no se han conciliado aún contra la serie de Hacienda.

## Años faltantes / problemáticos
- **Ninguno: serie completa 2015-2026.** 2015 desde el PDF BOCYL (ver arriba); 2019/2020/2022 son prórrogas (2019≡2020≡2018, 2022≡2021 — el portal jcyl no publica recurso independiente y la ley prorroga el ejercicio anterior).
- **2016-2018:** presentes; ya CONSOLIDADOS tras el fix 2026-07-02 (ver arriba).
- **2025-2026:** prórroga de 2024 (ver arriba).

## Notas de uso
- Para comparación longitudinal, trata 2016-2018 aparte de 2021+ (romper la serie en el salto de consolidación) o aplica el ajuste de Hacienda cuando esté disponible.
- No interpretes la caída 2018→2021 como un recorte presupuestario: es un cambio de perímetro del origen (transferencias internas incluidas hasta 2018).
- 2025 y 2026 no aportan variación real sobre 2024 salvo 3 subprogramas.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py cym` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab nominal, 2026-07-02 tras consolidar; 2015 añadido 2026-07-03): `15:1316 16:1379 17:1446 18:1488 21:1812 23:1968 24:2020` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** ✅ **RESUELTA** (fix 2026-07-02: filtro de transferencias internas OOAA). Serie continua y en banda. Si 2016-18 vuelven a ~2800 €/hab, se coló otra vez el concepto económico 400/401/700/701. En 2015 el mismo síntoma sería no restar concepto 400/401/700/701 en la rama PDF (total saltaría de 9,92B a ~13,6B). Serie 2015-2026 completa.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
