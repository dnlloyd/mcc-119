#!/bin/bash

echo "Enter name: "
read name

# echo "Enter age: "
# read age

# if [[ "${name}" == "bob" && "${age}" -gt 15 ]]
# then
#   echo "Your name is bob and you are old enough to drive"
# elif [[ "${age}" -gt 15 ]]
# then
#   echo "you are old enough to drive"
# else
#   echo "you are too young to drive"
# fi

case $name in
  "dan")
    echo "You're the teacher"
    ;;

  "martha")
    echo "You're on the Brady Bunch"
    ;;

  *)
    echo "I don't know who you are"
    ;;
esac
