library(MASS)
data("Boston")
head(Boston)

# Summing the row
sum(Boston[1,])
#OR
apply(Boston[1,], 1, sum)

apply(Boston,1,sum)

apply(Boston,2,sum)

# All Rows' SDs
apply(Boston,1,sd)

# Columns' SDs
apply(Boston,2,sd)

################## lapply() #################

#lst <- list(a=1:15,b=rnorm(18),c=rpois(23,9))

lst <- list(a=c(2,4,1,5),
             b=c(34,21,90,45,25,91,47),
             c=c(50,234,999,122,199,344,899,121,112))

lapply(lst, sd)

#### When first argument is not a list ####
lapply(c(2,5,10),log)


#### User defined function #########
CV <- function(input){
  (sd(input,na.rm = TRUE)/mean(input,na.rm = TRUE))*100
}
lapply(lst,CV)

#### Anonymous #####
lapply(lst, function(input) (sd(input,na.rm = TRUE)/mean(input,na.rm = TRUE))*100)

##### sapply ######

g = lapply(lst,sd)
class(g)

f = sapply(lst,sd)
class(f)

sapply(lst, sd)

descriptive <- function(input) {
  df <- c(Mean = mean(input,na.rm = TRUE),
          SD = sd(input,na.rm = TRUE))
  df
}
decr <- descriptive(Boston$medv)
class(decr)

d <- lapply(lst, descriptive)
class(d)
d <- sapply(lst, descriptive)
class(d)
d

library(MASS)
data("Cars93")
nums <- sapply(Cars93, is.numeric)

# Data Frame with only numeric columns
dfNums <- Cars93[,nums]

facts <- sapply(Cars93, is.factor)

# Data Frame with only factor columns
dfFacts <- Cars93[,facts]

### mapply ###
#lst_a <- list(a=1:15,b=rnorm(18),c=rpois(23,9))
#lst_b <- list(d=18:36,e=runif(12),g=rnorm(18))
lst_a <- list(a=c(2,4,1,5),
            b=c(34,21,90,45,25,91,47),
            c=c(50,234,999,122,199,344,899,121,112))
lst_b <- list(d=c(34,10,3),
              e=c(3,4,1),
              f=c(0,3,5,1,6))

mapply(sum, lst_a, lst_b)

mapply(sd, lst_a, lst_b)

mapply(c, lst_a, lst_b)

### tapply ####
library(Ecdat)
data("Housing")

mean(Housing$price)
tapply(Housing$price, Housing$driveway,
       mean)
tapply(Housing$price, Housing$stories,
       mean)
tapply(Housing$price, Housing$stories,
       median)


tapply(Boston$medv, Boston$rad, mean)
tapply(Boston$medv, Boston$chas, mean)

