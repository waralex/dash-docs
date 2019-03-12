library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

all_options = list(
  'America' = list('New York City', 'San Francisco', 'Cincinnati'),
  'Canada' = list('Montréal', 'Toronto', 'Ottawa')
)
# [{'label': k, 'value': k} for k in all_options.keys()],
app$layout_set(htmlDiv(list(
      dccRadioItems(
        id = 'countries-dropdown',
        options = list(list(label = 'America', value = 'America'),
                       list(label = 'Canada', value = 'Canada')),
        value = 'America'
      ),
      htmlHr(),

      dccRadioItems(id='cities-dropdown'),

      htmlHr(),

      htmlDiv(id='display-selected-values')
    )
  )
)

app$callback(
  output=list(id='cities-dropdown', property='options'),
  params=list(input(id='countries-dropdown', property='value')),
  function(selected_country){
    data_selected <- all_options[selected_country]
    list_options <- list()
    for (i in 1:length(data_selected[[1]])){
      print(data_selected[[1]][i])
      list_options[[i]] <- list('label' = data_selected[[1]][i], 'value' = data_selected[[1]][i])
    }
    return(list_options)
})

app$callback(
  output=list(id='cities-dropdown', property='value'),
  params=list(input(id='cities-dropdown', property='options')),
  function(available_options) {
  return(available_options[1]['value'])
})

app$callback(
  output=list(id='display-selected-values', property='children'),
  params=list(input(id='countries-dropdown', property='value'),
              input(id='cities-dropdown', property='value')),
  function(selected_country, selected_city) {
    sprintf("\"%s\ is a city in \"%s\"", selected_city, selected_country)
})

#app$run_heroku()
