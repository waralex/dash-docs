import dash_core_components as dcc

# examples = [load_example(s) for s in [
#     'tutorial/examples/live_updates.py'
# ]]


layout = [dcc.Markdown('''
# Live Updating Components

## The `dash_core_components.Interval` component

Components in Dash usually update through user interaction:
selecting a dropdown, dragging a slider, hovering over points.

If you're building an application for monitoring, you may want to update
components in your application every few seconds or minutes.

The `dash_core_components.Interval` element allows you to update components
on a predefined interval. The `n_intervals` property is an integer that is
automatically incremented every time `interval` milliseconds pass.
You can listen to this variable inside your app's `callback` to fire
the callback on a predefined interval.

This example pulls data from live satellite feeds and updates the graph
and the text every second.
'''),
    dcc.SyntaxHighlighter('''import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
    
# pip install pyorbital
from pyorbital.orbital import Orbital
satellite = Orbital('TERRA')

app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        html.H4('TERRA Satellite Live Feed'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Longitude: {0:.2f}'.format(lon), style=style),
        html.Span('Latitude: {0:.2f}'.format(lat), style=style),
        html.Span('Altitude: {0:0.2f}'.format(alt), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    satellite = Orbital('TERRA')
    data = {
        'time': [],
        'Latitude': [],
        'Longitude': [],
        'Altitude': []
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        lon, lat, alt = satellite.get_lonlatalt(
            time
        )
        data['Longitude'].append(lon)
        data['Latitude'].append(lat)
        data['Altitude'].append(alt)
        data['time'].append(time)

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': data['time'],
        'y': data['Altitude'],
        'name': 'Altitude',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['Longitude'],
        'y': data['Latitude'],
        'text': data['time'],
        'name': 'Longitude vs Latitude',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 1)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

''',
        language='python',
        customStyle={'borderLeft': 'thin solid lightgrey'}
    ),

dcc.Markdown('''

***

## Updates on Page Load

By default, Dash apps store the `app.layout` in memory. This ensures that the
`layout` is only computed once, when the app starts.

If you set `app.layout` to a function, then you can serve a dynamic layout
on every page load.

For example, if your `app.layout` looked like this:

```
import datetime

import dash
import dash_html_components as html

app.layout = html.H1('The time is: ' + str(datetime.datetime.now()))

if __name__ == '__main__':
    app.run_server()
```

then your app would display the time when the app was started.

If you change this to a function, then a new `datetime` will get computed
everytime you refresh the page. Give it a try:

```
import datetime

import dash
import dash_html_components as html

def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server()
```

You can combine this with [time-expiring caching](/performance) and serve
a unique `layout` every hour or every day and serve the computed `layout`
from memory in between.
'''),

          dcc.Markdown('''

***

## Dynamically Create Layout for Multi-page App Validation

Dash applies validation to your callbacks, which performs checks such as 
validating the types of callback arguments and checking to see whether the 
specified Input and Output components actually have the specified properties. 

For full validation, all components within your callback must therefore appear 
in the initial layout of your app, and you will see an error if they do not.
However, in the case of more complex Dash apps that involve dynamic modification 
of the layout (such as multi-page apps), not every component appearing in your 
callbacks will be included in the initial layout.

Since this validation is done before flask has any request context, you can create 
a layout function that checks `flask.has_request_context()` and returns a complete
layout to the validator if there is no request context and returns the incomplete
index layout otherwise:
'''),
    dcc.SyntaxHighlighter(
        '''
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import flask

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

layout_index = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div(id='tabs-content')])

layout_tab_1 = html.Div([
    html.H3('Tab content 1'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

layout_tab_2 = html.Div([
    html.H2('Tab 2'),
    dcc.Dropdown(
        id='tab-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='tab-2-display-value')])


def serve_layout():
    if flask.has_request_context():
        return layout_index
    return html.Div([
        layout_index,
        layout_tab_1,
        layout_tab_2,
    ])


app.layout = serve_layout


# Index callbacks
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return layout_tab_1
    elif tab == 'tab-2':
        return layout_tab_2


# Tab 1 Callbacks
@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    return ('The Button has been pressed {} times,'
            'Input 1 is "{}",'
            'and Input 2 is "{}"').format(n_clicks, input1, input2)


# Tab 2 Callbacks
@app.callback(dash.dependencies.Output('tab-2-display-value', 'children'),
              [dash.dependencies.Input('tab-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
    
        ''',
        language='python',
        customStyle={'borderLeft': 'thin solid lightgrey'}
    )]
