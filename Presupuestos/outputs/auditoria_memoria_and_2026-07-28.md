# Auditoría con MEMORIA · Andalucía — origen ↔ modelo ↔ memoria (2026-07-28)

> **Pregunta:** ¿cuánto ha fallado el modelo de asignación de conceptos (código+keyword)
> al no incorporar la memoria de programas?
> **Método:** extracción de las **2.431 fichas de programa** de las 8 memorias en repo
> (2017-19, 2022-26; 220-365 fichas/año), aislando el articulado de objetivos (OE/OO/AC).
> Comparación a tres bandas contra el **ORIGEN** (`Tablas_Correspondencias_CCAA.docx`,
> tabla de Andalucía) y el **MODELO ACTUAL** (staging vía `correspondencias.yml`).
> **Universo:** 332,2 B€ nominales (8 ejercicios).

---

## Titular

**Concordancia memoria ↔ modelo, ponderada por €: 92,8 %.**
**Impacto de los errores CONFIRMADOS: 4.713 M€ = 1,42 % del gasto extraído.**

El modelo no está roto, pero falla de forma **sistemática y silenciosa** en dos frentes que
solo la memoria puede revelar: códigos que el origen documentó con un significado que ya no
tienen, y programas sociales que ningún prefijo/keyword alcanza.

---

## Hallazgo 1 · El origen metodológico tiene 11 de 42 códigos MUERTOS (26 %)

Códigos citados en `Tablas_Correspondencias_CCAA.docx` que **no existen en ningún año** de la
memoria real de Andalucía:

| Concepto | Vivos | Muertos |
|---|:---:|---|
| **salud_mental** | **0/1** | `41M` — *su único código* |
| **igualdad** | **0/1** | `32G` — *su único código* |
| soberania | 5/11 | `71C` `71D` `71G` `71I` `71J` `71K` |
| empleo | 1/3 | `32B` `32C` |
| sanidad | 3/4 | `41B` |

**Consecuencia grave:** según el origen documentado, Andalucía **no tendría ni salud mental ni
igualdad**. Lo que hoy aparece en esos dos conceptos procede **al 100 % de coincidencias de
keyword**, sin respaldo metodológico:

- `igualdad` ← `31A` D.S.G. de Igualdad y Políticas Sociales (339 M€) + `12P` + `31T`
- `salud_mental` ← `31B` Plan sobre Adicciones (281 M€)

Ambas asignaciones son **razonables**, pero son *hallazgos del keyword*, no decisiones
metodológicas. Es exactamente la fragilidad diagnosticada: si mañana cambia la denominación,
el concepto se vacía en silencio.

---

## Hallazgo 2 · Deriva semántica — el código dice una cosa, el programa hace otra

El origen documentó un significado que **el documento real contradice**:

| Código | El ORIGEN dice | La MEMORIA dice (denominación real) | Modelo actual | € 8 años |
|---|---|---|---|---:|
| `31P` | «LGTBI (creado 2017)» → diversidad | **«SERVICIO DE APOYO A LAS FAMILIAS»** (2017-2026) | diversidad | **2.031 M€** |
| `54C` | «Sociedad de la Información» → idi | **«INNOVACIÓN Y EVALUACIÓN EDUCATIVA»** | idi | **611 M€** |
| `31D` | «Comunidad Gitana» → diversidad | **«ATENCIÓN A LAS FAMILIAS»** (2023-26) | NULL | 17 M€ |
| `32E` | prefijo 32 → empleo | «INCLUSIÓN SOCIAL» / «PROYECTOS DE INTERÉS SOCIAL» | diversidad ✔ | 1.013 M€ |

`31P` es el caso más serio: **2.031 M€ imputados a `diversidad` durante 8 años sobre la premisa
de que era el programa LGTBI**, cuando la memoria demuestra que nunca lo fue en ese periodo —
es apoyo a familias. El concepto *diversidad* de Andalucía está inflado por esta vía.

`32E` es el contrario: el modelo **corrigió bien** al origen (el fix del 2026-07-02 lo movió a
diversidad) y la memoria lo confirma. No todo cambio del modelo fue un error.

---

## Hallazgo 3 · Fuga real de gasto: `32L`

`32L` **«EMPLEABILIDAD, INTERMEDIACIÓN Y FOMENTO DEL EMPLEO»** — presente 2017-2019 con
**2.054 M€** y clasificado como **NULL**. El origen lo cubriría (prefijo 32 → empleo) y la
memoria lo confirma sin ambigüedad (`EMPLEABILIDAD`, `DESEMPLE`, `EMPLEO`×8). Es gasto social
real que hoy **no está en ningún concepto**. Coincide con la alerta ya anotada en el catálogo
de correcciones del usuario («32L cambia de concepto: empleo → NULL»).

---

## Caso frontera (no es error, es decisión metodológica pendiente)

`32D` **«FORMACIÓN PROFESIONAL PARA EL EMPLEO»** — 2.055 M€. El origen y el modelo dicen
`empleo`; la memoria, por contenido, apunta a `educacion`. Ambas defendibles: es formación
profesional *finalista de empleo*. **Requiere arbitraje del cuaderno**, no un fix de código.

---

## Advertencia metodológica sobre esta auditoría

El clasificador automático sobre la memoria **tiene falsos positivos** y no debe usarse como
verdad automática. Dos fuentes de contaminación detectadas y corregidas en la v2:

1. **Nombre de la consejería** en la cabecera de ficha (hacía que `51B` Carreteras puntuara
   «vivienda», al pertenecer a la Consejería de Fomento… *y Vivienda*).
2. **Boilerplate «TIPO AFECTACIÓN GÉNERO»**, presente en *todas* las fichas, disparaba
   `igualdad` de forma generalizada.

Aun corregidas, sobrevive ruido: `14B` Administración de Justicia puntúa `igualdad` (4.440 M€)
porque sus objetivos citan violencia de género — el programa es justicia y `direccion` es
correcto. **Por eso los hallazgos se reportan en tiers de confianza y los CONFIRMADOS se han
verificado uno a uno contra la denominación real del documento.**

---

## Conclusión operativa

| Tier | Caso | Acción | € |
|---|---|---|---:|
| 🔴 Corregir | `32L` → empleo | añadir a `correspondencias.yml` | 2.054 M€ |
| 🔴 Revisar | `31P` fuera de diversidad | decidir destino (familias/dependencia) | 2.031 M€ |
| 🟠 Revisar | `54C` idi → educacion | reasignar | 611 M€ |
| 🟠 Documentar | `salud_mental` e `igualdad` sin código de origen | fijar códigos reales en el cuaderno | — |
| 🟡 Arbitrar | `32D` empleo vs educacion | decisión del cuaderno §1.6 | 2.055 M€ |
| ⬜ Limpiar | 11 entradas muertas del origen | linter de `correspondencias.yml` | — |

**El valor de la memoria queda demostrado:** ninguno de estos hallazgos era detectable con
código+denominación. Los cuatro CONFIRMADOS provienen de leer *qué hace realmente el programa*.

Datos completos: `outputs/and_memoria_vs_modelo_2026-07-28.csv` (2.431 fichas con objetivos,
score, evidencia léxica y los tres veredictos por celda).
