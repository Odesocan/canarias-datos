# ============================================================
# R/ccaa_dictionary.R — Diccionario canónico CCAA del pipeline
# Presupuestos. Compatible con Vivienda / Salud mental / Dependencia.
# Devuelve siempre los 17 nombres canónicos; ciudades autónomas
# disponibles bajo bandera explícita.
# ============================================================

ced_normalize_text_key <- function(x) {
  value <- trimws(as.character(x))
  value <- iconv(value, from = "", to = "ASCII//TRANSLIT")
  value <- tolower(value)
  value <- gsub("^\\d{1,2}\\s*", "", value)
  value <- gsub("[^a-z0-9]+", " ", value)
  trimws(value)
}

# El value mantiene el prefijo INE "NN " para poder ordenar y
# clasificar por código sin perder compatibilidad con los pipelines
# hermanos.
ced_ccaa_dictionary <- c(
  "España" = "00 Media Estatal",
  "Espana" = "00 Media Estatal",
  "ES" = "00 Media Estatal",
  "Total" = "00 Media Estatal",
  "Total Nacional" = "00 Media Estatal",
  "Andalucía" = "01 Andalucía",
  "Andalucia" = "01 Andalucía",
  "AND" = "01 Andalucía",
  "and" = "01 Andalucía",
  "Aragón" = "02 Aragón",
  "Aragon" = "02 Aragón",
  "ARA" = "02 Aragón",
  "ara" = "02 Aragón",
  "Asturias" = "03 Principado de Asturias",
  "Asturias, Principado de" = "03 Principado de Asturias",
  "Principado de Asturias" = "03 Principado de Asturias",
  "AST" = "03 Principado de Asturias",
  "ast" = "03 Principado de Asturias",
  "Balears, Illes" = "04 Islas Baleares",
  "Illes Balears" = "04 Islas Baleares",
  "Islas Baleares" = "04 Islas Baleares",
  "Baleares" = "04 Islas Baleares",
  "BAL" = "04 Islas Baleares",
  "bal" = "04 Islas Baleares",
  "Canarias" = "05 Canarias",
  "Islas Canarias" = "05 Canarias",
  "CAN" = "05 Canarias",
  "can" = "05 Canarias",
  "Cantabria" = "06 Cantabria",
  "CNT" = "06 Cantabria",
  "cnt" = "06 Cantabria",
  "Castilla y León" = "07 Castilla y León",
  "Castilla y Leon" = "07 Castilla y León",
  "Castilla-León" = "07 Castilla y León",
  "CYL" = "07 Castilla y León",
  "cym" = "07 Castilla y León",
  "Castilla-La Mancha" = "08 Castilla-La Mancha",
  "Castilla La Mancha" = "08 Castilla-La Mancha",
  "CLM" = "08 Castilla-La Mancha",
  "clm" = "08 Castilla-La Mancha",
  "Cataluña" = "09 Cataluña",
  "Cataluna" = "09 Cataluña",
  "Catalunya" = "09 Cataluña",
  "CAT" = "09 Cataluña",
  "cat" = "09 Cataluña",
  "Comunitat Valenciana" = "10 Comunidad Valenciana",
  "Comunidad Valenciana" = "10 Comunidad Valenciana",
  "C. Valenciana" = "10 Comunidad Valenciana",
  "VAL" = "10 Comunidad Valenciana",
  "val" = "10 Comunidad Valenciana",
  "Extremadura" = "11 Extremadura",
  "EXT" = "11 Extremadura",
  "ext" = "11 Extremadura",
  "Galicia" = "12 Galicia",
  "GAL" = "12 Galicia",
  "gal" = "12 Galicia",
  "Madrid, Comunidad de" = "13 Comunidad de Madrid",
  "Comunidad de Madrid" = "13 Comunidad de Madrid",
  "Madrid" = "13 Comunidad de Madrid",
  "MAD" = "13 Comunidad de Madrid",
  "mad" = "13 Comunidad de Madrid",
  "Murcia, Región de" = "14 Región de Murcia",
  "Region de Murcia" = "14 Región de Murcia",
  "Región de Murcia" = "14 Región de Murcia",
  "Murcia" = "14 Región de Murcia",
  "MUR" = "14 Región de Murcia",
  "mur" = "14 Región de Murcia",
  "Navarra, Comunidad Foral de" = "15 Comunidad Foral de Navarra",
  "Comunidad Foral de Navarra" = "15 Comunidad Foral de Navarra",
  "Navarra" = "15 Comunidad Foral de Navarra",
  "NAV" = "15 Comunidad Foral de Navarra",
  "nav" = "15 Comunidad Foral de Navarra",
  "País Vasco" = "16 País Vasco",
  "Pais Vasco" = "16 País Vasco",
  "Euskadi" = "16 País Vasco",
  "PVC" = "16 País Vasco",
  "pvc" = "16 País Vasco",
  "Rioja, La" = "17 La Rioja",
  "La Rioja" = "17 La Rioja",
  "LAR" = "17 La Rioja",
  "lar" = "17 La Rioja",
  "Ceuta" = "18 Ceuta",
  "CEU" = "18 Ceuta",
  "ceu" = "18 Ceuta",
  "Melilla" = "19 Melilla",
  "MEL" = "19 Melilla",
  "mel" = "19 Melilla"
)

# Mapping id_ccaa de 3 letras (convención del cuaderno) ↔ código INE.
ced_ccaa_id3 <- c(
  "and"="01","ara"="02","ast"="03","bal"="04","can"="05","cnt"="06",
  "cym"="07","clm"="08","cat"="09","val"="10","ext"="11","gal"="12",
  "mad"="13","mur"="14","nav"="15","pvc"="16","lar"="17",
  "ceu"="18","mel"="19"
)

ced_ccaa_lookup_table <- local({
  lookup <- data.frame(
    raw_name = names(ced_ccaa_dictionary),
    mapped_value = unname(ced_ccaa_dictionary),
    stringsAsFactors = FALSE
  )
  lookup$key <- ced_normalize_text_key(lookup$raw_name)
  lookup$ccaa_code <- sub(" .*", "", lookup$mapped_value)
  lookup$ccaa <- sub("^\\d{2} ", "", lookup$mapped_value)
  lookup <- lookup[!duplicated(lookup$key), c("key", "raw_name", "ccaa_code", "ccaa")]

  function() lookup
})

ced_official_ccaa_levels <- function(include_state = FALSE, include_autonomous_cities = FALSE) {
  lookup <- ced_ccaa_lookup_table()
  catalog <- unique(lookup[, c("ccaa_code", "ccaa")])
  catalog <- catalog[order(catalog$ccaa_code), , drop = FALSE]
  if (!include_state) catalog <- catalog[catalog$ccaa_code != "00", , drop = FALSE]
  if (!include_autonomous_cities) catalog <- catalog[!catalog$ccaa_code %in% c("18", "19"), , drop = FALSE]
  unname(catalog$ccaa)
}

ced_id3_to_ccaa <- function(id3) {
  code <- ced_ccaa_id3[tolower(id3)]
  lookup <- ced_ccaa_lookup_table()
  out <- lookup$ccaa[match(code, lookup$ccaa_code)]
  out
}

ced_ccaa_to_id3 <- function(ccaa) {
  lookup <- ced_ccaa_lookup_table()
  key <- ced_normalize_text_key(ccaa)
  code <- lookup$ccaa_code[match(key, lookup$key)]
  names_id3 <- names(ced_ccaa_id3)
  out <- names_id3[match(code, unname(ced_ccaa_id3))]
  out
}
