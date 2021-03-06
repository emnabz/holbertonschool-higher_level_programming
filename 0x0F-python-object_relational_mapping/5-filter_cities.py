#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cites
using the db hbtn_0e_4_usa
"""
import MySQLdb
import sys


def print_all_cites():
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               charset="utf8"
                               )
    cur = database.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
    cities.state_id=states.id WHERE states.name \
    LIKE %s ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    database.close()


if __name__ == "__main__":
    print_all_cites()
