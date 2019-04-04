source('app.R')
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

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
chapters.dashCoreComponents <- new.env()
source('dashr/chapters/dash-core-components/index.R', local=chapters.dashCoreComponents)
chapters.dccDropdown <- new.env()
source('dashr/chapters/dash-core-components/dropdown/index.R', local=chapters.dccDropdown)
chapters.dashHtmlComponents <- new.env()
source('dashr/chapters/dash-html-components/index.R', local=chapters.dashHtmlComponents)
chapters.external_resources <- new.env()
source('dashr/chapters/external-resources/index.R', local=chapters.external_resources)


header <- htmlDiv(
  className = 'header',
  list(
    htmlDiv(
      style = list(height = '95%'),
      className = 'container-width',
      children = list(
        htmlA(htmlImg(
          style = list(height = '100%'),
          src = 'https://user-images.githubusercontent.com/1865834/50180824-abcc5f80-02d8-11e9-8319-8842909c3f8e.png'
        ), href = 'https://plot.ly/products/dash', className='logo-link'),

        htmlDiv(className='links', children = list(
          htmlA('pricing', className='link', href = 'https://plot.ly/dash/pricing'),
          htmlA('user guide', className='link', href = '/'),
          htmlA('plotly', className='link', href = 'https://plot.ly/'),
          htmlA(children=list(htmlI(className="fa fa-search")), className='link', href='https://dash.plot.ly/search')
        ))
      ))
))

app$layout(
  header,
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
  } else if (pathname == '/dash-core-components') {
    return(chapters.dashCoreComponents$layout)
  } else if (pathname == '/dash-core-components/dropdown') {
    return(chapters.dccDropdown$layout)
  } else if (pathname == '/dash-html-components') {
    return(chapters.dashHtmlComponents$layout)
  } else if (pathname == '/external-resources') {
    return(chapters.external_resources$layout)
  # } else if (startsWith(pathname, '/dashCoreComponents/')) {
  #   return(chapters.dashCoreComponents$route(pathname))
  } else {
    return(htmlDiv(list(
      htmlH1('DashR User Guide'),
      htmlH2('What\'s Dash?'),
      htmlHr(),
      htmlA('Introduction',
            href='https://dash.plot.ly/introduction'),
      htmlBr(),
      dccMarkdown("
A quick paragraph about Dash and a link to the talk at Plotcon that started it all.
      "),

      dccLink(
        'Announcement Essay',
        href='https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503'
      ),
      htmlBr(),
      dccMarkdown("
Our extended essay on Dash.
An extended discussion of Dash's architecture and our motivation behind the project.
      "),

      dccLink(
        'Dash App Gallery',
        href='https://dashr-docs.herokuapp.com'
      ),
      htmlBr(),
      dccMarkdown("
A glimpse into what's possible with Dash.
      "),
      dccLink(
        'Dash Club',
        href='https://plot.us12.list-manage.com/subscribe?u=28d7f8f0685d044fb51f0d4ee&id=0c1cb734d7'
      ),
      htmlBr(),
      dccMarkdown("
A fortnightly email newsletter by chriddyp, the creator of Dash.
      "),

      htmlH2("Dash Tutorial"),
      htmlHr(),
      dccLink(
        'Part 1. Installation',
        href='/installation'
      ),
      htmlBr(),
      dccLink(
        'Part 2. The Dash Layout',
        href='/getting-started'
      ),
      dccMarkdown("
The Dash `layout` describes what your app will look like
and is composed of a set of declarative Dash components.
      "),
      htmlBr(),
      dccLink(
        'Part 3. Basic Callbacks',
        href='/getting-started-part-2'
      ),
      dccMarkdown("
Dash apps are made interactive through Dash Callbacks:
R functions that are automatically called whenever
an input component's property changes. Callbacks can be chained,
allowing one update in the UI to trigger several updates across the app.
    "),
      htmlBr(),
      dccLink(
        'Part 4. Callbacks With State',
        href='/state'
      ),
      dccMarkdown("
Basic callbacks are fired whenever the values change.
Use Dash `State` with Dash `Inputs` to pass in extra values whenever the `Inputs` change.
`State` is useful for UIs that contain forms or buttons.
    "),
      htmlBr(),
      dccLink(
        'Part 5. Interactive Graphing and Crossfiltering',
        href='/graph-crossfiltering'
      ),
      dccMarkdown("
Bind interactivity to the Dash `Graph` component whenever you hover, click,
or select points on your chart.
      "),
      htmlBr(),
      dccLink(
        'Part 6. Sharing Data Between Callbacks',
        href='/data-callbacks'
      ),
      dccMarkdown("
`global` variables will break your Dash apps.
However, there are other ways to share data between callbacks.
This chapter is useful for callbacks that run expensive data processing tasks or process large data.
      "),
      htmlBr(),
      dccLink(
        'Part 7. FAQs and Gotchas',
        href='/faq-gotchas'
      ),
      dccMarkdown("
If you have read through the rest of the tutorial and still have questions
or are encountering unexpected behaviour,
this chapter may be useful.
      "),

      htmlH2('Component Libraries'),
      htmlHr(),
      dccLink(
        'Dash Core Components',
        href='/dash-core-components'
      ),
      htmlBr(),
      dccMarkdown("
The Dash Core Component library contains a set of higher-level components like sliders, graphs, dropdowns, tables, and more.
      "),
      dccLink(
        'Dash HTML Components',
        href='/dash-html-components'
      ),
      htmlBr(),
      dccMarkdown("
Dash provides all of the available HTML tags as user-friendly Python classes.
This chapter explains how this works and the few important key differences between Dash HTML components and standard html.
      "),

      htmlH2('Creating Your Own Components'),
      htmlHr(),
      dccMarkdown("
IN PROGRESS...
      "),

      htmlH2('Beyond the Basics'),
      htmlHr(),
      dccMarkdown("
IN PROGRESS...
      "),

      htmlH2('Getting Help'),
      htmlHr(),
      dccMarkdown("
IN PROGRESS...
      "),


      htmlH2('Dash Deployment Server',
             style = list(color = "rgb(13, 118, 191)")),
      htmlHr(),
      dccMarkdown("
Dash Deployment Server is Plotly's commercial offering for hosting and sharing
Dash apps on-premises or in the cloud.
      "),
      dccLink(
        'About Dash Deployment Server',
        href='/faq-gotchas'
      ),
      htmlBr(),
      dccLink(
        'Dash Deployment Server Documentation',
        href='/faq-gotchas'
      )

    )))
  }
})

app$run_server()
