read -p "Enter name: " name

if [ "$name" == "bob" ]
then
  echo "liar"
else
  echo "Your name is $name"
fi

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
