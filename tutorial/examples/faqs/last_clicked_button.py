import json

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-1'),
    html.Button('Button 2', id='btn-2'),
    html.Button('Button 3', id='btn-3'),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('btn-1', 'n_clicks'),
               Input('btn-2', 'n_clicks'),
               Input('btn-3', 'n_clicks')])
def display(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        msg = 'None of the buttons have been clicked yet'
    else:
        button_num = ctx.triggered[0]['prop_id'].split('.')[0].split('-')[1]
        msg = 'Button {} was most recently clicked'.format(button_num)

    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Div('btn1: {}'.format(btn1)),
        html.Div('btn2: {}'.format(btn2)),
        html.Div('btn3: {}'.format(btn3)),
        html.Div(msg),
        html.Pre(ctx_msg)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
