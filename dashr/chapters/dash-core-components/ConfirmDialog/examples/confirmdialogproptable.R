test =utils$props_to_list('dccConfirmDialog')
x <- data.table::rbindlist(test, fill = TRUE)

app = Dash$new()

layout = app$layout(
 utils$generate_table(x)
  
)

app$run_server()