# Limitaciones conocidas — Castilla-La Mancha (clm)

> Advertencias de la extracción de Castilla-La Mancha. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `clm-gastosf-csv` (datos abiertos, gasto funcional multi-año, 2015-2021) · `clm-tomo-I-resumen-secciones` (PDF Tomo I, "GASTOS. RESUMEN POR SECCIONES Y PROGRAMAS", 2022-2026) · Fallback `clm-xlsx-adjunto` si el operador deja `programas*.{xlsx,csv}` · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~63-66 % concepto, 13/13 conceptos).

## Perímetro / decisiones de consolidación
- **⚠️ Unidades distintas según la rama — punto crítico:**
  - **CSV `gastosf` (2015-2021): importes en EUROS** (formato en-US, columna `Presupuesto Gasto`). **NO** se multiplican.
  - **PDF Tomo I (2022-2026): importes en MILES de euros** → el extractor los **multiplica ×1000**. La cabecera del tomo lo advierte ("(IMPORTE EN MILES DE EUROS)").
  Si tocas el extractor, respeta esta asimetría: mezclar unidades desplaza sanidad ~3 órdenes de magnitud.
- CSV: se toman las filas de detalle (`Id Programa` no vacío); se descartan los subtotales de política. Código de programa (3 díg+letra) → concepto vía `correspondencias.yml`.
- PDF: se entra en modo lectura solo tras la cabecera real de sección (no desde el TOC) y se corta en "DISTRIBUCIÓN DE CAPÍTULOS POR SECCIONES". Subtotales "Total Sección" ignorados.

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno conocido (los 13 conceptos aparecen en la serie). El ~34-36 % de filas sin concepto es gasto no-social fuera de catálogo (contabilidad `612X`, deuda `011A`, fomento `511A`, reservas de crédito, capítulos económicos sueltos) → esperado.

## Advertencias de calidad del dato
- **FIX 2026-07-02 (correspondencias):** (1) `324A` "FP para el empleo" se renombró en 2024 a "FP EN EL ÁMBITO LABORAL" y dejó de casar el keyword → empleo perdía ~90 M€/año; ahora mapeado por código exacto (`324A`/`324B`→empleo). (2) `salud_mental` estaba FABRICADO con `313A` "Programas sociales básicos" (97-101 M) y `313E` "Atención al menor" (57-66 M), que NO son salud mental → retirados (313E→diversidad; salud_mental queda NULL estructural, CLM no tiene programa propio). (3) `432A` "Gestión del urbanismo" (10-15 M) iba a turismo por colisión de código exacto → retirado de turismo (queda en vivienda). Efecto: n_conc pasa de 13 a 12 (se pierde el salud_mental ficticio; ganancia de integridad).
- **Salto del *total* entre ramas 2021→2022 (CSV→PDF):** el total pasa de 9,67 (CSV 2021) a ~12,26 (PDF 2022). Es un **artefacto de alcance CSV vs PDF**, no un error de magnitud. Verificado: **sanidad SÍ es continua** cruzando los dos motores (2021=3.718 CSV → 2022=3.673 → 2023=3.676 → 2024=3.910 PDF mil M€). Los años PDF entre sí son coherentes (2022/23 ≈12,3-12,4 vs 2024-26 ≈12,5).
- Parser CSV tolerante: algunas líneas del datos abiertos CLM vienen con la línea entera entre comillas y comillas internas duplicadas (`""`); se desenvuelven en `_split_csv_line` antes de delegar en `csv.reader`.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos.

## Notas de uso
- Compara **niveles de *total*** solo dentro de la misma rama (2015-2021 CSV entre sí; 2022-2026 PDF entre sí); el escalón 2021→2022 es de alcance, no económico.
- Para series de **conceptos sociales** (p. ej. sanidad) sí puedes cruzar las dos ramas: la continuidad está verificada.
- No re-apliques ×1000 a los años CSV ni lo omitas en los años PDF.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py clm` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1177 16:1283 17:1329 18:1370 19:1370 20:1483 21:1813 22:1792 23:1793 24:1907 25:1870 26:2013` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Unidad **miles vs euros**: si el total salta ×1000 entre años, es error de unidad (PDF en miles ×1000, CSV en euros).
- **Seams documentados** (salto esperado, NO error): 2021→22 (CSV gastosf → PDF tomo I)

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
