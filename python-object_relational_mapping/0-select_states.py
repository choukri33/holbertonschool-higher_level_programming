#!/usr/bin/python3
"""Script that retrieves all states from the database"""
import sys
import MySQLdb as db

def connect_and_query() -> None:

    """Establish connection to the database and execute the query."""
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT * FROM states ORDER BY `id` ASC;')
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_and_query()
