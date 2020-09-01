using Dash
using DashHtmlComponents
using DashCoreComponents

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.layout = html_div() do
    dcc_input(id="input", value="initial value", type = "text"),
    html_div(id="output")
end

callback!(app, Output("output", "children"), Input("input", "value")) do input_value
    "You've entered $(input_value)"
end

run_server(app, "0.0.0.0", 8000)
