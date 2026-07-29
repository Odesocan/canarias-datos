# Asimetría informativa del SAAD pre-2023-01-01 vs post-2023-01-01

> Generado por `_analisis/analisis_asimetria_pre2023.R` el 2026-04-29 10:49.
> Fuente: `1_extraccion/saad_by_year_month.rds` (todas las hojas publicadas por el IMSERSO).

## 1. Cobertura temporal

- **Pre-2023-01-01**: 129 meses observados (2012-01-01 → 2022-12-01).
- **Post-2023-01-01**: 38 meses observados (2023-01-01 → 2026-02-01).

## 2. Hojas presentes por tipo y periodo

La columna *firmas distintas* indica cuántas combinaciones diferentes de cabecera se han detectado para esa hoja en ese periodo. Una cifra alta sugiere inestabilidad estructural (renombres, columnas que aparecen y desaparecen).

| tipo_hoja | periodo | meses con hoja | cobertura % | ncol mediana | ncol min/max | firmas distintas |
| --- | --- | --- | --- | --- | --- | --- |
| benpresaad_v1 | pre | 129 | 100 | 24 | 24/25 | 3 |
| benpresaad_v2 | post | 38 | 100 | 16 | 16/16 | 1 |
| dictsaad | post | 38 | 100 | 26 | 24/26 | 2 |
| dictsaad | pre | 129 | 100 | 21 | 21/28 | 8 |
| perfsaad | post | 38 | 100 | 29 | 29/29 | 1 |
| perfsaad | pre | 129 | 100 | 29 | 23/31 | 9 |
| solsaad | post | 38 | 100 | 9 | 9/9 | 1 |
| solsaad | pre | 129 | 100 | 5 | 4/10 | 7 |

## 2.1 Hojas publicadas por el IMSERSO **no procesadas** por el ETL actual

Listado de hojas que aparecen en `saad_by_year_month.rds` pero no casan con ningún patrón del ETL (`solsaad`, `perfsaad`, `dictsaad`, `benpresaad_v1/v2`). Su existencia indica capacidad informativa publicada por el IMSERSO que hoy **no está llegando** a la tabla `ced_dependencia`.

**Post-2023-01-01** (38 meses observados):

| hoja | meses con la hoja | ncol mediana | nrow mediana | primera aparición |
|---|---|---|---|---|
| `10pend` | 38 | 14 | 33 | 2023-01 |
| `10pendPrest` | 38 | 17 | 32 | 2023-01 |
| `10pendResol` | 38 | 16 | 35 | 2023-01 |
| `11ListaEspera` | 38 | 16 | 26 | 2023-01 |
| `11ListaEsperaGI` | 38 | 16 | 26 | 2023-01 |
| `11ListaEsperaGII` | 38 | 16 | 26 | 2023-01 |
| `11ListaEsperaGIII` | 38 | 16 | 26 | 2023-01 |
| `15pbpcasaad` | 38 | 26 | 32 | 2023-01 |
| `20pobl` | 38 | 35 | 33 | 2023-01 |
| `22solcasaadpot` | 38 | 18 | 29 | 2023-01 |
| `23solcasaad` | 38 | 29 | 37 | 2023-01 |
| `24asolcasaad_pobl` | 38 | 50 | 29 | 2023-01 |
| `24solcasaad_pobl` | 38 | 14 | 33 | 2023-01 |
| `25solaltabaja` | 38 | 29 | 50.5 | 2023-01 |
| `32dictcasaadpot` | 38 | 18 | 31 | 2023-01 |
| `33dictcasaad` | 38 | 29 | 32 | 2023-01 |
| `33dictcasaadG0` | 38 | 29 | 32 | 2023-01 |
| `33dictcasaadGI` | 38 | 29 | 32 | 2023-01 |
| `33dictcasaadGII` | 38 | 29 | 32 | 2023-01 |
| `33dictcasaadGIII` | 38 | 29 | 32 | 2023-01 |
| `34adictcasaad` | 38 | 14 | 33 | 2023-01 |
| `34bdictcasaad` | 38 | 50 | 29 | 2023-01 |
| `35ResolGraAltaBaj` | 38 | 29 | 50.5 | 2023-01 |
| `36aperfresol_graf` | 38 | 28 | 27 | 2023-01 |
| `36bperfresol_graf` | 38 | 28 | 27 | 2023-01 |
| `36perfresol` | 38 | 29 | 36 | 2023-01 |
| `3solcasaad` | 38 | 26 | 32 | 2023-01 |
| `41abenpreGIII` | 38 | 24 | 35 | 2023-01 |
| `41abenpreGIII_graf` | 38 | 19 | 32 | 2023-01 |
| `41bbenpreGII` | 38 | 24 | 35 | 2023-01 |
| `41bbenpreGII_graf` | 38 | 19 | 32 | 2023-01 |
| `41benpresaad` | 38 | 24 | 32 | 2023-01 |
| `41benpresaad_graf` | 38 | 19 | 32 | 2023-01 |
| `41cbenpreGI` | 38 | 24 | 35 | 2023-01 |
| `41cbenpreGI_graf` | 38 | 19 | 32 | 2023-01 |
| `42pbpcasaadpot` | 38 | 17 | 31 | 2023-01 |
| `43pbpcasaad` | 38 | 29 | 32 | 2023-01 |
| `43pbpcasaadGI` | 38 | 29 | 32 | 2023-01 |
| `43pbpcasaadGII` | 38 | 29 | 32 | 2023-01 |
| `43pbpcasaadGIII` | 38 | 29 | 32 | 2023-01 |
| `44apbpcasaad` | 38 | 14 | 33 | 2023-01 |
| `44bpbpcasaad` | 38 | 50 | 29 | 2023-01 |
| `45ResolPIAAltaBaj` | 38 | 31 | 50.5 | 2023-01 |
| `46aperfpb_graf` | 38 | 28 | 20 | 2023-01 |
| `46perfpbsaad` | 38 | 29 | 34 | 2023-01 |
| `51aPAPDgrado` | 38 | 20 | 28 | 2023-01 |
| `51bTeleasgrado` | 38 | 20 | 28 | 2023-01 |
| `51cSADgrado` | 38 | 20 | 28 | 2023-01 |
| `51dCDgrado` | 38 | 20 | 28 | 2023-01 |
| `51eSARgrado` | 38 | 20 | 34 | 2023-01 |
| `51fPEVincgrado` | 38 | 20 | 28 | 2023-01 |
| `51gPECgrado` | 38 | 20 | 28 | 2023-01 |
| `51hPEAsistPgrado` | 38 | 20 | 28 | 2023-01 |
| `51pbgrado` | 38 | 17 | 28 | 2023-01 |
| `52SubtipoVinculada` | 38 | 16 | 28 | 2023-01 |
| `52SubtipoVinculadaGI` | 38 | 16 | 45 | 2023-01 |
| `52SubtipoVinculadaGII` | 38 | 16 | 45 | 2023-01 |
| `52SubtipoVinculadaGIII` | 38 | 16 | 45 | 2023-01 |
| `61aperfcuidadorCCAA` | 38 | 8 | 26 | 2023-01 |
| `62bperfcuidadorCCAA` | 38 | 13 | 24 | 2023-01 |
| `63cperfcuidadorCCAA` | 38 | 21 | 24 | 2023-01 |
| `6perfcuidador` | 38 | 9 | 17 | 2023-01 |
| `7IntenPE_SAD_CCAA` | 38 | 17 | 31 | 2023-01 |
| `7IntenSAD_CCAA` | 38 | 17 | 31 | 2023-01 |
| `7Intensidad` | 38 | 17 | 18 | 2023-01 |
| `7IntensidadCCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaAP_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEC_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEVcd_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEVpapd_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEVsad_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEVsar_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPEVteleasist_CCAA` | 38 | 17 | 31 | 2023-01 |
| `8CuantíaPrest` | 38 | 11 | 36 | 2023-01 |
| `8dictcasaad` | 38 | 26 | 32 | 2023-01 |
| `9TiempoEspera` | 38 | 17 | 33 | 2023-01 |
| `EVO` | 38 | 23 | 40 | 2023-01 |
| `EVO_derecho` | 38 | 23 | 24 | 2023-01 |
| `EVO_prest` | 38 | 23 | 24 | 2023-01 |
| `EVO_resol` | 38 | 23 | 24 | 2023-01 |
| `EVO_resolPIA` | 38 | 23 | 24 | 2023-01 |
| `EVO_sinPIA` | 38 | 23 | 24 | 2023-01 |
| `EVO_sol` | 38 | 23 | 24 | 2023-01 |
| `indsaad` | 38 | 16 | 28 | 2023-01 |
| `indsaad2` | 38 | 16 | 32 | 2023-01 |
| `porsaad` | 38 | 1 | 9 | 2023-01 |
| `91TiempoEspera_evo` | 2 | 7 | 31 | 2023-01 |

**Pre-2023-01-01** (129 meses observados, hojas con presencia ≥ 12 meses):

| hoja | meses con la hoja | ncol mediana |
|---|---|---|
| `indsaad` | 129 | 2 |
| `porsaad` | 129 | 1 |
| `2solcasaad` | 117 | 13 |
| `5dictcasaad` | 117 | 10 |
| `6granivsaad` | 117 | 22 |
| `8perfpbsaad` | 117 | 23 |
| `9pbpcasaad` | 117 | 11 |
| `10pbagpsaad` | 109 | 10 |
| `12solcasaad` | 12 | 14 |
| `13solaltabaja` | 12 | 29 |
| `22dictcasaad` | 12 | 14 |
| `23ResolGraAltaBaj` | 12 | 29 |
| `24perfresol` | 12 | 29 |
| `31benpresaad_graf` | 12 | 19 |
| `32pbpcasaad` | 12 | 14 |
| `33ResolPIAAltaBaj` | 12 | 31 |
| `34perfpbsaad` | 12 | 29 |
| `41pbgrado` | 12 | 17 |
| `42SubtipoVinculada` | 12 | 16 |
| `43pbagpsaad` | 12 | 11 |

## 3. Cambios en el universo de columnas (etiquetas detectadas)

Etiquetas únicas detectadas en cada hoja, separadas por *exclusivas pre*, *exclusivas post* y *comunes*. Las exclusivas post identifican lo que se **perdería** si se truncase la serie en pre-2023-01-01.

| tipo_hoja | comunes | exclusivas pre-2023 | exclusivas post-2023 |
|---|---|---|---|
| benpresaad_v1 | 0 | 86 | 0 |
| benpresaad_v2 | 0 | 0 | 46 |
| dictsaad | 17 | 135 | 39 |
| perfsaad | 22 | 82 | 0 |
| solsaad | 2 | 22 | 0 |

Detalle completo en `cambios_columnas_pre_post.csv`.

### 3.1 Top 30 etiquetas exclusivas de post-2023 por tipo de hoja

- **benpresaad_v2**: `10`, `11`, `12`, `12_personas_con_resolución_de_pia_y_prestación_efectiva_o_no_efectiva`, `13`, `14`, `15`, `16`, `situación_a_28_de_febrero_de_2023`, `situación_a_28_de_febrero_de_2025`, `situación_a_28_de_febrero_de_2026`, `situación_a_29_de_febrero_de_2024`, `situación_a_30_de_abril_de_2023`, `situación_a_30_de_abril_de_2024`, `situación_a_30_de_abril_de_2025`, `situación_a_30_de_junio_de_2023`, `situación_a_30_de_junio_de_2024`, `situación_a_30_de_junio_de_2025`, `situación_a_30_de_noviembre_de_2023`, `situación_a_30_de_noviembre_de_2024`, `situación_a_30_de_noviembre_de_2025`, `situación_a_30_de_septiembre_de_2023`, `situación_a_30_de_septiembre_de_2024`, `situación_a_30_de_septiembre_de_2025`, `situación_a_31_de_agosto_de_2023`, `situación_a_31_de_agosto_de_2024`, `situación_a_31_de_agosto_de_2025`, `situación_a_31_de_diciembre_de_2023`, `situación_a_31_de_diciembre_de_2024`, `situación_a_31_de_diciembre_de_2025`
- **dictsaad**: `3_1_resoluciones_de_grado`, `situación_a_28_de_febrero_de_2023`, `situación_a_28_de_febrero_de_2025`, `situación_a_28_de_febrero_de_2026`, `situación_a_29_de_febrero_de_2024`, `situación_a_30_de_abril_de_2023`, `situación_a_30_de_abril_de_2024`, `situación_a_30_de_abril_de_2025`, `situación_a_30_de_junio_de_2023`, `situación_a_30_de_junio_de_2024`, `situación_a_30_de_junio_de_2025`, `situación_a_30_de_noviembre_de_2023`, `situación_a_30_de_noviembre_de_2024`, `situación_a_30_de_noviembre_de_2025`, `situación_a_30_de_septiembre_de_2023`, `situación_a_30_de_septiembre_de_2024`, `situación_a_30_de_septiembre_de_2025`, `situación_a_31_de_agosto_de_2023`, `situación_a_31_de_agosto_de_2024`, `situación_a_31_de_agosto_de_2025`, `situación_a_31_de_diciembre_de_2023`, `situación_a_31_de_diciembre_de_2024`, `situación_a_31_de_diciembre_de_2025`, `situación_a_31_de_enero_de_2023`, `situación_a_31_de_enero_de_2024`, `situación_a_31_de_enero_de_2025`, `situación_a_31_de_enero_de_2026`, `situación_a_31_de_julio_de_2023`, `situación_a_31_de_julio_de_2024`, `situación_a_31_de_julio_de_2025`

### 3.2 Top 30 etiquetas exclusivas de pre-2023 por tipo de hoja

- **benpresaad_v1**: `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `1_7_personas_beneficiarias_y_prestaciones`, `20`, `21`, `22`, `23`, `24`, `25`, `3_1_personas_con_resolución_de_pia_y_prestaciones`, `atención_residencial`, `ayuda_a_domicilio`, `centros_día_noche`, `papd`, `pe_asistencia_personal`, `pe_cuidados_familiares`, `pe_vinculada_al_servicio`, `situación_a_28_de_febrero_de_2014`, `situación_a_28_de_febrero_de_2015`, `situación_a_28_de_febrero_de_2017`, `situación_a_28_de_febrero_de_2018`, `situación_a_29_de_febrero_de_2016`
- **dictsaad**: `1_4_dictámenes`, `1_4_resoluciones`, `27`, `28`, `2_1_resoluciones_de_grado`, `2_4_dictámenes`, `situación_a_1_de_abril_de_2012`, `situación_a_1_de_agosto_de_2012`, `situación_a_1_de_enero_de_2012`, `situación_a_1_de_febrero_de_2012`, `situación_a_1_de_julio_de_2012`, `situación_a_1_de_junio_de_2012`, `situación_a_1_de_marzo_de_2012`, `situación_a_1_de_mayo_de_2012`, `situación_a_1_de_octubre_de_2012`, `situación_a_1_de_septiembre_de_2012`, `situación_a_28_de_febrero_de_2013`, `situación_a_28_de_febrero_de_2014`, `situación_a_28_de_febrero_de_2015`, `situación_a_28_de_febrero_de_2017`, `situación_a_28_de_febrero_de_2018`, `situación_a_28_de_febrero_de_2019`, `situación_a_28_de_febrero_de_2021`, `situación_a_28_de_febrero_de_2022`, `situación_a_29_de_febrero_de_2016`, `situación_a_29_de_febrero_de_2020`, `situación_a_30_de_abril_de_2014`, `situación_a_30_de_abril_de_2015`, `situación_a_30_de_abril_de_2016`, `situación_a_30_de_abril_de_2017`
- **perfsaad**: `10`, `13`, `16`, `19`, `1_3_perfil_de_la_persona_solicitante_sexo_y_edad`, `22`, `25`, `30`, `31`, `42220`, `43044`, `43171`, `54648`, `5785`, `58520`, `5884`, `5913`, `59228`, `situación_a_28_de_febrero_de_2014`, `situación_a_28_de_febrero_de_2015`, `situación_a_28_de_febrero_de_2017`, `situación_a_28_de_febrero_de_2018`, `situación_a_29_de_febrero_de_2016`, `situación_a_30_de_abril_de_2014`, `situación_a_30_de_abril_de_2015`, `situación_a_30_de_abril_de_2016`, `situación_a_30_de_abril_de_2017`, `situación_a_30_de_abril_de_2018`, `situación_a_30_de_junio_de_2014`, `situación_a_30_de_junio_de_2015`
- **solsaad**: `1_1_solicitudes`, `2_1_solicitudes`, `34477`, `34829`, `35731`, `391739`, `397446`, `413279`, `45651`, `46239`, `49141`, `situación_a_1_de_abril_de_2012`, `situación_a_1_de_agosto_de_2012`, `situación_a_1_de_julio_de_2012`, `situación_a_1_de_junio_de_2012`, `situación_a_1_de_mayo_de_2012`, `situación_a_30_de_noviembre_de_2013`, `situación_a_31_de_agosto_de_2013`, `situación_a_31_de_diciembre_de_2013`, `situación_a_31_de_marzo_de_2013`, `situación_a_31_de_mayo_de_2014`, `situación_a_31_de_octubre_de_2013`

## 4. Cobertura por columna en las tablas ya transformadas

Para cada columna métrica de las tablas en `2_transformacion/`, % de filas no-NA en cada periodo. Una columna marcada *solo_post_o_casi_vacia_pre* indica que ese indicador en la práctica no existe antes de 2023-01-01.

**Distribución por flag**:

| tabla | flag | n columnas |
|---|---|---|
| benpresaad_all | comparable | 11 |
| dictsaad_all | comparable | 8 |
| dictsaad_all | solo_post_o_casi_vacia_pre | 1 |
| solsaad_all | comparable | 1 |

**Columnas exclusivas o casi exclusivas de post-2023**:

| tabla | columna | %no-NA pre | %no-NA post |
|---|---|---|---|
| dictsaad_all | resoluciones_grado | 0.0% | 100.0% |

Detalle completo en `cobertura_por_columna_periodo.csv`.

## 5. Lectura recomendada

- **Subconjunto longitudinal seguro**: usar únicamente las columnas comunes a ambos periodos y/o las que aparezcan con `flag = comparable` en la tabla de cobertura. Permite un histórico desde 2012 sin imputaciones ad-hoc.
- **Subconjunto enriquecido (post-2023-01-01)**: aprovecha el detalle adicional aportado a partir de 2023 (perf_saad enriquecido, benefect_pre con ratios y desgloses). Idóneo para análisis transversal, ranking territorial y dashboard.
- **Estrategia híbrida**: publicar una vista A (longitudinal, columnas mínimas, desde 2012) y una vista B (transversal, columnas completas, desde 2023), con un campo `version_schema` que el front-end pueda usar para condicionar los gráficos más detallados al periodo en que existen.

> **Nota crítica**: la sección 2.1 lista hojas publicadas por el IMSERSO post-2023 que el ETL actual **no está procesando** (listas de espera, pendientes de PIA, dictámenes y beneficiarios desglosados por grado, perfil de resoluciones, etc.). Antes de tomar la decisión longitudinal/transversal, conviene evaluar si ampliar los patrones de clasificación de hojas en `extraccion.R` (actualmente limitados a `solsaad`, `perfsaad`, `dictsaad`, `benefect_pre`) para incorporar estos bloques. Sin esa ampliación, una parte sustancial de la riqueza informativa post-2023 permanece invisible para el dashboard, independientemente del periodo elegido.

