setwd("/home/student/Desktop/Statistics with R/Datasets")

a <- read.csv("Orders.csv")
a
b <- subset(a,Payment.Terms=="Online")
b



cars <- mtcars
cars

write.csv(mtcars,"mtcars1.csv")
write.csv(mtcars,"/home/student/Desktop/mtcars.csv")

d <- read.csv2("Diamonds.csv")
d
c <- subset(d,cut=="Premium" & color=="J")
c

df <- data.frame(d$carat,d$color,d$depth,d$price)
df


r <- cars[c(2,18,30,12),]
r



