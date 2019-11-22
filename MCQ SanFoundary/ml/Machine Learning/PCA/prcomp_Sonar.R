library(mlbench)
data("Sonar")

library(caret)
set.seed(1992)
intrain<-createDataPartition(y=Sonar$Class,p=0.7,list=FALSE)
training <- Sonar[intrain,]
validation <- Sonar[-intrain,]


library(MASS)

model.lda <- lda(Class ~ . , data = training)

pred.lda <- predict(model.lda, newdata = validation)
confusionMatrix(pred.lda$class,validation$Class)


prc <- prcomp(Sonar[,-61])
names(prc)
pr.var <- prc$sdev^2
pve <- pr.var / sum(pr.var)

# Plot variance explained for each principal component
plot(pve, xlab = "Principal Component",
     ylab = "Proportion of Variance Explained",
     ylim = c(0, 1), type = "b")

# Plot cumulative proportion of variance explained
plot(cumsum(pve), xlab = "Principal Component",
     ylab = "Cummulative Proportion of Variance Explained",
     ylim = c(0, 1), type = "b")

data.frame(pve,cumsum(pve)*100)

trainingPCA <- cbind.data.frame(prc$x[intrain,1:6],Class=training$Class)
model.lda.PCA <- lda(Class ~ . , data = trainingPCA)

valid.PCA <- as.data.frame(prc$x[-intrain,1:6])
pred.lda.PCA <- predict(model.lda.PCA, newdata = valid.PCA)
confusionMatrix(pred.lda.PCA$class,validation$Class)


#############################################################################
###### Applying Seperately
#############################################################################



prc <- prcomp(training[,-61])
names(prc)

trainingPCA <- cbind.data.frame(prc$x[,1:6],Class=training$Class)
model.lda.PCA <- lda(Class ~ . , data = trainingPCA)

validation.PCA <- as.data.frame(predict(prc, newdata = validation))

pred.lda.PCA <- predict(model.lda.PCA, newdata = validation.PCA)
confusionMatrix(pred.lda.PCA$class,validation$Class)
