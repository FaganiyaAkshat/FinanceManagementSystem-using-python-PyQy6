import os
import sqlite3
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def delete_tables():
    conn = sqlite3.connect(resource_path("db/firm_management.db"))
    cursor = conn.cursor()

    try:
        # Drop all the tables
        cursor.execute("DROP TABLE IF EXISTS admin")
        cursor.execute("DROP TABLE IF EXISTS check_vote")
        cursor.execute("DROP TABLE IF EXISTS addmember")
        cursor.execute("DROP TABLE IF EXISTS funds")
        cursor.execute("DROP TABLE IF EXISTS loan")
        cursor.execute("DROP TABLE IF EXISTS voting")
        cursor.execute("DROP TABLE IF EXISTS entry")
        cursor.execute("DROP TABLE IF EXISTS bankrupt")
        cursor.execute("DROP TABLE IF EXISTS bad_dept")

        print("All tables deleted successfully!")
    except Exception as e:
        print("Error in deleting tables:", e)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_tables()