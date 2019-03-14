library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  hello.world=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-world.R'),
  hello.dash2=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-dash-components.R'),
  hello.table=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-table.R'),
  hello.bubble=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-bubble.R'),
  hello.markdown=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-markdown.R'),
  hello.dcc=utils$LoadExampleCode('dashr/chapters/getting-started/examples/hello-dcc.R'),
  dropdown.doc=utils$LoadExampleCode('dashr/chapters/getting-started/examples/markdown-doc-dropdown.R')
)

layout <- htmlDiv(list(
  dccMarkdown("
# Dash Layout
> This is the 2nd chapter of the
> [Dash Tutorial](/).
> The [previous chapter](/installation)
> covered installation
> and the [next chapter](/getting-started-part-2) covers Dash callbacks.


This tutorial will walk you through a fundamental aspect of Dash apps, 
the app `layout_set`, through 6 self-contained apps.
"),
  
htmlBr(),

dccMarkdown("
Dash apps are composed of two parts.
The first part is the \"`layout_set`\" of the app and 
it describes what the application looks like. 
The second part describes the interactivity of the application 
and will be covered in the [next chapter](/getting-started-part-2).


Dash provides R classes for all of the visual components of the application. 
We maintain a set of components in the `dash_core_components` 
and the `dash_html_components` library 
but you can also [build your own](https://github.com/plotly/dash-components-archetype) with JavaScript and React.js.


To get started, create a file named `app.py` with the following code:
"),
examples$hello.world$source_code,
  
dccMarkdown("
Run the app with

   ```
   $ Rscript index.R
   Fire started at 127.0.0.1:8080
   start: 127.0.0.1:8080
   ```
  "),
  # hello markdown example
  dccMarkdown("
and visit [http:127.0.0.1:8050/](http:127.0.0.1:8050/)
in your web browser. You should see an app that looks like this.
  "),
  examples$hello.world$layout,

  dccMarkdown("
Note:
1. The `layout_set` is composed of a tree of \"components\" like `htmlDiv`
and `dccGraph`.
2. The `dash_html_components` library has a component for every HTML
tag. The `htmlH1(children='Hello Dash')` component generates
a `<h1>Hello Dash</h1>` HTML element in your application.
3. Not all components are pure HTML. The `dash_core_components` describe
higher-level components that are interactive and are generated with
JavaScript, HTML, and CSS through the React.js library.
4. Each component is described entirely through keyword attributes.
Dash is _declarative_: you will primarily describe your application
through these attributes.
5. The `children` property is special. By convention, it's always the
first attribute which means that you can omit it:
`htmlH1(children='Hello Dash')` is the same as `htmlH1('Hello Dash')`.
Also, it can contain a string, a number, a single component, or a
list of components.
6. The fonts in your application will look a little bit different than
what is displayed here. This application is using a
custom CSS stylesheet to modify the default styles of the elements.
You can learn more in the [css tutorial](/external-resources),
but for now you can initialize your app with
```
dash_css <- htmltools::htmlDependency(
name = \"dash-css\",
version = \"1.0.0\",
src = c(href = \"https://codepen.io/chriddyp/pen\"),
stylesheet = \"bWLwgP.css\"
)

app$dependencies_set(dash_css())
```
to get the same look and feel of these examples.

### Making your first change

**New in dash 0.30.0 and dash-renderer 0.15.0**
Dash includes \"hot-reloading\", this features is activated by default when
you run your app with `app$run_server(debug=True)`. This means that DashR
will automatically refresh your browser when you make a change in your code.
Give it a try: change the title \"Hello Dash\" in your application or change the `x` or the `y` data. Your app should auto-refresh with your change.
> Don't like hot-reloading? You can turn this off with `app.run_server(dev_tools_hot_reload=False)`. 
> Learn more in [Dash Dev Tools documentation](/devtools) Questions? See the [community forum hot reloading discussion](https://community.plot.ly/t/announcing-hot-reload/14177).
#### More about HTML
The `dash_html_components` library contains a component class for every
HTML tag as well as keyword arguments for all of the HTML arguments.

Let's customize the text in our app by modifying the inline styles of the components:
  "),

  # hello layout example
  examples$hello.dash2$source_code,
  examples$hello.dash2$layout,

  dccMarkdown("
In this example, we modified the inline styles of the `htmlDiv`
and `htmlH1` components with the `style` property.
`htmlH1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'})`
is rendered in the Dash application as
`<h1 style=\"text-align: center; color: #7FDBFF\">Hello Dash</h1>`.
There are a few important differences between the `dash_html_components`
and the HTML attributes:
1. The `style` property in HTML is a semicolon-separated string. In Dash,
you can just supply a dictionary.
2. The keys in the `style` dictionary are [camelCased](https://en.wikipedia.org/wiki/Camel_case).
So, instead of `text-align`, it's `textAlign`.
3. The HTML `class` attribute is `className` in Dash.
4. The children of the HTML tag is specified through the `children` keyword
argument. By convention, this is always the _first_ argument and
so it is often omitted.
Besides that, all of the available HTML attributes and tags are available
to you within your Python context.
***
#### Reusable Components
By writing our markup in Python, we can create complex reusable
components like tables without switching contexts or languages.

Here's a quick example that generates a `Table` from a Pandas dataframe.
  "),
  # hello table example
  examples$hello.table$source_code,
  examples$hello.table$layout,

  dccMarkdown("
#### More about Visualization
The `dash_core_components` library includes a component called `Graph`.
`Graph` renders interactive data visualizations using the open source
[plotly.js](https://github.com/plotly/plotly.js) JavaScript graphing
library. Plotly.js supports over 35 chart types and renders charts in
both vector-quality SVG and high-performance WebGL.
The `figure` argument in the `dash_core_components.Graph` component is
the same `figure` argument that is used by `plotly.py`, Plotly's
open source Python graphing library.
Check out the [plotly.py documentation and gallery](https://plot.ly/python)
to learn more.
  "),
  # hello scater example
  examples$hello.bubble$source_code,
  examples$hello.bubble$layout,

  dccMarkdown("
*These graphs are interactive and responsive.
**Hover** over points to see their values,
**click** on legend items to toggle traces,
**click and drag** to zoom,
**hold down shift, and click and drag** to pan.*
#### Markdown
While Dash exposes HTML through the `dash_html_components` library,
it can be tedious to write your copy in HTML.
For writing blocks of text, you can use the `Markdown` component in the
`dash_core_components` library.
  "),

  # hello dmarkdown example
  examples$hello.markdown$source_code,
  examples$hello.markdown$layout,

  dccMarkdown("
#### Core Components
The `dash_core_components` includes a set of higher-level components like
dropdowns, graphs, markdown blocks, and more.
Like all Dash components, they are described entirely declaratively.
Every option that is configurable is available as a keyword argument
of the component.

Here are a few of the available components:
  "),

  # hello dcc example
  examples$hello.dcc$source_code,
  examples$hello.dcc$layout,

  # dropdown help with example
  # examples$dropdown.doc$source_code,
  examples$dropdown.doc$layout,

  dccMarkdown("
#Summary
The layout of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. The dash_html_components library provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, className, and id. The dash_dcc_components library generates higher-level components like controls and graphs.
For reference, see:
- [dash_core_components gallery](https://dash.plot.ly/dash-core-components)
- [dash_html_components gallery](https://dash.plot.ly/dash-html-components)


The next part of the Dash tutorial covers how to make these apps interactive.

Dash Tutorial Part 3: Basic Callbacks
[Back to the Table of Contents](/getting-started-part-2)
  ")
))
