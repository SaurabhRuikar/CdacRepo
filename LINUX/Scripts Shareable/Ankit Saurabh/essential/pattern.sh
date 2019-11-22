########################################################

#Title:
#Author:AnkitSaurabh
#description :This is pattern program
#usage ./pattern.sh
#usage bash pattern.sh


#########################################################

#!/bin/bash

echo "Enter Value for specific pattern"
read num

echo "You entered $num"

for ((i=0; i<=num; i++))
do 
    for ((j=0; j<=i; j++))
    do
        echo -n "*"
      
    done
    echo 

done
