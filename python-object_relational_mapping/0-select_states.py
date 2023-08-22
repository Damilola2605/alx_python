#!/bin/usr/python3
"""
This module list the states in the hbtn database
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function is to connect Mysql server
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    """Creating a cursor object for interation in database"""
    cursor = db.cursor()
    """Executing the SQL quary to get the list of states"""
    quary = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(quary)
    """Get all the rows in the result set"""
    results = cursor.fetchall()
    """Print the results"""
    for row in results:
        print(row)

    """Stop the cursor and database connection"""
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
