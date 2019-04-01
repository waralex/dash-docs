import dash
import dash_bio as dashbio
import dash_html_components as html
import dash_core_components as dcc

import sys

try:
    import urllib.request as urlreq
except ImportError:
    import urllib2 as urlreq

import dash_bio.utils.xyz_reader as xyz_reader

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/speck_caffeine.xyz").read()

if sys.version_info >= (3, 0):
    data = data.decode("utf-8")

data = xyz_reader.read_xyz(data_string=data)

app.layout = html.Div([
    dcc.Dropdown(
        id='speck-preset-views',
        options=[
            {'label': 'Default', 'value': 'default'},
            {'label': 'Ball and stick', 'value': 'stickball'}
        ],
        value='default'
    ),
    dashbio.Speck(
        id='my-speck',
        scrollZoom=True,
        view={'resolution': 400},
        data=data
    ),
    html.Div(id='speck-output')
])


@app.callback(
    dash.dependencies.Output('my-speck', 'presetView'),
    [dash.dependencies.Input('speck-preset-views', 'value')]
)
def update_preset_view(preset_name):
    return preset_name


if __name__ == '__main__':
    app.run_server(debug=True)
