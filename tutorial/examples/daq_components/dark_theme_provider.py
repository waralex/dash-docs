import dash
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

theme =  {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

rootLayout = html.Div([
    daq.BooleanSwitch(
        on=True,
        className='dark-theme-control'
    ), html.Br(),
    daq.ToggleSwitch(
        className='dark-theme-control'
    ), html.Br(),
    daq.ColorPicker(
        value=17,
        className='dark-theme-control'
    ), html.Br(), 
    daq.Gauge(
        min=0,
        max=10,
        value=6,
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.GraduatedBar(
        min=0,
        max=100,
        value=42,
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.Indicator(
        value=True,
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.Knob(
        min=0,
        max=10,
        value=6,
        className='dark-theme-control'
    ), html.Br(), 
    daq.LEDDisplay(
        value="3.14159",
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.NumericInput(
        min=0,
        max=10,
        value=4, 
        className='dark-theme-control'
    ), html.Br(), 
    daq.PowerButton(
        on=True,
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.PrecisionInput(
        precision=4,
        value=299792458,
        className='dark-theme-control'
    ), html.Br(), 
    daq.StopButton(
        className='dark-theme-control'
    ), html.Br(), 
    daq.Slider(
        min=0,
        max=100,
        value=30,
        targets = {"25": {"label": "TARGET"}},
        color=theme['primary'],
        className='dark-theme-control'
    ), html.Br(), 
    daq.Tank(
        min=0,
        max=10,
        value=5,
        className='dark-theme-control'
    ), html.Br(), 
    daq.Thermometer(
        min=95,
        max=105,
        value=98.6,
        className='dark-theme-control'
    ), html.Br() 

])


app.layout = html.Div(id='dark-theme-container', children=[
    daq.ToggleSwitch(
        id='toggle-theme',
        label=['Light', 'Dark'],
        value=True
    ),
    html.Br(),
    html.Div(
        id='theme-colors',
        children=[
            daq.ColorPicker(
                id='primary-color',
                label='Primary color',
                value=dict(hex='#00EA64')
            ),
            daq.ColorPicker(
                id='secondary-color',
                label='Accent color',
                value=dict(hex='#6E6E6E')
            ),
            daq.ColorPicker(
                id='detail-color',
                label='Detail color',
                value=dict(hex='#007439')
            )
        ]
    ), 
    html.Div(id='dark-theme-components', children=[
        daq.DarkThemeProvider(theme=theme, children=rootLayout)
    ], style={'border': 'solid 1px #A2B1C6', 'border-radius': '5px', 'padding': '50px', 'margin-top': '20px'})
], style={'padding': '50px'})


@app.callback(
    dash.dependencies.Output('dark-theme-components', 'children'),
    [dash.dependencies.Input('toggle-theme', 'value'),
     dash.dependencies.Input('primary-color', 'value'),
     dash.dependencies.Input('secondary-color', 'value'),
     dash.dependencies.Input('detail-color', 'value')]
)
def edit_theme(dark, p, s, d):
    
    if(dark):
        theme.update(
            dark=True
        )
    else: 
        theme.update(
            dark=False
        )

    if p is not None:
        theme.update(
            primary=p['hex']
        )
    if s is not None:
        theme.update(
            secondary=s['hex']
        )
    if d is not None:
        theme.update(
            detail=d['hex']
        )
    return daq.DarkThemeProvider(theme=theme, children=rootLayout)


@app.callback(
    dash.dependencies.Output('dark-theme-components', 'style'),
    [dash.dependencies.Input('toggle-theme', 'value')],
    state=[dash.dependencies.State('dark-theme-components', 'style')]
)
def switch_bg(dark, currentStyle):
    if(dark):
        currentStyle.update(
            backgroundColor='#303030'
        )
    else:
        currentStyle.update(
            backgroundColor='white'
        )
    return currentStyle


if __name__ == '__main__':
    app.run_server(debug=True)
