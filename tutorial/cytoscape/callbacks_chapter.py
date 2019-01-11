from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .utils import CreateDisplay
from tutorial import tools, styles


examples = {
    example: tools.load_example('tutorial/examples/cytoscape/{}'.format(example))
    for example in ['update_layout.py']
}


'''
- Adding and removing elements
- Modifying the layout and the stylesheet
- Advanced usage of callbacks
'''


nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': -20*long}
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

Display = CreateDisplay({
    'dash_cytoscape': dash_cytoscape,
    'elements': nodes + edges,
    'dcc': dcc
})

layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash Callbacks for Cytoscape
    
    One important concept introduced by Dash is that of callbacks, the Python
    equivalent of event handlers. Rather than modifying and updating the graph
    by using `cy.on(...)` or other event handler, we use callbacks that takes
    as input the ID of a component (button, dropdown, text field, etc.) and
    output the result of our callback function to the property of the 
    Cytoscape component (i.e., modifies the argument of one of `Cytoscape`'s
    parameters). We assume you have already gone through the 
    [introductory tutorial on callbacks](/getting-started-part-2), or that
    you are familiar with them; this chapter will go over Dash callbacks 
    specific to Dash Cytoscape.
    
    ## Layouts
    
    Consider the graph containing North American cities from the layout 
    chapter. We have shown in that chapter how to display the same graph in
    multiple layouts. But what if we want to introduce the option for the 
    user to interactively update the layouts?
    
    Recall the declaration of the graph:
    ''')),

    html.Details(open=False, children=[
        html.Summary('View Elements Declaration'),
        dcc.SyntaxHighlighter(dedent('''
        nodes = [
            {
                'data': {'id': short, 'label': label}, 
                'position': {'x': 20*lat, 'y': -20*long}
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
    
        elements = nodes + edges
        '''))
    ]),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '400px'},
        layout={
            'name': 'grid'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    What we want to modify is the argument to `layout`. To do so, we could use
    a `dash_core_components.Dropdown` with the name of the layouts as options.
    We could set the default value to 'grid', and force it to be unclearable
    (since we do not want to pass a dictionary with null value to `Cytoscape`).
    ''')),

    Display('''
    dcc.Dropdown(
        id='dropdown',
        value='grid',
        clearable=False,
        options=[
            {'label': name.capitalize(), 'value': name}
            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
        ]
    )
    '''),

    dcc.Markdown(dedent('''
    The construction of the callback becomes extremely easy. We simply create
    a function as such:
    
    ```python
    @app.callback(Output('cytoscape', 'layout'),
                  [Input('dropdown', 'value')])
    def update_layout(layout):
        return {'name': layout}
    ``` 
    
    In fact, it is even possible to animate the layouts after an update! 
    Simply enable `animate`:
    
    ```python
    @app.callback(Output('cytoscape', 'layout'),
                  [Input('dropdown', 'value')])
    def update_layout(layout):
        return {
            'name': layout,
            'animate': True
        }
    ```
    
    Piecing everything together, we get:
    ''')),

    dcc.SyntaxHighlighter(
        examples['update_layout.py'][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(
        examples['update_layout.py'][1],
        className='example-container'
    )

])
