library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  hello.world=utils$LoadExampleCode('dashR/chapters/getting-started/examples/hello-world.R', app=app),
  hello.dash2=utils$LoadExampleCode('dashR/chapters/getting-started/examples/hello-dash-components.R', app=app)
)

#link <- coreLocation(pathname='/getting-started')

layout <- htmlDiv(list(
  coreMarkdown("
# Dash Layout
> This is the 2nd chapter of the
> [Dash Tutorial](/).
> The [previous chapter](/installation)
> covered installation
> and the next chapter covers Dash callbacks.

DashR is an R interface for Plotly's Dash.

It has feature parity with Dash for Python and its
interface is designed to feel similar across the
two languages. Dash for Python and DashR share
the same front-end code, meaning that the same
component libraries are available in both communities.

DashR is a package for creating analytic, data intensive
web applications - no javascript required.

Built on top of React.js, DashR is packaged with a set of
interactive web based components like graphs, data tables,
dropdowns, sliders, and more.

## Hello World
  "),
  examples$hello.world$source_code,

  coreMarkdown("
    Run the app with

   ```
   $ Rscript index.R
   Fire started at 127.0.0.1:8080
   start: 127.0.0.1:8080
   ```
  "),

  coreMarkdown("
    and visit [http://127.0.0.1:8080](http://127.0.0.1:8080)
    in your web browser. You should see an app that looks like this.
  "),

  examples$hello.world$layout,

  examples$hello.dash2$source_code,
  examples$hello.dash2$layout
))
