import dash
import dash_html_components as html
import dash_daq as daq

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWlwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    daq.BooleanSwitch(
        id='my-boolean-switch',
        label='Default'
    ),
    html.Div(id='boolean-switch-output-container')
])


@app.callback(
    dash.dependencies.Output('boolean-switch-output-container', 'children'),
    [dash.dependencies.Input('my-boolean-switch', 'value')])
def update_output(value):
    return 'The switch is {}.'.format("on" if value else "off")

if __name__ == '__main__':
    app.run_server(debug=True)
