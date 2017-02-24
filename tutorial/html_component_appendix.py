import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.Div(style={'marginTop': '60px'}),

    html.H3('Appendix - Common HTML Components'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H1("H1 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H1('H1 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H2("H2 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H2('H2 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H3("H3 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H3('H3 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H4("H4 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H4('H4 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H5("H5 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H5('H5 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.H6("H6 Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.H6('H6 Element'),

    html.Hr(),

    dcc.SyntaxHighlighter('html.Div("Generic Div Element")', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div('Generic Div Element')
])
