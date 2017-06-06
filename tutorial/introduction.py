import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, Event, State
import datetime
from pyorbital.orbital import Orbital
import os

from server import app

layout = html.Div([
    dcc.Markdown('''
        ## Dash User Guide

        Dash is a productive python framework for building web applications.

        Written on top of Plotly.js and React.js,
        Dash is ideal for building data visualization apps
        with highly custom user interfaces.

        This is an exclusive developer preview of Dash.
        Dash is currently unreleased and unannounced.
        Please do not share Dash without Plotly's constent.

        The core functionality of Dash will be open sourced.
        For enterprises, Plotly offers a platform for
        deploying, orchestrating, and permissioning dash apps behind
        your firewall. If you're interested,
        please get in touch at
        [https://plot.ly/products/consulting-and-oem/](https://plot.ly/products/consulting-and-oem/)
        to register for early access.

        ***

        ### Why Dash?

        Learn more about dash from our talk at
        [Plotcon](https://plotcon.plot.ly).

    '''.replace('  ', '')),

    html.Iframe(
        width="100%",
        height="480",
        style={'border': 'none'},
        src="https://www.youtube-nocookie.com/embed/5BAthiN0htc?rel=0"
    )
])
