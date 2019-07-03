library(dash)
library(dashHtmlComponents)
library(dashCanvas)
library(dashTable)
library(jsonlite)
library(magrittr)
library(compiler)


filename <- 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg'
canvas_width <- 300 
columns <- c("type", "width", "height", "scaleX", "strokeWidth", "path")

app <- Dash$new()

app$layout(htmlDiv(list(

  htmlH6('Draw on image and press Save to show annotations geometry')
  ,
  htmlDiv(list(

    dashCanvas(id='annot-canvas', lineWidth=5, filename=filename, width=canvas_width)

  )),
  dashDataTable(id='annot-canvas-table',
                style_cell = list(textAlign='left'),
                columns = lapply(columns, function(col){return(list(name=col, id=col))})
                )
 
)))

app$callback(
  output = list(id='annot-canvas-table', property='data'),
  params = list(input(id='annot-canvas',property='json_data')),
  function(json)
  {
    if(is.null(json)||is.na(json)){return(list(0,0,0,0,0,0))} else{
    data = fromJSON(json)
    return(data[['objects']][-1])
    }
  }
)

#app$run_server()
  

