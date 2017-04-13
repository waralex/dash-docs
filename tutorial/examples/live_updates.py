import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import datetime
import plotly

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


if __name__ == '__main__':
    app.run_server(debug=True)
