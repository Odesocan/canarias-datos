# ============================================================
#  Figura 2: Evolución de los principales indicadores de
#  salud mental en Canarias respecto a todas las CCAA
#  Fuente: ced_saludmental.csv – ODESOCAN · Canarias en Datos
# ============================================================

library(tidyverse)
library(patchwork)

# ── 1. Carga y preparación ───────────────────────────────────
ruta <- paste0(
  "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/",
  "CANARIAS EN DATOS/Salud mental/4_carga/ced_saludmental.csv"
)

# read_csv2: sep = ";" y decimal = ","  (estándar europeo)
df_raw <- read_csv2(ruta)

df <- df_raw |>
  filter(genero == "total") |>
  select(ccaa, anio = periodo, antidep_ajustado, hipno_ajustado,
         t_mental, origen) |>
  mutate(
    es_canarias   = ccaa == "Canarias",
    es_proyeccion = origen == "proyeccion"
  ) |>
  # Reshape a formato largo para función genérica
  pivot_longer(
    cols      = c(antidep_ajustado, hipno_ajustado, t_mental),
    names_to  = "indicador",
    values_to = "valor"
  )


# ── 2. Paleta y tema ─────────────────────────────────────────
COL_CANARIAS <- "#E63946"
COL_RESTO    <- "#B0BEC5"
COL_FONDO    <- "#FAFBFC"
COL_PANEL    <- "#F0F4F8"

ALPHA_RESTO  <- 0.50
SIZE_RESTO   <- 0.40
SIZE_CAN     <- 1.30

tema_fig <- theme_minimal(base_size = 10.5) +
  theme(
    plot.background    = element_rect(fill = COL_FONDO, color = NA),
    panel.background   = element_rect(fill = COL_PANEL, color = NA),
    panel.grid.major.x = element_blank(),
    panel.grid.minor   = element_blank(),
    panel.grid.major.y = element_line(color = "white", linewidth = 0.55),
    axis.text          = element_text(color = "#4A4A4A", size = 8),
    axis.title.y       = element_text(color = "#555555", size = 8.5,
                                      margin = margin(r = 6)),
    axis.title.x       = element_blank(),
    plot.title         = element_text(face = "bold", size = 10.5,
                                      color = "#1C2B3A", margin = margin(b = 2)),
    plot.subtitle      = element_text(size = 7.8, color = "#6B7A8D",
                                      margin = margin(b = 8), lineheight = 1.3),
    legend.position    = "none",
    plot.margin        = margin(10, 20, 8, 10)
  )


# ── 3. Función genérica por indicador ────────────────────────
grafico_indicador <- function(data, id_ind, titulo, subtitulo, etiq_y) {

  d       <- data |> filter(indicador == id_ind)
  d_real  <- d   |> filter(!es_proyeccion)
  d_proy  <- d   |> filter(es_proyeccion)
  d_can_r <- d   |> filter(es_canarias, !es_proyeccion)
  d_can_p <- d   |> filter(es_canarias,  es_proyeccion)

  # Conector entre último año real y primer año proyectado (Canarias)
  anio_union <- max(d_can_r$anio, na.rm = TRUE)
  val_union  <- d_can_r |> filter(anio == anio_union) |> pull(valor)
  anio_proy1 <- min(d_can_p$anio, na.rm = TRUE)
  val_proy1  <- d_can_p |> filter(anio == anio_proy1) |> pull(valor)
  seg_can    <- tibble(
    x = anio_union, xend = anio_proy1,
    y = val_union,  yend = val_proy1
  )

  # Etiqueta final (último año proyectado)
  anio_fin  <- max(d_can_p$anio, na.rm = TRUE)
  valor_fin <- d_can_p |> filter(anio == anio_fin) |> pull(valor)

  ggplot() +

    # ── Resto CCAA – datos reales ──
    geom_line(
      data      = d_real |> filter(!es_canarias),
      aes(x = anio, y = valor, group = ccaa),
      color     = COL_RESTO, alpha = ALPHA_RESTO,
      linewidth = SIZE_RESTO, lineend = "round"
    ) +

    # ── Resto CCAA – proyecciones ──
    geom_line(
      data      = d_proy |> filter(!es_canarias),
      aes(x = anio, y = valor, group = ccaa),
      color     = COL_RESTO, alpha = ALPHA_RESTO * 0.7,
      linewidth = SIZE_RESTO, linetype = "dashed", lineend = "round"
    ) +

    # ── Canarias – datos reales ──
    geom_line(
      data      = d_can_r,
      aes(x = anio, y = valor, group = ccaa),
      color     = COL_CANARIAS, linewidth = SIZE_CAN, lineend = "round"
    ) +

    # ── Canarias – conector real→proyección ──
    geom_segment(
      data  = seg_can,
      aes(x = x, xend = xend, y = y, yend = yend),
      color = COL_CANARIAS, linewidth = SIZE_CAN,
      linetype = "dashed", lineend = "round"
    ) +

    # ── Canarias – proyecciones ──
    geom_line(
      data      = d_can_p,
      aes(x = anio, y = valor, group = ccaa),
      color     = COL_CANARIAS, linewidth = SIZE_CAN,
      linetype  = "dashed", lineend = "round"
    ) +

    # ── Canarias – puntos en datos reales ──
    geom_point(
      data   = d_can_r,
      aes(x = anio, y = valor),
      shape  = 21, fill = "white", color = COL_CANARIAS,
      size   = 1.8, stroke = 1.2
    ) +

    # ── Banda sombreada proyección ──
    annotate(
      "rect",
      xmin = anio_union + 0.5, xmax = anio_fin + 0.5,
      ymin = -Inf, ymax = Inf,
      fill = "#E0E8F0", alpha = 0.35
    ) +

    # ── Etiqueta "Proyección" ──
    annotate(
      "text",
      x = anio_union + 1.5, y = Inf,
      label = "Proyección", vjust = 1.6, size = 2.5,
      color = "#7A8EA0", fontface = "italic"
    ) +

    # ── Etiqueta Canarias + valor final ──
    annotate(
      "text",
      x = anio_fin + 0.2, y = valor_fin,
      label      = paste0("Canarias\n", round(valor_fin, 1)),
      color      = COL_CANARIAS, fontface = "bold",
      size       = 2.9, hjust = 0, vjust = 0.4, lineheight = 1.15
    ) +

    scale_x_continuous(
      breaks = seq(2010, anio_fin, by = 2),
      expand = expansion(mult = c(0.02, 0.15))
    ) +
    scale_y_continuous(expand = expansion(mult = c(0.05, 0.08))) +
    labs(title = titulo, subtitle = subtitulo, y = etiq_y) +
    tema_fig
}


# ── 4. Los tres gráficos ─────────────────────────────────────
g1 <- grafico_indicador(
  data      = df,
  id_ind    = "antidep_ajustado",
  titulo    = "DHD antidepresivos",
  subtitulo = "Dosis Diarias Definidas ajustadas\npor 1.000 hab./día",
  etiq_y    = "DHD"
)

g2 <- grafico_indicador(
  data      = df,
  id_ind    = "hipno_ajustado",
  titulo    = "Gráfico 2. DHD hipnóticos y sedantes",
  subtitulo = "Dosis Diarias Definidas ajustadas\npor 1.000 hab./día",
  etiq_y    = "DHD"
)

g3 <- grafico_indicador(
  data      = df,
  id_ind    = "t_mental",
  titulo    = "Prevalencia de trastornos mentales",
  subtitulo = "Tasa registrada en población general\n(%)",
  etiq_y    = "Prevalencia (%)"
)


# ── 5. Leyenda como mini-gráfico ─────────────────────────────
df_ley <- tibble(
  x     = c(0.01, 0.09,  0.38, 0.46),
  y     = c(0.65, 0.65,  0.65, 0.65),
  grupo = c("Resto de CCAA", "Resto de CCAA", "Canarias", "Canarias")
)
df_ley_d <- tibble(
  x     = c(0.12, 0.20,  0.49, 0.57),
  y     = c(0.35, 0.35,  0.35, 0.35),
  grupo = c("Resto de CCAA", "Resto de CCAA", "Canarias", "Canarias")
)
df_ley_pt <- tibble(x = 0.42, y = 0.65, grupo = "Canarias")

leyenda <- ggplot() +
  # Línea continua (datos reales)
  geom_line(
    data = df_ley,
    aes(x = x, y = y, color = grupo, group = grupo),
    linewidth = 1.2
  ) +
  # Línea discontinua (proyección)
  geom_line(
    data = df_ley_d,
    aes(x = x, y = y, color = grupo, group = grupo),
    linewidth = 1.2, linetype = "dashed"
  ) +
  geom_point(
    data  = df_ley_pt,
    aes(x = x, y = y, color = grupo),
    shape = 21, fill = "white", size = 2.8, stroke = 1.3
  ) +
  scale_color_manual(
    values = c("Canarias" = COL_CANARIAS, "Resto de CCAA" = COL_RESTO)
  ) +
  # Etiquetas fila 1 (reales)
  annotate("text", x = 0.11, y = 0.65, label = "Resto de CCAA (dato real)",
           hjust = 0, size = 3.0, color = "#555555") +
  annotate("text", x = 0.48, y = 0.65, label = "Canarias (dato real)",
           hjust = 0, size = 3.0, color = COL_CANARIAS, fontface = "bold") +
  # Etiquetas fila 2 (proyección)
  annotate("text", x = 0.22, y = 0.35, label = "Proyección",
           hjust = 0, size = 3.0, color = "#555555") +
  annotate("text", x = 0.59, y = 0.35, label = "Proyección Canarias",
           hjust = 0, size = 3.0, color = COL_CANARIAS, fontface = "bold") +
  xlim(0, 1) + ylim(0, 1) +
  theme_void() +
  theme(
    plot.background = element_rect(fill = COL_FONDO, color = NA),
    legend.position = "none"
  )


# ── 6. Composición final ─────────────────────────────────────
figura2 <- (g1 | g2 | g3) +
  plot_annotation(
    title      = paste0(
      "Figura 2: Evolución de los principales indicadores de salud mental\n",
      "en Canarias respecto a todas las CCAA (2010–2026)"
    ),
    caption    = paste0(
      "Fuente: Sistema de Información Sanitaria (MSCBS). ",
      "Elaboración propia – ODESOCAN · Canarias en Datos. ",
      "Datos 2024–2026: proyecciones. Total poblacional (ambos sexos)."
    ),
    theme = theme(
      plot.background = element_rect(fill = COL_FONDO, color = NA),
      plot.margin     = margin(14, 16, 8, 16),
      plot.title      = element_text(
        face = "bold", size = 13.5, color = "#1C2B3A",
        margin = margin(b = 4)
      ),
      plot.caption    = element_text(
        size = 7.8, color = "#777777", hjust = 0,
        margin = margin(t = 8), lineheight = 1.4
      )
    )
  )

figura2_final <- figura2 /
  plot_spacer() /
  leyenda +
  plot_layout(heights = c(10, 0.05, 1.1))


# ── 7. Exportar ──────────────────────────────────────────────
ruta_salida <- paste0(
  "/Users/cristiancpv/Desktop/TRABAJO/OBSERVATORIO/",
  "CANARIAS EN DATOS/Salud mental/fuentes/raw/sanidad/",
  "figura2_salud_mental.png"
)

ggsave(
  filename = ruta_salida,
  plot     = figura2_final,
  width    = 13,
  height   = 6.2,
  dpi      = 300,
  bg       = COL_FONDO
)

message("✓ Figura guardada en: ", ruta_salida)
