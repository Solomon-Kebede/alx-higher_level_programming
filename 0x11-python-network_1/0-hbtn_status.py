#!/usr/bin/python3

'''
-Write a Python script that fetches `https://alx-intranet.hbtn.io/status`
    -You must use the package `urllib`
    -You are not allowed to import any packages other than `urllib`
    -The body of the response must be displayed like the following
    example (tabulation before -)
    -You must use a `with` statement

'''


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    data = res.read()
print(f"Body response:\n\t- type: {type(data)}\n\t- \
content: {data}\n\t- utf8 content: {data.decode('utf-8')}")
