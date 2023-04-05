#/bin/bash
#send a post request to the url and display response
curl -s -X -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
