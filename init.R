# R script to run author supplied code, typically used to install additional R packages
# contains placeholders which are inserted by the compile script
# NOTE: this script is executed in the chroot context; check paths!

r <- getOption("repos")
r["CRAN"] <- "http://cloud.r-project.org"
options(repos=r)

# ======================================================================

# packages go here
install.packages("remotes")

# installs Rcpp, rlang, BH
install.packages("later")

install.packages("jsonlite")
install.packages("rjson")
install.packages("listenv")
install.packages("anytime")
install.packages("readr")
install.packages("heatmaply")
install.packages("bezier")
install.packages("magick")

remotes::install_github("plotly/dashR", upgrade=TRUE, ref="dev")
install.packages("manhattanly")
remotes::install_github("plotly/dash-cytoscape")
remotes::install_github("plotly/dash-bio")
remotes::install_github("plotly/dash-daq")
