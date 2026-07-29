# Cobertura por concepto · capa autonómica — 2026-07-10

Nº de años (de 12: 2015-2026) con importe>0 por CCAA×concepto sobre el staging nominal completo (204 celdas). `12`=serie completa · `0`=nulo estructural en esa CCAA · valores intermedios = hueco puntual o entrada tardía en catálogo.

| Concepto | and | ara | ast | bal | can | cat | clm | cnt | cym | ext | gal | lar | mad | mur | nav | pvc | val | ΣCCAA |
|------|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| sanidad | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| educacion | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| soberania | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 11 | 12 | 12 | 12 | 12 | 17/17 |
| direccion | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| vivienda | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 9 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| empleo | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| idi | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 8 | 12 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| dependencia | 12 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 0 | 12 | 14/17 |
| discapacidad | 12 | 0 | 0 | 12 | 12 | 12 | 12 | 2 | 12 | 0 | 0 | 9 | 11 | 12 | 4 | 0 | 11 | 12/17 |
| salud_mental | 12 | 3 | 0 | 12 | 3 | 12 | 0 | 0 | 12 | 0 | 0 | 3 | 0 | 12 | 12 | 12 | 12 | 11/17 |
| diversidad | 12 | 11 | 6 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 11 | 9 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| turismo | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 8 | 11 | 12 | 12 | 12 | 12 | 12 | 17/17 |
| igualdad | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 7 | 9 | 12 | 12 | 12 | 12 | 12 | 17/17 |

### Diagnóstico

**Nulos estructurales por CCAA** (concepto sin ningún año con dato — normalmente gasto fuera del catálogo funcional de esa comunidad, no un error de extracción):

- **Aragón** (ara): dependencia, discapacidad — 9/13 conceptos con serie completa.
- **Asturias** (ast): dependencia, discapacidad, salud_mental — 9/13 conceptos con serie completa.
- **Cast.-La Mancha** (clm): salud_mental — 12/13 conceptos con serie completa.
- **Cantabria** (cnt): salud_mental — 11/13 conceptos con serie completa.
- **Extremadura** (ext): discapacidad, salud_mental — 11/13 conceptos con serie completa.
- **Galicia** (gal): discapacidad, salud_mental — 6/13 conceptos con serie completa.
- **Madrid** (mad): salud_mental — 10/13 conceptos con serie completa.
- **País Vasco** (pvc): dependencia, discapacidad — 11/13 conceptos con serie completa.

**Conceptos más cubiertos** (CCAA con ≥1 año): vivienda (17/17), turismo (17/17), soberania (17/17), sanidad (17/17).

**Conceptos con menos cobertura**: salud_mental (11/17), discapacidad (12/17), dependencia (14/17), direccion (17/17). Coinciden con partidas que muchas CCAA no desagregan como línea propia (salud mental suele ir dentro de sanidad; dependencia/discapacidad dentro de servicios sociales; diversidad/igualdad son programas pequeños o transversales).

> **Sobre la conciliación §2.6 por-concepto:** no se ejecuta contra Hacienda porque la serie homogénea SGCIEF es económica (capítulos 1-9), no funcional; no existe subfunción sanidad/educación comparable. La conciliación §2.6 a nivel de TOTAL ya está superada (187/187 OK, 2026-07-09). Una conciliación funcional real requeriría la liquidación funcional del Ministerio (BDGEL/clasificación funcional), no publicada en el SGCIEF descargado.