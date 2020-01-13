library(shiny)

data("mtcars")
function(input,output) {

  output$histogram <- renderPlot({

    hist(mtcars[,input$VarName],
         main = paste("Histogram of", input$VarName),
         col="pink")
  })
}