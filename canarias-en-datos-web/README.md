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
- [x] **Fase 2 — Motor agnóstico** (`core/engine.js`): mapa coroplético, evolución,
      género y metodología, con descarga de CSV y periodos de cadencia mixta.
- [x] **Fase 3 — Shell**: botonera generada desde el `MANIFEST` de `index.html`,
      con `?tematica=<slug>` en la URL (`pushState` + `popstate`).
- [x] **Fase 4 — Config de Vivienda** (`topics/vivienda.js`)
- [~] **Fase 5 — Temática solo-global**: `topics/presupuestos.js` declara
      `genderTable: null`, pero hoy no se puede validar contra él porque el área
      está en cuarentena y su render falla (ver más abajo).
- [x] **Fase 6 — Deploy a GitHub Pages**: Pages está habilitado (Source: GitHub
      Actions) y `.github/workflows/web-deploy.yml` publica en cada push a `main`
      que toque la web.

### Qué se sirve en cada URL

La raíz del sitio **no** es este hub, sino el modelo D3 consolidado de
`master/canendatos_storytelling_d3.html` — el que ya estaba terminado y del que
se migraron `topics/sanidad.js` y `topics/salud-mental.js` (commit `5159c6b`).
Trae geometría NUTS-2 de Eurostat, selector de género y las seis secciones en
tarjetas. El workflow lo envuelve en una página completa al desplegar, porque
el fichero es un fragmento pensado para incrustarse en Divi y sin `<head>`
propio ni sale el charset ni se carga d3.

| URL | Qué es |
| --- | --- |
| `/` | Modelo D3 consolidado (`master/canendatos_storytelling_d3.html`) |
| `/hub/` | Este hub modular, la migración en curso |

Mientras la migración no alcance al modelo consolidado, lo que se enseña es `/`.

### Temáticas activas

Seis, todas leyendo de Supabase: Dependencia, Educación, Empleo, Salud mental,
Sanidad y Vivienda. Desactivadas en el `MANIFEST`: Comunicación y Migraciones
(fuera de alcance) y **Presupuestos**, en cuarentena mientras se resuelve la
asignación de programas presupuestarios a conceptos. Su temática además falla al
renderizar (`renderContext`, `core/engine.js`), pendiente de diagnóstico.

## Seguridad y credenciales

- `core/config.js` contiene la **anon key pública** de Supabase. Es segura
  para commitear: el control de acceso real lo impone Row Level Security
  (RLS) sobre las tablas.
- **Nunca** añadir la service_role key ni la contraseña de Postgres al
  repositorio. Esas viven en `.Renviron` en tu máquina local para el
  pipeline R y están ignoradas por `.gitignore`.

## Requisitos de datos

- Schema `canendatos`. Conviven **tres formas de tabla**, y el motor las admite
  todas:
  - `ced_<tematica>_global` + `ced_<tematica>_gen` — Dependencia, Educación,
    Empleo y Vivienda.
  - `global_<tematica>` + `gen_<tematica>` — Sanidad, que no sigue el prefijo
    `ced_`.
  - **Una sola tabla** con la columna `genero` incluyendo `'total'` — Salud
    mental (`ced_saludmental`). Se declara poniendo `globalTable` y `genderTable`
    al mismo nombre; el motor detecta la igualdad y parte las filas. Sin eso, las
    filas de hombres y mujeres contaminarían la serie global sin dar error.
  - `genderTable: null` para temáticas sin brecha de género: el motor oculta la
    escena "género".
- Schema `geodesocan`: tabla `ccaa` con columna `geom` (geometrías CCAA).
  **Hoy devuelve HTTP 400** para todas las temáticas y el motor cae al fallback
  de `GEO_FALLBACK`; los mapas se dibujan igual. Pendiente de revisar.
- Las tablas deben tener **RLS con política `SELECT` para el rol `anon`**,
  si no la web no verá datos. Lo verifica `.github/workflows/rls-audit.yml`,
  que falla si alguna tabla queda sin RLS o con permisos de escritura para `anon`.

Cada slug marcado `ready: true` en el `MANIFEST` de `index.html` necesita su
`topics/<slug>.js`; `web-deploy.yml` lo comprueba antes de publicar.

## Desarrollo local

Al usar módulos ES (`import/export`), abrir `index.html` con un servidor
estático — no funcionará con `file://`:

```bash
cd canarias-en-datos-web
python3 -m http.server 8000
# → http://localhost:8000
```
