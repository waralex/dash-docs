library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  local_css=readLines('dashr/chapters/external-resources/examples/local-css.R')
  # custom_index_string=utils$LoadExampleCode('dashr/chapters/external-resources/examples/custom-index-string.R'),
  # custom_interpolate_string=utils$LoadExampleCode('dashr/chapters/external-resources/examples/custom-interpolate-string.R'),
  # dash_meta_tags=utils$LoadExampleCode('dashr/chapters/external-resources/examples/dash-meta-tags.R'),
  # custom_dash_renderer=utils$LoadExampleCode('dashr/chapters/external-resources/examples/custom-dash-renderer.R'),
  # custom_dash_renderer_hooks=utils$LoadExampleCode('dashr/chapters/external-resources/examples/custom-dash-renderer-hooks.R'),
  # external_resources_init=utils$LoadExampleCode('dashr/chapters/external-resources/examples/external-resources-init.R')
)

layout <- htmlDiv(list(
  htmlH1('Adding CSS & JS and Overriding the Page-Load Template'),
  dccMarkdown("
Dash applications are rendered in the web browser with CSS and JavaScript.
On page load, Dash serves a small HTML template that includes references to
the CSS and JavaScript that are required to render the application.
This chapter covers everything that you need to know about configuring
this HTML file and about including external CSS and JavaScript in Dash
applications.

**Table of Contents**
- Adding Your Own CSS and JavaScript to Dash Apps
- Embedding Images in Your Dash Apps
- Adding External CSS and JavaScript
- Customizing Dash's HTML Index Template
- Adding Meta Tags
- Serving Dash's Component Libraries Locally or from a CDN
- Sample Dash CSS Stylesheet
***

## Adding Your Own CSS and JavaScript to Dash Apps

**New in dash 0.22.0**

Including custom CSS or JavaScript in your Dash apps is simple.
Just create a folder named `assets` in the root of your app directory
and include your CSS and JavaScript
files in that folder. Dash will automatically serve all of the files that
are included in this folder. By default the url to request the assets will
be `/assets` but you can customize this with the `assets_url_path` argument
to `dash.Dash`.

**Important: For these examples, you need to include `__name__` in your Dash constructor.**

That is, `app = dash.Dash(__name__)` instead of `app = dash.Dash()`. [Here's why](https://community.plot.ly/t/dash-app-does-not-load-assets-and-app-index-string/12178/10?u=chriddyp).

### Example: Including Local CSS and JavaScript

We'll create several files: `app.py`, a folder named `assets`, and
three files in that folder:
```
- app.py
- assets/
    |-- typography.css
    |-- header.css
    |-- custom-script.js


```

`app.py`
  "),

  dccSyntaxHighlighter(
    examples$local_css,
    language='r'
  ),
  htmlDiv(
    dccMarkdown('`typography.css`'),
    style=list('paddingTop' = 20)
  ),

  dccSyntaxHighlighter(
"body {
    font-family: sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: hotpink
}
",
    language='css'
  ),
htmlHr(),

htmlDiv(
  dccMarkdown('`header.css`'),
  style=list('paddingTop' = 20)
),

dccSyntaxHighlighter(
  "app-header {
    height: 60px;
    line-height: 60px;
    border-bottom: thin lightgrey solid;
}

.app-header .app-header--title {
    font-size: 22px;
    padding-left: 5px;
}
",
language='css'
),

htmlHr(),
htmlDiv(
  dccMarkdown('`custom-script.js`'),
  style=list('paddingTop' = 20)
),
dccSyntaxHighlighter("
alert('If you see this alert, then your custom JavaScript script has run!')
",
  language='javascript'
),
htmlHr(),

dccMarkdown("
When you run `app.py`, your app should look something like this:
(Note that there may be some slight differences in appearance as
the CSS from this Dash User Guide is applied to all of these embedded
examples.)
    ")
))
