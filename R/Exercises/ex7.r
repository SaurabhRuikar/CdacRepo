setwd("/home/student/Desktop/R1/Statistics with R/Datasets")

a <- read.csv("AutoCollision.csv")
a
install.packages("ggplot2")
library(ggplot2)
qplot(Severity,Claim_Count,data = a,main = "Severity by claim count",color=Vehicle_Use)+  
theme(plot.title = element_text(hjust = 0.5))



ggplot(data=a,aes(x=Vehicle_Use,y=Claim_Count,fill=Vehicle_Use))+geom_boxplot()+
  labs(title="Claim Count by vehicle type")+
  labs(x="ClaimCount",y="VehicleType")+
  theme(plot.title = element_text(hjust = 0.5))


b <- read.csv("Ornstein.csv")
b

ggplot(b,aes(nation,fill=sector))+geom_bar()

  


ggplot(data = b,aes(x=assets,y=interlocks,color=sector))+geom_point()+facet_grid(.~nation)


data(mtcars)
c <- mtcars

ggplot(data = c,aes(x=disp,y=mpg,color=as.factor(gear)))+geom_point()+
  labs(title="Displacement by mpg")+
  labs(x="Displacement",y="Miles per Gallon")+
  theme(plot.title = element_text(hjust = 0.5))
  


 