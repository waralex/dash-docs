import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

root_layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                daq.ToggleSwitch(
                    id="toggleTheme",
                    style={"position": "absolute", "transform": "translate(-50%, 20%)"},
                    size=25,
                )
            ],
            id="toggleDiv",
            style={"width": "fit-content", "margin": "0 auto"},
        ),
        html.Div(id="page-content"),
    ]
)

base_layout = html.Div(
    [
        'Hello World'
    ]
)


light_layout = html.Div(id="container", children=[base_layout])

dark_layout = daq.DarkThemeProvider(
    [
        html.Link(
            href="https://cdn.rawgit.com/matthewchan15/dash-css-style-sheets/e84db719/dash-dark-hp-multimeter.css",
            rel="stylesheet",
        ),
        html.Div([base_layout]),
    ]
)

app.layout = root_layout


@app.callback(
    dash.dependencies.Output("toggleTheme", "value"),
    [dash.dependencies.Input("url", "pathname")]
)
def display_page(pathname):

    if pathname == "/dark":
        return True
    else:
        return False


@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("toggleTheme", "value")]
)
def page_layout(value):
    if value:
        return dark_layout
    else:
        return light_layout

if __name__ == '__main__':
    app.run_server(debug=True)
