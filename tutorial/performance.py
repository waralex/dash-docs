import dash_html_components as html
import dash_core_components as dcc
import functools32

import styles
import tools

examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/performance_memoization.py',
        'tutorial/examples/performance_flask_caching.py'
    ]
]


layout = [
dcc.Markdown('''# Performance

This chapter contains several recommendations for improving the performance
of your dash apps.

The main performance limitation of dash apps is likely the callbacks in
the application code itself. If you can speed up your callbacks, your app
will feel snappier.

### Memoization

Since Dash's callbacks are functional in nature (they don't contain any state),
it's easy to add memoization caching. Memoization stores the results of a
function after it is called and re-uses the result if the function is called
with the same arguments.

If you're using Python 3,
you can use the built-in [functools.lrucache](https://docs.python.org/3/library/functools.html).

If you're using Python 2, you can import a backport called [functools32](https://github.com/MiCHiLU/python-functools32).

Here is a simple example

```
import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
```

Calling `slow_function('test')` the first time will take 10 seconds.
Calling it a second time with the same argument will take almost no time
since the result was reused.

You can use this in your dash apps by just wrapping your callbacks:

```
@app.callback(...)
@functools32.lru_cache(maxsize=32)
def update_graph(...):
    ...
```

Here's an example. Try changing values in the dropdown.
If there is a 2 second delay, then it means that no one has selected that
value before. If there isn't, then someone has already selected that value
and the cached version of the result was available.

'''),

dcc.SyntaxHighlighter(
    examples[0][0], language='python', customStyle=styles.code_container
),
html.Div(examples[0][1], className="example-container"),

dcc.Markdown('''

Note that `lru_cache` is entirely in memory. If your app is running with
multiple workers, each worker will have its own cache.

There are a few cases where this `lru_cache` isn't a good solution.
If your callbacks perform a computation that necessarily incorporates
randomness, then you may not want cache the results.

If your callbacks fetch data that is time-varying, then you may want to a
cache that allows expiration. For example, you could expire the cache on an
hourly or daily basis.

The [Flask-Caching](https://pythonhosted.org/Flask-Caching/) library allows
time-based expiry and also stores the cache on the filesystem or
in a shared memory database like Redis instead of in the worker's memory.
This means that it may be a little bit slower than `lru_cache` but the cache
will be shared across workers.'''),

dcc.SyntaxHighlighter(
    examples[1][0], language='python', customStyle=styles.code_container
),
html.Div(examples[1][1], className="example-container"),

dcc.Markdown('''

***

### Graphs

[Plotly.js](https://github.com/plotly/plotly.js) is pretty fast out of the box.

Most plotly charts are rendered with SVG. This provides crisp rendering,
publication-quality image export, and wide browser support.
Unfortunately, rendering graphics in SVG can be slow for large datasets
(like those with more than 5k-10k points).
To overcome this limitation, plotly.js has WebGL alternatives to
some chart types. WebGL uses the GPU to render graphics.

The high performance, WebGL alternatives include:
- `scattergl`: A webgl implementation of the `scatter` chart type. [Examples](https://plot.ly/python/webgl-vs-svg/), [reference](https://plot.ly/python/reference/#scattergl)
- `pointcloud`: A lightweight version of `scattergl` with limited chart. [Reference](https://plot.ly/python/reference/#pointcloud)
    attributes but even faster rendering. [Reference](https://plot.ly/python/reference/#pointcloud)
- `heatmapgl`: A webgl implementation of the `heatmap` chart type. [Reference](https://plot.ly/python/reference/#heatmapgl)

Currently, dash redraws the entire graph on update using the `plotly.js`
`newPlot` call. The performance of updating a chart could be improved
considerably by introducing `restyle` calls into this logic. If you or
your company would like to sponsor this work,
[get in touch](https://plot.ly/products/consulting-and-oem/).

***

### Sponsoring Performance Enhancements

There are many other ways that we can improve the performance of dash apps,
like caching front-end requests, pre-filling the cache, improving plotly.js's
webgl capabilities, reducing javascript bundle sizes, and more.

Historically, many of these performance related features have been funded
through company sponorship. If you or your company would like to sponsor
these types of enhancements, [please get in touch](https://plot.ly/products/consulting-and-oem/),
we'd love to help.

***''')
]
