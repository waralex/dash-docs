# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, Event, State
import styles
from tools import load_example

source, _example_layout = load_example('tutorial/examples/getting_started.py')

layout = html.Div([
    html.Strong('Installation'),
    html.Div('''
        In your terminal, install several dash libraries.
        These libraries are under active development,
        so install and upgrade frequently.
        Note that dash currently only supports Python 2.7.
        3.x will be supported in the stable release.
    '''),
    dcc.SyntaxHighlighter('''$ pip install dash.ly=={}  # The core dash backend
$ pip install dash-renderer=={}  # The dash front-end
$ pip install dash-html-components=={}  # HTML components
$ pip install dash-core-components=={}  # Supercharged components
$ pip install pandas_datareader # Pandas extension used in some examples
'''.format(dash.__version__,
           dash_renderer.__version__,
           html.__version__,
           dcc.__version__),
          language='bash',
          customStyle={'borderLeft': 'thin solid lightgrey'}
    ),

    html.Strong('Hello World'),
    html.Div('''
        Here's a quick example to get you started.
        In a file called app.py, write:
    '''),
    dcc.SyntaxHighlighter(
        source,
        language='python',
        customStyle={'borderLeft': 'thin solid lightgrey'}
    ),
    dcc.Markdown('''
    Run the app with

    ```
    $ python app.py
    ...Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

    and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    in your web browser.
    '''.replace('    ', '')),

    html.Div(_example_layout, style=styles.example_container)
])
