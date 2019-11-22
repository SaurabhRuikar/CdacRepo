# Function Definition
add <- function(a,b,c){
  a+b+c
}

# OR

add <- function(a,b,c){
  return(a+b+c)
}

add(3,4,9)

descriptive <- function(input) {
  df <- data.frame(Mean = mean(input,na.rm = TRUE),
                   SD = sd(input,na.rm = TRUE))
  df
}

desc <- descriptive(mtcars$mpg)

###### Nested Function #######
raise_val <- function(n){
  inner <- function(x){
    x ** n
  }
  inner
}

square<-raise_val(2)
square(12)

cube <- raise_val(3)
cube(4)

quad <- raise_val(4)
quad(2)
