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
#dropmissing!(df)
available_indicators = unique(df[:Indicator])
years = unique(df[:Year])

dff = filter(row -> row.Year == years[1], df)

figure_data = (
    x = filter(row -> row.Indicator == "Fertility rate, total (births per woman)", dff)[:Value],
    y = filter(row -> row.Indicator == "Life expectancy at birth, total (years)", dff)[:Value],
    type = "scatter",
)

figure_1 = (
    data = figure_data,
)


app = dash()

app.layout = html_div() do
    dcc_graph(id = "indicator-graphic", figure=figure_1)
end

run_server(app, "0.0.0.0", 8000)
