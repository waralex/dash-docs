from server import app, server

import dash_html_components as html
import dash_core_components as dcc

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


def display_chapter(chapter_id):
    chapters = {
        'introduction': introduction.layout,
        'getting-started': getting_started.layout,
        'html-attributes': html_components.layout,
        'supercharged-components': core_components.layout,
        'callbacks': basic_callbacks.layout,
        'callback-resolution': callbacks_with_dependencies.layout,
        'html-component-library': html_component_appendix.layout,
        'dynamic-content': dynamic_content.layout,
        'custom-css-and-js': external_css_and_js.layout,
        'open-problems': open_problems.layout,
        'architecture': architecture.layout
    }

    return chapters[chapter_id]


toc = html.Div([
    dcc.RadioItems(options=[
        {'label': 'Introduction', 'value': 'introduction'},
        {'label': 'Getting Started', 'value': 'getting-started'},
        {'label': 'HTML Attributes', 'value': 'html-attributes'},
        {'label': 'Supercharged Components', 'value': 'supercharged-components'},
        {'label': 'Basic Callbacks', 'value': 'callbacks'},
        {'label': 'Callback Resolution', 'value': 'callback-resolution'},
        {'label': 'HTML Component Library', 'value': 'html-component-library'},
        {'label': 'Dynamic Content', 'value': 'dynamic-content'},
        {'label': 'Custom CSS and Javascript', 'value': 'custom-css-and-js'},
        {'label': 'Open Problems', 'value': 'open-problems'},
        {'label': 'Architecture Drafts', 'value': 'architecture'},
    ], value='introduction', id='toc', labelStyle={'fontWeight': 400})
])


@app.react('chapter', ['toc'])
def display_content(toc):
    return {'content': display_chapter(toc['value'])}


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


app.css.append_css({
    'external_url': (
        'https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/9ee5fa299197c90bb1a94a1e7711e22c28533812/dash.css'
    )
})

app._setup_server()
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
