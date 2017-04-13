from server import app, server

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Event, Output

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
import live_updates
import urls

toc = html.Div([
    dcc.RadioItems(options=[
        {'label': 'Introduction', 'value': 'introduction'},
        {'label': 'Getting Started', 'value': 'getting-started'},
        {'label': 'HTML Attributes', 'value': 'html-attributes'},
        {'label': 'Supercharged Components', 'value': 'supercharged-components'},
        {'label': 'Basic Callbacks', 'value': 'callbacks'},
        {'label': 'Graphs with Callbacks', 'value': 'graph-callbacks'},
        {'label': 'Live Updating Graphs', 'value': 'live-updating-graphs'},
        {'label': 'Callback Resolution', 'value': 'callback-resolution'},
        {'label': 'HTML Component Library', 'value': 'html-component-library'},
        # {'label': 'Dynamic Content', 'value': 'dynamic-content'},
        {'label': 'Custom CSS and Javascript', 'value': 'custom-css-and-js'},
        {'label': 'URLs', 'value': 'urls'},
        {'label': 'Open Problems', 'value': 'open-problems'},
        {'label': 'Architecture Drafts', 'value': 'architecture'},
    ], value='introduction', id='toc', labelStyle={'fontWeight': 400})
])

app.scripts.config.serve_locally = True

def layout():
    return html.Div([
        html.Div([
            toc
        ], className="three columns"),
        html.Div([
            html.Div(id="chapter")
        ], className="nine columns")
    ], style={'fontSize': '1.7rem'}, className="container")


app.layout = layout


def display_chapter(chapter_id):
    chapters = {
        'introduction': introduction.layout,
        'getting-started': getting_started.layout,
        'html-attributes': html_components.layout,
        'supercharged-components': core_components.layout,
        'callbacks': basic_callbacks.layout,
        'graph-callbacks': graph_callbacks.layout,
        'live-updating-graphs': live_updates.layout,
        'callback-resolution': callbacks_with_dependencies.layout,
        'html-component-library': html_component_appendix.layout,
        'dynamic-content': dynamic_content.layout,
        'custom-css-and-js': external_css_and_js.layout,
        'urls': urls.layout,
        'open-problems': open_problems.layout,
        'architecture': architecture.layout
    }

    return chapters[chapter_id]


@app.callback(Output('chapter', 'content'), [Input('toc', 'value')])
def display_content(selected_chapter):
    return display_chapter(selected_chapter)


app.routes = [
    {
        'pathname': ('/{}'.format(option['value'])
                     if option['value'] != 'introduction'
                     else '/'),
        'state': {'toc.value': option['value']}
    } for option in toc['toc'].options
]

app.routes.extend([
    {
        'pathname': '/callbacks/coke',
        'state': {
            'toc.value': 'callbacks',
            'section3-dropdown.value': 'COKE'
        }
    },
    {
        'pathname': '/callbacks/apple',
        'state': {
            'toc.value': 'callbacks',
            'section3-dropdown.value': 'AAPL'
        }
    }
])

app.css.append_css({
    'external_url': (
        'https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

app._setup_server()
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
