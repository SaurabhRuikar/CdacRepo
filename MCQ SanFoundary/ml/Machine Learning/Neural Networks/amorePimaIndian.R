
library(mlbench)
data("PimaIndiansDiabetes")
PimaIndiansDiabetes[,9] <- ifelse(PimaIndiansDiabetes[,9] == "pos",1,0)
library(caret)
set.seed(1992)
intrain<-createDataPartition(y=PimaIndiansDiabetes$diabetes , 
                             p=0.7,list=FALSE)
training   <- PimaIndiansDiabetes[ intrain , ]
validation <- PimaIndiansDiabetes[-intrain , ]

library(AMORE)

pim <- scale(PimaIndiansDiabetes[,-9])
net <- newff(n.neurons = c(8,4,1), learning.rate.global = 0.01,
             momentum.global = 0.5, error.criterium = "LMS",
             hidden.layer = "sigmoid", output.layer = "purelin",
             method = "ADAPTgdwm")
fitnnet <- train(net, P=pim[intrain,] , 
                 T=PimaIndiansDiabetes[intrain ,9],
                 report = T, show.step = 100, n.shows = 5)
sim.net <- sim(net = fitnnet$net , P=pim[-intrain,])
pred.nnet <- ifelse(sim.net[,1] > 0 , 1,0)
confusionMatrix(pred.nnet, PimaIndiansDiabetes[-intrain, 9],
                positive = "1")
