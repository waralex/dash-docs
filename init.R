# init.R
#

install.packages(c("devtools", "fiery", "routr", "base64enc"), build = FALSE)
# #install.packages("/app/localpkgs/dashHtmlComponents_0.13.5.tar.gz", repos=NULL, type="source")
# #install.packages("/app/localpkgs/dashCoreComponents_0.43.0.tar.gz", repos=NULL, type="source")
# #install.packages("/app/localpkgs/dashR_0.0.2.tar.gz", repos=NULL, type="source")
remotes::install_github("plotly/dashR", build = FALSE)
remotes::install_github("plotly/dash-html-components", build = FALSE)
remotes::install_github("plotly/dash-core-components", build = FALSE)
