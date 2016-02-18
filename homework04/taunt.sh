PATH=$PATH:/afs/nd.edu/user15/pbui/pub/bin

welcome()
{
          echo "Welcome to my house!" | cowsay

}

waiting()
{
          echo "What's taking so long? Netflix and chilling?" | cowsay
                  exit 0

}

hangup()
{
          echo "Mooooooooooooooo!" | cowsay
                  exit 0

}

terminate()
{
          echo "Bye Felicia." | cowsay
                  exit 0

}

welcome

for i in 0 1 2 3 4 5 6 7 8 9; do

  sleep 1
  trap hangup SIGHUP
  trap terminate SIGINT SIGTERM

done

waiting
