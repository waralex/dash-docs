# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json
import styles

from server import app

layout = html.Div(children=[
    html.H1('Dash Core Components'),

    html.Div('''
        Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the authors of dash,
        is available in the `dash-core-components` library. Let's take a look:
    '''),

    html.Hr(),
    html.Strong('Dropdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], value="MTL", id='section2-dropdown-1'),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
)''', language='python', customStyle=styles.code_container),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], multi=True, value="MTL", id='section2-dropdown-2'),

    html.Hr(),
    html.Strong('Slider'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
)''', language='python', customStyle=styles.code_container),
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        value=-3,
        id='section2-slider-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)''', language='python', customStyle=styles.code_container),
    html.Div(dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=5,
        id='section2-slider-2'
    ), style={'padding': 20}),
    html.Hr(),
    html.Strong('RangeSlider'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)''', language='python', customStyle=styles.code_container),
    dcc.RangeSlider(
        count=1,
        min=-5,
        max=10,
        step=0.5,
        value=[-3, 7],
        id='section2-rangeslider-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)''', language='python', customStyle=styles.code_container),
    html.Div(dcc.RangeSlider(
        marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
        min=-5,
        max=6,
        value=[-3, 4],
        id='section2-rangeslider-2'
    ), style={'padding': 20}),

    html.Hr(),
    html.Strong('Input'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)''', language='python', customStyle=styles.code_container),
    dcc.Input(
        placeholder="Enter a value...",
        value="",
        type='text',
        id='section2-input'
    ),

    html.Hr(),
    html.Strong('Checkboxes'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)''', language='python', customStyle=styles.code_container),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF'],
        id='section2-checklist-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),
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
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        id='section2-radioitems-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),
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
    html.Strong('Markdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

    dcc.Markdown(\'\'\'
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
    \'\'\')
    '''.replace('  ', ''),
        customStyle=styles.code_container,
        language='python'
    ),

    dcc.Markdown('''
    #### Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.'''.replace('  ', ''),
    containerProps={'className': 'example-container'}),

    html.Hr(),
    html.Strong('Graphs'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
import plotly.graph_objs as go

dcc.Graph(
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
    id='my-graph'
)''', language='python', customStyle=styles.code_container),
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


for k in layout.keys():
    if k == 'hidden':
        continue

    if k in ['section2-rangeslider-2', 'section2-slider-2']:
        layout[k] = html.Div(layout[k],
            className="example-container",
            style=dict({'padding': '25px'})
        )

    else:
        layout[k] = html.Div(layout[k], className="example-container")

# add dependencies to all of section2's elements so that they become controlled
@app.callback(
    Output('hidden', 'children'),
    [Input(k, 'value' if 'checklist' not in k else 'values')
     for k in layout.keys() if k != 'hidden'])
def update_hidden_div(*args):
    return ''
