#!/usr/bin/python3
"""
Module that lists states with names starts with N
from the database hbtn_0e_0_usa
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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for i in row:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    database.close()


if __name__ == "__main__":
    print_all_names()
