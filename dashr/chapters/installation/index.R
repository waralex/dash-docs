library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

layout <- htmlDiv(list(
  htmlH1('Dash Installation'),
  dccMarkdown("
    > In your terminal, install several dash libraries. 
    > These libraries are under active development, so install and upgrade frequently. 
    > Make sure you're on at least version `3.0.2` of R. 
    > You can see what version of R you have by entering version in the R CLI. 
    > CRAN is the easiest place to download the latest R version.
  
  "),
  dccMarkdown("

    ```
    library(devtools) # devtools: Tools to Make Developing R Packages Easier  
    install_github('plotly/dashR') # The core dash backend
    install_github('plotly/dash-html-components') # HTML components   
    install_github('plotly/dash-dcc-components') # Supercharged components
    ```

    Ready? Now, let's [make your first Dash app](/getting-started).
  ")
  
))
