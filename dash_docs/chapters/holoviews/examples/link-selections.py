# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from plotly.data import iris

import holoviews as hv
from holoviews import opts
from holoviews.plotting.plotly.dash import holoviews_to_dash

# Load dataset
df = iris()
dataset = hv.Dataset(df)

# Build selection linking object
selection_linker = hv.selection.link_selections.instance()
scatter = selection_linker(
    hv.Scatter(dataset, kdims=["sepal_length"], vdims=["sepal_width"])
)
hist = selection_linker(
    hv.operation.histogram(dataset, dimension="petal_width", normed=False)
)

# Use plot hook to set the default drag mode to box selection
def set_dragmode(plot, element):
    fig = plot.state
    fig['layout']['dragmode'] = "select"

scatter.opts(opts.Scatter(hooks=[set_dragmode]))
hist.opts(opts.Histogram(hooks=[set_dragmode]))

app = dash.Dash(__name__)
components = holoviews_to_dash(
    app, [scatter, hist], reset_button=True
)

app.layout = html.Div(
    [
        components.graphs[0],
        components.graphs[1],
        components.resets[0],
        components.store
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
