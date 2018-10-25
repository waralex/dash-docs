import dash
import dash_html_components as html


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        print(kwargs)
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>My App</title>
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
                <!-- Google Tag Manager (noscript) -->
                <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG"
                height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
                <!-- End Google Tag Manager (noscript) -->

                <div id="custom-header">My custom header</div>
                {app_entry}
                {config}
                {scripts}
                <div id="custom-footer">My custom footer</div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'])

app = CustomDash()

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)
