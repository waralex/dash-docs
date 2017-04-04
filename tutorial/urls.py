# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import styles
from server import app

layout = [dcc.Markdown('''
## URLs

Dash renders web applications as a "single-page app". This means that
the application does not completely reload when the user navigates the
application, making browsing very fast.

Navigation is supported through Dash's native callbacks by
simply hiding and showing content in response to clicking on links,
radio buttons, or tabs.

For example, here is a simple "navigation" implementation using
radio buttons.
'''),

dcc.SyntaxHighlighter('''app.layout = html.Div([
    dcc.RadioItems(options=[
        {'label': i, 'value': i} for i in ['Chapter 1', 'Chapter 2']
    ], value='Chapter 1',
    id='navigation-links'),
    html.Div(id='body')
])

@app.callback(Output('body', 'content'), [Input('navigation-links', 'value')])
def display_content(chapter):
    if chapter == 'Chapter 1':
        return Div('Welcome to Chapter 1')
    elif chapter == 'Chapter 2':
        return Div('Welcome to Chapter 2')
''', language='python', customStyle=styles.code_container),
html.Div([
    dcc.RadioItems(options=[
        {'label': i, 'value': i} for i in ['Chapter 1', 'Chapter 2']
    ], value='Chapter 1', id='navigation-links-urls'),
    html.Div(id='body-urls')
], id='urls-example', style=styles.example_container),

dcc.Markdown('''
Hiding and showing content like this gives the effect of
navigating to new pages.

The second part of navigation is updating the browser's navigation bar
with a new URL and loading the correct content when the user navigates
to a particular URL pathname.

Dash supports URLs like this by mapping values in the application's state
to named URL paths. When the application's state matches an entry in these
routes, Dash will update the address bar with the matching pathname.

If an application is loaded with a pathname in the URL, then dash will
look up the state that is associated with that URL and prefill the initial
controls with that state.

This mapping between state and URL pathnames is done through an application
variable named `routes`. In this example, navigating to `/chapter-1`
will prefill the RadioItem's value with the `Chapter 1` value and
navigating to `/chapter-2` will prefil its value with `Chapter 2`.
As you click between these values in the radio item, the browser's
URL path will get updated with the associated pathname without preloading
the page.
'''),

dcc.SyntaxHighlighter('''app.layout = html.Div([
    dcc.RadioItems(options=[
        {'label': i, 'value': i} for i in ['Chapter 1', 'Chapter 2']
    ], value='Chapter 1',
    id='navigation-links'),
    html.Div(id='body')
])


app.routes = [
    {
        # The relative URL pathname that this entry is synced with
        'pathname': '/chapter-1',
        'state': {
            # The key is the ID and the property combined with a '.',
            # the value is the value of that ID and property.
            'toc.value': 'Chapter 1'
        }
    },

    {
        'pathname': '/chapter-2',
        'state': {
            'toc.value': 'Chapter 2'
        }
    }
]

@app.callback(Output('body', 'content'), [Input('navigation-links', 'value')])
def display_content(chapter):
    if chapter == 'Chapter 1':
        return Div('Welcome to Chapter 1')
    elif chapter == 'Chapter 2':
        return Div('Welcome to Chapter 2')''',
language='python',
customStyle=styles.code_container
),

dcc.Markdown('''
This is experimental beta behaviour. The interface may change slightly but
the concepts will remain the same.
''')]


@app.callback(
    Output('body-urls', 'content'),
    [Input('navigation-links-urls', 'value')])
def display_content(chapter):
    if chapter == 'Chapter 1':
        return html.Div('Welcome to Chapter 1')
    elif chapter == 'Chapter 2':
        return html.Div('Welcome to Chapter 2')
