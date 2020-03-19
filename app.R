library(dash)

metas <- list(
  list(name = 'description', 
       content = 'Dash User Guide and Documentation. Dash is a framework for building analytical web apps in Python and R.')
)

app <- Dash$new(assets_folder="dash_docs/assets", meta_tags = metas)

app$title("Dash for R User Guide and Documentation | R & RStats | Plotly")
