library(dash)
library(dashHtmlComponents)
library(dashCoreComponents)
library(dashTable)

app <- Dash$new()

params <- c('Weight', 'Torque', 'Width', 'Height',
            'Efficiency', 'Power', 'Displacement')

app$layout(
  htmlDiv(
    list(
      dashDataTable(
        id = 'table-editing-simple',
        columns = c(
          list(
            list(
              id = 'Model',
              name = 'Model'
            )
          ),
          lapply(params,
                 function(colName){
                   list(
                     id = colName,
                     name = colName
                   )
                 })
        ),
        data = lapply(1:4,
                      function(i) {
                        setNames(
                          as.list(
                            c(
                              i, rep(0, length(params))
                            )
                          ),
                          c('Model', params)
                        )
                      }

        ),
        editable = TRUE
      ),
      dccGraph(id = 'table-editing-simple-output')
    )
  )
)

app$callback(
  output = list(id = 'table-editing-simple-output', property = 'figure'),
  params = list(input(id = 'table-editing-simple', property = 'data'),
                input(id = 'table-editing-simple', property = 'columns')),
  function(rows, columns) {

    df <- do.call(rbind, rows)
    #browser()
    list(
      data = list(
        list(
          type = 'parcoords',
          # dimensions = lapply(columns,
          #                     function(column) {
          #                       list(
          #                         range = ifelse(column[["name"]] == "Model", c(1,4), c(-1,1)),
          #                         label = column[['name']],
          #                         values = unlist(df[, column[['id']]])
          #                       )
          #                     })

          dimensions = list(
            list(range = c(1,4),
                 constraintrange = c(1,2),
                 label = 'Model', values = c(1,2,3,4)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Weight', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Torque', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Width', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Height', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Efficiency', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Power', values = c(0,0,0,0)),
            list(range = c(-1,1),
                 tickvals = c(1.5,3,4.5),
                 label = 'Displacement', values = c(0,0,0,0))
          )


        )
      )
    )
  }
)

#app$run_server(port = 8054)

