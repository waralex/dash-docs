library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout_set(htmlDiv(list(
  coreInput(id='input-1-state', type='text', value='Montréal'),
  coreInput(id='input-2-state', type='text', value='Canada'),
  htmlButton(id='submit-button', n_clicks=0, children='Submit'),
  htmlDiv(id='output-state')
)))


app$callback(output('output-state', 'children'),
             list(input('submit-button', 'n_clicks'),
                  input('input-1-state', 'value'),
                  input('input-2-state', 'value')),
             function(n_clicks, input1, input2) {
               sprintf("The Button has been pressed \"%s\" times, Input 1 is \"%s\", and Input 2 is \"%s\"", n_clicks, input1, input2)
             })

#app$run_heroku()
