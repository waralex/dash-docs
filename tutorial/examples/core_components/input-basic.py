# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-keypress', type='text', value='Montréal'),
    dcc.Input(id='input-2-keypress', type='text', value='Canada'),
    html.Div(id='output-keypress')
])


@app.callback(Output('output-keypress', 'children'),
              [Input('input-1-keypress', 'value'),
               Input('input-2-keypress', 'value')])
def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
