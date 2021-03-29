#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys

def print_all_states():
    """print all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    db = MySQLdb.Connect(host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=dataBase)

    cur = db.cursor()
    cur.execute("SELECT * WHERE states.name LIKE 'N%' ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print (state)

    cur.close()
    db.close()

if __name__ == "__main__":
    print_all_states()
