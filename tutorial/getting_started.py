# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

import plotly

from dash.dependencies import Input, Output, Event, State
import styles
from tools import load_example, merge

examples = [
    load_example(s) for s in [
        'tutorial/examples/getting_started_layout_1.py',
        'tutorial/examples/getting_started_layout_2.py',
        'tutorial/examples/getting_started_table.py',
        'tutorial/examples/getting_started_viz.py',
        'tutorial/examples/getting_started_markdown.py',
        'tutorial/examples/getting_started_core_components.py',
        'tutorial/examples/getting_started_interactive_simple.py',
        'tutorial/examples/getting_started_graph.py',
        'tutorial/examples/getting_started_multiple_viz.py',
        'tutorial/examples/getting_started_multiple_outputs_1.py',
        'tutorial/examples/getting_started_callback_chain.py',
        'tutorial/examples/graph_callbacks_simple.py',
        'tutorial/examples/getting_started_crossfilter.py'
    ]
]


layout = html.Div([

    dcc.Markdown('''
    # Dash Tutorial

    This tutorial will walk you through the fundamentals of creating Dash apps
    through {} self-contained apps.

    '''.format(len(examples)).replace('    ', '')),

    dcc.Markdown('''***

1. [Installation](#installation)
2. [Dash App Layout](#dash-app-layout)
    - Generating HTML with Dash
    - Data Visualization in Dash
    - Markdown
    - Core Components
    - Calling `help`
3. [Interactivity](#interactivity)
    - Fundamentals
    - Multiple Inputs
    - Multiple Outputs
    - Graph Crossfiltering

  ***'''),

    html.H2('''
    1. Installation
    ''', id='installation'),

    dcc.Markdown('''

    In your terminal, install several dash libraries.
    These libraries are under active development,
    so install and upgrade frequently.
    Python 2 and 3 are supported.'''.replace('    ', '')),

    dcc.SyntaxHighlighter('''pip install dash.ly=={}  # The core dash backend
        pip install dash-renderer=={}  # The dash front-end
        pip install dash-html-components=={}  # HTML components
        pip install dash-core-components=={}  # Supercharged components
        pip install plotly=={}  # Plotly graphing library used in examples
    '''.replace('    ', '').format(
        dash.__version__,
        dash_renderer.__version__,
        html.__version__,
        dcc.__version__,
        plotly.__version__
    ), customStyle=styles.code_container),

    html.H2('''
    2. Dash App Layout
    ''', id='dash-app-layout'),

    dcc.Markdown('''***

    #### Generating HTML with Dash

    Dash apps are composed of two parts. The first part is the "`layout`" of
    the app and it describes what the application looks like.
    The second part describes the interactivity of the application.

    Dash provides Python classes for all of the visual components of
    the application. We maintain a set of components in the
    `dash_core_components` and the `dash_html_components` library
    but you can also [build your own](https://github.com/plotly/dash-components-archetype)
    with JavaScript and React.js.

    To get started, create a file named `app.py` with the following code:
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[0][0],
        language='python',
        customStyle=styles.code_container
    ),
    dcc.Markdown('''
    Run the app with

    ```
    $ python app.py
    ...Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

    and visit [http:127.0.0.1:8050/](http:127.0.0.1:8050/)
    in your web browser. You should see an app that looks like this.
    '''.replace('    ', '')),

    html.Div(examples[0][1], className="example-container"),

    # TODO - Comment about the default CSS of the graph?

    dcc.Markdown('''
        Note:
        1. The `layout` is composed of a tree of "components" like `html.Div`
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
           but for now you can add `app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css")`
           to your file to get the same look and feel of these examples.

    By default, the items in your layout are arranged one on top of the other.
    You can create different arrangements using CSS and stylesheets in the
    custom layout arrangements in Dash apps tutorial (coming soon!).

    #### More about HTML

    The `dash_html_components` library contains a component class for every
    HTML tag as well as keyword arguments for all of the HTML arguments.

    Let's customize the text in our app by modify the inline styles of the
    components:
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[1][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[1][1], className="example-container"),

    dcc.Markdown('''
        In this example, we modified the inline styles of the `html.Div`
        and `html.H1` components with the `style` property.

        `html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDFF'})`
        is rendered in the Dash application as
        `<h1 style="text-align: center; color: #7FDFF">Hello Dash</h1>`.

        There are a few important differences between the `dash_html_components`
        and the HTML attributes:
        1. The `style` property in HTML is a semicolon-separated string. In Dash,
           you can just supply a dictionary.
        2. The keys in the `style` dictionary are [camelCased](https://en.wikipedia.org/wiki/Camel_case).
           So, instead of `text-align`, it's `textAlign`.
        3. The HTML `class` attribute is `className` in Dash.
        4. The children of the HTML tag is specified through the `children` keyword
           argument.

        Besides that, all of the available HTML attributes and tags are available
        to you within your Python context.

        ***

        #### Reusable Components

        By writing our markup in Python, we can create complex resuable
        components like tables without switching contexts or languages.

        Here's a quick example that generates a `Table` from a Pandas dataframe.
        If you don't have Pandas installed, install with `pip install pandas`.

    '''.replace('   ', '')),

    dcc.SyntaxHighlighter(
        examples[2][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[2][1], className="example-container"),

    dcc.Markdown('''
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

    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[3][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[3][1], className="example-container"),

    dcc.Markdown('''
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
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[4][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[4][1], className="example-container"),

    dcc.Markdown('''
        #### Core Components

        The `dash_core_components` includes a set a higher-level components like
        dropdowns, graphs, markdown blocks, and more.

        Like all Dash components, they are described entirely declaratively.
        Every option that is configurable is available as a keyword argument
        of the component.

        We'll see many of these components throughout the tutorial.
        You can view all of the available components in the
        [Dash Core Components Gallery](/dash-core-components)
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[5][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[5][1], className="example-container"),

    dcc.Markdown('''

        Notice that these elements aren't interactive yet:
        clicking on the checkboxes, dragging the slider,
        and entering text in the input doesn't update the component.
        These components will become interactive in the final section
        of this tutorial on interactivity.

        #### Calling `help`

        Dash components are declarative: every configurable aspect of these
        components is set during instantiation as a keyword argument.
        Call `help` in your Python console on any of the components to
        learn more about a component and its available arguments:

    '''.replace('    ', '')),

    html.Div(
        dcc.Markdown('''```
>>> help(dcc.Dropdown)
class Dropdown(dash.development.base_component.Component)
|  A Dropdown component.
|  Dropdown is an interactive dropdown element for selecting one or more
|  items.
|  The values and labels of the dropdown items are specified in the `options`
|  property and the selected item(s) are specified with the `value` property.
|
|  Use a dropdown when you have many options (more than 5) or when you are
|  constrained for space. Otherwise, you can use RadioItems or a Checklist,
|  which have the benefit of showing the users all of the items at once.
|
|  Keyword arguments:
|  - id (string; optional)
|  - className (string; optional)
|  - disabled (boolean; optional): If true, the option is disabled
|  - multi (boolean; optional): If true, the user can select multiple values
|  - options (list; optional)
|  - placeholder (string; optional): The grey, default text shown when no option is selected
|  - value (string | list; optional): The value of the input. If `multi` is false (the default)
|  then value is just a string that corresponds to the values
|  provided in the `options` property. If `multi` is true, then
|  multiple values can be selected at once, and `value` is an
|  array of items with values corresponding to those in the
|  `options` prop.```'''), style=styles.code_container),

    dcc.Markdown('''
        ### Summary

        The `layout` of a Dash app describes what the app looks like.
        The `layout` is a hierarchical tree of components.
        The `dash_html_components` library provides classes for all of the HTML
        tags and the keyword arguments describe the HTML attributes like `style`,
        `className`, and `id`. The `dash_core_components` library
        generates higher-level components like controls and graphs.

        For reference, see:
        - [`dash_core_components` gallery](/dash-core-components)
        - [`dash_html_components` reference](/dash-html-components)

        ***
    '''.replace('    ', '')),

    html.H2('''
    3. Interactivity
    ''', id='interactivity'),

    dcc.Markdown('''

        This section describes how to make your Dash apps interactive.

        Let's get started with a simple example.

    '''.replace('    ', '')),

    html.H4('''
    Dash App Layout
    ''', id='dash-app-layout'),

    dcc.SyntaxHighlighter(
        examples[6][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[6][1], className="example-container"),

    dcc.Markdown('''
    Try typing in the text box. The children of the output component updates
    right away. Let's break down what's happening here:
    1. The "inputs" and "outputs" of our application interface are described
       declaratively through the `app.callback` decorator.
    2. In Dash, the inputs and outputs of our application are simply the
       properties of a particular component. In this example,
       our input is the "`value`" property of the component that has the ID
       "`my-id`". Our output is the "`children`" property of the
       component with the ID "`my-div`".
    3. Whenver an input property changes, the function that the
       callback decorator wraps will get called automatically.
       Dash provides the function with the new value of the input property as
       an input argument and Dash updates the property of the output component
       with whatever was returned by the function.
    4. The `component_id` and `component_property` keywords are optional
       (there are only two arguments for each of those objects).
       I have included them here for clarity but I will omit them from here on
       out for brevity and readability.
    5. Don't confuse the `dash.dependencies.Input` object from the
       `dash_core_components.Input` object. The former is just used in these
       callbacks and the latter is an actual component.
    6. Notice how we don't set a value for the `children` property of the
       `my-div` component in the `layout`. When the Dash app starts, it
       automatically calls all of the callbacks with the initial values of the
       input components in order to populate the initial state of the output
       components. In this example, if you specified something like
       `html.Div(id='my-div', children='Hello world')`, it would get overwritten
       when the app starts.

    It's sort of like programming with Microsoft Excel:
    whenever an input cell changes, all of the cells that depend on that cell
    will get updated automatically. This is called "Reactive Programming".

    Remember how every component was described entirely through its set of
    keyword arguments? Those properties are important now.
    With Dash interactivity, we can dynamically update any of those properties
    through a callback function. Frequently we'll update the `children` of a
    component to display new text or the `figure` of a `dcc.Graph` component
    to display new data, but we could also update the `style` of a component or
    even the available `options` of a `dcc.Dropdown` component!

    ***

    Let's take a look at another example where a `dcc.Slider` updates a
    `dcc.Graph`.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[7][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[7][1], className="example-container"),

    dcc.Markdown('''
    In this example, the `"value"` property of the `Slider` is the input of the app
    and the output of the app is the `"figure"` property of the `Graph`.
    Whenever the `value` of the `Slider` changes, Dash calls the callback
    function `update_figure` with the new value. The function filters the
    dataframe with this new value, constructs a `figure` object,
    and returns it to the Dash application.

    There are a few nice patterns in this example:
    1. We're using the [Pandas](http://pandas.pydata.org/) library for importing
       and filtering datasets in memory.
    2. We load our dataframe at the start of the app: `df = pd.read_csv('...')`.
       This dataframe `df` is in the global state of the app and can be
       read inside the callback functions.
    3. Loading data into memory can be expensive. By loading querying data at
       the start of the app instead of inside the callback functions, we ensure
       that this operation is only done when the app server starts. When a user
       visits the app or interacts with the app, that data (the `df`)
       is already in memory.
       If possible, expensive initialization (like downloading or querying data)
       should be done in the global scope of the app instead of within the
       callback functions.
    4. The callback does not modify the original data, it just creates copies
       of the dataframe by filtered through pandas filters.
       This is important: *your callbacks should never mutate variables
       outside of their scope*. If your callbacks modify global state, then one
       user's session might affect the next user's session and when the app is
       deployed on multiple processes or threads, those modifications will not
       be shared across sessions.

    #### Multiple inputs

    In Dash any "`Output`" can have multiple "`Input`" components.
    Here's a simple example that binds 5 Inputs
    (the `value` property of 2 `Dropdown` components, 2 `RadioItems` components,
    and 1 `Slider` component) to 1 Output component
    (the `figure` property of the `Graph` component).
    Notice how the `app.callback` lists all 5 `dash.dependencies.Input` inside
    a list in the second argument.

    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[8][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[8][1], className="example-container"),

    dcc.Markdown('''

    In this example, the `update_graph` function gets called whenever the
    `value` property of the `Dropdown`, `Slider`, or `RadioItems` components
    change.

    The input arguments of the `update_graph` function are the new or current
    value of the each of the `Input` properties, in the order that they were
    specified.

    Even though only a single `Input` changes at a time (a user can only change
    the value of a single Dropdown in a given moment), Dash collects the current
    state of all of the specified `Input` properties and passes them into your
    function for you. Your callback functions are always guarenteed to be passed
    the representative state of the app.

    Let's extend our example to include multiple outputs.

    #### Multiple Outputs

    Each Dash callback function can only update a single Output property.
    To update multiple Outputs, just write multiple functions.

    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[9][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[9][1], className="example-container"),

    dcc.Markdown('''
    You can also chain outputs and inputs together: the output of one callback
    function could be the input of another callback function.

    This pattern can be used to create dynamic UIs where one input component
    updates the available options of the next input component.
    Here's a simple example.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[10][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[10][1], className="example-container"),

    dcc.Markdown(u'''
    The first callback updates the available options in the second `RadioItems`
    component based off of the selected value in the first `RadioItems` component.

    The second callback sets an initial value when the `options` property changes:
    it sets it to the first value in that `options` array.

    The final callback displays the selected `value` of each component.
    If you change the `value` of the countries `RadioItems` component, Dash
    will wait until the `value` of the cities component is updated
    before calling the final callback. This prevents your callbacks from being
    called with inconsistent state like with `"USA"` and `"Montréal"`.

    '''.replace('    ', '')),

    dcc.Markdown('''
    #### Graph Crossfiltering

    Dash components are described declaratively by a set of attributes.
    All of these attributes can be updated by callback functions but only
    a subset of these attributes are updated through user interaction.
    For example, when you click on an option in a `dcc.Dropdown` component, the
    `value` property of that component changes.

    The `dcc.Graph` component has three attributes that can change
    through user-interaction: `hoverData`, `clickData`, and `selectedData`.
    These properties update when you hover over points, click on points, or
    select regions of points in a graph.

    Here's an simple example that prints these attributes in the screen.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[11][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[11][1], className="example-container"),

    dcc.Markdown('''***
    Let's update our world indicators example by displaying time series when
    we hover over points in our scatter plot.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[12][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[12][1], className="example-container"),

    dcc.Markdown('''

    ### Summary

    We've covered the fundamentals of Dash. Dash apps are built off of a set
    of simple but powerful principles: declarative UIs that are customizable
    through reactive and functional Python callbacks.
    Every element attribute of the declarative components can be updated through
    a callback and a subset of the attributes, like the `value` properties of
    the `dcc.Dropdown`, are editable by the user in the interface.

    '''.replace('    ', ''))

])
