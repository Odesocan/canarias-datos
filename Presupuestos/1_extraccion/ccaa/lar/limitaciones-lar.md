# Limitaciones conocidas — La Rioja (lar)

> Advertencias de la extracción de La Rioja. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `lar-resumen-programas-pdfplumber` (2016-2017) y `lar-pdfplumber-funcional-economico` (2019, 2021, 2022, 2024, 2025, 2026), ambos + `lar-transform` · Años: 2016, 2017, 2019, 2021, 2022, 2024, 2025, 2026 (8 ejercicios) · Estado global: 1 VERDE estricto (2025, 84.5 %) + 7 VERDE_PRAGM (68.6-76.7 %). 7-13 conceptos según año.

## Perímetro / decisiones de consolidación
- Fuente: PDF de la Ley de presupuestos (BOLR) publicados en larioja.org. El extractor ya NO depende de Camelot; usa **pdfplumber** con dos patrones: (1) tablas `Resumen ... por Programas` (código `NNNN - denominación` + total), y (2) `Detalle Gastos Funcional / Económico`, con una máquina de estado que reconstruye códigos jerárquicos de 4 niveles `G.F.SF.P` (p.ej. `3.1.2.1` = Sanidad / Hospitales / Atención primaria) desde Grupo/Función/Subfunción/Programa.
- El texto de estos PDF trae artefactos de OCR (el cero renderiza como "o" minúscula, rótulos partidos como "AL TA DIRECCIÓN") que el extractor normaliza. La extracción se acota por ventanas de página específicas por año (`_PAGE_WINDOWS`).
- Importes en euros. Sin factor ×1000.
- **2024 lleva un suplemento manual acotado:** en la Ley BOLR 2024 las páginas renderizadas 23300 y 23304 muestran tablas visibles que pdfminer/pdfplumber NO exponen como texto (educación, cultura/deporte y cierre de administración/deuda). Esas ~16 filas se transcribieron a mano en `_supplement_image_only_rows` y cierran contra el Total General de Gastos = 1.947.377.372 €.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno estructural en el correspondencias (los 13 conceptos tienen códigos/keywords asignados; salud_mental=`3.1.3.3`, discapacidad=`2.3.2.3`, etc.). En la práctica los años más antiguos aparecen con menos conceptos por cobertura del origen: 2016 solo 7 conceptos (sin dependencia/discapacidad/salud_mental/diversidad/igualdad/vivienda); 2019-2022 con 12 (sin salud_mental).

## Advertencias de calidad del dato
- **Códigos punteados incompatibles con el correspondencias RAÍZ de R:** el extractor emite códigos `3.1.1.1` pero el raíz de R traía La Rioja como `312A`, así que R re-derivaba el concepto y NO reconocía los punteados → sanidad (y otros) caían a NULL en la DB. **Rescatado el 2026-07-01 por el fallback Python** en `2_transformacion/transformacion.R` (`regla="python_local_fallback"`): donde R queda NA y Python asignó, se adopta el de Python. Efecto en La Rioja: sanidad 2016-2026 pasó de ~0 a la serie continua 0,42-0,64 B. (Ver `LIMITACIONES.md` §2.)
- La certificación VERDE_PRAGM no valida magnitudes (ver `LIMITACIONES.md` §1); conciliación contra Hacienda pendiente.

## Años faltantes / problemáticos
- **2015:** los raws/fragmentos actuales solo dan 17 filas y total 0,326B (incompleto); NO incorporado.
- **2018:** texto del PDF invertido (right-to-left, 1214 pág); el tramo localizado produce 1 fila espuria; NO incorporado.
- **2020:** el PDF devuelve 100 % texto CID (no extraíble) y apunta a anexo de inversiones; sin tabla útil; NO incorporado.
- **2023:** la sección existe en el BOLR pero la tabla aparece rotada y el OCR/parseo local no es lo bastante fiable para incorporar programa a programa; NO incorporado.
- **2024:** incorporado (VERDE_PRAGM) pero DEPENDE del suplemento manual descrito arriba; sin él perdería educación y el total caería a 1,317B vs 1,947B real.
- **2016:** VERDE_PRAGM con solo 7 conceptos (cobertura limitada del resumen por programas de ese año).

## Notas de uso
- Verifica la magnitud de sanidad (serie objetivo continua ~0,42-0,64 B; La Rioja ~320k hab): si aparece en 0/NULL, es que el fallback Python no se aplicó (revisar `concepto_python` en la transformación).
- La serie útil de La Rioja tiene HUECOS (falta 2015, 2018, 2020, 2023): no la trates como serie anual continua; interpola con cautela.
- 2024 es fiable solo con el suplemento de código incluido; si se re-parsea sin él, quedará incompleto.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py lar` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-02 tras el fix legacy): `15:1245 16:1276 17:1276 19:1361 21:1653 22:1639 24:1851 25:2002 26:1991` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **FIX 2026-07-02 — el "2016 BAJO 353 €/hab" era MIS-ASIGNACIÓN, no infra-extracción del origen.** Los BOLR 2015-2016 usan el esquema funcional ANTIGUO (4.1=Sanidad); el `correspondencias.yml` codifica el NUEVO (2017+, 3.1=Sanidad), así que 403 M€ de sanidad (`4.1.2.1/2` atención primaria+especializada) se etiquetaban `soberania` (el prefijo de código gana al keyword) y solo `3.1.1.4` mal-mapeado quedaba en sanidad (→353 €/hab). Añadido `correspondencias_legacy.yml` (esquema antiguo) que `transform.py` usa para anio≤2016. Sanidad 2016 353→1276 €/hab (=2017, serie continua); %concepto 59→77 %.
- **Bandera(s) roja(s):** ✅ 2016 RESUELTO (mis-mapping). Pendiente menor: **2018 solo 9 conceptos** — la ventana `_ORG_PROGRAMA_WINDOWS[2018]=(230,523)` corta el bloque de servicios sociales (mayores/discapacidad/dependencia), que está en págs. 567-626 (con repetición en 732+, requiere dedup).
- **Seams documentados** (salto esperado, NO error): ~2017→19 (resumen-programas → funcional-economico)

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
