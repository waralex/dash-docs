# -*- coding: utf-8 -*-
import dash
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask
import json
import plotly.graph_objs as go

server = Flask(__name__)
print(__name__)
app = Dash(__name__, server=server)

app.config.supress_callback_exceptions = True
