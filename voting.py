import os
import random
import sys
import urllib
import sqlite3  # Importing sqlite3 instead of mysql.connector
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox
from voting2 import *
from PyQt6 import QtCore, QtGui, QtWidgets

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Ui_wotingFrame(object):
    def setupUi(self, wotingFrame):
        wotingFrame.setObjectName("wotingFrame")
        wotingFrame.resize(881, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(wotingFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=wotingFrame)
        self.frame.setStyleSheet("QFrame:addmember{\n"
"border:none;\n"
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
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
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
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setHorizontalSpacing(51)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(118, 16777215))
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
        self.pushButton_3.setMaximumSize(QtCore.QSize(131, 16777215))
        self.pushButton_3.clicked.connect(self.start_v2)

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
        self.frame_4.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_4.setMaximumSize(QtCore.QSize(92, 16777215))
        self.pushButton_4.clicked.connect(self.in_vote)
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
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame_4)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.dateEdit.setStyleSheet("QDateEdit {\n"
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
"QDateEdit:hover {\n"
"    background-color: #F5F0FA;  /* Slightly lighter background on hover */\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #653C87;  /* Darker border on focus */\n"
"    background-color: #F5F5F5;  /* Slightly lighter background on focus */\n"
"}")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(178878, 380))
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

        self.lineEdit_2.setStyleSheet("QLabel {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid black; /* Green border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 10px; /* Padding */\n"
"    font-family: \'Arial\', sans-serif; /* Font family */\n"
"    font-size: 18px; /* Font size */\n"
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
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(102)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(22)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(wotingFrame)
        QtCore.QMetaObject.connectSlotsByName(wotingFrame)

    def retranslateUi(self, wotingFrame):
        _translate = QtCore.QCoreApplication.translate
        wotingFrame.setWindowTitle(_translate("wotingFrame", "Frame"))
        self.label_4.setText(_translate("wotingFrame", "Voting"))
        self.pushButton_2.setText(_translate("wotingFrame", "Add voting"))
        self.pushButton_3.setText(_translate("wotingFrame", "Start Voting"))
        self.label_6.setText(_translate("wotingFrame", "Date of Voting"))
        self.label_5.setText(_translate("wotingFrame", "Subject of Voting"))
        self.pushButton_4.setText(_translate("wotingFrame", "Submit"))
        self.lineEdit_2.setText(_translate("wotingFrame", ""))
        self.lineEdit_2.setPlaceholderText("Search")
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("wotingFrame", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("wotingFrame", "subject of voting"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("wotingFrame", "date of voting"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("wotingFrame", "yes"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("wotingFrame", "no"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("wotingFrame", "cnd"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.display1()
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.frame_4.hide()

    def display1(self):
        """
        This function fetches data from the SQLite database and populates the tableWidget.
        It first connects to the database, executes a SELECT query to fetch the columns from the voting table,
        and then adds the data to the tableWidget.
        """
        try:
            # Connect to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()

            # Execute the SELECT query and fetch the data
            cursor.execute("SELECT * FROM voting")
            rows = cursor.fetchall()

            # Clear existing rows in the tableWidget
            self.tableWidget_2.setRowCount(0)

            # Set column headers
            headers = ["id", "subject of voting", "date of voting", "yes", "no", "cnd"]
            self.tableWidget_2.setColumnCount(len(headers))
            self.tableWidget_2.setHorizontalHeaderLabels(headers)

            # Add rows and populate them with data
            for row_data in rows:
                new_row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(new_row_position)
                for column, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget_2.setItem(new_row_position, column, item)

        except sqlite3.Error as e:
            print(f"Error display1: {e}")

        finally:
            # Close the database connection
            if con:
                con.close()

    def start_v2(self):
        try:
            if self.is_internet_connected():
                # Clear existing layout in frame_6
                try:
                    layout = self.frame.layout()
                    if layout is not None:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                child.widget().deleteLater()

                    # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
                    self.content_widget = QtWidgets.QWidget()
                    self.ui_content = Ui_Frame_voting2()
                    self.ui_content.setupUi(self.content_widget)

                    # Set layout if not already set
                    if not self.frame.layout():
                        self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame)
                        self.frame.setLayout(self.frame_6_layout)
                    self.frame.layout().addWidget(self.content_widget)
                except sqlite3.Error as e:
                    print(f"Error start_v2: {e}")
                print("Content added to vote")  # Debugging print statement
            else:
                QMessageBox.warning(None, 'Validation Error', 'Check internet connection')
        except sqlite3.Error as e:
            print(f"Error start_v2: {e}")

    def show_field(self):
        self.frame_4.show()
        self.frame_8.hide()

    def in_vote(self):
        try:
            # Connect to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()
            sub = self.lineEdit_3.text().strip()
            date = self.dateEdit.date().toString('yyyy-MM-dd')
            while True:
                five_digit_number = random.randint(10000, 99999)
                cursor.execute("SELECT COUNT(*) FROM voting WHERE id = ?", (five_digit_number,))
                result = cursor.fetchone()
                if result[0] == 0:
                    random_number = five_digit_number
                    break
            if not sub:
                QMessageBox.warning(None, 'Validation Error', 'Subject should not be empty')
                return
            # Validate the date
            if not date or date == '0000-00-00':
                QMessageBox.warning(None, 'Invalid Date', 'Please select a valid date.')
                return

            insert_query = """
                        INSERT INTO voting (id, subject, date)
                        VALUES (?, ?, ?)
                        """
            record = (random_number, sub, date)
            cursor.execute(insert_query, record)

            # Commit the transaction
            con.commit()

            # Display success message box
            QMessageBox.information(None, 'Success', 'Record inserted successfully')
            self.display1()
        except sqlite3.Error as e:
            print(f"Error in_vote: {e}")

        finally:
            # Close the database connection
            if con:
                con.close()
        self.frame_4.hide()
        self.frame_8.show()

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

    def is_internet_connected(self):
        """
        Checks if the user's device is connected to the internet.

        Returns:
            bool: True if the device is connected to the internet, False otherwise.
        """
        try:
            # Try to fetch a known website to check the internet connection
            urllib.request.urlopen('https://www.google.com', timeout=5)
            return True
        except urllib.request.URLError:
            print("is internet Connect")
            return False