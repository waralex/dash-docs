library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(rjson)
library(jsonlite)
library(readr)
library(heatmaply)


utils <- new.env()
source('assets/styles.R')
source('assets/utils.R', local=utils)


# Necessary Functions:

titleLink <- function(componentName) {
  return(htmlH2(
    dccLink(
      componentName,
      href=paste('/', componentName, sep='')
    )
  ))
}

referenceLink <- function(componentName) {
  return(dccLink(
    'More examples & reference',
    href=paste('/', componentName, sep='')
  ))
}



# app <- Dash$new()


# Header and Introduction

header <- htmlDiv(list(
  htmlDiv(list(
    htmlDiv(list(
      htmlA(className = "logo-link", href = "https://plot.ly/products/dash",
            children= htmlImg(src="assets/logo.png",
                              style = list("height" = "60px", "width" = "230px"))),
      htmlDiv(className = "links", children = list(
        htmlA(className = "link", children = "pricing", href = "https://plot.ly/dash/pricing?_ga=2.241429382.584183071.1559580389-2135338473.1556993734"),
        htmlA(className = 'link', children = 'user guide', href = "/"),
        htmlA(className = 'link', children = 'plotly', href = "https://plot.ly/"),
        htmlA(className = 'link', href="https://dash.plot.ly/search", children = 
          htmlI(className = 'fa fa-search'))
        
      ))
    ))
  ), className = 'container-width')
), className = "header")


dashbio_intro <- htmlDiv(list(
  dccMarkdown('# Dash Bio'),

  
  dccMarkdown('
  Dash is a web application framework that provides pure Python abstraction
  around HTML, CSS, and JavaScript.
  
  Dash Bio is a suite of bioinformatics components that make it simpler to
  analyze and visualize bioinformatics data and interact with them in a Dash
  application.
  
  The source can be found on GitHub at [plotly/dash-bio](https://github.com/plotly/dash-bio).
  These docs are using Dash Bio version 1.0.0.
  
  To install, run the following commands below in your R console:
  '),
  
  dccMarkdown('
```r
>remotes::install_github("plotly/dash-bio")
>library(dashBio)
```              
              ')
))


# Individual Components and Examples


alignmentChart <- htmlDiv(list(
  htmlDiv(titleLink('AlignmentChart')),
  htmlP('An alignment chart that intuitively graphs complex, genome-scale, sequence alignments.'),
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
  ),
  htmlDiv(referenceLink('alignmentchart'))
))

circos <- htmlDiv(list(
  htmlDiv(titleLink('Circos')),
  htmlP('A circular ideogram with arcs representing links between genes.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(readr)
library(jsonlite)
    
data <- "assets/sample_data/circos_graph_data.json"

circos_graph_data = read_json(data)
     
dashbioCircos(
id = "my-dashbio-circos",
layout = circos_graph_data[["GRCh37"]],
tracks = list(list(
  "type" = "CHORDS",
  "data" = circos_graph_data[["chords"]],
  "opacity" = 0.7,
  "color" = list("name" = "color"),
  "config" = list(
      "tooltipContent" = list(
        "source" = "source",
        "sourceID" = "id",
        "target" = "target",
        "targetID" = "id",
        "targetEnd" = "end"
      )
    )
))

)
    '
  ),
  htmlDiv(referenceLink('Circos'))
))




clustergram <- htmlDiv(list(
  htmlDiv(titleLink('Clustergram')),
  htmlP('A heatmap with dendrograms to display clustering of data such as gene expression data.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(dashCoreComponents)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                  skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                  

dccGraph(figure = heatmaply(df, 
        row_labels = list(row.names(data)),
        hide_labels = list("row"),
        column_labels = as.list(colnames(data)),
        color_threshold = list(
            "row" = 150,
            "col" = 700
          )
       )
    )
    '
  ),
  htmlDiv(referenceLink('Clustergram'))
))


ideogram <- htmlDiv(list(
  htmlDiv(titleLink('Ideogram')),
  htmlP('A visual representation and analysis tool for chromosome bands.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
    
dashbioIdeogram(
id = "my-dashbio-ideogram",
chrHeight = 300
)
    '
  ),
  htmlDiv(referenceLink('Ideogram'))
))


manhattanPlot <- htmlDiv(list(
  htmlDiv(titleLink('ManhattanPlot')),
  htmlP('A plot that can be used to display the results of genomic studies sorted out by chromosome. 
        Perfect for Genome Wide Association Studies (GWAS)'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
    

data = read.table("assets/sample_data/manhattan_data.csv",
                     header = TRUE, sep = ",")


dccGraph(figure = dashbioManhattan(
    dataframe=data
))
                     
    '
  ),
  htmlDiv(referenceLink('ManhattanPlot'))
))


molecule2dviewer <- htmlDiv(list(
  htmlDiv(titleLink('Molecule2dViewer')),
  htmlP('A 2D rendering of molecular structures.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(jsonlite)

     
model_data = read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol2d_buckminsterfullerene.json")


dashbioMolecule2dViewer(
id = "my-dashbio-molecule2dviewer",
modelData = model_data
)
    '
  ),
  htmlDiv(referenceLink('Molecule2dViewer'))
))




molecule3dviewer <- htmlDiv(list(
  htmlDiv(titleLink('Molecule3dViewer')),
  htmlP('A 3D visualization of biomolecular structures.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(jsonlite)

model_data <- read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js")
styles_data <- read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js")

dashbioMolecule3dViewer(
    id = "my-dashbio-molecule3dviewer",
    styles = styles_data,
    modelData = model_data,
    selectionType = "Chain"
  )
    '
  ),
  htmlDiv(referenceLink('Molecule3dViewer'))
))



needleplot <- htmlDiv(list(
  htmlDiv(titleLink('NeedlePlot')),
  htmlP('A combination of a bar chart and a scatter plot, for data that are both categorical and continuous.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(jsonlite)
    
mdata = read_json("assets/sample_data/needle_PIK3CA.json")

dashbioNeedlePlot(
id = "my-dashbio-needleplot",
mutationData = mdata
)
    '
  ),
  htmlDiv(referenceLink('NeedlePlot'))
))


oncoprint <- htmlDiv(list(
  htmlDiv(titleLink('OncoPrint')),
  htmlP('A chart that can be used to visualize multiple genomic alternations with an interactive heatmap.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(jsonlite)
    
data = read_json("assets/sample_data/oncoprint_dataset3.json")

dashbioOncoPrint(
id = "my-dashbio-oncoprint",
data = data
)
    '
  ),
  htmlDiv(referenceLink('OncoPrint'))
))


sequenceviewer <- htmlDiv(list(
  htmlDiv(titleLink('SequenceViewer')),
  htmlP('A sequence viewer that can highlight and display strings of amino acids sequences.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
    
sequence ="MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFY
TPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"


dashbioSequenceViewer(
id = "my-dashbio-sequenceviewer",
sequence = sequence
)
    '
  ),
  htmlDiv(referenceLink('SequenceViewer'))
))



speck <- htmlDiv(list(
  htmlDiv(titleLink('Speck')),
  htmlP('A 3D WebGL molecule viewer.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(jsonlite)
    
data = read.table("assets/sample_data/speck_methane.xyz", skip = 2)


dashbioSpeck(
id = "my-dashbio-speck",
view = list("resolution" = 600),
data = data
)
    '
  ),
  htmlDiv(referenceLink('Speck'))
))



volcanoplot <- htmlDiv(list(
  htmlDiv(titleLink('VolcanoPlot')),
  htmlP("A graph that can be used to identify clinically meaningful markers in genomic experiments."),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(dashCoreComponents)
    
data = read.table("assets/sample_data/volcano_data1.csv",
                     header = TRUE, sep = ",")


dccGraph(figure = dashbioVolcano(
    id = "my-dashbio-volcanoplot",
    dataframe = data
  )
)
    '
  ),
  htmlDiv(referenceLink('VolcanoPlot'))
))



# Main docs layout

mainLayout <- htmlDiv(list(
  dashbio_intro,
  htmlHr(),
  alignmentChart,
  htmlHr(),
  circos,
  htmlHr(),
  clustergram,
  htmlHr(),
  ideogram,
  htmlHr(),
  manhattanPlot,
  htmlHr(),
  molecule2dviewer,
  htmlHr(),
  molecule3dviewer,
  htmlHr(),
  needleplot,
  htmlHr(),
  oncoprint,
  htmlHr(),
  sequenceviewer,
  htmlHr(),
  speck,
  htmlHr(),
  volcanoplot
))


# app$run_server(showcase = TRUE)

