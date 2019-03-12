library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  hello.world=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-world.R'),
  hello.dash2=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-dash-components.R'),
  hello.table=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-table.R'),
  hello.bubble=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-bubble.R'),
  hello.markdown=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-markdown.R'),
  hello.dcc=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-dcc.R'),
  dropdown.doc=utils$LoadExampleCode('dashr/chapters/getting-started/examples/markdown-doc-dropdown.R')
)

layout <- htmlDiv(list(
  dccMarkdown("
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

  dccMarkdown("
    Run the app with

   ```
   $ Rscript index.R
   Fire started at 127.0.0.1:8080
   start: 127.0.0.1:8080
   ```
  "),
  # hello markdown example
  dccMarkdown("
    and visit [https://dashr-docs.herokuapp.com/](https://dashr-docs.herokuapp.com/)
    in your web browser. You should see an app that looks like this.
  "),
  examples$hello.world$layout,

  # hello layout example
  examples$hello.dash2$source_code,
  examples$hello.dash2$layout,

  # hello table example
  examples$hello.table$source_code,
  examples$hello.table$layout,

  # hello scater example
  examples$hello.bubble$source_code,
  examples$hello.bubble$layout,

  # hello dmarkdown example
  examples$hello.markdown$source_code,
  examples$hello.markdown$layout,

  # hello dcc example
  examples$hello.dcc$source_code,
  examples$hello.dcc$layout,

  # dropdown help with example
  # examples$dropdown.doc$source_code,
  examples$dropdown.doc$layout,

  dccMarkdown("
  #Summary
  The layout of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. The dash_html_components library provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, className, and id. The dash_dcc_components library generates higher-level components like controls and graphs.
  For reference, see:
  - [dash_core_components gallery](https://dash.plot.ly/dash-core-components)
  - [dash_html_components gallery](https://dash.plot.ly/dash-html-components)


  The next part of the Dash tutorial covers how to make these apps interactive.

  Dash Tutorial Part 3: Basic Callbacks
  [Back to the Table of Contents](/getting-started-part-2)
  ")
))
