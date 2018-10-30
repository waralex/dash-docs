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
