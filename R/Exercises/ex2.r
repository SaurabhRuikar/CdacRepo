setwd("/home/student/Desktop/Statistics with R/Datasets")

c <- read.csv("Orders.csv")
c

str(c)

summary(c)


d <- read.csv("Bollywood_2015.csv")
d
e <- c(d$BO_Collection)
e
'
THIS IS A COMMENT 
'

f <- cut(e,breaks = 5)
f

a <- table(f)
a


k <- prop.table(a)*100
k

s <- addmargins(k)
s

t <- read.csv("Ord_Details.csv")
t


u <- sample(t$Qty,size= 80, replace = T)
u
v <- t[u,] 
v

load("events.Rdata")

events

#x <- length(events$eventID)



df1 <- data.frame(events,dur)
df1


events$dur[1]=events$occur[1]
for (i in 2:15)
{
  events$dur[i] = events$occur[i] - events$occur[i-1] 
}
events


far <- function(f)
{
  return ((f - 32)*(5/9))
}
far(90)



k <- c(20,30,50,60)

cal <- function(k) {
  m <- mean(k,na.rm = T)
  
  s <- sd(k,na.rm = T)
  
  l1 = m - 2*s
  
  l2 = m + 2*s
  
  df <- data.frame(l1,l2)
   df
}
cal(k)



cal2 <- function(k) {
  r <- mean(k,na.rm = T)
  s <- sd(k,na.rm = T)
  q <- (r/s)*100
  q
}

cal2(k)





g <- c(5,6,NA,4,3,NA,8,9)


cal3 <- function(g) {
  l <- mean(g,na.rm=T)
  l
  
  z <- ifelse(is.na(g)==TRUE,l,g)
  z
}
cal3(g)


  
  