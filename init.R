# init.R
#

install.packages(c("devtools", "fiery", "routr", "base64enc"), build_opts = c("--no-resave-data", "--no-manual",
                                                                              "--no-build-vignettes"))
# #install.packages("/app/localpkgs/dashHtmlComponents_0.13.5.tar.gz", repos=NULL, type="source")
# #install.packages("/app/localpkgs/dashCoreComponents_0.43.0.tar.gz", repos=NULL, type="source")
# #install.packages("/app/localpkgs/dashR_0.0.2.tar.gz", repos=NULL, type="source")
remotes::install_github("plotly/dashR", build_opts = c("--no-resave-data", "--no-manual",
                                                       "--no-build-vignettes"))
remotes::install_github("plotly/dash-html-components", build_opts = c("--no-resave-data", "--no-manual",
                                                                      "--no-build-vignettes"))
remotes::install_github("plotly/dash-core-components", build_opts = c("--no-resave-data", "--no-manual",
                                                                      "--no-build-vignettes"))
