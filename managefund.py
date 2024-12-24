from PyQt6 import QtCore, QtGui, QtWidgets
from addfunds import *
from withdrawl import *
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QPushButton, QHBoxLayout, QWidget
import sqlite3  # Changed from mysql.connector to sqlite3
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_managefund(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(925, 548)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 59))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 58))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
"background:none;\n"
"font: 700 20pt \"Verdana\";\n"
"color:#653C87;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setStyleSheet("QFrame{\n"
"border: 2px solid #000;  /* Adds a 2px solid black border */\n"
"    border-radius: 0px;     /* Optional: Adds rounded corners */\n"
"    background-color: #9A79BA;  /* Optional: Adds a background color */\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 51))
        self.lineEdit.setStyleSheet("QLabel {\n"
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
"    font-size: 20px; /* Font size */\n"
"    transition: all 0.3s ease; /* Smooth transition */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: gray; /* Darker green border on focus */\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 1px solid #888888; /* Green border for the table */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    background-color: #f0f0f0; /* Light grey background */\n"
"    font-family: \'Arial\', sans-serif; /* Font for the table cells */\n"
"    font-size: 17px; /* Font size for the table cells */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid #888888; /* Grey border for each cell */\n"
"    padding: 5px; /* Padding inside each cell */\n"
"    margin: px; /* Margin between cells */\n"
"    font-family: \'Arial\', sans-serif; /* Font for the table cells */\n"
"    font-size: 14px; /* Font size for the table cells */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #757575; /* Green header background */\n"
"    color: white; /* White text in the header */\n"
"    padding: 4px; /* Padding in header cells */\n"
"    border: 1px solid #dddddd; /* Border for header cells */\n"
"    font-family: \'Verdana\', sans-serif; /* Font for the header */\n"
"    font-size: 16px; /* Font size for the header */\n"
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(171)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.lineEdit.textChanged.connect(self.search_table)
        self.lineEdit.setPlaceholderText("Search")

        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.display1()  # Populate the table

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setWhatsThis(_translate("Frame", "<html><head/><body><p>sa</p></body></html>"))
        self.label_4.setText(_translate("Frame", "Manage funds"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Frame", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "funds"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "action"))

    def display1(self):
        """
        This function fetches data from the database and populates the tableWidget.
        It fetches data from a sample 'funds' table in the database and adds the 'Add' and 'Withdrawal' buttons.
        """
        try:
            # Connect to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
            cursor = con.cursor()

            # Execute the SELECT query and fetch the data
            cursor.execute("SELECT id, username, funds FROM funds")
            rows = cursor.fetchall()

            # Clear existing rows in the table
            self.tableWidget.setRowCount(0)

            # Populate rows with data
            for row_data in rows:
                new_row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(new_row_position)

                # Insert data into the first three columns (id, username, funds)
                for column, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(new_row_position, column, item)

                # Add "Add" and "Withdrawal" buttons in the action column
                action_widget = QWidget()
                action_layout = QHBoxLayout(action_widget)
                action_layout.setContentsMargins(0, 0, 0, 0)  # No margins
                action_layout.setSpacing(10)  # Space between buttons

                # Set the action_widget background to transparent
                action_widget.setStyleSheet("background: transparent;")

                # Create buttons
                add_button = QPushButton("Add")
                withdrawal_button = QPushButton("Withdrawal")

                # Set fixed width for the buttons to reduce their size
                add_button.setFixedWidth(100)  # Adjust this width value as needed
                withdrawal_button.setFixedWidth(100)  # Adjust this width value as needed

                # Connect the buttons to their functions
                add_button.clicked.connect(lambda _, row=new_row_position: self.on_add_clicked(row))
                withdrawal_button.clicked.connect(lambda _, row=new_row_position: self.on_withdrawal_clicked(row))

                # Set styles for buttons
                add_button.setStyleSheet(
                    "QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 0px; font-weight: bold; height:30px; }")
                withdrawal_button.setStyleSheet(
                    "QPushButton { background-color: #f44336; color: white; border-radius: 5px; padding: 0px; font-weight: bold;height:30px; }")

                # Add buttons to the layout
                action_layout.addWidget(add_button)
                action_layout.addWidget(withdrawal_button)

                # Add the action widget (containing buttons) to the last column
                self.tableWidget.setCellWidget(new_row_position, 3, action_widget)

        except sqlite3.Error as e:  # Changed to sqlite3.Error
            print(f"Error executing the query: {e}")

        finally:
            # Close the database connection
            if con:
                cursor.close()
                con.close()

    def on_add_clicked(self, row):
        user_id = self.tableWidget.item(row, 0).text()  # Get 'id' from the first column
        print(f"Add clicked for user ID: {user_id}")
        layout = self.frame.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_add()
        self.ui_content.setupUi(self.content_widget,user_id)

        # Set layout if not already set
        if not self.frame.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame)
            self.frame.setLayout(self.frame_6_layout)
        self.frame.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statement

    def on_withdrawal_clicked(self, row):
        """
        This method is triggered when the 'Withdrawal' button is clicked.
        It will print the ID of the selected user.
        """
        user_id = self.tableWidget.item(row, 0).text()  # Get 'id' from the first column
        print(f"Withdrawal clicked for user ID: {user_id}")
        # Further action (like updating the user's funds) can be added here.
        user_id = self.tableWidget.item(row, 0).text()  # Get 'id' from the first column
        print(f"Add clicked for user ID: {user_id}")
        layout = self.frame.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_Withraw()
        self.ui_content.setupUi(self.content_widget,user_id)

        # Set layout if not already set
        if not self.frame.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame)
            self.frame.setLayout(self.frame_6_layout)
        self.frame.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statement

    def search_table(self, search_text):
        """
        Searches the table for the given search text and displays the matching results.
        """
        # Get the search text from the lineEdit_2
        search_text = search_text.lower()

        # Iterate through the table rows and columns
        for row in range(self.tableWidget.rowCount()):
            # Assume the row should be hidden initially
            row_visible = False

            for col in range(self.tableWidget.columnCount()):
                # Get the item at the current row and column
                item = self.tableWidget.item(row, col)
                if item:
                    # Convert the item text to lowercase for case-insensitive search
                    item_text = item.text().lower()
                    # Check if the search text is in the item text
                    if search_text in item_text:
                        # If the search text is found in any cell, the row should be visible
                        row_visible = True
                        break  # No need to check other cells in this row

            # Set the row visibility based on whether the search text was found
            self.tableWidget.setRowHidden(row, not row_visible)