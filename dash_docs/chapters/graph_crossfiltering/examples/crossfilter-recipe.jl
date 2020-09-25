using DataFrames, Dash, DashHtmlComponents, DashCoreComponents
using RDatasets, JSON3
using PlotlyJS


df = DataFrame(Dict(("Col $(i)" => rand(30)) for i = 1:6))

#p1 = scatter(;x=df[:, "Col 1"], y=df[:, "Col 2"], mode="markers", marker_size=8)

function create_figure2(df, x_col, y_col, points)
    return Plot(df,
                x=df[:, x_col],
                y=y_col,
                mode="markers+text",
                marker = ((color = "rgba(0, 116, 217, 0.7)"), size = 20)
                marker_size=20,
                text=1:size(df)[1],
                customdata = 1:size(df)[1],
                selectedpoints = points,
                unselected = (marker = (opacity = 0.3, textfont = (color = "rgba(0,0,0,0)")))
            )
end

function create_figure(df, x_col, y_col, points)
    fig = (
        data = [
            (
                x = df[:, x_col],
                y = df[:, y_col],
                type = "scatter",
                mode = "markers",
                marker_size = 20,
                text = 1:size(df)[1],

            ),
        ],
        layout = (dragmode = "select")
    )

    return fig
end

app = dash()

app.layout = html_div() do
    html_div(
        children=[dcc_graph(
            id = "graph1",
        )],
        style = (width = "32%", display = "inline-block"),
    ),
    html_div(
        children=[dcc_graph(
            id = "graph2",
        )],
        style = (width = "32%", display = "inline-block"),
    ),
    html_div(
        children=[dcc_graph(
            id = "graph3",
        )],
        style = (width = "32%", display = "inline-block"),
    )
end



callback!(
    app,
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Input("graph1", "selectedData"),
    Input("graph2", "selectedData"),
    Input("graph3", "selectedData"),
) do selection1, selection2, selection3
    selectedpoints = 1:size(df)[1]

    for selected_data in [selection1, selection2, selection3]
        if selected_data != nothing
            selectedpoints = [p[:customdata] for p in selected_data.points]
        end
    end

    println("**************************")
    println(selection1)
    println("**************************")

    println("**************************")
    println(selection2)
    println("**************************")

    println("**************************")
    println(selection3)
    println("**************************")


    return create_figure2(df, "Col 1", "Col 2"),
           create_figure2(df, "Col 3", "Col 4"),
           create_figure2(df, "Col 5", "Col 6")
end



run_server(app, "0.0.0.0", 8000)
