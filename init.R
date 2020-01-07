# R script to run author supplied code, typically used to install additional R packages
# contains placeholders which are inserted by the compile script
# NOTE: this script is executed in the chroot context; check paths!

r <- getOption("repos")
r["CRAN"] <- "http://cloud.r-project.org"
options(repos=r)

# ======================================================================
remotes::install_github("plotly/dashR", upgrade=TRUE)
install.packages("manhattanly")
remotes::install_github("plotly/dash-canvas", ref="93224c3")
remotes::install_github("plotly/dash-cytoscape", ref="25b0301")
remotes::install_github("plotly/dash-bio", ref="44f8f3a")
remotes::install_github("plotly/dash-daq", ref="7ad539")
