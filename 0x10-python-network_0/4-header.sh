#!/bin/bash
# script takes in a URL as an argument, makes a `GET` request to URL, and displays the response body; header variable `X-School-User-Id` = `98`
curl -sH "X-School-User-Id: 98" $1
