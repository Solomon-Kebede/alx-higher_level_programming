#!/bin/bash
# Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
curl -sL -H "Content-Type: application/json" -H "user_id: 98" -X PUT --data 'You got me!' $1 | grep "You" | cut -c 42-52
