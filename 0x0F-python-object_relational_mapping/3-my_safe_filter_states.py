#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
   butsafe from MySQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s"
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
