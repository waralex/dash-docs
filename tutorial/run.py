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
    content = html.Div([
        head,
        html.Div([introduction.layout], id='introduction', style={'display': 'none'}),
        html.Div([getting_started.layout], id='getting-started', style={'display': 'none'}),
        html.Div([html_components.layout], id='html-attributes', style={'display': 'none'}),
        html.Div([core_components.layout], id='supercharged-components', style={'display': 'none'}),
        html.Div([basic_callbacks.layout], id='callbacks', style={'display': 'none'}),
        html.Div([callbacks_with_dependencies.layout], id='callback-resolution', style={'display': 'none'}),
        html.Div([html_component_appendix.layout], id='html-component-library', style={'display': 'none'}),
        html.Div([open_problems.layout], id='open-problems', style={'display': 'none'})
    ])

    content[chapter_id].style = {'display': 'block'}

    return content

toc = html.Div([
    dcc.RadioItems(options=[
        {'label': 'Introduction', 'value': 'introduction'},
        {'label': 'Getting Started', 'value': 'getting-started'},
        {'label': 'HTML Attributes', 'value': 'html-attributes'},
        {'label': 'Supercharged Components', 'value': 'supercharged-components'},
        {'label': 'Basic Callbacks', 'value': 'callbacks'},
        {'label': 'Callback Resolution', 'value': 'callback-resolution'},
        {'label': 'HTML Component Library', 'value': 'html-component-library'},
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
    app.server.run(debug=True)
