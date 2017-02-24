# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from server import app

layout = html.Div(content=[

    html.H4('Section 1 - HTML Attributes', id="html-attributes"),
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
    html.Div("If you're not comfortable with HTML, don't worry! "
             "You can get 95% of the way there with just a few elements. "
             "View the Component Library in the appendix of these docs "
             "to see what these components look like."),

    dcc.SyntaxHighlighter('''from dash_html_components import Div, H2, Span, Img

Div([
    # H1 - H6 are for headings
    H2('Dash App'),

    # Div is generic - use it to encapsulate other components or just for text
    Div('A description of your dash app'),

    # Embed images with the Img tag and the `src` key
    Img(src="https://plot.ly/~chris/1638.png")
])
''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),

    html.Div('HTML elements have properties like `style`, `class`, and `id`. '
             'All of these attributes are available in the Python classes.'),
    html.Div("The HTML elements and Dash classes are mostly the same. "
             "Here are a few key differences:"),
    html.Li('The `style` property is a dictionary'),
    html.Li('Properties in the `style` dictionary are camelCased'),
    html.Li('The `class` key is renamed as `className`'),
    html.Li('Style properties in pixel units can be supplied as just numbers without the `px` unit'),
    html.Div("Let's take a look at an example."),
    dcc.SyntaxHighlighter('''from dash_html_components import Div

Div([
    Div('Example Div', style={'color': 'blue', fontSize: 14}),
    P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})
''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
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
''', language='html', customStyle={'borderLeft': 'thin solid lightgrey'})
])
