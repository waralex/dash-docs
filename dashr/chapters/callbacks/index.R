library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  simple.callbacks=utils$LoadExampleCode('dashr/chapters/callbacks/examples/simple-callback.R'),
  simple.slider=utils$LoadExampleCode('dashr/chapters/callbacks/examples/hello-slider.R'),
  multi.inputs=utils$LoadExampleCode('dashr/chapters/callbacks/examples/multi-inputs.R'),
  multi.output=utils$LoadExampleCode('dashr/chapters/callbacks/examples/multi-output.R'),
  multi.output2=utils$LoadExampleCode('dashr/chapters/callbacks/examples/multi-output-v2.R')
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
  # Example of basic callbacks
  examples$simple.callbacks$source_code,
  examples$simple.callbacks$layout,
  
  # Example of slicer
  examples$simple.slider$source_code,
  examples$simple.slider$layout,
  
  # Example of mutli-inputs
  examples$multi.inputs$source_code,
  examples$multi.inputs$layout,
  
  # Example of mutli-output
  examples$multi.output$source_code,
  examples$multi.output$layout,
  
  # Example of mutli-output
  examples$multi.output2$source_code,
  examples$multi.output2$layout
))

