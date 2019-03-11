# library(dashCoreComponents)
# library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  two_inputs=utils$LoadExampleCode('dashr/chapters/state/examples/two_inputs.R'),
  one_input_two_states=utils$LoadExampleCode('dashr/chapters/state/examples/one_input_two_states.R')
)



layout <- htmlDiv(list(
  coreMarkdown("
# Dash State
> This is the 4th chapter of the
> Dash Tutorial.
> The [previous chapter](/getting-started-part-2) covered Dash
> Callbacks and the [next chapter](/state)
> covers interactive graphing and
> crossfiltering.
> Just getting started?
> Make sure to
> [install the necessary dependencies](/installation).

In the previous chapter on [basic Dash callbacks](/getting-started),
our callbacks looked something like:
"),
  #example of two inputs
  examples$two_inputs$source,
  examples$two_inputs$layout,
  
  #example of one input and two states
  examples$one_input_two_states$source,
  examples$one_input_two_states$layout
))
