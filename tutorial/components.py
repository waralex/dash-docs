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
                '``` python  \n' + children + '  \n ```',
                style=style
            )
        ], open=True)
    else:
        return dcc.Markdown(
            '``` python  \n' + children + '  \n ```',
            style=style
        )


def Example(example):
    return html.Div(example, className='example-container')
