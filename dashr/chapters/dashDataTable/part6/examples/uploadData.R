library(dash)
library(dashHtmlComponents)
library(dashCoreComponents)
library(dashTable)

external_stylesheets <- list('https://codepen.io/chriddyp/pen/bWLwgP.css')

app <- Dash$new(external_stylesheets = external_stylesheets)

app$layout(
  htmlDiv(
    list(
      dccUpload(
        id = 'datatable-upload',
        children = htmlDiv(
          list(
            'Drag and Drop or ',
            htmlA('Select Files')
          )
        ),
        style = list(
          width = '100%', 
          height = '60px', 
          lineHeight = '60px',
          borderWidth = '1px', 
          borderStyle = 'dashed',
          borderRadius = '5px', 
          textAlign = 'center', 
          margin = '10px'
        )
      ),
      dashDataTable(id = 'datatable-upload-container'),
      dccGraph(id = 'datatable-upload-graph')
    )
  )
)

app$callback(
  output = list(id = 'datatable-upload-container', property = 'data'),
  params = list(input(id = 'datatable-upload', property = 'contents'),
                input(id = 'datatable-upload', property = 'filename')),
  function(contents, filename) {
    # TODO: base64 decode
  }
)

app$run_server()