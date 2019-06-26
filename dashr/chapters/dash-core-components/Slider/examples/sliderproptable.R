<<<<<<< HEAD
=======
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)


>>>>>>> b55713055cca0685792ba311911ec9a3d89482d8
test =utils$props_to_list('dccSlider')
x <- data.table::rbindlist(test, fill = TRUE)

app = Dash$new()

layout = app$layout(
  generate_table(x)
  
)

app$run_server()
