import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles

import dash_bio

from tutorial.utils.dashbio_docs import generate_docs

dashbio_library_heading = dcc.Markdown('''
    # Dash Bio

    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and JavaScript.

    Dash Bio is a suite of bioinformatics components that make it simpler to
    analyze and visualize bioinformatics data and interact with it in a Dash
    application.

    The source is on GitHub at [plotly/dash-bio](https://github.com/plotly/dash-bio).

    These docs are using version {}.
    '''.replace('    ', '').format(dash_bio.__version__)
)

dashbio_install_instructions = dcc.SyntaxHighlighter('''>>> import dash_bio
    >>> print(dash_bio.__version__)
    {}'''.replace('    ', '').format(dash_bio.__version__),
    customStyle=styles.code_container)


dashbio_components = {

    'AlignmentChart': {
        'description': '''An alignment chart.''',
        'datafile': {
            'name': 'alignment_viewer_p53.fasta',
            'parameter': 'data'
        },
        'iframe_location': 'https://dash-playground.plotly.host/dash-alignment-chart-demo/'
    },

    'Circos': {
        'description': '''A circular ideogram with arcs representing links between genes.''',
        'library_imports': [
            ['json', 'json'],
        ],
        'datafile': {
            'name': 'circos_graph_data.json'
        },
        'params': {
            'layout': 'circos_graph_data[\'GRCh37\']',
            'tracks': '''[{
  'type': 'CHORDS',
  'data': circos_graph_data['chords'],
  'opacity': 0.7,
  'color': {'name': 'color'},
  'config': {
    'tooltipContent': {
      'source': 'source',
      'sourceID': 'id',
      'target': 'target',
      'targetID': 'id',
      'targetEnd': 'end'
    }
  }
}]'''
        },
        'setup_code': '''circos_graph_data = json.loads(data)'''
    },

    'Clustergram': {
        'description': '''A heatmap with dendrograms to display clustering of
        data such as gene expression data.''',
        'default_id': False,
        'library_imports': [
            ['pandas', 'pd'],
            ['dash_core_components', 'dcc']
        ],
        'params': {
            'data': 'data',
            'columnLabels': 'list(df.columns.values)',
            'rowLabels': 'list(df.index)',
            'hideLabels': '[\'row\']',
            'height': '800',
            'width': '600'
        },
        'component_wrap': 'dcc.Graph(figure=_[0])',
        'setup_code': '''df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
        sep='\t', skiprows=4).set_index('model')
data = df.values''',
        'iframe_location': 'https://dash-playground.plotly.host/dash-clustergram-demo/'
    },

    'SequenceViewer': {
        'description': '''A sequence viewer.''',
        'params': {
            'sequence': '\"MALWMRLLPLLALLALWGPDPAAAFVN\
            QHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLA\
            LEGSLQKRGIVEQCCTSICSLYQLENYCN\"'
        }
    },

    'Speck': {
        'description': '''A 3D WebGL molecule viewer.''',
        'params': {
            'view': '{\'resolution\': 600}'
        },
        'datafile': {
            'name': 'speck_methane.xyz',
            'parameter': 'data'
        },
        'library_imports': [
            ['dash_bio.utils.xyz_reader', 'xyz_reader']
        ],
        'setup_code': '''data = xyz_reader.read_xyz(data_string=data)''',
        'iframe_location': 'https://dash-playground.plotly.host/dash-speck-demo/'
    }
}

layout_children = generate_docs(
    'dash_bio',
    'dashbio',
    dashbio_library_heading,
    dashbio_install_instructions,
    dashbio_components
)

layout = html.Div(className="gallery", children=layout_children)
