#!/usr/bin/python3

'''
Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

    -Your script should take 3 arguments: `mysql username`, `mysql password`
    and `database name`
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running on `localhost`
    at port `3306`
    -Results must be sorted in ascending order by `cities.id`
    -You can use only `execute()` once
    -Your code should not be executed when imported

'''


from sys import argv
import MySQLdb


def list_all_cities(user, passwd, db):
    '''List all cities ordered by id in
    ascending order'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('''SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;''')
    for result in cursor.fetchall():
        print(result)


if __name__ == '__main__':
    list_all_cities(argv[1], argv[2], argv[3])
