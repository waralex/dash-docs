library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout_set(
  htmlDiv(list(
    htmlH1('Hello Dash'),
    htmlDiv(children="Dash: A web application framework for R."),
    coreGraph(figure=list(
      data=list(
        list(
          x=list(1, 2, 3),
          y=list(3, 1, 5),
          type='bar',
          name='SF'
        ),
        list(
          x=list(1, 2, 3),
          y=list(3, 9, 3),
          type='bar',
          name='Montréal'
        )
      ),
      layout=list(title='Dash Data Visualization')
    ))
  ))
)

app$run_server()
