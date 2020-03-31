import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools, styles
from dash_docs import reusable_components as rc
from textwrap import dedent

examples = tools.load_examples(__file__)

layout = html.Div([

    html.H1('Dynamic Callbacks'),

    rc.Markdown(
    '''
    🎉 New in Dash 1.11.0!

    The dynamic callback selectors `MATCH` & `ALL` allow you to write
    callbacks that respond to or update an arbitrary number of elements.

    ## Simple Example with `ALL`

    This example renders an arbitrary number of `dcc.Dropdown` elements
    and the callback is fired whenever any of the `dcc.Dropdown` elements
    change. Try adding a few dropdowns and selecting their values to see how
    the app updates.
    '''
    ),

    rc.Syntax(examples['simple_all.py'][0]),

    rc.Example(examples['simple_all.py'][1], style={'overflowX': 'initial'}),

    rc.Markdown(
    '''
    Some notes about this example:
    - Notice how the `id` in `dcc.Dropdown` is a _dictionary_ rather than a _string_.
    This is a new feature that we enabled for dynamic callbacks
    (previously, IDs had to be strings).
    - In our second callback, we have `Input({'type': 'dropdown', 'index': ALL}, 'value')`.
    This means "match any input that has an ID dictionary where `'type'` is `'dropdown'`
    and `'index'` is _anything_. Whenever the `value` property of any of the
    dropdowns change, send _all_ of their values to the callback."
    - The keys & values of the ID dictionary (`type`, `index`, `filter-dropdown`)
    are arbitrary. This could've be named `{'foo': 'bar', 'baz': n_clicks}`.
    - However, for readability, we recommend using keys like `type`, `index`, or `id`.
    `type` can be used to refer to the class or set dynamic components and
    `index` or `id` could be used to refer _which_ component you are matching
    within that set. In this example, we just have a single set of dynamic
    components but you may have multiple sets of dynamic components in more
    complex apps or if you are using `MATCH` (see below).
    - In fact, in this example, we didn't actually _need_ `'type': 'filter-dropdown'`.
    The same callback would have worked with `Input({'index': ALL})`.
    We included `'type': 'filter-dropdown'` as an extra specifier in case you
    create multiple sets of dynamic components.
    - The compontent properties themselves, in this case `value`, are not dynamic.
    Only the IDs are dynamic.
    '''
    ),

    rc.Markdown(
    '''
    ## Simple Example with `MATCH`

    Like `ALL`, `MATCH` will fire the callback when any of the
    component's properties change. However, instead of passing _all_ of the
    values into the callback, `MATCH` will pass just a single value into the
    callback.

    In this example, whenever a dropdown changes, its associated output
    component is updated.
    '''
    ),

    rc.Syntax(examples['simple_match.py'][0]),

    rc.Example(examples['simple_match.py'][1], style={'overflowX': 'initial'}),

    html.H2('TODO App'),

    rc.Markdown(
    '''
    Creating a Todo App is a classic UI exercise in that demonstrates many
    features in common "create, read, update and delete" (CRUD) applications.
    '''
    ),

    rc.Syntax(examples['todo.py'][0]),

    rc.Example(examples['todo.py'][1]),

])
