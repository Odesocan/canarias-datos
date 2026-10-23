# Incidencias del pipeline Dependencia (SAAD)

Registro con el formato de la rutina de salud de los repos
(`SALUD-REPOS.md` en `odesocan/salud-repos-log`). Una fila por incidencia y,
debajo, el detalle.

| Fecha | Repo | Síntoma | Causa raíz | Solución | Estado |
|---|---|---|---|---|---|
| 2026-10-19 | canarias-datos | `canendatos.ced_dependencia_global` con datos reales solo hasta 2026-03; de 2026-04 a 2026-11 solo proyección, aunque el IMSERSO ya había publicado hasta 2026-09 | (1) El cron nunca escribe: `CED_CRON_ESCRIBE` no existe y la carga se queda en modo validación. (2) Aunque escribiera, lo haría en `saad`, no en `canendatos`, que es donde lee la web. (3) Desde el informe de 2026-05 el IMSERSO cambió la maquetación del Excel y el parser perdía columnas en silencio. | Carga por upsert a `canendatos` con ensayo previo en `ced_staging`; parsers por cabecera; Ceuta y Melilla agregadas; validación de descargas y fechas; aviso de antigüedad del último mes real. | Datos cargados en producción el 2026-10-23; código en rama, sin mergear |

## 2026-10-19 · Carga de dependencia detenida en marzo de 2026

### Síntoma

En `canendatos.ced_dependencia_global` las filas `origen = 'real'` terminaban
en 2026-03-01. De abril a noviembre solo había `origen = 'proyeccion'`. El
IMSERSO ya había publicado la estadística mensual hasta el 30/09/2026.

### Qué hacía realmente el pipeline

Los cron del 5 de septiembre y del 5 de octubre terminaron en verde. La
extracción llegó a 2026-07 y 2026-08, respectivamente, pero el log dice:

```
Evento: schedule · carga a producción: false
```

Ninguna ejecución en CI ha llegado a escribir en la base. La última carga buena
fue una ejecución manual en local con `SUPABASE_SCHEMA=canendatos` en
`Dependencia/.Renviron`, con datos hasta marzo.

### Causas

1. **El cron no escribe.** Desde el commit `29ce6fb`, la carga desde el cron
   depende de la variable de repositorio `CED_CRON_ESCRIBE`, que no está dada
   de alta. Es una decisión deliberada (que no se escriba en producción sin
   supervisión), pero no había nada que avisara de que los datos publicados se
   estaban quedando viejos.
2. **El esquema no era el correcto.** `carga.R` escribía todas las tablas en
   `SUPABASE_SCHEMA`, que por defecto es `saad`. Las tablas hub que lee la web
   viven en `canendatos`. En CI (sin la variable) habría creado
   `saad.ced_dependencia_global`, que nadie lee. Además, la carga hacía
   `DROP TABLE` y `RENAME`: reemplazaba la tabla entera.
3. **El Excel del IMSERSO cambió de maquetación en el informe de 2026-05.** Sin
   ningún error, el parser:
   - leía `12BenefEfect` por posición. Desaparece una columna intermedia y
     `personas_prest_efectiva` pasa a tomar el porcentaje (84,86) en lugar del
     número de personas (67.740). Eso dejaba el limbo de prestaciones en ~0 %;
   - no reconocía `P.E. Cuidados Familiares` (antes `P.E Cuidados Familiares`),
     y lo mismo ocurría con la vinculada y la de asistente personal, así que
     `pct_pecef` quedaba en NA;
   - perdía Ceuta y Melilla, que ahora vienen en filas separadas, con lo que
     quedaban 17 CCAA;
   - la hoja `61aperfcuidadorCCAA` (perfil del cuidador por sexo) llega vacía,
     y como `pct_mujeres_benef` no tenía dato, el modelado marcaba como
     `proyeccion` filas que eran reales.

### Hipótesis descartadas

- **Descargas bloqueadas.** Es cierto: sin `User-Agent` de navegador,
  imserso.es devuelve un 403 con una página HTML de 35.092 bytes. Pero el
  pipeline ya mandaba `User-Agent` y descargaba bien. Aun así, ahora usa
  cabeceras de navegador y valida cada fichero, para que esa página nunca
  llegue a la caché como si fuera un `.xlsx`.
- **Fecha de la cabecera del PDF.** El PDF de evolución de septiembre dice «a
  28 de febrero de 2026» en la cabecera, pero el pipeline no lee PDF: toma la
  fecha del nombre del fichero (`estsisaad_AAAAMMDD.xlsx`). Ahora, además,
  compara esa fecha con la de la cabecera de cada Excel y avisa si no
  coinciden.

### Cambios

| Archivo | Cambio |
|---|---|
| `utils/pipeline_utils.R` | `validate_download()` (firma binaria + tamaño mínimo; detecta el HTML de 35 KB), `fecha_mes_from_filename()`, `fecha_mes_from_text()`, `check_freshness()` (aviso y anotación `::warning::` si el último mes real tiene más de 2 meses), `--db-target`, `--aux-tables`, `publish_schema = canendatos` |
| `1_extraccion/extraccion.R` | Cabeceras de navegador; valida descargas y caché (los inválidos van a `_invalidos/`); un único fichero por mes; avisa si la fecha de la cabecera no coincide con la del nombre |
| `2_transformacion/transformacion.R` | `12BenefEfect` por cabecera y `pendientes_prest_efectiva = PIA − efectiva`; patrones `P.E.`; agregación de Ceuta y Melilla; PPD anual fijada (`ppd_anual_fijada.csv`); comprobación de identidades contables |
| `3_modelado/modelado.R` | Solo se proyecta después del último mes real del conjunto |
| `4_carga/carga.R` | Upsert de las tablas hub en `canendatos`: lo real sustituye a la proyección y la proyección nunca pisa lo real, sin DROP ni TRUNCATE; modo `staging` en el esquema privado `ced_staging` con resumen de cambios; comprobación de solo lectura de la antigüedad de la tabla publicada en cada ejecución |
| `.github/workflows/dependencia-pipeline.yml` | Con carga pedida pasa `--db-target=produccion` |
| `_analisis/validacion_incidencia_2026_10.R` | 33 controles contra las cifras del IMSERSO (marzo y septiembre de 2026) |

### Resultado (2026-10-19)

- 33 de 33 controles OK en `_analisis/validacion_incidencia_2026_10.R`
  (Canarias 2026-03 y 2026-09, España 2026-09, indicadores derivados y PPD).
- Identidades contables (pendientes de grado, de PIA y personas con PIA): se
  cumplen en todas las filas de 2023-01 a 2026-09.
- Ensayo en `ced_staging` del upsert sobre una copia de producción:
  - `ced_dependencia_global`: 108 proyecciones sustituidas por dato real
    (2026-04 a 2026-09 × 18 CCAA), 738 filas actualizadas, 198 insertadas,
    0 borradas.
  - `ced_dependencia_gen`: 216 sustituidas, 1.476 actualizadas, 396
    insertadas, 0 borradas.
  - Las 702 filas reales ya publicadas (2023-01 a 2026-03) son idénticas
    antes y después.
  - Último mes real: 2026-09. Proyección ETS de 2026-10 a 2027-04.

### Definiciones que se mantienen

- `pers_benef_prest` = personas con resolución de PIA.
- `pendientes_grado_total` = solicitudes − resoluciones de grado.
- `pendientes_pia_total` = personas con derecho − personas con PIA.
- `pendientes_prest_efectiva` = personas con PIA − personas con prestación
  efectiva.
- `*_pct_ppd` y `cobertura_pct_ppd` se calculan sobre la PPD anual, constante
  dentro del año. Para 2026, Canarias 267.797 y suma de CCAA 6.689.939.
- `pct_pecef` = PE de cuidados familiares / total de prestaciones.
- `fecha` = primer día del mes del informe.

### Paso a producción (2026-10-23)

Confirmado por Cristian, con la PPD 2026 fijada en 267.797 y la proyección ETS
sin cambios. Comando:

```bash
Rscript Dependencia/00_maestro.R --steps=carga --with-db=true --db-target=produccion --aux-tables=false
```

- `canendatos.ced_dependencia_global`: 810 filas reales (2023-01 a 2026-09)
  y 126 de proyección (2026-10 a 2027-04), sin claves duplicadas. Mismas
  cifras de upsert que en el ensayo.
- `canendatos.ced_dependencia_gen`: mismas operaciones que en el ensayo.
- Las dos tablas coinciden fila a fila con `ced_staging`. Después se borró
  el esquema `ced_staging`.
- Las tablas intermedias de `saad` no se tocaron.

### Pendiente

- Decidir si el cron escribe en producción: hay que dar de alta
  `CED_CRON_ESCRIBE=true` en *Settings → Variables*, o lanzar a mano con
  `escribir_produccion`. Mientras tanto, cada ejecución avisa si la tabla
  publicada se queda atrás.
- PPD 2026: el valor fijado (267.797 en Canarias) es la media de los informes
  de enero a marzo, y el de enero todavía traía la PPD de 2025 (262.023). La
  PPD que publica el IMSERSO para 2026 desde febrero es 270.684. Hay que decidir
  si se mantiene o se actualiza (cambiaría todas las tasas de 2026).
- Perfil del cuidador por sexo y CCAA: el IMSERSO ha dejado de publicarlo en
  `estsisaad` desde 2026-05. `pct_mujeres_benef` queda en NA de mayo a
  septiembre y `ced_dependencia_gen` arrastra el último reparto observado
  (abril).
- `general.censo_ppd` ya no tiene la estructura que espera
  `load_ppd_from_supabase()`: ahora trae `genero` y `edad` en lugar de `sexo` y
  `variable/valor`. Por eso se usa siempre la PPD del Excel.
- La proyección ETS del tiempo de espera extrapola la caída reciente (374 días
  en marzo, 214 en septiembre) y en Canarias llega a 2 días en 2027-03 y a 0
  en 2027-04, donde la corta la cota inferior. Es el mismo modelo de siempre;
  valorar una tendencia amortiguada para esta variable.
- Las tablas intermedias de `canendatos` (`benpresaad_all`, `dictsaad_all`…)
  tienen RLS desactivado y quedan expuestas a `anon`. Proceden de la carga
  manual antigua.
