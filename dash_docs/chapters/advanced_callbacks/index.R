library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dash_docs/utils.R', local=utils)

examples <- list(
  prevent_update_button=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/prevent_update_button.R'),
  prevent_update=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/prevent_update.R'),
  last_clicked_button=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/last_clicked_button.R')
)

layout <- htmlDiv(
  list(
    # htmlH1('Advanced Callbacks'),
    dccMarkdown("
## Catching errors with `dashNoUpdate()`
In certain situations, you don't want to update the callback output. You can
achieve this by returning a `dashNoUpdate()` in the callback function.
  "),

    examples$prevent_update_button$source_code,
    examples$prevent_update_button$layout,

    dccMarkdown("
## Displaying errors with `dashNoUpdate()`
This example illustrates how you can show an error while keeping the previous
input, using `dashNoUpdate()` to update the output partially.
  "),

    examples$prevent_update$source_code,
    examples$prevent_update$layout,

    dccMarkdown("
## Determining which `Input` has fired with `callback_context()`
In addition to event properties like `n_clicks` that change whenever
an event happens (in this case a click), there is a global variable
`app$callback_context()`, available only inside a callback. It has properties:

  - `triggered`:  list of changed properties.
This will be empty on initial load, unless an `input` prop got its value from
another initial callback.
After a user action it is a length-1 list,
unless two properties of a single component update simultaneously,
such as a value and a timestamp or event counter.

   - `inputs` and `states`: allow you to access the callback params by id and prop instead of through the function args.
These have the form of dictionarie `app$callback_context()$triggered$value`

Here's an example of how this can be done:
  "),

    examples$last_clicked_button$source,
    examples$last_clicked_button$layout,

    dccMarkdown("
### Legacy behavior: Using timestamps
Prior to the addition of `callback_context`, you needed to compare timestamp properties
like `n_clicks_timestamp` to find the most recent click.
While existing uses of `*_timestamp` continue to work for now, this approach is deprecated,
and may be removed in a future update. The one exception is `modified_timestamp` from `dccStore`,
which is safe to use, it is NOT deprecated.
  "),

    dccMarkdown("
## Improving performance with memoization
Memoization allows you to bypass long computations by storing the results of function calls.

To better understand how memoization works, let's start with a simple example.
  "),

    dccMarkdown("
```r
library(memoise)

# We can start by memoising the function sys.sleep
memoised_sleep <- memoise::memoise(Sys.sleep)

# The first time it is called will take the full 10 seconds
memoised_sleep(10)

# The second time it will instantly execute.
memoised_sleep(10)
```
    "),

    dccMarkdown("
Calling `memoised_sleep(10)` the first time will take 10 seconds.
Calling it a second time with the same argument will take almost no time
since the previously computed result was saved in memory and reused.

The [Performance](/performance) section of the Dash docs delves a
little deeper into leveraging multiple processes and threads in
conjunction with memoization to further improve performance.
"),

dccMarkdown('''
    ## The Callback Chain

    - Upon initial load of a Dash app or based on later interactions, all of the related callbacks are collected, based on both the existence of newly-created outputs and newly-changed inputs.
      - Upon initial load or in the case of callbacks returning `children` with new compononets, none of the inputs are conisidered to have "changed" unless (1) they're outputs of another callback, or (2) the callback is updating something *outside* the new `children` (not possible upon initial load).
      - But, the callback will still be queued as an "initial call", unless ALL of its inputs are outputs of something else- then it's no longer considered an "initial call", but it's still put into the callback queue on the assumption that those inputs will change.
    - Callbacks are then executed in the order that their inputs are ready.
      - First dispatched are callbacks that have no inputs that are the outputs of another callback.
      - As callbacks return, if their outputs were prevented from updateing, these are removed as "changed" in any other callbacks that they are inputs for. Either way, they're marked as no longer blocking the other callback.
      - If a callback has no changed props and is not an "initial call", then it is removed from the callback queue.
      - Then, Dash dispatches any callbacks that are no longer blocked by any of their inputs.
      - This process is repeated until the callback queue is empty.


'''),

    htmlHr(),
    dccMarkdown("
[Back to the Table of Contents](/)
                ")
  )
)
