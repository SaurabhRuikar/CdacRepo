########################################################

#Title:
#Author:AnkitSaurabh
#description :This is if program
#usage ./if_simple.sh
#usage bash if_simple.sh


#########################################################

#!/bin/bash

echo "Enter your marks"
read marks

if [ $marks -lt 60 ];
then
echo "Sorry you're a failure!"
else
echo "Wow you managed to pass"
fi