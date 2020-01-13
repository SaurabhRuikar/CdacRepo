setwd("F:\\R Course\\Datasets")

items <- read.csv("Items.csv")

str(items)

s <- seq(1,20,by=4)

for(i in s) {
  print(i)
}

table(items$Item.Type)
table(items$Brand)
table(items$Item.Type,items$Brand)

tbl <- table(items$Item.Type,items$Brand)

prop.table(table(items$Item.Type))

prop.table(tbl)

prop.table(tbl,1)
prop.table(tbl,1)*100


prop.table(tbl,2)
prop.table(tbl,2)*100
###############################################
library(MASS)
data("survey")

table(survey$Exer)
table(survey$Sex)

table(survey$Sex, useNA = "ifany")

table(survey$Sex,survey$Exer)
addmargins(table(survey$Sex,survey$Exer))

table(survey$Sex,survey$Exer,survey$Smoke)

table(survey$Sex,survey$Exer, useNA = "ifany")
table(survey$Sex,survey$Exer,survey$Smoke, useNA = "ifany")

prop.table(table(survey$Exer))

tbl <- table(survey$Sex,survey$Exer)
prop.table(tbl)
addmargins(prop.table(tbl))

prop.table(tbl,1)
addmargins(prop.table(tbl,1),margin = 2)
prop.table(tbl,1)*100

prop.table(tbl,2)
addmargins(prop.table(tbl,2),margin = 1)
prop.table(tbl,2)*100

survey$Age
cut(survey$Age,breaks = c(15,30,50,70,100))

cut(survey$Age,breaks = 4)
agegrp <- cut(survey$Age,breaks = 4)
class(survey$Age)
class(agegrp)
table(agegrp)

agegrp <- cut(survey$Age,breaks = c(16,25,30,40,50,80))
table(agegrp)

cut(items$Price,breaks=4)

cut(items$Price,breaks=c(40,50,65,80,100,300,400,500))

table(cut(items$Price,breaks=4))

set.seed(34512)
sample(1:50,size = 10)

set.seed(71)
sample(items$Price, size=8)

sample(items$Price, size=8,replace = TRUE)

sampInd <- sample(1:237,size = 20)
rndSamp <- survey[sampInd, ]

log(2)
log(2,10)
log1p(2) #log(1+x)
log10(2)
log2(2)

exp(0.6931472)
10^0.30103
expm1(1.098612) # exp(x) - 1
10^0.30103
2^1

exp(0.6931472)
expm1(0.6931472)
y <- c(100,23,4,200,3,89,2,34,2,95,34,93,56)
x <- 1:13
plot(x,y,type = "l",ylim = c(0,200))
lny <- log(y)
plot(x,lny,type = "l",ylim = c(0,50))

items$Item.Type
Pen <- ifelse(items$Item.Type=="Pen",1,0)

mean(survey$Pulse)
mean(survey$Pulse, na.rm = T)
sum(survey$Pulse,na.rm = T)/237
sum(survey$Pulse,na.rm = T)/192
var(survey$Pulse, na.rm = T)

mean(items$Price,na.rm = TRUE)
sd(items$Price,na.rm = TRUE)
var(items$Price,na.rm = TRUE)

summary(items$Price)

summary(items$Item.Type)

summary(items)

table(items$Item.Type)
with(items,table(Item.Type))

mean(items$Price,na.rm = TRUE)
with(items,mean(Price,na.rm = TRUE))

with(items,{
  print(table(Item.Type))
  print(mean(Price,na.rm = TRUE))
  })

attach(items)
table(Item.Type)
mean(Price)
