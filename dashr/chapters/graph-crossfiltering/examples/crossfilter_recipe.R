library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

set.seed(0)
df <- data.frame(replicate(1,sample(0:6,30,rep=TRUE))) 
df <- data.frame()
for (i in 1:6){
  val <- i*10
  print(val)
  df <- data.frame(replicate(1,sample((val-1):6,30,rep=TRUE))) 
}
  # pd.DataFrame({
  # 'Column {}'.format(i): np.random.rand(30) + i*10
  # for i in range(6)})

app$layout_set(htmlDiv(list(
  htmlDiv(
    dccGraph(
      id='g1',
      config=list(displayModeBar = FALSE)
    ), className='four columns'
  ),
  htmlDiv(
    dccGraph(
      id='g2',
      config=list(displayModeBar = FALSE)
    ), className='four columns'),
  htmlDiv(
    dccGraph(
      id='g3',
      config=list(displayModeBar = FALSE)
    ), className='four columns')
  ), className='row')
)

highlight <- function(x, y){
  callback <- function(selectedDatas){
    selectedpoints = df.index
    for i, selected_data in enumerate(selectedDatas):
      if selected_data is not None:
      selected_index = [
        p['customdata'] for p in selected_data['points']
        ]
    if len(selected_index) > 0:
      selectedpoints = np.intersect1d(
        selectedpoints, selected_index)
    
    
    # set which points are selected with the `selectedpoints` property
    # and style those points with the `selected` and `unselected`
    # attribute. see
    # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43e21
    # for an explanation
    
    figure = {
      'data': [
        {
          'x': df[x],
          'y': df[y],
          'text': df.index,
          'textposition': 'top',
          'selectedpoints': selectedpoints,
          'customdata': df.index,
          'type': 'scatter',
          'mode': 'markers+text',
          'marker': {
            'color': 'rgba(0, 116, 217, 0.7)',
            'size': 12,
            'line': {
              'color': 'rgb(0, 116, 217)',
              'width': 0.5
            }
          },
          'textfont': {
            'color': 'rgba(30, 30, 30, 1)'
          },
          'unselected': {
            'marker': {
              'opacity': 0.3,
            },
            'textfont': {
              # make text transparent when not selected
              'color': 'rgba(0, 0, 0, 0)'
            }
          }
        },
        ],
      'layout': {
        'clickmode': 'event+select',
        'margin': {'l': 15, 'r': 0, 'b': 15, 't': 5},
        'dragmode': 'select',
        'hovermode': 'closest',
        'showlegend': False
      }
    }
    
    # Display a rectangle to highlight the previously selected region
    shape = {
      'type': 'rect',
      'line': {
        'width': 1,
        'dash': 'dot',
        'color': 'darkgrey'
      }
    }
    if selectedDatas[0] and selectedDatas[0]['range']:
      figure['layout']['shapes'] = [dict({
        'x0': selectedDatas[0]['range']['x'][0],
        'x1': selectedDatas[0]['range']['x'][1],
        'y0': selectedDatas[0]['range']['y'][0],
        'y1': selectedDatas[0]['range']['y'][1]
      }, **shape)]
    else:
      figure['layout']['shapes'] = [dict({
        'type': 'rect',
        'x0': np.min(df[x]),
        'x1': np.max(df[x]),
        'y0': np.min(df[y]),
        'y1': np.max(df[y])
      }, **shape)]
    
    return(figure)
  }
  return(callback)
}


# app.callback is a decorator which means that it takes a function
# as its argument.
# highlight is a function "generator": it's a function that returns function
app$callback(
  output = list(id='g1', property='figure'),
  params = list(input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 0', 'Column 1'))

app$callback(
  output = list(id='g2', property='figure'),
  params = list(input(id='g2', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 2', 'Column 3'))

app$callback(
  output = list(id='g3', property='figure'),
  params = list(input(id='g3', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'))
)(highlight('Column 4', 'Column 5'))


# app$run_heroku()
