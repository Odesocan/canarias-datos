# Presupuestos · Canarias en Datos — Cobertura de extracción por CCAA × ejercicio

> Generado 2026-07-02 desde `outputs/smoke_regresion_py.csv` (catálogo vivo de regresión).
> Capa **autonómica** (dato oficial de cada CCAA). **196 ejercicios-año · 17/17 CCAA.**

**Leyenda:** ✅ VERDE (≥80% filas con concepto) · 🟡 VERDE_PRAGM (35–80%, NULLs no-sociales legítimos) · — sin extraer.

| CCAA | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | Años | %conc̄ | Concep. |
|:---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Andalucía** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 74% | 13 |
| **Aragón** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 65% | 11 |
| **Asturias** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 70% | 10 |
| **Baleares** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 68% | 13 |
| **C. Valenciana** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 11 | 84% | 13 |
| **Canarias** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 66% | 13 |
| **Cantabria** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 54% | 12 |
| **Cast. y León** | — | ✅ | ✅ | ✅ | — | — | ✅ | — | ✅ | ✅ | ✅ | ✅ | 8 | 86% | 13 |
| **Cast.-La Mancha** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 65% | 12 |
| **Cataluña** | 🟡 | 🟡 | 🟡 | — | 🟡 | 🟡 | — | 🟡 | 🟡 | 🟡 | — | 🟡 | 9 | 66% | 13 |
| **Extremadura** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | 🟡 | 12 | 82% | 11 |
| **Galicia** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | 12 | 76% | 11 |
| **La Rioja** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | 🟡 | 12 | 74% | 13 |
| **Madrid** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 48% | 12 |
| **Murcia** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 75% | 13 |
| **Navarra** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 77% | 13 |
| **País Vasco** | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 12 | 48% | 11 |

**Total: 196 ejercicios-año extraídos.**

## Huecos de cobertura (candidatos a completar)

- **C. Valenciana**: falta 2015
- **Cast. y León**: falta 2015, 2019, 2020, 2022
- **Cataluña**: falta 2018, 2021, 2025

## Notas de calidad (conceptual) abiertas

- **Andalucía**: ramas CSV/PDF no homogéneas — sanidad rama CSV ~2015/16/20/21 doble-cuenta la transferencia al SAS (22,9 B vs 14,1 B PDF); igualdad ×80 entre ramas. Pendiente unificar perímetro (una sola vista) + alias 12S↔41H en ambas ramas.
- **Cast.-La Mancha**: `322B Fomento y gestión del empleo` (~113 M/año) y `322A` (relaciones laborales) mapeados a *educacion* vía prefijo `322*`; deberían ir a *empleo* (candidato de alta confianza, no aplicado — fuera del alcance auditado).
- **Madrid / País Vasco / Cantabria**: %concepto por filas bajo (48–54%) pero por importe 65–68%: NULL = deuda/carreteras/corporaciones locales (origen legítimo, no error).