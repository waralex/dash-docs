import dash_html_components as html

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import section_title
from tutorial import tools
from tutorial import styles


# examples = {
#     example: tools.load_example('tutorial/examples/table/{}'.format(example))
#     for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
# }


layout = html.Div([

    dcc.Markdown(dedent('''
    # Applications

    ''')),


])
