# Limitaciones conocidas — Islas Baleares (bal)

> Advertencias de la extracción de Islas Baleares. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-24.

## Motor(es) y cobertura
- Motor(es): `bal-frameset-secciones` (frameset legacy del Tomo 3 en pressuposts.caib.es: 27 PDFs de sección `titol*_d.pdf`, 2015-2025) + `bal-resumen-programas-pdf` (PDF resumen de estados numéricos, solo 2026) · Años: 2015-2026 · Estado global: 12 VERDE_PRAGM (~51-76 % concepto, 8-13 conceptos).

## Perímetro / decisiones de consolidación
- Rama frameset: el mismo programa funcional (p.ej. `411A`) aparece bajo varios C.Cost (centro de coste) con su propia línea `Total Programa`; el extractor **suma esos parciales** por (codigo, denominación) → una fila por programa. Solo procesa ficheros con firma `%PDF` real (salta stubs 404).
- Rama resumen (2026, prórroga): la prórroga publica un PDF de estados numéricos, no el frameset histórico. Se lee el bloque `Clasificación por programas` y **se limita a Administración general, parando antes de "Prórroga de presupuesto del Servicio de Salud"** para no duplicar la transferencia sanitaria `411E`. Se excluye `011A` (deuda) para mantener el universo comparable con el Tomo III histórico.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido: `correspondencias.yml` mapea los 13 conceptos con códigos funcionales reales baleares (`411E` finançament sanitari, `313D` dependència, `316A` drets i diversitat, `323C` igualtat…). Desde 2017 la serie alcanza los 13 conceptos.

## Advertencias de calidad del dato
- **Cautela con doble conteo de la transferencia sanitaria en 2026:** el corte antes del Servicio de Salud (`bal-resumen-programas-pdf`) evita duplicar `411E`, pero implica que 2026 procede de un motor distinto (PDF resumen) que el resto de la serie (frameset); comparar 2026 con años previos con esa salvedad de perímetro.
- **2015 y 2016 — RESUELTO 2026-07-02 (mismo bug que 2017).** Estaban con 8 y 11 conceptos porque a las secciones `titol0_d.pdf`…`titol9_d.pdf` (Parlament, Presidència, Hisenda, **Educació ~800 M€**, Turisme, Agricultura…) se les pedía el nombre con cero (`titol00`) y en el path equivocado → 34 B stub 404, saltados en SILENCIO. La educación de 2016 quedaba en 1 fila de 0,2 M€. Re-descargadas del path correcto `pressuposts.caib.es/www/ant/pr<año>/archivos/toms/tom3/titol<N>_d.pdf` (SIN cero): 2015 → 131 filas/13 conc/4,01 B; 2016 → 132 filas/13 conc/4,22 B. El salto documentado "2016→2017 tot×1,44" era cobertura recuperada, no crecimiento. Añadido contador de stubs a `notes` para que la ausencia deje de ser silenciosa.
- **2018, 2019, 2020 y 2021 — RESUELTO 2026-07-24 (MISMO bug que 2015-2017, se quedaron fuera de aquel fix).** Las secciones `titol00_d.pdf`…`titol09_d.pdf` (2 dígitos) eran stubs de 34 B (`No es pot trobar la pàgina!`): el servidor sirve esas secciones SIN cero a la izquierda (`titol0`…`titol9`), y las ≥10 coinciden con/sin padding (por eso solo 00-09 fallaban). La sección `titol8` = **Conselleria d'Educació** (índice 8 del desplegable) quedaba ausente → `imp_educacion` en **~1,0 M€/año** (vs ~936-1.021 M€ reales; ~1.000 M€/año perdidos) y `var_educacion` 2022 disparado a **+107.058 %**. También faltaban turisme (`titol7`), i+d+i, igualtat i diversitat de esas secciones. Re-descargadas `titol0`…`titol9` (sin cero) de `pressuposts.caib.es/www/ant/pr<año>/archivos/toms/tom3/` y eliminados los stubs de 2 dígitos → 28-29 PDFs de sección/año, **13 conceptos, educación continua** (2017: 883 → 2018: 936 → 2019: 1.001 → 2020: 1.006 → 2021: 1.021 → 2022: 1.136 M€ constantes) y `var_educacion` 2022 normalizado a **+11,3 %**. Sanidad (`titol12`) no se vio afectada (siempre fue índice ≥10, real).
- Sin inflación de totales conocida en la rama frameset.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos VERDE_PRAGM.
- **2017 (resuelto 2026-07-01):** los `titol*_d.pdf` originales eran stubs de 34 B (`No es pot trobar la pàgina!`). La fuente correcta no es `pr2017` sino `pr2017-def`, y las secciones usan nombres sin cero a la izquierda (`titol0_d.pdf`…`titol25_d.pdf`). Re-descargados 26 PDFs reales → 129 filas, 13 conceptos, total 4.647 M€.
- **2026 (resuelto 2026-07-01):** documento de prórroga; el enlace con punto final (`id=540093.`) devuelve 400; sin el punto descarga `estats_numerics_2026_(castella).pdf`. No tiene `Total Programa` pero sí `Clasificación por programas` → nueva rama `bal-resumen-programas-pdf` (148 filas, 13 conceptos, total 6.442 M€). Es prórroga, no presupuesto propio del ejercicio.

## Notas de uso
- Ten presente que 2026 es prórroga y se extrae con un motor/perímetro distinto (solo Administración general + programas de resumen, sin el detalle por C.Cost del frameset).
- No dupliques la transferencia sanitaria `411E` si combinas fuentes: el diseño del extractor ya la cuenta una sola vez.
- Valida magnitudes por per cápita y contra Hacienda; la certificación VERDE no comprueba totales.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py bal` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1096 16:1160 17:1249 18:1317 19:1446 20:1445 21:1492 22:1642 23:1863 24:1925 25:2027 26:2054` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible (1096-2027 €/hab). Sin banderas rojas de magnitud.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
