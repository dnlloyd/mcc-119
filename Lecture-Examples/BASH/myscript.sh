echo "Enter name"
read name
 
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
