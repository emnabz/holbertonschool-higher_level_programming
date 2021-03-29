#!/usr/bin/python3
"""
Same script of 'task2' with a script of MySQL injections
"""
import MySQLdb
import sys


def print_all_names():
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               charset="utf8"
                               )
    cur = database.cursor()
    search = sys.argv[4]
    cur.execute("""SELECT id,name FROM states WHERE name = %s
        ORDER BY id ASC""", (search, ))
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    database.close()


if __name__ == "__main__":
    print_all_names()
