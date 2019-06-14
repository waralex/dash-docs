library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

LoadExampleCode <- function(filename, wd = NULL) {
  # Take a self-contained DashR example filename,
  # eval it, and return that example's `layout`
  # and the source code.

  example.file.as.string <- readChar(filename, file.info(filename)$size);

  # modify the example code so that it can run within
  # the context of an already running app
  example.ready.for.eval <- example.file.as.string
  replacements = list(
    # set the layout to a variable so that we can access it
    # and return it
    list('app\\$layout\\(', 'layout <- htmlDiv\\('),

    # Since app is in the namespace from the `app.R` import,
    # it will implicity be picked up by the
    # `eval` call below
    list('app <- Dash\\$new\\(\\)', ''),
    list('app\\$run_server\\(\\)', '')
  )
  for(replacement in replacements) {
    example.ready.for.eval <- gsub(
      replacement[1],
      replacement[2],
      example.ready.for.eval
    )
  }

  example.ready.for.eval <- paste(unlist(strsplit(example.ready.for.eval, "\r")), collapse = " ")
  
  if(!is.null(wd)) {

    currentWd <- getwd()
    newWd <- paste(c(currentWd, wd),collapse =  "/")
    
    example.ready.for.eval <- paste(c("setwd(newWd)", 
                                      example.ready.for.eval, 
                                      "setwd(currentWd)"), 
                                    collapse = "\n")
  }

  # run the example and implicitly assign the `layout` variable
  eval(parse(text=example.ready.for.eval))
  
  list(
    layout = htmlDiv(className = 'example-container', children = layout),
    source_code=htmlDiv(
      children=dccSyntaxHighlighter(example.file.as.string),
      className = 'code-container'
    )
  )
}

LoadAndDisplayComponent <- function(example_string) {
  return(
    htmlDiv(
      list(
        htmlDiv(
          children=dccSyntaxHighlighter(example_string),
          className='code-container'
        ),
        htmlDiv(
          className='example-container',
          children=eval(parse(text=example_string))
        )
      )
    )
  )
}


# ComponentBlock <- function(example_string){
#   return(htmlDiv(list(
#     dccSyntaxHighlighter(
#       example_string,
#       language='r',
#       customStyle=styles.code_container
#     ),
#     htmlDiv(
#       children=eval(parse(text=example_string)),
#       className='example-container',
#       style=list('overflow-x' = 'initial')
#     ))))
# }
