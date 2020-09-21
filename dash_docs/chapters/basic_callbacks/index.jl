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
    dcc_markdown("
    In the [previous chapter](/getting-started) on the app `layout` we learned that the
    `app.layout` describes what the app looks like and is a hierarchical tree of components.
    The `DashHtmlComponents` package provides classes for all of the HTML tags, and the keyword
    arguments describe the HTML attributes like `style`, `className`, and `id`. The `DashCoreComponents`
    package generates higher level components like controls and graphs.

    This chapter describes how to make your Dash apps interactive.

    Let's get started with a simple example.
    "),
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
    """),

    dcc_markdown("""
    Try typing in the text box. The `children` property of the output
    component updates right away. Let's break down what's happening here:

    1. The "inputs" and "outputs" of our application interface are described
    declaratively by the `callback!` function definition.

    2. We load our dataframe at the start of the app: `df = CSV.read("...")`. This dataframe `df` is in the global state of the app and can be read inside callback functions.

    3.Loading data into memory can be expensive. By loading data at the start of the app instead of inside callback functions, we ensure that this operation is only done with the app server starts. When a user visits the app or interacts with the app, the data (the `df`) is already in memory. If possible, expensive initialization (like downloading or querying data) should be done in the global scope of the app instead of within callback functions.

    The callback does not modify the original data, it just creates copies of the dataframe by filtering. This is important: *your callbacks should never mutate variables outside of their scope*. If your callbacks modify global state, then one user's session might affect the next user's session and when the app is deployed on a server with multiple processes or threads, those modifications will not be shared across sessions.

    4. We are turning on transitions with `layout.transition` to give an idea of how the dataset evolves with time: transitions allow the chart to update from one state to the next smoothly, as if it were animated.

    4. We are turning on transitions with `layout.transition` to give an idea of how the dataset evolves with time: transitions allow the chart to update from one state to the next smoothly, as if it were animated.

    * The "inputs" and "outputs" of our application interface are described
    declaratively by the `callback!` function definition.

    * In Dash, the inputs and outputs of our application are simply the
    properties of a particular component. In this example, our input is the `value`
    property of of the component with the ID `input`. Our output is the `children` property
    of the compnoent with the ID `output`.

    * Whenever an input property changes, the callback function will be executed automatically.
    Dash provides the callback function with the new value of the input property as an input argument
    and Dash updates the property of the output component with whatever was returned by the callback
    function.

    * Don't confuse the `Dash::Input` object with the `DashCoreComponents::Input` object. The former is just used to declare
    inputs of callback functions while the latter is an UI component which is used to render HTML input elements.

    * Notice how we don't set a value for the `children` property of the `input` component in the `layout`. When
    the Dash app starts, it automatically calls all the callbacks with the initial values of the input componets in
    order to populate the initial state of the output components. In this example, if you specified something like
    `html_div(id=\"output\", children=\"hello world\")`, it would get overwritten when the app starts by what is
    returned by the callback function.

    It's sort of like programming with Microsoft Excel: whenever an input cell changes, all of the cells that
    depend on that cell will get updated automatically. This is called \"Reactive Programming\".

    Remember how every component was described entirely through its set of keyword arguments? Those properties are important now.
    With Dash's interactivity, we can dynamically update any of those properties through a callback function.
    Frequently we'll update the `children` of a component to display new text or the `figure` of a `Graph` component to
    display new data, but we could also update the `style` of a component or even the available `options` of a `Dropdown`
    component!
    """),
    html_hr(),
    dcc_markdown("""
    Let's take a look at another example where a `Slider` updates a `Graph`.

    ## Dash App Layout With Figure and Slider

    ```julia
    using CSV
    using DataFrames
    using Dash
    using DashHtmlComponents
    using DashCoreComponents
    using PlotlyJS

    url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
    download(url, "gapminder-data.csv")
    df = CSV.read("gapminder-data.csv")

    continents = unique(df[:continent])
    years = unique(df[:year])

    app = dash()

    app.layout = html_div() do
        dcc_graph(id="graph"),
        dcc_slider(
            id = "year-slider",
            min = 0,
            max = length(years) - 1,
            marks = years,
            value = 0)
    end

    callback!(
        app,
        Output("graph", "figure"),
        Input("year-slider", "value"),
    ) do index

        single_year_df = filter(row -> row.year == years[index+1], df)

        figure_data = []

        for cont in continents
            single_continent_df = filter(row -> row.continent == cont, single_year_df)
            push!(figure_data,
                (x = single_continent_df[:gdpPercap],
                y = single_continent_df[:lifeExp],
                type = "scatter",
                mode = "markers",
                opacity=0.5,
                name = cont)
            )
        end

        figure = (
            data = figure_data,
            layout = (xaxis = ((type="log"), (title="GDP")),
                    yaxis = ((title="Life Expectancy"), range=(20, 90)),
            ),
        )

        return figure
    end


    run_server(app, "0.0.0.0", 8000)
    ```

    In this example, the `value` property of the `Slider` component is the input of the app and the output of the app is the `figure` property of the `Graph` component. When the `value` of the `Slider` changes, Dash calls the callback function with new value. The function filters the dataframe with this new value, constructs a `figure` object, and returns it to the Dash app.

    There are a few nice patterns in this example:

    1. We're using the `CSV` and `DataFrames` libraries to import and filter datasets in memory.
    2. We load our dataframe at the start of the app: `df = CSV.read("...")`. This dataframe `df` is in the global state of the app and can be read inside callback functions.

    3.Loading data into memory can be expensive. By loading data at the start of the app instead of inside callback functions, we ensure that this operation is only done with the app server starts. When a user visits the app or interacts with the app, the data (the `df`) is already in memory. If possible, expensive initialization (like downloading or querying data) should be done in the global scope of the app instead of within callback functions.

    The callback does not modify the original data, it just creates copies of the dataframe by filtering. This is important: *your callbacks should never mutate variables outside of their scope*. If your callbacks modify global state, then one user's session might affect the next user's session and when the app is deployed on a server with multiple processes or threads, those modifications will not be shared across sessions.

    4. We are turning on transitions with `layout.transition` to give an idea of how the dataset evolves with time: transitions allow the chart to update from one state to the next smoothly, as if it were animated.
    """),
    html_h1("Dash App With Multiple Inputs"),
    dcc_markdown("""
    In Dash, any `Output` can have multiple `Input` components. Here's a simple example that binds five Inputs (the `value` property of 2 `Dropdown` components, 2 `RadioItems` components, and 1 `Slider` component) to 1 Output component (the `figure` property of the `Graph` component).

    ```julia

    ```
    """),
    html_h1("Dash App With Multiple Outputs"),
    dcc_markdown("""
    So far all the callbacks we've written only update a single Output property. We can also
    update several at once: put all the properties you want to update as inputs to the callback,
    and return that many items from the callback. This is particularly nice if two outputs depend
    on the same computationaly intense itermediate result, such as a slow database query.

    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents

    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    app.layout = html_div() do
        dcc_input(id = "input", value = "1", type = "text"),
        html_tr((html_td("x^2"), html_td(id="square"))),
        html_tr((html_td("x^3"), html_td(id="cube"))),
        html_tr((html_td("2^x"), html_td(id="twos"))),
        html_tr((html_td("3^x"), html_td(id="threes"))),
        html_tr((html_td("x^x"), html_td(id="xx")))
    end

    callback!(
        app,
        Output("square", "children"),
        Output("cube", "children"),
        Output("twos", "children"),
        Output("threes", "children"),
        Output("xx", "children"),
        Input("input", "value"),
    ) do x
        x = parse(Int64, x)
        return (x^2, x^3, 2^x, 3^x, x^x)
    end

    run_server(app, "0.0.0.0", 8000)
    ```

    A word of caution: it's not always a good idea to combine Outputs, even if you can:
    - If the Outputs depend on some but not all of the same inputs, keeping them separate
    can avoid unneccessary updates.
    - If they have the same inputs but do independent computations with these same inputs,
    keeping the callbacks separate can allow them to run in parallel.
    """),
    html_h1("Dash App With Chained Callbacks"),
    dcc_markdown("""
    You can also chain outputs and inputs together: the output of one callback function could
    be the input of another callback function.

    This pattern can be used to create dynamic UIs where one input component updates the available
    options of the next input component. Here's a simple example:

    ```julia
    using CSV
    using DataFrames
    using Dash
    using DashHtmlComponents
    using DashCoreComponents
    using RDatasets
    using PlotlyJS

    app = dash()

    all_options = Dict("America"=>["New York City", "San Francisco", "Cincinnati"],
                       "Canada"=>["Montreal", "Toronto", "Ottawa"]
    )

    app.layout = html_div() do
        html_div(
            children = [
                dcc_radioitems(
                    id = "countries-radio",
                    options = [(label = i, value = i) for i in keys(all_options)],
                    value="America"
                ),
                html_hr(),
                dcc_radioitems(id="cities-radio"),
                html_hr(),
                html_div(id="display-selected-values")

            ]
        )
    end

    callback!(
        app,
        Output("cities-radio", "options"),
        Input("countries-radio", "value"),
    ) do selected_country

        return [(label = i, value = i) for i in all_options[selected_country]]

    end

    callback!(
        app,
        Output("cities-radio", "value"),
        Input("cities-radio", "options"),

    ) do available_options

        return available_options[1][:value]
    end

    callback!(
        app,
        Output("display-selected-values", "children"),
        Input("countries-radio", "value"),
        Input("cities-radio", "value"),
    ) do selected_country, selected_city

        return \"\$(selected_city) is a city in \$(selected_country)\"
    end


    run_server(app, "0.0.0.0", 8000)

    ```

    The first callback updates the available options in the second
    `RadioItems` component.

    The second callback sets an initial value when the `options` property
    changes: it sets it to the first value in that `options` array.

    The final callback displays the selected `value` of each component. If you
    change the `value` of the countries `RadioItems` component, Dash will wait until
    the `value` of the cities component is updated before calling the final callback.
    This prevents your callbacks from being called with inconsistent state like with
    "America" and "Montreal".
    """),
    html_h1("Dash Apps With State"),
    dcc_markdown("""
    In some cases, you might have a "form"-type pattern in your appliication.
    In such a situation, you might want to read the value of the input component,
    but only when the user is finished entering all of his or her information in
    the form.

    Attaching a callback to the input values directly can look like this:

    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents


    app = dash()

    app.layout = html_div() do
        dcc_input(id="input-1", type="text", value="Montreal"),
        dcc_input(id="input-2", type="text", value="Canada"),
        html_div(id="output-keywords")

    end

    callback!(
        app,
        Output("output-keywords", "children"),
        Input("input-1", "value"),
        Input("input-2", "value"),
    ) do input_1, input_2

        return "Input 1 is \"\$input_1\" and Input 2 is \"\$input_2\""

    end

    run_server(app, "0.0.0.0", 8000)

    ```

    In this example, the callback function is fired whenever any of the attributes
    described by the `Input` change. Try it for yourself by entering data in the inputs
    above.

    `State` allows you pass along extra values without firing the callbacks. Here's the same
    example as above but with the `Input` as `State` and a button as an `Input`.exec

    ```
    using Dash
    using DashHtmlComponents
    using DashCoreComponents


    app = dash()

    app.layout = html_div() do
        dcc_input(id="input-1-state", type="text", value="Montreal"),
        dcc_input(id="input-2-state", type="text", value="Canada"),
        html_button(id="submit-button-state", children="submit", n_clicks=0),
        html_div(id="output-state")

    end

    callback!(
        app,
        Output("output-state", "children"),
        Input("submit-button-state", "n_clicks"),
        State("input-1-state", "value"),
        State("input-2-state", "value")
    ) do clicks, input_1, input_2

        return "The Button has been pressed \"$clicks\" times, Input 1 is \"$input_1\" and Input 2 is \"$input_2\""

    end

    run_server(app, "0.0.0.0", 8000)

    ```

    In this example, changing text in the `Input` boxes won't fire the callback but clicking on the button will.
    The current values of the `Input` values are still passed into the callback even though they don't trigger the
    callback function itself.

    Note that we're triggering the callback by listening to the `n_clicks` property of the `Button` component. `n_clicks`
    is a property that gets incremented every time the component has been clicked on. It is available in
    every component in the `DashHtmlComponents` components library. 
    """),
    html_h1("Summary"),
    dcc_markdown("""
    """)

end

run_server(app, "0.0.0.0", 8000)
