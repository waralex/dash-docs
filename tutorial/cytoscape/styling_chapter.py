from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .utils import section_title, CreateDisplay
from tutorial import tools, styles

'''
- Using selectors to modify specific groups of elements
- Organize your edges with curve and line properties
- Advanced node styling with pie charts and images
'''

# examples = {
#     example: tools.load_example('tutorial/examples/table/{}'.format(example))
#     for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
# }

simple_elements = [
    {
        'data': {'id': 'one', 'label': 'Modified Color'},
        'position': {'x': 75, 'y': 75},
        'classes': 'red' # Single class
    },
    {
        'data': {'id': 'two', 'label': 'Modified Shape'},
        'position': {'x': 75, 'y': 200},
        'classes': 'triangle' # Single class
    },
    {
        'data': {'id': 'three', 'label': 'Both Modified'},
        'position': {'x': 200, 'y': 75},
        'classes': 'red triangle' # Multiple classes
    },
    {
        'data': {'id': 'four', 'label': 'Regular'},
        'position': {'x': 200, 'y': 200}
    },
    {'data': {'source': 'one', 'target': 'two'}, 'classes': 'red'},
    {'data': {'source': 'two', 'target': 'three'}},
    {'data': {'source': 'three', 'target': 'four'}, 'classes': 'red'},
    {'data': {'source': 'two', 'target': 'four'}},
]

weighted_elements = [
    {'data': {'id': 'A'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'C'}},
    {'data': {'id': 'D'}},
    {'data': {'id': 'E'}},

    {'data': {'source': 'A', 'target': 'B', 'weight': 1}},
    {'data': {'source': 'A', 'target': 'C', 'weight': 2}},
    {'data': {'source': 'B', 'target': 'D', 'weight': 3}},
    {'data': {'source': 'B', 'target': 'E', 'weight': 4}},
    {'data': {'source': 'C', 'target': 'E', 'weight': 5}},
    {'data': {'source': 'D', 'target': 'A', 'weight': 6}}
]

Display = CreateDisplay({
    'dash_cytoscape': dash_cytoscape,
    'simple_elements': simple_elements,
    'weighted_elements': weighted_elements
})

layout = html.Div([

    dcc.Markdown(dedent('''
    # Styling
    
    ## The `stylesheet` parameter
    
    Just like how the `elements` parameter takes as an input a list of 
    dictionaries specifying all the elements in the graph, the stylesheet takes
    a list of dictionaries specifying the style for a group of elements, a 
    class of elements, or a single element. Each of these dictionaries accept
    two keys:
    - `'selector'`: A string indicating which elements you are styling.
    - `'style'`: A dictionary specifying what exactly you want to modify. This
    could be the width, height, color of a node, the shape of the arrow on an
    edge, or many more.
    
    Both the selector and the style dictionary are exhaustively documented in 
    the Cytoscape.js docs. The selector is documented 
    [here](http://js.cytoscape.org/#selectors). 
    You can find all the possible keys for your style dictionary in the 
    [*Style* section of the docs](http://js.cytoscape.org/#style/node-body), 
    starting with the "Node Body" subsection. We will show examples that can
    be easily modified for any type of design, and you can create your own
    styles with the sandbox (open by running `usage-advanced.py`).
    
    
    ## Basic selectors and styles
    
    We start by looking at the same example shown in the elements
    chapter, but this time we examine the stylesheet:
    ''')),

    html.Details(open=False, children=[
        html.Summary('View simple elements'),
        dcc.SyntaxHighlighter(dedent('''
        simple_elements = [
            {
                'data': {'id': 'one', 'label': 'Modified Color'},
                'position': {'x': 75, 'y': 75},
                'classes': 'red' # Single class
            },
            {
                'data': {'id': 'two', 'label': 'Modified Shape'},
                'position': {'x': 75, 'y': 200},
                'classes': 'triangle' # Single class
            },
            {
                'data': {'id': 'three', 'label': 'Both Modified'},
                'position': {'x': 200, 'y': 75},
                'classes': 'red triangle' # Multiple classes
            },
            {
                'data': {'id': 'four', 'label': 'Regular'},
                'position': {'x': 200, 'y': 200}
            },
            {'data': {'source': 'one', 'target': 'two'}, 'classes': 'red'},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}, 'classes': 'red'},
            {'data': {'source': 'two', 'target': 'four'}},
        ]
        '''))
    ]),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=simple_elements,
        stylesheet=[
            # Group selectors
            {
                'selector': 'node',
                'style': {
                    'content': 'data(label)'
                }
            },
        
            # Class selectors
            {
                'selector': '.red',
                'style': {
                    'background-color': 'red',
                    'line-color': 'red'
                }
            },
            {
                'selector': '.triangle',
                'style': {
                    'shape': 'triangle'
                }
            }
        ]
    )
    '''),

    dcc.Markdown(dedent('''
    In this example, we use the group and class selectors. Group selectors 
    consist of either the string `'node'` or the string `'edge'`, since an 
    element can only be one or the other. 
    
    To select a class, you simply pass `.className` to the selector, where 
    `className` is the name of one of the classes you assigned to some of your
    elements. Notice in the example above that if an element has two or more
    classes, it will accept all the styles that select it.
    
    Here, we modify the background color and line color of all the elements of
    class "red". This means that if the element is a node, then it will be 
    filled with red, and it is an edge, then the color of the line will be red.
    Although this offers great flexibility, you need to be careful with your 
    declaration, since you won't receive warning if you use the wrong key or
    make a typo. Standard RGB and Hex colors are accepted, along with basic 
    colors recognized by CSS.
    
    Additionally, the `content` key takes as value what you want to display 
    above or next to the element on the screen, which in this case is the 
    label inside the `data` dictionary of the input element. Since we defined 
    a label for each element, that label will be displayed for every node.
    
    ## Comparing data items
    
    A nice property of the selector is that you select elements by comparing
    the value of an item in each of the data dictionaries. Say we have some
    nodes with IDs A to F. One of the edges might be declared the following 
    way:
    ```
    {'data': {'source': 'A', 'target': 'B', 'weight': 1}}
    ```
    The `'weight'` key indicates the weight of your edge. You can find the 
    declaration below:
    ''')),

    html.Details(open=False, children=[
        html.Summary('View weighted elements'),
        dcc.SyntaxHighlighter(dedent('''
        weighted_elements = [
            {'data': {'id': 'A'}},
            {'data': {'id': 'B'}},
            {'data': {'id': 'C'}},
            {'data': {'id': 'D'}},
            {'data': {'id': 'E'}},
        
            {'data': {'source': 'A', 'target': 'B', 'weight': 1}},
            {'data': {'source': 'A', 'target': 'C', 'weight': 2}},
            {'data': {'source': 'B', 'target': 'D', 'weight': 3}},
            {'data': {'source': 'B', 'target': 'E', 'weight': 4}},
            {'data': {'source': 'C', 'target': 'E', 'weight': 5}},
            {'data': {'source': 'D', 'target': 'A', 'weight': 6}}
        ]
    '''))
    ]),

    dcc.Markdown(dedent('''
    If you want to highlight all the of the edges above a certain weight 
    (e.g. 3), simply use the selector `'[weight>3]'`. Here's an example:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '400px'},
        elements=weighted_elements,
        stylesheet=[
            {
                'selector': 'edge',
                'style': {
                    'content': 'data(weight)'
                }
            },
            {
                'selector': '[weight > 3]',
                'style': {
                    'line-color': 'blue'
                }
            }
        ]
    )
    ''')

])
