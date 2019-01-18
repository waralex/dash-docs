from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .utils import CreateDisplay
from tutorial import tools, styles


examples = {
    example: tools.load_example(
        'tutorial/examples/cytoscape/{}'.format(example)
    )
    for example in [
        'event_callbacks.py'
    ]
}

nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20 * lat, 'y': -20 * long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 34.03, -118.25),
        ('nyc', 'New York', 40.71, -74),
        ('to', 'Toronto', 43.65, -79.38),
        ('mtl', 'Montreal', 45.50, -73.57),
        ('van', 'Vancouver', 49.28, -123.12),
        ('chi', 'Chicago', 41.88, -87.63),
        ('bos', 'Boston', 42.36, -71.06),
        ('hou', 'Houston', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'boston'),
        ('to', 'hou'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'label': 'data(label)'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'line-color': '#A3C4BC'
        }
    }
]

Display = CreateDisplay({
    'dash_cytoscape': dash_cytoscape,
    'html': html,
    'dcc': dcc,
    'default_stylesheet': default_stylesheet,
    'nodes': nodes,
    'edges': edges
})


layout = html.Div([

    dcc.Markdown(dedent('''
    # Events Callbacks for User Interactions in Cytoscape
    
    In [part 4](/cytoscape/callbacks), we showed how to update Cytoscape with
    other components by assigning callbacks that output to `'elements',
    'stylesheet', 'layout'`. Moreover, it is also possible to use properties 
    of Cytoscape as an input to callbacks, which can be used to update other
    components, or Cytoscape itself. Those properties are updated (which fires
    the callbacks) when the user interact with elements in a certain way, 
    which justifies the name of event callbacks. You can find props such as 
    `tapNode`, which returns a complete description of the node object when 
    the user clicks or taps on a node, `mouseoverEdgeData`, which returns only 
    the data dictionary of the edge that was most recently hovered by the user.
    The complete list can be found in the [Cytoscape Reference](/cytoscape/reference).
    
    ## Simple callback construction
    
    Let's look back at the same city example as the previous chapter:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape-eventsx',
        layout={'name': 'preset'},
        elements=edges+nodes,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    )
    '''),

    dcc.Markdown(dedent('''
    This time, we will use the `tapNode` and `tapNodeData` properties as input
    to our callbacks, which will simply dump the the content into an HTML div: 
    ''')),

    dcc.SyntaxHighlighter(
        examples['event_callbacks.py'][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(
        examples['event_callbacks.py'][1],
        className='example-container'
    ),

])
