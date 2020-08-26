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
    The second part describes the interactivity of the application and will be covered in the next chapter.

    Dash provides Julia methods for all of the visual components of the application.
    We maintain a set of components in the `dash_core_components` and the `dash_html_components` libraries
     but you can also build your own with JavaScript and React.js.

    Note: Throughout this documentation, Julia code examples are meant to be saved as files and executed using `julia app.jl`.
    These examples are not intented to run in Jupyter notebooks as-is, although most can be modified slightly to function in that environment.

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
    """)
end

run_server(app, "0.0.0.0", 8000)
