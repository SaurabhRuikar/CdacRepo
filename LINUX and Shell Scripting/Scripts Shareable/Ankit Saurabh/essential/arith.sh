########################################################

#Title:
#Author:AnkitSaurabh
#description :This is arithmetic operations program
#usage ./arith.sh
#usage bash arith.sh


#########################################################


#!/bin/bash

#let command used to perform arithmetic operations
#shell variables

let arg1=12
let arg2=11

let add=$arg1+$arg2
let sub=$arg1-$arg2
let mul=$arg1*$arg2
let div=$arg1/$arg2
echo $add $sub $mul $div