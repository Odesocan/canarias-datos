# Estado de extracción — Comunitat Valenciana (`val`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** HTML · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `val-rpc-secciones`  
**Portal oficial:** https://hisenda.gva.es/auto/presupuestos/

## 1 · Fase del proceso

**Extracción consolidada (11/11 años registrados en VERDE).**

- Años en VERDE: **11** (2016–2026)
- Años registrados en `fuentes.yml`: **11** (2016–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2016 | ✅ Extraído (VERDE) | 129 | 78.3% | 12/13 |
| 2017 | ✅ Extraído (VERDE) | 128 | 78.9% | 12/13 |
| 2018 | ✅ Extraído (VERDE) | 128 | 81.2% | 12/13 |
| 2019 | ✅ Extraído (VERDE) | 131 | 81.7% | 12/13 |
| 2020 | ✅ Extraído (VERDE) | 153 | 83.7% | 12/13 |
| 2021 | ✅ Extraído (VERDE) | 154 | 85.1% | 12/13 |
| 2022 | ✅ Extraído (VERDE) | 169 | 84.0% | 12/13 |
| 2023 | ✅ Extraído (VERDE) | 174 | 83.9% | 12/13 |
| 2024 | ✅ Extraído (VERDE) | 173 | 85.5% | 13/13 |
| 2025 | ✅ Extraído (VERDE) | 174 | 86.2% | 13/13 |
| 2026 | ✅ Extraído (VERDE) | 176 | 86.4% | 13/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 86% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ✅ capturado |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ✅ capturado |
| I+D+i (`idi`) | ✅ capturado |
| Dependencia (`dependencia`) | ✅ capturado |
| Discapacidad (`discapacidad`) | ✅ capturado |
| Salud mental (`salud_mental`) | ✅ capturado |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Cobertura conceptual completa (13/13).** Ningún concepto del catálogo falta.
- **Años sin fuente registrada (2015–2026):** 2015 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015.
2. **Reintentar `sec26_RPC.pdf` de 2026** cuando GVA lo publique (hoy 404 — ver §5).

## 5 · Revisión / test de bugs (2026-06-29)

Auditoría de la serie 2016-2026 (motor `val-rpc-secciones`). Resultado: **extracción
sólida**, un único hueco de datos (de origen) y una mejora de robustez aplicada.

**Verificado OK:**
- **Núcleo correcto.** El "Total General" es el último número de cada fila RPC; cotejado
  manualmente (p.ej. 412B22 Atención Hospitalaria 2024: Op.Corr 3.905.581,29 + Op.Cap
  341.015,39 + Op.Fin 0 = Total 4.246.596,68 miles → ×1000 = 4,25 mil M€). ✔
- **Escalado miles→euros correcto** (sanity de magnitud: sanidad 5,9→9,2 mil M€ 2016-2026,
  total 17→33 mil M€, serie monótona sin saltos). ✔
- **Sin duplicados:** 0 códigos repetidos por año; ambos formatos de código
  (`NNN.NN` 2016-2023 y `NNNXNN` 2024-2026) se capturan. ✔
- **Secciones:** todas las conselleries con menú real tienen su PDF, salvo el hueco abajo.

**Hueco de datos (origen GVA):**
- **2026 sec26** ("Vicepresidencia Segunda y Conselleria para la Recuperación Económica
  y Social") → su `RPC-26-50-A-0007-...pdf` da **404 en hisenda.gva.es** (no publicado).
  Impacto: ~14 M€ / 3 subprogramas (`120A00`, `120D00`, `442G00`) = **0,04 % del total** →
  despreciable en magnitud, pero hueco de cobertura real. No es un bug del extractor.

**Mejora de robustez aplicada (no cambia filas; VERDE intacto):**
- Antes el extractor **descartaba en silencio** cualquier `sec*_RPC.pdf` sin cabecera
  `%PDF`, por lo que un 404 desaparecía sin rastro. Ahora distingue un *placeholder vacío*
  (sección inexistente ese año) de un *hueco real* (sección con menú `T2_sec##_ES.html`
  con contenido pero sin PDF) y lo **reporta en `notes`**:
  `⚠️ 1 sección(es) con menú pero sin PDF (hueco de datos): sec26`.

---
*Revisado a mano (test de bugs) el 2026-06-29. Foto de regresión en
`outputs/smoke_regresion_py.csv`.*
