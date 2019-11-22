##P[x<=69]
pbinom(69,71,0.94)

1-pbinom(69,71,0.94) 


dbinom(0,20,0.35)

dbinom(10,20,0.35)

pbinom(10,20,0.35)

pbinom(13,20,0.35,lower.tail = F)


qnorm(0.95,100,15)









ppois(69,56,lower.tail = F)
ppois(19,56)

ppois(5,56,lower.tail = F) 
 
ppois(2,56)


qnorm(0.95,100,15)

pnorm(2000,1678,500,lower.tail = F)

qnorm(0.1,1678,500,lower.tail = F)



pnorm(1900,1678,500)-pnorm(1000,1978,500)



1-pbinom(279,300,0.94) 
pbinom(20,300,0.06)



 
##13
Male  <- c(123 ,24 ,17 ,52 ,8)
Female<- c(86,  8, 10, 73, 4)
dt <- rbind(Male,Female)
dt
prop.table(dt)
addmargins(prop.table(dt))
  
East  =c(56 ,42)
North =c(43 ,42)
South =c(62 ,37)
West  =c(100,90)

r <- rbind(East,North,South,West)
r


prop.table(r)

addmargins(prop.table(r))


prop.table(r,1)


(pnorm(700,590,22,lower.tail = F))*100


g <- c(550,600,650,700)
(g-590)/22