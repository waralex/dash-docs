import dash_html_components as html
from .import Markdown
from textwrap import dedent
from .Markdown import Markdown

def CreateDisplay(scope):
    def Display(example_string):
        return html.Div([
            Markdown(
                '```python  \n ' + dedent(example_string).strip() + '  \n```',
                style={'marginBottom': 10, 'borderLeft': 'thin #C8D4E3 solid'}
            ),
            eval(dedent(example_string), scope)
        ])
    return Display
