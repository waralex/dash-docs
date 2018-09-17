import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

app = dash.Dash()

tabs_styles = {
    "width": "33%",
    "height": "50px",
    "padding": "14px",
    "box-shadow": "0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2)",
}
tab_style = {
    "padding": "11px",
    "margin": "0px 12px",
    "borderRadius": "100%",
    "width": "50px",
    "box-shadow": "0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2)"
}

tab_selected_style = {
    "padding": "11px",
    "margin": "0px 12px",
    "borderRadius": "100%",
    "width": "50px",
    "fontWeight": "bold",
    "border": "1px solid lightgrey"
}

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])

@app.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
