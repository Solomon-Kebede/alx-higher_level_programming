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


if __name__ == '__main__':
    '''Executed when run not on import'''
    import sys
    from urllib.request import urlopen
    from urllib.parse import urlencode
    if len(sys.argv) >= 2:
        url, email = sys.argv[1:3]
        data = urlencode({'email': email}).encode('ascii')
        with urlopen(url, data) as res:
            body = res.read().decode('utf-8')
        print(body)
