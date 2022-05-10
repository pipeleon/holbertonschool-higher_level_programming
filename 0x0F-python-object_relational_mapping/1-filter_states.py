#!/usr/bin/python3
"""Task 0 Project 0x0F Python"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Conecting to the Databese take on argument to make a query and print"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    try:
        com1 = "SELECT * FROM states WHERE states.name"
        command = com1 + " REGEXP '^N' ORDER BY states.id ASC"
        cur.execute(command)
        query_rows = cur.fetchall()
    except e:
        try:
            print("MySQL Error {:d}: {:s}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
