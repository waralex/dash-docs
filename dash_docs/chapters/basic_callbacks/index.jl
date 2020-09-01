using Dash
using DashHtmlComponents
using DashCoreComponents

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])


app.layout = html_div() do
    html_h1("Basic Dash Callbacks"),
    html_blockquote(dcc_markdown("This is the 3rd chapter of the [Dash Tutorial](/).
    The previous chapter covered the Dash app [layout](/getting-started) and the [next chapter](/state) covers an additional concept of callbacks
    known as `state`.")),
    dcc_markdown("""
    In the [previous chapter](/getting-started) on the app `layout` we learned that the
    `app.layout` describes what the app looks like and is a hierarchical tree of components.
    The `DashHtmlComponents` package provides classes for all of the HTML tags, and the keyword
    arguments describe the HTML attributes like `style`, `className`, and `id`. The `DashCoreComponents`
    package generates higher level components like controls and graphs.

    This chapter describes how to make your Dash apps interactive.

    Let's get started with a simple example.
    """),
    dcc_markdown("""
    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents

    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    app.layout = html_div() do
        dcc_input(id="input", value="initial value", type = "text"),
        html_div(id="output")
    end

    callback!(app, Output("output", "children"), Input("input", "value")) do input_value
        "You've entered \$(input_value)"
    end

    run_server(app, "0.0.0.0", 8000)
    ```
    Try typing in the text box. The `children` property of the output
    component updates right away. Let's break down what's happening here.

    1. The "inputs" and "outputs" of our application interface are described
    declaratively by the `callback!` function definition.

    2. In Dash, the inputs and outputs of our application are simply the
    properties of a particular component. In this example, our input is the `value`
    property of of the component with the ID `input`. Our output is the `children` property
    of the compnoent with the ID `output`.

    3. Whenever an input property changes, the callback will be executed automatically.
    Dash provides the function with the new value of the input property as an input argument
    and Dash updates the property of the output component with whatever was returned by the callback
    function.

    4. Don't confuse the `Dash::Input` object with the `DashCoreComponents::Input` object. The former is just used in
    callbacks while the latter is an actual component.

    5. Notice how we don't set a value for the `children` property of the `input` component in the `layout`. When
    the Dash app starts, it automatically calls all the callbacks with the initial values of the input componets in
    order to populate the initial state of the output components. In this example, if you specified something like
    `html_div(id="output", children="hello world")`, it would get overwritten when the app starts.

    It's sort of like programming with Microsoft Excel: whenever an input cell changes, all of the cells that
    depend on that cell will get updated automatically. This is called "Reactive Programming".

    Remember how every component was described entirely through its set of keyword arguments? Those properties are important now.
    With Dash's interactivity, we can dynamically update any of those properties through a callback function.
    Frequently we'll update the `children` of a component to display new text or the `figure` of a `dcc_graph` component to
    display new data, but we could also update the `style` of a component or even the available `options` of a `dcc_dropdown`
    component!
    """),
    html_hr(),
    dcc_markdown("""
    Let's take a look at another example where a `dcc_slider` updates a `dcc_graph`.
    """),
    html_h1(""),
    dcc_markdown("""
    """),
    html_h1(""),
    dcc_markdown("""
    """),
    html_h1(""),
    dcc_markdown("""
    """)

end

run_server(app, "0.0.0.0", 8000)
