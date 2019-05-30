library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

df <- read.csv(url("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"))

continents <- unique(df$continent)
years <- unique(df$year)

# dccSlider starts from 0;
app$layout(
  htmlDiv(
    list(
      dccGraph(id = 'graph-with-slider'),
      dccSlider(
        id = 'year-slider',
        min = 0,
        max = length(years) - 1,
        marks = years,
        value = 0
      )
    )
  )
)



app$callback(
  output = list(id='graph-with-slider', property='figure'),
  params = list(input(id='year-slider', property='value')),
  
  function(indice_selected_year) {
    
    which_year_is_selected <- which(df$year == years[indice_selected_year + 1])
    
    traces <- lapply(continents,
                     function(cont) {
                       
                       which_continent_is_selected <- which(df$continent == cont)
                       
                       df_sub <- df[intersect(which_year_is_selected, which_continent_is_selected), ]
                       
                       with(
                         df_sub, 
                         list(
                           x = gdpPercap,
                           y = lifeExp,
                           opacity=0.5,
                           text = country,
                           mode = 'markers',
                           marker = list(
                             size = 15,
                             line = list(width = 0.5, color = 'white')
                           ),
                           name = cont
                         )
                       )
                     }
    )
    
    list(
      data = traces,
      layout= list(
        xaxis = list(type = 'log', title = 'GDP Per Capita'),
        yaxis = list(title = 'Life Expectancy', range = c(20,90)),
        margin = list(l = 40, b = 40, t = 10, r = 10),
        legend = list(x = 0, y = 1),
        hovermode = 'closest'
      )
    )
  }
)

app$run_server()
