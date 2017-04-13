from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
from pyorbital.orbital import Orbital
import datetime
import plotly

import styles
from server import app

from tools import load_example

examples = [load_example(s) for s in [
    'tutorial/examples/live_updates.py'
]]


layout = [dcc.Markdown('''
## Live Updating Graphs

Components in dash usually update through user interaction:
selecting a dropdown, dragging a slider, hovering over points.

If you're building an application for monitoring, you may want to update
components in your application every few seconds or minutes.

The `dash_core_components.Interval` element allows you to update components
on a predefined interval.

This example pulls data from live satellite feeds and updates the graph
and the text every second.
'''),
    dcc.SyntaxHighlighter(
        examples[0][0],
        language='python',
        customStyle={'borderLeft': 'thin solid lightgrey'}
    ),
    html.Div(examples[0][1], style=styles.example_container)
]
