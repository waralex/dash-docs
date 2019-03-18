library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  interactive_graph_1 = utils$LoadExampleCode('dashr/chapters/graph-crossfiltering/examples/interactive-graph-1.R'),
  interactive_graph_2 = utils$LoadExampleCode('dashr/chapters/graph-crossfiltering/examples/interactive-graph-2.R')
)



layout <- htmlDiv(list(
  dccMarkdown("
# Interactive Visualizations

> This is the *5th* chapter of the [Dash Tutorial](/).
> The [previous chapter](/state) covered callbacks with `State`
> and the [next chapter](/sharing-data-between-callbacks) describes how to
> share data between callbacks.
> Just getting started? Make sure to [install the necessary dependencies](/installation).

The `dashCoreComponents` library includes a component called `Graph`.

`Graph` renders interactive data visualizations using the open source
[plotly.js](https://github.com/plotly/plotly.js) JavaScript graphing
library. Plotly.js supports over 35 chart types and renders charts in
both vector-quality SVG and high-performance WebGL.

The `figure` argument in the `dashCoreComponents.Graph` component is
the same `figure` argument that is used by `plotly.py`, Plotly's
open source Python graphing library.
Check out the [plotly.py documentation and gallery](https://plot.ly/r/)
to learn more.

Dash components are described declaratively by a set of attributes.
All of these attributes can be updated by callback functions, but only
a subset of these attributes are updated through user interaction, such as  
when you click on an option in a `dccDropdown` component and the
`value` property of that component changes.

The `dccGraph` component has four attributes that can change
through user-interaction: `hoverData`, `clickData`, `selectedData`,
`relayoutData`.
These properties update when you hover over points, click on points, or
select regions of points in a graph.
"),
  # Example of interactive visualizations 1
  examples$interactive_graph_1$source,
  examples$interactive_graph_1$layout,

  # Example of interactive visualizations 2
  examples$interactive_graph_2$source,
  examples$interactive_graph_2$layout,
  
  dccLink(
    'Dash Tutorial Part 6. Sharing Data Between Callbacks',
    href='/data-callbacks'
  )
))
