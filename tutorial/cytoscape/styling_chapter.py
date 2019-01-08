from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .utils import section_title
from tutorial import tools, styles



# examples = {
#     example: tools.load_example('tutorial/examples/table/{}'.format(example))
#     for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
# }


layout = html.Div([

    dcc.Markdown(dedent('''
    # Styling

    ''')),


])
