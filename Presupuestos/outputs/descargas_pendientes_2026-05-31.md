# Manifiesto de descargas pendientes — para la run matinal (R/httr)

_Generado Noche 13 (2026-05-31). El sandbox nocturno NO puede descargar (curl/wget/requests
bloqueados, sin R). Estas son las descargas que, ejecutadas por la mañana con el maestro R,
amplían la cobertura autonómica usando extractores YA VERDES (sin tocar código)._

Cobertura autonómica actual: **91 ejercicios VERDE** + 1 ROJO (ara 2016). Objetivo 17×12 = 204.

## A · Alta confianza (extractor ya verde, solo falta el fichero)

### cat — faltan 2018, 2021, 2025  (patrón gencat estable, mismo VOL_P_EID que los 9 verdes)
```
https://aplicacions.economia.gencat.cat/wpres/AppPHP/2018/pdf/VOL_P_EID.pdf  -> fuentes/raw/cat/2018/VOL_P_EID.pdf
https://aplicacions.economia.gencat.cat/wpres/AppPHP/2021/pdf/VOL_P_EID.pdf  -> fuentes/raw/cat/2021/VOL_P_EID.pdf
https://aplicacions.economia.gencat.cat/wpres/AppPHP/2025/pdf/VOL_P_EID.pdf  -> fuentes/raw/cat/2025/VOL_P_EID.pdf
```
Tras descargar: `Rscript 00_maestro.R --steps=extraccion,transformacion --ccaa=cat`
Nota: 2021 puede ser prórroga de 2020 en Cataluña → verificar que el PDF no sea idéntico (md5) al de 2020 antes de declararlo año nuevo.

## B · Confianza media (URL conocida, requiere resolver ID/ruta por año)

### cym — faltan 2015–2025  (jcyl publica un XLS «gastos consolidado» por año)
El extractor `cym/extract.py` descarga el ZIP CKAN, pero la URL fija
`.../presupuestos/1284548037482-8.csv` sólo sirve el año corriente. Buscar en
`https://datosabiertos.jcyl.es/.../hacienda/presupuestos/` el dataset por ejercicio y
volcar cada `Presupuesto de gastos consolidado_<año>.xls` a `fuentes/raw/cym/<año>/`.
Recordatorio: en el sandbox falta `xlrd` — ya está pip-instalable; en R/local debe existir.

### pvc — faltan 2015–2021, 2023  (euskadi Datuak_datos.csv por año)
```
https://www.euskadi.eus/contenidos/informacion/presupuestos_cae_fich/es_def/adjuntos/<AÑO>A/Datuak_datos.csv
```
2021A y 2023A devolvieron 404 en noches previas; probar variantes `<AÑO>` sin sufijo `A`
y el portal nuevo open-data de Eusko Jaurlaritza.

### mad — faltan 2015–2025  (comunidad.madrid, IDs VersionId volátiles)
Resolver desde la landing por año: `https://www.comunidad.madrid/presupuestos/presupuestos-generales-comunidad-madrid-<AÑO>`
y descargar el «Libro» de clasificación funcional/programa (no el folleto resumen).

## C · Bloqueadas / requieren otra vía (documentadas, no perder tiempo en visor)

- **mur** 2015–2024: visor CARM móvil con anti-bot (~200 .htm a 1,5–3 s/req). Vía probable:
  CKAN `datosabiertos.regiondemurcia.es` (buscar dataset presupuesto por programa).
- **gal** 2015–2024: endpoint xunta `0665/gastos-orzamento-<año>` sirve SIEMPRE el mismo
  fichero (md5 idéntico 2021–2025). Vía probable: datos abiertos Xunta CSV por ejercicio.
- **lar** 2015–2024: larioja.org usa `idMmedia=<n>` opacos; hay que navegar la landing por año.
- **clm** 2015–2023: landing transparencia 404 para años antiguos; revisar hemeroteca DOCM.
- **cnt** 2015–2024: cantabria.es documents IDs opacos por año.
- **can** 2015–2017: galería `Presupuestos/<año>/ley/TOMO-3-Resumenes.pdf` 404 (sólo desde 2018).
- **ast** 2022: el `tomo_I.pdf` en disco es SÓLO el articulado (verificado: 0 tablas de
  distribución funcional/económica). Falta el anexo «estados numéricos» 2022 como doc aparte.
- **bal** 2017 y 2026: los `secciones/titol*_d.pdf` y `memoria_programas.html` en disco son
  stubs de 34 B (404). Falta la ruta real en pressuposts.caib.es para esos dos años.
