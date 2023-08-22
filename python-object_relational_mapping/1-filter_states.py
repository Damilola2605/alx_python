#!/bin/usr/python3
"""
This module list all state that starts with N
"""
import MySQLdb
import sys


def list_states_with_N(username, password, database):
    """
    This function list states with uppercase N
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
    """Execute the SQL query to retrieve states starting with 'N'"""
    query = "SELECT * FROM states WHERE name LIKE 'N' ORDER BY id ASC"
    cursor.execute(query)
    """Get all the rows from the result set"""
    results = cursor.fetchall()
    """Print the results"""
    for row in results:
        print(row)
    """Close the cursor and the database connection"""
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_N(username, password, database)
