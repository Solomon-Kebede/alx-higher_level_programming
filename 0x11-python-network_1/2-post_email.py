#!/usr/bin/python3


'''
Write a Python script that takes in a URL and an email, sends a
`POST` request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
    The `email` must be sent in the email variable
    You must use the packages `urllib` and `sys`
    You are not allowed to import packages other than `urllib` and `sys`
    You don’t need to check arguments passed to the script (number or type)
    You must use the `with` statement
Please test your script in the sandbox provided, using
the web server running on port 5000
'''

from sys
from urllib

if __name__ == '__main__':
    if len(sys.argv >= 2):
        url, email = sys.argv[1:3]
        data = urllib.parse.urlencode({'email': email}).encode('ascii')
        with urllib.request.urlopen(url, data) as res:
            body = res.read().decode('utf-8')
        print(body)