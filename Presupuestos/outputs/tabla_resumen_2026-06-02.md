# Tabla resumen — Presupuestos extraídos por anualidad y CCAA

**Fecha:** 2026-06-02 (Noche 15) · ODESOCAN · Canarias en Datos
**Fuente:** capa autonómica (motor Python verificado, spot-check reproducible esta noche)

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

- **91 ejercicios-año VERDE** en la capa autonómica, cubriendo las **17/17 CCAA**. Sin cambios de cobertura respecto a 2026-05-30/06-01.
- Capa **Hacienda (SGCIEF)**: serie 2015–2025 para las 17 CCAA (concepto `total`), pendiente de carga matinal.
- **Único ROJO:** ara/2016 — el PDF disponible es el articulado del BOA, no el libro de estados numéricos. Confirmado de nuevo esta noche (raw idéntico en disco).
- **Reproducibilidad verificada esta noche** (4 motores, aislado): gal/2025 (47 filas), mur/2025 (106), pvc/2025 (122), cym/2026 (103). Todos ≥30 filas y ≥5 conceptos.
- Series largas (≥9 años): and (12), ara (11), ast (11), bal (10), can (9), cat (9), nav (9).
- CCAA aún delgadas (1 año): cnt, cym, gal, lar, mad, mur — ejercicios antiguos bloqueados por reorganización de portales / IDs opacos. Requieren entorno con red (no el sandbox nocturno).
