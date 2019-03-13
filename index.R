library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)
getwd()
dir()
source('app.R')

chapters.installation <- new.env()
source('dashr/chapters/installation/index.R', local=chapters.installation)
chapters.getting_started <- new.env()
source('dashr/chapters/getting-started/index.R', local=chapters.getting_started)
chapters.callbacks <- new.env()
source('dashr/chapters/callbacks/index.R', local=chapters.callbacks)
chapters.state <- new.env()
source('dashr/chapters/state/index.R', local=chapters.state)


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

    htmlDiv(css.links),
    dccLocation(id='url'),

    # Temporary workaround until https://github.com/plotly/dashR/commit/7663d584926ca0cb49797f7c122da9a30af5910b
    # is merged
    dccGraph(
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
        )
    )))
  }
})

app$run_server()
