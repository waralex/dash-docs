import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import functools32
import time

app = dash.Dash(__name__)
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    html.Div(id='memoized-content'),
    dcc.RadioItems(
        id='memoized-dropdown',
        options=[
            {'label': 'Option {}'.format(i), 'value': 'Option {}'.format(i)}
            for i in range(1, 4)
        ],
        value='Option 1'
    )
])


# When you click the button, this content gets loaded
@app.callback(
    Output('memoized-content', 'content'),
    [Input('memoized-dropdown', 'value')])
@functools32.lru_cache()
def render(value):
    time.sleep(2)
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
