import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go

from server import app

layout = html.Div(content=[
    html.H4('Interactivity with Callbacks'),
    html.Div('''
    The heart and soul of dash is providing an easy way to bind Python
    callbacks to web interfaces.
    '''),
    html.Div('''
    With Dash's callback decorators, you can update certain components
    when other components change values. Here's a practical example.
    View the interactive app below the code.
    '''),
    dcc.SyntaxHighlighter('''
import dash
from dash_core_components import Dropdown, Graph
from dash_html_components import Div

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.react.Dash('')

# Describe the layout of the app
app.layout = Div([
    Dropdown(
        id='section3-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    Graph(id='section3-graph')
])

# Bind a callback to a dash app with dash's "react" decorator
# The first argument is the ID of the "target" component, the component we want to update.
# The second argument is a list of components that this "target" component depends on.
# Whenever these components change values, e.g. when a dropdown gets fired, dash will
# call this function and provide you with the component's properties or attributes.
# This includes the newly selected value of the dropdown.
# The function will return a new set of properties that will get merged into the target component.
# In this case, the target component is a Graph, so we'll return a `figure` property.
@app.react('section3-graph', ['section3-dropdown'])
def update_graph(dropdown_properties):
    # Get the value of the dropdown
    selected_dropdown_value = dropdown_properties['value']

    # Get some new data from Yahoo finance with Pandas
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )

    # Construct a figure and return it to dash's front-end
    return {
        'figure': go.Figure(
            data=[{
                'x': df.index,
                'y': df.Close
            }]
        )
    }

# Run the server
if __name__ == '__main__':
    app.server.run(debug=True)''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),
    html.Div('This code will generate an app like this:'),

    html.Div([
        dcc.Dropdown(
            id='section3-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Graph(id='section3-graph')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'})
])


@app.react('section3-graph', ['section3-dropdown'])
def update_graph(dropdown_properties):
    selected_dropdown_value = dropdown_properties['value']
    df = web.DataReader(
        selected_dropdown_value, 'yahoo',
        dt(2017, 1, 1), dt.now()
    )
    return {
        'figure': go.Figure(
            data=[{
                'x': df.index,
                'y': df.Close
            }],
            layout=go.Layout(
                margin=go.Margin(
                    l=30,
                    r=0,
                    b=40,
                    t=20
                )
            )
        )
    }
