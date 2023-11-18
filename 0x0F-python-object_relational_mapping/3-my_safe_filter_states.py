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
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        states = cur.fetchall()

    if states is not None:
        for state in states:
            print(state)
