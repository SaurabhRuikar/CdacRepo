########################################################

#Title:
#Author:AnkitSaurabh
#description :This is array program
#usage ./array_num.sh
#usage bash array_num.sh


#########################################################

#!/bin/bash

marks=(77 88 45 98 56 22 72 35)

size=${#marks[*]}
for((i=0;i<size;i++))
do
  echo -n "${marks[i]} "
done
