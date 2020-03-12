library(dash)

metas <- list(
  list(name = 'description', 
       content = 'Dash User Guide and Documentation. Dash is a framework for building analytical web apps in Python and R.')
)

app <- Dash$new(meta_tags = metas)

app$title("Dash User Guide and Documentation - Dash by Plotly")
