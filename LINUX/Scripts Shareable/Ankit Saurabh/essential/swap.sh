########################################################

#Title:
#Author:AnkitSaurabh
#description :This is swap program
#usage ./swap.sh
#usage bash swap.sh


#########################################################

#!/bin/bash

echo "Enter num1"
read num1

echo "Enter num2"
read num2

echo "Number 1 is $num1"
echo "Number 2 is $num2"
<<e
let temp=0
#Swapping numbers

temp=$num1
num1=$num2
num2=$temp
e

#Without Temp

let num1=$num1+$num2
let num2=$num1-$num2
let num1=$num1-$num2







echo "Swapped nos are number1 is $num1 and Number2 is $num2"