import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.H1('Coming Soon'),
    html.H3(dcc.Link('Linking a Redis Database',
                     href='/dash-deployment-server/redis-database')),
    html.H3(dcc.Link('Setting Enviornment Variables',
                     href='/dash-deployment-server/enviornment-variables')),
    html.H3(dcc.Link('Mapping Local Directories',
                     href='/dash-deployment-server/map-local-directories')),
    html.Img(
        alt='Coming Soon',
        src='https://github.com/plotly/dash-docs/raw/master/images/building.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])
