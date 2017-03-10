import dash_html_components as html
import dash_core_components as dcc
import datetime
from pyorbital.orbital import Orbital
import os

from server import app

layout = html.Div([
    html.H2('Dash Developer Preview'),

    html.Div('''Dash is a productive python framework for building web applications.

    Written on top of Plotly.js and React.js,
    Dash is ideal for building data visualization apps
    with highly custom user interfaces.
    '''),

    html.Div('''This is an exclusive developer preview of Dash.
    Dash is currently unreleased and unannounced. Call it a Beta.
    Please do not share Dash without Plotly's constent.'''),

    html.Div('''The core functionality of Dash will be open sourced.
    For enterprises, Plotly offers a platform for
    deploying, orchestrating, and permissioning dash apps behind
    your firewall. If you're interested,
    please get in touch at https://plot.ly/products/consulting-and-oem/
    to register for early access.'''),

    html.Hr(),

    html.Div([
        dcc.Dropdown(
            id='satellite-dropdown',
            options=[
                {'label': 'Satellite {}'.format(s), 'value': s}
                for s in [
                    'NOAA 19',
                    'NOAA 15',
                    'TERRA',
                    'NOAA 18',
                    'AQUA',
                    'METOP-B',
                ]
            ],
            value='NOAA 19'
        ),
        html.Div([
            html.Span(i) for i in
            ['  ', '  ', '  ']
        ], id='metrics'),
        dcc.Graph(id='satellite-graph'),
        dcc.Interval(id='satellite-interval', interval=2000)
    ]),

    html.Div('''
        This real-time satellite viewer is an example of an app
        built with Dash.
        Find many more examples like this throughout this user guide.
        Dash is productive: this app weighs in at just 88 lines of pure python.
    '''),

    html.Hr(),

    html.H3('Why Dash?'),
    html.Span('Learn more about dash from our talk at '),
    html.A('Plotcon', href="plotcon.plot.ly", target="_blank"),
    html.Span('.'),
    html.Iframe(
        width="853",
        height="480",
        style={'border': 'none'},
        src="https://www.youtube-nocookie.com/embed/5BAthiN0htc?rel=0"
    )
])


@app.react('metrics',
           ['satellite-dropdown'],
           events=[{'id': 'satellite-interval', 'event': 'setInterval'}])
def update_metrics(dropdown):
    satellite_name = dropdown['value']
    satellite = Orbital(satellite_name)
    lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    style = {'padding': '5px', 'fontSize': '16px'}
    return {
        'content': [
            html.Span('Real Time Longitude: {0:.2f}'.format(lon), style=style),
            html.Span('Latitude: {0:.2f}'.format(lat), style=style),
            html.Span('Altitude: {0:0.2f}'.format(alt), style=style)
        ]
    }


@app.react('satellite-graph', ['satellite-dropdown'])
def update_graph(dropdown):
    satellite_name = dropdown['value']
    satellite = Orbital(satellite_name)
    data = [[], [], [], []]
    for i in range(100):
        time = datetime.datetime.now() - datetime.timedelta(minutes=i)
        lon, lat, alt = satellite.get_lonlatalt(
            time
        )
        data[0].append(lon)
        data[1].append(lat)
        data[2].append(alt)
        if i == 0:
            data[3].append('Less than 60 seconds ago'.format(i))
        else:
            data[3].append('{} minutes ago'.format(i))

    return {'figure': {
        'data': [{
            'lat': data[1],
            'lon': data[0],
            'text': data[3],
            'mode': 'lines+markers',
            'type': 'scattermapbox',
            'marker': {'opacity': 0.9, 'size': 5},
            'line': {'width': 0.5, 'opacity': 0.7}
        }],
        'layout': {
            'mapbox': {
                'accesstoken': os.environ['accesstoken'],
                'style': 'light'
            },
            'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0}
        }
    }}
