# -*- coding: utf-8 -*-
from tutorial import tools
from tutorial.utils.dashbio_docs import create_doc_page, get_component_names, create_examples

component_names = get_component_names('dash_bio')

examples = {
    'alignment-chart': tools.load_example(
        'tutorial/examples/dashbio_components/alignment_chart.py'),
    'sequence-viewer': tools.load_example(
        'tutorial/examples/dashbio_components/sequence_viewer.py'),
    'clustergram': tools.load_example(
        'tutorial/examples/dashbio_components/clustergram.py'),
    'speck': tools.load_example(
        'tutorial/examples/dashbio_components/speck.py'),
    'circos': tools.load_example(
        'tutorial/examples/dashbio_components/circos.py'),
    'ideogram': tools.load_example(
        'tutorial/examples/dashbio_components/ideogram.py'),
    'molecule-3d-viewer': tools.load_example(
        'tutorial/examples/dashbio_components/molecule_3d_viewer.py'),
    'needle-plot': tools.load_example(
        'tutorial/examples/dashbio_components/needle_plot.py'),
    'manhattan-plot': tools.load_example(
        'tutorial/examples/dashbio_components/manhattan_plot.py'),
    'volcano-plot': tools.load_example(
        'tutorial/examples/dashbio_components/volcano_plot.py'),
    'onco-print': tools.load_example(
        'tutorial/examples/dashbio_components/oncoprint.py')
}


# AlignmentChart/AlignmentViewer
AlignmentChart = create_doc_page(
    examples, component_names, 'alignment-chart', component_examples=[

        {
            'param_name': 'Color Scales',
            'description': 'Change the colors used for the heatmap.',
            'code': '''from six.moves.urllib import request as urlreq
import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode('utf-8')

dashbio.AlignmentChart(
    data=data,
    colorscale='hydro',
    conservationcolorscale='blackbody'
)

'''
        },
        {
            'param_name': 'Show/hide Barplots',
            'description': 'Enable or disable the secondary bar plots for gaps and conservation.',
            'code': '''from six.moves.urllib import request as urlreq
import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode('utf-8')

dashbio.AlignmentChart(
    data=data,
    showconservation=False,
    showgap=False
)'''
        },

        {
            'param_name': 'Tile Size',
            'description': 'Change the height and/or width of the tiles.',
            'code': '''from six.moves.urllib import request as urlreq
import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode('utf-8')

dashbio.AlignmentChart(
    data=data,
    tilewidth=50
)'''
        },
        {
            'param_name': 'Consensus Sequence',
            'description': 'Toggle the display of the consensus sequence at the bottom of the heatmap.',
            'code': '''from six.moves.urllib import request as urlreq
import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode('utf-8')

dashbio.AlignmentChart(
    data=data,
    showconsensus=False
)'''
        }
    ]
)


# Circos
Circos = create_doc_page(
    examples, component_names, 'circos', component_examples=[
        {
            'param_name': 'Inner and Outer Radii',
            'description': 'Change the inner and outer radii of your Circos graph.',
            'code': '''import json
from six.moves.urllib import request as urlreq
import dash_bio as dashbio

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/circos_graph_data.json').read()
circos_graph_data = json.loads(data)

dashbio.Circos(
    layout=circos_graph_data['GRCh37'],
    tracks=[{
        'type': 'CHORDS',
        'data': circos_graph_data['chords']
    }],
    config={
        'innerRadius': 40,
        'outerRadius': 200
    }
)'''
        },
    ]
)

# Clustergram
Clustergram = create_doc_page(examples, component_names, 'clustergram')

# Ideogram
Ideogram = create_doc_page(examples, component_names, 'ideogram')

# ManhattanPlot
ManhattanPlot = create_doc_page(examples, component_names, 'manhattan-plot')

# Molecule3dViewer
Molecule3dViewer = create_doc_page(examples, component_names, 'molecule-3d-viewer')

# NeedlePlot
NeedlePlot = create_doc_page(examples, component_names, 'needle-plot')

# Oncoprint
Oncoprint = create_doc_page(examples, component_names, 'onco-print')

# SequenceViewer
SequenceViewer = create_doc_page(examples, component_names, 'sequence-viewer')

# Speck
Speck = create_doc_page(examples, component_names, 'speck')

# VolcanoPlot
VolcanoPlot = create_doc_page(examples, component_names, 'volcano-plot')
