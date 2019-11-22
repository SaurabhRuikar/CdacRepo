biopsy <- read.csv("F:/Statistics/Cases/Wisconsin/BreastCancer.csv")

library(caret)

set.seed(1992)
intrain<-createDataPartition(y=biopsy$Class,p=0.7,list=FALSE)

training <- biopsy[intrain, -1]
validation <- biopsy[-intrain, -1]

library(e1071)
fit.svm <- svm(Class~., type="C",data=training, 
               kernel="linear")

fit.svm <- svm(Class~., type="C",data=training, 
               kernel="polynomial")
fit.svm <- svm(Class~., type="C",data=training, 
               kernel="radial")


svm.pred <- predict(fit.svm, newdata=validation)
svm.perf <- table(svm.pred, validation$Class, 
                  dnn=c("Predicted","Actual"))
confusionMatrix(svm.perf, positive = "Malignant") 


