library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  button = utils$LoadExampleCode('dashr/chapters/dash-core-components/button/examples/button.R'),
  tabs = utils$LoadExampleCode('dashr/chapters/dash-core-components/tabs/examples/tabs.R')
)

titleLink <- function(componentName) {
  return(htmlH2(dccLink(
    paste(componentName),
    href=paste('/dash-core-components/', componentName, sep='')
  )))
}

referenceLink <- function(componentName, Title) {
  return(dccLink(
    paste(Title),
    href=paste('/dash-core-components/', componentName, sep='')
  ))
}

layout <- htmlDiv(list(

htmlH1('Dash Core Components'),

dccMarkdown(
  " Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the Dash team,
  is available in the `dashCoreComponents` package.
  The source is on GitHub at [plotly/dash-core-components](https://github.com/plotly/dash-core-components).
```{r}
install.packages('dashCoreComponents')
sessionInfo('dashCoreComponents')
```
  "
),

htmlDiv(titleLink('Dropdown')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccDropdown(
  options=list(
    list(label = "New York City", value = "NYC"),
    list(label = "Montréal", value = "MTL"),
    list(label = "San Francisco", value = "SF")
  ),
  value="MTL"
)
'
),


utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)

  dccDropdown(
    options=list(
      list(label = "New York City", value = "NYC"),
      list(label = "Montréal", value = "MTL"),
      list(label = "San Francisco", value = "SF")
    ),
    value = "MTL",
    multi = TRUE
  )
  '
),
htmlBr(),
htmlDiv(referenceLink('Dropdown', 'More Dropdown Examples and Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('Slider')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
dccSlider(
  min = -5,
  max = 10,
  step = 0.5,
  value = -3,
)
  '
),

utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
dccSlider(
  min = 0,
  max = 9,
  marks = lapply(1:10, function(x){paste("Label", x)}),
  value = 5,
)
  '
)
), style = list('padding' = '5px',
                'margin' = '0 auto')),

htmlBr(),
htmlDiv(referenceLink('Slider', 'More Slider Examples and Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('RangeSlider')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccRangeSlider(
  count = 1,
  min = -5,
  max = 10,
  step = 0.5,
  value = list(-3, 7)
  )
  '
),

utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccRangeSlider(
  marks = lapply(-5:7, function(x){paste("Label", x)}),
  min = -5,
  max = 6,
  value = list(-3,4)
  )
  '
)
)),
htmlBr(),
htmlDiv(referenceLink('RangeSlider', 'More RangeSlider Examples and Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('Input')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccInput(
  placeholder = "Enter a value...",
  type = "text",
  value = ""
  )
  '
))),

htmlBr(),
htmlDiv(referenceLink('Input', 'More Input Examples and Reference')),
htmlHr(),

#--------------------------------
htmlDiv(titleLink('Textarea')),

htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccTextarea(
  placeholder = "Enter a value...",
  value = "This is a TextArea component",
  style = list("width" = "100%")
  )
  '
))),
htmlBr(),
htmlDiv(referenceLink('Textarea', 'Textarea Reference')),
htmlHr(),

#--------------------------------
htmlDiv(titleLink('Checkboxes')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
dccChecklist(
  options=list(
  list("label" = "New York City", "value" = "NYC"),
  list("label" = "Montréal", "value" = "MTL"),
  list("label" = "San Francisco", "value" = "SF")
  ),
  values=list("MTL", "SF")
)
  '
),

utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
dccChecklist(
  options=list(
  list("label" = "New York City", "value" = "NYC"),
  list("label" = "Montréal", "value" = "MTL"),
  list("label" = "San Francisco", "value" = "SF")
  ),
  values=list("MTL", "SF"),
  labelStyle = list("display" = "inline-block")
  )
  '
)
)),
htmlBr(),
htmlDiv(referenceLink('Checklist', 'Checklist Properties')),
htmlHr(),

#--------------------------------
htmlDiv(titleLink('Radioitems')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccRadioItems(
  options=list(
  list("label" = "New York City", "value" = "NYC"),
  list("label" = "Montréal", "value" = "MTL"),
  list("label" = "San Francisco", "value" = "SF")
  ),
  value = "MTL"
  )
  '
),

utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  dccRadioItems(
  options=list(
  list("label" = "New York City", "value" = "NYC"),
  list("label" = "Montréal", "value" = "MTL"),
  list("label" = "San Francisco", "value" = "SF")
  ),
  value = "MTL",
  labelStyle = list("display" = "inline-block")
  )
  '
)
)),
htmlBr(),
htmlDiv(referenceLink('Radioitems', 'RadioItems Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('Button')),
examples$button$source,
examples$button$layout,

htmlBr(),
htmlDiv(referenceLink('Button', 'More Button Examples and Reference')),

#--------------------------------

htmlDiv(titleLink('DatePickerSingle')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
dccDatePickerSingle(
    id="date-picker-single",
    date=as.Date("1997/5/10")
)
  
  '
))),

htmlBr(),
htmlDiv(referenceLink('datepickersingle', 'More DatePickerSingle Examples and Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('DatePickerRange')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
dccDatePickerRange(
  id = "date-picker-range",
  start_date = as.Date("1997/5/10"),
  end_date_placeholder_text="Select a date!"
)
  
  '
))),

#--------------------------------

htmlBr(),
htmlDiv(referenceLink('datepickerrange', 'More DatePickerRange Examples and Reference')),
htmlHr(),

htmlDiv(titleLink('Markdown')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
dccMarkdown("
Dash supports [Markdown](http://commonmark.org/help).
Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
")
  
  '
))),
htmlBr(),
htmlDiv(referenceLink('markdown', 'More Markdown Examples and Reference')),
htmlHr(),

#--------------------------------
htmlDiv(htmlH3('Interactive Tables')),


#--------------------------------
htmlDiv(titleLink('Upload Component')),
utils$LoadAndDisplayComponent(
  'library(dashR)
  library(dashCoreComponents)
dccMarkdown("
The `dccUpload` component allows users to upload files into your app
through drag-and-drop or the system\'s native file explorer.
![Dash Upload Component](https://user-images.githubusercontent.com/1280389/30351245-6b93ee62-97e8-11e7-8e85-0411e9d6c98c.gif)
")
'),

#--------------------------------

htmlDiv(htmlH3('Tabs')),
examples$tabs$source,
examples$tabs$layout,

htmlBr(),
htmlDiv(referenceLink('tabs', 'More Tabs Examples and Reference')),
htmlHr(),

#--------------------------------
htmlDiv(titleLink('Graphs')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
library(plotly)

year = c(1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012)
  
  Rest_of_world = c(219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
  350, 430, 474, 526, 488, 537, 500, 439)
  
  china = c(16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
  299, 340, 403, 549, 499)
  
  data = data.frame(year, Rest_of_world, china)

  dccGraph(
    figure = plot_ly(data, x = ~year, y = ~Rest_of_world, type = "bar", 
      name = "Rest of World", marker = list(
      color = "rgb(55, 83, 109)")) %>%
  
      add_trace(y = ~china, name = "China", 
      marker = list(color = "rgb(26, 118, 255)")) %>%
  
    layout(yaxis = list(title = "Count"), barmode = "group",
      title="US Export of Plastic Scrap"),
  
  style = list("height" = 300),
  id = "my_graph"
  
  )
  '
  ))),
htmlBr(),
htmlDiv(referenceLink('graph', 'View the plotly.R docs')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('ConfirmDialog')),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  confirm = dccConfirmDialog(
  id = "confirm",
  message = "Danger danger! Are you sure you want to continue?"
  )
  
  '
))),

htmlBr(),
htmlDiv(referenceLink('ConfirmDialog', 'More ConfirmDialog Examples and Reference')),
htmlHr(),

#--------------------------------

dccMarkdown(
  " There is also a `dccConfirmDialogProvider`,
     it will automatically wrap a child component 
    to send a `dccConfirmDialog` when clicked.
  "
),

htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  confirm = dccConfirmDialogProvider(
  children = htmlButton("Click Me"),
  id = "danger-danger",
  message = "Danger danger! Are you sure you want to continue?"
  )
  
  '
))),

htmlBr(),
htmlDiv(referenceLink('confirmdialogprovider', 'More ConfirmDialogProvider Examples and Reference
')),
htmlHr(),

#--------------------------------
htmlDiv(titleLink('ConfirmDialog')),
dccMarkdown(
  " The store component can be used to keep data in the visitor's browser.
    The data is scoped to the user accessing the page.
  **Three types of storage (`storage_type` prop):**
  - `memory`: default, keep the data as long the page is not refreshed.
  - `local`: keep the data until it is manually cleared.
  - `session`: keep the data until the browser/tab closes.
  _For `local`/`session`, the data is serialized as json when stored._
  "
),

htmlDiv(list(utils$LoadAndDisplayComponent(
  '
  library(dashCoreComponents)
  store = dccStore(id = "my-store", data = list("my-data" = "data"))
  '
))),
dccMarkdown('_The store must be used with callbacks_'),
htmlDiv(referenceLink('store', 'More Store Examples and Reference')),

#--------------------------------

htmlDiv(titleLink('Logout Button')),

dccMarkdown(
  " The logout button can be used to perform logout mechanism.
    It's a simple form with a submit button, when the button is clicked,
    it will submit the form to the `logout_url` prop. Please note that no authentication is performed in Dash by default
    and you have to implement the authentication yourself.
  "
),
htmlBr(),
htmlDiv(referenceLink('logout', 'More Logout Button Examples and Reference')),
htmlHr(),
#--------------------------------
htmlDiv(titleLink('Loading component')),

dccMarkdown(
  " The Loading component can be used to wrap components that you want to display a spinner for, if they take too long to load.
    It does this by checking if any of the Loading components' children have a `loading_state` prop set where `is_loading` is true.
    If true, it will display one of the built-in CSS spinners.
  "
),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
library(dashCoreComponents)
loading = dccLoading(list(list(
    # ...
)))
  
  '
  ))),

htmlBr(),
htmlDiv(referenceLink('loadingcomponenet', 'More Loading Component Examples and Reference')),
htmlHr(),

#--------------------------------

htmlDiv(titleLink('Location')),
dccMarkdown(
  " The location component represents the location bar in your web browser. Through its `href`, `pathname`,
    `search` and `hash` properties you can access different portions of your app's url.
  
  For example, given the url `http://127.0.0.1:8050/page-2?a=test#quiz`:

  - `href` = `http://127.0.0.1:8050/page-2?a=test#quiz\`
  - `pathname` = `/page-2`
  - `search` = `?a=test`
  - `hash` = `#quiz`

  "
),
htmlDiv(list(utils$LoadAndDisplayComponent(
  '
#library(dashCoreComponents)
#location = dccLocation(id= "url", refresh= FALSE)
  '
))),

htmlBr(),
htmlDiv(referenceLink('location', 'More Location Examples and Reference')),
htmlBr()

)

)

route <- function(pathname) {
  componentName = gsub('dropdown', '', pathname)
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
