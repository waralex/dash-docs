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
        <!-- Global site tag (gtag.js) - AdWords: 1009791370 -->
        <script async src=""https://www.googletagmanager.com/gtag/js?id=AW-1009791370""></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'AW-1009791370');
        </script>
        <!-- Google Tag Manager Tag -->
        <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-N6T2RXG');</script>
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
