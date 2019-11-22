library(mlbench)
data("Glass")

library(caret)
set.seed(1992)
intrain<-createDataPartition(y=Glass$Type,p=0.7,list=FALSE)
training <- Glass[intrain,]
validation <- Glass[-intrain,]


library(MASS)
trainingX <- scale(training[,-10])
training <- cbind.data.frame(trainingX, Type = training$Type)
model.lda <- lda(Type ~ . , data = training)

validationX <- scale(validation[,-10])
validation <- cbind.data.frame(validationX, Type = validation$Type)

pred.lda <- predict(model.lda, newdata = validation)
confusionMatrix(pred.lda$class,validation$Type)


prc <- prcomp(training[,-10])
names(prc)

trainingPCA <- cbind.data.frame(prc$x,Type=training$Type)
model.lda.PCA <- lda(Type ~ . , data = trainingPCA)

validation.PCA <- as.data.frame(predict(prc, newdata = validation[,-10]))

pred.lda.PCA <- predict(model.lda.PCA, newdata = validation.PCA)
confusionMatrix(pred.lda.PCA$class,validation$Type)
