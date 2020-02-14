import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import datetime
import numpy as np

app = dash.Dash(__name__, suppress_callback_exceptions=True)


def get_newest_data(last_updated_timestamp, current_timestamp):
    # this function returns a list of xaxis date strings
    # between the current time and the last time your dash app updated the graph.
    # It generates random y data for each of those x values but
    # you can replace this function with a query to your database so that
    # the values represent all data newer than the last_updated_timestamp.
    dates = []
    last_updated_timestamp += datetime.timedelta(seconds=1)
    while last_updated_timestamp < current_timestamp:
        last_updated_timestamp += datetime.timedelta(seconds=1)
        dates.append(last_updated_timestamp.strftime("%Y-%m-%d %H:%M:%S"))
    y = np.random.randn(len(dates))
    return dates, y

# create the initial figure
dates = []
for i in range(5):
    new_date = datetime.datetime.now() + datetime.timedelta(seconds=-i)
    dates.append(new_date.strftime("%Y-%m-%d %H:%M:%S"))
dates.reverse()

initial_fig = go.Figure([
    go.Scatter(x=dates, y=np.random.randn(5), marker=dict(color='MidnightBlue')),
    go.Scatter(x=dates, y=np.random.randn(5) + 2, marker=dict(color='LightSkyBlue')),
])

app.layout = html.Div(
        children=[
            dcc.Store(id='time-series-last-updated-store', data=dates[-1]),
            dcc.Graph(id='time-series-graph',
                      figure=initial_fig
                      ),
            dcc.Interval(id='time-series-interval', interval=3000)
        ]
    )


@app.callback([Output('time-series-graph', 'extendData'), Output('time-series-last-updated-store', 'data')],
              [Input('time-series-interval', 'n_intervals')],
              [State('time-series-last-updated-store', 'data')])
def update_graph(n_intervals, last_updated_time_string):

    last_updated_timestamp = datetime.datetime.strptime(last_updated_time_string, "%Y-%m-%d %H:%M:%S")
    current_timestamp = datetime.datetime.now()

    x0_new_points, y0_new_points= get_newest_data(last_updated_timestamp, current_timestamp)
    x1_new_points, y1_new_points = get_newest_data(last_updated_timestamp, current_timestamp)
    extend_data_tuple = (dict(
        x=[x0_new_points, x1_new_points],
        y=[y0_new_points, y1_new_points + 2],
    ), [0, 1])
    return extend_data_tuple, current_timestamp.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    app.run_server(debug=True)
