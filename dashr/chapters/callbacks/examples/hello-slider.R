library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

df <- read.csv('dashr/chapters/callbacks/examples/gapminderDataFiveYear.csv', header = TRUE, sep = ",")
continents <- unique(df$continent)

app$layout_set(htmlDiv(list(
  dccGraph(id = 'graph-with-slider'),
  dccSlider(
    id = 'year-slider',
    min = 1,
    max = length(unique(df$year))-1,
    marks = unique(df$year),
    value = 1
  )
)))


app$callback(
  output = list(id='graph-with-slider', property='figure'),
  params = list(input(id='year-slider', property='value')),
  function(indice_selected_year) {
    selected_year <- unique(df$year)[indice_selected_year]
    if (selected_year %in% unique(df$year)){
      filtered_df <- split(df, as.factor(df$year==selected_year))$`TRUE`
      traces <- list()
      for (i in 1:length(continents)){
        df_by_continent <- split(filtered_df, as.factor(filtered_df$continent==continents[i]))$`TRUE`
        traces[[i]] <- list(
          x = df_by_continent$gdpPercap,
          y = df_by_continent$lifeExp,
          opacity=0.7,
          text = df_by_continent$country,
          mode = 'markers',
          marker = list(
            'size'= 15,
            'line' = list('width' = 0.5, 'color' = 'white')
          ),
          name = continents[i]
        )}

      return (list(
        'data' = traces,
        'layout'= list(
          xaxis = list('type' = 'log', 'title' = 'GDP Per Capita'),
          yaxis = list('title' = 'Life Expectancy', 'range' = c(20,90)),
          margin = list('l' = 40, 'b' = 40, 't' = 10, 'r' = 10),
          legend = list('x' = 0, 'y' = 1),
          hovermode = 'closest'
        )
      ))
    }
  }
)

#app$run_heroku()
