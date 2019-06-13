library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  checklistproptable = utils$LoadExampleCode('dashr/chapters/dash-core-components/Checklist/examples/checklistproptable.R')
)

layout = htmlDiv(list(
  htmlH3('Checklist Properties'),
  examples$checklistproptable$layout
))