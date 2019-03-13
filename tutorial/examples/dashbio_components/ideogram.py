import dash
import dash_bio as dashbio
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dashbio.Ideogram(
        id="my-dashbio-ideogram",
        dataDir="https://unpkg.com/ideogram@1.3.0/"
        "dist/data/bands/native/",
        organism="human",
        assembly="GRCh37",
        chromosomes=['X', 'Y'],
        orientation="horizontal",
        showBandLabels=True,
        chrHeight=400,
        rotatable=False,
        annotationsPath='https://eweitz.github.io/ideogram/data/annotations/SRR562646.json'
    ),
    html.Div(id='ideogram-output')
])


@app.callback(
    dash.dependencies.Output('ideogram-output', 'children'),
    [dash.dependencies.Input('my-dashbio-ideogram', 'annotationsData')]
)
def show_annotations(annot):
    if annot is None or len(annot) == 0:
        return ''
    annot_info = annot.split('<br>')
    gene_name = annot_info[0]
    gene_location_info = annot_info[1].split(':')
    chromosome_name = gene_location_info[0].replace('chr', '')
    basepair_location = gene_location_info[1]

    return [
        "Hover information:",
        html.Div('Gene name: {}'.format(gene_name)),
        html.Div('Location: chromosome {}, base pairs {}'.format(
            chromosome_name,
            basepair_location
        ))
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
