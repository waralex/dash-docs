import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output, Event

import styles
from server import app

layout = html.Div(content=[
    html.H1('Interactivity with Callbacks'),
    html.Div('''
    The heart and soul of dash is providing an easy way to bind Python
    callbacks to web interfaces.
    '''),
    html.Div('''
    With Dash's callback decorators, you can update certain components
    when other components change values. Here's a practical example.
    View the interactive app below the code.
    '''),
    dcc.SyntaxHighlighter('''import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('')

# Describe the layout of the app
app.layout = html.Div([
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
])

# Bind a function to a dash app with dash's "callback" decorator
# This "callback" decorator describes how input components should
# update output components.
#
# The first argument is an object that describes the component
# containing the ID  of the output component ("section3-graph")
# and the particular property of that component that this function
#  should update ("figure").
#
# The second argument is a list of Input components. Similarly,
# the first argument is the ID of the component ("section3-dropdown")
# and the second argument is property of the input component ("value").
#
# Whenever the "value" property changes in the application, for example
# when you select a new dropdown item, this function will get called
# with that value. Dash expects that this function will return an
# object that will update whatever output component that you subscribed to,
# in this case a "figure" object.
@app.callback(
    Output('section3-graph', 'figure'),
    [Input('section3-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    # Get some new data from Yahoo finance with Pandas
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    # Construct a figure and return it to dash's front-end
    # This will end up updating the Graph's `figure` property
    # in the front-end of the application.
    return go.Figure(
        data=[{
            'x': df.index,
            'y': df.Close
        }]
    )


# Run the server
if __name__ == '__main__':
    app.server.run(debug=True)''',
    language='python',
    customStyle=styles.code_container),
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
    ], style=styles.example_container)
])


@app.callback(Output('section3-graph', 'figure'),
              [Input('section3-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return go.Figure(
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



layout.content.extend([
    dcc.Markdown('''
## Multiple Inputs

Let's extend this example by including
a secondary input element that controls
which variable we should plot.

Dash apps are "reactive" which means that
whenever values change in the front-end,
the callback functions will get called
automatically.

'''),
    dcc.SyntaxHighlighter('''import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('')

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-ticker-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Dropdown(
        id='column-selector',
        options=[
            {'label': i, 'value': i} for i in
            ['Open', 'High', 'Low', 'Close', 'High - Low']
        ],
        value='Open',
        style={'display': 'inline-block'}
    ),

    dcc.Graph(id='graph')
])

@app.callback(
    Output('id', 'graph'),
    [Input('stock-ticker-dropdown', 'value'),
     Input('column-selector', 'value')]
)
def update_graph(stock_ticker, column):
    # The order of the inputs in the callback
    # decorator match the order of the input
    # arguments of the function

    df = web.DataReader(
        stock_ticker, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    if column != 'High - Low':
        y = df[column]
    else:
        y = df.High - df.Low

    return go.Figure(
        data=[go.Scatter(x=df.Index, y=y)],
        layout=go.Layout(
            yaxis=go.YAxis(title=column)
        )
    )

''', language='python', customStyle=styles.code_container),
    html.Div([
        dcc.Dropdown(
            id='stock-ticker-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Dropdown(
            id='column-selector',
            options=[
                {'label': i, 'value': i} for i in
                ['Open', 'High', 'Low', 'Close', 'High - Low']
            ],
            value='Open'
        ),
        dcc.Graph(id='section3-multi-dropdowns-graph')
    ], style=styles.example_container)
])

@app.callback(
    Output('section3-multi-dropdowns-graph', 'figure'),
    [Input('stock-ticker-dropdown', 'value'),
     Input('column-selector', 'value')]
)
def update_graph(stock_ticker, column):
    # The order of the inputs in the callback
    # decorator match the order of the input
    # arguments of the function

    df = web.DataReader(
        stock_ticker, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    if column != 'High - Low':
        y = df[column]
    else:
        y = df.High - df.Low

    return go.Figure(
        data=[go.Scatter(x=df.index, y=y)],
        layout=go.Layout(
            yaxis=go.YAxis(title=column),
            margin=go.Margin(
                l=40,
                r=0,
                b=40,
                t=20
            )
        )
    )

layout.content.extend([
    dcc.Markdown('''
## Events and States

Reactive interfaces are great when the callbacks are fast.
As a user, the delay between selected an option in the dropdown
and seeing the graph update is small and the interface feels
snappy.

An alternative to these types of reactive interfaces is subscribing
explicitly to events. Subscribing to events is great when your
callbacks takes at least a couple of seconds to run or when
you would like your users to update a set of controls before showing
them the output.

You can subscribe to event changes with the
`dash.dependencies.Event` object. Most Dash components will have
events that you can subscribe to. To see the available events of any
dash component, either call `help()` or look up a list with the
`available_events` property:

```
>>> print(html.Button.available_events)
['click']

>>> print(dcc.Graph.available_events)
['restyle', 'relayout']
```

In this example, we'll update our graph when we click on the button.
We'll pass in the currently selected values of the dropdowns through
the `state` arguments.

'''),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import State, Event

app = dash.Dash('')

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-ticker-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Dropdown(
        id='column-selector',
        options=[
            {'label': i, 'value': i} for i in
            ['Open', 'High', 'Low', 'Close', 'High - Low']
        ],
        value='COKE',
        style={'display': 'inline-block'}
    ),

    html.Button('Update Graph', id='my-button'),

    dcc.Graph(id='graph')
])


@app.callback(
    Output('id', 'graph'),
    events=[Event('my-button', 'click')]
    state=[State('stock-ticker-dropdown', 'value'),
           State('column-selector', 'value')]
)
def update_graph(stock_ticker, column):
    df = web.DataReader(
        stock_ticker, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    if column != 'High - Low':
        y = df[column]
    else:
        y = df.High - df.Low

    return go.Figure(
        data=[go.Scatter(x=df.Index, y=y)],
        layout=go.Layout(
            yaxis=go.YAxis(title=column)
        )
    )


''', language='python', customStyle=styles.code_container),
    html.Div([
        dcc.Dropdown(
            id='stock-ticker-dropdown-2',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Dropdown(
            id='column-selector-2',
            options=[
                {'label': i, 'value': i} for i in
                ['Open', 'High', 'Low', 'Close', 'High - Low']
            ],
            value='Open'
        ),
        html.Button('Update Graph', id='section3-my-button'),
        dcc.Graph(id='section3-multi-dropdowns-graph-2')
    ], style=styles.example_container)
])


@app.callback(
    Output('section3-multi-dropdowns-graph-2', 'figure'),
    events=[Event('section3-my-button', 'click')],
    state=[
        State('stock-ticker-dropdown-2', 'value'),
        State('column-selector-2', 'value')
    ]
)
def update_graph(stock_ticker, column):
    df = web.DataReader(
        stock_ticker, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    if column != 'High - Low':
        y = df[column]
    else:
        y = df.High - df.Low

    return go.Figure(
        data=[go.Scatter(x=df.index, y=y)],
        layout=go.Layout(
            yaxis=go.YAxis(title=column),
            margin=go.Margin(
                l=40,
                r=0,
                b=40,
                t=20
            )
        )
    )
