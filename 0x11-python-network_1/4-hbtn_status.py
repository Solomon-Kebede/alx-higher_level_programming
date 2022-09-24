#!/usr/bin/python3


'''
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

    -You must use the package `requests`
    -You are not allow to import packages other than `requests`
    -The body of the response must be display like the
    following example (tabulation before -)
'''


import requests
res = requests.get('https://alx-intranet.hbtn.io/status')
print(f"Body response:\n\t- type: {type(res.text)}\n\t- \
content: {res.text}")
