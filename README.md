# canarias-datos

Entorno de desarrollo de Canarias en datos.

## El visor publicado

**https://odesocan.github.io/canarias-datos/**

| URL | Qué es |
| --- | --- |
| [`/`](https://odesocan.github.io/canarias-datos/) | Modelo D3 consolidado: seis áreas, mapa, evolución, brecha de género y metodología |
| [`/hub/`](https://odesocan.github.io/canarias-datos/hub/) | Hub modular (`canarias-en-datos-web/`), la migración en curso |

El `index.html` de la raíz **no existe como fichero en el repositorio**: lo
ensambla el paso *"Ensamblar el sitio"* de
[`.github/workflows/web-deploy.yml`](.github/workflows/web-deploy.yml) juntando,
por este orden, la capa móvil (`master/capa-movil.html`), el modelo
(`master/canendatos_storytelling_d3.html`) y una envoltura con el charset. Se
republica solo en cada push a `main` que toque `master/**` o
`canarias-en-datos-web/**`.

La web lee la base de datos en tiempo real, así que un dato nuevo se ve en la
siguiente carga de página sin necesidad de re-desplegar.
