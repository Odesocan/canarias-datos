# Tabla resumen Presupuestos · ODESOCAN Canarias en Datos
_Noche 11 — 2026-05-29 (sesión bal + ast)_  
_82 ejercicios-año cargables; 17 CCAA × 2015-2026_  
_Presupuesto total de gastos (capa autonómica) en miles de millones € (mM€)_

| CCAA | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | n |
|------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|---:|
| and | 37.97 | 40.37 | 28.18 | 29.68 | 29.77 | 49.58 | 55.83 | 34.99 | 24.24 | 24.45 | 25.49 | 26.80 | 12 |
| ara | 7.11 | · | 7.78 | 8.50 | 8.50 | 8.87 | 10.11 | 10.03 | 11.16 | 11.76 | 11.76 | 11.76 | 11 |
| ast | 5.13 | 3.53 | 3.65 | 3.82 | 3.91 | 4.03 | 4.47 | · | 5.20 | 5.44 | 5.75 | 6.03 | 11 |
| bal | 2.73 | 3.22 | · | 3.85 | 4.25 | 4.57 | 4.60 | 6.35 | 7.07 | 7.10 | 6.33 | · | 10 |
| can | · | · | · | 6.99 | 7.51 | 7.69 | 8.04 | 8.60 | 9.70 | 10.74 | 11.10 | 11.91 | 9 |
| cat | 32.48 | 22.98 | 23.45 | · | 24.83 | 25.79 | · | 27.48 | 29.36 | 30.49 | · | 35.20 | 9 |
| clm | · | · | · | · | · | · | · | · | · | 12.47 | 12.72 | 12.90 | 3 |
| cnt | · | · | · | · | · | · | · | · | · | · | 3.97 | · | 1 |
| cym | · | · | · | · | · | · | · | · | · | · | · | 14.56 | 1 |
| ext | · | · | · | · | · | · | · | · | · | · | 5.40 | 5.07 | 2 |
| gal | · | · | · | · | · | · | · | · | · | · | 14.19 | · | 1 |
| lar | · | · | · | · | · | · | · | · | · | · | 1.71 | · | 1 |
| mad | · | · | · | · | · | · | · | · | · | · | · | 52.13 | 1 |
| mur | · | · | · | · | · | · | · | · | · | · | 6.82 | · | 1 |
| nav | · | · | · | · | · | · | · | · | · | · | · | 6.32 | 1 |
| pvc | · | · | · | · | · | · | · | 27.81 | · | 32.91 | 34.30 | 34.45 | 4 |
| val | · | · | · | · | · | · | · | 27.97 | 28.44 | 29.73 | 32.29 | · | 4 |
|------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|---:|
| **Σ visible** | 85.4 | 70.1 | 63.1 | 52.8 | 78.8 | 100.5 | 83.0 | 143.2 | 115.2 | 165.1 | 171.8 | 217.1 | 82 |
| **nº CCAA** | 5 | 4 | 4 | 5 | 6 | 6 | 5 | 7 | 7 | 9 | 13 | 11 | |

Leyenda: `·` = ejercicio no declarado. Pendientes conocidos: bal 2017/2026, ast 2022 (documento sin tabla de gasto), ara 2016 (ROJO).

## Novedad de esta sesión (N11) — Baleares y Asturias

- **bal**: 4 → 10 años. Nuevos VERDE: 2015 (2,73), 2016 (3,22), 2018 (3,85), 2019 (4,25), 2020 (4,57), 2021 (4,60 mM€). Descarga de las secciones `titol*_d.pdf` del Tomo III por año (numeración variable: 2021 usa titol10–28). Extractor parcheado para ignorar stubs no-PDF de índices inexistentes.
- **ast**: 3 → 11 años. Nuevos VERDE: 2015 (5,13), 2016 (3,53), 2017 (3,65), 2018 (3,82), 2019 (3,91), 2020 (4,03), 2021 (4,47), 2023 (5,20 mM€). Dos formatos de fuente: tomos de transparencia.asturias.es (2015-2020) y leyes BOPA (2021,2023); sidecars pagetext generados para los PDF grandes (>600-1537 págs).
- **Pendientes**: bal 2017 (no hay `pr2017` en /ant/, buscar URL) y 2026 (ruta distinta, fuera de /ant/); ast 2022 (el PDF del BOPA es sólo el articulado, sin la tabla de distribución del gasto → buscar anexo de estados numéricos).

> Nota de heterogeneidad: ast 2015 (5,13 mM€, doc PROYECTO completo) queda por encima de 2016 (3,53, tomo t2). Fuentes distintas; conciliar en capa Hacienda SGCIEF para serie comparable.