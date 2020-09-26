using CSV, DataFrames, Dash, DashHtmlComponents, DashCoreComponents


url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
download(url, "gapminder-data.csv")
df = DataFrame(CSV.File("gapminder-data.csv"))

continents = unique(df[!, :continent])
years = unique(df[!, :year])

app = dash()

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
    single_year_df = df[df.year .== years[index+1], :]

    figure_data = []

    for cont in continents
        single_continent_df = single_year_df[single_year_df.continent .== cont, :]
        push!(figure_data,
             (x = single_continent_df[:, :gdpPercap],
              y = single_continent_df[:, :lifeExp],
              type = "scatter",
              mode = "markers",
              hovertext = single_continent_df[:, :country],
              opacity=0.5,
              name = cont)
        )
    end

    figure = (
        data = figure_data,
        layout = (xaxis = ((type="log"), (title="GDP")),
                  yaxis = ((title="Life Expectancy"), range=(20, 90)),
                  transition_duration=500
        ),
    )

    return figure
end

run_server(app, "0.0.0.0", 8000)
