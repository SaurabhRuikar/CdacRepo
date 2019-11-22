########################################################

#Title:
#Author:AnkitSaurabh
#description :This is directory program
#usage ./directory.sh
#usage bash directory.sh


#########################################################

#!/bin/bash
<<q
echo "Enter Directory name"
read name

echo "$name"
mkdir $name
q
<<co
echo "Enter dirctory name and directory where you have to create"
echo "The directory name is := $1"
echo "The directory will get created in =$2"

cd $2
mkdir $1
co

#################
<<p
declare  -a dir=("Sankalp" "Ankit1" "Saurabh2")
cd /home/student/Desktop
for val in ${dir[@]}
do 
    
    mkdir $val
done    
p


<<x 
THIS IS WRONG LOL but correct output for another program
declare  -a dir=("a.txt" "b.txt" "c.txt")
#cd /home/student/Desktop
for val in ${dir[@]}
do 
    echo "Enter the current directory"
    read curd
    cd $curd
    touch $val
done  
x

<<y
declare  -a dir=("ankit" "kamthe" "saurabh")
#cd /home/student/Desktop
for val in ${dir[@]}
do 
    cd $val
    for ((i=0; i<2 ;i++))
    do
        echo "File ? :"
        read file
        touch $file
    done
    cd ..
done 
y


<<q
echo "Enter the directory name"
read path
cd $path
for ((i=0; i<2 ;i++))
    do
        echo "File ? :"
        read file
        touch $file
    done
q


<<o
echo "Enter Directory"
read dir


rm -r $dir
o




