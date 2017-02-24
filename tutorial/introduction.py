import dash_html_components as html

layout = html.Div([
    html.H2('Dash Developer Preview'),

    html.Div('''Dash is a productive python framework for building web applications.

    Written on top of Plotly.js and React.js,
    Dash is ideal for data visualization with highly custom user interfaces.
    '''),

    html.Div('''This is an exclusive developer preview of Dash.
    Dash is currently in an unreleased and unannounced. Call it a Beta.
    Please do not share Dash without Plotly's constent.'''),

    html.Div('''The core functionality of Dash will be open sourced.
    For enterprises, Plotly offers a platform for
    deploying, orchestrating, and permissioning dash apps behind
    your firewall. If you're interested,
    please get in touch at <sales@plot.ly> to register for early access.''')
])
