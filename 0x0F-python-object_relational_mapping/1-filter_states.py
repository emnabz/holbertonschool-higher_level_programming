#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys


def print_table_state():
    """print table state"""
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dataBase)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'ORDER BY states.id ASC")
    names = cur.fetchall()
    for name in names:
        print(name)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_table_state()
