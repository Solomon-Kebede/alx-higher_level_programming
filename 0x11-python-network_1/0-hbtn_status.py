#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    data = res.read()
print(f"Body response:\n\t- type: {type(data)}\n\t- \
content: {data}\n\t- utf8 content: {data.decode('utf-8')}")
