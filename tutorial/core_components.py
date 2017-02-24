# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json

from server import app

layout = html.Div(content=[
    html.H4('Supercharged Components'),

    html.Div('''
        Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the authors of dash,
        is available in the `dash-core-components` library. Let's take a look:
    '''),

    html.Hr(),
    html.Strong('Dropdown'),
    dcc.SyntaxHighlighter('''from dash_core_components import Dropdown

Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value="MTL"
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], value="MTL", id='section2-dropdown-1'),

    dcc.SyntaxHighlighter('''from dash_core_components import Dropdown

Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], multi=True, value="MTL", id='section2-dropdown-2'),
    html.Div('''
    Heads up!
    Dropdown requires some special CSS to render properly.
    Include this CSS by `Link`'ing it in your app's `layout`:
    '''),
    dcc.SyntaxHighlighter('''import dash_html_components as html
from dash_core_components import Dropdown

app.layout = html.Div([
    html.Link(
        rel="stylesheet",
        href="https://unpkg.com/react-select@1.0.0-rc.3/dist/react-select.css"
    ),

    # And then the rest of your dash layout:
    Dropdown(...)
])'''),

    html.Hr(),
    html.Strong('Slider'),
    dcc.SyntaxHighlighter('''from dash_core_components import Slider

Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        value=-3,
        id='section2-slider-1'
    ),

    dcc.SyntaxHighlighter('''from dash_core_components import Slider

Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=5,
        id='section2-slider-2'
    ),
    html.Div('''Heads up!
    Slider and RangeSlider requires some special CSS to render properly.
    Include this CSS by `Link`'ing it in your app's `layout`:
    ''', style={'marginTop': 40}),
    dcc.SyntaxHighlighter('''import dash_html_components as html
from dash_core_components import Slider

app.layout = html.Div([
    html.Link(
        rel="stylesheet",
        href="https://cdn.rawgit.com/chriddyp/abcbc02565dd495b676c3269240e09ca"
             "/raw/816de7d5c5d5626e3f3cac8e967070aa15da77e2/rc-slider.css"
    ),

    # And then the rest of your dash layout:
    Slider(...)
])''', language='python'),
    html.Hr(),
    html.Strong('RangeSlider'),
    dcc.SyntaxHighlighter('''from dash_core_components import RangeSlider

RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.RangeSlider(
        count=1,
        min=-5,
        max=10,
        step=0.5,
        value=[-3, 7],
        id='section2-rangeslider-1'
    ),

    dcc.SyntaxHighlighter('''from dash_core_components import RangeSlider

RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.RangeSlider(
        marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
        min=-5,
        max=6,
        value=[-3, 4],
        id='section2-rangeslider-2'
    ),

    html.Hr(),
    html.Strong('Input'),
    dcc.SyntaxHighlighter('''from dash_core_components import Input

Input(
    placeholder="Enter a value...",
    value=""
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Input(
        placeholder="Enter a value...",
        value="",
        id='section2-input'
    ),

    html.Hr(),
    html.Strong('Checkboxes'),
    dcc.SyntaxHighlighter('''from dash_core_components import Checklist

Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF'],
        id='section2-checklist-1'
    ),

    dcc.SyntaxHighlighter('''from dash_core_components import Checklist

Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF'],
        labelStyle={'display': 'inline-block'},
        id='section2-checklist-2'
    ),


    html.Hr(),
    html.Strong('Radio Items'),
    dcc.SyntaxHighlighter('''from dash_core_components import RadioItems

RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        id='section2-radioitems-1'
    ),

    dcc.SyntaxHighlighter('''from dash_core_components import RadioItems

RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        id='section2-radioitems-2'
    ),


    html.Hr(),
    html.Strong('Graphs'),
    dcc.SyntaxHighlighter('''from dash_core_components import Graph
import plotly.graph_objs as go

Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='lines'),
            go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
        ],
        layout=go.Layout(
            title='Quarterly Results',
            showlegend=False,
            margin=go.Margin(l=20, r=0, t=40, b=20)
        )
    ),
    style={'height': 300},
    id="my-graph"
)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='lines'),
                go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
            ],
            layout=go.Layout(
                title='Quarterly Results',
                showlegend=False,
                margin=go.Margin(
                    l=20, r=0, t=40, b=20
                )
            )
        ),
        style={'height': 300},
        id="my-graph"
    ),

    html.Div(style={'marginBottom': 50}),

    html.Div(id='hidden', style={'display': 'none'})
])


# add dependencies to all of section2's elements so that they become controlled
@app.react('hidden', [k for k in layout.keys() if k != 'hidden'])
def update_hidden_div(*args):
    return {'content': json.dumps(args, indent=4)}
