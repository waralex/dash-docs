# -*- coding: utf-8 -*-
import dash
from dash.react import Dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask
import json
import plotly.graph_objs as go

server = Flask(__name__)
app = Dash(__name__, server=server)

head = html.Div([
    html.Link(
        rel="stylesheet",
        href="https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75"
             "/raw/d4f178bc09f253251135aeb2141aa077300d1b3f/dash.css"
    ),
    html.Link(
        rel="stylesheet",
        href="https://unpkg.com/react-select@1.0.0-rc.3/dist/react-select.css"
    ),
    html.Link(
        rel="stylesheet",
        href="https://cdn.rawgit.com/chriddyp/abcbc02565dd495b676c3269240e09ca"
             "/raw/816de7d5c5d5626e3f3cac8e967070aa15da77e2/rc-slider.css"
    ),

    html.H2('Dash Developer Preview'),

    html.Div('''Dash is a productive python framework for building web applications.

    Written on top of Plotly.js and React.js,
    Dash is ideal for data visualization with highly custom user interfaces.'''),

    html.Div('''This is an exclusive developer preview of Dash.
    Dash is currently in an unreleased and unannounced. Call it a Beta.
    Please do not share Dash without Plotly's constent.'''),

    html.Div('''The core functionality of Dash will be open sourced.
    For enterprises, Plotly offers a platform for
    deploying, orchestrating, and permissioning dash apps behind
    your firewall. If you're interested,
    please get in touch at <sales@plot.ly> to register for early access.'''),

    html.Div('''Let's get started!'''),

    html.Hr(),

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
from dash_core_components import Dropdown, Graph
from dash_html_components import Div, H3, Link

from plotly import graph_objs as go
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.react.Dash('Hello World')

# Describe the layout, or the UI, of the app
app.layout = Div([
    # Include Dropdown's CSS - Won't be necessary in upcoming version
    Link(
        rel="stylesheet",
        href="https://unpkg.com/react-select@1.0.0-rc.3/dist/react-select.css"
    ),

    H3('Hello World'),
    Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    Graph(id='my-graph')
])

# Register a callback to update 'my-graph' component when 'my-dropdown' changes
@app.react('my-graph', ['my-dropdown'])
def update_graph(dropdown_properties):
    df = web.DataReader(
        dropdown_properties['value'], 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return {
        'figure': go.Figure(
            data=[{
                'x': df.index,
                'y': df.Close
            }]
        )
    }

# Boiler plate
app.component_suites=[
    'dash_core_components',
    'dash_html_components'
]

# Run the server
if __name__ == '__main__':
    app.server.run(debug=True)
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
    html.Hr(),
    html.Div(style={'marginBottom': '100px'})
])

# Section 1 - HTML Attributes
section1 = html.Div([

    html.H4('Section 1 - HTML Attributes'),
    html.Div('''
    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and Javascript.

    Instead of writing HTML or using an HTML templating engine,
    you compose your layout using Python structures.
    HTML in dash looks like this:
    '''),
    dcc.SyntaxHighlighter('''import dash_html_components as html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P('This conversion happens behind the scenes by Dash\'s Javascript front-end')
    ])
])''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div(
        'which gets converted (behind the scenes) into the '
        'following HTML in your web-app:'
    ),
    dcc.SyntaxHighlighter('''<div>
    <h1>Hello</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's Javascript front-end</p>
    </div>
</div>''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div("If you're not comfortable with HTML, don't worry! "
             "You can get 95% of the way there with just a few elements. "
             "View the Component Library in the appendix of these docs "
             "to see what these components look like."),

    dcc.SyntaxHighlighter('''from dash_html_components import Div, H2, Span, Img

Div([
    # H1 - H6 are for headings
    H2('Dash App'),

    # Div is generic - use it to encapsulate other components or just for text
    Div('A description of your dash app'),

    # Embed images with the Img tag and the `src` key
    Img(src="https://plot.ly/~chris/1638.png")
])
''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),

    html.Div('HTML elements have properties like `style`, `class`, and `id`.'
             'All of these attributes are available in the Python classes.'),
    html.Div("The HTML elements and Dash classes are mostly the same. "
             "Here are a few key differences:"),
    html.Li('The `style` property is a dictionary'),
    html.Li('Properties in the `style` dictionary are camelCased'),
    html.Li('The `class` key is renamed as `className`'),
    html.Li('Style properties in pixel units can be supplied as just numbers without the `px` unit'),
    html.Div("Let's take a look at an example."),
    dcc.SyntaxHighlighter('''from dash_html_components import Div

Div([
    Div('Example Div', style={'color': 'blue', fontSize: 14}),
    P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})
''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div("That dash code will end up getting rendered as this HTML markup:"),
    dcc.SyntaxHighlighter('''
<div style="margin-bottom: 50px; margin-top: 25px;">

    <div style="color: blue; font-size: 14px">
        Example Div
    </div>

    <p class="my-class", id="my-p-element">
        Example P
    </p>

</div>
''', language='html', customStyle={'borderLeft': 'thin solid lightgrey'})
])

# Section 2 - Core Components
section2 = html.Div([
    html.H4('Section 2 - Supercharged Components'),

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
@app.react('hidden', [k for k in section2.keys() if k != 'hidden'])
def update_hidden_div(*args):
    return {'content': json.dumps(args, indent=4)}


# Section 3 - Basic Callbacks
section3 = html.Div([
    html.H4('Section 3 - Interactivity with Callbacks'),
    html.Div('''
    The heart and soul of dash is providing an easy way to bind Python
    callbacks to web interfaces.
    '''),
    html.Div('''
    With Dash's callback decorators, you can update certain components
    when other components change values. Here's a practical example.
    View the interactive app below the code.
    '''),
    dcc.SyntaxHighlighter('''
import dash
from dash_core_components import Dropdown, Graph
from dash_html_components import Div

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.react.Dash('')

# Describe the layout of the app
app.layout = Div([
    Dropdown(
        id='section3-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    Graph(id='section3-graph')
])

# Bind a callback to a dash app with dash's "react" decorator
# The first argument is the ID of the "target" component, the component we want to update.
# The second argument is a list of components that this "target" component depends on.
# Whenever these components change values, e.g. when a dropdown gets fired, dash will
# call this function and provide you with the component's properties or attributes.
# This includes the newly selected value of the dropdown.
# The function will return a new set of properties that will get merged into the target component.
# In this case, the target component is a Graph, so we'll return a `figure` property.
@app.react('section3-graph', ['section3-dropdown'])
def update_graph(dropdown_properties):
    # Get the value of the dropdown
    selected_dropdown_value = dropdown_properties['value']

    # Get some new data from Yahoo finance with Pandas
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    # Construct a figure and return it to dash's front-end
    return {
        'figure': go.Figure(
            data=[{
                'x': df.index,
                'y': df.Close
            }]
        )
    }''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div('This code will generate an app like this:'),

    html.Div([
        dcc.Dropdown(
            id='section3-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Graph(id='section3-graph')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'})
])

from pandas_datareader import data as web
from datetime import datetime as dt
@app.react('section3-graph', ['section3-dropdown'])
def update_graph(dropdown_properties):
    selected_dropdown_value = dropdown_properties['value']
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return {
        'figure': go.Figure(
            data=[{
                'x': df.index,
                'y': df.Close
            }],
            layout=go.Layout(
                margin=go.Margin(
                    l=30,
                    r=0,
                    b=40,
                    t=20
                )
            )
        )
    }


# Section 4 - Callbacks With Dependencies
section4 = html.Div([
    # html.H4('Section 4 - Advanced Callbacks')
])

# Section 4 - Callbacks With Dependencies
section5 = html.Div([
    html.H4('Section 5 - Advanced DOM Manipulation')
])


# Section 5 - HTML Component Appendix
section5 = html.Div([
    html.Div(style={'marginTop': '60px'}),

    html.H3('Appendix - Common HTML Components'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H1("H1 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H1('H1 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H2("H2 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H2('H2 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H3("H3 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H3('H3 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H4("H4 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H4('H4 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H5("H5 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H5('H5 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H6("H6 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H6('H6 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.Div("Generic Div Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div('Generic Div Element')
])

# Run the app

app.layout = html.Div([
    head, section1, section2, section3, section4, section5
], className="container", style={'fontSize': '1.7rem'})

app.component_suites = [
    'dash_html_components',
    'dash_core_components'
]

if __name__ == '__main__':
    app.server.run(debug=True)
