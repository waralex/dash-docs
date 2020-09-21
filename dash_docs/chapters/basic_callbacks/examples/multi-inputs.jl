using CSV
using DataFrames
using Dash
using DashHtmlComponents
using DashCoreComponents
using PlotlyJS


url = "https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv"
download(url, "country-indicators.csv")
df = CSV.read("country-indicators.csv")

rename!(df, Dict(:"Indicator Name" => "Indicator"))
available_indicators = unique(df[:Indicator])
years = unique(df[:Year])

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
) do xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value

    dff = filter(row -> row.Year == years[year_value+1], df)

    figure_data = (
        x = filter(row -> row.Indicator == xaxis_column_name, dff)[:Value],
        y = filter(row -> row.Indicator == yaxis_column_name, dff)[:Value],
        type = "scatter",
    )

    figure = (
        data = figure_data,
    )

    return figure

end


run_server(app, "0.0.0.0", 8000)
