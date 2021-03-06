library(carData)
data("Salaries")

library(ggplot2)
p <- ggplot(data=Salaries,aes(x=yrs.service,y=salary))
print(p)

p+geom_point()
p+geom_point()+geom_line()

ggplot(Salaries,aes(yrs.service,salary))+
  geom_point()

ggplot(Salaries,aes(yrs.service,salary,color=rank))+
  geom_point()

ggplot(Salaries,aes(yrs.service,salary,color=rank,
                    shape=discipline))+ geom_point()

p <- ggplot(Salaries,aes(yrs.service,salary))
p+geom_point()+geom_smooth()

p+geom_point()+geom_smooth(method="lm")

p+geom_point()+geom_smooth(method="lm",se=FALSE)

p+geom_point()+geom_smooth(method="lm",size=1,
                           linetype=2,se=FALSE)

p+geom_point()+geom_smooth(method="lm",size=1,
                           linetype=3,se=FALSE)

# Boxplot
ggplot(Salaries, aes(y=salary))+
  geom_boxplot()

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot()

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(fill=c("red","green","blue"))

ggplot(Salaries, aes(x=rank,y=salary,fill=rank))+
  geom_boxplot()

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(color=c("red","green","blue"))

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(fill=c("red","green","blue"))+
  geom_jitter()

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(fill=c("red","green","blue"))+
  geom_jitter(width = 0.2)

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(fill=c("red","green","blue"))+
  geom_jitter(width = 0.0)

ggplot(Salaries, aes(x=rank,y=salary))+
  geom_boxplot(fill=c("red","green","blue"))+
  geom_jitter(width = 0.4)

# Histogram
ggplot(Salaries,aes(x=salary)) + geom_histogram()

ggplot(Salaries,aes(x=salary)) +
  geom_histogram(bins=20,fill="pink",color="red")

ggplot(Salaries,aes(x=salary)) +
  geom_histogram(binwidth = 25000,
                 fill="lightskyblue2",color="blue")

# Density
ggplot(Salaries, aes(x=salary))+geom_density()

ggplot(Salaries, aes(x=salary,color=rank))+
  geom_density()

ggplot(Salaries, aes(x=salary,fill=rank))+
  geom_density()
ggplot(Salaries, aes(x=salary,fill=rank))+
  geom_density(alpha=0.6)

# Bar Chart
ggplot(Salaries, aes(rank))+
  geom_bar(fill="steelblue4")

ggplot(Salaries, aes(rank,fill=discipline))+
  geom_bar()

ggplot(Salaries, aes(rank,fill=discipline))+
  geom_bar(position = 'dodge')

ggplot(Salaries, aes(rank,fill=discipline))+
  coord_flip()+
  geom_bar()

### Plotting the Descriptive Statistics
library(dplyr)
meanSals <- Salaries %>%
  group_by(rank) %>%
  summarise(Mean=mean(salary,na.rm = T))

ggplot(data=meanSals,aes(x=rank,y=Mean))+
  geom_bar(stat = "identity",fill="steelblue2")

## Facet

p+geom_point()+geom_smooth(method="lm")+
  facet_grid(.~rank)

p+geom_point()+geom_smooth(method="lm")+
  facet_grid(rank~.)

p+geom_point()+geom_smooth(method="lm")+
  facet_grid(discipline~rank)

p+geom_point()+geom_smooth(method="lm")+
  facet_wrap(~rank,nrow = 2)

p+geom_point()+geom_smooth(method="lm")+
  facet_wrap(~rank,ncol = 2)

p+geom_point(color="blue", size=3, alpha=1/4)

ggplot(Salaries,aes(yrs.service,salary,size=yrs.since.phd))+
  geom_point(color="blue",  alpha=1/4)

p+geom_point(aes(color=rank), size=2, alpha=3/4)

p+geom_point(aes(color=rank), size=2, alpha=3/4)+
  labs(title="Plot by Rank")+
  labs(x="Years in Service",y="Salary",color='Rank')+
  theme(plot.title = element_text(hjust = 0.5))

p+geom_point(aes(color=rank), size=2, alpha=3/4)+
  labs(title="Plot by Rank")+
  labs(x="Years in Service",y="Salary")+
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))

## Saving the graph

ggplot(Salaries,aes(x=salary)) +
  geom_histogram(bins=20)+ggsave("Histo.pdf")

ggplot(Salaries,aes(x=salary)) +
  geom_histogram(bins=20)+ggsave("Histo.jpg")

## Themes
ggplot(Salaries,aes(yrs.service,salary,color=rank))+
  geom_point() +
  theme_light()

library(ggthemes)
ggplot(Salaries,aes(yrs.service,salary,color=rank))+
  geom_point() +
  theme_foundation()

## Customising themes
ggplot(Salaries,aes(yrs.service,salary,color=rank))+
  geom_point() +
  theme_light() +
  theme(legend.position = "top")






