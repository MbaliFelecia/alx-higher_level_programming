#!/usr/bin/python3
"""
Lists all states starting with upper N
from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE BINARY 'N%'\
                 ORDER BY states.id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)
