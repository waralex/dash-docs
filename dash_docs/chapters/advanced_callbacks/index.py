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

    To better understand the order in which callbacks are fired, consider the following example.
    '''),

    rc.Syntax('''
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
from datetime import datetime
import time

app = dash.Dash()
app.layout = html.Div(
    [
        html.Button("start callback chain", id="btn"),
        html.P("first output of callback A", id="p1"),
        html.P("second output of callback A", id="p2"),
        html.P("output of callback B", id="p3"),
        html.P("output of callback C", id="p4"),
    ]
)


@app.callback(
    [Output("p1", "children"), Output("p2", "children")],
    [Input("btn", "n_clicks")],
    prevent_initial_call=True,
)
def first(n):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return ["in callback A it is " + current_time, "in callback A it is " + current_time]


@app.callback(
    Output("p3", "children"), [Input("p2", "children")], prevent_initial_call=True
)
def second(n):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "in callback B it is " + current_time


@app.callback(
    Output("p4", "children"),
    [Input("p1", "children"), Input("p3", "children")],
    prevent_initial_call=True,
)
def third(n, m):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "in callback C it is " + current_time


app.run_server(debug=True)

    '''),


    rc.Markdown('''
    - The `dash-renderer` front-end introspects the app's entire callback chain (1) when an app is initially loaded; (2) when it learns that the value of an input to a callback changes; and (3) when new components are inserted into the app's layout. This is a recursive process: the `dash-renderer` collects not only those callbacks whose inputs changed directly, but also those callbacks whose inputs include outputs of another callback that has already been collected.
      - Once it has collected all the callbacks that it knows will need to fire as the result of a changed input, the `dash-renderer` separates them into two categories: those callbacks which can be fired right away with newly changed values for their inputs and those which are currently blocked from firing because their inputs are the outputs of callbacks that haven't fired yet.
      - In the example above, all three callbacks are collected when the button is clicked since they will all need to fire as a result of the changed input. Callback A is in the first category, while callbacks B and C are in the second. It's important that the `dash-renderer` collects the entire callback chain up front, or else it wouldn't be able tell for sure which callbacks are blocking others.
    - Upon initial load or in the case of callbacks returning `children` with new compononets, none of the inputs are conisidered to have "changed" unless (1) they're outputs of another callback, or (2) the callback is updating something *outside* the new `children` (not possible upon initial load).
      - But, the callback will still be queued as an "initial call", unless ALL of its outputs are outputs of something else- then it's no longer considered an "initial call", but it's still put into the callback queue on the assumption that those outputs will change.
      - To prevent callbacks from firing when an app is initially loaded, you can use the [`prevent_initial_call`](#add link here#) attribute.
    - After they are collected and categorized, callbacks are then executed in the order that their inputs are ready. Many server-side callbacks can be requested simultaneously, if they're all unblocked together- and assuming the program is running on a multi-process server they can execute in parallel.
      - First dispatched are callbacks that have no inputs that are the outputs of another callback.
      - As callbacks return, if their outputs were prevented from updating using `raise PreventUpdate` or `return dash.no_update`, these outputs are removed as "changed" in any other callbacks that they are inputs for. Regardless of which methord is used, they're marked as no longer blocking the other callback.
      - If a callback has no changed inputs and is not an "initial call", then it is removed from the callback queue and all of its outputs are also removed as "changed" in other callbacks, possibly resulting in these callbacks being removed as well.
      - Then, the `dash-renderer` dispatches any callbacks that are no longer blocked by any of their inputs.
      - This process is repeated until the callback collection is empty.
'''),
])
