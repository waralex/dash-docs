import dash_html_components as html

import performance
import urls
import live_updates

layout = html.Div([
    html.H1('Advanced Features'),
    html.Hr(),
    html.Div(performance.layout),
    html.Hr(),
    html.Div(urls.layout),
    html.Hr(),
    html.Div(live_updates.layout)
])
