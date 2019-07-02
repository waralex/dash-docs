getwappName <- Sys.getenv("DASH_APP_NAME")

if (appName != ""){
  
  pathPrefix <- sprintf("/%s/", appName)
  
  
  
  Sys.setenv(DASH_ROUTES_PATHNAME_PREFIX = pathPrefix,
             
             DASH_REQUESTS_PATHNAME_PREFIX = pathPrefix)
  
  
  
  setwd(sprintf("/app/apps/%s", appName))
  
}



setwd("C:/Users/hamma/Documents/dashBioDocs/dashR/chapters/dashBio")

#Source assets
source("assets/utils.R")
source("DashBioDocsMain.R")
source("app.R")

# Load Necessary Packages
library('dash')
library('dashCoreComponents')
library('dashHtmlComponents')
library('dashBio')
library('dashTable')
library('readr')
library('heatmaply')
library('data.table')
library('jsonlite')
library('rjson')




chapters.alignment <- new.env()
source('alignment-chart/alignment-chart.R', local=chapters.alignment)
chapters.circos <- new.env()
source('circos/circos.R', local=chapters.circos)
chapters.clustergram <- new.env()
source('clustergram/clustergram.R', local=chapters.clustergram)
chapters.ideogram <- new.env()
source('ideogram/ideogram.R', local=chapters.ideogram)
chapters.volcanoplot <- new.env()
source('volcanoplot/volcano.R', local=chapters.volcanoplot)
chapters.manhattan <- new.env()
source('manhattan/manhattan.R', local = chapters.manhattan)
chapters.molecule3dviewer <- new.env()
source('molecule3dviewer/molecule3dviewer.R', local=chapters.molecule3dviewer)
chapters.molecule2dviewer <- new.env()
source('molecule2dviewer/molecule2dviewer.R', local=chapters.molecule2dviewer)
chapters.needleplot <- new.env()
source('needleplot/needleplot.R', local=chapters.needleplot)

header <- htmlDiv(list(
  htmlDiv(list(
    htmlDiv(list(
      htmlA(className = "logo-link", href = "https://plot.ly/products/dash",
            children= htmlImg(src="assets/logo.png",
                              style = list("height" = "60px", "width" = "230px"))),
      htmlDiv(className = "links", children = list(
        htmlA(className = "link", children = "pricing", href = "https://plot.ly/dash/pricing?_ga=2.241429382.584183071.1559580389-2135338473.1556993734"),
        htmlA(className = 'link', children = 'user guide', href = "/"),
        htmlA(className = 'link', children = 'plotly', href = "https://plot.ly/"),
        htmlA(className = 'link', href="https://dash.plot.ly/search", children = 
                htmlI(className = 'fa fa-search'))
        
      ))
    ))
  ), className = 'container-width')
), className = "header")


app$layout(
  header,
  htmlDiv(
    list(
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
                 "/AlignmentChart" = return(chapters.alignment$layout),
                 "/Circos" = return(chapters.circos$layout),
                 "/Clustergram" = return(chapters.clustergram$layout),
                 "/Ideogram" = return(chapters.ideogram$layout),
                 "/ManhattanPlot" = return(chapters.manhattan$layout),
                 "/Molecule2dViewer" = return(chapters.molecule2dviewer$layout),
                 "/Molecule3dViewer" = return(chapters.molecule3dviewer$layout),
                 "/VolcanoPlot" = return(chapters.volcanoplot$layout),
                 "/NeedlePlot" = return(chapters.needleplot$layout),
                 {mainLayout
                   }
               )
             })



if (appName != "") {
  
  app$run_server(host = "0.0.0.0", port = Sys.getenv('PORT', 8050))
  
} else {
  
  app$run_server()
  
}

