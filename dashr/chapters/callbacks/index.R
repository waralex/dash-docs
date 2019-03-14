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
  dccMarkdown("
# Basic Dash Callbacks
> This is the *3rd* chapter of the [Dash Tutorial](/).
> The [previous chapter](/getting-started) covered the Dash app `layout_set`
> and the [next chapter](/state) covers an additional concept of callbacks
> known as `state`.
> Just getting started? Make sure to [install the necessary dependencies](/installation).
  "),
  
  dccMarkdown("
In the [previous chapter on the `app.layout`](/getting-started) we learned
that the `app$layout_set()` describes what the app looks like and is
a hierarchical tree of components.
The `dash_html_components` library provides classes for all of the HTML
tags, and the keyword arguments describe the HTML attributes like `style`,
`className`, and `id`. The `dash_core_components` library
generates higher-level components like controls and graphs.

This chapter describes how to make your
Dash apps interactive.

Let's get started with a simple example.
  "),
  
  htmlH4("
    Dash App Layout
    ", id='dash-app-layout'),
  
  # Example of basic callbacks
  dccSyntaxHighlighter(
    examples$simple.callbacks$source_code,
    language='r',
    customStyle=styles.code_container
  ),
  
  html.Div(examples$simple.callbacks$layout,
           className="example-container"),
  dccMarkdown("
Try typing in the text box. The children of the output component updates
right away. Let's break down what's happening here:
1. The \"inputs\" and \"outputs\" of our application interface are described
declaratively through the `app.callback` decorator.
2. In Dash, the inputs and outputs of our application are simply the
properties of a particular component. In this example,
our input is the \"`value`\" property of the component that has the ID
\"`my-id`\". Our output is the \"`children`\" property of the
component with the ID \"`my-div`\".
3. Whenever an input property changes, the function that the
callback decorator wraps will get called automatically.
Dash provides the function with the new value of the input property as
an input argument and Dash updates the property of the output component
with whatever was returned by the function.
4. The `component_id` and `component_property` keywords are optional
(there are only two arguments for each of those objects).
I have included them here for clarity but I will omit them from here on
out for brevity and readability.
5. Don't confuse the `dash.dependencies.Input` object from the
`dash_core_components.Input` object. The former is just used in these
callbacks and the latter is an actual component.
6. Notice how we don't set a value for the `children` property of the
`my-div` component in the `layout`. When the Dash app starts, it
automatically calls all of the callbacks with the initial values of the
input components in order to populate the initial state of the output
components. In this example, if you specified something like
`html.Div(id='my-div', children='Hello world')`, it would get overwritten
when the app starts.

It's sort of like programming with Microsoft Excel:
whenever an input cell changes, all of the cells that depend on that cell
will get updated automatically. This is called \"Reactive Programming\".

Remember how every component was described entirely through its set of
keyword arguments? Those properties are important now.
With Dash interactivity, we can dynamically update any of those properties
through a callback function. Frequently we'll update the `children` of a
component to display new text or the `figure` of a `dccGraph` component
to display new data, but we could also update the `style` of a component or
even the available `options` of a `dccDropdown` component!

***

Let's take a look at another example where a `dccSlider` updates a
`dccGraph`.
  "),
  examples$simple.callbacks$source_code,
  examples$simple.callbacks$layout,

  dccMarkdown("
Try typing in the text box. The children of the output component updates
right away. Let's break down what's happening here:
1. The \"inputs\" and \"outputs\" of our application interface are described
declaratively through the `app.callback` decorator.
2. In Dash, the inputs and outputs of our application are simply the
properties of a particular component. In this example,
our input is the \"`value`\" property of the component that has the ID
\"`my-id`\". Our output is the \"`children`\" property of the
component with the ID \"`my-div`\".
3. Whenever an input property changes, the function that the
callback decorator wraps will get called automatically.
Dash provides the function with the new value of the input property as
an input argument and Dash updates the property of the output component
with whatever was returned by the function.
4. The `component_id` and `component_property` keywords are optional
(there are only two arguments for each of those objects).
I have included them here for clarity but I will omit them from here on
out for brevity and readability.
5. Don't confuse the `dash.dependencies.Input` object from the
`dash_core_components.Input` object. The former is just used in these
callbacks and the latter is an actual component.
6. Notice how we don't set a value for the `children` property of the
`my-div` component in the `layout`. When the Dash app starts, it
automatically calls all of the callbacks with the initial values of the
input components in order to populate the initial state of the output
components. In this example, if you specified something like
`html.Div(id='my-div', children='Hello world')`, it would get overwritten
when the app starts.

It's sort of like programming with Microsoft Excel:
whenever an input cell changes, all of the cells that depend on that cell
will get updated automatically. This is called \"Reactive Programming\".

Remember how every component was described entirely through its set of
keyword arguments? Those properties are important now.
With Dash interactivity, we can dynamically update any of those properties
through a callback function. Frequently we'll update the `children` of a
component to display new text or the `figure` of a `dccGraph` component
to display new data, but we could also update the `style` of a component or
even the available `options` of a `dccDropdown` component!

***

Let's take a look at another example where a `dccSlider` updates a
`dccGraph`.
"),
  
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
