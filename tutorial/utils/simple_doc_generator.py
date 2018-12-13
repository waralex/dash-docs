import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles
from textwrap import dedent as s

from tutorial.utils.component_block import ComponentBlock


def generate_code_container(
        component_name,
        library_name, library_short,
        default_id=True,
        description='',
        props=None,
        style=None
):
    propString = '\n  '
    if(default_id):
        propString += 'id=\'my-{}-{}\', '.format(
            library_short,
            component_name.lower())

    if props is not None:
        for key in props.keys():
            propString += '{}={}, '.format(key, props[key])

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
 
    propString = propString.replace(', ', ',\n  ')

    if(len(propString) > 4): 
        propString = propString[:-4] + '\n'
    else:
        propString = ''
        
    return [

        html.Hr(),

        html.H3(dcc.Link(component_name,
                         href='/{}/{}'.format(
                             library_name,
                             component_name.lower()))),
        
        dcc.Markdown(s(description)),
        
        ComponentBlock(
            '''import {} as {}

{}.{}({})'''.format(library_name.replace('-', '_'),
                    library_short,
                    library_short, 
                    component_name,
                    propString),
            language='python',
            customStyle=styles.code_container
        ),

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

    for component in component_dict.keys():
        layout_children += generate_code_container(
            component,
            library_name,
            library_short,
            **component_dict[component]
        )

    return html.Div(className='gallery', children=layout_children)

    
