import dash
import dash_bio as dashbio
import dash_html_components as html
import tempfile as tf
import json
import dash_bio.utils.pdb_parser as parser
import dash_bio.utils.styles_parser as sparser

try:
    import urllib.request as urlreq
except ImportError:
    import urllib2 as urlreq

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/molecule3d_2mru.pdb').read()

tmp = tf.NamedTemporaryFile(suffix='.pdb', delete=False, mode='w+')

try:
    tmp.write(data)
except TypeError:
    tmp.write(data.decode())

fname = tmp.name
tmp.close()

model_data = json.loads(parser.create_data(fname))
styles_data = json.loads(sparser.create_style(fname, 'cartoon', 'residue'))

app.layout = html.Div([
    dashbio.Molecule3dViewer(
        id='my-dashbio-molecule3d',
        styles=styles_data,
        modelData=model_data,
        backgroundOpacity='0'
    ),
    "Selection data",
    html.Hr(),
    html.Div(id='molecule3d-output')
])


@app.callback(
    dash.dependencies.Output('molecule3d-output', 'children'),
    [dash.dependencies.Input('my-dashbio-molecule3d', 'selectedAtomIds')]
)
def show_selected_atoms(atom_ids):
    if atom_ids is None or len(atom_ids) == 0:
        return 'No atoms have been selected. Click somewhere on the molecular structure to select an atom.'
    return [html.Div([
        html.Div('Element: {}'.format(model_data['atoms'][atm]['element'])),
        html.Div('Chain: {}'.format(model_data['atoms'][atm]['chain'])),
        html.Div('Residue name: {}'.format(model_data['atoms'][atm]['residue_name'])),
        html.Br()
    ]) for atm in atom_ids]


if __name__ == '__main__':
    app.run_server(debug=True)
