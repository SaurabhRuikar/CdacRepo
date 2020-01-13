setwd("/home/student/Desktop/R/Statistics with R/Datasets")

install.packages("mlbench")
library(mlbench)
data("Sonar")
df <- Sonar[,1:60]

cal2 <- function(k) {
  r <- mean(k,na.rm = T)
  s <- sd(k,na.rm = T)
  q <- (s/r)*100
  q
}
cal2(k)
apply(df,2,cal2)








ls <- list(a <- rbinom(50000,10000,0.023),b <- rpois(45000,230),d <- rnorm(40000,230,30),e <- rnorm(40000,230,40))
ls

cal3<- function(k) {
  r <- mean(k,na.rm = T)
  s <- sd(k,na.rm = T)
 a<- r-(3*s)
 b <- r+(3*s)
  df <- data.frame(a,b)
  df
}

 sapply(ls,cal3)

 cal4<- function(k) {
   r <- mean(k,na.rm = T)
   s <- sd(k,na.rm = T)
 
   df <- data.frame(r,s)
   df
 }
 
sapply(ls,cal4)
 
 
 
install.packages("carData")
library(carData)
data("Salaries")
Salaries
 
tapply(Salaries$salary,Salaries$rank,mean)
 
 
install.packages("Ecdat")

h1 <- Housing
hlist <-sapply(h1,is.numeric)
hlist2 <- sapply(h1,is.factor)
housingno=h1[,hlist]
housingfact=h1[,hlist2]
housingno
housingfact
