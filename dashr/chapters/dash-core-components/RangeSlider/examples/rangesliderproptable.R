
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

test =utils$props_to_list('dccRangeSlider')
rangesliderproptable <- data.table::rbindlist(rangesliderproptable, fill = TRUE)

app = Dash$new()

layout = app$layout(
  generate_table(x)
  
)

app$run_server()
