import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.H2('Open Problems'),

    html.Div('This is a diary of unsolved problems and proposals for Dash.'),

    html.Hr(),

    html.H3('Circular dependencies'),

    html.Hr(),

    html.H3('Expose available events in python classes'),

    html.Div('React docgen?'),

    html.Hr(),

    html.H3('Multi-page apps'),

    html.Hr(),

    html.H3('Event meta information'),

    dcc.SyntaxHighlighter('''
Div('Tab 1', id='1'),
Div('Tab 2', id='2'),
Div(id='content')


@app.react('content',
           state=[{'id': 'dropdown'}],
           events=[{'id': '1', 'event': 'click'},
                   {'id': '2', 'event': 'click'}])
def display_content(dropdown, id1, id2):
    id1['event'] # '' || 'click'
    id2['event'] # '' || 'click'
    dropdown['event'] # '' || 'propChange' || 'select'

    if id1['event'] == 'click':
        return content1
    elif id2['event'] == 'click':
        return content2

# If state shares events,
# then events get merged with the state object.
# This keeps the default case simple.
app.react('content', ['dropdown'], events=[{'id': '1', 'event': 'click'}])

# Is equivalent to
app.react('content',
          state=[{'id': 'dropdown', 'props': '*'}],
          events=[
              {'id': 'dropdown', 'event': 'propChange'},
              {'id': '1', 'event': 'click'}])

def update_content(dropdownProps, clickEvent)
    dropdownProps # {'event': 'propChange', 'value': 'my-val'}
    clickEvent    # {'event': ''}
''', language='python'),

    html.Hr(),

    html.H3('Specificity in props and events'),

    dcc.SyntaxHighlighter('''
# Nice and simple.
@app.react('s', ['dropdown', 'graph'])

# Object is too complicated.
@app.react('s', {
    'dropdown': {
        'state': ['value', 'options']}},
        'events': ['onSelect']
    'graph': {
        'state': ['hoverData'],
        'events': ['hover']
    }
})

## Something like this is nice but it's unordered.
@app.react('s',
           state={'dropdown': ['value', 'options']},
           events={'graph': ['onSelect', 'onHover']})

# Propositions for all props
@app.react('s',
           state={
                'dropdown': Dropdown._prop_names, # explicit. easy to update.
                'input': '*' # implicit but easy to understand.
           },
           event={
                'dropdown': Dropdown.events, # all events
                'input': [Dash.events.propChange],
                'slider': [Slider.events.onSlide]
           })

# Unordered state and events - call signature is too implicit
def update_content(**state_and_events):
    dropdown = state_and_events['dropdown']

## Ordered dicts include order but are a lil ugly and hard...
@app.react(
    's',
    state=OrderedDict([
        ('dropdown', Dropdown._prop_names),
        ('input', '*')
    ])
)

## Leaves us with lists...
@app.react('s',
            state=[
                dict(id='dropdown', props=Dropdown._prop_names),
                dict(id='input', props=['value'])
            ])
'''),

    html.Hr(),

    html.H3('Optional front-end state store'),

    html.Div('''
        Some users might want to store additional data that isn't
        stored in any components.
    '''),

    html.Ul([
        html.Li('Last item clicked'),
        html.Li('Username'),
        html.Li('Data that was hidden')
    ]),

    html.Hr(),

    html.H3('Hotloading'),

    html.Div('''
    Use flask-sockets and re-run the initialization steps in the front-end.
    ''')

])
