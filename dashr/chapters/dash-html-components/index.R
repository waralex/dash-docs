library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1('Dash HTML Components'),
  dccMarkdown("
Dash is a web application framework that provides pure R abstraction around HTML, CSS, and JavaScript.
Instead of writing HTML or using an HTML templating engine, you compose your layout using R structures with the `dashHtmlComponents` library.
The source for this library is on GitHub: [plotly/dash-html-components](https://github.com/plotly/dash-html-components).
Here is an example of a simple HTML structure:
  "),

  htmlHr(),
  dccMarkdown("
[Back to the Table of Contents](/)
  ")
  ))
