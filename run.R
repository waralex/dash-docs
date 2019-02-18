library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

dash_css <- htmltools::htmlDependency(
  name = "dash-css",
  version = "1.0.0",
  src = c(href = "https://codepen.io/chriddyp/pen"),
  stylesheet = "bWLwgP.css"
)

app$dependencies_set(dash_css)

app$layout_set(
  htmlDiv(list(
    coreLocation(list(id='url', refresh=FALSE)),
    coreLink('Navigate to "/"', href='/'),
    htmlBr(),
    coreLink('Navigate to "/page-2"', href='/page-2'),
    htmlDiv(id='page-content')
  )
  )
)

app$callback(output=list(id='page-content', property='children'),
             params=list(input('url', 'pathname')),
             func = function(pathname)
             {
               htmlDiv(list(htmlH3(sprintf('You are on page %s', pathname))))
             }
)

app$run_server()
