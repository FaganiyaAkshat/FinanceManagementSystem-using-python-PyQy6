import os
import sys
import time
from datetime import datetime, timedelta
import sqlite3  # Changed from mysql.connector to sqlite3
from decimal import Decimal
from PyQt6.QtCore import QThread, QCoreApplication

# Database connection details
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

DB_CONFIG = resource_path('db/firm_management.db')  # SQLite database file

class InterestCalculationThread(QThread):
    def run(self):
        while True:
            try:
                now = datetime.now()
                if now.hour == 0 and now.minute == 0:  # Ensure it's exactly midnight
                    self.update_funds_and_interest()
                    time.sleep(61)  # Sleep for more than one minute to avoid multiple updates within the same minute

                self.update_funds_and_interest()  # Check and update interest if missed
                # Sleep for one minute before checking again
                time.sleep(60)
            except Exception as e:
                print(f"An error occurred in the run loop: {e}")

    def calculate_interest(self, funds):
        try:
            con = sqlite3.connect(DB_CONFIG)  # Connect to SQLite database
            cursor = con.cursor()
            in_new = "SELECT interest FROM funds LIMIT 1"
            cursor.execute(in_new)
            r = cursor.fetchone()
            d_interest = None
            if r is not None:
                d_interest = r[0]
            daily_interest_rate = Decimal(d_interest / 100) / 365  # 12% annual interest rate divided by 365 days
            return funds * daily_interest_rate
        except Exception as e:
            print(f"An error occurred while calculating interest: {e}")
            return Decimal(0)
        finally:
            if con:
                con.close()  # Ensure the connection is closed

    def update_funds_and_interest(self):
        con = None
        try:
            con = sqlite3.connect(DB_CONFIG)  # Connect to SQLite database
            cursor = con.cursor()

            # Select all records to update
            cursor.execute("SELECT sr, funds, last_interest_date FROM funds")
            records = cursor.fetchall()

            now = datetime.now().date()  # Current date

            for record in records:
                sr, funds, last_interest_date = record

                # Ensure funds is not None and is valid
                if funds is None:
                    funds = Decimal(0)  # Default to 0 if funds is None

                if last_interest_date is None:
                    last_interest_date = now - timedelta(days=1)  # Default to one day ago
                else:
                    last_interest_date = datetime.strptime(last_interest_date.split()[0],
                                                           '%Y-%m-%d').date()  # Adjusted line

                # Calculate the number of missed intervals (days)
                missed_intervals = (now - last_interest_date).days

                if missed_intervals > 0:  # Only print if there are missed intervals
                    print(f"Processing record: sr={sr}, funds={funds}, last_interest_date={last_interest_date}")
                    print(f"Missed intervals: {missed_intervals}")

                    for _ in range(missed_intervals):  # Missed days up to but not including today
                        interest = self.calculate_interest(Decimal(funds))  # Ensure Decimal type
                        funds += interest

                    # Update funds and last_interest_date in the database
                    update_query = "UPDATE funds SET funds = ?, last_interest_date = ? WHERE sr = ?"
                    cursor.execute(update_query, (float(funds), now, sr))  # Ensure funds is a float
                    print(f"Updated record: sr={sr}, funds={funds}, last_interest_date={now}")

            con.commit()
            if any(record for record in records if (now - datetime.strptime(record[2].split()[0],
                                                                            '%Y-%m-%d').date()).days > 0):  # Adjusted line for comparison
                print(f"Interest updated at {datetime.now()}")

        except sqlite3.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"An error occurred while updating funds and interest: {e}")
        finally:
            if con:
                con.close()  # Ensure the connection is closed
