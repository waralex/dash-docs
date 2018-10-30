import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
         <!-- Google Tag Manager Tag -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG" height="0" width="0" style="display:none visibility:hidden"></iframe></noscript>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)
