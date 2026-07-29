# Tabla resumen — Presupuestos extraídos por anualidad y CCAA

**Fecha:** 2026-06-08 (Noche 17) · ODESOCAN · Canarias en Datos
**Fuente:** capa autonómica, motor Python verificado (catálogo autoritativo `outputs/smoke_regresion_py.csv`).

Leyenda: ● VERDE (extraído y verificado) · ✗ ERROR (raw no válido) · · sin datos

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Años | Filas | Conc. medio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andalucía | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 12 | 1208 | 12.0 |
| Aragón | ● | ✗ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 11 | 1961 | 9.9 |
| Asturias | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 11 | 1069 | 9.5 |
| Baleares | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | · | 10 | 1058 | 12.3 |
| Canarias | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 | 1261 | 12.3 |
| Cataluña | ● | ● | ● | · | ● | ● | · | ● | ● | ● | · | ● | 9 | 933 | 13.0 |
| Castilla-La Mancha | · | · | · | · | · | · | · | · | · | ● | ● | ● | 3 | 340 | 13.0 |
| Cantabria | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 91 | 12.0 |
| Castilla y León | · | · | · | · | · | · | · | · | · | · | · | ● | 1 | 103 | 13.0 |
| Extremadura | · | · | · | · | · | · | · | · | · | · | ● | ● | 2 | 147 | 13.0 |
| Galicia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 47 | 8.0 |
| La Rioja | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 56 | 11.0 |
| Madrid | · | · | · | · | · | · | · | · | · | · | · | ● | 1 | 103 | 11.0 |
| Murcia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 106 | 10.0 |
| Navarra | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 | 1520 | 12.1 |
| País Vasco | · | · | · | · | · | · | · | ● | · | ● | ● | ● | 4 | 478 | 8.0 |
| C. Valenciana | · | · | · | · | · | · | · | ● | ● | ● | ● | ● | 5 | 866 | 12.6 |
| **TOTAL/año** | **5** | **4** | **4** | **6** | **7** | **7** | **6** | **8** | **8** | **10** | **14** | **12** | **91** | | |

**Cobertura autonómica: 91 ejercicios-año VERDE en 17/17 CCAA** (rango 2015–2026) + capa Hacienda 2015–2025. Único ROJO: ara/2016 (articulado BOA, sin estados numéricos).

## Detalle de ejercicios por CCAA

| CCAA | Ejercicios extraídos | Nº | Motor |
|---|---|---|---|
| Andalucía | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 | 12 | and-ckan-csv |
| Aragón | 2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 | 11 | ara-pdf-program-total |
| Asturias | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2023, 2024, 2025, 2026 | 11 | ast-distribucion-gasto |
| Baleares | 2015, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | 10 | bal-frameset-secciones |
| Canarias | 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 | 9 | can-tomo3-resumen-programas |
| Cataluña | 2015, 2016, 2017, 2019, 2020, 2022, 2023, 2024, 2026 | 9 | cat-programa-suma-secciones |
| Castilla-La Mancha | 2024, 2025, 2026 | 3 | clm-tomo-I-resumen-secciones |
| Cantabria | 2025 | 1 | cnt-total-programa-suma-servicios |
| Castilla y León | 2026 | 1 | cym-jcyl-xls |
| Extremadura | 2025, 2026 | 2 | ext-tomo-eig-suma-capitulos |
| Galicia | 2025 | 1 | gal-csv-abertos-xunta |
| La Rioja | 2025 | 1 | lar-camelot-funcional-economico |
| Madrid | 2026 | 1 | mad-libro-03-centros |
| Murcia | 2025 | 1 | mur-html |
| Navarra | 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 | 9 | nav-breakdowns-functional |
| País Vasco | 2022, 2024, 2025, 2026 | 4 | pvc-csv-tidy |
| C. Valenciana | 2022, 2023, 2024, 2025, 2026 | 5 | val-rpc-secciones |

## Notas (Noche 17 · 2026-06-08)

- Catálogo estable en **91 ejercicios-año VERDE** (17/17 CCAA), sin cambios de cobertura respecto a la Noche 16.
- **Verificación de código sana**: sanity-check fresco de esta noche reproduce VERDE en val (2022/23/25), pvc (2022/24/25/26), cym/2026 y mur/2025 con el código actual.
- **Entorno degradado** (recurrente): el mount del sandbox volvió a dar `Resource deadlock avoided` en ~559/1003 archivos raw; además los procesos en background no sobreviven entre llamadas, impidiendo re-correr la regresión completa de las 92 cells esta noche. Se preservó intacto el CSV autoritativo (no se sobrescribió con lecturas parciales corruptas).
- **Sin ejercicios nuevos esta noche**: aunque hubo red disponible, la descarga de raw binarios (PDF/XLS) no es viable con las herramientas permitidas + escritura en mount inestable. Pendiente para run con entorno estable.
