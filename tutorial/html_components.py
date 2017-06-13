# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import styles
from server import app

layout = html.Div(children=[

    html.H4('HTML Attributes', id="html-attributes"),
    html.Div('''
    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and Javascript.

    Instead of writing HTML or using an HTML templating engine,
    you compose your layout using Python structures.
    HTML in dash looks like this:
    '''),
    dcc.SyntaxHighlighter('''import dash_html_components as html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P('This conversion happens behind the scenes by Dash\'s Javascript front-end')
    ])
])''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div(
        'which gets converted (behind the scenes) into the '
        'following HTML in your web-app:'
    ),
    dcc.SyntaxHighlighter('''<div>
    <h1>Hello</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's Javascript front-end</p>
    </div>
</div>''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    dcc.Markdown('''
        If you're not comfortable with HTML, don't worry!
        You can get 95% of the way there with just a few elements
        and attributes.
        Dash's core component library also supports
        [Markdown](http://commonmark.org/help).
    '''.replace('  ', '')),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

    dcc.Markdown(\'\'\'
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
    \'\'\')
    '''.replace('  ', ''),
        customStyle=styles.code_container,
        language='python'
    ),

    dcc.Markdown('''
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.'''.replace('  ', ''),
    containerProps={'className': 'example-container'}),

    html.Div('If you\'re using HTML components, then you also access to '
             'properties like `style`, `class`, and `id`. '
             'All of these attributes are available in the Python classes.'),
    html.Div("The HTML elements and Dash classes are mostly the same. "
             "Here are a few key differences:"),
    html.Li('The `style` property is a dictionary'),
    html.Li('Properties in the `style` dictionary are camelCased'),
    html.Li('The `class` key is renamed as `className`'),
    html.Li('Style properties in pixel units can be supplied as just numbers without the `px` unit'),
    html.Div("Let's take a look at an example."),
    dcc.SyntaxHighlighter('''import dash_html_components as html

html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})
''', language='python', customStyle=styles.code_container),
    html.Div("That dash code will render this HTML markup:"),
    dcc.SyntaxHighlighter('''
<div style="margin-bottom: 50px; margin-top: 25px;">

    <div style="color: blue; font-size: 14px">
        Example Div
    </div>

    <p class="my-class", id="my-p-element">
        Example P
    </p>

</div>
''', language='html', customStyle=styles.code_container)
])
