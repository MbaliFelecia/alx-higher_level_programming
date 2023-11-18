#!/usr/bin/python3
"""
Script that takes an argument and
all states values that match it
from the database `hbtn_0e_0_usa`
safe from MySQL injections
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
                 WHERE name = %s;", argv[4])
    states = cur.fetchall()

    for state in states:
        print(state)
