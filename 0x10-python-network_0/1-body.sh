#!/bin/bash
# script takes in a URL, sends a `GET` request to the URL, and displays the body of the response if `200` status code response
curl -sL $1
