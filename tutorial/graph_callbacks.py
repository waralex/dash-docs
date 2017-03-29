import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import json

import styles
from server import app

layout = [dcc.Markdown('''
# Graph Callbacks

Dash renders graphs using the interactive
[plotly.js](https://github.com/plotly/plotly.js) graphing library.

Plotly.js graphs are natively interactive.
- Hover over points to see their values
- Click and drag on the graph to zoom into regions
- Double click to zoom out
- Shift + Click + Drag to pan regions
- Select points using the lasso or the rectangle in the graph bar

With dash, these events update the `Graph` component's
`clickData`, `hoverData`, and `selectedData` values.

By setting those properties as `Input` properties, you can
update your Dash application in response to these events.

'''),
    dcc.SyntaxHighlighter('''import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json

app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [
                {
                    'x': [1, 2, 3, 4],
                    'y': [4, 1, 3, 5],
                    'text': ['a', 'b', 'c', 'd'],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 12}
                },
                {
                    'x': [1, 2, 3, 4],
                    'y': [9, 4, 1, 4],
                    'text': ['w', 'x', 'y', 'z'],
                    'name': 'Trace 2',
                    'mode': 'markers',
                    'marker': {'size': 12}
                }
            ]
        }
    ),

    # display the result of the interactions
    # of the graph in these divs
    dcc.Markdown("""
    **Hover Data**

    Mouse over values in the graph to see this data update.
    """),
    html.Pre(id='hover-data', style={'border': 'thin grey solid'}),

    dcc.Markdown("""
    **Click Data**

    Click on points in the graph to see this data update.
    """),
    html.Pre(id='click-data', style={'border': 'thin grey solid'}),

    dcc.Markdown("""
    **Selction Data**

    Choose the lasso or rectangle tool in the graph's menu
    bar and then select points in the graph to see this
    data update.
    """),
    html.Pre(id='selected-data', style={'border': 'thin grey solid'}),
])

@app.callback(
    Output('hover-data', 'content'),
    [Input('my-graph', 'hoverData')]
)
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'content'),
    [Input('my-graph', 'clickData')]
)
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

@app.callback(
    Output('selected-data', 'content')
    [Input('my-graph', 'selectedData')]
)
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

''', customStyle=styles.code_container),

    html.Div([
        dcc.Graph(
            id='my-graph-callback',
            figure={
                'data': [
                    {
                        'x': [1, 2, 3, 4],
                        'y': [4, 1, 3, 5],
                        'text': ['a', 'b', 'c', 'd'],
                        'name': 'Trace 1',
                        'mode': 'markers',
                        'marker': {'size': 12}
                    },
                    {
                        'x': [1, 2, 3, 4],
                        'y': [9, 4, 1, 4],
                        'text': ['w', 'x', 'y', 'z'],
                        'name': 'Trace 2',
                        'mode': 'markers',
                        'marker': {'size': 12}
                    }
                ]
            }
        ),

        # display the result of the interactions
        # of the graph in these divs
        dcc.Markdown("""
**Hover Data**

Mouse over values in the graph to see this data update.
        """),
        html.Pre(id='hover-data', style={'border': 'thin grey solid'}),

        dcc.Markdown("""
**Click Data**

Click on points in the graph to see this data update.
        """),
        html.Pre(id='click-data', style={'border': 'thin grey solid'}),

        dcc.Markdown("""
**Selction Data**

Choose the lasso or rectangle tool in the graph's menu
bar and then select points in the graph to see this
data update.
        """),
        html.Pre(id='selected-data', style={'border': 'thin grey solid'}),
    ], style=styles.example_container)
]


@app.callback(
    Output('hover-data', 'content'),
    [Input('my-graph-callback', 'hoverData')]
)
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'content'),
    [Input('my-graph-callback', 'clickData')]
)
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(
    Output('selected-data', 'content'),
    [Input('my-graph-callback', 'selectedData')]
)
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)
