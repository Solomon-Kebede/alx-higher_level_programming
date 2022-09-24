#!/usr/bin/python3

'''
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in `utf-8`).

    -You have to manage urllib.error.HTTPError exceptions and
    print: `Error code:` followed by the HTTP status code
    -You must use the packages `urllib` and `sys`
    -You are not allowed to import other packages than `urllib` and `sys`
    -You don’t need to check arguments passed to the script (number or type)
    -You must use the `with` statement

Please test your script in the sandbox provided, using the
web server running on port 5000
'''

from sys import argv
from urllib import request
from urllib.error import HTTPError

url = argv[1]

try:
    with request.urlopen(url) as res:
        if res.status < 400:
            print(res.read().decode())
except HTTPError as e:
    if e.status >= 400:
        print(f'Error code: {e.status}')
    else:
        print(res.read().decode())
