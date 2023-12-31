# installing packages 
#install.packages("data.table")
#install.packages("dplyr")
#install.packages("ggplot2")
#install.packages("shiny")
#install.packages("jsonlite")
#install.packages("tidyverse")
#install.packages("maps")
#install.packages("plotly")
#install.packages("gganimate")
#install.packages("animation")
#install.packages("gapminder")
#install.packages("readr")
#install.packages("reshape2")
#install.packages("ggthemes")
#install.packages("RColorBrewer")


# loading packages
library("data.table")
library(dplyr)
library(ggplot2)
library(shiny)
library(jsonlite)
library(tidyverse)
library(maps)
library(plotly)
library(gganimate)
library(animation)
library(gapminder)
library(ggthemes)
library(readr)
library(reshape2)
library(RColorBrewer)


# before running the code please change the datasets locations
# specifying the path
mul_country <- read.csv("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/mul_country.csv")
json_data <- fromJSON("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/Refugee_per_state.json")
json_data_state <- fromJSON("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/table-data.json")
heatmap <- read.csv("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/API_SM.POP.REFG.OR_DS2_en_csv_v2_4696212.csv")
refugee_data <- read.csv("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/clean_data_11_except_refused.csv")
unemployment_data <- read.csv("D:/Monash/Sem1/FIT5147 Data Visualization/Project/Data Visualization Project/Datasets/unemployment_rate.csv") 

#declaring 2 variables for refugee data
years <- unique(refugee_data$qn1jyear)
color_palette <- brewer.pal(nlevels(refugee_data$ui_work), "Set3")


ui <- fluidPage(
  # Introduction
  tags$h4("Name: Nazmus Sakib, StudentID: 33361991, FIT5147 Data Exploration and Visualization S1 2023, Tutor: Niranjan Nanjunda"),
  tags$p("This is the Data Visualization Project on Refugee Unemployment Rate in USA. 
         The audience is any Statistitian or anyone who works with Unemployment or at the Bureau of Statistics."),
      
  tags$head(
    tags$style(
      HTML("
      body {
        background-repeat: repeat;
        height: 100vh;
        margin: 0;
      }
      
      .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 15vh;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      }
      
      .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(to right, red, blue);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        cursor: pointer;
        padding: 20px;
        transition: background-position 1s ease;
        background-size: 200% auto;
        animation: shine 5s linear infinite;
      }
      ")
    )
  ),
  
  div(class = "title-container",
      div(class = "title", "Refugees Unemployment")
  ),
  tags$h4("This is a graph of Annual Change VS Year for United States of America, Canada, France and Germany. 
          The user can select from the dropdown list and if not then it will display all the countries together."),
  
  fluidRow(
    column(3, selectInput("country_select", "Select Country:",
                          choices = c("All", "France", "United States", "Germany", "Canada"),
                          selected = "All"),
           textOutput("country_info")),
    column(8, plotOutput("refugees_plot"))
  ),
  tags$p("  "),
  tags$p("  "),
  tags$p("  "),
  
  tags$h4("This is a graph below shows the Refugee intake of the countries. 
          If hovered over any point in line it will display year and number of refugee intake for that year. 
          We can see that Germany has taken 1.418 Million refugees in 1993 which is the highest recorded. 
          And the lowest was taken by Canada in the year 1965 where they took only 9800 refugees."),
  tags$p(" "),
  plotlyOutput("mul_country_refugee"),
  
  tags$p("  "),
  tags$p("  "),
  tags$p("  "),
  
  tags$h4("This is an animated graph which shows in which state the refugees entered inside USA for the year 2020. 
          The data shows the informations of the refugees who answered the survey. 
          This data does not display information for all the 340 thousand refugges that entered USA. 
          The minimum number of refugees settled in Disctrict of Columbia for just 5 refugees and the maximum settle for Texas which is 7479 in number and also has information on all the states of USA. 
          The color codes show from dark to light with lower number to higher number of refugees. Click the play button and watch the animation."),
  plotlyOutput("state_map"),
  tags$h4("The Disctrict of Columbia is so small that it cannot be displayed with 100% of the country in view. 
          Please Zoom in and zoom out as per your convenience. 
          You can also slide the slider and show the specific state. 
          When you hover over the state it will display the State Name and the Total Number of Refugees."),
  
  tags$h4("  "),
  tags$h4("  "),
  tags$h4("  "),
  
  tags$h4("This is a Proportional Symbol maps to display the refugee's work status and the year they entered in USA"),
  plotlyOutput("proportionalSymbolGraph"),
  tags$h4("The work status is denoted by ui_work and the representation is as follows:
          1 = Working now, 
          2 = Not working now but previously worked in us, 
          3 = not working now and never worked in us. 
          It can be displayed that 2016 was the year with the most number of refugee with working status 1, 2 and 3. 
          334 refugees are working, 103 refugees are not working but have worked befoer in USA and 205 refugees have not found work yet in USA"),
  
  tags$p(" "),
  tags$p(" "),
  tags$p(" "),
  
  plotlyOutput("proportionalSymbolGraph2"),
  tags$h4("The graph above displays a proportional symbol graph of refugee PR Status and the year they entered. 
          The PR status is denoted by ui_lpr and the representation is as follows:
          1 = Already has PR in USA, 
          2 = Does not have PR but applied for PR in USA, 
          3 = Not applied yet. It can be displayed that in 2016 the highest number of refugee got PR which is 572 in number. 
          The highest number of refugees who applied for PR is in 2018 with only 81 refugees and 15 refugees who entered in 2017 didnot apply for PR yet."),
  
  tags$p(" "),
  tags$p(" "),
  tags$p(" "),
  
  tags$h4("This line graph below displays the unemployment rate with the refugees. 
          The user can click on the button to display or hide the information for all the years together. 
          Different years are represented by different colors and the play button displays the information of the unemployment rate according to the year."),
  titlePanel("Animated Line Graph"),
  actionButton("toggle_button", "Show/Hide All Years Together"),
  plotlyOutput("animation"),
  tags$h4("We can see that the maximum unemployment rate was in 2020 April for 14.4"),
  
  tags$p(" "),
  tags$p(" "),
  tags$p(" "),
  
  plotlyOutput("correlationGraph"),
  tags$h4("The graph above displays the correlation matrix between all the variables that have been selected from the ASR Dataset.
          It actually describes that none of the variables in the dataset has a strong correlation with each other. 
          Hover over the graph to view the exact correlation"),
  
  fluidRow(
    column(2, selectInput("year_select", "Select Year:",
                          choices = c("1960","1970","1980","1990","2000","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"),
                          selected = "2021"),
              textOutput("country_year_info")),
    column(9, plotlyOutput("heatmapworld")),
  ),
  
  tags$p(" "),
  tags$p(" "),
  tags$p(" "),
  
  # A conclusion can not be made as more data is required for that 
  # analysis. We could only see that refugees granted asylum and Annual Change of US, the correct number 
  # of total refugees and the total number of refugees that are working now is yet to be determined. The job 
  # opening rate and the unemployment rate is discovered but that does not say anything about refugees, 
  # so those graphs are for refugees as well as citizens. A refugee employment dataset is needed for the 
  # analysis of the second question.
)

server <- function(input, output) {
  
  #Render Proportional Symbol Graph for Work Status
  output$proportionalSymbolGraph <- renderPlotly({
    # Load and prepare data
    data <- refugee_data
    
    # Filter data to include only rows where 'ui_work' <= 3
    data <- data[data$ui_work <= 3, ]
    
    # Count the number of refugees for each combination of 'qn1jyear' and 'ui_work'
    data_count <- data %>%
      group_by(qn1jyear, ui_work) %>%
      summarise(n = n(), .groups = "drop")
    
    # Create a proportional symbol graph
    p <- ggplot(data_count, aes(x = as.factor(ui_work), y = as.factor(qn1jyear), size = n, color = as.factor(ui_work),
                                text = paste("Year: ", qn1jyear, "<br>Work: ", ui_work, "<br>Total refugees: ", n))) +
      geom_point(alpha = 0.6) +
      scale_size_continuous(range = c(1, 15)) +
      labs(x = "Work", y = "Year", size = "Total refugees", color = "Work") +
      theme_minimal() +
      theme(legend.position = "bottom")
    
    ggplotly(p, tooltip = "text")
  })
  
  #Render Proportional Symbol Graph for PR Status
  output$proportionalSymbolGraph2 <- renderPlotly({
    # Load and prepare data
    data <- refugee_data
    
    # Filter data to include only rows where 'ui_lpr' <= 3
    data <- data[data$ui_lpr <= 3, ]
    
    # Count the number of refugees for each combination of 'qn1jyear' and 'ui_lpr'
    data_count <- data %>%
      group_by(qn1jyear, ui_lpr) %>%
      summarise(n = n(), .groups = "drop")
    
    # Create a proportional symbol graph
    p <- ggplot(data_count, aes(x = as.factor(ui_lpr), y = as.factor(qn1jyear), size = n, color = as.factor(ui_lpr),
                                text = paste("Year: ", qn1jyear, "<br>PR Status: ", ui_lpr, "<br>Total refugees: ", n))) +
      geom_point(alpha = 0.6) +
      scale_size_continuous(range = c(1, 15)) +
      labs(x = "PR Status", y = "Year", size = "Total refugees", color = "PR Status") +
      theme_minimal() +
      theme(legend.position = "bottom")
    
    ggplotly(p, tooltip = "text")
  })
  
  
  # Render Animated line graph
  output$animation <- renderPlotly({
    #taking the data in data variable
    data <- unemployment_data
    
    #reshaping the data
    data_melt <- reshape2::melt(data, id.vars = "Year", variable.name = "Month", value.name = "Rate")
    
    #turning months into factors
    data_melt$Month <- factor(data_melt$Month, levels = month.abb)
    
    if(!is.null(input$toggle_button) && input$toggle_button %% 2 == 1) {
      p <- ggplot(data_melt, aes(x = Month, y = Rate, colour = as.factor(Year), group = Year, 
                                 text = paste("Year: ", Year, "<br>Month: ", Month, "<br>Rate: ", Rate))) + 
        geom_line() + 
        theme_minimal() +
        labs(x = "Month", y = "Unemployment Rate", colour = "Year") +
        theme(legend.title = element_blank())
    } else {
      # If the button is clicked an even number of times or not clicked at all, show the animated plot
      p <- ggplot(data_melt, aes(x = Month, y = Rate, colour = as.factor(Year), group = Year, 
                                 text = paste("Year: ", Year, "<br>Month: ", Month, "<br>Rate: ", Rate), frame = Year)) + 
        geom_line() + 
        theme_minimal() +
        labs(x = "Month", y = "Unemployment Rate", colour = "Year") +
        theme(legend.title = element_blank()) +
        transition_reveal(Year)
    }
    
    ggplotly(p, tooltip = "text")
  
  })
  
  
  # Render correlation matrix graph
  output$correlationGraph <- renderPlotly({
    
    # Get data for correlation graph
    cor_matrix <- cor(refugee_data)
    
    # display the graph
    heatmap <- plot_ly(
      z = cor_matrix,
      x = colnames(cor_matrix),
      y = colnames(cor_matrix),
      type = "heatmap",
      colorscale = "Viridis"
    )
    
  })
  
  # Render heat map of USA region only 
  output$state_map <- renderPlotly({
    #This dataset json data and it is turned to Uppercase for ease of use.
    json_data_state <- lapply(json_data_state, function(x) {
      if(is.character(x)) {
        toupper(x)
      } else {
        x
      }
    })
    
    #merge 20 json dataset on state
    states_data <- merge(json_data, json_data_state, by = "state", all = TRUE)
    
    #Remove null values
    states_data_clean <- na.omit(states_data)
    
    #only take code, state, Total and abbrev from all the columns
    statesdf <- states_data_clean[c("code", "state", "Total", "abbrev")] %>%
      mutate(hover = paste0(state, "\nRefugees: ", Total))
    
    #plot the graph
    plot_geo(statesdf,
             locationmode = "USA-states",
             frame = ~Total) %>%
      add_trace(locations = ~code,
                z = ~Total,
                zmin = min(statesdf$Total),
                zmax = max(statesdf$Total),
                color = ~Total,
                colorscale = "Electric",
                text = ~hover,
                hoverinfo = 'text') %>%
      layout(geo = list(scope = 'usa'))
  })
  
  # Render line graph for refugee intake
  output$mul_country_refugee <- renderPlotly({
    mul_country$date <- dmy(mul_country$date)
    
    # Extract the year from the date column
    mul_country$year <- year(mul_country$date)
    
    # Change the date format to 19th century if the year is greater than 2022
    mul_country$year[mul_country$year > 2022] <- mul_country$year[mul_country$year > 2022] - 100
    
    #plot the line chart
    plot_ly(data = mul_country, x = ~year, mode = "bar") %>%
      add_trace(y = ~us_Refugees_Granted_Asylum, name = "USA Refugee Intake") %>%
      add_trace(y = ~Ge_Asylum, name = "Germany Refugee Intake") %>%
      add_trace(y = ~France_Refugees, name = "France Refugee Intake") %>%
      add_trace(y = ~Canada_Refugees, name = "Canada Refugee Intake") %>%
      layout(title = "Refugee Numbers",
             xaxis = list(title = "Year"),
             yaxis = list(title = "Number of Refugees"),
             font = list(color = 'black'))
  })
  
  #Render heat map of the world
  output$heatmapworld <- renderPlotly({
    #get the world map
    mapdata <- map_data("world")
    
    #join 2 dataset by region
    mapdata <-left_join(mapdata, heatmap, by="region")
    
    # Lets user to select year and display info according to that
      mapdata$Refugee_Count <- switch (input$year_select,
                               "2021" = mapdata$X2021,
                               "2020" = mapdata$X2020,
                               "2019" = mapdata$X2019,
                               "2018" = mapdata$X2018,
                               "2016" = mapdata$X2016,
                               "2017" = mapdata$X2017,
                               "2015" = mapdata$X2015,
                               "2014" = mapdata$X2014,
                               "2013" = mapdata$X2013,
                               "2012" = mapdata$X2012,
                               "2011" = mapdata$X2011,
                               "2010" = mapdata$X2010,
                               "2000" = mapdata$X2000,
                               "1990" = mapdata$X1990,
                               "1980" = mapdata$X1980,
                               "1970" = mapdata$X1970,
                               "1960" = mapdata$X1960)
      mapdata$id <- seq_along(mapdata$long) # create unique id for each region
      
      # dsiplay the heatmap
      map1 <- ggplot(mapdata, aes(x=long, y = lat, group=group, id=id, text=paste("Country: ", mapdata$region, "<br>Refugee Count: ", mapdata$Refugee_Count))) +
        geom_polygon(aes(fill = Refugee_Count), color = "black") +
        scale_fill_gradient(name = "Refugee Count", low ="blue", high = "red", na.value = "grey50")+
        theme(axis.text.x = element_blank(),
              axis.text.y = element_blank(),
              axis.ticks = element_blank(),
              axis.title.x = element_blank(),
              axis.title.y = element_blank(),
              rect = element_blank())
      
      ggplotly(map1, tooltip = "text", height = 1000, width = 1600)
  })
  
  
  # Render line graph for Annual Change
  output$refugees_plot <- renderPlot({
    x <- seq_along(mul_country$us_AnnualChange)
    
    #change the format to date month year
    mul_country$date <- dmy(mul_country$date)
    
    # Extract the year from the date column
    mul_country$year <- year(mul_country$date)
    
    # Change the date format to 19th century if the year is greater than 2022
    mul_country$year[mul_country$year > 2022] <- mul_country$year[mul_country$year > 2022] - 100
    
    # IF all is selected then display all countries annual change
    if (input$country_select == "All") {
      ggplot(mul_country) +
        geom_line(aes(x = year, y = us_AnnualChange, color = "United States")) +
        geom_line(aes(x = year, y = Ge_AnnualChange, color = "Germany")) +
        geom_line(aes(x = year, y = Fr_AnnualChange, color = "France")) +
        geom_line(aes(x = year, y = Canada_AnnualChange, color = "Canada")) +
        labs(x = "Year", y = "Annual Change", color = "Country") +
        theme_minimal() +
        scale_color_manual(values = c("United States" = "blue", "Germany" = "green", "France" = "red", "Canada" = "purple"))
    } else {
      # Only display the specific country
      selected_country <- switch(input$country_select,
                                 "France" = mul_country$Fr_AnnualChange,
                                 "United States" = mul_country$us_AnnualChange,
                                 "Germany" = mul_country$Ge_AnnualChange,
                                 "Canada" = mul_country$Canada_AnnualChange)
      
      ggplot() +
        geom_line(aes(x = x, y = selected_country, color = input$country_select)) +
        labs(x = "Index", y = "Annual Change", color = "Country") +
        theme_minimal() +
        scale_color_manual(values = c("France" = "red", "United States" = "blue", "Germany" = "green", "Canada" = "purple"))
    }
  })
  
  
  # Render The info according to the country and let user select country
  output$country_info <- renderText({
    selected_info <- switch(input$country_select,
                            "All" = "This graph display the anuuan Change for all four of the countries. We can observe that Germany has the hieghest Annual Change of all the countries and that was in the year 1985. The lowest annual change is observed by Canada and that was in 1963. Other than that the individual Annual Changes will be displayed if teh user selects the country that he wants to view.",
                            "France" = "France has the minimal changes in the Annual Change from 1960 to 2022. With the highest Annual Change in the year 1982 and lowest in the year 1964.",
                            "United States" = "United States has the most variations according to Annual Changes from 1960 to 2022. It has the highest Annual Change in the year 2006 and the lowest in the year 2008. Now for the latest year 2022 the Annual Change is now 0 as they are not accepting or removing any refugges.",
                            "Germany" = "Germany has the highest and the lowest Annual Change of all the countries. Though the variations is quite similar to the variations of USA but Germany has higher value in variuations. Forexample the highest Annual Change was recorded in 1985 and the lowest was recorded in 2003 then again in 2006 the variations completely changed to positive 110% and for the lastest year 2022 it is close to 0 as for corona there has been limited number of travels to and from the country.",
                            "Canada" = "Canada has mostly positive Annual Changes. The lowest annual change was in the year 1962 which was -70% from the year before. After the eyar 1975 Canada has consecutive positive changes with the highest mark on year 1989 which was more than 80%. After that year Canada had very little variationswith only less than -20% changes annually. For the present year thje annual change is increasing as Canada is one of the countries that is accepting refugees from all arround the world.")
    selected_info
  })
  
  #render the heatmap info and let user select year
  output$country_year_info <- renderText({
    paste("Selected Year for Heatmap: ", input$year_select)
    paste("The Heat Map displays which countries had refugees flying out of the country according to the year. If the user hovers over the shaded region it will display the exact Country and the Number of refugees that flew out that year. Forexample the most refugees that flew out in a single year is from Afghanistan in the year 1990. A total of 6339095 refugees flew out. The user needs to select the year in the box to display the output.")
  })
  
}

# Run the app
shinyApp(ui = ui, server = server)