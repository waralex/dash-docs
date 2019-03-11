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

# Temporary workaround until `assets/` are loaded
# This will serve the CSS files in `assets` from a separate
# webserver.
# In a separate terminal, run
# python2 -m SimpleHTTPServer 8000
css.files = list.files('assets')
css.links = lapply(css.files, function(filename) {
  htmlLink(
    href=sprintf('http://localhost:8000/assets/%s', filename),
    rel="stylesheet"
  )
})

app$layout_set(
  htmlDiv(list(

    coreLocation(id='url'),

    # Temporary workaround until https://github.com/plotly/dashR/commit/7663d584926ca0cb49797f7c122da9a30af5910b
    # is merged
    coreGraph(
      id='hidden',
      figure=list(data=list()),
      style=list(display='none')
    ),

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
  } else {
    return(htmlDiv(list(
      htmlH1('DashR User Guide'),
      coreLink(
        'Part 1. Installation',
        href='/installation'
      ),
      htmlBr(),
      coreLink(
        'Part 2. The Dash Layout',
        href='/getting-started'
      ),
      htmlBr(),
      coreLink(
        'Part 3. Basic Callbacks',
        href='/getting-started-part-2'
      ),
      htmlBr(),
      coreLink(
        'Part 4. Callbacks With State',
        href='/state'
      ),
      htmlBr(),
      coreLink(
        'Part 5. Interactive Graphing and Crossfiltering',
        href='/graph-crossfiltering'
      ),
      htmlBr(),
      coreLink(
        'Part 6. Sharing Data Between Callbacks',
        href='/data-callbacks'
      )
    )))
  }
})

app$run_heroku()
