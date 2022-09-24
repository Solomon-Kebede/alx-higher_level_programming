#!/usr/bin/python3
from sys import argv
import requests

url, email = argv[1:3]
data = {'email': email}
res = requests.post(url, data=data)
print(res.text)
