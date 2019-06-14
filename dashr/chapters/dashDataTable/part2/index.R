library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashTable)

utils <- new.env()
source('dashr/utils.R', local=utils)

df <- data.frame(
  Date = c("2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"),
  Region = c("Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"),
  Temperature = c(1, -20, 3.512, 4, 10423, -441.2),
  Humidity = seq(10, 60, by = 10),
  Pressure = c(2, 10924, 3912, -10, 3591.2, 15)
)

examples <- list(
  example = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/example.R'),
  examplePseudo = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/examplePseudo.R'),
  highlight1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlight1.R'),
  highlightPseudo1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlightPseudo1.R'),
  highlight2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlight2.R'),
  highlightPseudo2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlightPseudo2.R'),
  highlight3 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlight3.R'),
  highlightPseudo3 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlightPseudo3.R'),
  highlight4 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlight4.R'),
  highlightPseudo4 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/highlightPseudo4.R'),
  darkTheme1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/darkTheme1.R'),
  darkThemePseudo1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/darkThemePseudo1.R'),
  darkTheme2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/darkTheme2.R'),
  darkThemePseudo2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/darkThemePseudo2.R'),
  stripedRows1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stripedRows1.R'),
  stripedRowsPseudo1 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stripedRowsPseudo1.R'),
  stripedRows2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stripedRows2.R'),
  stripedRowsPseudo2 = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stripedRowsPseudo2.R'),
  columnAlignment = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/columnAlignment.R'),
  columnAlignmentPseudo = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/columnAlignmentPseudo.R'),
  minimalHeaders = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/minimalHeaders.R'),
  minimalHeadersPseudo = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/minimalHeadersPseudo.R'),
  multiHeaders = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/multiHeaders.R'),
  multiHeadersPseudo = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/multiHeadersPseudo.R'),
  stylingAsList = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stylingAsList.R'),
  stylingAsListPseudo = utils$LoadExampleCode('dashr/chapters/dashDataTable/part2/examples/stylingAsListPseudo.R')
)

layout <- htmlDiv(
  list(
    dccMarkdown("
# Styling the DataTable
                
## Default Styles
                
By default, the DataTable has grey headers and borders around each cell. 
It resembles a spreadsheet and the headers are clearly defined.              
    "),
    
    examples$examplePseudo$source_code,
    examples$example$layout,
    
    dccMarkdown("
## Column Alignment

When displaying numerical data, 
it's a good practice to use monospaced fonts, 
to right-align the data, and to provide the same number of decimals throughout the column.

> Note that it's not possible to modify the number of decimal places in css. 
> Package `dashDataTable` will provide formatting options in the future, 
> until then you'll have to modify your data before displaying it. 
> Relevant issue: https://github.com/plotly/dash-table/issues/189

For textual data, left-aligning the text is usually easier to read.

In both cases, the column headers should have the same alignment as the cell content.
                "),
    
    examples$columnAlignmentPseudo$source_code,
    examples$columnAlignment$layout,
    
    dccMarkdown("
## Styling the Table as a list

The gridded view is a good default view for an editable table as it looks and feels like a spreadsheet. If your table isn't editable, 
then in many cases it can look cleaner without the vertical grid lines.
                "),
    
    examples$stylingAsListPseudo$source_code,
    examples$stylingAsList$layout,
    
    dccMarkdown("
## List Style with Minimal Headers

In some contexts, the grey background can look a little heavy. 
You can lighten this up by giving it a white background and a bold text.
                "),
    
    examples$minimalHeadersPseudo$source_code,
    examples$minimalHeaders$layout,
    
    dccMarkdown("
## Striped Rows

When you're viewing datasets where you need to compare values within individual rows, it can sometimes be helpful to give the rows alternating background colors. We recommend 
using colors that are faded so as to not attract too much attention to the stripes.
                "),
    
    examples$stripedRowsPseudo1$source_code,
    examples$stripedRows1$layout,
    examples$stripedRowsPseudo2$source_code,
    examples$stripedRows2$layout,
    
    dccMarkdown("
## Multi-Headers

Multi-headers are natively supported in the `DataTable`. 
Just set `name` inside `columns` as a list of strings instead of a single string and 
toggle `merge_duplicate_headers = TRUE`. 
`DataTable` will check the neighbors of each header row and, 
if they match, will merge them into a single cell automatically.                
                "),
    
    examples$multiHeadersPseudo$source_code,
    examples$multiHeaders$layout,
    
    dccMarkdown("
## Dark Theme with Cells

You have full control over all of the elements in the table. If you are viewing your table in an app with a dark background, 
you can provide inverted background and font colors.
                "),
    
    examples$darkThemePseudo1$source_code,
    examples$darkTheme1$layout,
    examples$darkThemePseudo2$source_code,
    examples$darkTheme2$layout,
    
    dccMarkdown("
## Conditional Formatting - Highlighting Certain Rows

You can draw attention to certain rows by providing 
a unique background color, bold text, or colored text.
                "),
    
    examples$highlightPseudo1$source_code,
    examples$highlight1$layout,
    examples$highlightPseudo2$source_code,
    examples$highlight2$layout,
    
    dccMarkdown("
## Conditional Formatting - Highlighting Certain Columns
                
Similarly, certain columns can be highlighted.
                "),
    
    examples$highlightPseudo3$source_code,
    examples$highlight3$layout,
    
    dccMarkdown("
## Conditional Formatting - Highlighting Cells
                
You can also highlight certain cells. 
For example, you may want to highlight certain cells 
that exceed a threshold or that match a filter elsewhere 
in the app.

The `filter` keyword in 
`style_data_conditional` uses the same filtering expression 
language as the table's interactive filter UI. 
See the [DataTable filtering chapter] for more info.

> Note, the filtering expression language is subject to change. 
> Please subscribe to [dash-table#169](https://github.com/plotly/dash-table/issues/169) for more info.
                "),
    
    examples$highlightPseudo4$source_code,
    examples$highlight4$layout,
    
    htmlHr(),
    dccMarkdown("
[Back to the DashTable Documentation](/dashDataTable)
                "),
    dccMarkdown("
[Back to the Dash Documentation](/)
                ")
  )
)