#!/bin/bash

# 1. ###########################
echo "Hello World!"


# 2. ###########################
echo -e "Hello\nWorld!"


# 9. ###########################
NAME=Dan
echo "My name is ${NAME}"


# 3. ###########################
read -p "Enter your name: " name

echo "Your name is ${name}"

# 3. ###########################
read -s -p "Enter your password: " password

echo -e "Password: ${password}"


# 4. ###########################
echo "Enter your name: "
read name

if [ $name == "Dan" ]
then
    echo "Hey, that's my name"
else
    echo "Nice name ${name}"
fi


# 5. ###########################
echo "Enter your name: "
read name

echo "Enter your age: "
read age

if [[ $name == "Dan" && $age -lt 50 ]]
then
    echo "Hey, that's my name and you're younger than I am!"
elif [ $name == "Dan" ]
then
    echo "Hey, that's my name but you're NOT younger than I am"
else
    echo "Nice name ${name}"
fi


# 6. ###########################
ls -1 /var/www/html/
ls -1 /var/www/html | grep ^S

for dir in $( ls -1 /var/www/html | grep ^S)
do
    cat /var/www/html/$dir/index.html
done


# 7. ###########################
ps -ef  |grep pts
ps -ef  |grep pts | grep "\-bash"

ps -ef | grep pts | grep "\-bash" | grep -v grep | awk '{print $2}'

for user_pid in $( ps -ef | grep pts | grep "\-bash" | grep -v grep | awk '{print $2}' )
do
    # kill -9 $user_pid
    echo "kill -9 ${user_pid}"
done


# 8. ###########################
while true
do
    clear
    echo "-------------------------------------------------"
    date
    echo "-------------------------------------------------"
    df -h
    sleep 
done


# 10. ###########################
cat .bashrc
echo $?

cat .mashrc
echo $?


# 10. ###########################
function print_some_params() {
    echo "parameter one: ${1}"
    echo "parameter two: ${2}"
    echo ""
}

print_some_params "hello" "World"
print_some_params "World" "hello"
