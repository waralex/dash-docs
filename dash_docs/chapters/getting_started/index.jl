using Dash
using DashHtmlComponents
using DashCoreComponents

app = dash()


app.layout = html_div() do
    html_h1("Dash Layout"),
    html_blockquote(dcc_markdown("This is the 2nd chapter of the [Dash Tutorial](/).
    The previous chapter covered [installation](/installation) and the next chapter covers [Dash callbacks](/basic-callbacks).")),
    dcc_markdown("""
    This tutorial will walk you through a fundamental aspect of Dash apps, the app `layout`, through several self-contained apps.
    """),
    html_hr(),
    dcc_markdown("""
    Dash apps are composed of two parts. The first part is the `layout` of the app and it describes what the application looks like.
    The second part describes the interactivity of the application and will be covered in the [next chapter](/basic-callbacks).

    Dash provides Julia methods for all of the visual components of the application.
    We maintain a set of components in the `DashCoreComponents` and the `DashHtmlComponents` packages
    but you can also build your own with JavaScript and React.js

    Note: Throughout this documentation, Julia code examples are meant to be saved as files and executed using `julia app.jl`.
    These examples are not intented to run in Jupyter notebooks as-is,
    although most can be modified slightly to function in that environment.

    To get started, create a file called `app.jl` with the following code:

    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents

    app = dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    app.layout = html_div() do
        html_h1("Hello Dash"),
        html_div("Dash: A web application framework for Julia"),
        dcc_graph(
            id = "example-graph",
            figure = (
                data = [
                    (x = ["giraffes", "orangutans", "monkeys"], y = [20, 14, 23], type = "bar", name = "SF"),
                    (x = ["giraffes", "orangutans", "monkeys"], y = [12, 18, 29], type = "bar", name = "Montréal"),
                ],
                layout = (title = "Dash Data Visualization", barmode="group")
            )
        )
    end

    run_server(app, "0.0.0.0", 8000)
    ```

    Run the app with
    ```
    \$ julia app.jl
    ```

    In the `julia` REPL you can run, assuming that `app.jl` is in your current working directory.
    ```
    julia> include("app.jl")
    ```

    You can visit the app by visiting the URL http://127.0.0.1:8000.

    Note:

    1. The `layout` is composed of a tree of "components" like `html_div` and `dcc_graph`.
    2. The `DashHtmlComponents` package has a component for every HTML tag. The `html_h1("Hello Dash")` component
    generates a `<h1>Hello Dash</h1>` HTML element in your application.
    3. Not all components are pure HTML. The `DashCoreComponents` package describes higher level components
    that are interactive and genrated with JavaScript, HTML, and CSS through the React.js library.
    4. Each component is described entirely through keyword attributes. Dash is *declarative*: you will
    priimarily describe your application through these attributes.
    5. The `children` property is special. By convention, it's always the first attribute which means that you can omit it;
    `html_div(children="Hello Dash")` is the same as `html_div("Hello Dash")`. Also, it can contain a string, a number, a single
    component, or a list of components.
    6. The fonts in your application will look a little bit different than what is displayed here. This application is using
    a custom CSS stylesheet to modify the default styles of the elements. If you would like to use this stylesheet,
    you can initialize your app with

    `app = dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])`


    """),
    html_h1("More About HTML"),
    dcc_markdown("""
    The `DashHtmlComponents` package contains a component class for every HTML tag as well as keyword arguments for all of the
    HTML arguments.

    Let's customize the text in our app by modifying the inline styles of the components:
    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents

    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    app.layout = html_div(style = Dict("backgroundColor" => "#111111")) do
        html_h1(
            "Hello Dash",
            style = Dict("color" => "#7FDBFF", "textAlign" => "center"),
        ),
        html_div(
            "Dash: A web application framework for Julia",
            style = Dict("color" => "#7FDBFF"),
        ),
        dcc_graph(
            id = "example-graph",
            figure = (
                data = [
                    (
                        x = ["giraffes", "orangutans", "monkeys"],
                        y = [20, 14, 23],
                        type = "bar",
                        name = "SF",
                    ),
                    (
                        x = ["giraffes", "orangutans", "monkeys"],
                        y = [12, 18, 29],
                        type = "bar",
                        name = "Montréal",
                    ),
                ],
                layout = (
                    title = "Dash Data Visualization",
                    barmode = "group",
                    plot_bgcolor = "#111111",
                    paper_bgcolor = "#111111",
                    font = Dict("color" => "#7FDBFF"),
                ),
            ),
        )
    end

    run_server(app, "0.0.0.0", 8000)
    ```

    In this example, we modified the inline styles of the `html_div` and
    `html_h1` components with the style property. `html_h1("Hello Dash",
    style = Dict("color" => "#7FDBFF", "textAlign" => "center"))` is rendered
    in the Dash application as `<h1 style="text-align: center; color: rgb(127, 219, 255);">Hello Dash</h1>`

    There are a few important differences between the `DashHtmlComponents` and HTML attributes:

    1. The `style` property in HTML is a semicolon separated string. In Dash, you can just suppy a `Dict`.
    2. The keys in the `style` `Dict` are [camelCased]("https://en.wikipedia.org/wiki/Camel_case"). So instead of `text-align`, it's `textAlign`.
    3. The HTML `class` attribute is `className` in Dash.
    4. The children of the HTML tag is specified through the `children` keywork argument. By convention, this is
    always the first argument and so it is often omitted. Besides that, all of the available HTML attributes and
    tags are available to you within your Julia context.
    """),
    html_h1("Reusable Components"),
    dcc_markdown("""
    By writing our markup in Julia, we can create
    complex reusable components like tables without switching contexts or
    languages.

    Here's a quick example that generates a `Table` from a `DataFrame`.
    Create a file named `app.jl` with the following code:
    ```julia
    using DataFrames, CSV
    using Dash
    using DashHtmlComponents
    using DashCoreComponents


    url = "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
    download(url, "usa-agriculture.csv")
    df = DataFrame(CSV.File("usa-agriculture.csv"))

    function generate_table(dataframe, max_rows = 10)
        html_table([
            html_thead(html_tr([html_th(col) for col in names(df)])),
            html_tbody([
                html_tr([html_td(dataframe[r, c]) for c in names(dataframe)]) for r = 1:min(nrow(dataframe), max_rows)
            ]),
        ])

    end


    app =
        dash(external_stylesheets = [\"https://codepen.io/chriddyp/pen/bWLwgP.css\"])

    app.layout = html_div() do
        html_h4(\"US Agriculture Exports (2011)\"),
        generate_table(df, 10)
    end

    run_server(app, \"0.0.0.0\", 8000)
    ```
    """),
    html_h1("More About Visualization"),
    dcc_markdown("""
    The `DashCoreComponents` package includes a component called `graph`.

    `graph` renders interactive data visualizations using the open source
    plotly.js JavaScript graphing library. Plotly.js supports over 35 chart types
    and renders charts in both vector-quality SVG and high-performance WebGL.

    The `figure` argument in the `dcc_graph` component is the same `figure` argument
    that is used by `plotly.py`, Plotly's open-source Python graphing library. Check out the
    plotly.py documentatioin and gallery to learn more.

    Here's an example that creates a scatter plot from a `DataFrame`. Create a file named `app.jl`
    with the following code:

    ```julia
    using DataFrames, CSV, HTTP
    using Dash
    using DashHtmlComponents
    using DashCoreComponents
    using PlotlyJS
    using RDatasets


    iris = dataset("datasets", "iris")

    p1 = Plot(iris, x=:SepalLength, y=:SepalWidth, mode="markers", marker_size=8, group=:Species)

    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    app.layout = html_div() do
        html_h4("Iris Sepal Length vs Sepal Width"),
        dcc_graph(
            id = "example-graph",
            figure = p1,
        )
    end

    run_server(app, "0.0.0.0", 8000)
    ```

    These graphs are interactive and responsive. *Hover* over points to see their values, *click* on legend items to
    toggle traces, *click and drag* to zoom, *hold down shift and click and drag* to pan.

    """),
    html_h1("Markdown"),
    dcc_markdown("""
    While Dash exposes HTML through the `DashHtmlComponents` package, it can be tedious to write your
    copy in HTML. For writing blocks of text, you can use the `dcc_markdown` component in the `DashCoreComponents` package.

    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents


    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])
    markdown_text = "
    ### Dash and Markdown

    Dash apps can be written in Markdown.
    Dash uses the [CommonMark](http://commonmark.org/)
    specification of Markdown.
    Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
    if this is your first introduction to Markdown!
    "

    app.layout = html_div() do
        dcc_markdown(markdown_text)
    end

    run_server(app, "0.0.0.0", 8000)
    ```

    """),
    html_h1("Core Components"),
    dcc_markdown("""
    The `DashCoreComponents` package includes a set of higher level components like
    dropdowns, graphs, markdown blocks, and more. Like all Dash components, they are described
    entirely declaratively. Every optiion that is configuragble is available as a keyword
    argument to the component.
    ```julia
    using Dash
    using DashHtmlComponents
    using DashCoreComponents


    app =
        dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

    dropdown_options = [
        Dict("label" => "New York City", "value" => "NYC"),
        Dict("label" => "Montreal", "value" => "MTL"),
        Dict("label" => "San Francisco", "value" => "SF"),
    ]
    app.layout = html_div(style=Dict("columnCount" => 2)) do
        html_label("Dropdown"),
        dcc_dropdown(options = dropdown_options, value = "MTL"),
        html_label("Multi-Select Dropdown"),
        dcc_dropdown(options = dropdown_options, value = ["MTL", "SF"], multi=true),
        html_label("Radio Items"),
        dcc_radioitems(options = dropdown_options, value = "MTL" ),
        html_label("Checkboxes"),
        dcc_checklist(options = dropdown_options, value = ["MTL", "SF"]),
        html_label("Text Input"),
        dcc_input(value = "MTL", type = "text"),
        html_label("Slider"),
        dcc_slider(min = 0, max = 9, marks = ["", "Label 1", "Label 3"], value = 5)


    end

    run_server(app, "0.0.0.0", 8000)
    ```

    """),



end

run_server(app, "0.0.0.0", 8000)
