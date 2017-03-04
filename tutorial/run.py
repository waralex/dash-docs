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
import open_problems

head = html.Div([
    html.Link(
        rel="stylesheet",
        href="https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75"
             "/raw/d4f178bc09f253251135aeb2141aa077300d1b3f/dash.css"
    ),
    html.Link(
        rel="stylesheet",
        href="https://unpkg.com/react-select@1.0.0-rc.3/dist/react-select.css"
    ),
    html.Link(
        rel="stylesheet",
        href="https://cdn.rawgit.com/chriddyp/abcbc02565dd495b676c3269240e09ca"
             "/raw/816de7d5c5d5626e3f3cac8e967070aa15da77e2/rc-slider.css"
    )
])

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
        'open-problems': open_problems.layout
    }

    return html.Div([
        head,
        chapters[chapter_id]
    ])


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
        {'label': 'Open Problems', 'value': 'open-problems'}
    ], value='introduction', id='toc', labelStyle={'fontWeight': 400})
])


@app.react('chapter', ['toc'])
def display_content(toc):
    return {'content': [display_chapter(toc['value'])]}


app.layout = html.Div([
    html.Div([
        toc
    ], className="three columns"),
    html.Div([
        html.Div([display_chapter('introduction')], id="chapter")
    ], className="nine columns")
], style={'fontSize': '1.7rem'})


# Run the app
app.component_suites = [
    'dash_html_components',
    'dash_core_components'
]

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
