test =utils$props_to_list('dccChecklist')
x <- data.table::rbindlist(test, fill = TRUE)

app = Dash$new()

layout = app$layout(
  generate_table(x)
  
)

app$run_server()