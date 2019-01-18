import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape
from tutorial.utils.convert_props_to_table import generate_prop_table


layout = html.Div([
    html.H1('Dash Cytoscape Reference'),
    # generate_prop_table('Cytoscape', dash_cytoscape)
    html.Div(className='cytoscapeReference', children=dcc.Markdown("""A Cytoscape component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- className (string; optional): Sets the class name of the element (the value of an element's html
class attribute).
- style (dict; optional): Add inline styles to the root element.
- elements (list; optional): A list of dictionaries representing the elements of the networks.
    1. Each dictionary describes an element, and specifies its purpose.
        - `group` (string): Either 'nodes' or 'edges'. If not given, it's automatically inferred.
        - `data` (dictionary): Element specific data.
             - `id` (string): Reference to the element, useful for selectors and edges. Randomly assigned if not given.
             - `label` (string): Optional name for the element, useful when `data(label)` is given to a style's `content` or `label`. It is only a convention.
             - `parent` (string): Only for nodes. Optional reference to another node. Needed to create compound nodes.
             - `source` (string): Only for edges. The id of the source node, which is where the edge starts.
             - `target` (string): Only for edges. The id of the target node, where the edge ends.
        - `position` (dictionary): Only for nodes. The position of the node.
             - `x` (number): The x-coordinate of the node.
             - `y` (number): The y-coordinate of the node.
        - `selected` (boolean): If the element is selected upon initialisation.
        - `selectable` (boolean): If the element can be selected.
        - `locked` (boolean): Only for nodes. If the position is immutable.
        - `grabbable` (boolean): Only for nodes. If the node can be grabbed and moved by the user.
        - `classes` (string): Space separated string of class names of the element. Those classes can be selected by a style selector.

    2. The [official Cytoscape.js documentation](http://js.cytoscape.org/#notation/elements-json) offers an extensive overview and examples of element declaration.
- stylesheet (list; optional): A list of dictionaries representing the styles of the elements.
- layout (dict; optional): A dictionary specifying how to set the position of the elements in your
graph. * The `'name'` key is required, and indicates which layout (algorithm) to
use.
- pan (dict; optional): Dictionary indicating the initial panning position of the graph. The
following keys are accepted:
- zoom (number; optional): The initial zoom level of the graph. You can set `minZoom` and
`maxZoom` to set restrictions on the zoom level.
- panningEnabled (boolean; optional): Whether panning the graph is enabled (i.e., the position of the graph is
mutable overall).
- userPanningEnabled (boolean; optional): Whether user events (e.g. dragging the graph background) are allowed to
pan the graph.
- minZoom (number; optional): A minimum bound on the zoom level of the graph. The viewport can not be
scaled smaller than this zoom level.
- maxZoom (number; optional): A maximum bound on the zoom level of the graph. The viewport can not be
scaled larger than this zoom level.
- zoomingEnabled (boolean; optional): Whether zooming the graph is enabled (i.e., the zoom level of the graph
is mutable overall).
- userZoomingEnabled (boolean; optional): Whether user events (e.g. dragging the graph background) are allowed
to pan the graph.
- boxSelectionEnabled (boolean; optional): Whether box selection (i.e. drag a box overlay around, and release it
to select) is enabled. If enabled, the user must taphold to pan the graph.
- autoungrabify (boolean; optional): Whether nodes should be ungrabified (not grabbable by user) by
default (if true, overrides individual node state).
- autolock (boolean; optional): Whether nodes should be locked (not draggable at all) by default
(if true, overrides individual node state).
- autounselectify (boolean; optional): Whether nodes should be unselectified (immutable selection state) by
default (if true, overrides individual element state).
- autoRefreshLayout (boolean; optional): Whether the layout should be refreshed when elements are added or removed.
- tapNode (dict; optional): The complete node dictionary returned when you tap or click it.
- tapNodeData (dict; optional): The data dictionary of a node returned when you tap or click it.
- tapEdge (dict; optional): The complete edge dictionary returned when you tap or click it.
- tapEdgeData (dict; optional): The data dictionary of an edge returned when you tap or click it.
- mouseoverNodeData (dict; optional): The data dictionary of a node returned when you hover over it.
- mouseoverEdgeData (dict; optional): The data dictionary of an edge returned when you hover over it.
- selectedNodeData (list; optional): The list of data dictionaries of all selected nodes (e.g. using
Shift+Click to select multiple nodes, or Shift+Drag to use box selection).
- selectedEdgeData (list; optional): The list of data dictionaries of all selected edges (e.g. using
Shift+Click to select multiple nodes, or Shift+Drag to use box selection).
"""))
])
