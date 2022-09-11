#!/usr/bin/python3

'''
Write a script that takes in an argument and displays all values in
the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

    -Your script should take 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name searched` (no argument validation needed)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running on `localhost`
    at port `3306`
    -You must use `format` to create the SQL query with the user input
    -Results must be sorted in ascending order by `states.id`
    -Your code should not be executed when imported
'''


from sys import argv
import MySQLdb


def list_states_matching(user, passwd, db, state_name):
    '''List all states ordered by id in
    ascending order that match "state_name"'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        if result[1].startswith(state_name):
            print(result)


if __name__ == '__main__':
    list_states_matching(argv[1], argv[2], argv[3], argv[4])
