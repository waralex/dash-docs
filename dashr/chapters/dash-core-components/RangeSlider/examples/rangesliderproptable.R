
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)


test =utils$props_to_list('dccRangeSlider')
x <- data.table::rbindlist(test, fill = TRUE)

app = Dash$new()

layout = app$layout(
  generate_table(x)
  
)

app$run_server()
