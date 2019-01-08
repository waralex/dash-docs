import dash_html_components as html
import dash_cytoscape
from tutorial.utils.convert_props_to_table import generate_prop_table


layout = html.Div([
    html.H1('Dash Cytoscape Reference'),
    generate_prop_table('Cytoscape', dash_cytoscape)
])
