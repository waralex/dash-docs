using Dash
using DashHtmlComponents
using DashCoreComponents

app =  dash()


app.layout = html_div() do
    html_h1("Interactive Visualizations"),
    html_blockquote(dcc_markdown("This is the 4th chapter of the [Dash Tutorial](/).
    The [previous chapter](/basic-callbacks) covered basic callback usage and the [next chapter](/state)
    describes how to share data between callbacks. Just getting started? Make sure to [install the necessary
    dependencies](/installation)")),
    dcc_markdown("
    The `DashCoreComponents` package includes a component called `Graph`.exec

    `Graph` renders interactive visualizations using the open source [plotly.js](https://github.com/plotly/plotly.js) JavaScript
    graphing library. Plotly.js supports over 35 chart types and renders charts in both vector-quality SVG and high-performance
    WebGL.

    The `figure` argument in the `dcc_graph` component is the same `figure` argument that is used by
    `plotlyjs.jl`, an open source Julia graphing library. Check out
    the [plotlyjs.jl documentation](http://juliaplots.org/PlotlyJS.jl/stable/) and gallery to learn more.

    Dash components are described declaratively by a set of attributes. All of these attributes can be updated by callback
    functions, but only a subset of these attributes are updated through user interaction, such as when you click on an
    option in a `Dropdown` component and the `value` property of that component changes.

    The `Graph` component has four attributes that can change through user interaction: `hoverData`, `clickData`, `selectedData`,
    and `relayoutData`. THese properties update when you hover over points, click on points, or select regions in a graph.

    Here's a simple example that prints these attributes to the screen.
    "),
    dcc_markdown("""
    ```
    using CSV, DataFrames, JSON3
    using Dash, DashHtmlComponents, DashCoreComponents

    df = DataFrame(
        x = [1, 2, 1, 2],
        y = [1, 2, 3, 4],
        customdata = [1, 2, 3, 4],
        fruit = ["apple", "apple", "orange", "orange"],
    )

    fig = (
        data = [
            (
                x = df[:, "x"],
                y = df[:, "y"],
                type = "scatter",
                color = df[:, "fruit"],
                mode = "markers",
                custom_data = df[:, "customdata"],
            ),
        ],
        layout = (clickmode = "event+select"),
    )

    app = dash()

    app.layout = html_div() do
        dcc_graph(id = "basic-interactions", figure = fig),
        html_div(
            children = [
                html_div(
                    children = [
                        dcc_markdown("
                        **Hover Data**

                        Mouse over values in the graph.
                        "),
                        html_pre(id = "hover-data"),
                    ],
                ),
                html_div(
                    children = [
                        dcc_markdown("
                        **Click Data**

                        Click on points in the graph.
                        "),
                        html_pre(id = "click-data"),
                    ],
                ),
                html_div(
                    children = [
                        dcc_markdown("
                        **Selection Data**

                        Choose the lasso or rectangle tool in the graph's menu
                        bar and then select points in the graph.

                        Note that if `layout.clickmode = 'event+select'`, selection data also
                        accumulates (or un-accumulates) selected data if you hold down the shift
                        button while clicking.
                        "),
                        html_pre(id = "selected-data"),
                    ],
                ),
                html_div(
                    children = [
                        dcc_markdown("
                        **Zoom and Relayout Data**

                        Click and drag on the graph to zoom or click on the zoom
                        buttons in the graph's menu bar.
                        Clicking on legend items will also fire
                        this event.
                        "),
                        html_pre(id = "relayout-data"),
                    ],
                ),
            ],
        )

    end

    callback!(
        app,
        Output("hover-data", "children"),
        Input("basic-interactions", "hoverData"),
    ) do hover_data

        return JSON3.write(hover_data)
    end

    callback!(
        app,
        Output("click-data", "children"),
        Input("basic-interactions", "clickData"),
    ) do click_data

        return JSON3.write(click_data)
    end

    callback!(
        app,
        Output("selected-data", "children"),
        Input("basic-interactions", "selectedData"),
    ) do selected_data

        return string(selected_data)
    end

    callback!(
        app,
        Output("relayout-data", "children"),
        Input("basic-interactions", "relayoutData"),
    ) do relayout_data

        return string(relayout_data)
    end

    run_server(app, "0.0.0.0", 8000, debug=true)
    ```
    """),

    dcc_markdown("""
    ### Update Graphs on Hover

    Let's update our world indicators example from the previous chapter by updating time series
    when we hover over points in our scatter plot.

    """),
    dcc_markdown("""

    ```
    using CSV, DataFrames, Dash, DashHtmlComponents, DashCoreComponents
    using PlotlyJS


    url = "https://plotly.github.io/datasets/country_indicators.csv"
    download(url, "country-indicators.csv")
    df = DataFrame(CSV.File("country-indicators.csv"))

    dropmissing!(df)

    available_indicators = unique(df[:, "Indicator Name"])
    years = unique(df[:, "Year"])

    app = dash()

    app.layout = html_div() do
        html_div(
            children = [
                html_div(
                    children = [
                        dcc_dropdown(
                            id = "crossfilter-xaxis-column",
                            options = [
                                (label = i, value = i)
                                for i in available_indicators
                            ],
                            value = "Fertility rate, total (births per woman)",
                        ),
                        dcc_radioitems(
                            id = "crossfilter-xaxis-type",
                            options = [
                                (label = i, value = i) for i in ["linear", "log"]
                            ],
                            value = "linear",
                        ),
                    ],
                    style = (width = "49%", display = "inline-block"),
                ),
                html_div(
                    children = [
                        dcc_dropdown(
                            id = "crossfilter-yaxis-column",
                            options = [
                                (label = i, value = i)
                                for i in available_indicators
                            ],
                            value = "Life expectancy at birth, total (years)",
                        ),
                        dcc_radioitems(
                            id = "crossfilter-yaxis-type",
                            options = [
                                (label = i, value = i) for i in ["linear", "log"]
                            ],
                            value = "linear",
                        ),
                    ],
                    style = (
                        width = "49%",
                        float = "right",
                        display = "inline-block",
                    ),
                ),
            ],
            style = (
                borderBottom = "thin lightgrey solid",
                backgroundColor = "rgb(250, 250, 250)",
                padding = "10px 5px",
            ),
        ),
        html_div(
            children = [
                dcc_graph(id = "crossfilter-indicator-scatter"),
                dcc_slider(
                    id = "crossfilter-year-slider",
                    min = minimum(years),
                    max = maximum(years),
                    marks = Dict([Symbol(v) => Symbol(v) for v in years]),
                    value = minimum(years),
                    step = nothing,
                ),
            ],
            style = (
                width = "49%",
                display = "inline-block"
            ),
        ),
        html_div(
            children = [
                dcc_graph(id = "x-time-series"),
                dcc_graph(id = "y-time-series"),
            ],
            style = (width = "49%", display = "inline-block"),
        )
    end

    callback!(
        app,
        Output("crossfilter-indicator-scatter", "figure"),
        Input("crossfilter-xaxis-column", "value"),
        Input("crossfilter-yaxis-column", "value"),
        Input("crossfilter-xaxis-type", "value"),
        Input("crossfilter-yaxis-type", "value"),
        Input("crossfilter-year-slider", "value"),
    ) do xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_slider_value

        dff = df[df.Year.==year_slider_value, :]

        return Plot(
            dff[dff[Symbol("Indicator Name")] .== xaxis_column_name, :Value],
            dff[dff[Symbol("Indicator Name")] .== yaxis_column_name, :Value],
            Layout(
                xaxis_type = xaxis_type == "Linear" ? "linear" : "log",
                xaxis_title = xaxis_column_name,
                yaxis_title = yaxis_column_name,
                yaxis_type = yaxis_type == "Linear" ? "linear" : "log",
                hovermode = "closest",
                height = 450,
            ),
            kind = "scatter",
            text = dff[
                dff[Symbol("Indicator Name")] .== yaxis_column_name,
                Symbol("Country Name"),
            ],
            customdata = dff[
                dff[Symbol("Indicator Name")] .== yaxis_column_name,
                Symbol("Country Name"),
            ],
            mode = "markers",
            marker_size = 15,
            marker_opacity = 0.5,
            marker_line_width = 0.5,
            marker_line_color = "white",
        )
    end

    function create_time_series(dff, axis_type, title)
        Plot(
            dff[:, :Year],
            dff[:, :Value],
            Layout(
                yaxis_type = axis_type == "Linear" ? "linear" : "log",
                xaxis_showgrid = false,
                annotations = [attr(
                    x = 0,
                    y = 0.85,
                    xanchor = "left",
                    yanchor = "bottom",
                    xref = "paper",
                    yref = "paper",
                    showarrow = false,
                    align = "left",
                    bgcolor = "rgba(255, 255, 255, 0.5)",
                    text = title,
                )],
                height = 225,
            ),
            mode = "lines+markers",
        )
    end

    callback!(
        app,
        Output("x-time-series", "figure"),
        Input("crossfilter-indicator-scatter", "hoverData"),
        Input("crossfilter-xaxis-column", "value"),
        Input("crossfilter-xaxis-type", "value"),
    ) do hover_data, xaxis_column_name, axis_type
        country_name = isnothing(hover_data) ? "" : hover_data.points[1].customdata
        dff = df[df[:, Symbol("Country Name")].==country_name, :]
        dff = dff[dff[:, Symbol("Indicator Name")].==xaxis_column_name, :]
        title = "<b>\$(country_name)</b><br>\$(xaxis_column_name)"
        return create_time_series(dff, axis_type, title)

    end

    callback!(
        app,
        Output("y-time-series", "figure"),
        Input("crossfilter-indicator-scatter", "hoverData"),
        Input("crossfilter-yaxis-column", "value"),
        Input("crossfilter-yaxis-type", "value"),
    ) do hover_data, yaxis_column_name, axis_type
        country_name = isnothing(hover_data) ? "" : hover_data.points[1].customdata
        dff = df[df[:, Symbol("Country Name")].==country_name, :]
        dff = dff[dff[:, Symbol("Indicator Name")].==yaxis_column_name, :]
        return create_time_series(dff, axis_type, yaxis_column_name)
    end

    run_server(app, "0.0.0.0", 8000, debug = true)
    ```

    Try mousing over the points in the scatter plot on the left.
    Notice how the line graphs on the right update based off of the point that you are hovering over.

    """),

    dcc_markdown("""
    ### Generic Crossfilter Recipe

    Here's a slightly more generic example for crossfiltering across a six-column dataset.
    Each scatter plot's selection filters the underlying dataset.

    """),
    dcc_markdown("""

    ```
        ##CODE GOES HERE##
    ```

    """),
    dcc_markdown("""

    Try clicking and dragging in any of the plots to filter different regions.
    On every selection, the three graph callbacks are fired with the latest selected regions of each plot.
    A dataframe is filtered based off of the selected points and the graphs are replotted
    with the selected points highlighted and the selected region drawn as a dashed rectangle.

    """),

    dcc_markdown("""
    ### Current Limitations

    There are a few limitations in graph interactions right now.

    * It is not currently possible to customize the style of the hover interactions
    or the select box. This issue is being worked on in https://github.com/plotly/plotly.js/issues/1847.

    There's a lot that you can do  with these interactive plotting features. If you need
    help exploring your use case, open up a thread in the [Dash Community Forum](https://community.plotly.com/c/dash/julia/20)

    The next chapter of the Dash User Guide explains how to share data between
    callbacks.

    [Dash Tutorial Part 5: Sharing Data Between Callbacks](/sharing-data-between-callbacks)
    """)
end

run_server(app, "0.0.0.0", 8000, debug=true)
