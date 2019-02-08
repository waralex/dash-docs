import re
import dash_core_components as dcc
import dash_html_components as html
import dash


regex = {
    'react': r'\s*([a-zA-Z]+)\s*\(([a-z\s|]*;*\s*[a-z]*)\):*[\.\s]*(.*)', 
    'python': r'\s*\(([a-zA-Z]+)\)\s*([a-zA-Z_]+)\s*:\s*(.*)'
}


def component_names(library_name):
    '''
    Gets the names of all components, Python and React, in a library.
    
    :param (str)
    '''
    
    exec("import {}".format(library_name))

    library = eval(library_name)
    members = dir(library)

    all_components = [member for member in members if re.search(
        r'^[A-Z][a-zA-Z]+$', member
    ) is not None]

    react = [c.__name__ for c in library._components]
    python = [c for c in all_components if c not in react]

    return {'react': react,
            'python': python}


def generate_prop_table(component_name, component_names, library_name):

    component_type = 'react' \
        if component_name in component_names['react'] else 'python'
    
    sep = '-' if component_type == 'react' else ':param'

    exec("import {}".format(library_name))
    
    doc = eval("{}.{}".format(library_name, component_name)).__doc__

    if component_type == 'react':
        doc = doc.replace("  -", "...")
        
    props = doc.split(sep)

    tableRows = []

    for item in props:
        desc_sections = item.split('\n\n')

        partone = desc_sections[0]
    
        r = re.match(
            regex[component_type],
            partone.replace('\n', ' ')
        )
        if r is None:
            continue
        
        prop_optional = 'Yes'
        
        if component_type == 'python':
            (prop_type, prop_name, prop_desc) = r.groups()
        elif component_type == 'react':
            (prop_name, prop_type, prop_desc) = r.groups()
            if 'optional' not in prop_type:
                prop_optional = 'No'
            prop_type = prop_type.split(';')[0]

        if len(desc_sections) > 1:
            prop_desc += ' '
            prop_desc += desc_sections[1]
           
        tableRows.append(
            html.Tr([html.Td(dcc.Markdown(prop_name)),
                     html.Td(dcc.Markdown(prop_desc)),
                     html.Td(dcc.Markdown(prop_type)),
                     html.Td(dcc.Markdown(prop_optional))])
        )

    return html.Div([
        html.H3("{} Properties".format(component_name)),
        html.Table(tableRows)
    ])
                    

def default_example(component_name, example_code, styles):
    return [
        html.Hr(),
        
        html.H3("Default {}".format(
            component_name.replace('-', ' ').title()
        )),
        html.P("An example of a default {} without \
        any extra properties.".format(
            component_name.replace('-', ' ')
        )),
        dcc.SyntaxHighlighter(
            example_code[0],
        ),
        html.Div(
            example_code[1],
            className='example-container'
        )
    ]

if __name__ == '__main__':
    import dash_bio
    
    app = dash.Dash()

    components = component_names(dash_bio)
    app.layout = html.Div(
        [generate_prop_table(component, 'react', 'dash_bio') 
         for component in components['react']] +
        [generate_prop_table(component, 'python', 'dash_bio')
         for component in components['python']]
    )
    app.run_server(debug=True)
