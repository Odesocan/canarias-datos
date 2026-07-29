# ============================================================
#  Dumbbell Chart · Alquiler Canarias según tipo de tenedor
#  Formato Instagram Stories 9:16 — TEMA CLARO (v8)
#  ODESOCAN · odesocan.org
# ============================================================

library(dplyr)
library(tidyr)
library(forcats)
library(stringr)
library(ggplot2)
library(ggtext)
library(scales)
library(glue)


# ════════════════════════════════════════════════════════════
#  BLOQUE 1 — RUTA - SUPABASE
# ════════════════════════════════════════════════════════════

library(DBI)
library(odbc)

con <- dbConnect(
  odbc::odbc(),
  Driver   = "/opt/homebrew/lib/psqlodbcw.so",
  Server   = "aws-1-eu-west-1.pooler.supabase.com",
  Port     = 5432,
  Database = "postgres",
  UID      = "postgres.kdpsjutsgvghdtzoskkg",
  PWD      = "TU_PASSWORD",
  sslmode  = "require"
)
on.exit(dbDisconnect(con), add = TRUE)

alquiler_canarias <- dbReadTable(con, DBI::Id(schema = "public", table = "alquiler_canarias"))
dbDisconnect(con)


# ════════════════════════════════════════════════════════════
#  BLOQUE 2 — PALETA
# ════════════════════════════════════════════════════════════

FONDO      <- "#F4F7FA"
FONDO2     <- "#FFFFFF"
COL_PART   <- "#1A6FA8"
COL_PROF   <- "#B03A2E"
COL_SEG    <- "#C8D6E5"
COL_BRECHA <- "#D35400"
COL_TEXTO  <- "#1A2535"
COL_SUBTXT <- "#5D7285"
COL_GRID   <- "#DDE4ED"
COL_ACENTO <- "#1A3A5C"

# Colores de isla — distintos a COL_PART / COL_PROF para evitar confusión
ISLA_COL <- c(
  "Gran Canaria"  = "#2E86AB",
  "Tenerife"      = "#7B2D8E",
  "Lanzarote"     = "#B7770D",
  "Fuerteventura" = "#1E8449",
  "La Palma"      = "#C0392B",
  "La Gomera"     = "#117A65",
  "El Hierro"     = "#616A6B"
)

ISLA_BG <- c(
  "Gran Canaria"  = "#E8F4F8",
  "Tenerife"      = "#F3EAF6",
  "Lanzarote"     = "#FDF6E7",
  "Fuerteventura" = "#EAFAF1",
  "La Palma"      = "#FDEDEC",
  "La Gomera"     = "#E8F6F3",
  "El Hierro"     = "#F2F3F4"
)


# ════════════════════════════════════════════════════════════
#  BLOQUE 3 — DATOS
# ════════════════════════════════════════════════════════════

df_raw <- alquiler_canarias

acortar <- function(x) {
  x <- case_match(x,
    "Las Palmas de Gran Canaria" ~ "Las Palmas de GC",
    "Santa Cruz de Tenerife"     ~ "SC de Tenerife",
    "Santa Lucía de Tirajana"    ~ "Sta. Lucía de Tirajana",
    "Granadilla de Abona"        ~ "Granadilla de Abona",
    "Puerto de la Cruz"          ~ "Puerto de la Cruz",
    .default = x
  )
  str_wrap(x, width = 16)
}

df_wide <- df_raw |>
  group_by(municipio, isla, tipo_anunciante) |>
  summarise(
    precio_medio = mean(precio_euros, na.rm = TRUE),
    n            = n(),
    .groups      = "drop"
  ) |>
  pivot_wider(
    names_from  = tipo_anunciante,
    values_from = c(precio_medio, n)
  ) |>
  drop_na(precio_medio_particular, precio_medio_profesional) |>
  mutate(
    brecha     = precio_medio_profesional - precio_medio_particular,
    brecha_pct = round(brecha / precio_medio_particular * 100, 1),
    mid        = (precio_medio_particular + precio_medio_profesional) / 2,

    municipio_label = fct_reorder(acortar(municipio), brecha_pct),
    y_num           = as.numeric(fct_reorder(acortar(municipio), brecha_pct)),
    fondo_isla      = recode(isla, !!!ISLA_BG),

    # ── Etiqueta precio particular:
    #    - Si particular < profesional (brecha > 0): a la izquierda del punto
    #    - Si particular > profesional (brecha < 0): a la derecha del punto
    part_hjust = if_else(brecha >= 0, 1.25, -0.20),
    part_vjust = 0.5,

    # ── Etiqueta precio profesional:
    #    - Si profesional > particular (brecha > 0): a la derecha del punto
    #    - Si profesional < particular (brecha < 0): a la izquierda del punto
    #    - Excepción: si > 2500, encima del punto para no salirse del gráfico
    prof_hjust = case_when(
      precio_medio_profesional > 2500 ~ 0.5,
      brecha >= 0                     ~ -0.20,
      TRUE                            ~ 1.25
    ),
    prof_vjust = if_else(precio_medio_profesional > 2500, 1.9, 0.5),

    # ── Etiqueta brecha: signo correcto (sin "+" en negativos)
    brecha_label = if_else(brecha_pct >= 0,
                           paste0("+", brecha_pct, "%"),
                           paste0(brecha_pct, "%"))
  )

# Posición de la columna de porcentaje
X_DIVIDER <- max(df_wide$precio_medio_profesional, na.rm = TRUE) + 200
X_BRECHA  <- X_DIVIDER + 260


# ════════════════════════════════════════════════════════════
#  BLOQUE 4 — TEXTOS
# ════════════════════════════════════════════════════════════

# Calcular titular dinámicamente
max_brecha <- df_wide |> slice_max(brecha_pct, n = 1)
TITULAR <- glue("El alquiler con inmobiliaria cuesta hasta un {max_brecha$brecha_pct}% más que el particular")

leg_grupos <- glue(
  "<span style='color:{COL_PART};font-weight:700'>● Particular</span>",
  "&emsp;",
  "<span style='color:{COL_PROF};font-weight:700'>● Inmobiliaria</span>"
)

# Leyenda dinámica: solo islas presentes en los datos
islas_presentes <- sort(unique(df_wide$isla))
leg_islas <- paste(
  sapply(islas_presentes, function(isla) {
    glue(
      "<span style='background:{ISLA_BG[isla]};",
      "color:{ISLA_COL[isla]};",
      "padding:2px 6px;border-radius:3px;font-weight:600'>",
      "{isla}</span>"
    )
  }),
  collapse = "&ensp;"
)

# Insight dinámico
INSIGHT <- glue(
  "{max_brecha$municipio} registra la mayor brecha: ",
  "+{format(round(max_brecha$brecha), big.mark = '.')} €/mes ",
  "(+{max_brecha$brecha_pct}%) entre inmobiliaria y particular"
)
PIE     <- "Fuente: Idealista · Elaboración: ODESOCAN · Abril 2026"
CUENTA  <- "odesocan.org  ·  @odesocan"

caption_txt <- glue(
  "<span style='color:{COL_BRECHA};font-weight:700'>{INSIGHT}</span>",
  "<br>",
  "<span style='color:{COL_SUBTXT}'>{CUENTA}&emsp;{PIE}</span>"
)


# ════════════════════════════════════════════════════════════
#  BLOQUE 5 — GRÁFICO
# ════════════════════════════════════════════════════════════

p <- ggplot(df_wide) +

  # ── Franjas de isla ─────────────────────────────────────────
  geom_rect(
    aes(xmin = -Inf, xmax = Inf,
        ymin = y_num - 0.50,
        ymax = y_num + 0.50,
        fill = fondo_isla)
  ) +
  scale_fill_identity() +

  # ── Línea divisoria vertical ─────────────────────────────────
  geom_vline(
    xintercept = X_DIVIDER,
    color      = COL_GRID,
    linewidth  = 0.5
  ) +

  # ── Segmento conector ────────────────────────────────────────
  geom_segment(
    aes(x    = precio_medio_particular,
        xend = precio_medio_profesional,
        y    = municipio_label,
        yend = municipio_label),
    color = COL_SEG, linewidth = 3.5, lineend = "round"
  ) +

  # ── Label brecha — columna fija derecha ──────────────────────
  geom_label(
    aes(x     = X_BRECHA,
        y     = municipio_label,
        label = brecha_label),
    size          = 3.0,
    color         = COL_BRECHA,
    fill          = FONDO2,
    linewidth     = 0.35,
    label.padding = unit(0.22, "lines"),
    fontface      = "bold",
    hjust         = 0.5,
    vjust         = 0.5
  ) +

  # ── Puntos — particular ──────────────────────────────────────
  geom_point(aes(x = precio_medio_particular, y = municipio_label),
             color = "white", size = 5.5) +
  geom_point(aes(x = precio_medio_particular, y = municipio_label),
             shape = 21, fill = COL_PART, color = "white",
             size = 4.0, stroke = 0.8) +

  # ── Puntos — profesional ─────────────────────────────────────
  geom_point(aes(x = precio_medio_profesional, y = municipio_label),
             color = "white", size = 5.5) +
  geom_point(aes(x = precio_medio_profesional, y = municipio_label),
             shape = 21, fill = COL_PROF, color = "white",
             size = 4.0, stroke = 0.8) +

  # ── Etiqueta valor — particular ──────────────────────────────
  geom_text(
    aes(x     = precio_medio_particular,
        y     = municipio_label,
        label = paste0(
          format(round(precio_medio_particular),
                 big.mark = ".", decimal.mark = ","), " €"),
        hjust = part_hjust,
        vjust = part_vjust),
    size     = 3.0,
    color    = COL_PART,
    fontface = "bold"
  ) +

  # ── Etiqueta valor — profesional ─────────────────────────────
  geom_text(
    aes(x     = precio_medio_profesional,
        y     = municipio_label,
        label = paste0(
          format(round(precio_medio_profesional),
                 big.mark = ".", decimal.mark = ","), " €"),
        hjust = prof_hjust,
        vjust = prof_vjust),
    size     = 3.0,
    color    = COL_PROF,
    fontface = "bold"
  ) +

  # ── Escalas ──────────────────────────────────────────────────
  scale_x_continuous(
    limits = c(
      min(df_wide$precio_medio_particular, na.rm = TRUE) - 200,
      X_BRECHA + 200
    ),
    breaks = seq(800, 2800, by = 400),
    labels = function(x) {
      paste0(format(x, big.mark = ".", decimal.mark = ","), " €")
    },
    expand = expansion(mult = c(0, 0))
  ) +

  scale_y_discrete(expand = expansion(add = c(0.7, 0.7))) +

  # ── Títulos ──────────────────────────────────────────────────
  labs(
    title    = TITULAR,
    subtitle = glue("{leg_grupos}<br>{leg_islas}"),
    x        = "Precio medio mensual (€/mes)",
    y        = NULL,
    caption  = caption_txt
  ) +

  # ── Tema ─────────────────────────────────────────────────────
  theme_minimal(base_size = 10) +
  theme(

    plot.background  = element_rect(fill = FONDO, color = NA),
    panel.background = element_rect(fill = FONDO, color = NA),

    panel.grid.major.x = element_line(color = COL_GRID, linewidth = 0.40),
    panel.grid.major.y = element_blank(),
    panel.grid.minor   = element_blank(),

    axis.text.x  = element_text(color = COL_SUBTXT, size = 7.5,
                                  margin = margin(t = 3)),
    axis.title.x = element_text(color = COL_SUBTXT, size = 8,
                                  margin = margin(t = 6)),
    axis.ticks   = element_blank(),

    axis.text.y = element_text(
      color      = COL_TEXTO,
      size       = 8,
      face       = "bold",
      hjust      = 1,
      lineheight = 1.15,
      margin     = margin(r = 4)
    ),

    plot.title = element_textbox_simple(
      size       = 13,
      face       = "bold",
      color      = COL_ACENTO,
      lineheight = 1.22,
      margin     = margin(b = 8),
      width      = unit(1, "npc"),
      hjust      = 0,
      halign     = 0
    ),

    plot.subtitle = element_markdown(
      size       = 8,
      color      = COL_SUBTXT,
      lineheight = 1.9,
      margin     = margin(b = 14)
    ),

    plot.caption = element_markdown(
      size       = 6.5,
      color      = COL_SUBTXT,
      hjust      = 0.5,
      lineheight = 1.7,
      margin     = margin(t = 14)
    ),

    plot.margin = margin(t = 65, r = 10, b = 65, l = 8)
  )

print(p)


# ════════════════════════════════════════════════════════════
#  BLOQUE 6 — EXPORTAR · 1080 × 1920 px (9:16)
# ════════════════════════════════════════════════════════════

ggsave(
  filename = "story_alquiler_canarias_claro_v8.png",
  plot     = p,
  width    = 4.50,
  height   = 8.00,
  dpi      = 240,
  bg       = FONDO
)

message("story_alquiler_canarias_claro_v8.png  ->  1080 x 1920 px")
