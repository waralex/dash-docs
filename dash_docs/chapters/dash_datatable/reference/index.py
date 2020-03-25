import dash_html_components as html
import dash_table
from dash_docs import reusable_components as rc


layout = html.Div([
    html.H1('dash_table.DataTable Reference'),
    rc.ComponentReference('DataTable', dash_table)
])
