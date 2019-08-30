from .import tutorial

import dash_html_components as html
import dash_core_components as dcc
import dash_bio
import dash_table
import dash_daq
import dash_cytoscape

from .reusable_components import TOC, TOCChapters


## The chapters dict is used to generate the dash-docs search index
## If edited, update the search index by running `python dash_search_index.py`
## in the root of this repo.


def component_list(package, content_module, base_url, import_alias):
    return [
        {
            'url': '/{}/{}'.format(base_url, component.lower()),
            'name': '{}.{}'.format(import_alias, component),
            'content': (
                getattr(content_module, component)
                if (content_module is not None and
                    hasattr(content_module, component))
                else html.Div([
                    html.H1(html.Code('{}.{}'.format(
                        import_alias,
                        component
                    ))),
                    html.H2('Reference & Documentation'),
                    dcc.Markdown(getattr(package, component).__doc__),
                ])
            )
        } for component in sorted(dir(package))
        if not component.startswith('_') and
        component[0].upper() == component[0]
    ]


# chapterz = {
#     ### home.py ###
#     'introduction': {
#         'url': '/introduction',
#         'content': tutorial.introduction.layout,
#         'name':'Introduction',
#         'description': 'Dash is a productive Python framework for ' \
#                        'building web applications written on top of ' \
#                        'Flask, Plotly.js, and React.js.'
#     },
#
#     'gallery': {
#         'url': '/gallery',
#         'content': tutorial.gallery.layout,
#         'name': 'Dash App Gallery',
#         'description': 'Examples of Dash apps including ' \
#                        'drill down, stock tickers, streaming, ' \
#                        'and PDF generation.'
#     },
#
#     'dash-1-0-migration': {
#         'url': '/dash-1-0-migration',
#         'content': tutorial.migration.layout,
#         'name': 'Dash v1.0 Migration',
#         'description': 'How to upgrade from Dash v0.x to v1.0.'
#     },
#
#     'installation': {
#         'url': '/installation',
#         'content': tutorial.installation.layout,
#         'name': 'Part 1. Installation',
#         'description': 'How to install and upgrade dash libraries with pip.'
#     },
#
#     'getting-started': {
#         'url': '/getting-started',
#         'content': tutorial.getting_started_part_1.layout,
#         'name': 'Part 2. The Dash Layout',
#         'description': 'The Dash `layout` describes what your app will ' \
#                        'look like and is composed of a set of declarative ' \
#                        'Dash components.'
#     },
#
#     'getting-started-part-2': {
#         'url': '/getting-started-part-2',
#         'content': tutorial.getting_started_part_2.layout,
#         'name': 'Part 3. Basic Callbacks',
#         'description': "Dash apps are made interactive through Dash " \
#                        "Callbacks: Python functions that are " \
#                        "automatically called whenever an input " \
#                        "component's property changes. Callbacks " \
#                        "can be chained, allowing one update in the " \
#                        "UI to trigger several updates across the app."
#     },
#
#     'state': {
#         'url': '/state',
#         'content': tutorial.state.layout,
#         'name': 'Part 4. More About Callbacks',
#         'description': 'Basic callbacks are fired whenever the values ' \
#                        'change. Use Dash `State` with Dash `Inputs` to ' \
#                        'pass in extra values whenever the `Inputs` ' \
#                        'change. `State` is useful for UIs that contain ' \
#                        'forms or buttons. Use the `PreventUpdate` exception ' \
#                        'to leave the callback output unchanged' \
#     },
#
#     'graphing': {
#         'url': '/interactive-graphing',
#         'content': tutorial.graphing.layout,
#         'name': 'Part 5. Interactive Graphing and Crossfiltering',
#         'description': 'Bind interactivity to the Dash `Graph` ' \
#                        'component whenever you hover, click, or ' \
#                        'select points on your chart.'
#     },
#
#     'shared-state': {
#         'url': '/sharing-data-between-callbacks',
#         'content': tutorial.sharing_state.layout,
#         'name': 'Part 6. Sharing Data Between Callbacks',
#         'description': '`global` variables will break your Dash apps. ' \
#                        'However, there are other ways to share data ' \
#                        'between callbacks. This chapter is useful for ' \
#                        'callbacks that run expensive data processing ' \
#                        'tasks or process large data.'
#     },
#
#     'faqs': {
#         'url': '/faqs',
#         'content': tutorial.faqs.layout,
#         'name': 'Part 7. FAQs and Gotchas',
#         'description': 'If you have read through the rest of the ' \
#         'tutorial and still have questions or are encountering ' \
#         'unexpected behaviour, this chapter may be useful.'
#     },
#
#     'dash-core-components': {
#         'url': '/dash-core-components',
#         'content': tutorial.core_components.layout,
#         'name': 'Dash Core Components',
#         'description': 'The Dash Core Component library contains a set ' \
#                        'of higher-level components like sliders, graphs, ' \
#                        'dropdowns, tables, and more.'
#     },
#
#     'dash-html-components': {
#         'url': '/dash-html-components',
#         'content': [tutorial.html_components.layout],
#         'name': 'Dash HTML Components',
#         'description': 'Dash provides all of the available HTML tags ' \
#                        'as user-friendly Python classes. This chapter ' \
#                        'explains how this works and the few important ' \
#                        'key differences between Dash HTML components ' \
#                        'and standard html.'
#     },
#
#     'datatable': {
#         'url': '/datatable',
#         'content': tutorial.dash_table_index.layout,
#         'name': 'Dash DataTable',
#         'description': '(New! Released Nov 2, 2018) The Dash DataTable is our latest and ' \
#                        'most advanced component. It is an interactive table that ' \
#                        'supports rich styling, ' \
#                        'conditional formatting, editing, sorting, filtering, ' \
#                        'and more.'
#     },
#
#     'cytoscape': {
#         'url': '/cytoscape',
#         'content': tutorial.dash_cytoscape_index.layout,
#         'name': 'Dash Cytoscape',
#         'description': '(New! Released Feb 5, 2019) Dash Cytoscape is our new network ' \
#                        'visualization component. It offers a declarative and ' \
#                        'pythonic interface to create beautiful, customizable, ' \
#                        'interactive and reactive graphs.'
#
#     },
#
#     'dashdaq': {
#         'url': '/dash-daq',
#         'content': tutorial.daq.layout,
#         'name': 'Dash DAQ Components',
#         'description': 'Beautifully styled technical components for \
#         data acquisition and engineering applications.'
#     },
#
#     'dashbio': {
#         'url': '/dash-bio',
#         'content': tutorial.dashbio.layout,
#         'name': 'Dash Bio Components',
#         'description': '(New! Released April 2019) Components dedicated to visualizing \
#         bioinformatics data.'
#     },
#
#   'canvas': {
#         'url': '/canvas',
#         'content': tutorial.canvas.layout,
#         'name': 'Dash Canvas',
#         'description': '(New! Released March 2019) Drawing and annotations for image processing.'
#     },
#
#     'plugins': {
#         'url': '/plugins',
#         'content': tutorial.plugins.layout,
#         'name': 'Build Your Own Components',
#         'description': 'Dash components are built with ' \
#                        '[React.js](https://reactjs.org/). Dash provides ' \
#                        'a React &rarr; Dash toolchain that generates a Dash-' \
#                        'compatible interface to these components in Python.'
#     },
#
#     'd3-plugins': {
#         'url': '/d3-react-components',
#         'content': tutorial.d3.layout,
#         'name': 'Integrating D3.js into Dash Components',
#         'description': 'Tutorials and resources on encapsulating ' \
#                        'D3.js graphs in Dash-friendly React components. '\
#                        'Includes two sample components: a D3.js network graph '\
#                        'and a D3.js sunburst chart.'
#     },
#
#     'performance': {
#         'url': '/performance',
#         'content': tutorial.performance.layout,
#         'name': 'Performance',
#         'description': 'There are two main ways to speed up dash apps: '\
#                        'caching and using WebGL chart types.'
#     },
#
#     'live-updates': {
#         'url': '/live-updates',
#         'content': tutorial.live_updates.layout,
#         'name': 'Live Updates',
#         'description': 'Update your apps on page load or on a predefined ' \
#                        'interval (e.g. every 30 seconds).'
#     },
#
#     'external': {
#         'url': '/external-resources',
#         'content': tutorial.external_css_and_js.layout,
#         'name': 'Adding CSS & JS and Overriding the Page-Load Template',
#         'description': '''
#             New in dash v0.22.0! Learn how to add custom CSS and JS to your
#             application with the `assets` directory. Also, learn how to
#             customize the HTML template that Dash serves on page load in order
#             to add custom meta tags, customize the page's title, and more.
#         '''
#     },
#
#     'urls': {
#         'url': '/urls',
#         'content': tutorial.urls.layout,
#         'name': 'URL Routing and Multiple Apps',
#         'description': 'Dash provides two components (`dcc.Link` and ' \
#                        '`dcc.Location`) that allow you to easily make ' \
#                        'fast multipage apps using its own "Single Page ' \
#                        'App (SPA)" design pattern.'
#     },
#
#     'auth': {
#         'url': '/authentication',
#         'content': tutorial.auth.layout,
#         'name': 'Authentication',
#         'description': 'Authentication for dash apps is provided through a ' \
#                        'separate dash-auth package. `dash-auth` provides ' \
#                        'two methods of authentication: HTTP Basic Auth and ' \
#                        'Plotly OAuth.'
#     },
#
#     'deployment': {
#         'url': '/deployment',
#         'content': tutorial.deployment.layout,
#         'name': 'Deployment',
#         'description': 'To share a Dash app, you need to "deploy" your Dash ' \
#                        'app to a server'
#     },
#
#     'integrating-dash': {
#         'url': '/integrating-dash',
#         'content': tutorial.integrating_dash.layout,
#         'name': 'Integrating Dash with Existing Web Apps',
#         'description': 'Strategies for integrating Dash apps with existing web ' \
#                        'apps.'
#     },
#
#     'dash-deployment-server': {
#         'url': '/dash-deployment-server',
#         'content': tutorial.dash_deployment_server.layout,
#         'name': 'Dash Deployment Server Documentation',
#         'description': "Dash Deployment Server is Plotly's commercial " \
#                        "offering for hosting and sharing Dash Apps with " \
#                        "Plotly Enterprise."
#     },
#
#     'support': {
#         'url': '/support',
#         'content': tutorial.support.layout,
#         'name': 'Support and Contact',
#         'description': 'More information for Dash demos, Enterprise trials, ' \
#                        'Dash workshops, sponsored feature requests and ' \
#                        'customizations.'
#     },
#     'react-for-python-developers': {
#         'url': '/react-for-python-developers',
#         'content': tutorial.react_for_python_developers.layout,
#         'name': 'React for Python Developers',
#         'description': 'A tutorial on how to program in React and JavaScript for Python developers.'
#     },
#     'loading-states': {
#         'url': '/loading-states',
#         'content': tutorial.loading_states.layout,
#         'name': 'Loading States',
#         'description': 'Getting the loading state of a component and adding a loading component'
#     },
# ### End of home.py ###
#
# ### Start Components ###
#     'dropdown-examples': {
#         'url': '/dash-core-components/dropdown',
#         'content': tutorial.examples.Dropdown,
#         'name': 'Dropdowns',
#         'description': 'Dropdown examples, properties, and reference.'
#     },
#
#     'slider-examples': {
#         'url': '/dash-core-components/slider',
#         'content': tutorial.examples.Slider,
#         'name': 'Sliders Component',
#         'description': 'Slider examples, properties, and reference.'
#     },
#
#     'range-slider-examples': {
#         'url': '/dash-core-components/rangeslider',
#         'content': tutorial.examples.RangeSlider,
#         'name': 'Range Slider Component',
#         'description': 'Range slider examples, properties, and reference.'
#     },
#
#     'checklist-examples': {
#         'url': '/dash-core-components/checklist',
#         'content': tutorial.examples.Checklist,
#         'name': 'Checklist Component',
#         'description': 'Checklist examples, properties, and reference.'
#     },
#
#     'input-examples': {
#         'url': '/dash-core-components/input',
#         'content': tutorial.examples.Input,
#         'name': 'Input Component',
#         'description': 'Input properties and reference.'
#     },
#
#     'radio-item-examples': {
#         'url': '/dash-core-components/radioitems',
#         'content': tutorial.examples.RadioItems,
#         'name': 'Radio Item Component',
#         'description': 'Radio item examples, properties, and reference.'
#     },
#
#     'button-examples': {
#         'url': '/dash-core-components/button',
#         'content': tutorial.examples.Button,
#         'name': 'Button Component',
#         'description': 'Button examples, properties, and reference.'
#     },
#
#     'datepickersingle-examples': {
#         'url': '/dash-core-components/datepickersingle',
#         'content': tutorial.examples.DatePickerSingle,
#         'name': 'Date Picker: Single Component',
#         'description': 'Single date picker examples, properties, and reference.'
#     },
#
#     'datepickerrange-examples': {
#         'url': '/dash-core-components/datepickerrange',
#         'content': tutorial.examples.DatePickerRange,
#         'name': 'Date Picker: Range Component',
#         'description': 'Date range picker examples, properties, and reference.'
#     },
#
#     'markdown-examples': {
#         'url': '/dash-core-components/markdown',
#         'content': tutorial.examples.Markdown,
#         'name': 'Markdown Component',
#         'description': 'Markdown examples, properties, and reference.'
#     },
#
#     'link-examples': {
#         'url': '/dash-core-components/link',
#         'content': tutorial.examples.Link,
#         'name': 'Link Component',
#         'description': 'Link examples, properties, and reference.'
#     },
#
#     'tabs-example': {
#         'url': '/dash-core-components/tabs',
#         'content': tutorial.examples.Tabs,
#         'name': 'Tabs & Tab Component',
#         'description': 'Tabs examples, properties, and reference.'
#     },
#
#     'graphs-example': {
#         'url': '/dash-core-components/graph',
#         'content': tutorial.examples.Graphs,
#         'name': 'Graphs',
#         'description': 'Graph examples, properties, and reference.'
#     },
#
#     'textarea-examples': {
#         'url': '/dash-core-components/textarea',
#         'content': tutorial.examples.Textarea,
#         'name': 'Text Area Component',
#         'description': 'Text area properties and reference.'
#     },
#
#     'upload-examples': {
#         'url': '/dash-core-components/upload',
#         'content': tutorial.examples.Upload,
#         'name': 'Upload Component',
#         'description': 'Upload examples, properties, and reference.'
#     },
#
#     'location-examples': {
#         'url': '/dash-core-components/location',
#         'content': tutorial.examples.Location,
#         'name': 'Location Component',
#         'description': 'Location examples, properties, and reference.'
#     },
#
# ### Dash DAQ Components ###
#     'booleanswitch-examples': {
#         'url': '/dash-daq/booleanswitch',
#         'content': tutorial.daq_examples.BooleanSwitch,
#         'name': 'Boolean Switch Component',
#         'description': 'Boolean switch examples, properties, and reference.'
#     },
#
#     'colorpicker-examples': {
#         'url': '/dash-daq/colorpicker',
#         'content': tutorial.daq_examples.ColorPicker,
#         'name': 'Color Picker Switch Component',
#         'description': 'Color picker examples, properties, and reference.'
#     },
#
#     'gauge-examples': {
#         'url': '/dash-daq/gauge',
#         'content': tutorial.daq_examples.Gauge,
#         'name': 'Gauge Component',
#         'description': 'Gauge examples, properties, and reference.'
#     },
#
#     'graduatedbar-examples': {
#         'url': '/dash-daq/graduatedbar',
#         'content': tutorial.daq_examples.GraduatedBar,
#         'name': 'Graduated bar Component',
#         'description': 'Graduated bar examples, properties, and reference.'
#     },
#
#     'indicator-examples': {
#         'url': '/dash-daq/indicator',
#         'content': tutorial.daq_examples.Indicator,
#         'name': 'Indicator Component',
#         'description': 'Indicator examples, properties, and reference.'
#     },
#
#     'joystick-examples': {
#         'url': '/dash-daq/joystick',
#         'content': tutorial.daq_examples.Joystick,
#         'name': 'Joystick Component',
#         'description': 'Joystick examples, properties, and reference.'
#     },
#
#     'knob-examples': {
#         'url': '/dash-daq/knob',
#         'content': tutorial.daq_examples.Knob,
#         'name': 'Knob Component',
#         'description': 'Knob examples, properties, and reference.'
#     },
#
#     'leddisplay-examples': {
#         'url': '/dash-daq/leddisplay',
#         'content': tutorial.daq_examples.LEDDisplay,
#         'name': 'LED display Component',
#         'description': 'LED display examples, properties, and reference.'
#     },
#
#     'numericinput-examples': {
#         'url': '/dash-daq/numericinput',
#         'content': tutorial.daq_examples.NumericInput,
#         'name': 'Numeric input Component',
#         'description': 'Numeric input examples, properties, and reference.'
#     },
#
#     'powerbutton-examples': {
#         'url': '/dash-daq/powerbutton',
#         'content': tutorial.daq_examples.PowerButton,
#         'name': 'Power button Component',
#         'description': 'Power button examples, properties, and reference.'
#     },
#
#     'precisioninput-examples': {
#         'url': '/dash-daq/precisioninput',
#         'content': tutorial.daq_examples.PrecisionInput,
#         'name': 'Precision input Component',
#         'description': 'Precision input examples, properties, and reference.'
#     },
#
#     'stopbutton-examples': {
#         'url': '/dash-daq/stopbutton',
#         'content': tutorial.daq_examples.StopButton,
#         'name': 'Stop button Component',
#         'description': 'StopButton examples, properties, and reference.'
#     },
#
#     'daq-slider-examples': {
#         'url': '/dash-daq/slider',
#         'content': tutorial.daq_examples.Slider,
#         'name': 'Slider Component',
#         'description': 'Slider examples, properties, and reference.'
#     },
#
#     'tank-examples': {
#         'url': '/dash-daq/tank',
#         'content': tutorial.daq_examples.Tank,
#         'name': 'Tank Component',
#         'description': 'Tank examples, properties, and reference.'
#     },
#
#     'thermometer-examples': {
#         'url': '/dash-daq/thermometer',
#         'content': tutorial.daq_examples.Thermometer,
#         'name': 'Thermometer Component',
#         'description': 'Thermometer examples, properties, and reference.'
#     },
#
#     'toggleswitch-examples': {
#         'url': '/dash-daq/toggleswitch',
#         'content': tutorial.daq_examples.ToggleSwitch,
#         'name': 'Toggle switch Component',
#         'description': 'Toggle switch examples, properties, and reference.'
#     },
#
#     'darkthemeprovider-examples': {
#         'url': '/dash-daq/darkthemeprovider',
#         'content': tutorial.daq_examples.DarkThemeProvider,
#         'name': 'Dark theme provider Component',
#         'description': 'Dark theme provider examples, properties, and reference.'
#     },
#
#     # Dash Bio examples
#
#     'sequenceviewer-examples': {
#         'url': '/dash-bio/sequenceviewer',
#         'content': tutorial.dashbio_examples.SequenceViewer,
#         'name': 'Sequence Viewer Component',
#         'description': 'Sequence viewer examples, properties, and reference.'
#     },
#
#     'alignmentchart-examples': {
#         'url': '/dash-bio/alignmentchart',
#         'content': tutorial.dashbio_examples.AlignmentChart,
#         'name': 'Alignment Chart Component',
#         'description': 'Alignment Chart examples, properties, and reference.'
#     },
#
#     'clustergram-examples': {
#         'url': '/dash-bio/clustergram',
#         'content': tutorial.dashbio_examples.Clustergram,
#         'name': 'Clustergram Component',
#         'description': 'Clustergram examples, properties, and reference.'
#     },
#
#     'speck-examples': {
#         'url': '/dash-bio/speck',
#         'content': tutorial.dashbio_examples.Speck,
#         'name': 'Speck Component',
#         'description': 'Speck examples, properties, and reference.'
#     },
#
#     'circos-examples': {
#         'url': '/dash-bio/circos',
#         'content': tutorial.dashbio_examples.Circos,
#         'name': 'Circos Component',
#         'description': 'Circos examples, properties, and reference.'
#     },
#
#     'ideogram-exmaples': {
#         'url': '/dash-bio/ideogram',
#         'content': tutorial.dashbio_examples.Ideogram,
#         'name': 'Ideogram Component',
#         'description': 'Ideogram examples, properties, and reference.'
#     },
#
#     'molecule-2d-examples': {
#         'url': '/dash-bio/molecule2dviewer',
#         'content': tutorial.dashbio_examples.Molecule2dViewer,
#         'name': 'Molecule 2D Component',
#         'description': 'Molecule2D examples, properties, and reference.'
#     },
#
#     'molecule-3d-examples': {
#         'url': '/dash-bio/molecule3dviewer',
#         'content': tutorial.dashbio_examples.Molecule3dViewer,
#         'name': 'Molecule 3D Component',
#         'description': 'Molecule3D examples, properties, and reference.'
#     },
#
#     'needle-plot-examples': {
#         'url': '/dash-bio/needleplot',
#         'content': tutorial.dashbio_examples.NeedlePlot,
#         'name': 'Needle Plot Component',
#         'description': 'NeedlePlot examples, properties, and reference.'
#     },
#
#     'manhattan-plot-examples': {
#         'url': '/dash-bio/manhattanplot',
#         'content': tutorial.dashbio_examples.ManhattanPlot,
#         'name': 'Manhattan Plot Component',
#         'description': 'ManhattanPlot examples, properties, and reference.'
#     },
#
#     'volcano-plot-examples': {
#         'url': '/dash-bio/volcanoplot',
#         'content': tutorial.dashbio_examples.VolcanoPlot,
#         'name': 'Volcano Plot Component',
#         'description': 'VolcanoPlot examples, properties, and reference.'
#     },
#
#     'onco-print-examples': {
#         'url': '/dash-bio/oncoprint',
#         'content': tutorial.dashbio_examples.OncoPrint,
#         'name': 'OncoPrint Component',
#         'description': 'Oncoprint examples, properties, and reference.'
#     },
# ### End Components ###
#
# ### Start Dash Deployment Server ###
#     'ssh-examples': {
#         'url': '/dash-deployment-server/ssh',
#         'content': tutorial.dds_examples.Ssh,
#         'name': 'Authenticating to Dash Deployment Server with SSH',
#         'description': "There are two methods to deploy Dash Apps: HTTPS and SSH "
#         "and we recommend getting started with the HTTPS method."
#     },
#
#     'initialize-examples': {
#         'url': '/dash-deployment-server/initialize',
#         'content': tutorial.dds_examples.Initialize,
#         'name': 'Part 1. Initialize Dash Apps on Dash Deployment Server',
#         'description': 'Initialize Dash Apps on Plotly Enterprise'
#     },
#
#     'requirements-examples': {
#         'url': '/dash-deployment-server/application-structure',
#         'content': tutorial.dds_examples.Requirements,
#         'name': 'Application Structure',
#         'description': 'Ensure that your app meets all the requirements for deployment.'
#     },
#
#     'static-assets-examples': {
#         'url': '/dash-deployment-server/static-assets',
#         'content': tutorial.dds_examples.staticAssets,
#         'name': 'Adding Static Assets',
#         'description': 'Learn how to include custom CSS, JS, and images with the `assets` directory.'
#     },
#
#     'create-deploy-examples': {
#         'url': '/dash-deployment-server/deployment',
#         'content': tutorial.dds_examples.Deploy,
#         'name': 'Part 2. Deploy Dash Apps on Dash Deployment Server',
#         'description': 'Deploy Dash Apps on Dash Deployment Server'
#     },
#
#     'app-auth-examples': {
#         'url': '/dash-deployment-server/app-authentication',
#         'content': tutorial.dds_examples.Authentication,
#         'name': 'Dash Enterprise Auth Features',
#         'description': 'Accessing User Authentication Data in your Dash App'
#     },
#
#     'app-privacy': {
#         'url': '/dash-deployment-server/privacy',
#         'content': tutorial.dds_examples.AppPrivacy,
#         'name': 'Dash App Privacy',
#         'description': 'Dash App Privacy and Managing Collaborators'
#     },
#
#     'deployment-checks': {
#         'url': '/dash-deployment-server/checks',
#         'content': tutorial.dds_examples.Checks,
#         'name': 'Dash Deployment Health Checks',
#         'description': 'Create custom checks to ensure that a newly deployed app can serve traffic.'
#     },
#
#     'private-packages-examples': {
#         'url': '/dash-deployment-server/private-packages',
#         'content': tutorial.dds_examples.PrivatePackages,
#         'name': 'Adding Private Python Packages',
#         'description': 'Intsall private python packages in your Dash Apps.'
#     },
#
#     'config-sys-examples': {
#         'url': '/dash-deployment-server/configure-system-dependencies',
#         'content': tutorial.dds_examples.ConfigSys,
#         'name': 'Configuring System Dependencie',
#         'description': 'Install and configure system dependencies such '
#         'as database drivers or the Java JRE environment.'
#     },
#
#     'redis-examples': {
#         'url': '/dash-deployment-server/redis-database',
#         'content': tutorial.dds_examples.Redis,
#         'name': 'Linking a Redis Database',
#         'description': 'Create and link an in-memory database to your Dash Apps.'
#     },
#
#     'celery-examples': {
#         'url': '/dash-deployment-server/celery-process',
#         'content': tutorial.dds_examples.Celery,
#         'name': 'Linking a Celery Process',
#         'description': 'Add a task queue to your Dash Apps.'
#     },
#
#     'env-var-examples': {
#         'url': '/dash-deployment-server/environment-variables',
#         'content': tutorial.dds_examples.EnvVars,
#         'name': 'Setting Enviornment Variables',
#         'description': 'Environment variables are commonly used to store '
#         'secret variables like database passwords.'
#     },
#
#     'local-dir-examples': {
#         'url': '/dash-deployment-server/map-local-directories',
#         'content': tutorial.dds_examples.LocalDir,
#         'name': 'Mapping Local Directories',
#         'description': 'Directory mappings allow you to make directories '
#         'on the Dash Deployment Server available to your app.'
#     },
#
#     'stage-examples': {
#         'url': '/dash-deployment-server/staging-app',
#         'content': tutorial.dds_examples.StagingApp,
#         'name': 'Create a Staging Dash App ',
#         'description': 'Use a staged Dash App to test changes before updating '
#         'your prodcution Dash App.'
#     },
#
#     'pdf-service-examples': {
#         'url': '/dash-deployment-server/pdf-service',
#         'content': tutorial.dds_examples.pdfService,
#         'name': 'Dash Deployment Server PDF Service',
#         'description': 'Utilize the Dash Deployment Server API endpoint for '
#         'creating PDF exports of your Dash applications'
#     },
#     'troubleshooting-examples': {
#         'url': '/dash-deployment-server/troubleshooting',
#         'content': tutorial.dds_examples.Troubleshooting,
#         'name': 'Common Errors',
#         'description': 'Common errors when deploying Dash Apps.'
#     },
#
#     'analytics-examples': {
#         'url': '/dash-deployment-server/analytics',
#         'content': tutorial.dds_examples.Analytics,
#         'name': 'App Analytics',
#         'description': 'View app analytics such as last updated, '
#         'CPU usage, Memory Usage, and more.'
#     },
#
#     'logs-examples': {
#         'url': '/dash-deployment-server/logs',
#         'content': tutorial.dds_examples.Logs,
#         'name': 'App Logs',
#         'description': """Check your Dash App's logs via the Dash
#         Deployment Server UI or via the command line."""
#     },
#
#     'support-examples': {
#         'url': '/dash-deployment-server/support',
#         'content': tutorial.dds_examples.Support,
#         'name': 'Support',
#         'description': 'Having trouble deploying your app? Our dedicated '
#         'support team is available to help you out.'
#     },
#
#     'git-examples': {
#         'url': '/dash-deployment-server/git',
#         'content': tutorial.dds_examples.Git,
#         'name': 'Advanced Git',
#         'description': 'A reference for git commands and how they are used '
#         'with Dash Deployment Server.'
#     },
#
#     'dds-portal': {
#         'url': '/dash-deployment-server/portal',
#         'content': tutorial.dds_examples.Portal,
#         'name': 'Dash App Portal',
#         'description': 'Learn about the Dash App Portal '
#     },
#
#     'admin-panel': {
#         'url': '/dash-deployment-server/admin-panel',
#         'content': tutorial.dds_examples.AdminPanel,
#         'name': 'Admin Panel',
#         'description': 'Manage users in the Admin Panel '
#     },
# ### End Dash Deployment Server ###
#
# ### Start DataTable Docs
#
#     'datatable-sizing': {
#         'url': '/datatable/sizing',
#         'content': tutorial.table.sizing_chapter.layout,
#         'name': 'Sizing - DataTable',
#         'description': """
#             All about sizing the DataTable.
#             Examples on how to change the width and height of the table,
#             the widths of the individual columns columns, handling
#             text overflow, and more.
#         """
#     },
#
#     'datatable-styling': {
#         'url': '/datatable/style',
#         'content': tutorial.table.styling_chapter.layout,
#         'name': 'Style - DataTable',
#         'description': """
#             All about styling the DataTable.
#             Examples on how to change the colors, conditional formatting,
#             styling the table as a list view, and more.
#         """
#     },
#
#     'interactivity': {
#         'url': '/datatable/interactivity',
#         'content': tutorial.table.interactivity_chapter.layout,
#         'name': 'Interactive DataTable',
#         'description': '''
#         A showcase of the interactive features of the DataTable.
#         '''
#     },
#
#     'recipes': {
#         'url': '/datatable/editable',
#         'content': tutorial.table.editing_recipes_chapter.layout,
#         'name': 'Editable DataTable',
#         'description': '''
#         DataTable as a Spreadsheet: examples for determining which
#         cell has changed, filtering null values, adding or removing
#         columns, and more.
#         '''
#     },
#
#     'callbacks': {
#         'url': '/datatable/callbacks',
#         'content': tutorial.table.table_callbacks_chapter.layout,
#         'name': 'Python-Driven Filtering, Paging, Sorting - DataTable',
#         'description': '''
#         Examples on filtering, sorting, and paging data with Python.
#         '''
#     },
#
#     'typing': {
#         'url': '/datatable/typing',
#         'content': tutorial.table.table_typing_chapter.layout,
#         'name': 'Typing and User Input Processing',
#         'description': '''
#         Column typing and user input validation, coercing, defaulting.
#         '''
#     },
#
#     'dropdowns': {
#         'url': '/datatable/dropdowns',
#         'content': tutorial.table.dropdowns_chapter.layout,
#         'name': 'Dropdowns Inside DataTable',
#         'description': '''
#         Learn how to embed dropdowns inside the DataTable.
#         '''
#     },
#
#     'virtualization': {
#         'url': '/datatable/virtualization',
#         'content': tutorial.table.virtualization_chapter.layout,
#         'name': 'Virtualization',
#         'description': '''
#         Examples using DataTable virtualization.
#         '''
#     },
#
#     'filtering': {
#         'url': '/datatable/filtering',
#         'content': tutorial.table.filtering_chapter.layout,
#         'name': 'Filtering Syntax',
#         'description': '''
#         Reference for frontend and backend filtering syntax for the DataTable.
#         '''
#     },
#
#     'roadmap': {
#         'url': '/datatable/reference',
#         'content': tutorial.table.reference_chapter.layout,
#         'name': 'DataTable Reference',
#         'description': '''
#         A comprehensive list of all of the DataTable properties.
#         '''
#     },
#
# ### End DataTable Docs
#
# ### Start Cytoscape Docs
#
#     'cytoscape-elements': {
#         'url': '/cytoscape/elements',
#         'content': tutorial.cytoscape.elements_chapter.layout,
#         'name': 'Cytoscape Elements',
#         'description': '''
#         Overview of element declaration and manipulation.
#         '''
#     },
#
#     'cytoscape-layout': {
#         'url': '/cytoscape/layout',
#         'content': tutorial.cytoscape.layout_chapter.layout,
#         'name': 'Cytoscape Layouts',
#         'description': '''
#         Description of built-in layouts, and how to modify their properties.
#         '''
#     },
#
#     'cytoscape-styling': {
#         'url': '/cytoscape/styling',
#         'content': tutorial.cytoscape.styling_chapter.layout,
#         'name': 'Cytoscape Styling',
#         'description': '''
#         Methods to style elements with a CSS-like syntax.
#         '''
#     },
#
#     'cytoscape-callbacks': {
#         'url': '/cytoscape/callbacks',
#         'content': tutorial.cytoscape.callbacks_chapter.layout,
#         'name': 'Cytoscape Callbacks',
#         'description': '''
#         Methods to combine Dash callbacks to update your Cytoscape object.
#         '''
#     },
#
#     'cytoscape-events': {
#         'url': '/cytoscape/events',
#         'content': tutorial.cytoscape.events_chapter.layout,
#         'name': 'Cytoscape events',
#         'description': '''
#         Overview of user-interaction events that trigger callbacks in Dash,
#         and how to use them to update the Cytoscape component.
#         '''
#     },
#
#     'cytoscape-biopython': {
#         'url': '/cytoscape/biopython',
#         'content': tutorial.cytoscape.applications_chapter.layout,
#         'name': 'Cytoscape with Biopython',
#         'description': '''
#         Examples of applications in bioinformatics using Biopython.
#         '''
#     },
#
#     'cytoscape-reference': {
#         'url': '/cytoscape/reference',
#         'content': tutorial.cytoscape.reference_chapter.layout,
#         'name': 'Cytoscape Reference',
#         'description': '''
#         Comprehensive list of all of the Cytoscape properties.
#         '''
#     },
#
# ### End Cytoscape Docs
#
#     'search': {
#         'url': '/search',
#         'content': tutorial.search.layout,
#         'name': '',
#         'description': 'Search the Dash Docs'
#     },
#
#     'confirm-examples': {
#         'url': '/dash-core-components/confirm',
#         'content': tutorial.examples.ConfirmDialog,
#         'name': 'ConfirmDialog Component',
#         'description': 'ConfirmDialog examples, properties, and reference'
#     },
#
#     'confirm-provider-examples': {
#         'url': '/dash-core-components/confirm-provider',
#         'content': tutorial.examples.ConfirmDialogProvider,
#         'name': 'ConfirmDialogProvider Component',
#         'description': 'ConfirmDialogProvider examples, properties and reference'
#     },
#
#     'store-examples': {
#         'url': '/dash-core-components/store',
#         'content': tutorial.examples.Store,
#         'name': 'Store component',
#         'description': 'Store examples, properties and reference'
#     },
#
#     'devtools': {
#         'url': '/devtools',
#         'content': tutorial.devtools.layout,
#         'name': 'Dev tools',
#         'description': 'Dash dev tools reference'
#     },
#
#     'testing': {
#         'url': '/testing',
#         'content': tutorial.testing.layout,
#         'name': 'Dash Testing',
#         'description': '(New in Dash 1.0!) An introduction to testing your dash app with selenium'
#     },
#
#     'logout-button': {
#         'url': '/dash-core-components/logout_button',
#         'content': tutorial.examples.LogoutButton,
#         'name': 'Logout button',
#         'description': 'LogoutButton examples, properties and reference'
#     },
#
#     'loading-component': {
#         'url': '/dash-core-components/loading_component',
#         'content': tutorial.examples.LoadingComponent,
#         'name': 'Loading component',
#         'description': 'Loading component examples, properties and reference'
#     }
#
# }


URLS = [
    {
        'name': "What's Dash?",
        'chapters': [
            {
                'url': '/introduction',
                'name': 'Introduction',
                'description': '''
                    A quick paragraph about Dash and a link to the talk at
                    Plotcon that started it all.
                ''',
                'content': tutorial.introduction.layout
            },
            {
                'url': 'https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503',
                'name': 'Announcement Essay (2017)',
                'description': (
                    '''
                    Our extended essay on Dash. An extended discussion of
                    Dash's architecture and our motivation behind the project.
                    '''
                )
            },
            {
                'url': '/gallery',
                'name': 'Dash App Gallery',
                'description': '''
                    A glimpse into what's possible with Dash.
                '''
            },
            {
                'url': '/dash-1-0-migration',
                'name': 'Dash 1.0.0 Migration',
                'description': (
                    "Dash v1.0 is out! If you're new to Dash, just head down to "
                    "the tutorial section below and get started. This section is "
                    "for users Dash v0.x upgrading to v1.0. We've learned a lot "
                    "from working with the amazing Dash community, and Dash v1.0 "
                    "makes a number of changes to make your apps even more "
                    "intuitive, powerful, and extensible as Dash continues to "
                    "evolve."
                ),
                'content': tutorial.introduction.layout
            },
            {
                'url': 'http://eepurl.com/dE7CHT',
                'name': 'Dash Club',
                'description': '''
                    An email newsletter by chriddyp, the creator of Dash.
                '''
            }
        ]
    },

    {
        'name': 'Dash Tutorial',
        'chapters': [
            {
                'url': '/installation',
                'name': 'Part 1. Installation',
                'description': 'How to install and upgrade dash libraries with pip',
                'content': tutorial.installation.layout
            },
            {
                'url': '/getting-started',
                'name': 'Part 2. Layout',
                'description': (
                    'The Dash `layout` describes what your app will '
                    'look like and is composed of a set of declarative '
                    'Dash components.'
                ),
                'content': tutorial.getting_started_part_1.layout
            },
            {
                'url': '/getting-started-part-2',
                'name': 'Part 3. Basic Callbacks',
                'description': (
                    "Dash apps are made interactive through Dash "
                    "Callbacks: Python functions that are "
                    "automatically called whenever an input "
                    "component's property changes. Callbacks "
                    "can be chained, allowing one update in the "
                    "UI to trigger several updates across the app."
                ),
                'content': tutorial.getting_started_part_2.layout
            },
            {
                'url': '/state',
                'name': 'Part 4. More About Callbacks',
                'description': (
                    "Basic callbacks are fired whenever the values "
                    "change. Use Dash `State` with Dash `Inputs` to "
                    "pass in extra values whenever the `Inputs` "
                    "change. `State` is useful for UIs that contain "
                    "forms or buttons. Use the `PreventUpdate` exception "
                    "to leave the callback output unchanged"
                ),
                'content': tutorial.state.layout
            },
            {
                'url': '/interactive-graphing',
                'name': 'Part 5. Interactive Graphing and Crossfiltering',
                'description': 'Bind interactivity to the Dash `Graph` ' \
                               'component whenever you hover, click, or ' \
                               'select points on your chart.',
                'content': tutorial.graphing.layout
            },
            {
                'url': '/sharing-data-between-callbacks',
                'name': 'Part 6. Sharing Data Between Callbacks',
                'description': '`global` variables will break your Dash apps. ' \
                               'However, there are other ways to share data ' \
                               'between callbacks. This chapter is useful for ' \
                               'callbacks that run expensive data processing ' \
                               'tasks or process large data.',
                'content': tutorial.sharing_state.layout
            },
            {
                'url': '/faqs',
                'name': 'Part 7. FAQs & Gotchas',
                'description': 'If you have read through the rest of the ' \
                'tutorial and still have questions or are encountering ' \
                'unexpected behaviour, this chapter may be useful.',
                'content': tutorial.faqs.layout
            }
        ]
    },

    {
        'name': 'Open Source Component Libraries',
        'chapters': [
            {
                'name': 'Dash Core Components',
                'chapters': [{
                    'url': '/dash-core-components/',
                    'name': 'Overview',
                    'description': (
                        'The Dash Core Component library contains a set '
                        'of higher-level components like sliders, graphs, '
                        'dropdowns, tables, and more.'
                    ),
                    'content': tutorial.core_components.layout
                }] + component_list(
                    dcc,
                    tutorial.examples,
                    'dash-core-components',
                    'dcc'
                )
            },

            {
                'name': 'Dash HTML Components',
                'chapters': [
                    {
                        'url': '/dash-html-components/',
                        'name': 'Overview',
                        'description': 'Dash provides all of the available HTML tags ' \
                                       'as user-friendly Python classes. This chapter ' \
                                       'explains how this works and the few important ' \
                                       'key differences between Dash HTML components ' \
                                       'and standard html.',
                        'content': tutorial.html_components.layout
                    }
                ] + component_list(
                    html,
                    None,
                    'dash-html-components',
                    'html'
                )
            },

            {
                'name': 'Dash DataTable',

                'chapters': [
                    {
                        'url': '/dashtable',
                        'name': 'Overview',
                        'description': (
                            '`dash_table.DataTable` is an interactive table that ' \
                            'supports rich styling, ' \
                            'conditional formatting, editing, sorting, filtering, ' \
                            'and more.'
                        ),
                        'autogenerate_index': True,
                        'preamble': tutorial.dash_table_index.preamble,
                    },

                    {
                        'url': '/dashtable/reference',
                        'name': 'Reference',
                        'content': tutorial.table.reference_chapter.layout,
                        'description': '''
                            A comprehensive list of all of the
                            DataTable properties.
                        '''
                    },

                    {
                        'url': '/datatable/sizing',
                        'content': tutorial.table.sizing_chapter.layout,
                        'name': 'Sizing',
                        'description': """
                            All about sizing the DataTable. Examples include:
                            - Setting the width and the height of the table
                            - Responsive table design
                            - Setting the widths of individual columns
                            - Handling long text
                            - Fixing rows and columns
                        """
                    },

                    {
                        'url': '/datatable/style',
                        'content': tutorial.table.styling_chapter.layout,
                        'name': 'Styling',
                        'description': """
                            The style of the DataTable is highly customizable. This chapter
                            includes examples for:
                            - Conditional formatting
                            - Displaying multiple rows of headers
                            - Highlighting rows, columns, and cells
                            - Styling the table as a list view
                            - Changing the colors (including a dark theme!)

                            The sizing API for the table has been particularly tricky for
                            us to nail down, so be sure to read this chapter to understand the nuances,
                            limitations, and the APIs that we're exploring.
                        """
                    },

                    {
                        'url': '/datatable/interactivity',
                        'content': tutorial.table.interactivity_chapter.layout,
                        'name': 'Sorting, Filtering, Selecting, and Paging Natively',
                        'description': '''
                            The DataTable is interactive. This chapter demonstrates the
                            interactive features of the table and how to wire up these
                            interations to Python callbacks. These actions include:
                            - Paging
                            - Selecting Rows
                            - Sorting Columns
                            - Filtering Data
                        '''
                    },

                    {
                        'url': '/datatable/callbacks',
                        'content': tutorial.table.table_callbacks_chapter.layout,
                        'name': 'Python-Driven Filtering, Paging, Sorting',
                        'description': '''
                            In Part 3, the paging, sorting, and filtering was done entirely
                            clientside (in the browser). This means that you need to
                            load all of the data into the table up-front. If your data is large,
                            then this can be prohibitively slow.

                            In this chapter, you'll learn how to write your own filtering,
                            sorting, and paging backends in Python with Dash.
                            We'll do the data processing with Pandas but you could write your
                            own routines with SQL or even generate the data on the fly!
                        '''
                    },

                    {
                        'url': '/datatable/editable',
                        'content': tutorial.table.editing_recipes_chapter.layout,
                        'name': 'Editable DataTable',
                        'description': '''
                            The DataTable is editable. Like a spreadsheet, it can be used
                            as an input for controlling models with a variable number
                            of inputs.

                            This chapter includes recipes for:

                            - Determining which cell has changed
                            - Filtering out null values
                            - Adding or removing columns
                            - Adding or removing rows
                            - Ensuring that a minimum set of rows are visible
                            - Running Python computations on certain columns or cells
                        '''
                    },

                    {
                        'url': '/datatable/typing',
                        'content': tutorial.table.table_typing_chapter.layout,
                        'name': 'Typing and User Input Processing',
                        'description': '''
                            In this chapter, you'll learn how to configure the table to
                            - assign the column type
                            - change the data presentation
                            - change the data formatting
                            - validate or coerce user data input
                            - apply default behavior for valid and invalid data
                        '''
                    },

                    {
                        'url': '/datatable/dropdowns',
                        'content': tutorial.table.dropdowns_chapter.layout,
                        'name': 'Dropdowns Inside DataTable',
                        'description': '''
                            Cells can be rendered as editable Dropdowns. This is our first
                            stake in bringing a full typing system to the table.
                            Rendering cells as dropdowns introduces some complexity in the
                            markup and so there are a few limitations that you should be aware
                            of.
                        '''
                    },

                    {
                        'url': '/datatable/virtualization',
                        'content': tutorial.table.virtualization_chapter.layout,
                        'name': 'Virtualization',
                        'description': '''
                            Examples using DataTable virtualization.
                        '''
                    },

                    {
                        'url': '/datatable/filtering',
                        'content': tutorial.table.filtering_chapter.layout,
                        'name': 'Filtering Syntax',
                        'description': '''
                            An explanation and examples of filtering syntax for both frontend
                            and backend filtering in the DataTable.
                        '''
                    },
                ]
            },

            {
                'name': 'Dash Bio',
                'chapters': [
                    {
                        'url': '/dash-bio/',
                        'name': 'Overview',
                        'content': tutorial.dashbio.layout,
                        'description': (
                            'Components dedicated to visualizing bioinformatics data.'
                        )
                    }
                ] + component_list(
                    dash_bio,
                    tutorial.dashbio_examples,
                    'dash-bio',
                    'dash_bio'
                )
            },

            {
                'name': 'Dash DAQ',
                'chapters': [
                    {
                        'url': '/dash-daq',
                        'name': 'Overview',
                        'content': tutorial.daq.layout,
                        'description': (
                            '''
                            Beautifully styled technical components for
                            data acquisition, monitoring, and engineering
                            applications.
                            '''
                        )
                    }
                ] + component_list(
                    dash_daq,
                    tutorial.daq_examples,
                    'dash-daq',
                    'dash_daq'
                )
            },

            {
                'name': 'Dash Canvas',
                'chapters': [
                    {
                        'url': '/canvas',
                        'name': 'Overview & Reference',
                        'content': tutorial.canvas,
                        'description': (
                            'Image rendering, drawing, annotations '
                            'for image processing applications.'
                        )
                    }
                ]
            },

            {
                'name': 'Dash Cytoscape',
                'chapters': [
                    {
                        'url': '/cytoscape',
                        'name': 'Overview',
                        'description': (
                            '''
                            Dash Cytoscape is our new network visualization
                            component. It offers a declarative and pythonic
                            interface to create beautiful, customizable,
                            interactive and reactive graphs.
                            '''
                        ),
                        'autogenerate_index': True,
                        'preamble': tutorial.dash_cytoscape_index.preamble
                    },

                    {
                        'url': '/cytoscape/elements',
                        'content': tutorial.cytoscape.elements_chapter.layout,
                        'name': 'Basic Usage & Elements',
                        'description': '''
                        Overview of element declaration and manipulation.
                        '''
                    },

                    {
                        'url': '/cytoscape/layout',
                        'content': tutorial.cytoscape.layout_chapter.layout,
                        'name': 'Layouts',
                        'description': '''
                        Description of built-in layouts, and how to modify their properties.
                        '''
                    },

                    {
                        'url': '/cytoscape/styling',
                        'content': tutorial.cytoscape.styling_chapter.layout,
                        'name': 'Styling',
                        'description': '''
                        Methods to style elements with a CSS-like syntax.
                        '''
                    },

                    {
                        'url': '/cytoscape/callbacks',
                        'content': tutorial.cytoscape.callbacks_chapter.layout,
                        'name': 'Callbacks',
                        'description': '''
                        Methods to combine Dash callbacks to update your Cytoscape object.
                        '''
                    },

                    {
                        'url': '/cytoscape/events',
                        'content': tutorial.cytoscape.events_chapter.layout,
                        'name': 'User Interactions',
                        'description': '''
                        Overview of user-interaction events that trigger callbacks in Dash,
                        and how to use them to update the Cytoscape component.
                        '''
                    },

                    {
                        'url': '/cytoscape/biopython',
                        'content': tutorial.cytoscape.applications_chapter.layout,
                        'name': 'Biopython Examples',
                        'description': '''
                        Examples of applications in bioinformatics using Biopython.
                        '''
                    },

                    {
                        'url': '/cytoscape/reference',
                        'content': tutorial.cytoscape.reference_chapter.layout,
                        'name': 'Reference',
                        'description': '''
                        Comprehensive list of all of the Cytoscape properties.
                        '''
                    },

                ]
            },

        ]
    },

    {
        'name': 'Creating Your Own Components',
        'chapters': [
            {
                'name': 'React for Python Developers',
                'description': (
                    '''
                    A tutorial on how to program in React and JavaScript
                    for Python developers.
                    '''
                ),
                'url': '/react-for-python-developers',
                'content': tutorial.react_for_python_developers.layout,
            },

            {
                'name': 'Build Your Own Components',
                'description': 'Dash components are built with ' \
                               '[React.js](https://reactjs.org/). Dash provides ' \
                               'a React &rarr; Dash toolchain that generates a Dash-' \
                               'compatible interface to these components in Python.',
                'url': '/plugins',
                'content': tutorial.plugins.layout,
            },
            {
                'name': 'Integrating D3.js into Dash Components',
                'description': (
                    '''
                    Tutorials and resources on encapsulating D3.js graphs in
                    Dash-friendly React components.
                    Includes two sample components: a D3.js network graph
                    and a D3.js sunburst chart.
                    '''
                ),
                'url': '/d3-react-components',
                'content': tutorial.d3.layout,
            }
        ]
    },

    {
        'name': 'Beyond the Basics',
        'chapters': [
            {
                'url': '/performance',
                'content': tutorial.performance.layout,
                'name': 'Performance',
                'description': 'There are two main ways to speed up dash apps: '\
                               'caching and using WebGL chart types.'
            },

            {
                'url': '/live-updates',
                'content': tutorial.live_updates.layout,
                'name': 'Live Updates',
                'description': 'Update your apps on page load or on a predefined ' \
            },

            {
                'url': '/external-resources',
                'content': tutorial.external_css_and_js.layout,
                'name': 'Adding CSS & JS and Overriding the Page-Load Template',
                'description': '''
                    New in dash v0.22.0! Learn how to add custom CSS and JS to your
                    application with the `assets` directory. Also, learn how to
                    customize the HTML template that Dash serves on page load in order
                    to add custom meta tags, customize the page's title, and more.
                '''
            },

            {
                'url': '/urls',
                'content': tutorial.urls.layout,
                'name': 'URL Routing and Multiple Apps',
                'description': 'Dash provides two components (`dcc.Link` and ' \
                               '`dcc.Location`) that allow you to easily make ' \
                               'fast multipage apps using its own "Single Page ' \
                               'App (SPA)" design pattern.'
            },

            {
                'url': '/devtools',
                'content': tutorial.devtools.layout,
                'name': 'Dev tools',
                'description': 'Dash dev tools reference'
            },

            {
                'url': '/loading-states',
                'content': tutorial.loading_states.layout,
                'name': 'Loading States',
                'description': 'Getting the loading state of a component and adding a loading component'
            },

            {
                'url': '/testing',
                'content': tutorial.testing.layout,
                'name': 'Dash Testing',
                'description': '(New in Dash 1.0!) An introduction to testing your dash app with selenium'
            }
        ],
    },

    {
        'name': 'Production',
        'chapters': [
            {
                'url': '/authentication',
                'content': tutorial.auth.layout,
                'name': 'Authentication',
                'description': ''
            },

            {
                'url': '/deployment',
                'content': tutorial.deployment.layout,
                'name': 'Deployment',
                'description': 'To share a Dash app, you need to "deploy" your Dash ' \
                               'app to a server'
            },

            {
                'url': '/integrating-dash',
                'content': tutorial.integrating_dash.layout,
                'name': 'Integrating Dash with Existing Web Apps',
                'description': 'Strategies for integrating Dash apps with existing web ' \
                               'apps.'
            }
        ]
    },

    {
        'name': 'Getting Help',
        'chapters': [
            {
                'url': 'https://community.plot.ly/c/dash',
                'description': '',
                'name': 'The Dash Community Forum'
            },
            {
                'url': '/support',
                'name': 'Support and Contact',
                'description': '',
                'content': tutorial.support.layout,
            }
        ]
    },

    {
        'name': 'Dash Enterprise',
        'description': (
            """
            Dash Enterprise is Plotly's commercial offering for hosting
            and sharing Dash apps on-premises or in the cloud.
            """
        ),
        'chapters': [
            {
                'name': 'About Dash Enterprise',
                'url': 'https://plot.ly/dash/pricing'
            },
            {
                'name': 'Dash Enterprise Documentation',
                'url': '/dash-deployment-server',
                'content': tutorial.dash_deployment_server.layout,
            }
        ]
    }

]




def create_index_pages(url_set):
    for section in url_set:
        if 'autogenerate_index' in section and section['autogenerate_index']:
            print('Setting content for ')
            print(section['url'])
            section['content'] = html.Div([
                html.Div(section.get('preamble', '')),
                # Convention is to let the first chapter
                # be the "overview" chapter/link,
                # so skip it when we're generating that page
                # as we're already on it.
                html.Div(TOCChapters(url_set[1:]))
            ])
        if 'chapters' in section:
            create_index_pages(section['chapters'])
create_index_pages(URLS)


URL_TO_CONTENT_MAP = {}
def create_url_mapping(url_set):
    for section in url_set:
        if 'url' in section:
            URL_TO_CONTENT_MAP[section['url'].rstrip('/')] = section.get(
                'content',
                'Content for {} not defined'.format(section['url'])
            )
        if 'chapters' in section:
            create_url_mapping(section['chapters'])
create_url_mapping(URLS)


def find_section(url_set, name):
    for section in url_set:
        if section.get('name', '') == name:
            return section
        elif 'chapters' in section:
            return find_section(section['chapters'], name)
