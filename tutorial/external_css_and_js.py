# -*- coding: utf-8 -*-
import dash_core_components as dcc
from dash_html_components import *

layout = Div([
    H3('All About CSS and Javascript Bundles in Dash'),

    Div('''
    The component libraries that you use with dash, like `dash_core_components`
    and `dash_html_components`, are python packages that include Javascript
    and CSS bundles.'''),

    Div('''
    Dash automatically checks which javascript and CSS bundles are necessary
    to render the application.
    '''),

    Div('''
    Some of this functionality is customizable and extendable.
    This chapter includes some common customizations.
    '''),

    Hr(),

    H4('Including custom CSS and Javascript in your dash app'),

    dcc.SyntaxHighlighter('''from dash.react import Dash

app = Dash('')

# Append an externally hosted CSS stylesheet
my_css_url = "https://unpkg.com/normalize.css@5.0.0"
app.css.append_css({
    "external_url": my_css_url
})

# Append an externally hosted JS bundle
my_js_url = 'https://unkpg.com/some-npm-package.js'
app.scripts.append_script({
    "external_url": my_js_url
})''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),

    Div('''Dash currently only supports loading CSS and Javascript bundles
    that are externally hosted.'''),

    Hr(),

    H4('Rendering dash apps offline'),

    Div('''
    The Javascript and CSS bundles that are included in
    Dash component libraries are hosted on the web
    (on the unpkg CDN) and in the Python packages that you install.
    '''),

    Div('''
    By default, dash serves the Javascript and CSS resources from the
    online CDNs. This is usually much faster than loading the resources
    from the file system.
    '''),

    Div('''
    However, if you are working in an offline or firewalled environment or
    if the CDN is unavailable, then your dash app itself can serve these
    files. These files are stored as part of the component's site-packages
    folder.
    '''),

    Div('''
    Here's how to enable this option:
    '''),

    dcc.SyntaxHighlighter('''from dash.react import Dash

app = Dash('')

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True''',
    language='python',
    customStyle={'borderLeft': 'thin grey solid'})
])
