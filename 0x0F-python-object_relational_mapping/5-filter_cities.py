#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c\
              INNER JOIN states AS s\
              ON c.state_id = s.id\
              WHERE s.name = %s", (sys.argv[4],))
    cities = cur.fetchall()

    print(", ".join([city[1] for city in cities]))

    cur.close()
    db.close()
