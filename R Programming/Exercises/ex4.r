setwd("/home/student/Desktop/R/Statistics with R/Datasets")
a <- read.csv("Orders.csv")
a
b <- read.csv("Items.csv")
b
c <- read.csv("Ord_Details.csv")
c

m <- merge(a,c,by="Order.ID")
m
n <- merge(b,m,by="Item.ID")
n

x <- read.csv("Courses.csv")
x
y <- read.csv("CourseSchedule.csv")
y

z <- merge(x,y,by.x="CourseID",by.y="CourseCode")
z

install.packages("reshape")
library(reshape)

l <- read.csv("JobSalary.csv")
l

o <- melt(l,id=c("S_No"))
o





dt <- as.Date(n$Order.Date.x,format="%d-%b-%y")
dt
n$date=format(dt,"%d")
n$month=format(dt,"%b")
n$year=format(dt,"%Y")
n

n$year1 <- dt+366
n