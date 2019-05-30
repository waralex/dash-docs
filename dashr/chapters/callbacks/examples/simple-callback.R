library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(
  htmlDiv(
    list(
      dccInput(id='my-id-input', value='initial value', type='text'),
      htmlDiv(id='my-id-div')
    )
  )
)

app$callback(
  output=list(id='my-id-div', property='children'),
  params=list(input(id='my-id-input', property='value')),
  function(input_value) {
    sprintf("You've entered \"%s\"", input_value)
  })

app$run_server()
