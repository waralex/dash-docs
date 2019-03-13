library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)
source('app.R')

chapters.installation <- new.env()
source('dashr/chapters/installation/index.R', local=chapters.installation)
chapters.getting_started <- new.env()
source('dashr/chapters/getting-started/index.R', local=chapters.getting_started)
chapters.callbacks <- new.env()
source('dashr/chapters/callbacks/index.R', local=chapters.callbacks)
chapters.state <- new.env()
source('dashr/chapters/state/index.R', local=chapters.state)
chapters.graph_crossfiltering <- new.env()
source('dashr/chapters/graph-crossfiltering/index.R', local=chapters.graph_crossfiltering)
chapters.data_callbacks <- new.env()
source('dashr/chapters/data-callbacks/index.R', local=chapters.data_callbacks)
chapters.faq_gotchas <- new.env()
source('dashr/chapters/faq-gotchas/index.R', local=chapters.faq_gotchas)

# Temporary workaround until `assets/` are loaded
# This will serve the CSS files in `assets` from a separate
# webserver.
# In a separate terminal, run
# python2 -m SimpleHTTPServer 8000
# css.files = list.files('assets')
# css.links = lapply(css.files, function(filename) {
#   htmlLink(
#     href=sprintf('http://localhost:8000/assets/%s', filename),
#     rel="stylesheet"
#   )
# })


app$layout_set(
  htmlDiv(list(

    dccLocation(id='url'),
    htmlDiv(
      className='background',
      children=list(
        htmlDiv(id='wait-for-layout'),
        htmlDiv(
          className='container-width',
          children=htmlDiv(
            htmlDiv(id='chapter', className='content'),
            className='content-container'
          )
        )
      )
    )
  ))
)

app$callback(output=list(id='chapter', property='children'),
             params=list(input('url', 'pathname')),
             function(pathname) {
  if (pathname == "/installation") {
    return(chapters.installation$layout)
  } else if (pathname == "/getting-started") {
     return(chapters.getting_started$layout)
  } else if (pathname == "/getting-started-part-2") {
    return(chapters.callbacks$layout)
  } else if (pathname == "/state") {
    return(chapters.state$layout)
  } else if (pathname == "/graph-crossfiltering") {
    return(chapters.graph_crossfiltering$layout)
  } else if (pathname == "/data-callbacks") {
    return(chapters.data_callbacks$layout)
  } else if (pathname == "/faq-gotchas") {
    return(chapters.faq_gotchas$layout)
  } else {
    return(htmlDiv(list(
      htmlH1('DashR User Guide'),
      dccLink(
        'Part 1. Installation',
        href='/installation'
      ),
      htmlBr(),
      dccLink(
        'Part 2. The Dash Layout',
        href='/getting-started'
      ),
      htmlBr(),
      dccLink(
        'Part 3. Basic Callbacks',
        href='/getting-started-part-2'
      ),
      htmlBr(),
      dccLink(
        'Part 4. Callbacks With State',
        href='/state'
      ),
      htmlBr(),
      dccLink(
        'Part 5. Interactive Graphing and Crossfiltering',
        href='/graph-crossfiltering'
      ),
      htmlBr(),
      dccLink(
        'Part 7. FAQs and Gotchas',
        href='/faq-gotchas'
      )
    )))
  }
})

app$run_heroku()
