library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)
library(dashTable)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  quickStart = utils$LoadExampleCode('dashr/chapters/dashDataTable/examples/quickStart.R')
)

subTitleLink <- function(folder, componentName) {
  htmlH4(
    dccLink(
      paste0(c(folder, componentName), collapse = ". "),
      href = paste0('dashDataTable/', gsub(" ", "", folder))
    )
  )
}

layout <- htmlDiv(
  list(
    dccMarkdown("
> *** New! Released on November 2, 2018 ***
>
> *Dash DataTable is an interactive table component designed for viewing, 
> editing, and exploring large datasets.*
>
> *DataTable is rendered with standard, 
> semantic HTML `<table/>` markup, which makes it accessible, 
> responsive, and easy to style.*
>
> *7 months in the making, this is the most complex Dash component that Plotly has written, 
> all from the ground-up using React and TypeScript. 
> DataTable was designed with a featureset that allows 
> that Dash users to create complex, spreadsheet driven applications with no compromises. 
> We're excited to continue to work with users and companies that 
> [invest in DataTable's future](https://plot.ly/products/consulting-and-oem/?_ga=2.1935537.1022559183.1559571095-1541667138.1549398001).*
>
> *DataTable is in `Alpha`. This is more of a statement on the DataTable API rather than on its features. 
> The table currently works beautifully and is already used in production at F500 companies. 
> However, we expect to make a few more breaking changes to its API and behavior within the next couple of months. 
> Once the community feels good about its API, we'll lock it down and we'll commit to reducing the frequency of 
> breaking changes. Please subscribe to 
> [dash-table#207](https://github.com/plotly/dash-table/issues/207) and 
> the [CHANGELOG.md](https://github.com/plotly/dash-table/blob/master/CHANGELOG.md) to 
> stay up-to-date with any breaking changes.*
> 
> *So, check out DataTable and let us know what you think. Or even better, 
> share your DataTable Dash apps on the 
> [community forum](https://community.plot.ly/t/show-and-tell-community-thread/7554?_ga=2.70598800.1022559183.1559571095-1541667138.1549398001)!* 
> -- chriddyp   

# Quickstart
                "),
    
    examples$quickStart$source,
    examples$quickStart$layout,
    
    htmlDiv(
      list(
        subTitleLink("Part 1", "Sizing"),
        dccMarkdown("All about sizing the DataTable. Examples include:

- Setting the width and the height of the table

- Responsive table design

- Setting the widths of individual columns

- Handling long text

- Fixing rows and columns
                    ")
      )
    ),
    
    htmlDiv(
      list(
        subTitleLink("Part 2", "Styling"),
        dccMarkdown("The style of the DataTable is highly customizable. This chapter includes examples for:

- Conditional formatting

- Displaying multiple rows of headers

- Highlighting rows, columns, and cells

- Styling the table as a list view

- Changing the colors (including a dark theme!)

The sizing API for the table has been particularly tricky for us to nail down, so be sure to read this chapter to understand the nuances, 
limitations, and the APIs that we're exploring.
                    ")
      )
    ),
    
    htmlDiv(
      list(
        subTitleLink("Part 3", "Sorting, Filtering, Selecting, and Paging"),
        dccMarkdown("The DataTable is interactive. This chapter demonstrates the interactive features of the table and how to wire up these interations to Python callbacks. 
These actions include:
                    
- Paging
                    
- Selecting Rows
                    
- Sorting Columns
                    
- Filtering Data
                    ")
        )
        ),
    htmlHr(),
    dccMarkdown("
[Back to the Table of Contents](/)
                ")
  )
)
