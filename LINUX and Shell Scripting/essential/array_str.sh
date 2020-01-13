########################################################

#Title:
#Author:AnkitSaurabh
#description :This is array seperation program
#usage ./array_str.sh
#usage bash array_str.sh


#########################################################
#!/bin/bash
#Read a string with spaces using for loop

<<c
for value in Ankit saurabh Sankalp Jafar
do 
    echo $value
done
c

<<a

Stringval="Welcome my Friends Bye"
#Iterate the string variable using for loop
for value in $Stringval
do 
    echo $value
done
a



#Declare an array of string with type
declare -a cities=("Ankit" "saurabh" "Jafar")


#Iterate the string array using for loop
<<x
for val in ${cities[@]};do  #here ; is before do it is for to continue 'do' on same line
  echo $val
done  
x
<<y
for val in "${cities[*]}";do  #here ; is before do it is for to continue 'do' on same line
  echo $val
done  
y

DataList=" OS,DS ,Netwotking ,ImageProcessing"
Field_Separator=$IFS

# Set comma as internal field seperator for the string list
<<z
IFS=,
for val in ${DataList[*]};
do
  echo $val
done

IFS=$Field_Separator
z

dacModules=("C" "CPP" "C#")
dbdaModules=("Cloud" "Python" "ML")
combine=(dacModules dbdaModules)

for arrItem in ${combine[@]}
do
    eval 'for val in "${'$arrItem'[@]}";do echo "$val";done'
done











