a <- 34000
b <- 50000
if(a+b>10000) {
  paste("Total greater than 10000")
} else {
  paste("Total not greater than 10000")
}


for(i in 1:4) {
  print(i)
}

cnt <- 1
while(cnt < 5) {
  print(cnt)
  cnt <- cnt + 1
}

s <- seq(1,20,by=4)

for(i in s) {
  print(i*i)
}
