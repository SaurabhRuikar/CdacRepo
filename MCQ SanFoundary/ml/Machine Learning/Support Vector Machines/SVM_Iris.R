library(e1071)
data("iris")

library(caret)
set.seed(1992)
intrain<-createDataPartition(y=iris$Species , p=0.7,list=FALSE)

training   <- iris[ intrain , ]
validation <- iris[-intrain , ]

model.svm <- svm(Species ~ ., data = training, probability=T)

pred.svm <- predict(model.svm, newdata = validation)

tbl <- table(pred.svm, validation$Species)
confusionMatrix(tbl)

plot(model.svm,iris,Petal.Width ~ Petal.Length,
     slice = list(Sepal.Width = 3, Sepal.Length = 4))
