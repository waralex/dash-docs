from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles
from tutorial.utils.component_block import ComponentBlock
from tutorial.tools import load_example

import dash_bio

from tutorial.utils.simple_doc_generator import generate_docs

dashbio_library_heading = dcc.Markdown('''
    # Dash Bio 
    
    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and JavaScript. 

    Dash Bio is a suite of bioinformatics components that make it simpler to
    analyze and visualize bioinformatics data and interact with it in a Dash
    application. 

    The source is on GitHub at [plotly/dash-bio](https://github.com/plotly/dash-bio). 

    These docs are using version {}. 
    '''.replace('    ', '').format(dash_bio.__version__)
)

dashbio_install_instructions = dcc.SyntaxHighlighter('''>>> import dash_bio
    >>> print(dash_bio.__version)
    {}'''.replace('    ', '').format(dash_bio.__version__),
    customStyle=styles.code_container)


dashbio_components = {
    'SequenceViewer': {
        'description': '''A sequence viewer.''',
        'props': {
            'sequence': 'GATTACA'
        }
    }
}


layout_children = generate_docs(
    'dash-bio',
    'dashbio',
    dashbio_library_heading,
    dashbio_components
)

layout_children.insert(1, dashbio_install_instructions)

layout = html.Div(className="gallery", children=layout_children)
