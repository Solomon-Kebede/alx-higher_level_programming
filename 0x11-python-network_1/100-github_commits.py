#!/usr/bin/python3

'''
-Write a Python script that takes 2 arguments in order to solve this challenge.
    -The first argument will be the `repository name`
    -The second argument will be the `owner name`
    -You must use the packages `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
'''

if __name__ == '__main__':
    import requests
    from sys import argv
    owner, repo = argv[1:3]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        "User-Agent": "python-requests/2.27.1",
        "Accept": "application/vnd.github+json",
        "Accept-Language": "en-US,en;q=0.5"
    }
    res = requests.get(url, headers=headers)
    jsonData = res.json()
    import pprint
    for data in jsonData:
        sha = data.get('sha')
        author_name = data.get('commit').get('author').get('name')
        print(f'{sha}: {author_name}')
