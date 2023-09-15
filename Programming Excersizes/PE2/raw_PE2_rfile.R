#loading packages
library("data.table")
library(dplyr)
library(ggplot2)
library(jsonlite)
library(leaflet)
library(shiny)
library(cartography)
library(sp)
library(plotly)
library(reshape2)
library(tidyr)
library(tidyverse)

# specifying the path
path <- "D:/Monash/Sem1/FIT5147 Data Visualization/PE 2/PE2_frog_data.csv"

# reading contents of csv file
frog_data <- read.csv(path)
# contents of the csv file
View(frog_data)

# rounding to 3 decimal place for Longitude and Latitude
frog_data <- frog_data %>% mutate(across(c(Longitude, Latitude), ~ round(., 3)))

# filter out the missing values
frog_data <- frog_data  %>% filter(!is.na(Latitude))
frog_data <- frog_data  %>% filter(!is.na(Longitude))
frog_data <- frog_data  %>% filter(!is.na(Genus))

View(frog_data)

# Define UI
ui <- fluidPage(
  titlePanel("Proportional Symbol Map"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("n_obs", "Number of Observations", min = 1, max = nrow(frog_data), value = 250),
      checkboxGroupInput("obs_type", "Observation Type", unique(frog_data$Genus), selected = unique(frog_data$Genus)[1])
    ),
    mainPanel(
      leafletOutput("map")
    ),
    position = c("right"),
    fluid = TRUE
  )
)

# Define server
server <- function(input, output) {
  output$map <- renderLeaflet({
    
    # Filter data by selected observation type and count the value of observations
    df <- subset(frog_data, Genus %in% input$obs_type)
    value_counts <- table(frog_data$Genus)
    
    # Create a proportional symbol map
    pal <- colorFactor(c("black", "red", "green", "blue", "yellow"),
                       domain = unique(frog_data$Genus))
    
    #plot the proportional symbol map
    frog_location_map <- leaflet(frog_data) %>%
      addTiles() %>%
      addCircleMarkers(lng = ~Longitude,
                       lat = ~Latitude,
                       popup = ~paste0("Value: ", unique(frog_data$Genus), "<br>Total Count: ", value_counts[frog_data$Genus]),
                       color = ~pal(Genus),
                       stroke = FALSE,
                       fillOpacity = 0.5,
                       fillColor = ~pal(Genus)
      ) %>%
      #add legend for frog genus
      addLegend(
        pal = pal,
        values = frog_data$Genus,
        title = "Genus",
        position = "bottomleft"
      )
  })
}

# Run the app
shinyApp(ui, server)

#########################################################################################

# This is the Genus VS Number of observation bar chart 

# Count number of observations by genus and habitat
genus_habitat_counts <- frog_data %>%
  group_by(Genus, Habitat) %>%
  summarize(count = n()) %>%
  ungroup()

# Create a stacked bar chart with separate bars for Near Water and On Land
ggplot(genus_habitat_counts, aes(x = Genus, y = count, fill = Habitat)) +
  geom_col(position = position_dodge()) +
  labs(x = "Frog Genus", y = "Number of Observations", fill = "Preferred Terrain") +
  ggtitle("Number of Observations by Frog Genus and Preferred Terrain") +
  theme_minimal()

########################################################################################

# This is the Hourly Number of observation line graph

# Convert Time_Start column to POSIXct format
frog_data$Time_Start <- as.POSIXct(frog_data$Time_Start)

# Create a new column with only the time
frog_data$Time <- format(frog_data$Time_Start, "%H:%M:%S")

# Subset data to include only the top four genera
top_genera <- frog_data %>%
  count(Genus, sort = TRUE) %>%
  top_n(4)
subset_data <- frog_data %>% filter(Genus %in% top_genera$Genus)

# Create a line graph
ggplot(subset_data, aes(x = Time, group = Genus, color = Genus)) +
  geom_line(stat = "count",size = 1.25) +
  scale_x_discrete(limits = format(seq(as.POSIXct("00:00:00", format="%H:%M:%S"), 
                                       as.POSIXct("23:59:59", format="%H:%M:%S"), 
                                       by="hour"), "%H:%M:%S")) +
  labs(x = "Observation Time", y = "Number of Observations", color = "Frog Genus") +
  ggtitle("Observation Hours for Top Four Frog Genera") +
  theme_minimal()