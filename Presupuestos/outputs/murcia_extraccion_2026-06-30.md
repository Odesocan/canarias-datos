# Extracción Murcia — Presupuestos autonómicos

Actualizado: 2026-06-30  
Ámbito: Región de Murcia (`mur`), capa autonómica.

## Resultado

La serie Murcia queda extraída para **2016-2025** desde el visor HTML de CARM y
**2026** queda incorporado como prórroga de 2025. Todos los ejercicios procesados
entran como `VERDE_PRAGM`: tienen más de 30 filas, cubren los 13 conceptos
canónicos y mantienen un porcentaje de concepto no nulo de ~73-79 %.

| año | estado | filas | % concepto | conceptos | raw usado |
|---:|---|---:|---:|---:|---|
| 2016 | VERDE_PRAGM | 145 | 74.5 | 13/13 | `fuentes/raw/mur/2016/` |
| 2017 | VERDE_PRAGM | 149 | 74.5 | 13/13 | `fuentes/raw/mur/2017/` |
| 2018 | VERDE_PRAGM | 147 | 74.1 | 13/13 | `fuentes/raw/mur/2018/` |
| 2019 | VERDE_PRAGM | 149 | 73.8 | 13/13 | `fuentes/raw/mur/2019/` |
| 2020 | VERDE_PRAGM | 154 | 74.0 | 13/13 | `fuentes/raw/mur/2020/` |
| 2021 | VERDE_PRAGM | 154 | 73.4 | 13/13 | `fuentes/raw/mur/2021/` |
| 2022 | VERDE_PRAGM | 154 | 73.4 | 13/13 | `fuentes/raw/mur/2022/` |
| 2023 | VERDE_PRAGM | 155 | 73.5 | 13/13 | `fuentes/raw/mur/2023/` |
| 2024 | VERDE_PRAGM | 160 | 74.4 | 13/13 | `fuentes/raw/mur/2024/` |
| 2025 | VERDE_PRAGM | 149 | 79.2 | 13/13 | `fuentes/raw/mur/2025/` |
| 2026 | VERDE_PRAGM | 149 | 79.2 | 13/13 | prórroga: `fuentes/raw/mur/2025/` |

`2015` queda fuera de esta vía: el visor `/web/xml/31.xml` no existe para ese
ejercicio y solo se localizó la Ley completa en PDF. El PDF se dejó en
`fuentes/raw/mur/2015/ley_completa.pdf`, pero requiere extractor específico si
se quiere recuperar el año.

## Forma de extracción

El portal móvil (`/movil/index.html`) es solo navegación. Los datos reales están
en la ruta paralela `/web/`:

| fichero | contenido |
|---|---|
| `web/xml/31.xml` | índice de gasto de Administración General; enlaces `datos/p228-*` |
| `web/xml/32.xml` | índice de organismos autónomos; enlaces `datos/p230-*` y `datos/p231-*` |
| `web/datos/p228-*.htm` | gasto por servicio/programa/subconcepto de secciones |
| `web/datos/p230-*.htm`, `p231-*.htm` | gasto de organismos autónomos |

En cada HTML, el nivel útil es `tr.fila_5`: programa presupuestario (`412A`,
`421A`, etc.) e importe agregado en euros. El extractor `1_extraccion/ccaa/mur`
ya sumaba estas filas por programa y después asigna concepto con
`mur/correspondencias.yml`.

## Cambios realizados

- `tools/mur_download.py`
  - Añadidos slugs especiales:
    - `presupuesto2021`
    - `leypresup2022`
    - `leypresup2023`
    - `leypresup2024`
  - Añadido `--url` para normalizar enlaces de `/movil/index.html` a `/web`.
  - Cabeceras tipo Safari para reducir bloqueos.
  - Detección de bloqueos Radware/Shieldsquare/Incapsula.
  - Umbral de guardado ajustado para aceptar páginas válidas pequeñas.

- `fuentes.yml`
  - Añadidos ejercicios Murcia 2016-2026.
  - Añadido 2015 como PDF no homogéneo, no usado por `mur-html`.

- `tools/smoke_regresion_py.py`
  - Añadidos combos `mur` 2016-2026.
  - 2026 apunta al raw 2025 como prórroga.

- `outputs/smoke_regresion_py.csv`
  - Sustituidas las filas Murcia por los 11 ejercicios verificados.

## Reproducción

Descarga reanudable:

```bash
for y in 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025; do
  python3 tools/mur_download.py --anio "$y" --out "fuentes/raw/mur/$y" \
    --max 100 --delay-base 1.8 --resume
done
```

Extracción aislada:

```bash
cd 1_extraccion
python3 -m ccaa --ccaa mur --anio 2024 \
  --input ../fuentes/raw/mur/2024 \
  --output /tmp/mur_2024.csv
```

Validación ejecutada:

```bash
python3 -m py_compile tools/mur_download.py tools/smoke_regresion_py.py \
  1_extraccion/ccaa/mur/extract.py
```

## Notas operativas

- No hacer ráfagas: usar `--resume` y `--delay-base >= 1.8` si se reintenta.
- Algunos HTML válidos son pequeños, por ejemplo una sección de transparencia de
  ~4 KB. No debe filtrarse solo por tamaño.
- Algunas páginas válidas incluyen un script `/_Incapsula_Resource` al final; el
  bloqueo real aparece al principio de la respuesta con `NOINDEX/NOFOLLOW` y sin
  tabla `fila_5`.
- El total 2025 cambia respecto al raw parcial anterior porque se refrescaron las
  páginas que estaban bloqueadas por Incapsula.
