library(dashCoreComponents)
library(dashHtmlComponents)

layout <- htmlDiv(list(
  htmlH1('Installation Instructions'),
  coreMarkdown("
    library(devtools)
    install_github('plotly/dashR@0.0.2-issue11984')
    install_github('plotly/dash-html-components')
    install_github('plotly/dash-core-components'
  ")
))
