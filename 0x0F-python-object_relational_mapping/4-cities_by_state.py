#!/usr/bin/python3
"""
A script that lists all cites from the db hbtn_0e_4_usa
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
    cur.execute("""SELECT cities.id,cities.name,states.name
    FROM cities INNER JOIN states ON cities.state_id=states.id""")
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    database.close()


if __name__ == "__main__":
    print_all_cites()
