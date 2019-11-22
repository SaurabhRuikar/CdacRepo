########################################################

#Title:
#Author:AnkitSaurabh
#description :This is switch program
#usage ./case.sh
#usage bash case.sh


#########################################################

#!/bin/bash
echo "Enter no"
read n
case $n in
1)
echo "Monday" ;;
2)
echo "Tuesday" ;;
3)
echo "Wednesday" ;;
4) 
echo "Thursday" ;;
5)
echo "Friday" ;;
6)
echo "Saturday" ;;
7)
echo "Sunday" ;;
*) #can give any term in place of * . the * shows the default statement of a normal switch case statement
echo "Sorry you are dumb" ;;
esac
