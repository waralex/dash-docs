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
    html.Pre(id='hover-data', style={'border': 'thin lightgrey solid'}),

    dcc.Markdown("""
    **Click Data**

    Click on points in the graph to see this data update.
    """),
    html.Pre(id='click-data', style={'border': 'thin lightgrey solid'}),

    dcc.Markdown("""
    **Selction Data**

    Choose the lasso or rectangle tool in the graph's menu
    bar and then select points in the graph to see this
    data update.
    """),
    html.Pre(id='selected-data', style={'border': 'thin lightgrey solid'}),
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

                        # text appears on hover
                        'text': ['a', 'b', 'c', 'd'],

                        # customdata doesn't appear in the graph
                        # but it is available in the event data.
                        'customdata': [
                            'extra', 'metadata', 'for each', 'point'
                        ],
                        'name': 'Trace 1',
                        'mode': 'markers',
                        'marker': {'size': 12},
                        'customdata': ['x', 'y', 'z', 'w']
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
        """),
        html.Pre(id='click-data', style={'border': 'thin lightgrey solid'}),

        dcc.Markdown("""
**Selction Data**

Choose the lasso or rectangle tool in the graph's menu
bar and then select points in the graph to see this
data update.
        """),
        html.Pre(id='selected-data', style={'border': 'thin lightgrey solid'}),
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


layout.extend([
dcc.Markdown('''

***

## Crossfiltering Between Graphs

One of the really powerful things that you can do with these types of
variables is cross filtering between charts, allowing you to interact
with multiple dimensions of data across multiple views at once.

Here's a simple example.

In this example, we use the `customdata` property to add extra
metadata for the points that we've hovered over or selected.
'''),

dcc.SyntaxHighlighter('''import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import math

app = dash.Dash(__name__)

# Get data
df = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'plotly/datasets/master/'
    'gapminderDataFiveYear.csv')

# Get a list of unique years in the dataframe
years = sorted(list(df.year.unique()))

layout = html.Div([
        html.Div([
            dcc.Graph(id='graph-left', animate=True),
        ], className='six columns'),
        html.Div([
            dcc.Graph(id='graph-right', animate=True)
        ], className='six columns')
    ], className='row'),
    dcc.Slider(
        id='year-slider',
        marks={
            i: str((str(i) if (i-2) % 10 == 0 else ''))
            for i in years
        },
        value=1952, min=years[0], max=years[-1]
    )
])

# Common figure generation function shared by both callbacks
def create_figure(year, selectedData, hoverData, yaxis_column):
    if selectedData is None:
        selectedData = {'points': []}
    if hoverData is None:
        hoverData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in selectedData['points'] + hoverData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df[yaxis_column],
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': [
                    1.0
                    if (j in filtered_countries or
                        len(filtered_countries) == 0)
                    else 0.3
                    for j in list(continent_df.country)
                ],
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(120*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'annotations': [{
                'x': 0, 'xref': 'paper', 'xanchor': 'left',
                'y': 1, 'yref': 'paper', 'yancor': 'bottom',
                'text': year,
                'font': {'size': 16}, 'showarrow': False
            }],
            'legend': {
                'x': 1, 'xanchor': 'right',
                'y': 0, 'yanchor': 'bottom',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'lasso'
        }
    }


@app.callback(
    Output('graph-left', 'figure'),
    [Input('year-slider', 'value'),
     Input('graph-right', 'selectedData'),
     Input('graph-right', 'hoverData')])
def filterScatterPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'lifeExp')
    figure['layout']['yaxis'] = {
        'title': 'Life Expectancy',
        'range': [10, 90], 'autorange': False
    }
    return figure


@app.callback(
    Output('graph-right', 'figure'),
    [Input('year-slider', 'value'),
     Input('graph-left', 'selectedData'),
     Input('graph-left', 'hoverData')])
def filterScatterPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'pop')
    figure['layout']['yaxis'] = {
        'title': 'Population', 'type': 'log',
        'range': [math.log10(100), math.log10(10*1000*1000*1000)],
        'autorange': False
    }
    return figure

''', customStyle=styles.code_container)

])

import pandas as pd
import math

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

years = sorted(list(df.year.unique()))
layout.extend([html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='graph-left', animate=True),
        ], className='six columns'),
        html.Div([
            dcc.Graph(id='graph-right', animate=True)
        ], className='six columns')
    ], className='row'),
    dcc.Slider(
        id='year-slider',
        marks={
            i: str((str(i) if (i-2) % 10 == 0 else ''))
            for i in years
        },
        value=1952, min=years[0], max=years[-1],
        dots=False
    )
], style=dict({'paddingBottom': '30px'}, **styles.example_container))])


def create_figure(year, selectedData, hoverData, yaxis_column):
    if selectedData is None:
        selectedData = {'points': []}
    if hoverData is None:
        hoverData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in selectedData['points'] + hoverData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df[yaxis_column],
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': [
                    1.0
                    if (j in filtered_countries or len(filtered_countries) == 0)
                    else 0.3
                    for j in list(continent_df.country)
                ],
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(120*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'annotations': [{
                'x': 0, 'xref': 'paper', 'xanchor': 'left',
                'y': 1, 'yref': 'paper', 'yancor': 'bottom',
                'text': year,
                'font': {'size': 16}, 'showarrow': False
            }],
            'legend': {
                'x': 1, 'xanchor': 'right',
                'y': 0, 'yanchor': 'bottom',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'lasso'
        }

    }


@app.callback(
    Output('graph-left', 'figure'),
    [Input('year-slider', 'value'),
     Input('graph-right', 'selectedData'),
     Input('graph-right', 'hoverData')])
def filterScatterPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'lifeExp')
    figure['layout']['yaxis'] = {
        'title': 'Life Expectancy',
        'range': [10, 90], 'autorange': False
    }
    return figure


@app.callback(
    Output('graph-right', 'figure'),
    [Input('year-slider', 'value'),
     Input('graph-left', 'selectedData'),
     Input('graph-left', 'hoverData')])
def filterScatterPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'pop')
    figure['layout']['yaxis'] = {
        'title': 'Population', 'type': 'log',
        'range': [math.log10(100), math.log10(10*1000*1000*1000)],
        'autorange': False
    }
    return figure

layout.extend([
dcc.Markdown('''

This graph is highly interactive. Hovering over values will trigger our
callbacks and highlight the associated point (country) in the other graph.

The exact same filtering operation occurs if you select multiple points
by clicking and dragging on the plot with the lasso. The slider ties it
together by filtering the data by selected year.

***

It's also possible to update the same the graph in response to these events.
Here's another take on this dataset. Hovering over a value will replot the
chart with that country's historical trajectory.
'''),

    dcc.SyntaxHighlighter('''import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import math

app = dash.Dash(__name__)

df = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'plotly/datasets/master/'
    'gapminderDataFiveYear.csv')
years = sorted(list(df.year.unique()))

app.layout = html.Div([
    dcc.Graph(id='graph-with-history', animate=True),
    dcc.Slider(
        id='year-slider-2',
        marks={
            i: str((str(i) if (i-2) % 10 == 0 else ''))
            for i in years
        },
        value=1952, min=years[0], max=years[-1]
    )
])



@app.callback(
    Output('graph-with-history', 'figure'),
    [Input('graph-with-history', 'hoverData'),
     Input('graph-with-history', 'selectedData'),
     Input('year-slider-2', 'value')])
def filterTimeSeries(hoverData, selectedData, year):
    if hoverData is None:
        hoverData = {'points': []}
    if selectedData is None:
        selectedData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in hoverData['points'] + selectedData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df.lifeExp,
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    for country in filtered_countries:
        country_df = df[df.country == country]
        traces.append({
            'x': country_df.gdpPercap,
            'y': country_df.lifeExp,
            'hoverinfo': 'skip',
            'mode': 'lines',
            'line': {'width': 1, 'color': 'grey'},
            'name': country
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(100*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'legend': {
                'x': 0, 'xanchor': 'left',
                'y': 1, 'yanchor': 'top',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'select'
        }
    }


''', customStyle=styles.code_container),

    html.Div([
        dcc.Graph(id='graph-with-history', animate=True),
        dcc.Slider(
            id='year-slider-2',
            marks={
                i: str((str(i) if (i-2) % 10 == 0 else ''))
                for i in years
            },
            value=1952, min=years[0], max=years[-1]
        )
    ], style=dict({'paddingBottom': '30px'}, **styles.example_container))
])


@app.callback(
    Output('graph-with-history', 'figure'),
    [Input('graph-with-history', 'hoverData'),
     Input('graph-with-history', 'selectedData'),
     Input('year-slider-2', 'value')])
def filterTimeSeries(hoverData, selectedData, year):
    if hoverData is None:
        hoverData = {'points': []}
    if selectedData is None:
        selectedData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in hoverData['points'] + selectedData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df.lifeExp,
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    for country in filtered_countries:
        country_df = df[df.country == country]
        traces.append({
            'x': country_df.gdpPercap,
            'y': country_df.lifeExp,
            'hoverinfo': 'skip',
            'mode': 'lines',
            'line': {'width': 1, 'color': 'grey'},
            'name': country
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(100*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'legend': {
                'x': 0, 'xanchor': 'left',
                'y': 1, 'yanchor': 'top',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'select'
        }
    }
