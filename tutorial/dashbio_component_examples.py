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

examples = {
    'sequence-viewer': tools.load_example(
        'tutorial/examples/dashbio_components/sequence_viewer.py')
}


# SequenceViewer
SequenceViewer = html.Div(
    children=
    default_example('sequence-viewer',
                    examples['sequence-viewer'],
                    styles=styles) +
    [generate_prop_table('SequenceViewer', component_names, 'dash_bio')]
)


    
