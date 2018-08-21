# -*- coding: utf-8 -*-
from dash import Dash

from flask import Flask, redirect

import os


server = Flask(__name__, static_url_path='/static', static_folder='./static')
server.secret_key = os.environ.get('secret_key', 'secret')

app = Dash(
    __name__,
    server=server
)

app.css.config.serve_locally = False
app.scripts.config.serve_locally = False
app.config.suppress_callback_exceptions = True

@app.server.route('/deployment/on-premise')
def redirectDDS():
    return redirect("/dash-deployment-server", code=302)
