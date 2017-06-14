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
# Live Updating Components

## The `dash_core_components.Interval` component

Components in Dash usually update through user interaction:
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
    html.Div(examples[0][1], className="example-container"),

dcc.Markdown('''

***

## Updates on Page Load

By default, Dash apps store the `app.layout` in memory. This ensures that the
`layout` is only computed once, when the app starts.

If you set `app.layout` to a function, then you can serve a dynamic layout
on every page load.

For example, if your `app.layout` looked like this:

```
import dash
import dash_html_components as html
import datetime

app.layout = html.H1('The time is: ' + str(datetime.datetime.now()))

if __name__ == '__main__':
    app.run_server()
```

then your app would display the time when the app was started.

If you change this to a function, then a new `datetime` will get computed
everytime you refresh the page. Give it a try:

```
import dash
import dash_html_components as html
import datetime

def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server()
```

You can combine this with [time-expiring caching](/performance) and serve
a unique `layout` every hour or every day and serve the computed `layout`
from memory in between.
''')]
