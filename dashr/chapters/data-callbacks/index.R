# library(dashCoreComponents)
# library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  #two_inputs=utils$LoadExampleCode('dashr/chapters/state/examples/two_inputs.R'),
  #one_input_two_states=utils$LoadExampleCode('dashr/chapters/state/examples/one_input_two_states.R')
)

layout <- htmlDiv(list(
  dccMarkdown("
# Sharing State Between Callbacks
> This is the 6th chapter of the essential [Dash Tutorial](/). The [previous chapter](/graph-crossfiltering) 
> covered how to use callbacks with the `dashCoreComponents.Graph` component. 
> The [rest of the Dash documentation](/) covers other topics like multi-page apps and component libraries. 
> Just getting started? Make sure to [install the necessary dependencies](/installation). 
> The [next and final chapter](/faq-gotchas) covers frequently asked questions and gotchas.

")
  #example of two inputs
  #examples$two_inputs$source,
  #examples$two_inputs$layout,
  
  #example of one input and two states
  #examples$one_input_two_states$source,
  #examples$one_input_two_states$layout
))
