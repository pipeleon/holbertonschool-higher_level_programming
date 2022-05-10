#!/usr/bin/python3
"""Task 2 Project 0x0F Python"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Conecting to the Databese take on argument to make a query and print"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    com1 = "SELECT * FROM states WHERE "
    com2 = com1 + "states.name=%s ORDER BY states.id ASC"
    cur.execute(com2, (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
