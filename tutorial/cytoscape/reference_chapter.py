import re
from textwrap import dedent

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

    return html.Div(className='cytoscape-reference', children=[
        dcc.Markdown(trimmed_docs)
    ])


layout = html.Div([
    html.H1('Cytoscape Reference'),
    html.H2('Cytoscape'),
    html.H3('Properties'),
    component_doc(cyto.Cytoscape),
    html.H3('Default Values'),
    dcc.Markdown(dedent('''
    * *style*: {'width': '600px', 'height': '600px'}
    * *layout*: {'name': 'grid'}
    * *pan*: {'x': 0, 'y': 0}
    * *zoom*: 1
    * *panningEnabled*: True
    * *userPanningEnabled*: True
    * *minZoom*: 1e-50
    * *maxZoom*: 1e50
    * *zoomingEnabled*: True
    * *userZoomingEnabled*: True
    * *boxSelectionEnabled*: False
    * *autoungrabify*: False
    * *autolock*: False
    * *autounselectify*: False
    * *autoRefreshLayout*: True
    ''')),
])
