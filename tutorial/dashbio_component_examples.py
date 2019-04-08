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
Clustergram = create_doc_page(
    examples, component_names, 'clustergram', component_examples=[
        {
            'param_name': 'Heatmap color scale',
            'description': 'Change the color scale by specifying values and colors.',
            'code': '''import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    color_map= [
        [0.0, '#880088'],
        [0.25, '#FFF0FF'],
        [0.5, '#FFFFFF'],
        [0.75, '#000FFF'],
        [1.0, '#0000FF']
    ]
)

dcc.Graph(figure=clustergram)'''
        },

        {
            'param_name': 'Dendrogram Cluster Colors/Line Widths',
            'description': 'Change the colors of the dendrogram traces that \
            are used to represent clusters, and configure their line widths.',
            'code': '''import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    color_list={
        'row': ['#AA8822', '#AA0055', '#00AA00'],
        'col': ['#00AADD', '#FF0F0F'],
        'bg': '#004444'
    },
    line_width=2
)

dcc.Graph(figure=clustergram)'''
        },

        {
            'param_name': 'Relative Dendrogram Size',
            'description': 'Change the relative width and height of, respectively, the row and column \
            dendrograms compared to the width and height of the heatmap.',
            'code': '''import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    display_ratio=[0.5, 0.7]
)

dcc.Graph(figure=clustergram)'''
        },
        {
            'param_name': 'Hidden Labels',
            'description': 'Hide the labels along one or both dimensions.',
            'code': '''import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    hide_labels='row'
)

dcc.Graph(figure=clustergram)'''
        },
        {
            'param_name': 'Annotations',
            'description': 'Annotate the clustergram by highlighting specific clusters.',
            'code': '''import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    hide_labels='row',
    col_group_marker=[
        {'group': 1, 'annotation': 'largest column cluster', 'color': 'orange'}
    ],
    row_group_marker=[
        {'group': 2, 'annotation': 'smallest', 'color': 'purple'},
        {'group': 1, 'annotation': 'largest', 'color': 'yellow'}
    ]
)

dcc.Graph(figure=clustergram)'''
        }
    ]
)

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
