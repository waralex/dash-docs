import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tools import load_example
from components import Example, Syntax

examples = {
    'simple-graph-events': load_example(
        'tutorial/examples/graph_callbacks_simple.py'),
    'world-indicators': load_example(
        'tutorial/examples/getting_started_crossfilter.py'
    )
}

layout = html.Div([
    dcc.Markdown('''
    # Interactive Visualizations

    The `dash_core_components` library includes a component called `Graph`.

    `Graph` renders interactive data visualizations using the open source
    [plotly.js](https://github.com/plotly/plotly.js) JavaScript graphing
    library. Plotly.js supports over 35 chart types and renders charts in
    both vector-quality SVG and high-performance WebGL.

    The `figure` argument in the `dash_core_components.Graph` component is
    the same `figure` argument that is used by `plotly.py`, Plotly's
    open source Python graphing library.
    Check out the [plotly.py documentation and gallery](https://plot.ly/python)
    to learn more.

    Dash components are described declaratively by a set of attributes.
    All of these attributes can be updated by callback functions but only
    a subset of these attributes are updated through user interaction.
    For example, when you click on an option in a `dcc.Dropdown` component, the
    `value` property of that component changes.

    The `dcc.Graph` component has four attributes that can change
    through user-interaction: `hoverData`, `clickData`, `selectedData`,
    `relayoutData`.
    These properties update when you hover over points, click on points, or
    select regions of points in a graph.

    '''.replace('    ', '')),

    Syntax(
        examples['simple-graph-events'][0],
        summary="""
            Here's an simple example that
            prints these attributes in the screen.
    """),
    Example(examples['simple-graph-events'][1]),

    Syntax(examples['world-indicators'][0], summary="""
    Let's update our world indicators example by displaying time series when
    we hover over points in our scatter plot.
    """),
    Example(examples['world-indicators'][1]),

    dcc.Markdown(s('''
    ***

    The final chapter of the Dash tutorial explains one last concept of dash:
    Callbacks with `dash.dependencies.State`.
    `State` is useful for UIs that contain forms or buttons.
    ''')),

    dcc.Link('Dash Tutorial Part 4. Callbacks With State', href="/dash/state")

])
