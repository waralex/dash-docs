# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json

from server import app

layout = html.Div(content=[
    html.H2('Loading Content Dynamically'),

    html.Div('''Dash callbacks can return any type of property.
    By returning `content`, they can even dynamically
    render their content.
    '''),

    html.Div('''This allows you to build a lot of neat interactions.
    Here are some examples.'''),

    html.H5('Render content by clicking a button'),

    html.Div('''This is a clever hack that can make development a lot easier.
    Instead of refreshing the page to view your layout,
    just render the layout as a response to clicking on a button.'''),

    dcc.SyntaxHighlighter('''app.layout = html.Div([
    html.Button('Click to load content', id='button'),
    html.Div(id='content')
])

# When you click the button, this content gets loaded
@app.callback(
    Output('dynamic-content', 'content'),
    events=[Event('button-dynamic-content', 'click')])
def render():
    return html.Div([
        html.H3('Hello Dash')
    ])
    ''',
    language='python',
    customStyle={'borderLeft': 'thin solid lightgrey'}),

    html.Div([
        html.Button('Click to load content', id='button-dynamic-content'),
        html.Br(),
        html.Div(id='dynamic-content')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'})

])


@app.callback(
    Output('dynamic-content', 'content'),
    events=[Event('button-dynamic-content', 'click')])
def render(*args, **kwargs):
    return html.Div([
        html.H3('Hello Dash')
    ])
