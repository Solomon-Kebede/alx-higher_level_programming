#!/bin/bash
# Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
#     Display only body of a `200` status code response
#     You have to use `curl`
# Please test your script in the sandbox provided, using the web server running on port 5000
if [ $(curl -sI $1 | grep '200 OK' -c ) -eq 1 ]
then
	curl $1
fi
