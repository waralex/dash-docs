#=
using DataFrames, CSV, HTTP
using Dash
using DashHtmlComponents
using DashCoreComponents
using PlotlyJS

gdp_life_expectancy_2007_csv =
    HTTP.get("https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv").body

df = DataFrame(CSV.File(gdp_life_expectancy_2007_csv))

fig = Plot(df, x=:"gdp per capita", y=:"life expectancy")

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.layout = html_div() do
    html_h4("GDP vs Life Expectancy"),
    dcc_graph(figure=fig)
end

run_server(app, "0.0.0.0", 8000)
=#

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
