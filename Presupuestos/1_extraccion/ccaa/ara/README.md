# Aragón — sub-pipeline de extracción

## Estado a 2026-07-01

Serie longitudinal **12/12 VERDE_PRAGM** (2015-2026). Motor único
`ara-pdf-program-total` para todos los ejercicios.

Cobertura conceptual: ~52-56 % concepto mapeado, 8-9 conceptos del catálogo
§1.6. El ~45 % no mapeado es estructural (cultura, deporte, transportes,
energía no entran en el catálogo de 13 conceptos).

## 2016 — resuelto

El ZIP histórico `presupuestos-zip` (Liferay aragon.es) contiene el documento útil con un
nombre engañoso:

- `Ley Presupuestos de la Comunidad Autónoma de Aragón para 2016 (BOA 22).pdf`
  → texto legislativo, sin tablas extraíbles para el extractor.
- `Presupuesto de ingresos 2016.pdf` → PDF rotulado como ingresos; las primeras páginas
  son ingresos, pero a partir del bloque posterior contiene el detalle de gastos por
  programa, con `PROGRAMA` y `TOTAL PROGRAMA`.
- Órdenes de control de ejecución, liquidación e inversiones reales → no sustituyen
  al presupuesto inicial completo.

El raw canónico `fuentes/raw/ara/2016/ingresos_gastos.pdf` apunta ahora al PDF rotulado
`Presupuesto de ingresos 2016.pdf`; la Ley BOA queda preservada como
`fuentes/raw/ara/2016/ley_presupuestos_boa22.pdf`.

## Prórrogas

- **2019** ← 2018: Orden HAP 206-2018 prorroga el presupuesto. PDF idéntico.
- **2025**, **2026** ← 2024: sin ley nueva. PDFs idénticos a 2024.

Importes esperados: 2018 = 2019 = 8.50 B€ ✓; 2024 = 2025 = 2026 = 11.76 B€ ✓.

## URLs declarativas en fuentes.yml

- Liferay aragon.es usa slugs por año (`estado-de-ingresos-y-gastos`,
  `estado-de-ingresos-y-gastos-1`, etc.), volátiles. Para 2015-2019, el ZIP
  global `presupuestos-zip` (108 MB) es la única fuente consolidada.
