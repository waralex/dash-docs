library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(html.Div(list(
  htmlButton('Button 1', id='btn-1', n_clicks=0, children='Submit'),
  htmlButton('Button 2', id='btn-2', n_clicks=0, children='Submit'),
  htmlButton('Button 3', id='btn-3', n_clicks=0, children='Submit'),
  htmlDiv(id='container')
  
)))

app$callback(output('container', 'children'),
             list(input('btn-1', 'n_clicks'),
                  input('btn-2', 'value'),
                  input('btn-3', 'value')),
    function(n_clicks, input1, input2) {
    return(htmlDiv(list(
      htmlTable(list(
        htmlTr(list(htmlTh('Button 1'),
                 htmlTh('Button 2'),
                 htmlTh('Button 3'),
                 htmlTh('Most Recent Click'))),
        htmlTr(list(htmlTd(btn1),
                 htmlTd(btn2),
                 htmlTd(btn3),
                 htmlTd(button_id)))
        ))
      )))
    })
#app$run_heroku()
