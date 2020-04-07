import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools, styles
from dash_docs import reusable_components as rc
from textwrap import dedent

examples = tools.load_examples(__file__)

layout = html.Div([

    html.H1('Pattern-Matching Callbacks'),

    rc.Markdown(
    '''
    New in Dash 1.11.0!

    The pattern-matching callback selectors `MATCH`, `ALL`, & `ALLSMALLER`
    allow you to write callbacks that respond to or update an
    arbitrary or dynamic number of components.

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
    This is a new feature that we enabled for pattern-matching callbacks
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
    The same callback would have worked with `Input({'index': ALL}, 'value')`.
    We included `'type': 'filter-dropdown'` as an extra specifier in case you
    create multiple sets of dynamic components.
    - The component properties themselves (e.g. `value`) cannot be matched by
    a pattern, only the IDs are dynamic.
    - This example uses a common pattern with `State` - the currently displayed
    set of dropdowns within the `dropdown-container` component are passed into
    the callback when the button is clicked. Within the callback, the new
    dropdown is appended to the list and then returned.
    '''
    ),

    rc.Markdown(
    '''
    ## Simple Example with `MATCH`

    Like `ALL`, `MATCH` will fire the callback when any of the
    component's properties change. However, instead of passing _all_ of the
    values into the callback, `MATCH` will pass just a single value into the
    callback. Instead of updating a single output, it will update the dynamic
    output that is "matched" with.
    '''
    ),

    rc.Syntax(examples['simple_match.py'][0]),

    rc.Example(examples['simple_match.py'][1], style={'overflowX': 'initial'}),

    rc.Markdown(
    '''
    Notes about this example:
    - The `display_dropdowns` callback returns two elements with the _same_
    `index`: a dropdown and a div.
    - The second callback uses the `MATCH` selector. With this selector,
    we're asking Dash to:

      1. Fire the callback whenever the `value` property of any component
      with the id `'type': 'dynamic-dropdown'` changes:
      `Input({'type': 'dynamic-dropdown', 'index': MATCH}, 'value')`
      2. Update the component with the id `'type': 'dynamic-output'`
      and the `index` that _matches_ the same `index` of the input:
      `Output({'type': 'dynamic-output', 'index': MATCH}, 'children')`
      3. Pass along the `id` of the dropdown into the callback:
      `State({'type': 'dynamic-dropdown', 'index': MATCH}, 'id')`
    - With the `MATCH` selector, only a _single_ value is passed into the callback
    for each `Input` or `State`. This is unlike the previous example with the
    `ALL` selector where Dash passed _all_ of the values into the callback.
    - Notice how it's important to design IDs dictionaries that "line up" the
    inputs with outputs. The `MATCH` contract is that Dash will update
    whichever output has the same dynamic ID as the id. In this case, the
    "dynamic ID" is the value of the `index` and we've designed our layout to
    return dropdowns & divs with identical values of `index`.
    - In some cases, it may be important to know _which_ dynamic component changed.
    As above, you can access this by setting `id` as `State` in the callback.
    '''
    ),

    rc.Markdown('## Simple Example with `ALLSMALLER`'),

    rc.Markdown(
    '''
    In the example below, `ALLSMALLER` is used to pass in the values of
    all of the dropdowns on the page that have an index smaller than the
    index corresponding to the div.

    The user interface in the example below displays filter results that are
    increasingly specific in each as we apply each additional dropdown.

    `ALLSMALLER` can only be used in `Input` and `State` items, and
    must be used on a key that has `MATCH` in the `Output` item(s).

    `ALLSMALLER` it isn't always necessary (you can usually use `ALL` and
    filter out the indices in your callback) but it will make your logic simpler.
    '''
    ),


    rc.Syntax(examples['simple_allsmaller.py'][0]),

    rc.Example(examples['simple_allsmaller.py'][1]),

    rc.Markdown(
    '''
    - In the example above, try adding a few filters and then change the first
    dropdown. Notice how changing this dropdown will update the text
    of each `html.Div` that has an index that depends on that dropdown.
    - That is, each `html.Div` will get updated whenever any of the
    dropdowns with an `index` smaller than it has changed.
    - So, if there are 10 filters added and the first dropdown has changed, Dash
    will fire your callback 10 times, once to update each `html.Div` that depends
    on the `dcc.Dropdown` that changed.
    '''
    ),

    html.H2('Todo App'),

    rc.Markdown(
    '''
    Creating a Todo App is a classic UI exercise in that demonstrates many
    features in common "create, read, update and delete" (CRUD) applications.
    '''
    ),

    rc.Syntax(examples['todo.py'][0]),

    rc.Example(examples['todo.py'][1]),

])
