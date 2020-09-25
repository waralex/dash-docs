# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import numpy as np
import holoviews as hv
from holoviews.plotting.plotly.dash import holoviews_to_dash

frequencies = [0.5, 0.75, 1.0, 1.25]

def sine_curve(phase, freq):
    xvals = [0.1* i for i in range(100)]
    return hv.Curve((xvals, [np.sin(phase+freq*x) for x in xvals]))

# When run live, this cell's output should match the behavior of the GIF below
dmap = hv.DynamicMap(sine_curve, kdims=['phase', 'frequency'])
dmap = dmap.redim.range(phase=(0.5, 1), frequency=(0.5, 1.25))

# Create App
app = dash.Dash(__name__)

# Dash display
components = holoviews_to_dash(app, [dmap])

app.layout = html.Div(
    [components.graphs[0],
     components.kdims["phase"],  # Phase slider
     components.kdims["frequency"],  # Frequency Slider
     components.store]
)

if __name__ == '__main__':
    app.run_server(debug=True)
