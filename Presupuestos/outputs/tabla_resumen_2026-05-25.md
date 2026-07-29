# Tabla resumen — Presupuestos por anualidad extraídos por CCAA

ODESOCAN · Canarias en Datos — pipeline `presupuestos.ced_presupuestos`, capa autonómica.
Generado: 2026-05-25 (Noche 7). Verificación standalone `python3 -m ccaa` (sin R/psql en sandbox).

## Cobertura — nº de filas extraídas por ejercicio

Celda: `filas` extraídas. — = ejercicio no verificado en este ciclo.

| CCAA | 2015 | 2020 | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|-----|-----|-----|-----|-----|-----|-----|
| Andalucía (`and`) | 114 | — | — | — | 88 | 88 | 88 |
| Baleares (`bal`) | — | — | 143 | 150 | 145 | 141 | — |
| Canarias (`can`) | — | — | 135 | 135 | 140 | 141 | 143 |
| Cataluña (`cat`) | — | 105 | 105 | 105 | 105 | — | 106 |
| Castilla y León (`cym`) | — | — | — | — | — | — | 103 |
| Galicia (`gal`) | — | — | — | — | — | 47 | — |
| Murcia (`mur`) | — | — | — | — | — | 106 | — |
| Navarra (`nav`) | — | — | — | — | — | — | 167 |
| País Vasco (`pvc`) | — | — | 116 | — | 118 | 122 | — |
| C. Valenciana (`val`) | — | — | 169 | 174 | 173 | 174 | — |

## Estado de verificación por ejercicio

| CCAA | Año | Estado | Filas | % concepto | Nº conceptos | Importe total (B€) |
|------|-----|--------|-------|-----------|--------------|--------------------|
| Andalucía | 2015 | VERDE_PRAGM | 114 | 70.2 % | 12 | 37.97 |
| Andalucía | 2024 | VERDE_PRAGM | 88 | 73.9 % | 12 | 24.45 |
| Andalucía | 2025 | VERDE_PRAGM | 88 | 72.7 % | 12 | 25.49 |
| Andalucía | 2026 | VERDE_PRAGM | 88 | 72.7 % | 12 | 26.80 |
| Baleares | 2022 | VERDE_PRAGM | 143 | 73.4 % | 13 |  |
| Baleares | 2023 | VERDE_PRAGM | 150 | 75.3 % | 13 |  |
| Baleares | 2024 | VERDE_PRAGM | 145 | 75.2 % | 13 |  |
| Baleares | 2025 | VERDE_PRAGM | 141 | 74.5 % | 13 |  |
| Canarias | 2022 | VERDE_PRAGM | 135 | 65.2 % | 12 |  |
| Canarias | 2023 | VERDE_PRAGM | 135 | 65.2 % | 12 |  |
| Canarias | 2024 | VERDE_PRAGM | 140 | 65.0 % | 12 |  |
| Canarias | 2025 | VERDE_PRAGM | 141 | 66.0 % | 12 |  |
| Canarias | 2026 | VERDE_PRAGM | 143 | 65.7 % | 12 |  |
| Cataluña | 2020 | VERDE_PRAGM | 105 | 63.8 % | 13 | 25.79 |
| Cataluña | 2022 | VERDE_PRAGM | 105 | 63.8 % | 13 | 27.48 |
| Cataluña | 2023 | VERDE_PRAGM | 105 | 63.8 % | 13 | 29.36 |
| Cataluña | 2024 | VERDE_PRAGM | 105 | 63.8 % | 13 | 30.49 |
| Cataluña | 2026 | VERDE_PRAGM | 106 | 63.2 % | 13 | 35.20 |
| Castilla y León | 2026 | VERDE | 103 | 85.4 % | 13 |  |
| Galicia | 2025 | VERDE_PRAGM | 47 | 78.7 % | 8 |  |
| Murcia | 2025 | VERDE | 106 | 86.8 % | 10 |  |
| Navarra | 2026 | VERDE_PRAGM | 167 | 77.8 % | 12 |  |
| País Vasco | 2022 | VERDE_PRAGM | 116 | 44.0 % | 8 |  |
| País Vasco | 2024 | VERDE_PRAGM | 118 | 44.1 % | 8 |  |
| País Vasco | 2025 | VERDE_PRAGM | 122 | 44.3 % | 8 |  |
| C. Valenciana | 2022 | VERDE | 169 | 84.0 % | 12 |  |
| C. Valenciana | 2023 | VERDE | 174 | 83.9 % | 12 |  |
| C. Valenciana | 2024 | VERDE | 173 | 85.5 % | 13 |  |
| C. Valenciana | 2025 | VERDE | 174 | 86.2 % | 13 |  |

## Notas

- **29 ejercicios-año** verificados VERDE / VERDE_PRAGM, **10 CCAA**: Andalucía, Baleares, Canarias, Cataluña, Castilla y León, Galicia, Murcia, Navarra, País Vasco, C. Valenciana.
- **VERDE_PRAGM**: ≥30 filas, ≥35 % de filas con concepto del catálogo §1.6, ≥5 conceptos distintos. El resto de filas son partidas fuera de los 13 conceptos canónicos (cultura, deporte, seguridad, infraestructuras…).
- **7 CCAA** con módulo pero sin verificar en este ciclo: Aragón, Asturias, Castilla-La Mancha, Cantabria, Extremadura, La Rioja, Madrid (verificación en noches previas; pendiente re-confirmar).
- El **importe total** es la suma de los totales de programa extraídos; es un indicador de magnitud, no un total auditado. `and/2015` (37,97 B€) procede de la rama CKAN —líneas de gasto agregadas— y no es comparable directamente con los resúmenes PDF de and/2024-2026.
- Hueco conocido: **cat/2025** sin raw descargado.
