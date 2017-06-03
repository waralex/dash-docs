
def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)

toc = html.Div(
create_contents([
    html.A('Introduction', href="/introduction"),
    [
        'Why Dash?',
        'Licensing'
    ],
    html.A('Gallery', href="/gallery"),
    html.A('Create Your First App', href="/getting-started"),
    [
        'Installation',
        'Part 1 - Dash Layout',
        [
            'HTML Components',
            'Data Visualization in Dash',
            'Markdown',
            'Core Component Library',
            'Calling `help`'
        ],
        'Part 2 - Interactivity'
        [
            'Fundamentals',
            'Multiple Inputs',
            'Multiple Outputs',
            'Crossfiltering'
        ]
    ],
    html.A('Deploying', href="/deploying"),
    [
        'On Premise',
        'Cloud PaaS'
    ],
    html.A('Advanced Features', href="/advanced"),
    [
        'Caching',
        'Fast Charting with WebGL',
        'URLs and Single Page Apps',
        'Live Updates'
    ],
    html.A('Best Practices', href="/best-practices"),
    [
        'Virtual Environments',
        'Styling Apps',
        'Basic User Interface',
        'Initial State'
    ],
    html.A('Dash Core Component Library Reference', href="/dash-core-components"),
    [
        'Graph',
        'Dropdown',
        'RadioItems',
        'TextInput',
        'Slider',
        'RangeSlider',
        'Markdown'
    ],
    'Roadmap',
    [
        'Sponsoring Development',
        'Near Term',
        [
            'App Templates',
            'Authentication'
        ],
        'Long Term',
        [
            'Dash in Other Languages',
            'GUI App Builder',
            'Client-side Apps'
        ]
    ],
    'Credits',
    'Support and Contact'
]), style={'columnCount': 2}
)
