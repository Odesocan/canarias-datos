# Limitaciones conocidas — Comunitat Valenciana (val)

> Advertencias de la extracción de Comunitat Valenciana. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `val-rpc-secciones` (+ `val-transform`). · Años: 2016-2026 (11 años) · Estado global: 2018-2026 VERDE (~81-86 %); 2016-2017 VERDE_PRAGM (~78 %).

## Perímetro / decisiones de consolidación
- Fuente: Tomo II de `hisenda.gva.es`, un frameset por sección (`T2_menu_epp_ES.html` → `T2_sec##_ES.html`) que enlaza una **RPC (Resumen General por Programas y Capítulos)** en PDF por sección.
- Se procesan todos los `secciones/sec*_RPC.pdf` y se toma el **"Total General" por subprograma** (última columna). Código de subprograma `NNN+L+NN` (p. ej. 411A00, 412B22, 313D00) o formato legacy `NNN.NN` en ediciones ≤2023 (soportado por el mismo regex).
- **Importes en MILES de euros** (cabecera "(En miles de euros)"): el extractor multiplica **×1000** para pasar a euros.
- Los años ≤2021 usan un esquema de portal legacy (`index_cas.html` → `T2/EUR/RGPC<NN>.pdf`); el motor lo soporta sin cambios (mismo formato de código `NNN.NN`).

## Conceptos NO separables (NULL estructural por diseño)
- Ninguno declarado como vacío a propósito. Los ~15-24 programas sin concepto por año son gasto **fuera de la matriz §1.6** (transporte/infraestructuras 513*-514*, medio ambiente 442*, cultura 452-457*, energía/minas 731A, comercio 761A, internacional 762A, tributos 613B, parque móvil 612H…), correctamente NULL.

## Advertencias de calidad del dato
- El motor distingue **stubs** (secciones inexistentes = HTML 404 con extensión `.pdf`, ignorados) de **huecos reales** (sección con menú válido pero sin PDF publicado/descargado): estos últimos se reportan en `notes` en vez de desaparecer en silencio.
- **FIX 2026-07-02 — códigos legacy `NNN.NN` (≤2023) sin mapear:** el formato antiguo usa `011.10 Servicio de la Deuda` (4,1 B€ en 2016 = 23,6 % del total, iba a NULL) y `313.60/.70` (SS, →dependencia), `313.30 Menor` (→diversidad), `313.20 Drogodependencias` (→salud_mental). Sus equivalentes modernos (`011A00`, `313I00/J00`, `313C00`, `313B00`) sí estaban mapeados → la serie de `direccion` saltaba de 0,9 B (2016) a 10,7 B (2026) por artefacto. Añadidos al `correspondencias.yml` (prefijo `011*` + exactos ENTRECOMILLADOS — sin comillas YAML los lee como float `313.6`≠`313.60`). Tras el fix: `direccion` continua 4,9→10,7 B; 2016-2017 pasan a **VERDE estricto** (13 conceptos).
- Cobertura alta y creciente (VERDE estricto desde 2016 tras el fix).

## Años faltantes / problemáticos
- **2015 y anteriores: SIN FUENTE.** El portal GVA devuelve 404 para ≤2015 (no publicado con el esquema recuperable). La serie arranca en **2016**.
- **2026 — sección `sec26` = 404 en GVA — RESUELTO 2026-07-27 (no era hueco de datos).** Verificado en vivo contra `T2_menu_epp_ES.html`: la sección 26 ("Vicepresidencia Segunda y Conselleria para la Recuperación..." en 2025) se **fusionó** con la sección 05 de 2025 ("Presidencia de la Generalitat") en una única sección 05 de 2026 ("Vicepresidencia Segunda y Conselleria de Presidencia"). Es reorganización de gobierno, no un documento sin publicar: `sec05_RPC.pdf` (805 KB, PDF válido) ya incluye ese gasto íntegro. El extractor sigue reportando el 404 de `sec26` en `notes` por diseño (distingue stub de sección retirada), pero **no falta gasto**. 2026 es VERDE completo.
- `salud_mental` ya presente en TODA la serie desde 2016 tras el fix (legacy `313.20` Drogodependencias ≈12 M/año; salta a ~192-219 M en 2025-26 al ampliarse el programa moderno `313B00`). 13 conceptos en todos los años.

## Notas de uso
- La serie útil es **2016-2026**; no hay dato oficial de 2015 por este motor.
- No asumas `salud_mental` antes de 2024.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py val` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `16:1165 17:1200 18:1261 19:1309 20:1335 21:1486 22:1546 23:1629 24:1677 25:1778 26:1825` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible. Importes en **miles ×1000**. 2015 sin fuente.
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
