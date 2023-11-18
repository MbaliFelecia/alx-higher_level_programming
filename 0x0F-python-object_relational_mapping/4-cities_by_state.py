#!/usr/bin/python3
"""
Script that lists all cities
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
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                states.id ASC
        """)

        states = cur.fetchall()

    if states is not None:
        for state in states:
            print(state)
