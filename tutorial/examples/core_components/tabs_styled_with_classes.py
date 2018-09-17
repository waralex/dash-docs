import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Tabs(id="tabs-with-classes", parent_className='custom-tabs', content_className='custom-tabs-content', className='custom-tabs-container', children=[
        dcc.Tab(label='Tab one', className='custom-tab', selected_className='custom-tab--selected', children=[
            html.H1("Styled content with CSS classes")
    ]),
        dcc.Tab(label='Tab two', className='custom-tab', selected_className='custom-tab--selected', children=[
            html.H1("Styled content with CSS classes part 2!")
        ]),
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)
