using Dash
using DashHtmlComponents
using DashCoreComponents

app = dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.layout = html_div() do
        dcc_input(id = "my-id", value="initial value", type = "text"),
        html_div(id = "my-div"),
        html_div(id = "my-div2")
    end

callback!(app, [Output("my-div","children"), Output("my-div2","children")], Input("my-id", "value"), State("my-id", "type")) do input_value, state_value
    "You've entered $(input_value) in input with type $(state_value)",
    "You've entered $(input_value)"
end
run_server(app, "0.0.0.0", 8080)
