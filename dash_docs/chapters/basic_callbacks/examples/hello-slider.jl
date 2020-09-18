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
traces = []

figure = (
    data = [
        (x = ["giraffes", "orangutans", "monkeys"], y = [20, 14, 23], type = "bar", name = "SF"),
    ],
    layout = (title = "Dash Data Visualization", barmode="group")
)

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
        value = 0)
end

callback!(
    app,
    Output("graph", "figure"),
    Input("year-slider", "value"),
) do index
    #=
    println(years[index+1])

    for cont in continents
        print(cont)
    end

    =#

    df_sub = df[in.(df.year, Ref([years[index+1]])), :]

    figure_data = []

    for cont in continents
        push!(figure_data,
             (x = df_sub["gdpPercap"],
              y = df_sub["lifeExp"],
              type = "scatter",
              mode = "markers",
              opacity=0.5,
              name = cont)
        )
    end

    figure = (
        data = figure_data,
        layout = (xaxis = ((type="log"), (title="GDP")),
                  yaxis = ((title="Life Expectancy"), range=(20, 90)),
        ),
    )

    return figure
end


run_server(app, "0.0.0.0", 8000)
