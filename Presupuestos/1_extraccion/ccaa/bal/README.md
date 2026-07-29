# bal — Illes Balears

## Estado: ✅ VERDE Python (2026-05-15, Noche 4)

`memoria_programas.html` es un frameset shell que carga vía JS un
`<SELECT>` con 27 opciones (`titol0..titol26_d.pdf`). Cada PDF detalla
los programas presupuestarios de una sección, agrupados por C.Cost
(centro de coste), con secuencia:

```
C.Cost <id> <denominación>
Programa <CODIGO> <denominación>
... (capítulos/artículos/conceptos/subconceptos) ...
Total Programa <importe>
```

El extractor descarga (cuando hace falta) los 27 PDFs a
`fuentes/raw/bal/<año>/secciones/titol*_d.pdf`, parsea las cabeceras
"Programa" y suma todos los "Total Programa" del mismo código (un
mismo programa puede aparecer bajo varios C.Cost).

Smoke test 2025: 141 programas únicos, 13 conceptos canónicos cubiertos,
mapped 74.5 %. Los 36 NULL son programas no canónicos (transporte,
agua, residuos, energía, telecomunicaciones, cultura/deporte) que
legítimamente quedan fuera de la matriz de los 13 conceptos del
cuaderno metodológico §1.6.

## Cómo regenerar `secciones/` para un año nuevo

`fuentes.yml` define la URL canónica del frameset. Los PDFs hijos
viven en `<base>/toms/tom3/titol{0..26}_d.pdf`. Para descargarlos:

```python
import requests, os
base = "https://pressuposts.caib.es/www/ant/pr<AAAA>bis/archivos/toms/tom3/"
out = "fuentes/raw/bal/<AAAA>/secciones/"
os.makedirs(out, exist_ok=True)
for i in range(27):
    r = requests.get(f"{base}titol{i}_d.pdf", timeout=20)
    if r.status_code == 200:
        with open(f"{out}titol{i:02d}_d.pdf","wb") as f:
            f.write(r.content)
```

Para ediciones más antiguas (2024, 2023…) revisa el calendario de URLs
en `pressuposts.caib.es/www/`. Los selectores y la cantidad de OPTIONs
pueden variar año a año (en 2025 son 27).

## TODO

- Añadir años 2022-2024 cuando se confirme la URL canónica del Tom 3.
- Considerar ampliar `correspondencias.yml` con programas de transporte
  / energía si el cuaderno metodológico los reclasifica como vivienda
  / IDI o servicios sociales en futuras revisiones.
