#!/bin/bash
echo "Welcome to Shell scripting"
echo "Hello Linux"
read count 
echo "Current user = $count" 

echo "$(whoami) !!!!!!! yay"
echo "Operating System is  $(uname) !!!!!!!!"

echo "host $(hostname)"
echo "Added new line!!!!!!!!!!!"
echo "Enter number 1"
read c1
echo " Number 1 is $c1"


echo "Enter number 2"
read c2
echo " Number 2 is $c2"

((sum1= $c1+ $c2))

echo "result=$sum1"
<<a
ls>>r1.txt
cat r1.txt


cat r2.txt r3.txt >> r4.txt
cat r4.txt
 cat  r2.txt hello.sh >> r5.txt
 cat r5.txt 

a

# mathematical expression

#((sum = 34+66))

#show result 
#echo "result = $sum"
<<c
this is a simple script
this is a second line
c
