import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3  # Importing sqlite3 instead of mysql.connector

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_votingFrame(object):
    def setupUi(self, votingFrame):
        votingFrame.setObjectName("votingFrame")
        votingFrame.resize(806, 537)
        self.gridLayout = QtWidgets.QGridLayout(votingFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=votingFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("#widget\n"
                                  "{\n"
                                  "border:2px solid gray;\n"
                                  "border-radius:20px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(parent=self.widget)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setStyleSheet("QFrame{\n"
                                   "border: 2px solid #000;  /* Adds a 2px solid black border */\n"
                                   "border-radius: 0px;     /* Optional: Adds rounded corners */\n"
                                   "background-color: #9A79BA;  /* Optional: Adds a background color */\n"
                                   "}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_2.textChanged.connect(self.search_table)
        self.lineEdit_2.setPlaceholderText("Search")
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                       "background-color: #ffffff; /* White background */\n"
                                       "border: 2px solid black; /* Green border */\n"
                                       "border-radius: 10px; /* Rounded corners */\n"
                                       "padding: 10px; /* Padding */\n"
                                       "font-family: 'Arial', sans-serif; /* Font family */\n"
                                       "font-size: 14px; /* Font size */\n"
                                       "transition: all 0.3s ease; /* Smooth transition */\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "border-color: gray; /* Darker green border on focus */\n"
                                       "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)

        # Table setup
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame_8)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
                                          "border: 1px solid #888888; /* Green border for the table */\n"
                                          "border-radius: 10px; /* Rounded corners */\n"
                                          "background-color: #f0f0f0; /* Light grey background */\n"
                                          "font-family: 'Arial', sans-serif; /* Font for the table cells */\n"
                                          "font-size: 16px; /* Font size for the table cells */\n"
                                          "}\n"
                                          "QTableWidget::item {\n"
                                          "border: 1px solid #888888; /* Grey border for each cell */\n"
                                          "padding: 5px; /* Padding inside each cell */\n"
                                          "margin: px; /* Margin between cells */\n"
                                          "font-family: 'Arial', sans-serif; /* Font for the table cells */\n"
                                          "font-size: 16px; /* Font size for the table cells */\n"
                                          "}\n"
                                          "QHeaderView::section {\n"
                                          "background-color: #757575; /* Green header background */\n"
                                          "color: white; /* White text in the header */\n"
                                          "padding: 4px; /* Padding in header cells */\n"
                                          "border: 1px solid #dddddd; /* Border for header cells */\n"
                                          "font-family: 'Verdana', sans-serif; /* Font for the header */\n"
                                          "font-size: 16px; /* Font size for the header */\n"
                                          "font-weight: bold; /* Bold font for the header */\n"
                                          "}\n"
                                          "QScrollBar:vertical {\n"
                                          "background: #653C87;\n"
                                          "}")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(0)  # Initially no rows
        self.tableWidget_2.setColumnCount(4)  # Added column for delete button
        self.tableWidget_2.setObjectName("tableWidget_2")

        # Set column widths to occupy 100% of the table width
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        # Add headers for the table
        self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Subject of Voting", "Date of Voting", "Actions"])
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        # Load data from the database
        self.loadData()

    def loadData(self):
        try:
            # Connect to SQLite
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()

            # Query to fetch data from the database
            cursor.execute("SELECT id, subject, date FROM voting")
            records = cursor.fetchall()

            # Update table with records
            self.tableWidget_2.setRowCount(0)  # Clear existing rows
            for record in records:
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
                self.tableWidget_2.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(record[0])))  # ID
                self.tableWidget_2.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record[1]))  # Subject
                self.tableWidget_2.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record[2])))  # Date

                # Create a delete button for the last column
                delete_button = QtWidgets.QPushButton("Delete")
                delete_button.setStyleSheet("background-color: #DC143C; color: white; border-radius: 5px;")  # Set button color to red
                delete_button.clicked.connect(lambda checked, row=row_position: self.deleteRecord(row))
                self.tableWidget_2.setCellWidget(row_position, 3, delete_button)

            cursor.close()
            con.close()

        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")

    def deleteRecord(self, row):
        # Get the ID of the row to delete
        record_id = self.tableWidget_2.item(row, 0).text()

        try:
            # Connect to SQLite
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()

            # Query to delete record from the database
            cursor.execute("DELETE FROM voting WHERE id = ?", (record_id,))
            con.commit()

            # Remove the row from the table
            self.tableWidget_2.removeRow(row)

            cursor.close()
            con.close()

        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")

    def retranslateUi(self, votingFrame):
        _translate = QtCore.QCoreApplication.translate
        votingFrame.setWindowTitle(_translate("votingFrame", "Voting Management"))
        self.lineEdit_2.setText(_translate("votingFrame", "search"))

    def search_table(self, search_text):
        """
        Searches the table for the given search text and displays the matching results.
        """
        # Get the search text from the lineEdit_2
        search_text = search_text.lower()

        # Iterate through the table rows and columns
        for row in range(self.tableWidget_2.rowCount()):
            # Assume the row should be hidden initially
            row_visible = False

            for col in range(self.tableWidget_2.columnCount()):
                # Get the item at the current row and column
                item = self.tableWidget_2.item(row, col)
                if item:
                    # Convert the item text to lowercase for case-insensitive search
                    item_text = item.text().lower()
                    # Check if the search text is in the item text
                    if search_text in item_text:
                        # If the search text is found in any cell, the row should be visible
                        row_visible = True
                        break  # No need to check other cells in this row

            # Set the row visibility based on whether the search text was found
            self.tableWidget_2.setRowHidden(row, not row_visible)