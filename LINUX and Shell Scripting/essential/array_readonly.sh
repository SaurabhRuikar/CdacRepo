########################################################

#Title:
#Author:AnkitSaurabh
#description :This is array program
#usage ./array_readonly.sh
#usage bash array_readonly.sh


#########################################################

#!/bin/bash
#making array readonly
readonly -a shells=("Knowit" "Icasd" "Sunbeam" "Dac");
#readonly shells=("Knowit" "Icasd" "Sunbeam" "Dac")

echo ${#shells[@]}

shells[0]="MET"

echo ${shells[@]}

