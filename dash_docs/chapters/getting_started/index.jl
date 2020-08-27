using Dash
using DashHtmlComponents
using DashCoreComponents

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])


app.layout = html_div() do
    html_h1("Dash Layout"),
    html_blockquote("This is the 2nd chapter of the [Dash Tutorial](/).
    The previous chapter covered [installation](/installation) and the next chapter covers [Dash callbacks](/basic-callbacks)."),
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



    """)



end

run_server(app, "0.0.0.0", 8000)
