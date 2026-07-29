# Informe — Actualización de URLs de extracción (fuentes.yml)

**ODESOCAN · Canarias en Datos** — 2026-06-29
**Fuente:** `DIRECCIONES URL (1).xlsx` (94 filas, 18 CCAA + capa hacienda)
**Destino:** `fuentes.yml` (catálogo canónico de URLs que lee el resolver/descargador)
**Backup previo:** `fuentes.yml.bak.url_update_2026-06-29`

## Política aplicada
El Excel es la fuente autorizada, **salvo** donde `fuentes.yml` ya tenía un enlace
directo resuelto que funciona. Solo se actualizan ejercicios ya existentes (no se
añaden años nuevos). YAML validado tras la edición (20 claves CCAA, parseo correcto).

## Reconciliación global
- 86 ejercicios (CCAA-año) presentes en ambos: **76 ya idénticos**, 10 distintos.
- De los 10 distintos → **6 actualizados**, 4 preservados a propósito.
- Cobertura del Excel que ya estaba sincronizada: el grueso del catálogo no requería cambios.

## Cambios aplicados (6 URLs)

| CCAA | Año | Antes | Ahora | Motivo |
|------|-----|-------|-------|--------|
| ast | 2024 | `transparencia.asturias.es/web/.../presupuestos` (placeholder) | `miprincipado.asturias.es/bopa/2023/12/29/20231229Su1.pdf` | El nodo pedía "resolver URL canónica"; el Excel la aporta (BOPA) |
| ast | 2025 | `transparencia.asturias.es/web/.../presupuestos` (placeholder) | `miprincipado.asturias.es/bopa/2024/12/31/2024-11573.pdf` | Ídem |
| ast | 2026 | `transparencia.asturias.es/documents/.../presupuestos_2026_tomoI...pdf` | `miprincipado.asturias.es/bopa/2025/12/31/20251231Su1.pdf` | Excel canónico; homogeneiza con BOPA |
| cat | 2015 | `.../AppPHP/2015/pdf/VOL_P_EID.pdf` | `.../AppPHP/2015/pdf/VOL_P_RES.pdf` | Corrección de volumen (resúmenes) |
| cat | 2016 | `.../AppPHP/2016/pdf/VOL_P_EID.pdf` | `.../AppPHP/2016/pdf/VOL_P_RES.pdf` | Corrección de volumen (resúmenes) |
| cat | 2017 | `.../AppPHP/2017/pdf/VOL_P_EID.pdf` | `.../AppPHP/2017/pdf/VOL_L_EID.pdf` | Corrección de volumen (L-EID) |

> Nota ast→BOPA: la fila ast/2023 (VERDE) ya extrae desde una URL BOPA equivalente,
> así que el cambio homogeneiza la serie. Los raws de ast 2024/2025 ya estaban
> descargados y siguen VERDE; la nueva URL solo afecta a futuras re-descargas.

## Preservados / no modificados a propósito (4)

| CCAA | Año | Decisión | Motivo |
|------|-----|----------|--------|
| and | 2020 | Se mantiene el CSV directo resuelto en yml | El Excel solo da la *landing page* del dataset; el yml ya tiene el `download/gastos.csv` directo |
| and | 2021 | Ídem | Ídem |
| and | 2022 | Sin cambio | El Excel concatena 2 URLs en una celda; el yml ya las tiene separadas (`memoria_programas` + `estado_iii`) con esas mismas URLs |
| bal | 2017 | Se mantiene `PENDIENTE_BUSCAR` | La celda del Excel dice literalmente "No tenemos url, debes buscarla" (no es una URL) |

## No añadido (años solo en el Excel)
Por decisión del usuario, **no** se crearon nodos nuevos. Quedan disponibles en el
Excel para una futura ampliación de cobertura: **can 2015, 2016, 2017** y
**cat 2018, 2021, 2025**.

## Avisos de calidad de datos (no modificados; revisar en origen)
- **ara 2024 = 2025 = 2026** comparten la misma URL (`ingresos_gastos_24`) tanto en
  el Excel como en el yml. Probable copia-pega: 2025 y 2026 deberían tener su propio
  documento. Verificar en aragon.es.
- **gal 2026** sigue como `portal_index` (HTML índice, estado None) — pendiente del
  CSV de orzamentos abertos.
- **bal 2017** necesita localizar el `menu_tom3_d.html` real (las secciones en disco
  son stubs de 34 B).

## Próximo paso
En el run matinal (Mac, con R/psql), `Rscript tools/resolver_canonical_url.R` re-resolverá
las landing pages y `00_maestro.R --steps=extraccion` podrá descargar los raws con las
URLs corregidas (ast 2024-2026, cat 2015-2017). Las CCAA en VERDE no se ven afectadas.
