import re

import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape as cyto


def component_doc(component):
    trimmed_docs = re.sub(
        r'- setProps.*\n',
        '',
        re.sub(
            r'Available events: .*',
            '',
            component.__doc__.split('Keyword arguments:')[-1]
        )
    )

    return html.Div([
        html.H1('Cytoscape Reference'),
        html.H3('Keyword Arguments'),
        html.Div(className='cytoscape-reference', children=[
            dcc.Markdown(trimmed_docs)
        ])
    ])


layout = html.Div([
    component_doc(cyto.Cytoscape)
])
