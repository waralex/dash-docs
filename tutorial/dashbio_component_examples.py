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
Ideogram = create_doc_page(
    examples, component_names, 'ideogram', component_examples=[
        {
            'param_name': 'Height/width',
            'description': 'Change the size of the chromosomes in your ideogram.',
            'code': '''import dash_bio as dashbio

dashbio.Ideogram(
    id='ideogram-size',
    chrHeight=800,
    chrWidth=100
)'''
        },

        {
            'param_name': 'Annotations',
            'description': 'Display annotations that are loaded from a JSON file.',
            'code': '''import dash_bio as dashbio

dashbio.Ideogram(
    id='ideogram-annotations',
    chromosomes=['X', 'Y'],
    annotationsPath='https://eweitz.github.io/ideogram/data/annotations/SRR562646.json'
)'''
        },

        {
            'param_name': 'Rotatability',
            'description': 'Disable rotation of the chromosome upon clicking on it.',
            'code': '''import dash_bio as dashbio

dashbio.Ideogram(
    id='ideogram-rotate',
    rotatable=False
)'''
        },

        {
            'param_name': 'Orientation',
            'description': 'Display chromosomes horizontally or vertically.',
            'code': '''import dash_bio as dashbio

dashbio.Ideogram(
    id='ideogram-orientation',
    orientation='horizontal'
)'''
        },

        {
            'param_name': 'Brush',
            'description': 'Highlight a region of the chromosome by adding a brush.',
            'code': '''import dash_bio as dashbio

dashbio.Ideogram(
    id='ideogram-brush',
    chromosomes=['X'],
    orientation='horizontal',
    brush='chrX:1-10000000'
)'''
        }
    ]
)

# ManhattanPlot
ManhattanPlot = create_doc_page(
    examples, component_names, 'manhattan-plot', component_examples=[
        {
            'param_name': 'Line colors',
            'description': 'Change the colors of the suggestive line and the genome-wide line.',
            'code': '''import pandas as pd
import dash_core_components as dcc
import dash_bio as dashbio

df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/manhattan_data.csv")

manhattanplot = dashbio.ManhattanPlot(
    dataframe=df,
    suggestiveline_color='#AA00AA',
    genomewideline_color='#AA5500'
)

dcc.Graph(figure=manhattanplot)'''
        },

        {
            'param_name': 'Highlighted points color',
            'description': 'Change the color of the points that are considered significant.',
            'code': '''import pandas as pd
import dash_core_components as dcc
import dash_bio as dashbio

df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/manhattan_data.csv")

manhattanplot = dashbio.ManhattanPlot(
    dataframe=df,
    highlight_color='#00FFAA'
)

dcc.Graph(figure=manhattanplot)'''
        }

    ]
)

# Molecule3dViewer
Molecule3dViewer = create_doc_page(
    examples, component_names, 'molecule-3d-viewer', component_examples=[

        {
            'param_name': 'Selection type',
            'description': 'Choose what gets highlighted with the same color upon selection.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

dashbio.Molecule3dViewer(
    styles=styles_data,
    modelData=model_data,
    selectionType='Chain'
)'''
        },

        {
            'param_name': 'Background color/opacity',
            'description': 'Change the background color and opacity of the canvas on which \
            Mol3D is rendered.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

dashbio.Molecule3dViewer(
    styles=styles_data,
    modelData=model_data,
    backgroundColor='#FF0000',
    backgroundOpacity=0.2
)'''
        }

    ]
)

# NeedlePlot
NeedlePlot = create_doc_page(
    examples, component_names, 'needle-plot', component_examples=[

        {
            'param_name': 'Needle style',
            'description': 'Change the appearance of the needles.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/needle_PIK3CA.json").read().decode("utf-8")

mdata = json.loads(data)

dashbio.NeedlePlot(
    mutationData=mdata,
    needleStyle={
        'stemColor': '#FF8888',
        'stemThickness': 2,
        'stemConstHeight': True,
        'headSize': 10,
        'headColor': ['#FFDD00', '#000000']
    }
)'''
        },

        {
            'param_name': 'Domain style',
            'description': 'Change the appearance of the domains.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/needle_PIK3CA.json").read().decode("utf-8")

mdata = json.loads(data)

dashbio.NeedlePlot(
    mutationData=mdata,
    domainStyle={
        'displayMinorDomains': True,
        'domainColor': ['#FFDD00', '#00FFDD', '#0F0F0F', '#D3D3D3']
    }
)'''
        }

    ]
)

# Oncoprint
Oncoprint = create_doc_page(
    examples, component_names, 'onco-print', component_examples=[
        {
            'param_name': 'Colors',
            'description': 'Change the color of specific mutations, as well as the background color.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/oncoprint_dataset3.json").read()
data = json.loads(data)

dashbio.OncoPrint(
    data=data,
    colorscale={
        'MISSENSE': '#e763fa',
        'INFRAME': '#E763FA'
    },
    backgroundcolor='#F3F6FA'
)'''
        },

        {
            'param_name': 'Size and spacing',
            'description': 'Change the height and width of the component, and adjust the spacing between adjacent tracks.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/oncoprint_dataset3.json").read()
data = json.loads(data)

dashbio.OncoPrint(
    data=data,
    height=800,
    width=500,
    padding=0.25
)'''
        },

        {
            'param_name': 'Legend and overview',
            'description': 'Show or hide the legend and/or overview heatmap.',
            'code': '''import json
import six.moves.urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/oncoprint_dataset3.json").read()
data = json.loads(data)

dashbio.OncoPrint(
    data=data,
    showlegend=False,
    showoverview=False
)'''
        }
    ]
)

# SequenceViewer
SequenceViewer = create_doc_page(examples, component_names, 'sequence-viewer')

# Speck
Speck = create_doc_page(examples, component_names, 'speck')

# VolcanoPlot
VolcanoPlot = create_doc_page(examples, component_names, 'volcano-plot')
