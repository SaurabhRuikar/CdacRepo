library(shiny)


data(milk, package="flexclust")

pageWithSidebar(
  headerPanel = headerPanel("Heirarchical Clustering"),
  
  sidebarPanel = sidebarPanel(
   
    
    numericInput(inputId = "num", label = "How many Clusters do you want?", 
                 value = 3, step = 1, min = 1, max = nrow(milk))
    
    #submitButton("View Outputs")
  ) ,
  mainPanel = mainPanel(
    
    tabsetPanel(
      tabPanel("Average Linkage", plotOutput("dendroAvg")),
      tabPanel("Complete Linkage", plotOutput("dendroComp")),
      tabPanel("Single Linkage", plotOutput("dendroSing"))
    )
    
  )
)
