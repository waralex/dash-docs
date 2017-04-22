import dash
from dash.dependencies import Event, Output
import dash_html_components as html

app = dash.Dash(__name__)
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    html.Button('Click to load content', id='display-content-button'),
    html.Div('-', id='display-content')
])


# When you click the button, this content gets loaded
@app.callback(
    Output('display-content', 'content'),
    events=[Event('display-content-button', 'click')])
def render():
    return html.Div([
        html.H3('Hello Dash')
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
