library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

myList = list()

app$layout_set(htmlDiv(list(
  htmlLabel('Dropdown'),
  coreDropdown(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = 'MTL'
  ),
  htmlBr(),
  
  htmlLabel('Multi-Select Dropdown'),
  coreDropdown(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = list('MTL', 'SF'),
    multi=TRUE
  ),
  htmlBr(),
  htmlBr(),
  htmlBr(),
  htmlLabel('Radio Items'),
  coreRadioItems(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = 'MTL'
  ),
  htmlBr(),
  
  htmlLabel('Checkboxes'),
  coreChecklist(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = list('MTL', 'SF')
  ),
  htmlBr(),
  
  htmlLabel('Text Input'),
  coreInput(value='MTL', type='text'),
  htmlBr(),
  
  htmlLabel('Slider'),
  coreSlider(
    min = 0,
    max = 9,
    marks = c("", "Label 1", 2:5),
    value = 5
  )
  
  ), style = list('columnCount' = 2)))


#app$run_heroku()
