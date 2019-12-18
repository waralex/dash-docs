import dash_html_components as html

from dash_docs import styles
from . import Markdown

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
