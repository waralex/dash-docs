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

