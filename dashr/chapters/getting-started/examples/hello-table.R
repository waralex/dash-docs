library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

df <- read.csv('dashr/chapters/getting-started/examples/usa-agricultural-exports-2011.csv', header = TRUE, sep = ",", row.names = 1)

generate_table <- function(df, nrows=10) 
{
  n <- min(nrows, nrow(df))
  rows <- lapply(seq(1, n), function(i) {
    htmlTr(children = lapply(as.character(df[i,]), htmlTd))
  })
  
  header <- htmlTr(children = lapply(names(df), htmlTh))
  
  htmlTable(
    children = c(list(header), rows)
  )
  
}

app <- Dash$new()

app$layout_set(htmlDiv(list(
  htmlH4(children='US Agriculture Exports (2011)'),
  generate_table(df)
)))

#app$run_heroku()
