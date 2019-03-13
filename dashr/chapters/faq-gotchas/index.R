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
# FAQs and Gotchas
> This is the 7th and final chapter of the essential [Dash Tutorial](/).
> The [previous chapter](/faq-gotchas) described how to share data between callbacks.
> The [rest of the Dash documentation](/) covers other topics like multi-page apps and component libraries.
")
  #example of two inputs
  #examples$two_inputs$source,
  #examples$two_inputs$layout,

  #example of one input and two states
  #examples$one_input_two_states$source,
  #examples$one_input_two_states$layout
))
