library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  simple.callbacks=utils$LoadExampleCode('dashR/chapters/callbacks/examples/simple-callback.R')
)

layout <- htmlDiv(list(
  coreMarkdown("
# Basic Dash Callbacks
In the previous chapter on the [app.layout](/getting-started) we learned that the
app$layout describes what the app looks like and is a
hierarchical tree of components.
The dash_html_components library provides classes for
all of the HTML tags, and the keyword arguments describe
the HTML attributes like style, className, and id.
The dash_core_components library generates higher-level components
like controls and graphs.

This chapter describes how to make your Dash apps
interactive.

Let's get started with a simple example.
  "),
  examples$simple.callbacks$source_code,
  examples$simple.callbacks$layout
))
