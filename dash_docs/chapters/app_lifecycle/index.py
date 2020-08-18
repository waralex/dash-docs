import dash_core_components as dcc
import dash_html_components as html
from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div(children=[
    rc.Markdown('''# Dash App Life Cycle

    This section describes the lifecyle of a Dash app.

    ## Initial Load

    When a Dash app is loaded into a web browser by the `dash-renderer`, the app's callback chaiin is introspected to determine the relationships between inputs, callbacks, and outputs.

    ## Initial Call

    Once the `dash-renderer` has introspected the entire callback chain, all callbacks that have inputs in currently the app layout are executed. This is known as the "initial call" of the callbacks, and this behavior can be suppressed by using the `prevent_initial_call" attribute.

    ## User Interaction Triggers Callbacks

    Components in the layout communicate with the `dash-renderer` whenever their state changes. When this occurs, the `dash-renderer` looks to see which callbacks need to be executed as a response to the user input. This can include both callbacks that use the input directly and callbacks whose inputs are outputs of callbacks that use the input directly.

    Since the `dash-renderer` has introspected the entire callback chain, it can delay the execution of callbacks whose inputs are outputs of callbacks that use the input directly until after callbacks that use the input directly have executed. This minimizes the number of requests the `dash-renderer` needs to make to the server in response to a particular user input.

    ## (Optional) New Components Are Added The Layout

    In some cases, callbacks insert new components into the Dash app's layout. If these new components are inputs to callback functions, then their appearance in the layout triggers the execution of those callbacks.

''')
])
