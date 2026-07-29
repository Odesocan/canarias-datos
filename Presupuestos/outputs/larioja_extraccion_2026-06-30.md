# Extracción de presupuestos de La Rioja

Fecha: 2026-06-30

## Resumen ejecutivo

Se ha sustituido la dependencia práctica de `camelot` por un extractor basado en `pdfplumber` para los PDFs de La Rioja. El extractor trabaja con dos patrones:

- `lar-resumen-programas-pdfplumber`: tablas de resumen con código de programa de 4 dígitos y total.
- `lar-pdfplumber-funcional-economico`: detalle de gasto funcional/económico con reconstrucción de código jerárquico `G.F.SF.P`.

Resultado incorporado al catálogo de regresión: La Rioja pasa de 1 ejercicio a 12 ejercicios válidos: 2015-2026.

## Ejercicios integrados

| Año | Estado | Motor | Filas | % concepto | Conceptos | Observación |
|---:|---|---|---:|---:|---:|---|
| 2015 | VERDE_PRAGM | `lar-resumen-programas-invertido+lar-transform` | 69 | 59.4 | 6 | Tomo completo; resumen por programas con texto invertido. |
| 2016 | VERDE_PRAGM | `lar-resumen-programas-pdfplumber+lar-transform` | 70 | 68.6 | 7 | Resumen por programas dentro del tomo completo. |
| 2017 | VERDE_PRAGM | `lar-resumen-programas-pdfplumber+lar-transform` | 74 | 74.3 | 12 | Resumen por programas dentro del tomo completo. |
| 2018 | VERDE_PRAGM | `lar-detalle-organico-programas+lar-transform` | 53 | 79.2 | 9 | Detalle Orgánico/Económico de los Programas; Administración General. |
| 2019 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 73 | 71.2 | 12 | Fragmento `T02D23` de detalle funcional/económico. |
| 2020 | VERDE_PRAGM | `lar-informe-resumen-funcional+lar-transform` | 76 | 68.4 | 11 | Informe Resumen General Funcional-Económico al final de la Ley. |
| 2021 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 81 | 72.8 | 12 | Sin columna total explícita; se suman capítulos. |
| 2022 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 64 | 70.3 | 12 | Detalle funcional/económico. |
| 2023 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 62 | 71.0 | 12 | Fuente fina en ZIP parlamentario: `12. Detalle Gastos Funcional-Económico.pdf`. |
| 2024 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 76 | 71.1 | 13 | Ley BOLR; suplemento de dos páginas renderizadas sin texto PDF. |
| 2025 | VERDE | `lar-pdfplumber-funcional-economico+lar-transform` | 58 | 84.5 | 13 | Detalle funcional/económico ya existente, ahora sin Camelot. |
| 2026 | VERDE_PRAGM | `lar-pdfplumber-funcional-economico+lar-transform` | 60 | 76.7 | 13 | Detalle funcional/económico. |

## Ejercicios no incorporados

No quedan ejercicios de La Rioja pendientes en la capa autonómica 2015-2026.

## Archivos modificados

- `1_extraccion/ccaa/lar/extract.py`: motor `pdfplumber`, ventanas de páginas por año, parser de resumen por programas, parser de detalle orgánico/económico por programa, parser de informe resumen funcional-económico, parser de detalle funcional/económico y suplemento 2024 para dos páginas visibles sin texto extraíble.
- `fuentes.yml`: bloque `lar` actualizado con los enlaces 2015-2026 y notas de diagnóstico.
- `tools/smoke_regresion_py.py`: `COMBOS["lar"]` ampliado a los 12 ejercicios válidos.
- `outputs/smoke_regresion_py.csv`: catálogo actualizado con las nuevas filas de La Rioja.
- `fuentes/raw/lar/<año>/`: PDFs descargados desde los enlaces aportados.

## Validación

Comandos ejecutados:

```bash
python3 -m py_compile tools/smoke_regresion_py.py 1_extraccion/ccaa/lar/extract.py
python3 - <<'PY'
import yaml
yaml.safe_load(open('fuentes.yml', encoding='utf-8'))
PY
```

Comprobación del catálogo:

- Filas totales en `outputs/smoke_regresion_py.csv`: 194.
- Duplicados `(ccaa, anio)`: 0.
- La Rioja: 12 ejercicios válidos.

## Próximo paso recomendado

Revisar con calma las correspondencias históricas de La Rioja 2015-2016: la extracción es válida y coherente con el motor existente, pero esos años usan una codificación funcional antigua (`4.1.*` sanidad en origen) que conviene auditar antes de la validación final contra Hacienda.
