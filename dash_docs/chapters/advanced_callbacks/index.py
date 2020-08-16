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
        html.Button("execute callbacks", id="btn"),
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
def a(n):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return ["in callback A it is " + current_time, "in callback A it is " + current_time]


@app.callback(
    Output("p3", "children"), [Input("p2", "children")], prevent_initial_call=True
)
def b(n):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "in callback B it is " + current_time


@app.callback(
    Output("p4", "children"),
    [Input("p1", "children"), Input("p3", "children")],
    prevent_initial_call=True,
)
def c(n, m):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "in callback C it is " + current_time


app.run_server(debug=True)

    '''),


    rc.Markdown('''
    - Determining whether or not a network request is sent to the server to execute a callback is handled by the [`dash-renderer`](https://github.com/plotly/dash/tree/dev/dash-renderer). This is the client-side front-end of every Dash app, written using the React.js library.
    - Once a Dash app is initially loaded by a web browser, the `dash-renderer` introspects the entire app's callback chain in order to understand which callbacks need to be executed when a user interacts with a Dash component. When a Dash component changes state (for example, the `n_clicks` attribute of a button increases by 1 because a user clicked it), this change is communicated to the `dash-renderer` by the component (to learn more about how Dash components communicate their state to the `dash-renderer`, see http://dash.plotly.com/react-for-python-developers).
    - When the `dash-renderer` learns that an input to a callback has changed, it looks for every callback that depends on that input and groups them in a collection. In this collection, callbacks are then grouped into two categories: those that can be executed right away and those that are blocked from executing because they depend on inputs which have not yet changed. This process occurs before the first network request is made by the `dash-renderer` front-end client to the Dash back-end server.
    - After they are collected and categorized, callbacks are then executed in the order that their inputs are ready. Many server-side callbacks can be requested simultaneously, if they're all unblocked together. Whether or not these requests are executed in a synchronous or asyncrounous manner depends on the specific setup of the Dash back-end server. If it is running in a multi-threaded environment, then all of the callbacks can be executed simultaneously, in which case they will return values to the `dash-renderer` based on their speed of execution. In a single-threaded environment, they will be executed and returned in the order they are received.
      - First dispatched are callbacks that have no inputs that are the outputs of another callback.
      - As callbacks return, if their outputs were prevented from updating using `raise PreventUpdate` or `return dash.no_update`, these outputs are removed as "changed" in any other callbacks that they are inputs for. Regardless of which methord is used, they're marked as no longer blocking the other callback.
      - If a callback has no changed inputs and is not an "initial call", then it is removed from the callback collection and all of its outputs are also removed as "changed" in other callbacks, possibly resulting in these callbacks being removed as well.
      - Then, the `dash-renderer` dispatches any callbacks that are no longer blocked by any of their inputs.
      - This process is repeated until the callback collection is empty. When the `dash-renderer` receives the output of a callback, it once again goes over the collection of callbacks it has grouped to determine if this new output allows for callbacks that were previously blocked to be executed.
      -
    - In the example code above, when the button is clicked, all three callbacks are collected.
      - Callback A is placed in the first category while callbacks B and C are placed in the second category. This is because callback A can be executed right away since it only depends on the newly changed `n_clicks` attribute of the button, which is immediately available. Callback B is blocked from executing because it depends on an input that will only change once callback A has been executed, and callback C is blocked because it is blocked from executing because it depends on inputs that will only change when both callbacks A and B have been executed.
      - Since only callback A is not blocked, it gets executed first. Once it executes, that allows callback B to be executed with its newly changed input value, leading to another network request. Finally, callback C can be executed with a final network request.
    - It is important to note that this process occurs upon intital load of a Dash app as well. If you want to suppress this behavior, see the documentation for the `prevent_initial_call` attribute of callbacks. 
    - Upon initial load or in the case of callbacks returning `children` with new compononets, none of the inputs are considered to have "changed" unless (1) they're outputs of another callback, or (2) the callback is updating something *outside* the new `children` (not possible upon initial load).
      - But, the callback will still be queued as an "initial call", unless ALL of its outputs are outputs of something else- then it's no longer considered an "initial call", but it's still put into the callback collection on the assumption that those outputs will change.
'''),
])
