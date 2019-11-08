from collections import OrderedDict

import dash_html_components as html
import dash_core_components as dcc
import dash_table

from dash.dependencies import Input, Output

from .server import app, server

from .import chapter_index
from dash_docs import tools
from dash_docs.tutorial import home


def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)


header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.A(html.Img(
                src='/assets/images/logo.png',
                className='logo'
            ), href='/'),

            html.Div(className='links', children=[
                html.A('dash enterprise', className='link', href='https://plot.ly/dash/'),
                html.A('user guide', className='link active', href=tools.relpath('/')),
                html.A('plotly', className='link', href='https://plot.ly/'),
                html.A(children=[html.I(className="fa fa-search")], className='link', href=tools.relpath('/search'))
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [
        # Stores used by examples.
        dcc.Store(id='memory'),
        dcc.Store(id='memory-output'),
        dcc.Store(id='local', storage_type='local'),
        dcc.Store(id='session', storage_type='session'),
        header,
        html.Div([
            html.Div(id='wait-for-layout'),
            html.Div([
                html.Div(
                    html.Div(id='chapter', className='content'),
                    className='content-container'
                ),
            ], className='container-width')
        ], className='background'),
        dcc.Location(id='location', refresh=False),
    ]
)


@app.callback(Output('chapter', 'children'),
              [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None or pathname == '/':
        return home.layout
    pathname = pathname.rstrip('/')

    if pathname in chapter_index.URL_TO_CONTENT_MAP:
        return chapter_index.URL_TO_CONTENT_MAP[pathname]
    else:
        return '404 - {}'.format(pathname)


app.index_string = '''<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta
            name="description"
            content="Dash User Guide and Documentation. Dash is a Python framework for building analytical web apps in Python."
        >
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <!-- Google Tag Manager Tag -->
        <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-N6T2RXG');</script>
    </head>
    <body>
        <!-- Google Tag Manager Tag -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG"
            height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>'''

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
