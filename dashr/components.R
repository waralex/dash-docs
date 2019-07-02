source('dashr/styles.R')

# Added Reuseable Components

Header <- function(title) {
  return (
    htmlDiv(
      htmlH2(
        list(htmlDiv(title)),
        style = list('borderBottom' = 'thin lightgrey solid', 'marginRight' = 20)
      ),
    )
  )
}

Chapter <- function(name, href = NA, caption = NA) {
  divTitle <- htmlLi(
    dccLink(
      name,
      href = href,
      id = href,
      className = 'toc--chapter-link'
    ),
  )
  divCaption <- htmlSmall(
    className = 'toc--chapter-content',
    children = dccMarkdown(caption),
    style = list(
      'display' = 'block',
      'marginTop' = '-8px'
    )
  )
  if (!is.na(caption)) {
    return (htmlDiv(className = 'toc--chapter', children = list(divTitle, divCaption)))
  } else {
    return (htmlDiv(className = 'toc--chapter', children = list(divTitle)))
  }
}

# Existing Components (may need to edit)

Syntax <- function(children, language='R', style=styles$code_container, summary=''){
  if (!(summary == '')){
  return(htmlDetails(list(
    htmlSummary(summary),
    htmlDiv(children)
    ),
    open=TRUE))}
else{
  return(dccSyntaxHighlighter(
    children,
    'language'=language,
    'customStyle'=style
  ))
}}

Example <- function(example){
  return(htmlDiv(example, className='example-container'))}

