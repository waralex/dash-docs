import dash_core_components as dcc

from dash_docs.tutorial.components import Syntax
from dash_docs import tools
from dash_docs import reusable_components

examples = {
    'extend_data': tools.load_example(
        'tutorial/examples/performance_extend_data.py'),
}


layout = [
    reusable_components.Markdown('''# Data Transfer

Any time a callback is triggered, the data for all the `Input`
and `State` props defined in the callback is transferred from
the client's browser to your dash app. This could be a lot of
time if one of those `Input` props is a `dcc.Store` component
containing a large dataset.

In this section we will go over several ways to reduce the
amount of data transferred in each callback including:

1. Updating a graph using `extendData`.

### Updating a graph using `extendData`

It is often desirable to live update a graph and, for cases
where you only need to add some new data points to an existing
trace, using `extendData` will be the most efficient way to go
about this. The below example uses a callback to update the
`extendData` prop for the 'time-series-graph`. This prop is
updated with a tuple:
- The first element of the tuple is a `dict` with `x` and `y` as keys.
The values of those keys will be a list of lists of points
to be updated.
- The second element of the tuple is a list of traces to be updated.
'''),

    Syntax(examples['extend_data'][0]),
    examples['extend_data'][1]
]
