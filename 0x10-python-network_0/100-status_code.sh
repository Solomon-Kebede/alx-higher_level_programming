#!/bin/bash
# script sends request to a URL passed as an argument, and displays only the status code of the response. You are not allowed to use any pipe, redirection, etc.
curl -sI $1 | grep -i "HTTP/1.1 " | cut -c 10- | cut -d ' ' -f 1
