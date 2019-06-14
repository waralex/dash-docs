dashDataTable(
  n_fixed_columns = 1,
  columns = lapply(colnames(df_election), 
                   function(colName){
                     list(
                       id = colName,
                       name = colName
                     )
                   }),
  data = df_to_list(df_election)
)