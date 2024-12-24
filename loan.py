import os
import random
import sqlite3  # Changed from mysql.connector to sqlite3
import sys
from random import randint
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_Framloan(object):
    def setupUi(self, Framloan):
        Framloan.setObjectName("Framloan")
        Framloan.resize(916, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Framloan.sizePolicy().hasHeightForWidth())
        Framloan.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtWidgets.QGridLayout(Framloan)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(parent=Framloan)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("QFrame:addmember{\n"
"border:none;\n"
"}\n"
"#frame{\n"
"border:2px solid gray;\n"
"border-radius:20px;\n"
"}\n"
"QLabel {\n"
"\n"
"    background-color: #E6D7FA;\n"
"    color: #653C87;\n"
"    font-family: \'Segoe UI\', sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    padding: 8px;\n"
"    border: 2px solid #653C87;\n"
"    border-radius: 10px;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #D4C2EF;  /* Slightly darker background on hover */\n"
"    border-color: #553075;  /* Darker border on hover */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #9A79BA;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \'Segoe UI\', sans-serif;\n"
"    font-size: 19px;\n"
"    color: #653C87;\n"
"    background-color: #FFFFFF;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #F5F0FA;  /* Slightly lighter background on hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #653C87;  /* Darker border on focus */\n"
"    background-color: #F5F5F5;  /* Slightly lighter background on focus */\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 54))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 58))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
"background:none;\n"
"font: 700 20pt \"Verdana\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setHorizontalSpacing(51)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton_2.clicked.connect(self.show_field)

        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #653C87; /* Dark purple background */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-family: \'Segoe UI\', sans-serif; /* Font family */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border: 2px solid #9A79BA; /* Light purple border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9A79BA; /* Light purple background on hover */\n"
"    border-color: #653C87; /* Dark purple border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E6D7FA; /* Lightest purple background on press */\n"
"    border-color: #553075; /* Darker purple border on press */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3.setMaximumSize(QtCore.QSize(121, 16777215))
        self.pushButton_3.clicked.connect(self.bad_debt)

        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #653C87; /* Dark purple background */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-family: \'Segoe UI\', sans-serif; /* Font family */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border: 2px solid #9A79BA; /* Light purple border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9A79BA; /* Light purple background on hover */\n"
"    border-color: #653C87; /* Dark purple border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E6D7FA; /* Lightest purple background on press */\n"
"    border-color: #553075; /* Darker purple border on press */\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_4.setMaximumSize(QtCore.QSize(92, 16777215))
        self.pushButton_4.clicked.connect(self.give_loan)

        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #653C87; /* Dark purple background */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-family: \'Segoe UI\', sans-serif; /* Font family */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border: 2px solid #9A79BA; /* Light purple border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9A79BA; /* Light purple background on hover */\n"
"    border-color: #653C87; /* Dark purple border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E6D7FA; /* Lightest purple background on press */\n"
"    border-color: #553075; /* Darker purple border on press */\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(1000, 380))
        self.frame_8.setStyleSheet("QFrame{\n"
"border: 2px solid #000;  /* Adds a 2px solid black border */\n"
"    border-radius: 0px;     /* Optional: Adds rounded corners */\n"
"    background-color: #9A79BA;  /* Optional: Adds a background color */\n"
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

        self.lineEdit_2.setStyleSheet("QLabel {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid black; /* Green border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 10px; /* Padding */\n"
"    font-family: \'Arial\', sans-serif; /* Font family */\n"
"    font-size: 14px; /* Font size */\n"
"    transition: all 0.3s ease; /* Smooth transition for hover effect */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #f0f0f0; /* Light grey background on hover */\n"
"    border-color: #3e8e41; /* Darker green border on hover */\n"
"    color: #000000; /* Black text color on hover */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid black; /* Green border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 10px; /* Padding */\n"
"    font-family: \'Arial\', sans-serif; /* Font family */\n"
"    font-size: 19px; /* Font size */\n"
"    transition: all 0.3s ease; /* Smooth transition */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: gray; /* Darker green border on focus */\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"    border: 1px solid #888888; /* Green border for the table */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    background-color: #f0f0f0; /* Light grey background */\n"
"    font-family: \'Arial\', sans-serif; /* Font for the table cells */\n"
"    font-size: 18px; /* Font size for the table cells */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid #888888; /* Grey border for each cell */\n"
"    padding: 5px; /* Padding inside each cell */\n"
"    margin: px; /* Margin between cells */\n"
"    font-family: \'Arial\', sans-serif; /* Font for the table cells */\n"
"    font-size: 18px; /* Font size for the table cells */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #757575; /* Green header background */\n"
"    color: white; /* White text in the header */\n"
"    padding: 4px; /* Padding in header cells */\n"
"    border: 1px solid #dddddd; /* Border for header cells */\n"
"    font-family: \'Verdana\', sans-serif; /* Font for the header */\n"
"    font-size: 18px; /* Font size for the header */\n"
"    font-weight: bold; /* Bold font for the header */\n"
"\n"
"}\n"
"            QScrollBar:vertical {\n"
"                \n"
"                background: #653C87;\n"
"                \n"
"         \n"
"            }\n"
"\n"
"")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(102)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(22)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Framloan)
        QtCore.QMetaObject.connectSlotsByName(Framloan)

    def retranslateUi(self, Framloan):
        _translate = QtCore.QCoreApplication.translate
        Framloan.setWindowTitle(_translate("Framloan", "Frame"))
        self.label_4.setText(_translate("Framloan", "Loan"))
        self.pushButton_2.setText(_translate("Framloan", "loan approved"))
        self.pushButton_3.setText(_translate("Framloan", "bad debt"))
        self.label_5.setText(_translate("Framloan", "Name"))
        self.label_6.setText(_translate("Framloan", "Amount"))
        self.pushButton_4.setText(_translate("Framloan", "Submit"))
        self.lineEdit_2.setText(_translate("Framloan", ""))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Framloan", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Framloan", "name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Framloan", "amount"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Framloan", "date"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Framloan", "action"))
        self.fetch_data()  # Call fetch_data to populate the table on UI load

        self.frame_4.hide()

    def receive_payment(self, unique_id):
        # Function to handle receiving payment
        print(f"Receive payment for record with ID: {unique_id}")
        # Implement your logic here

    def fetch_data(self):
        try:
            # Establish a connection to the SQLite database
            connection = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite
            cursor = connection.cursor()

            # Query to fetch data from the loan table
            query = "SELECT unique_n, name, amount, date FROM loan"
            cursor.execute(query)

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Set the number of rows in the table widget
            self.tableWidget_2.setRowCount(len(rows))

            # Set a fixed height for the rows
            for row_index in range(len(rows)):
                self.tableWidget_2.setRowHeight(row_index, 50)  # Set the same height for all rows

            # Populate the table with data
            for row_index, row_data in enumerate(rows):
                for column_index, column_data in enumerate(row_data):
                    # Add data to the table widget
                    self.tableWidget_2.setItem(
                        row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data))
                    )

                # Create a layout for the action buttons
                action_layout = QtWidgets.QHBoxLayout()
                action_layout.addStretch()  # Add stretch to left side

                # Create the Delete button
                delete_button = QtWidgets.QPushButton("Delete")
                delete_button.setFixedSize(80, 25)  # Set the desired width and reduced height (in pixels)
                delete_button.setStyleSheet(
                    "background-color: #DC143C; color: white; border-radius: 5px; padding: 5px;")
                delete_button.clicked.connect(lambda checked, row=row_data[0]: self.delete_record(row))
                action_layout.addWidget(delete_button)  # Add delete button to layout

                # Check if unique_n exists in the admemerb table's userid column
                check_query = "SELECT COUNT(*) FROM addmember WHERE userid = ?"
                cursor.execute(check_query, (row_data[0],))
                exists = cursor.fetchone()[0] > 0  # Fetch the count and check if it's greater than 0

                # Create the Receive Payment button only if unique_n is not in admemerb
                if not exists:
                    receive_button = QtWidgets.QPushButton("Receive")
                    receive_button.setFixedSize(80, 25)  # Set the desired width and reduced height (in pixels)
                    receive_button.setStyleSheet(
                        "background-color: #32CD32; color: white; border-radius: 5px; padding: 5px;")
                    receive_button.clicked.connect(lambda checked, row=row_data[0]: self.receive_payment(row))
                    action_layout.addWidget(receive_button)  # Add receive payment button to layout

                action_layout.addStretch()  # Add stretch to right side

                # Set the action layout as a cell widget in the action column (index 4)
                action_widget = QtWidgets.QWidget()
                action_widget.setStyleSheet("background: transparent;")  # Make the background transparent
                action_widget.setLayout(action_layout)
                self.tableWidget_2.setCellWidget(row_index, 4, action_widget)

            # Close the connection
            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error: {e}")

    def receive_payment(self, unique_id):
        try:
            # Show a confirmation dialog
            reply = QtWidgets.QMessageBox.question(
                None,
                "Confirm Action",
                f"Are you sure you want to mark the payment as received for record ID: {unique_id}?",
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )

            # Proceed only if the user confirms
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                # Connect to the SQLite database
                connection = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite
                cursor = connection.cursor()

                # Update the `amount` field to 0 for the given `unique_id`
                update_query = "UPDATE loan SET amount = 0 WHERE unique_n = ?"
                cursor.execute(update_query, (unique_id,))
                connection.commit()  # Save changes to the database

                # Notify the user
                QtWidgets.QMessageBox.information(None, "Success",
                                                  f"Payment received for record ID: {unique_id}. Amount set to 0.")

                # Refresh the table data
                self.fetch_data()

                # Close the database connection
                cursor.close()
                connection.close()
            else:
                pass
        except Exception as e:
            # Handle exceptions and notify the user
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to update record: {e}")

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

    def give_loan(self):
        try:
            # Hide frame_4 and show frame_8
            self.frame_4.hide()
            self.frame_8.show()

            # Get user input for amount and name
            amount = self.lineEdit.text()
            name = self.lineEdit_3.text()
            if not name:
                QMessageBox.warning(None, 'Validation Error', 'Name should not be empty')
                return
            if not amount:
                QMessageBox.warning(None, 'Validation Error', 'Amount should not be empty')
                return
            # Generate a unique 6-digit random number
            unique_id = str(random.randint(100000, 999999))

            # Connect to the SQLite database
            connection = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite
            cursor = connection.cursor()

            # Check if the unique_id already exists in the loan table
            cursor.execute("SELECT COUNT(*) FROM loan WHERE unique_n = ?", (unique_id,))
            count = cursor.fetchone()[0]

            # If unique_id already exists, generate a new one
            while count > 0:
                unique_id = str(random.randint(100000, 999999))
                cursor.execute("SELECT COUNT(*) FROM loan WHERE unique_n = ?", (unique_id,))
                count = cursor.fetchone()[0]

            # Caution message before insertion
            reply = QMessageBox.question(None, 'Caution',
                                         f"Are you sure you want to pass the loan statement?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                # Insert the loan record into the database without the date field
                query = """INSERT INTO loan (unique_n, name, amount) 
                           VALUES (?, ?, ?)"""
                cursor.execute(query, (unique_id, name, amount))
                connection.commit()

                # Show success message
                QMessageBox.information(None, 'Success', 'Loan record has been successfully inserted!')
            else:
                pass
            # Close the connection
            cursor.close()

        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.critical(None, 'Error', 'An error occurred while processing the loan record.')
        self.lineEdit_3.clear()
        self.lineEdit.clear()
        # Show frame_4 and hide frame_8
        self.frame_4.hide()
        self.frame_8.show()
        self.fetch_data()

    def show_field(self):
        try:
            self.frame_4.show()
            self.frame_8.hide()
        except Exception as e:
            print(f"Error: {e}")

    def bad_debt(self):
        """
        This function deletes the entire column from tableWidget_2
        and adds new columns for name, amount, and date.
        """
        try:
            # Clear the existing table
            self.tableWidget_2.setRowCount(0)  # Clear all rows
            self.tableWidget_2.setColumnCount(0)  # Clear all columns

            # Set up new columns
            self.tableWidget_2.setColumnCount(3)  # Set to 3 columns
            self.tableWidget_2.setHorizontalHeaderLabels(["Name", "Amount", "Date"])  # Set new headers

            # Connect to the SQLite database
            connection = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite
            cursor = connection.cursor()

            # Query to fetch data from the bad_debt table
            query = "SELECT name, amount, date FROM bad_dept"
            cursor.execute(query)

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Set the number of rows in the table widget
            self.tableWidget_2.setRowCount(len(rows))

            # Populate the table with data
            for row_index, row_data in enumerate(rows):
                for column_index, column_data in enumerate(row_data):
                    # Add data to the table widget
                    self.tableWidget_2.setItem(
                        row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data))
                    )

            # Close the connection
            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error: {e}")

    def delete_record(self, unique_id):
        try:
            # Establish a connection to the SQLite database
            connection = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite
            cursor = connection.cursor()

            # Fetch the name and amount associated with the unique_id
            query_fetch = "SELECT name, amount FROM loan WHERE unique_n = ?"
            cursor.execute(query_fetch, (unique_id,))
            loan_record = cursor.fetchone()  # Fetch the single result row

            if loan_record:
                name, amount = loan_record  # Unpack the result

                # Check if the amount is greater than 0
                if float(amount) > 0:
                    # Prompt the user with a caution message
                    reply = QMessageBox.question(
                        None,
                        'Caution',
                        f"The amount for this record is {amount}. Do you want to add this record to the bad debt?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                        QMessageBox.StandardButton.No
                    )

                    if reply == QMessageBox.StandardButton.Yes:
                        # Insert the record into the bad_debt table
                        query_insert_bad_debt = "INSERT INTO bad_dept (name, amount) VALUES (?, ?)"
                        cursor.execute(query_insert_bad_debt, (name, amount))

                        # Fetch the aadhar number associated with the user ID
                        query_fetch_aadhar = "SELECT aadhar FROM addmember WHERE userid = ?"
                        cursor.execute(query_fetch_aadhar, (unique_id,))
                        aadhar_result = cursor.fetchone()

                        if aadhar_result:
                            aadhar_number = aadhar_result[0]

                            # Insert into the bankrupt table
                            query_insert_bankrupt = "INSERT INTO bankrupt (username, aadhar, fund) VALUES (?, ?, ?)"
                            cursor.execute(query_insert_bankrupt, (name, aadhar_number, amount))

                        # Delete the record from the loan table
                        query_delete_loan = "DELETE FROM loan WHERE unique_n = ?"
                        cursor.execute(query_delete_loan, (unique_id,))

                        # Delete the associated entries in other tables
                        query_delete_entry = "DELETE FROM entry WHERE u_id = ?"
                        cursor.execute(query_delete_entry, (unique_id,))

                        query_delete_funds = "DELETE FROM funds WHERE id = ?"
                        cursor.execute(query_delete_funds, (unique_id,))

                        query_delete_member = "DELETE FROM addmember WHERE userid = ?"
                        cursor.execute(query_delete_member, (unique_id,))

                        # Commit the transaction
                        connection.commit()

                        # Show success message
                        QMessageBox.information(None, 'Success', 'Record has been successfully deleted.')
                    else:
                        connection.rollback()
                        pass
                else:
                    query_delete_loan = "DELETE FROM loan WHERE unique_n = ?"
                    cursor.execute(query_delete_loan, (unique_id,))
                    connection.commit()
                    QMessageBox.warning(None, 'Not Found', 'The record delete successfully.')

            else:
                # Show warning if no record is found
                QMessageBox.warning(None, 'Not Found', 'The record with the given unique ID does not exist.')

        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.critical(None, 'Error', 'An error occurred while deleting the record.')
        finally:
            # Ensure the cursor and connection are properly closed
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection:
                connection.close()

            # Refresh the data in the table
            self.fetch_data()