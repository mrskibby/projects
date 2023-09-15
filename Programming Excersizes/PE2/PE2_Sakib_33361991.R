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

################################################################################

# This is the Preferred Terrain VS Observation Count bar chart

# Count number of observations by genus and habitat
genus_habitat_counts <- frog_data %>%
  group_by(Genus, Habitat) %>%
  summarize(count = n()) %>%
  ungroup()

# Create a stacked bar chart with separate bars for Near Water and On Land
genus_count_plot <- ggplot(genus_habitat_counts, aes(x = Genus, y = count, fill = Habitat)) +
  geom_col(position = position_dodge()) +
  labs(x = "Frog Genus", y = "Number of Observations", fill = "Preferred Terrain") +
  ggtitle("Number of Observations by Frog Genus and Preferred Terrain") +
  theme_minimal()

################################################################################

# This is the Hourly observation line graph

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
hourly_line_plot <- ggplot(subset_data, aes(x = Time, group = Genus, color = Genus)) +
  geom_line(stat = "count",size = 1.25) +
  scale_x_discrete(limits = format(seq(as.POSIXct("00:00:00", format="%H:%M:%S"), 
                                       as.POSIXct("23:59:59", format="%H:%M:%S"), 
                                       by="hour"), "%H:%M:%S")) +
  labs(x = "Observation Time", y = "Number of Observations", color = "Frog Genus") +
  ggtitle("Observation Hours for Top Four Frog Genera") +
  theme_minimal()

################################################################################

# Define the UI
ui <- fluidPage(
  # Introduction
  tags$h1("Introduction"),
  tags$p("This exercise is about using shiny, leaflet and ggplot2 in R to make an interactive graph using shiny and leaflet which displays the number of observations of each Genus in each location, then plotting a graph using ggplot2 with Genus on X axis and count of observations on Y axis with respect to preferred terrain of the frogs. And lastly plotting another graph using ggplot2 which shows the number of observations made by each hour for the top types of Genus provided."),
  
  # Genus vs Count plot and leaflet map side by side
  fluidRow(
    column(6, plotOutput("genus_count_plot")),
    column(6, leafletOutput("leaflet_map"),
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
           ))
  ),
  
  # Description of leaflet and Barchart
  tags$h2("Frequency and Location of Frogs"),
  tags$p("The first visualization shows that most of the Crinia frogs likes to stay near water and very very few of them stays on land area, Geocrinia are only found on land, Limnodynastes are found on both near water and on land but they have a slight preference to staying on land, Litoria are opposite of Crinia which are mostly found on land and very few are found near water and Pseudophryne are the rarest of them all whicha re only found near water. 
The Proportional Symbol Map shows different types of frogs are actually scattered throughout Melbourne. Litorias are mostly found on the suburbs and Limnodynastes are found on City areas, Pseudophrynes are rarely seen, Geocrinia are found on grass type areas mostly fields and Crinia have tendency to stay near water source. Most frogs are found within Vermont, Ringwood, Bayswater and Wantirna. Around these areas the frogs very dense."),
  
  # Description of hourly line graph and hourly line graph
  tags$h2("Observation Time"),
  tags$p("The top four Genus of frogs are Crinia, Geocrinia, Limnodynastes and Litoria. Pseudophryne  are very rare thus they are being omiited. At the start of the day or at midnight none of the frogs are observed and eventually up till 7 none of the frogs are actually being observed. At 8am Crinias are seen in less than 20 numbers, Limnodynastes are seen in less than 8 in number and 5 Litorias are seen, they start to fall in number by 9am. Geocrinia starts showing up at 11am only and only 1 to 2 can be seen. By 11 am Crinia also falls to the number of 1, Litoria falls to number 1 and Limnodynastes falls to number less than 5. After 11 Litoria and Crinia and Geocrinia starts increasing very slowly, but Limnodynastes still declines in number. Only at 7pm and 8pm 3 or 4 Limnodynastes and Litorias can be seen. And all disappears by 11 pm again."),
  plotOutput("hourly_line_plot")
)

# Define the server
server <- function(input, output) {
  output$genus_count_plot <- renderPlot({
    genus_count_plot
  })
  
  # This is the leaflet proportional symbol map
  # Render Leaflet map
  output$leaflet_map <- renderLeaflet({
    # Filter data by selected observation type and count the value of observations
    df <- subset(frog_data, Genus %in% input$obs_type)
    value_counts <- table(frog_data$Genus)
    
    # Create a proportional symbol map
    pal <- colorFactor(c("black", "red", "green", "blue", "yellow"),
                       domain = unique(frog_data$Genus))
    
    #plot the proportional symbol map
    leaflet_map <- leaflet(frog_data) %>%
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
  
  
  output$hourly_line_plot <- renderPlot({
    hourly_line_plot
  })
}

# Run the app
shinyApp(ui = ui, server = server)
