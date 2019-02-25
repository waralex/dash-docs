import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles
from textwrap import dedent as s

from tutorial.utils.component_block import ComponentBlock


def IframeComponentBlock(
        example_string,
        iframe_location
):
    return html.Div([
        dcc.SyntaxHighlighter(
            example_string,
            language='python',
            customStyle=styles.code_container
        ),
        html.Div(
            className='example-container',
            children=html.Iframe(
                width='600px',
                height='600px',
                style={'border': 'none'},
                src=iframe_location
            )
        )
    ])


def generate_code_container(
        component_name,
        library_name, library_short,
        component_dict,
        description=''
):
    # initialize and set all parts of code

    props = None
    style = None
    datafile = None
    default_id = True
    library_imports = []
    setup_code = ''
    component_wrap = None
    iframe_location = None

    if 'props' in component_dict.keys():
        props = component_dict['props']
    if 'style' in component_dict.keys():
        style = component_dict['style']
    if 'datafile' in component_dict.keys():
        datafile = component_dict['datafile']
    if 'default_id' in component_dict.keys():
        default_id = component_dict['default_id']
    if 'library_imports' in component_dict.keys():
        library_imports = component_dict['library_imports']
    if 'setup_code' in component_dict.keys():
        setup_code = component_dict['setup_code']
    if 'component_wrap' in component_dict.keys():
        component_wrap = component_dict['component_wrap']
    if 'iframe_location' in component_dict.keys():
        iframe_location = component_dict['iframe_location']

    # parameters for initial declaration of component
    propString = '\n  '
    if default_id is True:
        propString += 'id=\'my-{}-{}\', '.format(
            library_short,
            component_name.lower())

    if props is not None:
        for key in props.keys():
            propString += '{}={}, '.format(key, props[key])

    # style options
    if style is not None:
        styleString = 'style={\n  '
        for key in style.keys():
            styleString += '  \'{}\': \'{}\', '.format(
                key,
                str(style[key])
            )
        styleString = styleString[:-2]
        styleString += '\n  }, '
        propString += styleString

    # loading data if necessary
    if datafile is not None:

        # import urllib
        library_imports.append(
            ['urllib2', 'urlreq']
        )

        # add location of data
        data_location = '''https://raw.githubusercontent.com/plotly/\
dash-bio/master/tests/dashbio_demos/sample_data/'''
        setup_code = '''
data = urlreq.urlopen(\"{}{}\").read()
'''.format(data_location, datafile['name']) + setup_code

        # declare data in component initialization
        propString += '{}=data, '.format(
            datafile['parameter']
        )

    # add imports
    imports_string = ''
    for library in library_imports:
        imports_string += 'import {} as {}\n'.format(
            library[0],
            library[1]
        )

    # format prop string
    propString = propString.replace(', ', ',\n  ')

    if(len(propString) > 4):
        propString = propString[:-4] + '\n'
    else:
        propString = ''

    # format component string
    component_string = '{}.{}({})'.format(
        library_short,
        component_name,
        propString
    )
    if component_wrap is not None:

        component_string = component_wrap.replace(
            '_', component_string)

    example_string = '''import {} as {}
{}
{}

component = {}
'''.format(library_name.replace('-', '_'),
           library_short,
           imports_string,
           setup_code,
           component_string)


    # load the iframe if that is where the app is
    component_demo = ComponentBlock(
        example_string
    )
    if iframe_location is not None:
        component_demo = IframeComponentBlock(
            example_string,
            iframe_location
        )

    return [

        html.Hr(),

        html.H3(dcc.Link(component_name,
                         href='/{}/{}'.format(
                             library_name,
                             component_name.lower())),
                id=component_name.replace(' ', '-').lower()),

        dcc.Markdown(s(description)),

        component_demo,

        html.Br(),

        dcc.Link('More {} Examples and Reference'.format(component_name),
                 href='/{}/{}'.format(
                     library_name,
                     component_name.lower()))
    ]


def generate_docs(
        library_name,
        library_short,
        library_heading,
        component_dict
):
    layout_children = [library_heading]

    sorted_keys = list(component_dict.keys())
    sorted_keys.sort()

    for component in sorted_keys:
        layout_children += generate_code_container(
            component,
            library_name,
            library_short,
            component_dict[component]
        )

    return layout_children
