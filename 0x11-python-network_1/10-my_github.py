#!/usr/bin/python3

'''
-Write a Python script that takes your GitHub credentials
(username and password) and uses the `GitHub API` to display your `id`
    -You must use `[Basic Authentication]
(https://docs.github.com/en/rest/overview/other-authentication-methods)`
with a `[personal access token](https://docs.github.com/en/authentication\
/keeping-your-account-and-data-secure/creating-a-personal-access-token)`
as password to access to your information
(only `read:user` permission is needed)
    -The first argument will be your `username`
    -The second argument will be
    your `password` (in your case, a `personal access token as password`)
    -You must use the package `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to check arguments passed to the script (number or type)
'''

if __name__ == '__main__':
    import requests
    from sys import argv
    username, password_token = argv[1:3]
    url = f'https://api.github.com/users/{username}'
    headers = {
        "User-Agent": "python-requests/2.27.1",
        "Accept": "application/vnd.github+json",
        "Accept-Language": "en-US,en;q=0.5",
        "Authorization": f"Bearer {password_token}"
    }

    res = requests.get(url, headers=headers)
    jsonData = res.json()
    print(jsonData.get('id'))
