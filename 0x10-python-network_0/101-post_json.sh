#!/bin/bash
# Bash script that sends a JSON `POST` w/ First argument: URL and second argument: filename to read, server check s json validity
curl -s -H "Content-Type: application/json" -X POST --data "$(cat $2)" $1
