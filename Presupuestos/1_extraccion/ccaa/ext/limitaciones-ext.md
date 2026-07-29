# Limitaciones conocidas — Extremadura (ext)

> Advertencias de la extracción de Extremadura. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `ext-doe-resumen-programa` primario (+ `ext-transform`); `ext-tomo-eig-suma-capitulos` como fallback (NO usado en la serie actual) · Años: 2015-2026 (serie completa, 12 ejercicios) · Estado global: 9 VERDE estricto (2015-2023) + 3 VERDE_PRAGM (2024-2026, 79.7 %). 11 conceptos por año.

## Perímetro / decisiones de consolidación
- Fuente canónica: tabla "Resumen por programa" del anexo de la **Ley de Presupuestos publicada en el DOE** (resueltas vía ELI `doe.juntaex.es/eli/...`). Cada programa aparece UNA vez con su total consolidado (1 fila por programa, código `<3 díg + letra>`). Se evitan los documentos de Cuenta General (liquidación, no presupuesto).
- El parser aísla la tabla-resumen exigiendo páginas con ≥5 filas-programa, lo que la separa del detalle EIG.
- **Se descartó el motor de detalle EIG** (`ext-tomo-eig-suma-capitulos`, con el que 2025/2026 estuvieron "validados" inicialmente): el Tomo II EIG no está consolidado (los programas se repiten por sección/servicio: admin general + organismos SES/SEPAD/SEXPE) y el dedup infravaloraba educación ~3x (222A daba 60M vs 397M reales). Las correspondencias previas también eran un template genérico equivocado (313A "Regulación de Producciones" iba a salud_mental; turismo=432A cuando Extremadura usa 342A; sanidad sin 211x). Ambos corregidos el 2026-06-30.
- Estructura funcional: 21x sanidad, 22x educación, 23x dependencia, 24x/325 empleo, 252/253 social, 26x vivienda, 27x cultura/deporte, 31x agricultura, 33x idi, 342 turismo, 35x infraestructuras/medio ambiente.

## Conceptos NO separables (NULL estructural por diseño)
- **salud_mental** y **discapacidad:** `codigos: []` en el correspondencias — Extremadura NO tiene programa presupuestario propio para estos conceptos, así que quedan NULL por diseño (no es un fallo de extracción). Ese gasto está embebido en programas de sanidad/dependencia sin desagregar.

## Advertencias de calidad del dato
- **FIX 2026-07-02 (correspondencias):** `252A` "Atención a la infancia y a las familias" (40→77 M/año) y `252B` "Inclusión social" (76→98 M) iban a NULL en toda la serie → añadidos a `diversidad`. El comentario de cabecera del yml decía "252/253 social" pero solo mapeaba 252C/253B/253C. Efecto 2024: ~175 M€ recolocados (superaban el total previo de diversidad); %concepto por filas 79.7→82.2 %, 2024-2026 pasan a VERDE. El techo de 11 conceptos NO cambia (salud_mental/discapacidad siguen NULL estructural, ver arriba).
- **2025 y 2026 = PRÓRROGA de la Ley 1/2024** (órdenes de 6-feb-2025 y 16-dic-2025): su resumen por programa es idéntico al de 2024. Datos reales pero NO independientes de 2024.
- La certificación VERDE no valida magnitudes (ver `LIMITACIONES.md` §1): conciliación contra Hacienda pendiente. Como referencia, la serie de totales es continua y monótona (5.37B en 2015 → 8.13B en 2024) con educación ya correcta vía tabla resumen.

## Años faltantes / problemáticos
- Serie completa 2015-2026, todos aptos. Salvedades: 2024-2026 quedan en VERDE_PRAGM (79.7 % concepto, justo por debajo del 80 % estricto) y 2025-2026 son prórroga de 2024 (ver arriba).
- Nota de fuentes: 2016 tuvo una corrección de URL (la del catálogo previo, 1090o.pdf/N109, NO era la ley; la real es la Ley 3/2016, DOE 67).

## Notas de uso
- No busques `imp_salud_mental` ni `imp_discapacidad` para Extremadura: son NULL estructural, no cero real.
- Trata 2024/2025/2026 como el mismo presupuesto (prórroga) para análisis interanual.
- Educación es fiable en esta serie (tabla resumen consolidada); NO uses la extracción por detalle EIG, que la infravalora ~3x.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py ext` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1299 16:1462 17:1452 18:1513 19:1595 20:1644 21:1770 22:1895 23:2080 24:2153 25:2153 26:2153` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** Serie plausible. 2024-2026 son prórroga (valores repetidos, no crecimiento real).
- **Seams documentados** (salto esperado, NO error): ninguno.

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
