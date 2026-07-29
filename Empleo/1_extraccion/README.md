# Fase 1 · Extracción — Sección Empleo

**Canarias en Datos · ODESOCAN** · Implementación en **Python** de la etapa
`1_extraccion` del cuaderno metodológico (§8).

> Ámbito de esta fase (y sólo esta): **descargar** las fuentes y volcarlas
> crudas + en formato largo. **No** calcula indicadores ni normaliza
> exhaustivamente: eso es `2_transformacion`.

## Fuentes y cómo se ejecutan

| Vía | Script | Prerrequisito | Estado |
|-----|--------|---------------|--------|
| INE (EPA · ETCL · EAES) | `extraer_ine.py` | ninguno (API pública) | ✅ ejecutado |
| Supabase (alquiler CCAA) | `extraer_supabase.py` | `SUPABASE_SERVICE_KEY` | ✅ artefacto materializado |
| Seguridad Social (afiliación) | `extraer_seg_social.py` | ficheros en `fuentes_seg_social/` | 🟡 preparado, faltan ficheros |

```bash
cd 1_extraccion
pip install -r requirements.txt

python extraer.py                 # orquesta las 3 vías (omite las que no tengan prerrequisitos)
python extraer_ine.py             # sólo INE
export SUPABASE_SERVICE_KEY="..." # clave service_role (NO se sube al repo)
python extraer_supabase.py        # sólo alquiler
python extraer_seg_social.py      # sólo afiliación (tras dejar los Excel en fuentes_seg_social/)
```

## Artefactos generados

Por cada tabla: `raw/<slug>.json` (crudo) + `salida/<slug>.parquet` + `.csv`.
Globales: `salida/cobertura.csv`, `salida/manifiesto.json`.

## Estado de los 11 indicadores (verificado contra fuentes reales, 2026-07-21)

| # | Indicador | Fuente · tabla | Estado |
|---|-----------|----------------|--------|
| 1 | Tasa de paro | EPA · 14506 | ✅ OK |
| 2 | Tasa de actividad | EPA · 14509 | ✅ OK |
| 3 | Tasa de empleo | EPA · 14508 | ✅ OK |
| 6 | Paro juvenil (<25) | EPA · 14506 | ✅ OK |
| 7 | Paro larga duración | EPA · 65340 | 🟡 derivado (sumar % ≥1 año) |
| 8 | Temporalidad | EPA · 65328 | 🟡 derivado (% temporales) |
| 9 | Parcialidad | EPA · 65319 | 🟡 derivado (% t. parcial) |
| 4 | Horas sector servicios | ETCL · 6063 | ⚠️ OK **sin género** (la ETCL no lo publica) |
| 10 | Brecha salarial | EAES · 28191 | 🟡 derivado, anual ((H−M)/H) |
| 11 | % salario en alquiler | Supabase `alquiler_historico_ccaa` + EAES | ✅ alquiler extraído; deriva en transformación |
| 5 | Afiliación Seg. Social | Ficheros TGSS (provincial) | 🟡 lector listo; faltan ficheros |

- 🟡 **derivado**: el dato-insumo está extraído; el indicador final se calcula en `2_transformacion`.
- ⚠️ **Indicador 4** (decidido): se mantiene con desglose «sector · CCAA» **sin género** (la ETCL no lo ofrece).

## Ficheros del módulo

- `ine_cliente.py` — cliente de la API JSON del INE (cache, reintentos, back-off).
- `catalogo.py` — catálogo verificado indicador→tabla + fuentes no-INE decididas.
- `territorio.py` — diccionario canónico de CCAA (códigos INE) + parseo (territorio, género, periodo, numérico ES).
- `extraer_ine.py` — extractor INE (EPA/ETCL/EAES).
- `extraer_supabase.py` — extractor de alquiler desde Supabase (bd_odesocan).
- `extraer_seg_social.py` — lector de ficheros de afiliación de la Seguridad Social.
- `extraer.py` — orquestador de las tres vías.

## Notas y avisos de mantenimiento

- **La Rioja en Supabase** llega con `codigo_ccaa='26'` (código de provincia), no `'17'`
  (código INE de CCAA). El join alquiler↔salario debe hacerse por **nombre canónico**.
- **Afiliación**: la Seguridad Social publica nivel **provincial**; el desglose por
  **isla** no lo da (requeriría ISTAC). Ver `fuentes_seg_social/LEEME.txt`.
- **Zonas sensibles** (§11 del cuaderno): cambios en las tablas/códigos del INE, en el
  layout de los Excel de la SS, o en el esquema de Supabase romperían la extracción.

## Esquema de la salida tidy (INE)

`indicador_id, indicador, operacion, id_tabla, serie_cod, serie_nombre,
territorio_cod, territorio, género, anyo, periodo, periodicidad, fecha, valor,
unidad, escala, tipo_dato, secreto, origen, fuente`

La bandera `origen` se fija a `real`; `proyeccion` se añadirá en `3_modelado` (§7.6).
El desglose fino (edad, tipo de contrato, tiempo de búsqueda, sector) se conserva en
`serie_nombre` para que `2_transformacion` lo parsee.
