using CSV, DataFrames, Dash, DashHtmlComponents, DashCoreComponents
using PlotlyJS


url = "https://plotly.github.io/datasets/country_indicators.csv"
download(url, "country-indicators.csv")
df = DataFrame(CSV.File("country-indicators.csv"))

dropmissing!(df)

rename!(df, Dict(:"Indicator Name" => "Indicator"))
rename!(df, Dict(:"Country Name" => "Country"))

available_indicators = unique(df[:, "Indicator"])
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
        children = [dcc_graph(id = "crossfilter-indicator-scatter"),
                    dcc_slider(
                        id = "crossfilter-year-slider",
                        min = 0,
                        max = length(years) - 1,
                        value = 0,
                        marks = years,
                    )],
        style = (width = "49%", display = "inline-block", paddingBottom = "400px"),
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
) do x_indicator, y_indicator, x_axis_type, y_axis_type, year_slider_value

    dff = df[df.Year .== years[year_slider_value+1], :]

    x_indicator_data = dff[dff.Indicator .== x_indicator, :][:, :Value]
    y_indicator_data = dff[dff.Indicator .== y_indicator, :][:, :Value]
    country_names = dff[dff.Indicator .== y_indicator, :][:, :Country]

    figure = (
        data = [
            (
                x = x_indicator_data,
                y = y_indicator_data,
                type = "scatter",
                mode = "markers",
                text = country_names
            ),
        ],
        layout = (
            xaxis = ((title = x_indicator), (type = x_axis_type)),
            yaxis = ((title = y_indicator), (type = y_axis_type)),
        ),
    )

    return figure

end

callback!(
    app,
    Output("x-time-series", "figure"),
    Input("crossfilter-indicator-scatter", "hoverData"),
    Input("crossfilter-xaxis-column", "value"),
    Input("crossfilter-xaxis-type", "value"),
) do hoverData, x_indicator, axis_type

    if hoverData == nothing
        return PreventUpdate()
    end

    country = hoverData[1][1][:text]

    dff = df[df.Country .== country, :]
    dff = dff[dff.Indicator .== x_indicator, :]

    figure = (
        data = [
            (
                x = dff[!, "Year"],
                y = dff[!, "Value"],
                type = "scatter",
                mode = "markers+lines"
            )
        ],
        layout = (
            title = country,
            xaxis = ((title = "Year"), (type = axis_type)),
            yaxis = ((title = x_indicator), (type = axis_type)),
        ),
    )

    return figure

end

callback!(
    app,
    Output("y-time-series", "figure"),
    Input("crossfilter-indicator-scatter", "hoverData"),
    Input("crossfilter-yaxis-column", "value"),
    Input("crossfilter-yaxis-type", "value"),
) do hoverData, y_indicator, axis_type

    if hoverData == nothing
        return PreventUpdate()
    end

    country = hoverData[1][1][:text]

    dff = df[df.Country .== country, :]
    dff = dff[dff.Indicator .== y_indicator, :]

    figure = (
        data = [
            (
                x = dff[!, "Year"],
                y = dff[!, "Value"],
                type = "scatter",
                mode = "markers+lines"
            )
        ],
        layout = (
            title = country,
            xaxis = ((title = "Year"), (type = axis_type)),
            yaxis = ((title = y_indicator), (type = axis_type)),
        ),
    )

    return figure
end

run_server(app, "0.0.0.0", 8000)
