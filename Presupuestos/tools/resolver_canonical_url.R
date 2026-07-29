#!/usr/bin/env Rscript
# ============================================================
# tools/resolver_canonical_url.R
#
# Resuelve la URL canónica de cada ejercicio a partir del portal
# declarado en fuentes.yml para los portales con índices dinámicos:
# Aragón, Madrid, Galicia, Castilla y León, Canarias y Euskadi.
#
# Estrategia por CCAA (heurísticas declarativas — no usa JS):
#   1. Descarga la página índice del portal del ejercicio.
#   2. Extrae enlaces <a href> que matcheen patrones específicos
#      (palabras clave + extensión).
#   3. Ordena por preferencia (memoria de programas > tomos > anexos).
#   4. Devuelve la mejor URL.
#
# Escribe `fuentes_resolved.yml` y muestra un diff legible.
#
# Uso:
#   Rscript tools/resolver_canonical_url.R                  # todas
#   Rscript tools/resolver_canonical_url.R --ccaa=ara,mad   # subset
#   Rscript tools/resolver_canonical_url.R --apply          # sobreescribe fuentes.yml
# ============================================================

suppressPackageStartupMessages({
  library(yaml); library(httr); library(rvest); library(xml2)
  library(glue); library(stringr); library(dplyr)
})

PROJECT <- normalizePath(file.path(dirname(sub("^--file=", "",
                          grep("^--file=", commandArgs(), value=TRUE)[1])), ".."),
                          winslash = "/", mustWork = TRUE)
FUENTES_YML <- file.path(PROJECT, "fuentes.yml")
OUT <- file.path(PROJECT, "fuentes_resolved.yml")

cli <- function(args = commandArgs(trailingOnly = TRUE)) {
  out <- list()
  for (a in args) {
    if (grepl("^--", a)) {
      parts <- strsplit(sub("^--", "", a), "=", fixed = TRUE)[[1]]
      out[[parts[1]]] <- if (length(parts) > 1) parts[2] else "true"
    }
  }
  out
}

args <- cli()
ccaa_filter <- if (!is.null(args$ccaa)) strsplit(args$ccaa, ",")[[1]] else NULL
apply <- isTRUE(args$apply == "true")

# ------------------------------------------------------------
# Resolvers por CCAA
# ------------------------------------------------------------

UA <- "ODESOCAN-CanariasEnDatos/0.1 (+https://odesocan.org)"

.fetch_html <- function(url, timeout = 30) {
  tryCatch({
    r <- httr::GET(url, httr::user_agent(UA), httr::timeout(timeout))
    if (httr::status_code(r) >= 400) return(NULL)
    rvest::read_html(httr::content(r, as = "raw"))
  }, error = function(e) NULL)
}

.collect_links <- function(html, base_url, allow_ext = c("pdf","csv","xlsx","zip","ods")) {
  if (is.null(html)) return(tibble::tibble(href = character(0), text = character(0)))
  nodes <- rvest::html_elements(html, "a[href]")
  hrefs <- rvest::html_attr(nodes, "href")
  texts <- trimws(rvest::html_text2(nodes))
  hrefs <- xml2::url_absolute(hrefs, base_url)
  ext_re <- paste0("\\.(", paste(allow_ext, collapse = "|"), ")(\\?|$)")
  keep <- grepl(ext_re, tolower(hrefs))
  tibble::tibble(href = hrefs[keep], text = texts[keep])
}

# Aragón (Liferay): el portal redirige a documents/d/guest/<id>. Heurística:
# busca enlaces con "memoria", "presupuesto", "ingresos_gastos", "anexo" PDF.
resolver_ara <- function(portal_url, ejercicio, alias = "") {
  html <- .fetch_html(portal_url)
  links <- .collect_links(html, portal_url, c("pdf","csv","xlsx"))
  if (nrow(links) == 0) return(NA_character_)
  # Prefiere memoria_programas o ingresos_gastos del ejercicio
  pattern <- sprintf("(memoria.*program|ingresos.*gastos|tomo).*?(?:_|\\b)%s", ejercicio)
  best <- links |> dplyr::filter(grepl(pattern, tolower(.data$text)) |
                                  grepl(pattern, tolower(.data$href)))
  if (nrow(best) > 0) return(best$href[1])
  # Fallback: cualquier PDF con el año en el nombre
  best <- links |> dplyr::filter(grepl(as.character(ejercicio), .data$href))
  if (nrow(best) > 0) return(best$href[1])
  NA_character_
}

# Comunidad de Madrid (presupuestos/presupuestos-generales-comunidad-madrid-AAAA)
# Liferay con bloques de descarga. Buscamos enlaces "Libro 03", "Libro 04" PDF.
resolver_mad <- function(portal_url, ejercicio, alias = "") {
  url <- sub("AAAA", as.character(ejercicio), portal_url)
  html <- .fetch_html(url)
  links <- .collect_links(html, url, c("pdf","xlsx"))
  if (nrow(links) == 0) return(NA_character_)
  pat <- if (grepl("04|programa|memoria", alias, ignore.case = TRUE)) {
    "libro\\s*0?4|programa|memoria"
  } else if (grepl("03|ingresos|gastos", alias, ignore.case = TRUE)) {
    "libro\\s*0?3|ingresos.*gastos"
  } else {
    "libro\\s*0?4|memoria|programa"
  }
  prefer <- links |>
    dplyr::filter(grepl(pat, tolower(.data$text)) | grepl(pat, tolower(.data$href))) |>
    dplyr::filter(!grepl("folleto|resumen", tolower(.data$href)))
  if (nrow(prefer) > 0) return(prefer$href[1])
  links_no_fol <- links |> dplyr::filter(!grepl("folleto", tolower(.data$href)))
  if (nrow(links_no_fol) > 0) return(links_no_fol$href[1])
  links$href[1]
}

# Galicia (transparencia.xunta.gal): índice del año. Heurística: tomos II y III PDF.
resolver_gal <- function(portal_url, ejercicio, alias = "") {
  html <- .fetch_html(portal_url)
  links <- .collect_links(html, portal_url, c("pdf"))
  if (nrow(links) == 0) return(NA_character_)
  prefer <- links |> dplyr::filter(grepl("tomo\\s*(ii|iii|2|3)|memoria|orzament",
                                          tolower(.data$text)) &
                                    grepl(as.character(ejercicio), .data$href))
  if (nrow(prefer) > 0) return(prefer$href[1])
  links$href[grepl(as.character(ejercicio), links$href)][1] %|||% NA_character_
}

`%|||%` <- function(x, y) if (length(x) == 0 || is.na(x)) y else x

# Castilla y León (datosabiertos.jcyl.es): es un dataset CKAN. Busca el primer
# recurso CSV/XLSX descargable del dataset.
resolver_cym <- function(portal_url, ejercicio, alias = "") {
  html <- .fetch_html(portal_url)
  links <- .collect_links(html, portal_url, c("csv","xlsx","zip"))
  if (nrow(links) == 0) return(NA_character_)
  prefer <- links |> dplyr::filter(grepl(as.character(ejercicio), .data$href) |
                                    grepl(as.character(ejercicio), .data$text))
  if (nrow(prefer) > 0) return(prefer$href[1])
  links$href[1]
}

# Canarias (gobiernodecanarias.org/hacienda/planificacionypresupuesto/presupuestos/AAAA/)
resolver_can <- function(portal_url, ejercicio, alias = "") {
  base <- "https://www.gobiernodecanarias.org/hacienda/planificacionypresupuesto/presupuestos/"
  url <- paste0(base, ejercicio, "/")
  html <- .fetch_html(url)
  if (is.null(html)) return(NA_character_)
  # datos_abiertos prefiere CSV/XLSX/ODS del catálogo SEFLogiC
  if (grepl("datos|csv|seflogic", alias, ignore.case = TRUE)) {
    links <- .collect_links(html, url, c("csv","xlsx","ods","zip"))
    if (nrow(links) > 0) return(links$href[1])
    # Fallback: portal datos.canarias.es directo
    catalog <- "https://datos.canarias.es/catalogos/general/dataset?q=presupuesto"
    html2 <- .fetch_html(catalog)
    links2 <- .collect_links(html2 %||% xml2::read_html("<html></html>"),
                              catalog, c("csv","xlsx","ods"))
    if (nrow(links2) > 0) return(links2$href[1])
    return(NA_character_)
  }
  links <- .collect_links(html, url, c("pdf"))
  if (nrow(links) == 0) return(NA_character_)
  # Prefiere "Tomo 3" (Memoria de Programas) sobre "Tomo 4" (Informe Económico)
  by_text <- function(pat) links |>
    dplyr::filter(grepl(pat, tolower(.data$text)) | grepl(pat, tolower(.data$href)))
  prefer <- by_text("tomo[\\s-]?3|memoria.*program|program.*memoria")
  if (nrow(prefer) > 0) return(prefer$href[1])
  prefer <- by_text("memoria|programa")
  if (nrow(prefer) > 0) return(prefer$href[1])
  prefer <- by_text("tomo")
  if (nrow(prefer) > 0) return(prefer$href[1])
  links$href[1]
}
`%||%` <- function(x, y) if (is.null(x)) y else x

# Euskadi (euskadi.eus): los CSV tidy 2022+ están en data.euskadi.eus. La página
# raíz lista ZIPs por ejercicio.
resolver_pvc <- function(portal_url, ejercicio, alias = "") {
  html <- .fetch_html(portal_url)
  links <- .collect_links(html, portal_url, c("zip","csv","xlsx"))
  if (nrow(links) == 0) return(NA_character_)
  prefer <- links |> dplyr::filter(grepl(as.character(ejercicio), .data$href))
  if (nrow(prefer) > 0) return(prefer$href[1])
  links$href[1]
}

RESOLVERS <- list(
  ara = resolver_ara, mad = resolver_mad, gal = resolver_gal,
  cym = resolver_cym, can = resolver_can, pvc = resolver_pvc
)

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
cat("[resolver] Cargando", FUENTES_YML, "\n")
fuentes <- yaml::read_yaml(FUENTES_YML)

target_ccaa <- if (is.null(ccaa_filter)) names(RESOLVERS) else intersect(ccaa_filter, names(RESOLVERS))
cat("[resolver] CCAA objetivo:", paste(target_ccaa, collapse = ", "), "\n\n")

changes <- list()
for (cca in target_ccaa) {
  bloque <- fuentes[[cca]]
  if (is.null(bloque) || is.null(bloque$ejercicios)) next
  portal <- bloque$portal
  resolver <- RESOLVERS[[cca]]
  for (ej in names(bloque$ejercicios)) {
    for (alias in names(bloque$ejercicios[[ej]])) {
      meta <- bloque$ejercicios[[ej]][[alias]]
      old_url <- meta$url
      new_url <- tryCatch(resolver(portal, ej, alias), error = function(e) {
        message(sprintf("  [%s/%s/%s] ERROR: %s", cca, ej, alias, conditionMessage(e)))
        NA_character_
      })
      if (!is.na(new_url) && nzchar(new_url) && new_url != old_url) {
        cat(sprintf("  %s/%s/%-25s\n     ANT: %s\n     NEW: %s\n",
                    cca, ej, alias, old_url, new_url))
        fuentes[[cca]]$ejercicios[[ej]][[alias]]$url <- new_url
        # Si la URL nueva apunta a un PDF/CSV diferente, ajusta tipo
        ext <- tolower(tools::file_ext(sub("\\?.*", "", new_url)))
        if (ext %in% c("pdf","csv","xlsx","zip") && !identical(meta$tipo, ext)) {
          fuentes[[cca]]$ejercicios[[ej]][[alias]]$tipo <- ext
        }
        changes[[length(changes) + 1L]] <- list(ccaa = cca, ejercicio = ej,
                                                  alias = alias, old = old_url,
                                                  new = new_url)
      } else if (is.na(new_url)) {
        cat(sprintf("  %s/%s/%-25s  sin candidato\n", cca, ej, alias))
      } else {
        cat(sprintf("  %s/%s/%-25s  sin cambios\n", cca, ej, alias))
      }
    }
  }
}

cat(sprintf("\n[resolver] %d cambios detectados\n", length(changes)))

if (apply) {
  yaml::write_yaml(fuentes, FUENTES_YML)
  cat("[resolver] APLICADO sobre fuentes.yml\n")
} else {
  yaml::write_yaml(fuentes, OUT)
  cat("[resolver] Diff escrito en", OUT, "(usa --apply para aplicar)\n")
}
