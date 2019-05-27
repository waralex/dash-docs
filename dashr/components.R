source('dashr/styles.R')

Syntax = function(children, language='python', style=styles.code_container, summary=''){
  if (isTRUE(summary)){
  return(htmlDetails(list(
    htmlSummary(summary),
    dccSyntaxHighlighter(
      children,
      language=language,
      customStyle=style
    )
  ), 
    open=TRUE))}
  
else{
  return(dccSyntaxHighlighter(
    children,
    language=language,
    customStyle=style
  ))
}}

Example = function(example){
  return(htmlDiv(example, className='example-container'))}
