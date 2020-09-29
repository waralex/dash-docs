using CSV, DataFrames, Dash, DashHtmlComponents, DashCoreComponents, PlotlyJS


url = "https://plotly.github.io/datasets/country_indicators.csv"
download(url, "country-indicators.csv")

df = DataFrame(CSV.File("country-indicators.csv"))

dropmissing!(df)

available_indicators = unique(df[!, "Indicator Name"])
years = unique(df[!, "Year"])

app = dash()

app.layout = html_div() do
    html_div(
        children = [
            dcc_dropdown(
                id = "xaxis-column",
                options = [
                    (label = i, value = i) for i in available_indicators
                ],
                value = "Fertility rate, total (births per woman)",
            ),
            dcc_radioitems(
                id = "xaxis-type",
                options = [(label = i, value = i) for i in ["linear", "log"]],
                value = "linear",
            ),
        ],
        style = (width = "48%", display = "inline-block"),
    ),
    html_div(
        children = [
            dcc_dropdown(
                id = "yaxis-column",
                options = [
                    (label = i, value = i) for i in available_indicators
                ],
                value = "Life expectancy at birth, total (years)",
            ),
            dcc_radioitems(
                id = "yaxis-type",
                options = [(label = i, value = i) for i in ["linear", "log"]],
                value = "linear",
            ),
        ],
        style = (width = "48%", display = "inline-block", float = "right"),
    ),
    dcc_graph(id = "indicator-graphic"),
    dcc_slider(
        id = "year-slider",
        min = minimum(years),
        max = maximum(years),
        marks = Dict([Symbol(v) => Symbol(v) for v in years]),
        value = minimum(years),
        step = nothing,
    )
end

callback!(
    app,
    Output("indicator-graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
    Input("xaxis-type", "value"),
    Input("yaxis-type", "value"),
    Input("year-slider", "value"),
) do xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value
    dff = df[df.Year.== year_value, :]
    return Plot(
        dff[dff[!, Symbol("Indicator Name")] .== xaxis_column_name, :Value],
        dff[dff[!, Symbol("Indicator Name")] .== yaxis_column_name, :Value],
        Layout(
            xaxis_type = xaxis_type == "Linear" ? "linear" : "log",
            xaxis_title = xaxis_column_name,
            yaxis_title = yaxis_column_name,
            yaxis_type = yaxis_type == "Linear" ? "linear" : "log",
            hovermode = "closest",
        ),
        kind = "scatter",
        text = dff[
            dff[Symbol("Indicator Name")] .== yaxis_column_name,
            Symbol("Country Name"),
        ],
        mode = "markers",
        marker_size = 15,
        marker_opacity = 0.5,
        marker_line_width = 0.5,
        marker_line_color = "white"
    )
end

run_server(app, "0.0.0.0", 8000, debug = true)
