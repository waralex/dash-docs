library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashTable)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  example1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part1/examples/example1.R')
)

layout <- htmlDiv(
  list(
    dccMarkdown("
# DataTable Sizing

### Default Styles

By default, the table will expand to the width of its container. 
The width of the columns is determined automatically in order to accommodate the content in the cells.
                "
    ),
    
    examples$example1$source_code,
    examples$example1$layout,
    
    dccMarkdown("
> The set of examples on this page are rendered with a few different dataframes that have different sizes 
> and shapes. In particular, 
> some of the dataframes have a large number of columns or have cells with long contents. 
> If you'd like to follow along on your own machine, 
> then open up the menu below to copy and paste the code behind these datasets.
                "),
    
    htmlBr(),

    dccMarkdown("
The default styles work well for a small number of columns and short text. 
However, if you are rendering a large number of columns or cells with long contents, 
then you'll need to employ one of the following \"overflow strategies\" to keep the table within its container.

> Heads up! In the future, 
> we may modify our default styles to better accommodate wide content 
> while keeping the table full-width and responsive. Subscribe to 
> [plotly/dash-table#197](https://github.com/plotly/dash-table/issues/197) for more.

### Overflow Strategies - Multiple Lines

If your cells contain contain text with spaces, 
then you can overflow your content into multiple lines.

> We find that this interface is a little too complex. 
> We're looking at simplifying this in this issue: https://github.com/plotly/dash-table/issues/188


                ")
  )
)