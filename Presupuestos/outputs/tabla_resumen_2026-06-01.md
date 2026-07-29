# Tabla resumen — Presupuestos extraídos por anualidad y CCAA

**Fecha:** 2026-06-01 (Noche 14) · ODESOCAN · Canarias en Datos
**Fuente:** `outputs/smoke_regresion_py.csv` (capa autonómica, motor Python verificado)

Leyenda: ● VERDE (extraído y verificado) · ✗ ERROR (raw no válido) · · sin datos

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Años |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andalucía | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 12 |
| Aragón | ● | ✗ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 11 |
| Asturias | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 11 |
| Baleares | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | · | 10 |
| Canarias | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 |
| Cataluña | ● | ● | ● | · | ● | ● | · | ● | ● | ● | · | ● | 9 |
| Castilla-La Mancha | · | · | · | · | · | · | · | · | · | ● | ● | ● | 3 |
| Cantabria | · | · | · | · | · | · | · | · | · | · | ● | · | 1 |
| Castilla y León | · | · | · | · | · | · | · | · | · | · | · | ● | 1 |
| Extremadura | · | · | · | · | · | · | · | · | · | · | ● | ● | 2 |
| Galicia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 |
| La Rioja | · | · | · | · | · | · | · | · | · | · | ● | · | 1 |
| Madrid | · | · | · | · | · | · | · | · | · | · | · | ● | 1 |
| Murcia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 |
| Navarra | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 |
| País Vasco | · | · | · | · | · | · | · | ● | · | ● | ● | ● | 4 |
| C. Valenciana | · | · | · | · | · | · | · | ● | ● | ● | ● | ● | 5 |
| **TOTAL/año** | **5** | **4** | **4** | **6** | **7** | **7** | **6** | **8** | **8** | **10** | **14** | **12** | **91** |

## Notas

- **91 ejercicios-año VERDE** en la capa autonómica, cubriendo las **17/17 CCAA**.
- Capa **Hacienda (SGCIEF)**: serie 2015–2025 completa para las 17 CCAA (concepto `total`), en `outputs/hacienda_staging.csv` — pendiente de carga matinal.
- **Único ROJO:** ara/2016 — el PDF disponible (`ingresos_gastos.pdf`, 60 págs.) es el articulado del BOA, no el libro de estados numéricos. No extraíble con el raw actual.
- Series largas (≥9 años): and (12), ara (11), ast (11), bal (10), can (9), cat (9), nav (9).
- CCAA aún delgadas (1 año): cnt, cym, gal, lar, mad, mur — sus ejercicios antiguos siguen bloqueados por reorganización de portales / anti-bot / IDs opacos.
