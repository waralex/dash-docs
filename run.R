library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

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
chapters.dashDataTable <- new.env()
source('dashr/chapters/dashDataTable/index.R', local=chapters.dashDataTable)
chapters.dashDataTablePart1 <- new.env()
source('dashr/chapters/dashDataTable/part1/index.R', local=chapters.dashDataTablePart1)
chapters.dashDataTablePart2 <- new.env()
source('dashr/chapters/dashDataTable/part2/index.R', local=chapters.dashDataTablePart2)
chapters.dashDataTablePart3 <- new.env()
source('dashr/chapters/dashDataTable/part3/index.R', local=chapters.dashDataTablePart3)
chapters.dashDataTablePart4 <- new.env()
source('dashr/chapters/dashDataTable/part4/index.R', local=chapters.dashDataTablePart4)
chapters.dashDataTablePart5 <- new.env()
source('dashr/chapters/dashDataTable/part5/index.R', local=chapters.dashDataTablePart5)
chapters.dashDataTablePart6 <- new.env()
source('dashr/chapters/dashDataTable/part6/index.R', local=chapters.dashDataTablePart6)
chapters.dashDataTablePart7 <- new.env()
source('dashr/chapters/dashDataTable/part7/index.R', local=chapters.dashDataTablePart7)
chapters.dashDataTablePart8 <- new.env()
source('dashr/chapters/dashDataTable/part8/index.R', local=chapters.dashDataTablePart8)
chapters.dashDataTablePart9 <- new.env()
source('dashr/chapters/dashDataTable/part9/index.R', local=chapters.dashDataTablePart9)

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
  htmlDiv(
    list(
      htmlDiv(
        style = list(display = "none"),
        children = list(dashDataTable())
      ),
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
    )
  )
)

app$callback(output=list(id='chapter', property='children'),
             params=list(input('url', 'pathname')),
             function(pathname) {
               switch(
                 pathname,
                 "/installation" = return(chapters.installation$layout),
                 "/getting-started" = return(chapters.getting_started$layout),
                 "/getting-started-part-2" = return(chapters.callbacks$layout),
                 "/state" = return(chapters.state$layout),
                 "/graph-crossfiltering" = return(chapters.graph_crossfiltering$layout),
                 "/data-callbacks" = return(chapters.data_callbacks$layout),
                 "/faq-gotchas" = return(chapters.faq_gotchas$layout),
                 '/dash-core-components' = return(chapters.dashCoreComponents$layout),
                 '/dash-core-components/dropdown' = return(chapters.dccDropdown$layout),
                 '/dash-html-components' = return(chapters.dashHtmlComponents$layout),
                 '/dashDataTable' = return(chapters.dashDataTable$layout),
                 '/dashDataTable/Part1' = return(chapters.dashDataTablePart1$layout),
                 '/dashDataTable/Part2' = return(chapters.dashDataTablePart2$layout),
                 '/dashDataTable/Part3' = return(chapters.dashDataTablePart3$layout),
                 '/dashDataTable/Part4' = return(chapters.dashDataTablePart4$layout),
                 '/dashDataTable/Part5' = return(chapters.dashDataTablePart5$layout),
                 '/dashDataTable/Part6' = return(chapters.dashDataTablePart6$layout),
                 '/dashDataTable/Part7' = return(chapters.dashDataTablePart7$layout),
                 '/dashDataTable/Part8' = return(chapters.dashDataTablePart8$layout),
                 '/dashDataTable/Part9' = return(chapters.dashDataTablePart9$layout),
                 '/external-resources' = return(chapters.external_resources$layout),
                 {
                   
                   htmlDiv(
                     list(
                       htmlH1('DashR User Guide'),
                       htmlH2('What\'s Dash?',
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       htmlA('Introduction', href='https://dash.plot.ly/introduction'),
                       
                       dccMarkdown("A quick paragraph about Dash and a link to the talk at Plotcon that started it all."),
                       
                       htmlA(
                         'Announcement Essay',
                         href='https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503'
                       ),
                       
                       dccMarkdown("Our extended essay on Dash. An extended discussion of Dash's architecture and our motivation behind the project."),
                       
                       htmlA(
                         'Dash App Gallery',
                         href='https://dash.plot.ly/gallery'
                       ),
                       
                       dccMarkdown("A glimpse into what's possible with Dash."),
                       htmlA(
                         'Dash Club',
                         href='https://plot.us12.list-manage.com/subscribe?u=28d7f8f0685d044fb51f0d4ee&id=0c1cb734d7'
                       ),
                       
                       dccMarkdown("A fortnightly email newsletter by chriddyp, the creator of Dash."),
                       
                       htmlH2("Dash Tutorial",
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccLink(
                         'Part 1. Installation',
                         href='/installation'
                       ),
                       dccMarkdown(""),
                       dccLink(
                         'Part 2. The Dash Layout',
                         href='/getting-started'
                       ),
                       dccMarkdown("The Dash `layout` describes what your app will look like and is composed of a set of declarative Dash components."),
                       
                       dccLink(
                         'Part 3. Basic Callbacks',
                         href='/getting-started-part-2'
                       ),
                       dccMarkdown("Dash apps are made interactive through Dash Callbacks:
R functions that are automatically called whenever an input component's property changes. Callbacks can be chained,
allowing one update in the UI to trigger several updates across the app."),
                       
                       dccLink(
                         'Part 4. Callbacks With State',
                         href='/state'
                       ),
                       dccMarkdown("Basic callbacks are fired whenever the values change.
Use Dash `state` with Dash `inputs` to pass in extra values whenever the `inputs` change.
`state` is useful for UIs that contain forms or buttons."),
                       
                       dccLink(
                         'Part 5. Interactive Graphing and Crossfiltering',
                         href='/graph-crossfiltering'
                       ),
                       dccMarkdown("
Bind interactivity to the Dash `Graph` component whenever you hover, click or select points on your chart.
                       "),
                       
                       dccLink(
                         'Part 6. Sharing Data Between Callbacks',
                         href='/data-callbacks'
                       ),
                       dccMarkdown("`global` variables will break your Dash apps. 
However, there are other ways to share data between callbacks.
This chapter is useful for callbacks that run expensive data processing tasks or process large data.
                                   "),
                       
                       dccLink(
                         'Part 7. FAQs and Gotchas',
                         href='/faq-gotchas'
                       ),
                       dccMarkdown("If you have read through the rest of the tutorial and still have questions 
or are encountering unexpected behaviour,this chapter may be useful."),
                       
                       htmlH2('Component Libraries',
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccLink(
                         'Dash Core Components',
                         href='/dash-core-components'
                       ),
                       
                       dccMarkdown("The Dash Core Component library contains a set of higher-level components like sliders, graphs, dropdowns, tables, and more."),
                       dccLink(
                         'Dash HTML Components',
                         href='/dash-html-components'
                       ),
                       
                       dccMarkdown("Dash provides all of the available HTML tags as user-friendly Python classes.
This chapter explains how this works and the few important key differences between Dash HTML components and standard html.
                    "),
                       dccLink(
                         'Dash DataTable',
                         href='/dashDataTable'
                       ),
                       
                       dccMarkdown("The Dash DataTable is our latest and most advanced component. 
It is an interactive table that supports rich styling, conditional formatting, editing, sorting, filtering, and more."),
                       htmlH2('Creating Your Own Components',
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccMarkdown("IN PROGRESS..."),
                       
                       htmlH2('Beyond the Basics',
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccLink(
                         'Adding CSS & JS and Overriding the Page-Load Template',
                         href='/external-resources'
                       ),
                       
                       dccMarkdown("
Learn how to add custom CSS and JS to your application with the `assets` directory. 
Also, learn how to customize the HTML template that Dash serves on page load in order to add custom meta tags, customize the page's title, and more.
                                   "),
                       
                       htmlH2('Getting Help',
                              style = list(
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccMarkdown("IN PROGRESS..."),
                       
                       htmlH2('Dash Deployment Server',
                              style = list(
                                color = "rgb(13, 118, 191)",
                                'border-bottom' = 'thin lightgrey solid',
                                'margin-top' = '50px'
                              )),
                       dccMarkdown("Dash Deployment Server is Plotly's commercial offering for hosting and sharing 
Dash apps on-premises or in the cloud."),
                       dccLink(
                         'About Dash Deployment Server',
                         href='/faq-gotchas'
                       ),
                       
                       dccLink(
                         'Dash Deployment Server Documentation',
                         href='/faq-gotchas'
                       )
                       
                     )
                   )
                 }
               )
             })

app$run_server(host = "0.0.0.0", port = Sys.getenv('PORT', 8050))
