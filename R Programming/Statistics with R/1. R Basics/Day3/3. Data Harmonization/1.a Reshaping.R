setwd("F:\\R Course\\Datasets")

d <- c(12,23,14,45)
e <- c(34,24,90,13)
y <- data.frame(d,e)
tr <- t(y)
class(tr)

items <- read.csv("items.csv")

trnsp <- t(items)
class(trnsp)

library(reshape2)
quality <- read.csv("quality.csv")

melted1 <- melt(quality, id=c("Id"))

melted2 <- melt(quality, id=c("Id"),variable.name = "Policy",
                value.name = "Score")

quality2 <- read.csv("quality2.csv")

melted3 <- melt(quality2, id=c("Id","Group"),variable.name = "Policy",
                value.name = "Score")

quality3 <- read.csv("quality3.csv")

melted4 <- melt(quality3, id=c("Id","Group"), na.rm = TRUE)

