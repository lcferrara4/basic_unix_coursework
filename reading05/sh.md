Lauren Ferrara
Reading05 Summary Page

**variables**

  * Just use an = sign
  * Example: title = "System Information for"

**capturing STDOUT**

  for homedir in /home/*

    do rm "$homedir/secret"

  done 2> /dev/null 

**if statement**

  if [ -f .bash_profile  ]; then

      echo "You have a .bash_profile. Things are fine."

  else

      echo "Yikes! You have no .bash_profile!"

  fi

**case statement**

  echo -n "Enter a number between 1 and 3 inclusive > "

  read character

  case $character in

      1 ) echo "You entered one."

        ;;

      2 ) echo "You entered two."

        ;;

      3 ) echo "You entered three."

        ;;

      * ) echo "You did not enter a number between 1 and 3."

  esac

**for loop**
  

  for i in 1 2 3 4 5

  do

    echo "Looping ... number $i"

  done

**while loop**

  INPUT_STRING=hello

  while [ "$INPUT_STRING" != "bye"  ]

  do

    echo "Please type something in (bye to quit)"

    read INPUT_STRING

    echo "You typed: $INPUT_STRING"

  done

**function**

  myfunc(){

    echo "\$1 is $1"

    echo "\$2 is $2"

    a="Goodbye Cruel"

  }


**trap**

  TEMP_FILE=/tmp/printfile.txt

  trap "rm $TEMP_FILE; exit" SIGHUP SIGINT SIGTERM

  pr $1 > $TEMP_FILE

  echo -n "Print file? [y/n]: "

  read
    
   if [ "$REPLY" = "y"  ]; then
  
      lpr $TEMP_FILE

   fi

  rm $TEMP_FILE

