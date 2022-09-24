#!/usr/bin/python3


'''
Write a Python script that takes in a URL, sends a request to the
URL and displays the value of the `X-Request-Id` variable found
in the header of the response.
    You must use the packages `urllib` and `sys`
    You are not allow to import packages other than `urllib` and `sys`
    The value of this variable is different for each request
    You don’t need to check arguments passed to the script (number or type)
    You must use a `with` statement
'''

import urllib.request
from sys import argv

if len(argv) > 1:
    url = argv[1]
    with urllib.request.urlopen(url) as res:
        headers = res.headers

    headers_dict = dict()

    for header in headers.__str__().split('\n'):
        try:
            headers_dict[header.split(': ')[0]] = header.split(': ')[1]
        except IndexError:
            pass
    print(headers_dict['X-Request-Id'])
