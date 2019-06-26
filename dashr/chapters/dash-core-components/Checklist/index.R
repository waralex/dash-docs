library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  checklistproptable = utils$LoadExampleCode('dashr/chapters/dash-core-components/Checklist/examples/checklistproptable.R')
)

layout = htmlDiv(list(
  htmlH3('Checklist Properties'),
<<<<<<< HEAD
  examples$checklistproptable$layout,
  
  dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
=======
  examples$checklistproptable$layout
))
>>>>>>> b55713055cca0685792ba311911ec9a3d89482d8
