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
        html.H1('Sharing State with Dash Tabs'),
        dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
            dcc.Tab(label='Tab One', value='tab-1-example'),
            dcc.Tab(label='Tab Two', value='tab-2-example'),
        ]),
        html.Div(id='tab-content-output')
    ])


app.layout = serve_layout


def gen_tab1(session_id):
    return html.Div([
            html.H3('Tab content 1'),
            dcc.Dropdown(
                id='tab1-dropdown1',
                options=[{'label': 'Tab 1 Dropdown: {}'.format(i), 'value': i} for i in ['X', 'Y', 'Z']],
                value=cache.get('{}-dropdown1'.format(session_id))
            ),
            html.Div(id='tab1-output1'),
        ])


def gen_tab2(session_id):
    return html.Div([
        html.H3('Tab content 2'),
        dcc.Dropdown(
            id='tab2-dropdown1',
            options=[{'label': 'Tab 2 Dropdown: {}'.format(i), 'value': i} for i in ['X', 'Y', 'Z']],
            value=cache.get('{}-dropdown1'.format(session_id))
        ),
        html.Div(id='tab2-output1'),
    ])


@app.callback(Output('tab1-output1', 'children'),
              [Input('tab1-dropdown1', 'value')],
              [State('session-id', 'data')])
def update_tab1_dropdown(value, session_id):
    cache.set('{}-dropdown1'.format(session_id), value)
    return 'Value "{}" is selected. Refresh to reset the cache.'.format(value)


@app.callback(Output('tab2-output1', 'children'),
              [Input('tab2-dropdown1', 'value')],
              [State('session-id', 'data')])
def update_tab2_dropdown(value, session_id):
    cache.set('{}-dropdown1'.format(session_id), value)
    return 'Value "{}" is selected. Refresh to reset the cache.'.format(value)


@app.callback(Output('tab-content-output', 'children'),
              [Input('tabs-example', 'value')],
              [State('session-id', 'data')])
def render_content(tab, session_id):
    if tab == 'tab-1-example':
        return gen_tab1(session_id)
    elif tab == 'tab-2-example':
        return gen_tab2(session_id)


if __name__ == '__main__':
    app.run_server(debug=True)
