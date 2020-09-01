using Dash
using DashHtmlComponents
using DashCoreComponents


app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

dropdown_options = [
    Dict("label" => "New York City", "value" => "NYC"),
    Dict("label" => "Montreal", "value" => "MTL"),
    Dict("label" => "San Francisco", "value" => "SF"),
]
app.layout = html_div(style=Dict("columnCount" => 2)) do
    html_label("Dropdown"),
    dcc_dropdown(options = dropdown_options, value = "MTL"),
    html_label("Multi-Select Dropdown"),
    dcc_dropdown(options = dropdown_options, value = ["MTL", "SF"], multi=true),
    html_label("Radio Items"),
    dcc_radioitems(options = dropdown_options, value = "MTL" ),
    html_label("Checkboxes"),
    dcc_checklist(options = dropdown_options, value = ["MTL", "SF"]),
    html_label("Text Input"),
    dcc_input(value = "MTL", type = "text"),
    html_label("Slider"),
    dcc_slider(min = 0, max = 9, marks = ["", "Label 1", "Label 3"], value = 5)


end

run_server(app, "0.0.0.0", 8000)
