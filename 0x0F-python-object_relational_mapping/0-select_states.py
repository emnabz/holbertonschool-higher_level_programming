#!/usr/bin/python3
"""create states table in hbtn_0e_0_usa with some data"""
import MySQLdb
import sys


def print_all_states():
    """print all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dataBase)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_all_states()
