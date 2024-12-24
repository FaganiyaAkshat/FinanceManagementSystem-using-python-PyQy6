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

def made():
    conn = sqlite3.connect(resource_path("db/firm_management.db"))
    print(conn)
    cursor = conn.cursor()
    try:
        # Step 1: Connect to SQLite database
        # This will create the database file if it does not exist


        # Step 2: Create tables as per requirements

        # Table 1: admin
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin (
                id INTEGER NOT NULL PRIMARY KEY,
                uname TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        # Insert default record into admin
        cursor.execute("SELECT * FROM admin WHERE id = 1")
        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO admin (id, uname, password, email)
                VALUES (1, 'admin', 'admin', 'akshatpatel152@gmail.com');
            """)

        # Table 2: check_vote
        cursor.execute("""
            INSERT INTO admin (id, uname, password, email)
            VALUES (1, 'admin', 'admin', 'akshatpatel152@gmail.com')
            ON CONFLICT (id) DO NOTHING;
        """)
        # Table 3: addmember
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS addmember (
                sr INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                userid INTEGER NOT NULL UNIQUE,
                username TEXT NOT NULL,
                aadhar TEXT NOT NULL,
                mobile TEXT NOT NULL,
                email TEXT NOT NULL,
                city TEXT NOT NULL,
                joindae DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                nominyname TEXT NOT NULL,
                nominyaadhar TEXT NOT NULL
            );
        """)

        # Table 4: funds
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funds (
                sr INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id INTEGER NOT NULL,
                username TEXT NOT NULL,
                funds DECIMAL(10, 0) NOT NULL,
                interest DECIMAL(10, 0) NOT NULL,
                datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_interest_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        # Table 5: loan
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loan (
                sr INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                unique_n INTEGER NOT NULL,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL,
                date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (unique_n) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        # Table 6: voting
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS voting (
                id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                date DATE NOT NULL,
                yes INTEGER NOT NULL DEFAULT 0,
                no INTEGER NOT NULL DEFAULT 0,
                cdn INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (id),
                FOREIGN KEY (id) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        # Table 7: entry
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entry (
                t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                u_id INTEGER NOT NULL,
                t_amount INTEGER NOT NULL,
                t_type TEXT NOT NULL,
                t_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (u_id) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        # Table 8: bankrupt
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bankrupt (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                aadhar TEXT NOT NULL,
                fund INTEGER NOT NULL,
                UNIQUE (id),
                FOREIGN KEY (id) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        # Table 9: bad_dept
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bad_dept (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL,
                date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (id),
                FOREIGN KEY (id) REFERENCES addmember(userid) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS `check_vote` (
                `aadhar` varchar(100) NOT NULL,
                 PRIMARY KEY (`aadhar`)
            );
        """)
    except Exception:
        print("Error in creating tables")
    # Step 3: Commit changes and close connection
    conn.commit()
    conn.close()
    print("All tables created successfully!")

# Call the main function
if __name__ == "__main__":
    made()
