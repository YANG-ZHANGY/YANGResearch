#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(ggplot2)
  library(scales)
  library(jsonlite)
})

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(script_arg) != 1L) stop("Run this file with Rscript.")
script_path <- sub("^--file=", "", script_arg)
script_path <- gsub("~+~", " ", script_path, fixed = TRUE)
code_dir <- dirname(normalizePath(script_path, mustWork = TRUE))
package_root <- dirname(code_dir)
source_dir <- file.path(package_root, "source_data")
figure_dir <- file.path(package_root, "figures")
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

font_family <- "sans"
navy <- "#2B4C7E"
burnt_orange <- "#B35C1E"
npg_blue <- "#3C5488"
npg_red <- "#E64B35"
dark_grey <- "#4D4D4D"
mid_grey <- "#737373"
grid_grey <- "#D9D9D9"

theme_journal <- function(base_size = 10.5, base_family = font_family) {
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(
      text = element_text(colour = dark_grey),
      axis.title = element_text(
        colour = "#111111", size = rel(1.08),
        margin = margin(t = 6, r = 6, b = 6, l = 6)
      ),
      axis.text = element_text(colour = dark_grey, size = rel(0.92)),
      axis.ticks = element_line(colour = dark_grey, linewidth = 0.35),
      axis.ticks.length = grid::unit(1.8, "mm"),
      axis.line = element_line(colour = dark_grey, linewidth = 0.42),
      panel.background = element_rect(fill = "white", colour = NA),
      plot.background = element_rect(fill = "white", colour = NA),
      plot.margin = margin(7, 8, 7, 7),
      legend.background = element_rect(fill = "transparent", colour = NA),
      legend.key = element_rect(fill = "transparent", colour = NA),
      legend.title = element_blank(),
      legend.text = element_text(colour = "#111111", size = rel(0.93))
    )
}

png_type <- if (capabilities("aqua")) {
  "quartz"
} else if (capabilities("cairo")) {
  "cairo"
} else {
  "Xlib"
}

save_plot_set <- function(plot, stem, width_mm, height_mm) {
  pdf_path <- file.path(figure_dir, paste0(stem, ".pdf"))
  png_path <- file.path(figure_dir, paste0(stem, ".png"))
  tif_path <- file.path(figure_dir, paste0(stem, ".tiff"))
  ggsave(
    pdf_path, plot = plot, device = grDevices::pdf,
    width = width_mm, height = height_mm, units = "mm",
    useDingbats = FALSE, bg = "white"
  )
  ggsave(
    png_path, plot = plot, device = grDevices::png,
    width = width_mm, height = height_mm, units = "mm",
    dpi = 600, type = png_type, bg = "white"
  )
  python <- Sys.which("python3")
  if (!nzchar(python)) stop("python3 is required to create TIFF files.")
  status <- system2(
    python,
    c(
      shQuote(file.path(code_dir, "png_to_lzw_tiff.py")),
      shQuote(png_path),
      shQuote(tif_path)
    )
  )
  if (!identical(status, 0L)) stop("TIFF conversion failed for ", stem)
}

flatten_geojson <- function(path) {
  geojson <- jsonlite::fromJSON(path, simplifyVector = FALSE)
  rows <- list()
  row_index <- 1L
  append_ring <- function(
    ring, feature_index, polygon_index, ring_index,
    admin, continent, iso3
  ) {
    coordinates <- do.call(rbind, ring)
    data.frame(
      long = as.numeric(coordinates[, 1]),
      lat = as.numeric(coordinates[, 2]),
      order = seq_len(nrow(coordinates)),
      group = paste(feature_index, polygon_index, ring_index, sep = "."),
      admin = admin,
      continent = continent,
      iso3 = iso3,
      stringsAsFactors = FALSE
    )
  }
  for (feature_index in seq_along(geojson$features)) {
    feature <- geojson$features[[feature_index]]
    properties <- feature$properties
    admin <- properties$ADMIN
    continent <- properties$CONTINENT
    iso3 <- properties$ISO_A3
    if (admin == "France") iso3 <- "FRA"
    if (admin == "Norway") iso3 <- "NOR"
    geometry_type <- feature$geometry$type
    coordinates <- feature$geometry$coordinates
    if (geometry_type == "Polygon") {
      polygons <- list(coordinates)
    } else if (geometry_type == "MultiPolygon") {
      polygons <- coordinates
    } else {
      next
    }
    for (polygon_index in seq_along(polygons)) {
      polygon <- polygons[[polygon_index]]
      for (ring_index in seq_along(polygon)) {
        rows[[row_index]] <- append_ring(
          polygon[[ring_index]], feature_index, polygon_index, ring_index,
          admin, continent, iso3
        )
        row_index <- row_index + 1L
      }
    }
  }
  do.call(rbind, rows)
}

world_polygons <- flatten_geojson(
  file.path(source_dir, "ne_110m_admin_0_countries.geojson")
)
figure1_counts <- read.csv(
  file.path(source_dir, "figure1_country_counts.csv"),
  check.names = FALSE, stringsAsFactors = FALSE
)
country_to_iso3 <- c(
  "Ukraine" = "UKR", "Italy" = "ITA", "Turkey III" = "TUR",
  "Georgia" = "GEO", "Moldova" = "MDA",
  "North Macedonia" = "MKD", "Russia" = "RUS",
  "Albania" = "ALB", "Greece III" = "GRC",
  "Czechia" = "CZE", "France IV" = "FRA",
  "Montenegro" = "MNE", "Serbia" = "SRB",
  "Slovakia" = "SVK", "Slovenia" = "SVN"
)
figure1_counts$iso3 <- unname(country_to_iso3[figure1_counts$country])
incident_lookup <- setNames(figure1_counts$Incidents, figure1_counts$iso3)
label_positions <- data.frame(
  iso3 = c(
    "FRA", "CZE", "SVK", "SVN", "ITA", "MNE", "SRB",
    "ALB", "MKD", "GRC", "MDA", "UKR", "RUS", "TUR", "GEO"
  ),
  long = c(
    2.35, 15.35, 19.45, 14.90, 12.55, 19.25, 20.80,
    20.00, 21.75, 22.85, 28.55, 31.35, 30.30, 35.50, 43.35
  ),
  lat = c(
    48.85, 49.82, 48.70, 46.12, 42.60, 42.78, 44.02,
    41.10, 41.60, 39.05, 47.18, 49.02, 59.90, 39.00, 42.05
  ),
  stringsAsFactors = FALSE
)
label_positions$Incidents <- unname(incident_lookup[label_positions$iso3])
map_data <- world_polygons[
  world_polygons$continent == "Europe" | world_polygons$iso3 == "TUR",
]
map_data$Incidents <- unname(incident_lookup[map_data$iso3])
map_data$Incidents[is.na(map_data$Incidents)] <- 0
labels <- label_positions[
  label_positions$iso3 %in% unique(map_data$iso3) &
    label_positions$Incidents > 0,
]
reds <- c(
  "#FFF5F0", "#FEE0D2", "#FCBBA1", "#FC9272", "#FB6A4A",
  "#EF3B2C", "#CB181D", "#A50F15", "#67000D"
)
figure1 <- ggplot(
  map_data,
  aes(x = long, y = lat, group = group, subgroup = group, fill = Incidents)
) +
  geom_polygon(colour = "#383838", linewidth = 0.20, linejoin = "round") +
  geom_text(
    data = labels,
    aes(x = long, y = lat, label = Incidents),
    inherit.aes = FALSE, family = font_family, fontface = "bold",
    colour = "#111111", size = 2.65
  ) +
  scale_fill_gradientn(
    colours = reds, limits = c(0.5, 19), oob = scales::squish,
    breaks = seq(2.5, 17.5, by = 2.5),
    labels = label_number(accuracy = 0.1),
    name = "Number of Legislative Brawls"
  ) +
  guides(
    fill = guide_colourbar(
      title.position = "right",
      title.theme = element_text(
        family = font_family, colour = "#111111", angle = 90,
        hjust = 0.5, vjust = 0.5, size = 8.5
      ),
      label.theme = element_text(
        family = font_family, colour = dark_grey, size = 7.8
      ),
      barheight = grid::unit(57, "mm"),
      barwidth = grid::unit(5.2, "mm"),
      frame.colour = "#333333", frame.linewidth = 0.35, ticks = TRUE
    )
  ) +
  coord_quickmap(
    xlim = c(-25, 50), ylim = c(30, 72),
    expand = FALSE, clip = "on"
  ) +
  theme_void(base_family = font_family, base_size = 10) +
  theme(
    plot.background = element_rect(fill = "white", colour = NA),
    panel.background = element_rect(fill = "white", colour = NA),
    legend.position = "right",
    legend.margin = margin(0, 0, 0, 2),
    plot.margin = margin(5, 5, 5, 5)
  )
save_plot_set(
  figure1, "figure1_recorded_legislative_violence_europe",
  width_mm = 180, height_mm = 152
)

figure2_data <- read.csv(
  file.path(source_dir, "figure2_publication_source.csv"),
  check.names = FALSE, stringsAsFactors = FALSE
)
figure2_levels <- c(
  "Lower polarisation (10th pct.)",
  "Higher polarisation (90th pct.)"
)
figure2_data$polarisation_level <- factor(
  figure2_data$polarisation_level, levels = figure2_levels
)
figure2_low <- figure2_data[
  figure2_data$polarisation_level == figure2_levels[1],
]
figure2_high <- figure2_data[
  figure2_data$polarisation_level == figure2_levels[2],
]
closure_mean <- unique(figure2_data$mean_closure_reference)[1]
figure2 <- ggplot() +
  geom_ribbon(
    data = figure2_low,
    aes(x = closure, ymin = ci_low, ymax = ci_high),
    fill = navy, alpha = 0.14, colour = NA
  ) +
  geom_ribbon(
    data = figure2_high,
    aes(x = closure, ymin = ci_low, ymax = ci_high),
    fill = burnt_orange, alpha = 0.14, colour = NA
  ) +
  geom_line(
    data = figure2_data,
    aes(
      x = closure, y = mean,
      colour = polarisation_level, linetype = polarisation_level
    ),
    linewidth = 0.85, lineend = "butt"
  ) +
  geom_vline(
    xintercept = closure_mean, colour = mid_grey,
    linewidth = 0.45, linetype = "dashed"
  ) +
  annotate(
    "text", x = closure_mean + 1.7, y = 0.060,
    label = sprintf("Mean closure = %.1f", closure_mean),
    angle = 90, hjust = 0.5, vjust = 0.5,
    family = font_family, size = 3.0, colour = dark_grey
  ) +
  scale_colour_manual(
    values = c(
      "Lower polarisation (10th pct.)" = navy,
      "Higher polarisation (90th pct.)" = burnt_orange
    ),
    breaks = figure2_levels, drop = FALSE
  ) +
  scale_linetype_manual(
    values = c(
      "Lower polarisation (10th pct.)" = "solid",
      "Higher polarisation (90th pct.)" = "longdash"
    ),
    breaks = figure2_levels, drop = FALSE
  ) +
  scale_x_continuous(
    limits = c(33, 100), breaks = seq(40, 100, by = 10),
    expand = expansion(mult = c(0, 0))
  ) +
  scale_y_continuous(
    limits = c(0, 0.10), breaks = seq(0, 0.08, by = 0.02),
    labels = label_number(accuracy = 0.01),
    expand = expansion(mult = c(0, 0))
  ) +
  labs(x = "Party-system closure", y = "Predicted annual incidents") +
  guides(
    colour = guide_legend(
      override.aes = list(
        linewidth = 1.05, linetype = c("solid", "longdash")
      ),
      keywidth = grid::unit(13, "mm"),
      keyheight = grid::unit(4.5, "mm"), byrow = TRUE
    ),
    linetype = "none"
  ) +
  theme_journal(base_size = 10.5) +
  theme(
    panel.grid.major.y = element_line(colour = grid_grey, linewidth = 0.35),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    legend.position = "inside",
    legend.position.inside = c(0.015, 0.985),
    legend.justification = c(0, 1),
    legend.direction = "vertical",
    legend.spacing.y = grid::unit(0.3, "mm"),
    legend.margin = margin(0, 0, 0, 0),
    axis.title.x = element_text(margin = margin(t = 7)),
    axis.title.y = element_text(margin = margin(r = 7))
  )
save_plot_set(
  figure2, "figure2_predicted_incidence_closure_polarisation",
  width_mm = 180, height_mm = 124
)

figure3_data <- read.csv(
  file.path(source_dir, "figure3_leave_one_country_out_source.csv"),
  check.names = FALSE, stringsAsFactors = FALSE
)
figure3_top_to_bottom <- c(
  "ITA", "GEO", "SRB", "HUN", "CYP", "BEL", "SVK", "HRV",
  "EST", "ROU", "PRT", "LTU", "ESP", "FIN", "CHE", "DEU",
  "GBR", "DNK", "SWE", "MLT", "IRL", "ISL", "AUT", "NOR",
  "LUX", "LIE", "SVN", "NLD", "CZE", "AND", "MNE", "TUR",
  "MKD", "POL", "SMR", "BGR", "ALB", "GRC", "LVA", "FRA",
  "MDA", "RUS", "UKR"
)
figure3_data$omitted_iso3 <- factor(
  figure3_data$omitted_iso3, levels = rev(figure3_top_to_bottom)
)
full_sample_coefficient <- unique(figure3_data$full_sample_coef)[1]
legend_levels <- c("Leave-one-out estimate", "Full-sample estimate")
figure3 <- ggplot(figure3_data, aes(y = omitted_iso3)) +
  geom_vline(
    xintercept = 0, colour = "#8C8C8C",
    linewidth = 0.40, linetype = "dashed"
  ) +
  geom_vline(
    aes(xintercept = full_sample_coefficient, colour = "Full-sample estimate"),
    linewidth = 0.65, linetype = "dashed",
    key_glyph = "path", show.legend = TRUE
  ) +
  geom_segment(
    aes(x = ci_low, xend = ci_high, yend = omitted_iso3),
    colour = npg_blue, linewidth = 0.42, lineend = "butt"
  ) +
  geom_point(
    aes(x = coef, colour = "Leave-one-out estimate"),
    size = 2.15, shape = 16, show.legend = TRUE
  ) +
  scale_colour_manual(
    values = c(
      "Leave-one-out estimate" = npg_blue,
      "Full-sample estimate" = npg_red
    ),
    limits = legend_levels, breaks = legend_levels, drop = FALSE
  ) +
  scale_x_continuous(
    limits = c(-1.90, 0.05), breaks = seq(-1.75, 0, by = 0.25),
    labels = label_number(accuracy = 0.01),
    expand = expansion(mult = c(0, 0))
  ) +
  scale_y_discrete(expand = expansion(add = c(0.65, 1.55))) +
  labs(
    x = "Coefficient for party institutionalisation",
    y = "Country omitted"
  ) +
  guides(
    colour = guide_legend(
      override.aes = list(
        shape = c(16, NA), linetype = c("blank", "dashed"),
        linewidth = c(0, 0.75), size = c(2.5, NA)
      ),
      keywidth = grid::unit(11, "mm"),
      keyheight = grid::unit(4.5, "mm"), byrow = TRUE
    )
  ) +
  theme_journal(base_size = 9.7) +
  theme(
    panel.grid.major.x = element_line(colour = "#D0D0D0", linewidth = 0.38),
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    axis.text.y = element_text(size = 8.6, margin = margin(r = 2)),
    axis.text.x = element_text(size = 8.8),
    axis.title.x = element_text(size = 10.2, margin = margin(t = 7)),
    axis.title.y = element_text(size = 10.2, margin = margin(r = 7)),
    legend.position = "inside",
    legend.position.inside = c(0.985, 0.012),
    legend.justification = c(1, 0),
    legend.direction = "vertical",
    legend.margin = margin(1, 1, 1, 1),
    plot.margin = margin(5, 6, 5, 5)
  )
save_plot_set(
  figure3, "figure3_leave_one_country_out_party_institutionalisation",
  width_mm = 180, height_mm = 238
)

message("Publication figures written to: ", figure_dir)
