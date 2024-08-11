# Install required packages
# Load libraries
library(sf)
library(ggplot2)
library(rnaturalearth)
library(rnaturalearthdata)
library(dplyr)

# Define major cities and their coordinates
cities <- data.frame(
  city = c('Lagos', 'Kano', 'Ibadan', 'Abuja', 'Port Harcourt', 'Benin City', 'Maiduguri', 'Zaria', 'Aba', 'Jos'),
  lat = c(6.5244, 12.0022, 7.3775, 9.0723, 4.8241, 6.3382, 11.8333, 11.1113, 5.1167, 9.8965),
  lon = c(3.3792, 8.5320, 3.8958, 7.4913, 7.0336, 5.6235, 13.1510, 7.6839, 7.3667, 8.8997),
  population = c(20, 18, 8, 2.5, 1.8, 7.5, 1.2, 1.0, 0.9, 0.8)
)

# Load Nigeria map data
nigeria <- ne_countries(scale = "medium", returnclass = "sf") %>% 
  filter(admin == "Nigeria")

# Create the map
Kano= ggplot(data = nigeria) +
  geom_sf() +
  geom_point(data = cities, aes(x = lon, y = lat, size = population), color = "green", alpha = 0.6) +
  geom_text(data = cities, aes(x = lon, y = lat, label = city), hjust = 1.1, vjust = 1.1, size = 4, color = "blue") +
  scale_size_continuous(range = c(3, 10), breaks = c(0.8, 1.5, 3.6, 15)) +
  labs(
    title = "Major Cities in Nigeria with Population",
    size = "Population (in millions)"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 20, face = "bold"),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 12),
    axis.title = element_blank(),
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    panel.grid = element_blank()
  )
library(cowplot)
ggdraw() + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.35, y = 0.3, scale = .5) + draw_plot(Kano)
ng_sf %>% ggplot()+ geom_sf() + ggthemes::theme_map()
  ggdraw(Kanawa) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.45, y = 0.39, scale = .2)  