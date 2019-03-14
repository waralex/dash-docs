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

dcc.Markdown("
Note:
1. The `layout` is composed of a tree of \"components\" like `html.Div`
and `dcc.Graph`.
2. The `dash_html_components` library has a component for every HTML
tag. The `html.H1(children='Hello Dash')` component generates
a `<h1>Hello Dash</h1>` HTML element in your application.
3. Not all components are pure HTML. The `dash_core_components` describe
higher-level components that are interactive and are generated with
JavaScript, HTML, and CSS through the React.js library.
4. Each component is described entirely through keyword attributes.
Dash is _declarative_: you will primarily describe your application
through these attributes.
5. The `children` property is special. By convention, it's always the
first attribute which means that you can omit it:
 `html.H1(children='Hello Dash')` is the same as `html.H1('Hello Dash')`.
Also, it can contain a string, a number, a single component, or a
list of components.
6. The fonts in your application will look a little bit different than
what is displayed here. This application is using a
custom CSS stylesheet to modify the default styles of the elements.
You can learn more in the [css tutorial](/external-resources),
but for now you can initialize your app with
```
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```
to get the same look and feel of these examples.

### Making your first change

**New in dash 0.30.0 and dash-renderer 0.15.0**
 Dash includes \"hot-reloading\", this features is activated by default when
you run your app with `app.run_server(debug=True)`. This means that Dash
will automatically refresh your browser when you make a change in your code.
Give it a try: change the title \"Hello Dash\" in your application or change the `x` or the `y` data. Your app should auto-refresh with your change.
> Don't like hot-reloading? You can turn this off with `app.run_server(dev_tools_hot_reload=False)`. 
> Learn more in [Dash Dev Tools documentation](/devtools) Questions? See the [community forum hot reloading discussion](https://community.plot.ly/t/announcing-hot-reload/14177).
#### More about HTML
The `dash_html_components` library contains a component class for every
HTML tag as well as keyword arguments for all of the HTML arguments.
"),


  # hello layout example
  examples$hello.dash2$source_code,
  examples$hello.dash2$layout,

  # hello table example
  examples$hello.table$source_code,
  examples$hello.table$layout,

  # hello scater example
  examples$hello.bubble$source_code,
  examples$hello.bubble$layout,

  # hello dmarkdown example
  examples$hello.markdown$source_code,
  examples$hello.markdown$layout,

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
