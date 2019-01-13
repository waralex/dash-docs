from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .utils import CreateDisplay
from tutorial import tools, styles


examples = {
    example: tools.load_example('tutorial/examples/cytoscape/{}'.format(example))
    for example in ['update_layout.py', 'stylesheet_callbacks.py']
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

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': 'BFD7B5',
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
    'elements': nodes + edges,
    'html': html,
    'dcc': dcc,
    'default_stylesheet': default_stylesheet
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
    
    ## Changing Layouts
    
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
    ),

    dcc.Markdown(dedent('''
    ## Interactively update styles
    
    Updating the stylesheet using Dash components is similar to updating
    layouts, although it can get more complex. Indeed, you can choose to create
    a default stylesheet, and append new styles to that stylesheet every time
    a designated callback is fired. Let's take the following stylesheet:
    
    ```python
    default_stylesheet = [
        {
            'selector': 'node',
            'style': {
                'background-color': 'BFD7B5',
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
    ```
    
    This is generally declared at the beginning of your script, before layout
    declaration (therefore it is shared accross sessions). The city graph will 
    look something like this:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '400px'},
        layout={
            'name': 'circle'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    We might want to use text fields to input the color we want to add: 
    ''')),

    Display('''
    html.Div([
        html.Div(style={'width': '50%', 'display': 'inline'}, children=[
            'Edge Color:',
            dcc.Input(id='input-line-color', type='text')
        ]),
        html.Div(style={'width': '50%', 'display': 'inline'}, children=[
            'Node Color:',
            dcc.Input(id='input-bg-color', type='text')
        ])
    ])
    '''),

    dcc.Markdown(dedent('''
    All we need now is to assign a callback that will add new styles to the 
    default stylesheet in order to change the default color:
    
    ```python
    @app.callback(Output('cytoscape', 'stylesheet'),
              [Input('input-line-color', 'value'),
               Input('input-bg-color', 'value')])
    def update_stylesheet(line_color, bg_color):
        if line_color is None:
            line_color = ''
    
        if bg_color is None:
            bg_color = ''
    
        new_styles = [
            {
                'selector': 'node',
                'style': {
                    'background-color': bg_color
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': line_color
                }
            }
        ]
    
        return default_stylesheet + new_styles
    ```
    
    Notice that we are setting the line and background color to an empty
    string when they are set to `None`; this is to avoid feeding `None`
    to the dictionary, since it is not accepted by `Cytoscape`. 
    
    However, passing any string value to the dictionary is accepted, even when 
    the string value is not recognized. Therefore, the callback is fired every
    time you type a new character, but the changes are only applied when
    `Cytoscape` recognizes the input, which in this case could be the name of
    a color, the hex code, or the rgb function.
    
    Below, we show how the entire app is constructed:
    ''')),

    dcc.SyntaxHighlighter(
        examples['stylesheet_callbacks.py'][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(
        examples['stylesheet_callbacks.py'][1],
        className='example-container'
    ),

    dcc.Markdown(dedent('''
    In this example, we are not appending the new styles
    directly to the default style, but instead concatenating 
    `default_stylesheet` with `new_styles`. This is because any modification
    to `default_stylesheet` will be permanent, which is not a good thing if you
    are hosting your app for many users (since `default_stylesheet` is shared
    across all user sessions).
    
    If you want to find more examples of styling using callbacks,
    check out `usage-stylesheet.py`, which presents a comprehensive overview
    of techniques for manipulating stylesheets in Dash Cytoscape.
    
    ## Adding and removing elements
    '''))

])
