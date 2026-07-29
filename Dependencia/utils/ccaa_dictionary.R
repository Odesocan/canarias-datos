ced_normalize_text_key <- function(x) {
  value <- trimws(as.character(x))
  value <- iconv(value, from = "", to = "ASCII//TRANSLIT")
  value <- tolower(value)
  value <- gsub("^\\d{1,2}\\s*", "", value)
  value <- gsub("[^a-z0-9]+", " ", value)
  trimws(value)
}

ced_ccaa_dictionary <- c(
  # --- Media Estatal ---
  "España (ES)" = "00 Media Estatal",
  "España" = "00 Media Estatal",
  "Media Estatal" = "00 Media Estatal",
  "Total" = "00 Media Estatal",
  "Total Nacional" = "00 Media Estatal",
  "TOTAL NACIONAL" = "00 Media Estatal",
  "TOTAL" = "00 Media Estatal",
  "MEDIA ESTATAL" = "00 Media Estatal",
  # --- 01 Andalucia ---
  "Andalucía" = "01 Andalucía",
  "Andalucía (AN)" = "01 Andalucía",
  "ANDALUCÍA" = "01 Andalucía",
  "Andalucia" = "01 Andalucía",
  # --- 02 Aragon ---
  "Aragón" = "02 Aragón",
  "ARAGÓN" = "02 Aragón",
  "Aragón (AR)" = "02 Aragón",
  "Aragon" = "02 Aragón",
  # --- 03 Principado de Asturias ---
  "Asturias" = "03 Principado de Asturias",
  "ASTURIAS, PRINCIPADO DE" = "03 Principado de Asturias",
  "Asturias, Principado de" = "03 Principado de Asturias",
  "Asturias, Principado de (AS)" = "03 Principado de Asturias",
  "Asturias,Principado de" = "03 Principado de Asturias",
  "Principado de Asturias" = "03 Principado de Asturias",
  "Asturias, Principado" = "03 Principado de Asturias",
  "ASTURIAS, (PRINCIPADO DE)" = "03 Principado de Asturias",
  "03 Asturias, Principado de" = "03 Principado de Asturias",
  # --- 04 Islas Baleares ---
  "Balears, Illes" = "04 Islas Baleares",
  "BALEARS, ILLES" = "04 Islas Baleares",
  "Balears, Illes (IB)" = "04 Islas Baleares",
  "Islas Baleares" = "04 Islas Baleares",
  "Illes Balears" = "04 Islas Baleares",
  "BALEARS (ILLES)" = "04 Islas Baleares",
  "04 Balears, Illes" = "04 Islas Baleares",
  "Baleares" = "04 Islas Baleares",
  # --- 05 Canarias ---
  "Canarias" = "05 Canarias",
  "CANARIAS" = "05 Canarias",
  "Canarias (CN)" = "05 Canarias",
  "Islas Canarias" = "05 Canarias",
  # --- 06 Cantabria ---
  "Cantabria" = "06 Cantabria",
  "CANTABRIA" = "06 Cantabria",
  "Cantabria (CB)" = "06 Cantabria",
  # --- 07 Castilla y Leon ---
  "Castilla y León" = "07 Castilla y León",
  "CASTILLA Y LEÓN" = "07 Castilla y León",
  "Castilla León" = "07 Castilla y León",
  "Castilla-León" = "07 Castilla y León",
  "Castilla y León (CL)" = "07 Castilla y León",
  "CastillayLeón" = "07 Castilla y León",
  "Castilla y Leon" = "07 Castilla y León",
  # --- 08 Castilla-La Mancha ---
  "Castilla-La Mancha" = "08 Castilla-La Mancha",
  "Castilla-Mancha" = "08 Castilla-La Mancha",
  "Castilla - La Mancha" = "08 Castilla-La Mancha",
  "CASTILLA - LA MANCHA" = "08 Castilla-La Mancha",
  "Castilla la Mancha" = "08 Castilla-La Mancha",
  "Castilla - LaMancha" = "08 Castilla-La Mancha",
  "Castilla - La Mancha (CM)" = "08 Castilla-La Mancha",
  "Castilla- La Mancha" = "08 Castilla-La Mancha",
  "08 Castilla - La Mancha" = "08 Castilla-La Mancha",
  "CASTILLA-LA MANCHA" = "08 Castilla-La Mancha",
  # --- 09 Cataluna ---
  "Cataluña" = "09 Cataluña",
  "CATALUÑA" = "09 Cataluña",
  "Cataluña (CT)" = "09 Cataluña",
  "Catalunya" = "09 Cataluña",
  # --- 10 Comunidad Valenciana ---
  "Comunitat Valenciana" = "10 Comunidad Valenciana",
  "COMUNITAT VALENCIANA" = "10 Comunidad Valenciana",
  "Comunitat Valenciana (VC)" = "10 Comunidad Valenciana",
  "10 Comunitat Valenciana" = "10 Comunidad Valenciana",
  "ComunitatValenciana" = "10 Comunidad Valenciana",
  "C.Valenciana" = "10 Comunidad Valenciana",
  "C. Valenciana" = "10 Comunidad Valenciana",
  "Comunidad Valenciana" = "10 Comunidad Valenciana",
  # --- 11 Extremadura ---
  "Extremadura" = "11 Extremadura",
  "EXTREMADURA" = "11 Extremadura",
  "Extremadura (EX)" = "11 Extremadura",
  # --- 12 Galicia ---
  "Galicia" = "12 Galicia",
  "GALICIA" = "12 Galicia",
  "Galicia (GA)" = "12 Galicia",
  # --- 13 Comunidad de Madrid ---
  "Madrid, Comunidad de" = "13 Comunidad de Madrid",
  "MADRID, COMUNIDAD DE" = "13 Comunidad de Madrid",
  "MADRID (COMUNIDAD DE)" = "13 Comunidad de Madrid",
  "Madrid, Comunidad de (MD)" = "13 Comunidad de Madrid",
  "13 Madrid, Comunidad de" = "13 Comunidad de Madrid",
  "Comunidad de Madrid" = "13 Comunidad de Madrid",
  "Madrid, Comunidadde" = "13 Comunidad de Madrid",
  "Madrid" = "13 Comunidad de Madrid",
  "Madrid,Comunidad de" = "13 Comunidad de Madrid",
  # --- 14 Region de Murcia ---
  "Murcia, Región de" = "14 Región de Murcia",
  "MURCIA, REGIÓN DE" = "14 Región de Murcia",
  "MURCIA (REGIÓN DE)" = "14 Región de Murcia",
  "14 Murcia, Región de" = "14 Región de Murcia",
  "Murcia, Región de (MC)" = "14 Región de Murcia",
  "Murcia" = "14 Región de Murcia",
  "Región de Murcia" = "14 Región de Murcia",
  "Murcia, Region de" = "14 Región de Murcia",
  # --- 15 Comunidad Foral de Navarra ---
  "Navarra, Comunidad Foral de" = "15 Comunidad Foral de Navarra",
  "NAVARRA, COMUNIDAD FORAL DE" = "15 Comunidad Foral de Navarra",
  "NAVARRA (COMUNIDAD FORAL DE)" = "15 Comunidad Foral de Navarra",
  "15 Navarra, Comunidad Foral de" = "15 Comunidad Foral de Navarra",
  "Comunidad Foral de Navarra" = "15 Comunidad Foral de Navarra",
  "Navarra, C. Foral de (NC)" = "15 Comunidad Foral de Navarra",
  "Navarra" = "15 Comunidad Foral de Navarra",
  "Navarra, C. Foral de" = "15 Comunidad Foral de Navarra",
  "Navarra,ComunidadesForal de" = "15 Comunidad Foral de Navarra",
  # --- 16 Pais Vasco ---
  "País Vasco" = "16 País Vasco",
  "Pais Vasco" = "16 País Vasco",
  "PAÍS VASCO" = "16 País Vasco",
  "País Vasco (PV)" = "16 País Vasco",
  "Euskadi/País Vasco" = "16 País Vasco",
  "Euskadi/Pais Vasco" = "16 País Vasco",
  # --- 17 La Rioja ---
  "Rioja, La" = "17 La Rioja",
  "RIOJA (LA)" = "17 La Rioja",
  "RIOJA, LA" = "17 La Rioja",
  "17 Rioja, La" = "17 La Rioja",
  "Rioja, La (RI)" = "17 La Rioja",
  "La Rioja" = "17 La Rioja",
  "La Rioja (RI)" = "17 La Rioja",
  "Rioja" = "17 La Rioja",
  # --- 18 Ceuta ---
  "Ceuta" = "18 Ceuta",
  "COMUNIDAD AUTÓNOMA DE CEUTA" = "18 Ceuta",
  "Ceuta (CE)" = "18 Ceuta",
  # --- 19 Melilla ---
  "Melilla" = "19 Melilla",
  "COMUNIDAD AUTÓNOMA DE MELILLA" = "19 Melilla",
  "Melilla (ML)" = "19 Melilla",
  # --- 20 Ceuta y Melilla (combinado IMSERSO) ---
  "Ceuta y Melilla" = "20 Ceuta y Melilla",
  "CEUTA Y MELILLA" = "20 Ceuta y Melilla",
  "Ceuta y  Melilla" = "20 Ceuta y Melilla"
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

  function() {
    lookup
  }
})

ced_official_ccaa_levels <- function(include_state = FALSE,
                                    include_autonomous_cities = FALSE,
                                    include_ceuta_melilla_combined = TRUE) {
  lookup <- ced_ccaa_lookup_table()
  catalog <- unique(lookup[, c("ccaa_code", "ccaa")])
  catalog <- catalog[order(catalog$ccaa_code), , drop = FALSE]

  if (!include_state) {
    catalog <- catalog[catalog$ccaa_code != "00", , drop = FALSE]
  }
  if (!include_autonomous_cities) {
    catalog <- catalog[!catalog$ccaa_code %in% c("18", "19"), , drop = FALSE]
  }
  if (!include_ceuta_melilla_combined) {
    catalog <- catalog[catalog$ccaa_code != "20", , drop = FALSE]
  }

  unname(catalog$ccaa)
}
