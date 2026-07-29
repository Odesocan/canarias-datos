# Tabla resumen Presupuestos · ODESOCAN Canarias en Datos
_Noche 9 — 2026-05-28_  
_50 ejercicios-año verificados; 17 CCAA × 12 años (2015-2026)_  
_Importe total presupuesto de gastos en mil M € (extracción Python standalone)_

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| and | 37.97 | · | · | · | · | · | · | · | 24.24 | 24.45 | 25.49 | 26.80 |
| ara | · | · | · | · | · | · | · | · | · | 11.76 | · | · |
| ast | · | · | · | · | · | · | · | · | · | 5.44 | 5.75 | 6.03 |
| bal | · | · | · | · | · | · | · | 6.35 | 7.07 | 7.10 | 6.33 | · |
| can | · | · | · | 6.99 | 7.51 | 7.69 | 8.04 | 8.60 | 9.70 | 10.74 | 11.10 | 11.91 |
| cat | · | 22.98 | 23.45 | · | 24.83 | 25.79 | · | 27.48 | 29.36 | 30.49 | · | 35.20 |
| clm | · | · | · | · | · | · | · | · | · | 12.47 | 12.72 | 12.90 |
| cnt | · | · | · | · | · | · | · | · | · | · | 3.97 | · |
| cym | · | · | · | · | · | · | · | · | · | · | · | 14.56 |
| ext | · | · | · | · | · | · | · | · | · | · | 5.40 | 5.07 |
| gal | · | · | · | · | · | · | · | · | · | · | 14.19 | · |
| lar | · | · | · | · | · | · | · | · | · | · | 1.71 | · |
| mad | · | · | · | · | · | · | · | · | · | · | · | 52.13 |
| mur | · | · | · | · | · | · | · | · | · | · | 6.82 | · |
| nav | · | · | · | · | · | · | · | · | · | · | · | 6.32 |
| pvc | · | · | · | · | · | · | · | 27.81 | · | 32.91 | 34.30 | 34.45 |
| val | · | · | · | · | · | · | · | 27.97 | 28.44 | 29.73 | 32.29 | · |
|------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| **Σ visible** | 38.0 | 23.0 | 23.4 | 7.0 | 32.3 | 33.5 | 8.0 | 98.2 | 98.8 | 165.1 | 160.1 | 205.4 |
| **nº CCAA**   | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 5 | 5 | 9 | 12 | 10 |

## Conceptos cubiertos por CCAA

| CCAA | filas mediana | pct concepto rango | n conceptos | motor extracción |
|------|---:|---:|---:|------|
| and | 88 | 70.2-73.9 % | 12-12 | `and-ckan-csv+and-transform` |
| ara | 198 | 54.5-54.5 % | 9-9 | `ara-pdf-program-total+ara-transform` |
| ast | 104 | 67.3-68.6 % | 10-10 | `ast-distribucion-gasto+ast-transform` |
| bal | 144 | 73.4-75.3 % | 13-13 | `bal-frameset-secciones+bal-transform` |
| can | 141 | 65.0-66.9 % | 12-13 | `can-tomo3-resumen-programas+can-transform` |
| cat | 105 | 63.2-64.1 % | 13-13 | `cat-programa-totals+cat-transform` |
| clm | 113 | 64.9-65.5 % | 13-13 | `clm-tomo-I-resumen-secciones+clm-transform` |
| cnt | 91 | 54.9-54.9 % | 12-12 | `cnt-total-programa-suma-servicios+cnt-transform` |
| cym | 103 | 85.4-85.4 % | 13-13 | `cym-jcyl-xls+cym-transform` |
| ext | 73 | 66.2-69.9 % | 12-12 | `ext-tomo-eig-suma-capitulos+ext-transform` |
| gal | 47 | 78.7-78.7 % | 8-8 | `gal-csv-abertos-xunta+gal-transform` |
| lar | 56 | 76.8-76.8 % | 11-11 | `lar-camelot-funcional-economico+lar-transform` |
| mad | 103 | 50.5-50.5 % | 11-11 | `mad-libro-03-centros+mad-transform` |
| mur | 106 | 86.8-86.8 % | 10-10 | `mur-html+mur-transform` |
| nav | 167 | 77.8-77.8 % | 12-12 | `nav-breakdowns-functional+nav-transform` |
| pvc | 120 | 43.4-44.3 % | 8-8 | `pvc-csv-tidy+pvc-transform` |
| val | 173 | 83.9-86.2 % | 12-13 | `val-rpc-secciones+val-transform` |

## Notas

- Umbral pragmático: ≥30 filas, ≥35 % concepto y ≥5 conceptos (cuaderno §1.6).
- Capa `autonomica`. Conciliación contra capa `hacienda` SGCIEF pendiente del run R matinal.
- and/2015 procede de CSV CKAN (formato no consolidado); el salto -36 % vs 2023 está dentro de lo esperado.
