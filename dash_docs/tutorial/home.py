# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash_docs.chapter_index import URLS

from dash_docs.reusable_components import TOC
from dash_docs.tools import merge

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

layout = TOC(URLS)
