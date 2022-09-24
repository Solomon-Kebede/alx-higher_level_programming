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
