########################################################

#Title:
#Author:AnkitSaurabh
#description :This is a authentication program
#usage ./authentication.sh
#usage bash authentication.sh


#########################################################

#!/bin/bash

user1="abc"
pass1="def"

echo "Entered Username = $1"
echo "Entered Password = $2"

if [[($1 == $user1 && $2 == $pass1)]]; then
echo "valid user"
else
echo "Invalid"
fi

