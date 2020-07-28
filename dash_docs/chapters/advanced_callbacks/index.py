import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)


layout = html.Div([
    html.H1('Advanced Callbacks'),

    rc.Markdown('''
    ## Catching errors with `PreventUpdate`

    In certain situations, you don't want to update the callback output. You can
    achieve this by raising a `PreventUpdate` exception in the callback function.
    '''),
    rc.Syntax(examples['prevent_update_button.py'][0]),
    rc.Example(examples['prevent_update_button.py'][1]),

    rc.Markdown('''
    ## Displaying errors with `dash.no_update`

    This example illustrates how you can show an error while keeping the previous
    input, using `dash.no_update` to update the output partially.
    '''),
    rc.Syntax(examples['prevent_update.py'][0]),
    rc.Example(examples['prevent_update.py'][1]),

    rc.Markdown('''
    ## Determining which `Input` has fired with `dash.callback_context`

    In addition to event properties like `n_clicks`
    that change whenever an event happens (in this case a click), there is a
    global variable `dash.callback_context`, available only inside a callback.
    It has properties:
    - `triggered`: list of changed properties. This will be empty on initial
      load, unless an `Input` prop got its value from another initial callback.
      After a user action it is a length-1 list, unless two properties of a
      single component update simultaneously, such as a value and a timestamp
      or event counter.
    - `inputs` and `states`: allow you to access the callback params
      by id and prop instead of through the function args. These have the form
      of dictionaries `{ 'component_id.prop_name': value }`

    Here's an example of how this can be done:'''),

    rc.Syntax(examples['last_clicked_button.py'][0]),
    rc.Example(examples['last_clicked_button.py'][1]),
    rc.Markdown('''
    ### Legacy behaviour: using timestamps

    Prior to v0.38.0, you needed to compare timestamp properties like
    `n_clicks_timestamp` to find the most recent click. While existing uses of
    `*_timestamp` continue to work for now, this approach is deprecated, and
    may be removed in a future update. The one exception is
    `modified_timestamp` from `dcc.Store`, which is safe to use, it is NOT
    deprecated.

    ------------------------
    '''),

    rc.Markdown('''
    ## Improving performance with memoization

    Memoization allows you to bypass long computations by storing the
    results of function calls.

    To better understand how memoization works, let's start with a simple example.

'''),

    rc.Syntax('''
import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
    '''),

    rc.Markdown('''
    Calling `slow_function('test')` the first time will take 10 seconds.
    Calling it a second time with the same argument will take almost no time
    since the previously computed result was saved in memory and reused.

    The [Performance](/performance) section of the Dash docs delves a
    little deeper into leveraging multiple processes and threads in
    conjunction with memoization to further improve performance.
    '''),

    rc.Markdown('''
    ## The Callback Chain

    - Upon initial load of a Dash app or based on later interactions, all of the related callbacks are collected, based on both the existence of newly-created outputs and newly-changed inputs.
      - This is a recursive process: Dash collects not only those callbacks whose inputs changed directly, but also those callbacks whose inputs include outputs of another callback that has already been collected. It's important that Dash collects the entire callback chain up front, or else it wouldn't be able tell for sure which callbacks are blocking others.
        - For example, dropdown (A) is an input for for one callback (X) that sets the value of dropdown (B). A second callback, (Y) has both (A) and (B) as inputs and outputs to store (C). A third callback (Z) uses the store to create a graph (D). All three callbacks are collected, but (Y) is blocked until (X) completes and (Z) is blocked until (Y) completes.
      - Upon initial load or in the case of callbacks returning `children` with new compononets, none of the inputs are conisidered to have "changed" unless (1) they're outputs of another callback, or (2) the callback is updating something *outside* the new `children` (not possible upon initial load).
      - But, the callback will still be queued as an "initial call", unless ALL of its outputs are outputs of something else- then it's no longer considered an "initial call", but it's still put into the callback queue on the assumption that those outputs will change.
    - Callbacks are then executed in the order that their inputs are ready. Many server-side callbacks can be requested simultaneously, if they're all unblocked together- and assuming the program is running on a multi-process server they can execute in parallel.
      - First dispatched are callbacks that have no inputs that are the outputs of another callback.
      - As callbacks return, if their outputs were prevented from updating using `raise PreventUpdate` or `return dash.no_update`, these are removed as "changed" in any other callbacks that they are inputs for. Either way, they're marked as no longer blocking the other callback.
      - If a callback has no changed props and is not an "initial call", then it is removed from the callback queue and all of its outputs are also removed as "changed" in other callbacks, possibly resulting in these callbacks being removed as well.
      - Then, Dash dispatches any callbacks that are no longer blocked by any of their inputs.
      - This process is repeated until the callback queue is empty.


'''),
])
