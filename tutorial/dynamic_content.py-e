# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles
from tutorial import tools

examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/dynamic_content.py'
    ]
]


layout = html.Div(children=[
    dcc.Markdown('''
    ## Loading Content Dynamically

    Dash callbacks can return any type of property.
    By returning `children`, they can even dynamically
    render their content.

    This is an example that can be used in app development for
    quicker feedback.
    Instead of refreshing the page to view your layout,
    just render the layout as a response to clicking on a button.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[0][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[0][1], className="example-container")

])
