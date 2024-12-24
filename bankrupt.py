import os
import sqlite3  # Changed from mysql.connector to sqlite3
import sys

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

class Ui_bank(object):
    def setupUi(self, bank):
        bank.setObjectName("bank")
        bank.resize(901, 631)
        self.gridLayout_8 = QtWidgets.QGridLayout(bank)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_5 = QtWidgets.QFrame(parent=bank)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(44, 0, 70, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setStyleSheet("QFrame:addmember{\n"
"border:none;\n"
"}\n"
"QLabel {\n"
"    background-color: #E6D7FA;\n"
"    color: #653C87;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    padding: 8px;\n"
"    border: 2px solid #653C87;\n"
"    border-radius: 10px;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"QLabel:hover {\n"
"    background-color: #D4C2EF;\n"
"    border-color: #553075;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #9A79BA;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 19px;\n"
"    color: #653C87;\n"
"    background-color: #FFFFFF;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: #F5F0FA;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #653C87;\n"
"    background-color: #F5F5F5;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(-1, 23, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelheading = QtWidgets.QLabel(parent=self.frame_2)
        self.labelheading.setStyleSheet("#labelheading{\n"
"    font: 700 30pt \"Segoe UI\";\n"
"background:none;\n"
"border:none;\n"
"}")
        self.labelheading.setObjectName("labelheading")
        self.gridLayout_3.addWidget(self.labelheading, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_17.setMinimumSize(QtCore.QSize(142, 0))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_6.addWidget(self.lineEdit_14, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_11, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_6.setMinimumSize(QtCore.QSize(142, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_9)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(387, 16777215))
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_7.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_9, 1, 0, 1, 1)
        self.fframe_6 = QtWidgets.QFrame(parent=self.frame_7)
        self.fframe_6.setMinimumSize(QtCore.QSize(0, 0))
        self.fframe_6.setMaximumSize(QtCore.QSize(16777215, 93))
        self.fframe_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fframe_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fframe_6.setObjectName("fframe_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fframe_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.fframe_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #653C87;\n"
"    color: #FFFFFF;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 20px;\n"
"    border: 2px solid #9A79BA;\n"
"    border-radius: 10px;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #9A79BA;\n"
"    border-color: #653C87;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E6D7FA;\n"
"    border-color: #553075;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.in_bankrupt)

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.fframe_6)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.clicked.connect(self.de_bankrupt)

        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #653C87;\n"
"    color: #FFFFFF;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 20px;\n"
"    border: 2px solid #9A79BA;\n"
"    border-radius: 10px;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #9A79BA;\n"
"    border-color: #653C87;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E6D7FA;\n"
"    border-color: #553075;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.fframe_6, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setStyleSheet("QFrame{\n"
"border: 2px solid #000;\n"
"    border-radius: 0px;\n"
"    background-color: #653C87;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_2.setStyleSheet("QLabel {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-family: 'Arial', sans-serif;\n"
"    font-size: 19px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QLabel:hover {\n"
"    background-color: #f0f0f0;\n"
"    border-color: #3e8e41;\n"
"    color: #000000;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-family: 'Arial', sans-serif;\n"
"    font-size: 19px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: gray;\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Search")
        self.lineEdit_2.textChanged.connect(self.search_bank)

        self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame_8)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"    border: 1px solid #888888;\n"
"    border-radius: 10px;\n"
"    background-color: #f0f0f0;\n"
"    font-family: 'Arial', sans-serif;\n"
"    font-size: 18px;\n"
"}\n"
"QTableWidget::item {\n"
"    border: 1px solid #888888;\n"
"    padding: 5px;\n"
"    margin: 1px;\n"
"    font-family: 'Arial', sans-serif;\n"
"    font-size: 18px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #A8A2AB;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border: 1px solid #dddddd;\n"
"    font-family: 'Verdana', sans-serif;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #653C87;\n"
"}\n"
"")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)

        self.retranslateUi(bank)
        QtCore.QMetaObject.connectSlotsByName(bank)

    def search_bank(self, search_text):
        """ Searches the table for the given search text and displays the matching results. """
        search_text = search_text.lower()
        for row in range(self.tableWidget_2.rowCount()):
            row_visible = False
            for col in range(self.tableWidget_2.columnCount()):
                item = self.tableWidget_2.item(row, col)
                if item:
                    item_text = item.text().lower()
                    if search_text in item_text:
                        row_visible = True
                        break
            self.tableWidget_2.setRowHidden(row, not row_visible)

    def retranslateUi(self, bank):
        _translate = QtCore.QCoreApplication.translate
        bank.setWindowTitle(_translate("bank", "Frame"))
        self.labelheading.setText(_translate("bank", "Bankrupt"))
        self.label_17.setText(_translate("bank", "Username"))
        self.label_6.setText(_translate("bank", "Aadharnumber"))
        self.pushButton_2.setText(_translate("bank", "Save"))
        self.pushButton_4.setText(_translate("bank", "Delete"))
        self.lineEdit_2.setText(_translate("bank", ""))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("bank", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("bank", "username"))
        self.display2()

    def display2(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            con = sqlite3.connect(resource_path('db/firm_management.db'))
            cursor = con.cursor()
            cursor.execute("SELECT username, aadhar FROM bankrupt")
            rows = cursor.fetchall()
            self.tableWidget_2.setRowCount(0)
            for row_data in rows:
                new_row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(new_row_position)
                for column, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget_2.setItem(new_row_position, column, item)
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if con:
                cursor.close()
                con.close()

    def in_bankrupt(self):
        try:
            con = sqlite3.connect(resource_path('db/firm_management.db'))
            cursor = con.cursor()
            name = self.lineEdit_14.text().strip()
            a_number = self.lineEdit_4.text().strip()

            if len(a_number) != 12 or not a_number.isdigit():
                QMessageBox.warning(None, 'Invalid Input', 'Aadhar number must be 12 digits long.')
                return

            cursor.execute("SELECT COUNT(*) FROM addmember WHERE aadhar = ?", (a_number,))
            exists = cursor.fetchone()[0]

            if exists == 0:
                QMessageBox.warning(None, 'Not a Member', 'The Aadhar number does not exist in the addmember table.')
                return

            sql_insert_query = """INSERT INTO bankrupt (username, aadhar, fund) VALUES (?, ?, ?)"""
            data_tuple = (name, a_number, 0)
            cursor.execute(sql_insert_query, data_tuple)

            cursor.execute("SELECT userid FROM addmember WHERE aadhar = ?", (a_number,))
            result = cursor.fetchone()
            if result:
                unique_id = result[0]
                cursor.execute("DELETE FROM addmember WHERE aadhar = ?", (a_number,))
                cursor.execute("DELETE FROM entry WHERE u_id = ?", (unique_id,))
                cursor.execute("DELETE FROM funds WHERE id = ?", (unique_id,))
                cursor.execute("SELECT * FROM loan WHERE unique_n = ?", (unique_id,))
                loan_record = cursor.fetchone()
                if loan_record:
                    cursor.execute("DELETE FROM loan WHERE unique_n = ?", (unique_id,))
                    cursor.execute("INSERT INTO bad_dept (name, amount) VALUES (?, ?)", (loan_record[2], loan_record[3]))
                con.commit()
                QMessageBox.information(None, 'Success', 'Record of user successfully in bankruptcy.')
            else:
                print("No matching record found in addmember.")

            self.display2()
            self.lineEdit_14.clear()
            self.lineEdit_4.clear()
            self.display2()
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            QMessageBox.critical(None, 'Database Error', 'An error occurred while accessing the database.')
        except Exception as e:
            print(f"Unexpected Error: {e}")
            QMessageBox.critical(None, 'Unexpected Error', f'An unexpected error occurred: {e}')
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'con' in locals() and con:
                con.close()
                print("SQLite connection is closed")

    def de_bankrupt(self):
        try:
            con = sqlite3.connect(resource_path('db/firm_management.db'))
            cursor = con.cursor()
            a_number = self.lineEdit_4.text().strip()

            if len(a_number) != 12 or not a_number.isdigit():
                QMessageBox.warning(None, 'Invalid Input', 'Aadhar number must be 12 digits long.')
                return

            cursor.execute("SELECT COUNT(*) FROM bankrupt WHERE aadhar = ?", (a_number,))
            exists = cursor.fetchone()[0]

            if exists == 0:
                QMessageBox.warning(None, 'Not Found', 'The Aadhar number does not exist in the bankrupt table.')
                return

            cursor.execute("DELETE FROM bankrupt WHERE aadhar = ?", (a_number,))
            con.commit()
            QMessageBox.information(None, 'Success', 'Record deleted from bankrupt successfully.')
            self.display2()
            self.lineEdit_4.clear()

        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            QMessageBox.critical(None, 'Database Error', 'An error occurred while accessing the database.')
        except Exception as e:
            print(f"Unexpected Error: {e}")
            QMessageBox.critical(None, 'Unexpected Error', f'An unexpected error occurred: {e}')
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'con' in locals() and con:
                con.close()
                print("SQLite connection is closed")