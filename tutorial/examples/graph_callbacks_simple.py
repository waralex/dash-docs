import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
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
        html.Pre(id='hover-data', style={'border': 'thin lightgrey solid'}),

        dcc.Markdown("""
        **Click Data**

        Click on points in the graph to see this data update.
    """.replace('    ', '')),
    html.Pre(id='click-data', style={'border': 'thin lightgrey solid'}),

    dcc.Markdown("""
        **Selction Data**

        Choose the lasso or rectangle tool in the graph's menu
        bar and then select points in the graph to see this
        data update.
    """.replace('    ', '')),
    html.Pre(id='selected-data', style={'border': 'thin lightgrey solid'}),
])


@app.callback(
    Output('hover-data', 'content'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'content'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(
    Output('selected-data', 'content'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)
