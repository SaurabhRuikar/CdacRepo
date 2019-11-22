########################################################

#Title:
#Author:AnkitSaurabh
#description :This is combine string program
#usage ./combine_str.sh
#usage bash combine_str.sh


#########################################################

#!/bin/bash

string1="saurabh"
string2="ankit"
echo "$string1 $string2"
string3="$string1  $string2"
echo "$string3"

string3+=" Authorized Training Centre"
echo "$string3"