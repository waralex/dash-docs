library(dashR)
library(dashTable)

df <- read.csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app <- Dash$new()

app$layout(
  dashDataTable(
    id = "table",
    columns = lapply(colnames(df), 
                     function(colName){
                       list(
                         id = colName,
                         name = colName
                       )
                     }),
    data = dashTable::df_to_list(df)
  )
)

app$run_server()