library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$index_string = "
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
"

app$layout(htmlDiv('Simple Dash App'))

# app$run_heroku()
