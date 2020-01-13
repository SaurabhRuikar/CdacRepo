install.packages("dplyr")
library(dplyr)



setwd("/home/student/Desktop/R/Statistics with R/Datasets")

a <- read.csv("survey.csv")
a



b <- filter(a,Sex=="Male" & Smoke=="Never")
b

c <- a%>% select(Sex,Exer,Smoke,Pulse) %>% filter(Pulse>80)
c

d <- a %>%  mutate(Ratio_Hnd=Wr.Hnd/NW.Hnd) %>% select(Ratio_Hnd,Clap,Age)
d


p <- summarize(a, Mean = mean(Age,na.rm = TRUE),
          SD = sd(Age,na.rm = TRUE))
p

q <- group_by(a,Sex)
r <- summarize(q, Mean = mean(Age,na.rm = TRUE),
               SD = sd(Age,na.rm = TRUE))
r



x <- read.csv("Orders.csv")
x
y <- read.csv("Items.csv")
y
z <- read.csv("Ord_Details.csv")
z

xx <- full_join(x,z,by="Order.ID")
xx

xy <- full_join(xx,y,by="Item.ID")
xy

p <- read.csv("Courses.csv")
p
q <- read.csv("CourseSchedule.csv")
q


r <- full_join(p,q,by=c("CourseID"="CourseCode"))
r

s <- inner_join(p,q,by=c("CourseID"="CourseCode"))
s


install.packages("tidyr")
library(tidyr)

m <- read.csv("comb1.csv")
m

n <- m %>% gather("Highlighter","Marker","Pen","Refill",key="Itemtype",value="qty")
n


o <- read.csv("comb2.csv")
o

p <- o %>% separate(PatientID,into=c("ProjectID","SiteID","PatientNumber"))
p






