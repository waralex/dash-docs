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
> This is the 5th chapter of the [Dash Tutorial](/).
> The [previous chapter](/state) covered callbacks with `State` and
> the [next chapter](/data-callbacks) describes how to share data between callbacks.
> Just getting started?
> Make sure to [install the necessary dependencies](/getting-started).

"),
  # Example of interactive visualizations 1
  examples$interactive_graph_1$source,
  examples$interactive_graph_1$layout

  # Example of interactive visualizations 2
  #examples$interactive_graph_2$source,
  #examples$interactive_graph_2$layout
))
