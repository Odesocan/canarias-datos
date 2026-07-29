# Informe QA — Etapa de extracción · Área de Sanidad

**Canarias en Datos · ODESOCAN** — ejecutado el 22/07/2026 contra la API INCLASNS (Ministerio de Sanidad).
Fuente: `raw_sanidad.rds` (19.592 filas · 18 indicadores · 7 grupos). Niveles territoriales esperados: **20** (17 CCAA + Ceuta + Melilla + Media Estatal).

## 1. Veredicto

Extracción **válida y utilizable** (16 indicadores). El indicador de gasto público per cápita (INCLASNS 6020), que solo tenía cobertura nacional, se ha **sustituido por la variable de gasto sanitario sobre PIB importada del área de Presupuestos** (17 CCAA, 2015–2026, validada). Se ha **retirado autopercepción de salud (1060)** por discontinuidad; Estado de salud queda solo con años de vida saludable a los 65 (1050). El índice de mortalidad evitable se **reconstruye y valida** correctamente (2.100 filas, 0 NA).

## 2. Cobertura, continuidad y plausibilidad por indicador

| Grupo | Indicador (código) | Géneros | Nº CCAA | Continua 2015→ | Canarias cont. | Rango de valores (mín–mediana–máx) |
|---|---|---|---:|:---:|:---:|---|
| estado_salud | Años vida saludable 65 (1050) | H/M/T | 20 | ✅ | ✅ | 12,6 – 18,0 – 22,9 años |
| mort_evitable | Mort. prematura cáncer (1240) | H/M/T | 20 | ✅ | ✅ | 0,0 – 108,1 – 260,6 /100k |
| mort_evitable | Mort. prematura cardiopatía (1250) | H/M/T | 20 | ✅ | ✅ | 0,0 – 31,1 – 173,9 /100k |
| mort_evitable | Mort. prematura diabetes (1260) | H/M/T | 20 | ✅ | ✅ | 0,0 – 6,4 – 55,2 /100k |
| mort_evitable | Mort. prematura ictus (1270) | H/M/T | 20 | ✅ | ✅ | 0,0 – 9,0 – 88,3 /100k |
| mort_evitable | Mort. prematura EPOC (1280) | H/M/T | 20 | ✅ | ✅ | 0,0 – 17,2 – 98,4 /100k |
| recursos | Médico AE (4050) | T | 20 | ✅ | ✅ | 1,10 – 1,74 – 2,88 /1.000 |
| recursos | Médico AP (4060) | T | 20 | ✅ | ✅ | 0,58 – 0,76 – 1,12 /1.000 |
| recursos | Enfermería AE (4070) | T | 20 | ✅ | ✅ | 1,86 – 3,07 – 6,91 /1.000 |
| recursos | Enfermería AP (4080) | T | 20 | ✅ | ✅ | 0,45 – 0,66 – 1,12 /1.000 |
| recursos | Camas (4090) | T | 20 | ✅ | ✅ | 1,90 – 3,30 – 4,91 /1.000 |
| gasto | Gasto sanitario / PIB (Presupuestos) | T | **17** | ✅ | ✅ | 2,96 – 5,94 – 8,94 % del PIB |
| gasto | % gasto en farmacia (6060) | T | **18** | ✅ | ✅ | 11,2 – 17,9 – 28,4 % |
| accesibilidad | Espera quirúrgica (8200) | T | 20 | ✅ | ✅ | 28 – 94 – 286 días |
| accesibilidad | Espera 1ª consulta AE (8290) | T | 20 | ✅ | ✅ | 9,5 – 66,0 – 175,8 días |
| resultados | Reingresos psiquiátricos (7140) | H/M/T | 20 | ✅ | ✅ | 1,7 – 10,0 – 29,3 % |
| poblacion | Población total (9000) | H/M/T | 20 | ✅ | ✅ | 28.174 – 1.055.660 – 49.355.143 |

## 3. Hallazgos y recomendaciones

1. **🟢 RESUELTO — `gasto_pub_pc` (6020) solo tenía cobertura NACIONAL**. Se ha descartado y sustituido por la variable **`gasto_pib_sanidad`** importada del área de Presupuestos de Canarias en Datos (ver sección 4 bis): gasto sanitario autonómico presupuestado como % del PIB regional, con desglose por CCAA. Es una medida de esfuerzo comparable entre comunidades, que es el objeto del área.
2. **🟠 `gasto_farmacia_pct` (6060) no cubre Ceuta ni Melilla** (18 de 20 niveles). Aceptable si se documenta; las ciudades autónomas quedarán como NA en esa variable.
3. **🟢 RESUELTO — `autoperc_salud` (1060) se ha retirado** por discontinuidad (encuesta ENSE por oleadas). La dimensión Estado de salud queda con años de vida saludable a los 65 (1050), que es continua (2006–2023) y desagregada por género.
4. **🟡 Componentes de mortalidad con mínimo 0,00**: corresponde a Ceuta/Melilla en años con cero defunciones prematuras registradas para causas poco frecuentes (poblaciones pequeñas). No es un error de extracción, pero conviene tratarlo con cautela al interpretar el índice en las ciudades autónomas.
5. **🟢 Sin literales de CCAA sin mapear**: el diccionario territorial resuelve el 100 % de los nombres devueltos por la API.
6. **🟢 Géneros correctos**: los indicadores de resultado (estado de salud, mortalidad, reingresos, población) traen Hombres/Mujeres/Total; los de sistema (recursos, gasto, accesibilidad) solo Total, como corresponde a su naturaleza.

## 4. Validación del índice de mortalidad evitable

Reconstrucción portada de Prevención (`build_mort_evitable_idx`), verificada sobre los datos reales:

- **Normalizadores (media histórica nacional por componente):** cáncer 105,25 · cardiopatía 35,86 · ictus 20,48 · EPOC 11,73 · diabetes 7,85 (por 100.000). Confirman el motivo de la normalización: el cáncer multiplica por ~13 a la diabetes.
- **Cobertura:** 2.100 filas (CCAA × año × género), **0 NA**.
- **Distribución (ratio):** 0,29 – **mediana 0,92** – 3,33 → índice centrado cerca de 1, como en el proyecto original.
- **Reescalado 0–100:** 0,0 – 100,0 (correcto).
- **Serie nacional reciente (Media Estatal, total):** 2020→2024 en torno a 0,62–0,68 (mortalidad prematura por debajo de la media histórica 1990–2024, coherente con la tendencia descendente).
- **Canarias vs Media Estatal (2024, total):** Canarias 0,745 vs 0,630 → **Canarias registra un 18 % más de mortalidad evitable que la media estatal**.

## 4 bis. Validación del gasto sanitario sobre PIB (fuente: Presupuestos)

Variable `gasto_pib_sanidad` importada del fichero `presupuestos_pib_integrado_*.csv` del área de Presupuestos (`tools/integrar_pib_regional.py`). Es gasto **presupuestado** (esfuerzo), no liquidado.

- **Cobertura:** 204 filas · **17 CCAA** (sin Ceuta ni Melilla, sin datos faltantes) · 2015–2026.
- **`pct_pib_sanidad`:** rango 2,96 % – 8,94 % del PIB (mediana 5,94 %).
- **Origen del PIB:** 170 filas con PIB real · 34 con PIB proyectado (2025–2026, marcado en `origen_pib`).
- **Canarias:** serie continua 2015→último; rango 5,94 % – 7,90 % (pico COVID 2020).
- **Canarias vs mediana CCAA (2024, último con PIB real):** Canarias **7,07 %** vs mediana **6,34 %** → Canarias dedica más esfuerzo relativo (coherente con su menor PIB per cápita).
- **Lectura cruzada de interés:** Canarias combina mayor esfuerzo de gasto/PIB y mayor mortalidad evitable (118 % de la media) → hipótesis de eficiencia/necesidad a explorar en el análisis.

## 5. Artefactos

- `1_extraccion/*.rds` — un RDS por grupo temático + `raw_sanidad.rds` (crudo consolidado).
- `1_extraccion/qa/qa_resumen_indicadores.csv` — tabla completa de control por indicador.
- `1_extraccion/qa/qa_mort_evitable_idx.csv` — índice construido (ratio + reescalado 0–100) por CCAA × año × género.
- `1_extraccion/qa/qa_gasto_pib.csv` — gasto sanitario sobre PIB por CCAA × año (importado de Presupuestos).
- `1_extraccion/gasto_pib.rds` — variable de gasto/PIB normalizada.
