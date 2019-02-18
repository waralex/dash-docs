library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout_set(
  htmlDiv(list(
    htmlH1('Hello Dash'),
    coreGraph(figure=list(
      data=list(
        list(
          x=list(1, 2, 3),
          y=list(3, 1, 5),
          type='bar'
        ),
        list(
          x=list(1, 2, 3),
          y=list(3, 9, 3),
          type='bar'
        )
      ),
      layout=list(title='Dash Data Visualization')
    ))
  ))
)

app$run_server()
