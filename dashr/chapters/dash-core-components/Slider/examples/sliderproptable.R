library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

test =utils$props_to_list('dccSlider')
sliderproptable <- data.table::rbindlist(sliderproptable, fill = TRUE)

app = Dash$new()

layout = app$layout(
  generate_table(x)
  
)

app$run_server()
