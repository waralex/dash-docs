from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
from pyorbital.orbital import Orbital
import datetime
import plotly

import styles
from server import app

layout = [dcc.Markdown('''
## Live Updating Graphs

Components in dash usually update through user interaction:
selecting a dropdown, dragging a slider, hovering over points.

If you're building an application for monitoring, you may want to update
components in your application every few seconds or minutes.

The `dash_core_components.Interval` element allows you to update components
on a predefined interval.

This example pulls data from live satellite feeds and updates the graph
and the text every second.
'''),

dcc.SyntaxHighlighter('''import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import datetime
import plotly

# pip install pyorbital
from pyorbital.orbital import Orbital

satellite = Orbital('TERRA')

app.layout = html.Div(
    html.Div([
        html.H4('TERRA Satellite Live Feed'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000 # in milliseconds
        )
    ])
)

# The `dcc.Interval` component emits an event called "interval"
# every `interval` number of milliseconds.
# Subscribe to this event with the `events` argument of `app.callback`
@app.callback(Output('live-update-text', 'content'),
              events=[Event('interval-component', 'interval')])
def update_metrics():
    lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Longitude: {0:.2f}'.format(lon), style=style),
        html.Span('Latitude: {0:.2f}'.format(lat), style=style),
        html.Span('Altitude: {0:0.2f}'.format(alt), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    satellite = Orbital('TERRA')
    data = {
        'time': [],
        'Latitude': [],
        'Longitude': [],
        'Altitude': []
    }

    # Collect some data
    for i in range(120):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        lon, lat, alt = satellite.get_lonlatalt(
            time
        )
        data['Longitude'].append(lon)
        data['Latitude'].append(lat)
        data['Altitude'].append(alt)
        data['time'].append(time)

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(
        rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05
    )
    fig['layout']['margin'] = {
        'l': 20, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 1, 'y': 1, 'xanchor': 'right'}
    for i, name in enumerate(['Longitude', 'Latitude', 'Altitude']):
        fig.append_trace({
            'x': data['time'],
            'y': data[name],
            'name': name,
            'mode': 'lines',
            'type': 'scatter',
            'line': {'width': 0.5}
        }, i+1, 1)
    return fig


''', language='python',
     customStyle={'borderLeft': 'thin solid lightgrey'}),

html.Div(
    html.Div([
        html.H4('TERRA Satellite Live Feed'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000
        )
    ]),
    style=styles.example_container
)
]



satellite = Orbital('TERRA')
@app.callback(Output('live-update-text', 'content'),
              events=[Event('interval-component', 'interval')])
def update_metrics():
    lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Longitude: {0:.2f}'.format(lon), style=style),
        html.Span('Latitude: {0:.2f}'.format(lat), style=style),
        html.Span('Altitude: {0:0.2f}'.format(alt), style=style)
    ]


@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    satellite = Orbital('TERRA')
    data = {
        'time': [],
        'Latitude': [],
        'Longitude': [],
        'Altitude': []
    }
    for i in range(120):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        lon, lat, alt = satellite.get_lonlatalt(
            time
        )
        data['Longitude'].append(lon)
        data['Latitude'].append(lat)
        data['Altitude'].append(alt)
        data['time'].append(time)

    fig = plotly.tools.make_subplots(
        rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05
    )
    fig['layout']['margin'] = {
        'l': 20, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 1, 'y': 1, 'xanchor': 'right'}
    for i, name in enumerate(['Longitude', 'Latitude', 'Altitude']):
        fig.append_trace({
            'x': data['time'],
            'y': data[name],
            'name': name,
            'mode': 'lines',
            'type': 'scatter',
            'line': {'width': 0.5}
        }, i+1, 1)
    return fig
