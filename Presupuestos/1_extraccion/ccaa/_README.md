# Sub-pipelines por CCAA

Cada comunidad autónoma tiene su propia carpeta autocontenida en
`1_extraccion/ccaa/<id3>/` con todo lo necesario para extraer y normalizar
sus presupuestos. El maestro las orquesta a través del dispatcher común.

## Estructura mínima de una CCAA

```
ccaa/<id3>/
├── __init__.py              # vacío (marca el directorio como paquete)
├── README.md                # opcional: notas operativas (URLs, calendario, peculiaridades)
├── extract.py               # OBLIGATORIO: parser específico
├── transform.py             # OBLIGATORIO: aplica correspondencias.yml local
├── correspondencias.yml     # tabla CCAA × concepto
└── fixtures/                # opcional: ejemplos pequeños para pruebas
```

## Contrato de `extract.py`

```python
from pathlib import Path
from .._common import base
from .._common.base import make_row, ExtractionResult, NUM_RE

def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows = []
    # ... lógica específica de la CCAA ...
    rows.append(make_row(
        pagina=p_num,            # int o None
        codigo="412A",           # str — código presupuestario tal como aparece
        denominacion="Sanidad",  # str
        importe=12_345_678.90,   # float (en euros) o str es-ES
        anio=anio,
    ))
    return ExtractionResult(rows=rows, motor="<id3>-mi-formato")
```

## Contrato de `transform.py`

```python
from .._common.transform_helpers import asignar_concepto_local

def transform(rows, anio):
    """Devuelve la misma lista con 'concepto' añadido a cada fila."""
    return asignar_concepto_local(rows, mapping_path=__file__)
```

`asignar_concepto_local` lee el `correspondencias.yml` adyacente y aplica:
1. match exacto de código
2. match por prefijo (con `*` al final del código en el YAML)
3. match por keyword en la denominación

## Estructura de `correspondencias.yml`

```yaml
conceptos:
  sanidad:
    codigos: ["41A","41B","41C","41D","41J","41K"]      # match exacto
    keywords: ["sanidad","salud","servicio andaluz"]   # match en denominación
  educacion:
    codigos: ["42*"]                                    # prefijo: 42, 42A, 42B, …
    keywords: ["educación","enseñanza"]
  salud_mental:
    codigos: ["41M"]
    keywords: ["salud mental"]
  # … los 13 conceptos del cuaderno metodológico
```

Conceptos canónicos esperados (referencia, cuaderno §1.6):
`sanidad`, `educacion`, `soberania`, `direccion`, `vivienda`, `empleo`,
`idi`, `dependencia`, `discapacidad`, `salud_mental`, `diversidad`,
`turismo`, `igualdad`. (Y `total` para la capa Hacienda.)

## Cómo añadir una CCAA nueva (paso a paso)

1. **Inspecciona el formato real** del PDF/HTML/CSV:
   ```bash
   python3 -c "
   import pdfplumber
   with pdfplumber.open('fuentes/raw/<id3>/<año>/<archivo>.pdf') as pdf:
       for p in [10, 50, 100]:
           print(f'--- pág {p} ---')
           print(pdf.pages[p].extract_text()[:1500])
   "
   ```
2. **Crea `ccaa/<id3>/extract.py`** copiando una CCAA con formato similar
   (ver `ara/extract.py` para PROGRAMA+TOTAL, `and/extract.py` para tabla
   resumen, `pvc/extract.py` para CSV tidy).
3. **Crea `ccaa/<id3>/correspondencias.yml`** con los códigos reales que
   ves en el extracto (consulta `Tablas_Correspondencias_CCAA.docx`).
4. **`ccaa/<id3>/transform.py`** suele ser idéntico al patrón estándar
   (ver más arriba). Solo escríbelo distinto si necesitas reglas
   adicionales (deflactar, agregar entes…).
5. **Prueba aislado**:
   ```bash
   cd 1_extraccion
   python3 -m ccaa --ccaa <id3> --anio <año> \
                    --input ../fuentes/raw/<id3>/<año>/<archivo>.ext \
                    --output /tmp/test_<id3>.csv
   ```
6. **Integra en el pipeline completo**: el maestro detecta la nueva CCAA
   automáticamente vía `importlib`.

## CCAA actualmente soportadas

| id3 | CCAA                       | Estado | Notas |
|-----|----------------------------|--------|-------|
| and | Andalucía                  | ✅     | RESUMEN CAPÍTULOS-PROGRAMAS |
| ara | Aragón                     | ✅     | PROGRAMA + TOTAL PROGRAMA |
| ast | Principado de Asturias     | ✅     | DISTRIBUCIÓN GASTO POR PROGRAMA |
| bal | Islas Baleares             | ⏳ stub | HTML frames legacy — pendiente |
| can | Canarias                   | ⏳ stub | Necesita Tomo I real o CSV SEFLogiC |
| cat | Cataluña                   | ✅     | PROGRAMA <code> <denom> <total> |
| clm | Castilla-La Mancha         | ⏳ stub | URL canónica devolvió PDF vacío |
| cnt | Cantabria                  | 🟡     | ÍNDICE de programas (sin importes) |
| cym | Castilla y León            | ⏳ stub | CKAN endpoint inestable |
| ext | Extremadura                | ✅     | Suma de TOTAL CAPITULO por programa |
| gal | Galicia                    | ⏳ stub | Índice HTML, resolver tomos II/III |
| lar | La Rioja                   | ⏳ stub | PDF compacto, requiere camelot |
| mad | Comunidad de Madrid        | ⏳ stub | Falta Libro 04 (memoria programas) |
| mur | Región de Murcia           | ⏳ stub | Visor móvil HTML |
| nav | Comunidad Foral de Navarra | ⏳ stub | Visor JS — requiere Playwright |
| pvc | País Vasco                 | ✅     | CSV tidy bilingüe |
| val | Comunitat Valenciana       | ⏳ stub | HTML estático multi-tabla |
