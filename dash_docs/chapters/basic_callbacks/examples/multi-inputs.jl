using CSV
using DataFrames
using Dash
using DashHtmlComponents
using DashCoreComponents
using PlotlyJS


url = "https://plotly.github.io/datasets/country_indicators.csv"
download(url, "country-indicators.csv")
df = DataFrame(CSV.File("country-indicators.csv"))

dropmissing!(df)

rename!(df, Dict(:"Indicator Name" => "Indicator"))
available_indicators = unique(df[:, "Indicator"])
years = unique(df[:, "Year"])

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
                value="linear"
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
                value="linear",
            ),
        ],
        style = (width = "48%", display = "inline-block", float = "right"),
    ),
    dcc_graph(id = "indicator-graphic"),
    dcc_slider(
        id = "year-slider",
        min = 0,
        max = length(years) - 1,
        value = 0,
        marks = years,
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
) do x_axis_value, y_axis_value, x_axis_type, y_axis_type, year_value

    dff = filter(row -> row.Year == years[year_value+1], df)

    x_axis_data = filter(row -> row.Indicator == x_axis_value, dff)[:, "Value"]
    y_axis_data = filter(row -> row.Indicator == y_axis_value, dff)[:, "Value"]

    figure = (
        data = [
            (x = x_axis_data, y = y_axis_data, type = "scatter", mode="markers"),
        ],
        layout = (xaxis = ((title=x_axis_value), (type=x_axis_type)),
                  yaxis = ((title=y_axis_value), (type=y_axis_type)))
    )

    return figure

end

run_server(app, "0.0.0.0", 8000)
