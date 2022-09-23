#!/bin/bash
# script to make a `POST` request to URL, and displays the response body; `email`=`test@gmail.com` & `subject`=`I will always be here for PLD`
curl -sX "POST" -d email=test@gmail.com -d subject="I will always be here for PLD" $1
