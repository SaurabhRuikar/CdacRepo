library(shiny)

data("mtcars")
pageWithSidebar(
  headerPanel = headerPanel("Histogram"),

  sidebarPanel = sidebarPanel(

    selectInput(inputId = "VarName",
                label = "Select Numeric Variable:",
                choices = list("mpg",
                                   "disp", "hp",
                                   "drat", "wt","qsec","carb"))
  ) ,
  mainPanel = mainPanel(
    plotOutput(outputId = "histogram")
  )
)