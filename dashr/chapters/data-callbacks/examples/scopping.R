# library(dashR)
# library(dashCoreComponents)
# library(dashHtmlComponents)
# 
# app <- Dash$new()
# 
# df <- data.frame(
#   a = c(1,2,3),
#   b = c(4,1,4),
#   c = c('x', 'y', 'z'),
#   stringsAsFactors=FALSE
# )
# 
# app$layout(
#   htmlDiv(
#     list(
#       dccDropdown(
#         id = 'dropdown',
#         options = list(
#           list(label = 'x', value = 'x'),
#           list(label = 'y', value = 'y'),
#           list(label = 'z', value = 'z')
#         ),
#         value = 'x'
#       ),
#       htmlDiv(id='output')
#     )
#   )
# )
# 
# 
# app$callback(output('output', 'children'),
#              list(input('dropdown', 'value')),
#              function(val) {
#                # Here, `df` is an example of a variable that is
#                # 'outside the scope of this function'.
#                # *It is not safe to modify or reassign this variable
#                #  inside this callback.*
#                filtered_df <- lapply(df, `[[`, which(df$c == val)) # do not do this, this is not safe!
#                sprintf(paste(c('the output is', unlist(filtered_df))))
#              })
# 
# app$run_server()
