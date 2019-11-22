########################################################

#Title:
#Author:AnkitSaurabh
#description :This is while program
#usage ./while.sh
#usage bash while.sh


#########################################################

#!/bin/bash

status=true
count=1
while [ $status ]+

do 
    echo $count

    if [ $count -eq 4 ]
    then
    break;
    fi
((count++))
done