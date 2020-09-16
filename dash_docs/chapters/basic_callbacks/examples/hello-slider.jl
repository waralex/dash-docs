using CSV
using DataFrames
using Dash
using DashHtmlComponents
using DashCoreComponents
using RDatasets
using PlotlyJS

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
download(url, "gapminder-data.csv")
df = CSV.read("gapminder-data.csv")
iris = dataset("datasets", "iris")

continents = unique(df["continent"])
years = unique(df["year"])

p1 = Plot(iris, x=:SepalLength, y=:SepalWidth, mode="markers", marker_size=8, group=:Species)

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])


app.layout = html_div() do
    dcc_graph(id="graph"),
    dcc_slider(
        id = "year-slider",
        min = 0,
        max = length(years) - 1,
        marks = years,
        value = 0),
    html_div("kj;ksjf;lkdajfs", id="input",)

end

callback!(
    app,
    Output("graph", "figure"),
    Input("input", "children"),
) do
    return Plot(iris, x=:SepalLength, y=:SepalWidth, mode="markers", marker_size=8, group=:Species)
end


run_server(app, "0.0.0.0", 8000)
