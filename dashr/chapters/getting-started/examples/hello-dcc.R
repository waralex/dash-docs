library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

myList = list()

app$layout_set(htmlDiv(list(
  htmlLabel('Dropdown'),
  dccDropdown(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = 'MTL'
  ),
  htmlBr(),

  htmlLabel('Multi-Select Dropdown'),
  dccDropdown(
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
  dccRadioItems(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = 'MTL'
  ),
  htmlBr(),

  htmlLabel('Checkboxes'),
  dccChecklist(
    options = list(list(label = "New York City", value = "NYC"),
                   list(label = "Montréal", value = "MTL"),
                   list(label = "San Francisco", value = "SF")),
    value = list('MTL', 'SF')
  ),
  htmlBr(),

  htmlLabel('Text Input'),
  dccInput(value='MTL', type='text'),
  htmlBr(),

  htmlLabel('Slider'),
  dccSlider(
    min = 0,
    max = 9,
    marks = c("", "Label 1", 2:5),
    value = 5
  )

  ), style = list('columnCount' = 2)))


#app$run_heroku()
