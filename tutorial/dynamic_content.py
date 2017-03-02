# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json

from server import app

layout = html.Div(content=[
    html.H1('Loading Content Dynamically'),

    html.Div('''Dash callbacks can return any type of property.
    By returning `content`, they can even dyanimcally
    render their content.
    '''),

    html.Div('''This allows you to build a lot of neat interactions.
    Here are some examples.'''),

    html.H3('Render content by clicking a button'),

    html.Div('''This is a clever hack that can make development a lot easier.
    Instead of refreshing the page to view your layout,
    just render the layout as a response to clicking on a button.'''),

    dcc.SyntaxHighlighter('''app.layout = html.Div([
    html.Button('Click to load content', id='button'),
    html.Div(id='content')
])

# When you click the button, this content gets loaded
@app.react('content', events=[{'id': 'button', 'event': 'onClick'}])
def render_content(*args, **kwargs):
    return {
        'content': html.Div([
            html.H1('Hello Dash')
        ])
    }''', language='python'),

    html.Div([
        html.Button('Click to load content', id='button-dynamic-content'),
        html.Br(),
        html.Div(id='dynamic-content')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'})

])


@app.react('button-dynamic-content', events=[{
    'id': 'dynamic-content', 'event': 'onClick'
}])
def render(*args, **kwargs):
    return {
        'content': html.Div([
            html.H3('Hello Dash')
        ])
    }
