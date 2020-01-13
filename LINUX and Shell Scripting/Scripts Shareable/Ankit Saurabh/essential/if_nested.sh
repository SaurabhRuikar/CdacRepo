########################################################

#Title:
#Author:AnkitSaurabh
#description :This is nested_if program
#usage ./if_nested.sh
#usage bash if_nested.sh


#########################################################

#!/bin/bash

echo "Enter your marks"
read marks

if [ $marks -eq 101 ];
then
echo "Rank 3"
elif [ $marks -eq 510 ];
then
echo "Rank 2"
elif [ $marks -eq 600 ];
then
echo "Rank 1"
else
echo "You failed"
fi