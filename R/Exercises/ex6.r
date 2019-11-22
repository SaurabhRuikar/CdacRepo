setwd("/home/student/Desktop/R/Statistics with R/Datasets")
a <- read.csv("SingaporeAuto.csv")
a

k <- boxplot(a$Exp_weights,col = "pink")
k

z <- boxplot(a$Exp_weights~a$VehicleType,col=c(6,3,23,34,45,67,89,100,123,124))
z


b <- read.csv("cars2.csv")
b


plot(b$speed,b$dist,xlab = "Speed",ylab = "Distance",pch =17,col="hotpink")


pdf("/home/student/Desktop/R/Statistics with R/Datasets/Graphs.pdf")

par(mfrow=c(2,2))
boxplot(a$Exp_weights,col = "pink")
boxplot(a$Exp_weights~a$VehicleType,col=c(6,3,23,34,45,67,89,100,123,124))
plot(b$speed,b$dist,xlab = "Speed",ylab = "Distance",pch =17,col="hotpink")
dev.off()
