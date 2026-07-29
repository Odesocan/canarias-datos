# ============================================================
# R/correspondencias.R — Asignación de concepto presupuestario.
#
# Resuelve el principio del cuaderno (§3 de la guía: "no equivalencia
# automática"): aplica primero el mapping CCAA-específico declarado en
# correspondencias.yml, y solo si no hay coincidencia recurre a los
# patrones globales y al fuzzy Jaro-Winkler.
#
# Devuelve un tibble con (concepto, score, regla) por cada fila.
# ============================================================

cargar_correspondencias <- function(path) {
  corr <- yaml::read_yaml(path)
  if (is.null(corr$conceptos) || is.null(corr$patrones)) {
    stop(sprintf("%s incompleto: requiere 'conceptos' y 'patrones'", path), call. = FALSE)
  }
  corr$ccaa <- corr$ccaa %||% list()
  corr
}

#' Normaliza un código presupuestario (trim, mayúsculas, sin espacios).
.norm_codigo <- function(x) {
  x <- toupper(trimws(as.character(x)))
  x[is.na(x) | x == ""] <- NA_character_
  x
}

#' Normaliza una denominación (lower, sin acentos, sin signos).
.norm_denominacion <- function(x) {
  x <- tolower(trimws(as.character(x)))
  x <- stringi::stri_trans_general(x, "Latin-ASCII")
  x <- gsub("[^a-z0-9 ]+", " ", x)
  x <- trimws(gsub("\\s+", " ", x))
  x[x == ""] <- NA_character_
  x
}

#' Decide si un código encaja con uno de los patrones (longitud completa) y
#' devuelve el TIPO de match para poder puntuar por especificidad.
#' Evita el falso positivo "41" ⊂ "412": exige que el siguiente carácter,
#' si lo hay, no sea dígito (sí permite letra para variantes 412A/313D).
#' @return list(hit=<patron o NA>, tipo=<"exact"|"prefix"|"wild"|NA>)
.match_codigo_tipo <- function(codigo_norm, candidatos) {
  if (length(candidatos) == 0 || is.na(codigo_norm)) return(list(hit = NA_character_, tipo = NA_character_))
  cand <- toupper(as.character(candidatos))
  for (c in cand) {
    # Comodín explícito "41*": PREFIJO PURO (sin exigir frontera no-dígito).
    # Necesario para códigos funcionales contiguos de 4 díg (p.ej. País Vasco
    # 4111→sanidad, donde "41" nunca casaría por la regla de frontera). Es
    # aditivo: sólo afecta a patrones que terminan en "*".
    if (endsWith(c, "*")) {
      pref <- substr(c, 1L, nchar(c) - 1L)
      if (nzchar(pref) && startsWith(codigo_norm, pref)) return(list(hit = c, tipo = "wild"))
      next
    }
    if (identical(codigo_norm, c)) return(list(hit = c, tipo = "exact"))
    if (startsWith(codigo_norm, c)) {
      siguiente <- substr(codigo_norm, nchar(c) + 1L, nchar(c) + 1L)
      if (siguiente == "" || !grepl("[0-9]", siguiente)) return(list(hit = c, tipo = "prefix"))
    }
  }
  list(hit = NA_character_, tipo = NA_character_)
}

#' Compatibilidad: devuelve sólo el patrón que casó (o NA).
.match_codigo <- function(codigo_norm, candidatos) {
  .match_codigo_tipo(codigo_norm, candidatos)$hit
}

#' ¿La keyword aparece como palabra (o inicio de palabra) en la denominación?
#' Usa frontera de palabra (\\b): 'dependencia' NO casa dentro del token
#' "drogodependencias", pero 'educa' SÍ casa el inicio de "educacion". Corrige
#' los falsos positivos por substring conservando los keywords-prefijo
#' intencionados (educa, agrar, pesq, sanit...).
.match_keyword <- function(den_norm, kw_norm) {
  if (is.na(den_norm) || is.na(kw_norm) || !nzchar(kw_norm)) return(FALSE)
  grepl(paste0("\\b", kw_norm), den_norm, perl = TRUE)
}

#' Número de palabras de una keyword normalizada (para puntuar especificidad).
.nwords_kw <- function(s) {
  if (is.na(s) || !nzchar(s)) return(1L)
  length(strsplit(trimws(s), "\\s+")[[1]])
}

#' Asignación de concepto por ESPECIFICIDAD (best-score-wins).
#'
#' Sustituye el antiguo first-match-wins (que hacía que un keyword de un concepto
#' temprano ganara a un código de otro concepto posterior). Ahora cada regla que
#' casa aporta un CANDIDATO con un score de especificidad y gana el mayor:
#'   codigo CCAA exacto(100) > prefijo(92) > comodin(88)
#'   > keyword CCAA (78 + 6*n_palabras: 1p=84, 2p=90, 3p=96)
#'   > concepto_python local auditado (78)
#'   > codigo global exacto(74) > prefijo(66) > comodin(62)
#'   > keyword global (40 + 10*n_palabras)
#'   > fuzzy Jaro-Winkler (<=35)
#' Un keyword CCAA (aunque sea de 1 palabra) gana al python_local por ser una
#' decisión deliberada del raíz; python_local gana al código global tosco. La
#' frontera de palabra evita que un keyword corto casse dentro de otra palabra.
#' Resuelve p.ej.: "salud publica"(kw 2p=79) gana a codigo global 313A→salud_mental(74);
#' código CCAA 312→soberania(92) gana a keyword 'sanidad'(1p=67) en "sanidad vegetal";
#' y con frontera de palabra 'dependencia' ya no casa en "drogodependencias".
#'
#' @param concepto_python vector chr (opcional) con el concepto del yml LOCAL de
#'   cada CCAA (auditado); entra como candidato de score 78.
#' @return tibble (concepto, score, regla)
asignar_concepto <- function(codigo, denominacion, ccaa = NA_character_, corr,
                              concepto_python = NULL, fuzzy_threshold = 0.92) {
  stopifnot(length(codigo) == length(denominacion))
  n <- length(codigo)
  if (is.null(concepto_python)) concepto_python <- rep(NA_character_, n)
  concepto <- rep(NA_character_, n)
  score    <- rep(0, n)
  regla    <- rep(NA_character_, n)

  cod_norm <- .norm_codigo(codigo)
  den_norm <- .norm_denominacion(denominacion)

  W_CC <- c(exact = 100, prefix = 92, wild = 88)   # codigo CCAA-especifico
  W_GL <- c(exact = 74,  prefix = 66, wild = 62)   # codigo global
  W_PY <- 78                                        # concepto_python local

  # Localiza el bloque CCAA-específico del yml raíz.
  ccaa_block <- NULL
  if (!is.na(ccaa) && length(corr$ccaa) > 0) {
    key_candidates <- c(ccaa, ced_ccaa_to_id3(ccaa), tolower(ccaa))
    for (k in key_candidates) {
      if (!is.null(k) && !is.na(k) && !is.null(corr$ccaa[[k]])) { ccaa_block <- corr$ccaa[[k]]; break }
    }
  }

  # Pre-normaliza reglas (código + keywords con nº de palabras) una sola vez.
  .prep <- function(block) {
    lapply(names(block), function(cid) {
      r <- block[[cid]]
      kws <- .norm_denominacion(r$keywords %||% character(0))
      kws <- kws[!is.na(kws) & nzchar(kws)]
      list(concepto = cid,
           codigos = r$codigos %||% character(0),
           kws = kws,
           nkw = vapply(kws, .nwords_kw, integer(1)))
    })
  }
  cc_rules <- if (!is.null(ccaa_block)) .prep(ccaa_block) else list()
  gl_rules <- .prep(corr$patrones)

  for (i in seq_len(n)) {
    best_c <- NA_character_; best_s <- 0; best_r <- NA_character_
    ci <- cod_norm[i]; di <- den_norm[i]

    # 1) reglas CCAA-específicas (código y keyword)
    for (r in cc_rules) {
      if (length(r$codigos) > 0) {
        m <- .match_codigo_tipo(ci, r$codigos)
        if (!is.na(m$tipo)) { s <- W_CC[[m$tipo]]
          if (s > best_s) { best_c <- r$concepto; best_s <- s; best_r <- paste0("ccaa_codigo:", m$hit) } }
      }
      if (length(r$kws) > 0 && !is.na(di)) {
        for (j in seq_along(r$kws)) {
          if (.match_keyword(di, r$kws[j])) { s <- 78 + 6 * r$nkw[j]
            if (s > best_s) { best_c <- r$concepto; best_s <- s; best_r <- paste0("ccaa_keyword:", r$kws[j]) } }
        }
      }
    }

    # 2) concepto_python local auditado
    if (!is.na(concepto_python[i]) && W_PY > best_s) {
      best_c <- concepto_python[i]; best_s <- W_PY; best_r <- "python_local"
    }

    # 3) patrones globales (código y keyword)
    for (r in gl_rules) {
      if (length(r$codigos) > 0) {
        m <- .match_codigo_tipo(ci, r$codigos)
        if (!is.na(m$tipo)) { s <- W_GL[[m$tipo]]
          if (s > best_s) { best_c <- r$concepto; best_s <- s; best_r <- paste0("global_codigo:", m$hit) } }
      }
      if (length(r$kws) > 0 && !is.na(di)) {
        for (j in seq_along(r$kws)) {
          if (.match_keyword(di, r$kws[j])) { s <- 40 + 10 * r$nkw[j]
            if (s > best_s) { best_c <- r$concepto; best_s <- s; best_r <- paste0("global_keyword:", r$kws[j]) } }
        }
      }
    }

    # 4) fuzzy Jaro-Winkler (sólo si aún no hay nada razonable)
    if (best_s < 40 && !is.na(di) && requireNamespace("stringdist", quietly = TRUE)) {
      tokens <- strsplit(di, " ", fixed = TRUE)[[1]]
      if (length(tokens) > 0) {
        for (r in gl_rules) {
          if (length(r$kws) == 0) next
          for (kw in r$kws) {
            s <- max(1 - stringdist::stringdist(kw, tokens, method = "jw"))
            if (s >= fuzzy_threshold) { sc <- 35 * s
              if (sc > best_s) { best_c <- r$concepto; best_s <- sc; best_r <- "fuzzy_kw" } }
          }
        }
      }
    }

    concepto[i] <- best_c; regla[i] <- best_r
    # Score de salida 0-1 por banda de regla (preserva la semántica de `estimado`
    # aguas abajo: <0.95 = estimado para conceptos estimables).
    score[i] <- if (is.na(best_r)) 0
      else if (startsWith(best_r, "ccaa_codigo"))   1.00
      else if (startsWith(best_r, "ccaa_keyword"))  0.96
      else if (best_r == "python_local")            0.95
      else if (startsWith(best_r, "global_codigo")) 0.92
      else if (startsWith(best_r, "global_keyword"))0.90
      else                                          0.90  # fuzzy_kw
  }

  tibble::tibble(concepto = concepto, score = score, regla = regla)
}

#' Devuelve el catálogo de conceptos (id_concepto, nombre, procedencia).
catalogo_conceptos <- function(corr) {
  tibble::tibble(
    clave       = names(corr$conceptos),
    nombre      = vapply(corr$conceptos, function(x) x$nombre %||% NA_character_, character(1)),
    procedencia = vapply(corr$conceptos, function(x) x$procedencia %||% NA_character_, character(1))
  )
}
