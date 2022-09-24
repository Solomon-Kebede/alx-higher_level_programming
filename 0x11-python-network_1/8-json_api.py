#!/usr/bin/python3
from sys import argv
import requests


if len(argv > 1):
    letter = argv[1]
elif len(argv == 1):
    letter = ''

data = {'q': letter}
res = requests.post(url, data)
try:
    json = res.json()
    if json != {}:
        print(f"[{json['id']}] {json['name']}")
    elif json == {}:
        print('No result')
except Exception:
    print('Not a valid JSON')
