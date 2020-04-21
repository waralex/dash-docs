import dash_html_components as html
from .import Markdown
from textwrap import dedent
from .Markdown import Markdown
import copy

def CreateDisplay(scope):
    def Display(example_string, use_exec=False):
        scope_copy = copy.copy(scope)
        if 'result = ' in example_string:
            exec(dedent(example_string), scope_copy)
            result = scope_copy['result']
            example_string = example_string.replace('result = ', 'app.layout = ')
        else:
            result = eval(dedent(example_string), scope)
        return html.Div([
            Markdown(
                '```python  \n' + dedent(example_string).strip() + '\n```',
                style={'marginBottom': 10, 'borderLeft': 'thin #C8D4E3 solid'}
            ),
            result
        ])
    return Display
