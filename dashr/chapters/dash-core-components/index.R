library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

titleLink <- function(componentName) {
  return(htmlH2(
    dccLink(
      componentName,
      href=paste('/dashCoreComponents/', componentName, sep='')
    )
  ))
}

referenceLink <- function(componentName) {
  return(dccLink(
    'More examples & reference',
    href=paste('/dashCoreComponents/', componentName, sep='')
  ))
}

layout <- htmlDiv(list(

htmlH1('Dash Core Components'),

htmlDiv(titleLink('dccDropdown')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccDropdown(
  options=list(
    list(label="New York City", value="NYC"),
    list(label="Montréal", value="MTL"),
    list(label="San Francisco", value="SF")
  ),
  value="MTL"
)
'
),
htmlDiv(referenceLink('dccDropdown'))

))

route <- function(pathname) {
  componentName = gsub('/dashCoreComponents/dcc', '', pathname)
  component_chapter_index = file.path(
    'dashr',
    'chapters',
    'dash-core-components',
    componentName,
    'index.R'
  )
  tmp_namespace = new.env()
  source(component_chapter_index, local=tmp_namespace)
  return(tmp_namespace$layout);
}
