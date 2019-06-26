source('dashr/utils.R', local=utils)
test =utils$props_to_list('dccDatePickerRange')
x <- data.table::rbindlist(test, fill = TRUE)

app = Dash$new()

layout = app$layout(
  utils$generate_table(x)
  
)

app$run_server()