data("CO2")
CO2
t.test(CO2$uptake,mu=30,alternative = "l")                      

data("Indometh")
Indometh

t.test(Indometh$conc,mu=0.30,alternative = "g")


###Book 255-13
install.packages("readxl")
library("readxl")
df=read_excel("/home/student/Desktop/backup/R/Statistics with R/1. R Basics/Stats Book/Data_Files/Sales Data.xlsx",range = "A3:F63")
df

class(df)

t.test(df$`Gross Profit`,mu=4500,alternative = "l")




setwd("/home/student/Desktop/backup/R/Statistics with R/1. R Basics/R Options for Statistics/Exercises")

a <- read.csv("Rheumatic.csv")
a

t.test(a$Before,a$After,alternative = "l",paired = T)

--------------------------------------------------------------------------
  
  
  
df <- read.csv("Puromycin.csv")
df

ss <- subset(df,state=="treated")
ss1 <- subset(df,state=="untreated")

t.test(ss$conc,ss1$conc,var.equal = T)

t.test(ss$rate,ss1$rate,var.equal = T)


wilcox.test(ss$rate,ss1$rate)

##------------------------------------------------------------------------------
##ANOVA  

  
data("PlantGrowth")
avobj <- aov(PlantGrowth$weight ~ PlantGrowth$group)  
anova(avobj)

data("morley")
morley


morley$Expt <- as.factor(morley$Expt)
a <- aov(morley$Speed ~ morley$Expt)
anova(a)


morley$Run <- as.factor(morley$Run)
b <- aov(morley$Speed ~ morley$Run)
anova(b)

################################################################################
############    Correlation

data("mtcars")
mtcars
cor(mtcars$disp,mtcars$mpg)

flm <- lm(mpg~disp,data=mtcars)
flm

setwd("/home/student/Desktop/backup/R/Statistics with R/1. R Basics/R Options for Statistics/Regression Exercises")
y <- read.csv("Concrete_Data.csv")
y

fit <- lm(Strength~.,data =y)
fit
summary(fit)



z <- read.csv("housing.csv")
z

fit1 <- lm(median_house_value~.,data = z)
fit1
summary(fit1)






f <- read.csv("BreastCancer.csv")
f


fglm <- glm(Class~.-Code,data=f,family = binomial())
fglm


k <- read.csv2("bank-full.csv")
k

klm <- glm(y~.,data = k,family = binomial())
klm


################# Chi-Square Test
Like <- c(140,70,70,25)
dislike <- c(60,40,30,65)
rb <- rbind(Like,dislike)
chisq.test(rb)




Male   =c(12, 39, 27, 16)
Female =c(8 ,22 ,24 ,12)

rn <- rbind(Male,Female)
chisq.test(rn)


install.packages("AppliedPredictiveModeling")
library(AppliedPredictiveModeling)
data(FuelEconomy)

carall <- rbind.data.frame(cars2010,cars2011,cars2012)
carall

chisq.test(carall$DriveDesc,carall$CarlineClassDesc)

