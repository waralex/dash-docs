import dash_core_components as dcc
import dash_html_components as html

layout = dcc.Markdown('''
# Writing your own components

One of the really cool things about dash is that
it is built on top of [React.js](https://facebook.github.io/react/),
a javascript library for building web components.

React has a huge community and open source ecosystem.
There are thousands of components that have been built
by community members and released under open source licenses.
For example, here are implementations of
[slider components](https://react.rocks/?q=slider) and
[table components](https://react.rocks/?q=tables) built by the community.

## From React.js to Python

Dash provides a framework that converts React components
(written in Javascript) into Python classes that are
compatible with the Dash ecosystem.

On a high level, this is how that works:
- Components in dash are serialized as [JSON](www.json.org).
  To write a dash-compatabile component, all of the properties
  of the component must be serializable as JSON. For example,
  Javascript functions are not valid input arguments.
- By annotating components with React docstrings, Dash extracts
  the information about the component's name, properties, and a description
  of the components through [React Docgen](https://github.com/reactjs/react-docgen).
  This is exported as a JSON file.
- Dash reads this JSON file and dynamically creates python classes that subclass
  a core Dash component. These classes include argument validation,
  python docstrings, types, and a basic set of methods. _These classes are
  generated entirely automatically._ A javascript developer does not need to
  write _any_ python in order to generate a component that can be used in the
  Dash ecosystem.
- The python component package includes the JSON file and the Javascript bundle
  as extra files.
- The Dash app will crawl through the app's `layout` property and check which
  component packages are included in the layout and it will extract that
  component's necessary javascript or CSS bundles. Dash will serve these bundles
  to Dash's front-end. These javascript bundles are used to render the components.
- Dash's `layout` is serialized as JSON and served to Dash's front-end. This
  `layout` is recursively rendered with these javascript bundles and React.


## Step-by-step guide

The Dash ecosystem includes a command-line tool for
generating component package templates with all of the necessary
boiler plate.

We use the package [https://github.com/FormidableLabs/builder] built by
the excellent team at [Formidable Labs](https://formidable.com/) to manage
these templates.

The code behind the template is available in the [dash-components-archetype repository on GitHub](https://github.com/plotly/dash-components-archetype)
repository.

### Step 1 - Prerequisites

You'll need Node, NPM, and Python installed.
Components are built with [React.js](https://facebook.github.io/react/).

> If you're just getting started, we've written a great
[React.js tutorial](https://academy.plot.ly/) as part of our academy
that uses [plotly.js](https://github.com/plotly/plotly.js).

''')
