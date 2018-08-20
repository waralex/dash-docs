import dash_html_components as html
import dash_core_components as dcc

def s(string_block):
    return string_block.replace('    ', '')

def Chapter(name, href=None, caption=None):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div([
        html.Li(
            linkComponent(
                name,
                href=href,
                style={'paddingLeft': 0},
                id=href
            )
        ),
        html.Small(dcc.Markdown(s(caption or '')), style={
            'display': 'block',
            'marginTop': '-10px' if caption else ''
        }) if caption else None
    ])
