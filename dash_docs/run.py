from collections import OrderedDict

import dash_html_components as html
import dash_core_components as dcc
import dash_table

from dash.dependencies import Input, Output

from .server import app, server

from .import chapter_index
from dash_docs import tools
from dash_docs.tutorial import home

from dash_docs.tutorial import search

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


def create_backlinks(pathname):
    parts = pathname.strip('/').split('/')
    links = [
        dcc.Link('Table of Contents', href='/')
    ]
    for i, part in enumerate(parts[:-1]):
        links += [
            html.Span(' > '),
            dcc.Link(
                part.replace('-', ' ').title(),
                href='/' + '/'.join(parts[:i + 1])
            )
        ]
    links += [html.Span(' > ' + parts[-1].replace('-', ' ').title())]
    return links


@app.callback(Output('chapter', 'children'),
              [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None or pathname == '/':
        return home.layout
    pathname = pathname.rstrip('/')

    if pathname in chapter_index.URL_TO_CONTENT_MAP:
        backlinks = create_backlinks(pathname)
        return backlinks + [
            html.Br(),
            chapter_index.URL_TO_CONTENT_MAP[pathname],
            html.Hr()
        ] + backlinks + [
            html.Div(id='wait-for-page-{}'.format(pathname)),
        ]

    elif pathname == '/search':
        return create_backlinks(pathname) + [
            html.Br(),
            search.layout
        ]

    else:
        return [
            html.Div('Page {} not found'.format(pathname), className='warning-box'),
            home.layout
        ]


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
