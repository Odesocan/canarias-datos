# Limitaciones conocidas — Región de Murcia (mur)

> Advertencias de la extracción de Región de Murcia. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `mur-html` (visor CHAC 2016-2026) y `mur-pdf-programas` (Ley completa BORM, sólo 2015). · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~73-79 %, 13 conceptos).

## Perímetro / decisiones de consolidación
- Estándar: agregación por **código de programa funcional** (`\d{3}[A-Z]`, p. ej. 412A, 421B, 911A), sumando el importe del programa por servicio e ignorando desgloses inferiores. Mismo criterio en la rama HTML y en la PDF.
- Perímetro: Estado de Gastos de la Administración General (`xml/31.xml`, `p228-*`) **+ organismos autónomos** IMAS, SEF, BORM (`xml/32.xml`, `p230/p231-*`).
- **2015** no tiene visor HTML: se extrae de la **Ley completa BORM en PDF** (`ley_completa.pdf`), páginas "Estado de gastos por servicios y programas presupuestarios". La rama PDF activa el bloque por ese encabezado, sigue páginas de continuación (que no repiten la cabecera) y corta al entrar en ingresos/resúmenes por capítulos.
- Importes en euros (separador de miles con punto).

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido: correspondencias.yml mapea los 13 conceptos del catálogo (todos con códigos y/o keywords), y la serie cubre los 13 cada año.

## Advertencias de calidad del dato
- **Descarga sensible a Radware/ShieldSquare (captcha).** El motor HTML detecta y **descarta** ficheros con "Radware Captcha"/"shieldsquare" (los cuenta en `notes`). Una re-descarga desde IP rate-limitada puede dejar secciones fuera; hay que regenerar el raw con `tools/mur_download.py` desde IP no bloqueada.
- 2015 (rama PDF): si se busca el encabezado de forma literal sólo se recuperan ~59 programas / 2,98 B€; la rama actual sigue las continuaciones y recupera la serie completa (150 filas, 4.907.800.412 € totales; sanidad 1.859.495.700 €, educación 1.301.370.707 €).

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos (2015 vía PDF, 2016-2026 vía visor HTML).

## Notas de uso
- Si al re-extraer un año HTML caen filas o conceptos, revisa `notes` por ficheros Radware ignorados antes de dar el dato por bueno.
- 2015 procede de fuente distinta (Ley PDF) al resto (visor HTML); las magnitudes cuadran contra 2016, pero tenlo presente en auditorías de reproducibilidad.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py mur` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1215 16:1280 17:1308 18:1388 19:1430 20:1440 21:1626 22:1654 23:1739 24:1861 25:1943` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible (1280-1955 €/hab). Sin banderas rojas.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
