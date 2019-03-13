library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

layout <- htmlDiv(list(
htmlH1('Dash Installation'),
dccMarkdown("
In your terminal, install several dash libraries. 
These libraries are under active development, so install and upgrade frequently. 
Make sure you're on at least version `3.0.2` of R. 
You can see what version of R you have by entering version in the R CLI. 
CRAN is the easiest place to download the latest R version.
"),
  
dccMarkdown("
```{r}
library(devtools) # devtools: Tools to Make Developing R Packages Easier  
install_github('plotly/dashR') # The core dash backend
install_github('plotly/dash-html-components') # HTML components   
install_github('plotly/dash-dcc-components') # Supercharged components
```

Ready? Now, let's [make your first Dash app](/getting-started).
"),

htmlHr(),

dccMarkdown("
> A quick note on checking your versions and on upgrading. 
> These docs are run using the versions listed above and 
> these versions should be the latest versions available. 
> To check which version that you have installed, you can run e.g.

> ```{r}
> library(dashCoreComponents) 
> packageVersion('dashCoreComponents')
> ```
> 
> To see the latest changes of any package, check the GitHub repo's CHANGELOG.md file:
> - [dash changelog](https://github.com/plotly/dash/blob/master/CHANGELOG.md)

")
  
))
