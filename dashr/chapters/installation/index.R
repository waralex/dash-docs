library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

layout <- htmlDiv(list(
  htmlH1('Installation Instructions'),
  dccMarkdown("
    library(devtools)
    install_github('plotly/dashR')
    install_github('plotly/dash-html-components')
    install_github('plotly/dash-dcc-components'
  ")
))
