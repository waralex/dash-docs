library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

set.seed(0)
df <- data.frame(replicate(10,sample(0:30,6,rep=TRUE))) 
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



# app$run_heroku()
