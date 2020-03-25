import dash_core_components as dcc
import dash_html_components as html

from .Markdown import Markdown
from dash_docs import styles


def Syntax(children, style=styles.code_container, summary=''):
    code = children
    if not code.startswith('```'):
        code = '```py\n' + code + '\n```'

    if summary:
        return html.Details([
            html.Summary(summary),
            Markdown(code, style=style)
        ], open=True)
    else:
        return Markdown(code, style=style)
