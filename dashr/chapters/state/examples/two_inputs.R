library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout_set(htmlDiv(list(
    coreInput(id='input-1', type='text', value='Montréal'),
    coreInput(id='input-2', type='text', value='Canada'),
    htmlDiv(id='output')
)))


app$callback(output('output', 'children'),
            list(input('input-1', 'value'),
                 input('input-2', 'value')),
            function(input1, input2) {
  sprintf('Input 1 is "%s" and Input 2 is "%s"')
})

app$run_server()
