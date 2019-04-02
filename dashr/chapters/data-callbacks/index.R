library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

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

One of the core Dash principles explained in the
[Getting Started Guide on Callbacks](/getting-started-part-2)
is that **Dash Callbacks must never modify variables outside of their
scope**. It is not safe to modify any `global` variables.
This chapter explains why and provides some alternative patterns for
sharing state between callbacks.

## Why Share State?

In some apps, you may have multiple callbacks that depend on expensive data
processing tasks like making SQL queries,
running simulations, or downloading data.

Rather than have each callback run the same expensive task,
you can have one callback run the task and then share the
results to the rest of the callbacks.

This need has been somewhat ameliorated now that you can have
[multiple outputs](/getting-started-part-2) for one callback. This way,
that expensive task can be done once and immediately used in all the
outputs. But in some cases this still isn't ideal, for example if there are
simple follow-on tasks that modify the results, like unit conversions. We
shouldn't need to repeat a large database query just to change the results
from Fahrenheit to Celsius!
    "),

    dccMarkdown("
## Why `global` variables will break your app

Dash is designed to work in multi-user environments
where multiple people may view the application at the
same time and will have **independent sessions**.

If your app uses modified `global` variables,
then one user's session could set the variable to one value
which would affect the next user's session.

Dash is also designed to be able to run with **multiple python
workers** so that callbacks can be executed in parallel.
This is commonly done with `gunicorn` using syntax like
```
$ gunicorn --workers 4 app:server
```

(`app` refers to a file named `app.py` and `server` refers to a variable
in that file named `server`: `server = app.server`).

When Dash apps run across multiple workers, their memory
_is not shared_. This means that if you modify a global
variable in one callback, that modification will not be
applied to the rest of the workers.

***

    ")

  # syntax("df <- data.frame(matrix(c(1,2,3,4,1,4,\"x\",\"y\",\"z\"), ncol = 3, nrow = 3))
  #         colnames(df) <- c(\"a\", \"b\", \"c\")
  #
  #        app$layout(htmlDiv(list(
  #         dccDropdown(
  #           id = 'dropdown',
  #           options = [{'label': i, 'value': i} for i in df['c'].unique()],
  #           value = 'a'
  #         ),
  #         htmlDiv(id='output'),
  #        ))
  #
  #        app$callback(
  #           output = list(id='dropdown', property='children'),
  #           params = list(input(id='dropdown', property='value')),
  #           function(value) {
  #              # Here, `df` is an example of a variable that is
  #              # \"outside the scope of this function\".
  #              # *It is not safe to modify or reassign this variable
  #              #  inside this callback.*
  #              gdf <<- df[df['c'] == value]  # do not do this, this is not safe!
  #              return len(df)
  #        })
  #
  #        ''', summary='''
  #        Here is a sketch of an app with a callback that modifies data
  #        out of it's scope. This type of pattern *will not work reliably*
  #        for the reasons outlined above."))

  #example of two inputs
  #examples$two_inputs$source,
  #examples$two_inputs$layout,

  #example of one input and two states
  #examples$one_input_two_states$source,
  #examples$one_input_two_states$layout
))
