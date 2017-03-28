# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
from dash.dependencies import Input, Output, Event, State

from server import app


layout = html.Div([
    html.Strong('Installation'),
    html.Div('''
        In your terminal, install several dash libraries.
        These libraries are under active development,
        so install and upgrade frequently.
        Note that dash currently only supports Python 2.7.
        3.x will be supported in the stable release.
    '''),
    dcc.SyntaxHighlighter('''$ pip install dash.ly --upgrade  # The core dash backend
$ pip install dash-renderer --upgrade  # The dash front-end
$ pip install dash-html-components --upgrade  # HTML components
$ pip install dash-core-components --upgrade  # Supercharged components
$ pip install pandas_datareader # Pandas extension used in some examples
''', language='bash', customStyle={'borderLeft': 'thin solid lightgrey'}),

    html.Strong('Hello World'),
    html.Div('''
        Here's a quick example to get you started.
        In a file called app.py, write:
    '''),
    dcc.SyntaxHighlighter('''import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc Dropdown, Graph
from dash_html_components import Div, H3, Link

from plotly import graph_objs as go
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.react.Dash('Hello World')

# Describe the layout, or the UI, of the app
app.layout = Div([
    H3('Hello World'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
])

# Register a callback to update the 'figure' property of the 'my-graph'
# component when the 'value' property of the 'my-dropdown' component changes
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(dropdown_properties):
    df = web.DataReader(
        dropdown_properties['value'], 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return go.Figure(
        data=[{
            'x': df.index,
            'y': df.Close
        }]
    )

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div('Run the app with'),
    dcc.SyntaxHighlighter('''$ python app.py
...Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
''',  customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div([
        html.Span('and visit '),
        html.A('http://localhost:5000/', href='http://localhost:5000/', target='_blank'),
        html.Span(' in your web browser.')
    ]),
    html.Div([
        html.H3('Hello World'),
        dcc.Dropdown(
            id='my-dropdown-getting-started',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Graph(id='my-graph-getting-started')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'})
])


# Register a callback to update 'my-graph' component when 'my-dropdown' changes
@app.callback(Output('my-graph-getting-started', 'figure'),
              [Input('my-dropdown-getting-started', 'value')])
def update_graph(dropdown_value):
    df = web.DataReader(
        dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return go.Figure(
        data=[{
            'x': df.index,
            'y': df.Close
        }]
    )
