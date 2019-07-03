app <- Dash$new()

alignmentChart <- htmlDiv(list(
  htmlDiv(titleLink('AlignmentChart')),
  htmlP('An alignment chart that intuitively graphs complex, genome-scale, sequence alignments.'),
  
  htmlDiv(id = 'output-container', children = list()),
  daqToggleSwitch(
    id= 'img-live',
    value = FALSE,
    color = "#AB63FA",
    label = list('image', 'live')
  ),
  htmlDiv(referenceLink('alignmentchart'))
))


app$callback(
  output(id = 'output-container', property = 'children'),
  params = list(
    input(id = 'img-live', property = 'value')
  ),

  change_img <- function(value) {
    print(value)
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(readr)

data = read_file("assets/sample_data/alignment_viewer_p53.fasta")

dashbioAlignmentChart(
id = "my-dashbio-alignmentchart",
data = data
)
    '
        )
      )
      )
    }
    

    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/alignment.PNG")))
    }


  }
)

app$layout(htmlDiv(list(
  alignmentChart
)))

app$run_server(showcase = TRUE)