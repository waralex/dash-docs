import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles


def Syntax(children,
           style=styles.code_container,
           summary=''):
    if summary:
        return html.Details([
            html.Summary(summary),
            dcc.Markdown(
                children,
                style=style
            )
        ], open=True)
    else:
        return dcc.Markdown(
            children,
            style=style
        )


def Example(example):
    return html.Div(example, className='example-container')
