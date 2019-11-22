library(shiny)


data(milk, package="flexclust")

distance <- reactive({
  milk.scaled <- scale(milk)                                  
  d <- dist(milk.scaled) 
  return(d)
})

function(input,output) {
  
  output$dendroComp <- renderPlot({
    d <- distance()                                     
    fit.complete <- hclust(d, method="complete")  
    plot(fit.complete, main="Complete Linkage Clustering")
    rect.hclust(fit.complete, k= input$num)
  })
  
  output$dendroSing <- renderPlot({
    d <- distance()                                           
    fit.single <- hclust(d, method="single")  
    plot(fit.single, main="Single Linkage Clustering")
    rect.hclust(fit.single, k= input$num)
  })
  
  output$dendroAvg <- renderPlot({
    d <- distance()                                           
    fit.average <- hclust(d, method="average")  
    plot(fit.average, main="Average Linkage Clustering")
    rect.hclust(fit.average, k= input$num)
  })
  
 
}