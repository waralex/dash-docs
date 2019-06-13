
test =utils$props_to_list('dccTextarea')
df <- data.frame(matrix(unlist(test), nrow=length(test), byrow=T))
names(df) = c('Attribute', 'Description')

app = Dash$new()

layout = app$layout(
  dccGraph(
    figure = plot_ly(
      type = 'table',
      header = list(
        values = c("<b>Attribute</b>", names(df)[2]),
        align = c('left', rep('center', ncol(df))),
        line = list(width = 1, color = 'white'),
        fill = list(color = 'white'),
        font = list(family = "Arial", size = 14, color = "#264e86")
      ),
      cells = list(
        values = rbind(
          rownames(df), 
          t(as.matrix(unname(df)))
        )[c(2,3),],
        align = c('left', rep('left', ncol(df))),
        line = list(color = "white", width = 1),
        fill = list(color = c('white', 'white')),
        font = list(family = "Arial", size = 14, color = c("black"))
      ))))

app$run_server()