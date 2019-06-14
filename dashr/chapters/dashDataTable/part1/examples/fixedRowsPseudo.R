dashDataTable(
  n_fixed_rows = 1,
  style_cell = list(
    width = '150px'
  ),
  columns = lapply(colnames(df_long), 
                   function(colName){
                     list(
                       id = colName,
                       name = colName
                     )
                   }),
  data = df_to_list(df_long)
)