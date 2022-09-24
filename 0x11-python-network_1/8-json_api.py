#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a `POST` request
to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
    The letter must be sent in the variable `q`
    If no argument is given, set `q=""`
    If the response body is properly JSON formatted and not empty, display
    the id and name like this: [<id>] <name>
    Otherwise:
        Display `Not a valid JSON` if the JSON is invalid
        Display `No result` if the JSON is empty
    -You must use the packages `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to error check arguments passed to the
    script (number or type)
Please test your script in the sandbox provided, using the web server running
on port 5000
'''
if __name__ == '__main__':
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
