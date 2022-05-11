#!/usr/bin/python3
"""Task 2 Project 0x0F Python"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Conecting to the Databese take on argument to make a query and print"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    com1 = "SELECT name FROM cities WHERE state_id = (SELECT id FROM states "
    com2 = com1 + "WHERE name=%s) ORDER BY cities.id"
    cur.execute(com2, (sys.argv[4], ))
    query_rows = cur.fetchall()
    i = 0
    for row in query_rows:
        print(row[0], end="")
        if not i == len(query_rows) - 1:
            print(", ", end="")
        else:
            print("")
        i += 1
    cur.close()
    conn.close()
