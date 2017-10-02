import dash_core_components as dcc
import dash_html_components as html

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

layout = html.Div(className="toc", children=[
    html.H1('Dash User Guide'),

    html.H2("What's Dash?", style=styles['underline']),

    html.Div([html.Ul([

        html.Li(
            dcc.Link(html.A('Introduction'), href="/dash/introduction")
        ),

        html.Li(
            html.A('Announcement Letter',
                   href="https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503"),
        ),

        html.Li(
            dcc.Link(html.A('Dash App Gallery'), href="/dash/gallery"),
        ),
    ])], className=""),

    html.H2("Creating Your First App", style=styles['underline']),

    html.Div([html.Ul([
        html.Li(dcc.Link(html.A('Installation'), href="/dash/installation")),

        html.Li(
            dcc.Link(
                html.A('Dash Layout'),
                href="/dash/getting-started"
            )
        ),

        html.Li(
            dcc.Link(
                html.A('Dash Callbacks'),
                href="/dash/getting-started-part-2"
            )
        )
    ])], className=""),

    html.H2('Component Libraries', style=styles['underline']),
    html.Div([html.Ul([
        html.Li(dcc.Link(html.A('Dash Core Components'), href="/dash/dash-core-components")),

        html.Li(dcc.Link(html.A('Dash HTML Components'), href="/dash/dash-html-components")),

        html.Li(dcc.Link(html.A('Build Your Own Components'), href="/dash/plugins")),
    ])], className=""),

    html.H2('Advanced Usage', style=styles['underline']),
    html.Div([html.Ul([
        html.Li(
            dcc.Link(html.A('Performance'), href="/dash/performance"),
        ),

        html.Li(
            dcc.Link(html.A('Live Updates'), href="/dash/live-updates"),
        ),

        html.Li(
            dcc.Link(
                html.A('External CSS and JS'),
                href="/dash/external-resources"
            )
        ),

        html.Li(
            dcc.Link(
                html.A('URL Routing and Multiple Apps'),
                href="/dash/urls"
            )
        )
    ])], className=''),

    html.H2('Production', style=styles['underline']),

    html.Div(html.Ul([
        html.Li(dcc.Link(html.A('Authentication'), href="/dash/authentication")),

        html.Li(dcc.Link(html.A('Deployment'), href="/dash/deployment")),

    ]), className=""),

    html.H2('Getting Help', style=styles['underline']),
    html.Div([html.Ul([
        html.Li(html.A('FAQ', href="https://community.plot.ly/c/dash")),

        html.Li(dcc.Link(html.A('Support and Contact'), href="/dash/support"))
    ])], className="")
])
