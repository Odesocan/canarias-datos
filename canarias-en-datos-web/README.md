# Canarias en Datos — Hub D3

Visor web multitemática del Observatorio ODESOCAN. Cada temática
(Vivienda, Sanidad, Salud mental, Presupuestos…) se renderiza con un
mismo motor D3 agnóstico alimentado por una configuración declarativa.

## Estructura

```
canarias-en-datos-web/
├── index.html            Shell con la botonera de temáticas
├── core/
│   ├── config.js         URL + anon key de Supabase (pública por diseño)
│   ├── engine.js         Motor D3 (Fase 2 — en construcción)
│   └── styles.css        Estilos comunes del hub
├── topics/
│   ├── _schema.md        Documentación del formato de config por temática
│   └── <tematica>.js     Una por temática (Fase 4 en adelante)
└── assets/
    └── geo/              Geometrías cacheadas (CCAA)
```

## Estado del plan

- [x] **Fase 1 — Scaffolding** (directorios, config, placeholder HTML)
- [ ] **Fase 2 — Motor agnóstico** (`core/engine.js`)
- [ ] **Fase 3 — Shell** (botonera dinámica + estado en URL)
- [ ] **Fase 4 — Config de Vivienda** (`topics/vivienda.js`)
- [ ] **Fase 5 — Stub de una temática solo-global** (validar que el motor oculta la escena "género")
- [ ] **Fase 6 — Deploy a GitHub Pages** (cuenta `Cristianodesocan`)

## Seguridad y credenciales

- `core/config.js` contiene la **anon key pública** de Supabase. Es segura
  para commitear: el control de acceso real lo impone Row Level Security
  (RLS) sobre las tablas.
- **Nunca** añadir la service_role key ni la contraseña de Postgres al
  repositorio. Esas viven en `.Renviron` en tu máquina local para el
  pipeline R y están ignoradas por `.gitignore`.

## Requisitos de datos

- Schema `canendatos`: tablas `ced_<tematica>_global` y opcionalmente
  `ced_<tematica>_gen` (brecha de género).
- Schema `geodesocan`: tabla `ccaa` con columna `geom` (geometrías CCAA).
- Las tablas deben tener **RLS con política `SELECT` para el rol `anon`**,
  si no la web no verá datos.

## Desarrollo local

Al usar módulos ES (`import/export`), abrir `index.html` con un servidor
estático — no funcionará con `file://`:

```bash
cd canarias-en-datos-web
python3 -m http.server 8000
# → http://localhost:8000
```
