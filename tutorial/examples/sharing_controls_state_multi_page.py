import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from flask_caching import Cache
import uuid


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True

CACHE_CONFIG = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 200
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Store(id='session-id', storage_type='memory', data=session_id),
        dcc.Location(id='url'),
        html.H1('Sharing State in Multi-page Apps'),
        html.Div(id='page-content')
    ])


app.layout = serve_layout


def gen_page1(session_id):
    return html.Div([
        html.H3('Page 1 content'),
        dcc.Dropdown(
            id='page1-dropdown1',
            options=[{'label': 'Page 1 Dropdown: {}'.format(i), 'value': i} for i in ['X', 'Y', 'Z']],
            value=cache.get('{}-dropdown1'.format(session_id))
        ),
        html.Div(id='page1-output1'),
        dcc.Link('go to page 2', href='/page2'),
    ])


def gen_page2(session_id):
    return html.Div([
        html.H3('Page 2 content'),
        dcc.Dropdown(
            id='page2-dropdown1',
            options=[{'label': 'Page 2 Dropdown: {}'.format(i), 'value': i} for i in ['X', 'Y', 'Z']],
            value=cache.get('{}-dropdown1'.format(session_id))
        ),
        html.Div(id='page2-output1'),
        dcc.Link('go to page 1', href='/page1'),

    ])


@app.callback(Output('page1-output1', 'children'),
              [Input('page1-dropdown1', 'value')],
              [State('session-id', 'data')])
def update_page1_dropdown(value, session_id):
    cache.set('{}-dropdown1'.format(session_id), value)
    return 'Value "{}" is selected. Refresh to reset the cache.'.format(value)


@app.callback(Output('page2-output1', 'children'),
              [Input('page2-dropdown1', 'value')],
              [State('session-id', 'data')])
def update_page2_dropdown(value, session_id):
    cache.set('{}-dropdown1'.format(session_id), value)
    return 'Value "{}" is selected. Refresh to reset the cache.'.format(value)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'data')])
def render_content(pathname, session_id):
    if not pathname:
        pathname = 'page1'
    if 'page2' in pathname:
        return gen_page2(session_id)
    else:
        return gen_page1(session_id)


if __name__ == '__main__':
    app.run_server(debug=True)