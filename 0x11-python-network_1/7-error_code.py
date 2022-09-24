#!/usr/bin/python3
from sys import argv
import requests

url, email = argv[1]
res = requests.get(url)
if res.status_code >= 400:
    print(f'Error code: {res.status_code}')
else:
    print(res.text)
