#!/usr/bin/python3

'''
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

    -Your script should take 3 arguments: `mysql username`, `mysql password`
    and `database name` (no argument validation needed)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -Results must be sorted in ascending order by `states.id`
    -Your code should not be executed when imported
'''


from sys import argv
import MySQLdb


def list_states(user, passwd, db):
    '''List all states ordered by id in
    ascending order'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        print(result)


if __name__ == '__main__':
    list_states(argv[1], argv[2], argv[3])
