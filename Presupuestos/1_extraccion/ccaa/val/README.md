# val — Comunitat Valenciana

## Estado: ✅ VERDE Python (2026-05-15, Noche 4)

`tomo_II.html` es un frameset shell. La cadena real es:

```
tomo_II.html
└── T2_menu_epp_ES.html  (índice de secciones)
    └── T2_sec##_ES.html  (índice de programas dentro de la sección)
        └── pdf/RPC-25-##-...-ES.pdf  ←  RESUMEN GENERAL POR PROGRAMAS Y CAPÍTULOS
```

Cada PDF RPC tiene la tabla canónica con todos los subprogramas
(NNN+L+NN, p.e. 411A00, 412B22, 313D00) y, en la última columna,
"Total General" en miles de euros. El extractor procesa todos los
`secciones/sec*_RPC.pdf` y construye una fila por subprograma
(importe ×1000 → euros).

Smoke 2025: 174 subprogramas, 13 conceptos canónicos cubiertos,
mapped 86.2 %. Los 24 NULL son programas no canónicos
(transporte/infraestructuras 513*-514*, medio ambiente 442*,
cultura 452-457*, energía/minas 731A, comercio 761A, internacional
762A, tributos 613B, parques móvil 612H…) que legítimamente quedan
fuera de la matriz de los 13 conceptos.

## Cómo regenerar `secciones/` para un año nuevo

```python
import requests, re, os
base = "https://hisenda.gva.es/auto/presupuestos/<AAAA>/"
out = "fuentes/raw/val/<AAAA>/secciones/"; os.makedirs(out, exist_ok=True)
menu = requests.get(base + "T2_menu_epp_ES.html", timeout=15).text
for sid in sorted(set(re.findall(r"T2_sec(\d+)_ES\.html", menu))):
    sh = requests.get(base + f"T2_sec{sid}_ES.html", timeout=15).text
    with open(out + f"T2_sec{sid}_ES.html","w",encoding="utf-8") as f: f.write(sh)
    m = re.search(r'href="\.?\/?(pdf/RPC-[^"]+\.pdf)"', sh)
    if not m: continue
    rp = requests.get(base + m.group(1), timeout=30)
    if rp.status_code == 200:
        with open(out + f"sec{sid}_RPC.pdf","wb") as f: f.write(rp.content)
```

20 secciones para 2025. Variará en años con reorganizaciones de
conselleries (2024: 18, 2023: 17, etc.).

## TODO

- Añadir años 2022-2024 cuando se confirme la URL canónica del Tomo II.
- Considerar cargar también el "RGS" (Resumen General por Secciones y
  Capítulos) como cross-check para conciliar con totales publicados.
