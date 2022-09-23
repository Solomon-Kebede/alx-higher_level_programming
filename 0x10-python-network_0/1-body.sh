#!/bin/bash
# script takes in a URL, sends a `GET` request to the URL, and displays the body of the response if `200` status code response
if [ $(curl -sI $1 | grep '200 OK' -c ) -eq 1 ]; then curl $1; fi
