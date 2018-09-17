import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Tabs(id="tabs-with-classes", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
        dcc.Tab(label='Tab one', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Tab two', value='tab-2', className='custom-tab', selected_className='custom-tab--selected'),
    ]),
    html.Div(id='tabs-content-classes')
])

@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
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
