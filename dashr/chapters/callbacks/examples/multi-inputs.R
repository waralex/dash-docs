library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

df <- read.csv('dashr/chapters/callbacks/examples/indicators.csv', header = TRUE, sep = ",")
available_indicators <- unique(df$Indicator_Name)
option_indicator <- list()
for (i in 1:length(available_indicators)){
  option_indicator[[i]] <- list(label = available_indicators[i], value = available_indicators[i])
}


app$layout_set(
  htmlDiv(list(
    htmlDiv(list(
      htmlDiv(list(
        dccDropdown(
          id = 'xaxis-column',
          options = option_indicator,
          value = 'Fertility rate, total (births per woman)'
        ),
        dccRadioItems(
          id = 'xaxis-type',
          options = list(list(label = 'Linear', value = 'linear'),
                         list(label = 'Log', value = 'log')),
          value = 'linear',
          labelStyle = list(display = 'inline-block')
        )
      ), style = list(width = '48%', display = 'inline-block')),

      htmlDiv(list(
        dccDropdown(
          id = 'yaxis-column',
          options = option_indicator,
          value = 'Life expectancy at birth, total (years)'
        ),
        dccRadioItems(
          id = 'yaxis-type',
          options = list(list(label = 'Linear', value = 'linear'),
                         list(label = 'Log', value = 'log')),
          value = 'linear',
          labelStyle = list(display = 'inline-block')
        )
      ), style = list(width = '48%', flaot = 'display', display = 'inline-block'))
    )),
    dccGraph(id = 'indicator-graphic'),
    dccSlider(
      id = 'year--slider',
      min = 1,
      max = length(unique(df$Year)),
      marks = unique(df$Year),
      value = length(unique(df$Year))
    )
  ))
)


app$callback(
  output = list(id='indicator-graphic', property='figure'),
  params = list(input(id='xaxis-column', property='value'),
                input(id='yaxis-column', property='value'),
                input(id='xaxis-type', property='value'),
                input(id='yaxis-type', property='value'),
                input(id='year--slider', property='value')),
  function(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value) {
    selected_year <- unique(df$Year)[year_value]
    traces <- list()
    if (selected_year %in% unique(df$Year)){
      filtered_df <- df[df[["Year"]] %in% selected_year, ]
        traces[[1]] <- list(
          x = filtered_df[filtered_df$Indicator_Name %in% xaxis_column_name, "Value", drop = TRUE],
          y = filtered_df[filtered_df$Indicator_Name %in% yaxis_column_name, "Value", drop = TRUE],
          opacity=0.7,
          text = filtered_df[filtered_df$Indicator_Name %in% yaxis_column_name, "Country_Name", drop = TRUE],
          mode = 'markers',
          marker = list(
            'size'= 15,
            'line' = list('width' = 0.5, 'color' = 'white')
          )
        )

      return (list(
        'data' = traces,
        'layout'= list(
          xaxis = list('title' = xaxis_column_name, 'type' = xaxis_type),
          yaxis = list('title' = yaxis_column_name, 'type' = yaxis_type),
          margin = list('l' = 40, 'b' = 40, 't' = 10, 'r' = 10),
          legend = list('x' = 0, 'y' = 1),
          hovermode = 'closest'
        )
      ))
    }
  }
)

#app$run_heroku()
