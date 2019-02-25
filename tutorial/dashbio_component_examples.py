# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tutorial import styles
from tutorial import tools
from tutorial.utils.bio_convert_props import generate_prop_table, default_example, component_names
from tutorial.utils.component_block import ComponentBlock
from tutorial.components import Syntax, Example


component_names = component_names('dash_bio')

print(component_names)

examples = {
    'alignment-chart': tools.load_example(
        'tutorial/examples/dashbio_components/alignment_chart.py'),
    'sequence-viewer': tools.load_example(
        'tutorial/examples/dashbio_components/sequence_viewer.py'),
    'clustergram': tools.load_example(
        'tutorial/examples/dashbio_components/clustergram.py'),
}


def create_doc_page(component_name):
    return html.Div(
        children=
        [html.H1('{} Examples and Reference'.format(
            component_name.replace('-', ' ').title().replace(' ', '')))] +
        default_example(component_name,
                        examples[component_name],
                        styles=styles) +
        [generate_prop_table(
            component_name.replace('-', ' ').title().replace(' ', ''),
            component_names,
            'dash_bio')]
    )


# AlignmentChart/AlignmentViewer
AlignmentChart = create_doc_page('alignment-chart')

# Circos

# Clustergram
Clustergram = create_doc_page('clustergram')

# Ideogram

# ManhattanPlot

# Molecule3dViewer

# NeedlePlot

# OncoPrint

# SequenceViewer
SequenceViewer = create_doc_page('sequence-viewer')

# Speck

# VolcanoPlot
