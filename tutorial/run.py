import time
import six

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Event, Output

from server import app, server
import introduction
import getting_started
import html_components
import core_components
import basic_callbacks
import html_component_appendix
import callbacks_with_dependencies
import dynamic_content
import external_css_and_js
import open_problems
import architecture
import graph_callbacks
# import live_updates
import urls
import changelog
import plugins
import advanced_features


app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-1.27.1.min.js'

def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)

toc = html.Div(
create_contents([
    html.A('Introduction', href="/introduction"),
    [
        'Why Dash?',
        'Licensing'
    ],
    'Gallery',
    html.A('Create Your First App', href="/getting-started"),
    [
        'Installation',
        'Part 1 - Dash Layout',
        [
            'HTML Components',
            'Data Visualization in Dash',
            'Markdown',
            'Core Component Library',
            'Calling `help`'
        ],
        'Part 2 - Interactivity',
        [
            'Fundamentals',
            'Multiple Inputs',
            'Multiple Outputs',
            'Crossfiltering'
        ]
    ],
    'Deploying',
    [
        'On Premise',
        'Cloud PaaS'
    ],
    html.A('Advanced Features', href="/advanced"),
    [
        'Caching',
        'Fast Charting with WebGL',
        'URLs and Single Page Apps',
        'Live Updates'
    ],
    html.A('External CSS and JS', href="/external-resources"),

    html.A('Dash Core Component Library Reference', href="/dash-core-components"),
    [
        'Graph',
        'Dropdown',
        'RadioItems',
        'TextInput',
        'Slider',
        'RangeSlider',
        'Markdown'
    ],
    html.A('Dash HTML Component Library Reference', href="/dash-html-components"),
    'Base Component API',
    'Best Practices',
    [
        'Virtual Environments',
        'Styling Apps',
        'Basic User Interface',
        'Initial State'
    ],
    'Roadmap',
    [
        'Sponsoring Development',
        'Near Term',
        [
            'App Templates',
            'Authentication'
        ],
        'Long Term',
        [
            'Dash in Other Languages',
            'GUI App Builder',
            'Client-side Apps'
        ]
    ],
    'Get Involved',
    'Credits',
    'Support and Contact'
]), style={'columnCount': 2}
)

chapters = {
    'index': {
        'url': '/',
        'content': html.Div([
            html.H1('Dash Developer Preview'),
            toc
        ])
    },

    'introduction': {
        'url': '/introduction',
        'content': introduction.layout
    },

    'getting-started': {
        'url': '/getting-started',
        'content': getting_started.layout
    },

    'advanced-features': {
        'url': '/advanced',
        'content': advanced_features.layout
    },

    'dash-core-components': {
        'url': '/dash-core-components',
        'content': core_components.layout
    },

    'dash-html-components': {
        'url': '/dash-html-components',
        'content': [
            html_components.layout,
            html_component_appendix.layout
        ]
    },

    'external': {
        'url': '/external-resources',
        'content': external_css_and_js.layout
    }

}


app.layout = html.Div([
    html.Div([
        dcc.RadioItems(options=[
            {'label': i, 'value': i} for i in chapters.keys()
        ], value='index', id='toc', labelStyle={'fontWeight': 400})
    ], style={'display': 'none'}),
    html.Div(id="chapter")
    ], style={
        'fontSize': '1.7rem',
        'backgroundColor': 'white',
        'boxShadow': '5px 5px 5px 0px rgb(240, 240, 240)',
        'borderRadius': '5px',
        'border': 'thin solid rgb(240, 240, 240)',
        'padding': 20
    }, className="container")



@app.callback(Output('chapter', 'content'), [Input('toc', 'value')])
def display_content(selected_chapter):
    return chapters[selected_chapter]['content']

app.routes = [
    {
        'pathname': chapter_object['url'],
        'state': {'toc.value': chapter_id}
    } for chapter_id, chapter_object in six.iteritems(chapters)
]

app.css.append_css({
    'external_url': (
        'https://codepen.io/chriddyp/pen/bWLwgP.css?timestamp=' + str(int(time.time())),
        'https://codepen.io/chriddyp/pen/LLYbXR.css?timestamp=' + str(int(time.time()))
    )
})

app._setup_server()
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
