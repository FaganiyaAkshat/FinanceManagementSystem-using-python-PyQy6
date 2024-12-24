import os
import sqlite3 as sqlite
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import decimal
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Database connection details

class Ui_add(object):
    id_user = None

    def setupUi(self, withdrawlFrame, user_id):
        Ui_add.id_user = user_id
        withdrawlFrame.setObjectName("withdrawlFrame")
        withdrawlFrame.resize(1007, 699)
        self.horizontalLayout = QtWidgets.QHBoxLayout(withdrawlFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.onewidget = QtWidgets.QWidget(parent=withdrawlFrame)
        self.onewidget.setMinimumSize(QtCore.QSize(0, 0))
        self.onewidget.setStyleSheet("#onewidget{border:0px solid black;\n"
                                      "border-radius:0px;\n"
                                      "background:}\n"
                                      "QFrame:addmember{\n"
                                      "border:none;\n"
                                      "  background-color: #E6D7FA;\n"
                                      "}\n"
                                      "QLabel {\n"
                                      "    background-color: #E6D7FA;\n"
                                      "    color: #653C87;\n"
                                      "    font-family: 'Segoe UI', sans-serif;\n"
                                      "    font-size: 16px;\n"
                                      "    font-weight: 600;\n"
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
                                      "    font-size: 20px;\n"
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
        self.onewidget.setObjectName("onewidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.onewidget)
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.onewidget)
        self.widget_2.setMaximumSize(QtCore.QSize(370, 425))
        self.widget_2.setStyleSheet("#widget_2{\n"
                                     "border:2px solid black;\n"
                                     "border-radius:35px;\n"
                                     "    background-color: #E6D7FA;\n"
                                     "}\n"
                                     "QLabel{\n"
                                     " color: #653C87;\n"
                                     "    font-family: 'Segoe UI', sans-serif;\n"
                                     "    font-size: 20px;\n"
                                     "    font-weight: 600;\n"
                                     "border-radius:50px;\n"
                                     "}\n"
                                     "QLineEdit {\n"
                                     "    border: 2px solid #9A79BA;\n"
                                     "    border-radius: 10px;\n"
                                     "    padding: 8px;\n"
                                     "    font-family: 'Segoe UI', sans-serif;\n"
                                     "    font-size: 20px;\n"
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
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 56))
        self.frame_5.setStyleSheet("QFrame{\n"
                                    " border-radius:25px;\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_6.setStyleSheet("QFrame{\n"
                                    "border:none;\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 44))
        self.frame_7.setStyleSheet("QFrame{\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_14.setMinimumSize(QtCore.QSize(119, 0))
        self.label_14.setMaximumSize(QtCore.QSize(150, 24))
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.verticalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 66))
        self.frame_8.setStyleSheet("QFrame{\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_9.setStyleSheet("  background-color: #E6D7FA;\n"
                                    "")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_9)
        self.pushButton_2.setMaximumSize(QtCore.QSize(142, 16777215))
        self.pushButton_2.clicked.connect(self.add_fund)
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
        self.verticalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.frame_9, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setStyleSheet("color:red;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.onewidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(370, 425))
        self.widget_3.setStyleSheet("#widget_3{\n"
                                     "border:2px solid black;\n"
                                     "border-radius:35px;\n"
                                     "    background-color: #E6D7FA;\n"
                                     "}\n"
                                     "QLabel{\n"
                                     " color: #653C87;\n"
                                     "    font-family: 'Segoe UI', sans-serif;\n"
                                     "    font-size: 30px;\n"
                                     "    font-weight: 600;\n"
                                     "border-radius:0px;\n"
                                     "}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 184))
        self.frame_2.setStyleSheet("QFrame{\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 112))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_4.setMaximumSize(QtCore.QSize(264, 128))
        self.frame_4.setStyleSheet("QFrame{\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 112))
        self.label_2.setStyleSheet(" color: #653C87;\n"
                                    "    font-family: 'Segoe UI', sans-serif;\n"
                                    "    font-size: 20px;\n"
                                    "    font-weight: 600;\n"
                                    "border-radius:50px;\n"
                                    "")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 242))
        self.frame_3.setStyleSheet("QFrame{\n"
                                    "  background-color: #E6D7FA;\n"
                                    "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.onewidget)

        self.retranslateUi(withdrawlFrame)
        QtCore.QMetaObject.connectSlotsByName(withdrawlFrame)

    def retranslateUi(self, withdrawlFrame):
        _translate = QtCore.QCoreApplication.translate
        withdrawlFrame.setWindowTitle(_translate("withdrawlFrame", "Frame"))
        self.label_14.setText(_translate("withdrawlFrame", "Amount"))
        self.pushButton_2.setText(_translate("withdrawlFrame", "Fund Add"))
        self.set_text()

    def set_text(self):
        _translate = QtCore.QCoreApplication.translate

        try:
            con = sqlite.connect(resource_path('db/firm_management.db'))  # Connect to SQLite database
            cursor = con.cursor()

            # Check if the user id exists in the table and fetch funds
            cursor.execute("SELECT funds FROM funds WHERE id = ?", (Ui_add.id_user,))
            result = cursor.fetchone()

            if result:
                self.label.setText(_translate("withdrawlFrame", "Available Balance:\n"
                                                                f"{result[0]}"))
            else:
                self.label.setText(_translate("withdrawlFrame", "No funds available."))

        except Exception as e:
            print(f"Error this is exception: {e}")

        finally:
            if con:
                cursor.close()
                con.close()
                print("SQLite connection is closed")

    def add_fund(self):
        print(Ui_add.id_user)
        amount = self.lineEdit_5.text().strip()

        try:
            con = sqlite.connect(resource_path('db/firm_management.db'))  # Connect to SQLite database
            cursor = con.cursor()

            # Check if the user id exists in the table and fetch funds
            cursor.execute("SELECT funds FROM funds WHERE id = ?", (Ui_add.id_user,))
            result = cursor.fetchone()

            if result is not None:
                current_balance = decimal.Decimal(result[0])  # Convert to Decimal
                amount_to_add = decimal.Decimal(amount)  # Convert to Decimal

                # Convert to float for SQLite compatibility
                current_balance = float(current_balance)
                amount_to_add = float(amount_to_add)

                # Perform the addition with decimals
                balance = current_balance + amount_to_add

                # Update the funds column for the specific user id
                cursor.execute("UPDATE funds SET funds=? WHERE id=?", (balance, Ui_add.id_user))

                # Check if there's a loan associated with the user and update it
                cursor.execute("SELECT amount FROM loan WHERE unique_n = ?", (Ui_add.id_user,))
                result = cursor.fetchone()

                if result is not None:
                    # Calculate the new loan amount
                    new_amount = result[0] - amount_to_add

                    # If the new amount is negative or zero, set it to zero
                    if new_amount <= 0:
                        new_amount = 0

                    # Update the loan record with the adjusted amount
                    cursor.execute("UPDATE loan SET amount = ? WHERE unique_n = ?", (new_amount, Ui_add.id_user))

                # Insert the transaction entry
                entry = (Ui_add.id_user, amount_to_add, 'credit')
                cursor.execute("INSERT INTO entry(u_id, t_amount, t_type) VALUES(?, ?, ?)", entry)

                # Commit the changes to the database
                con.commit()

                # Show success message
                QMessageBox.information(None, 'Success', 'Fund credited successfully')
                self.lineEdit_5.clear()
                self.label_2.setText(f"Credited successfully on your account rupees\n{amount}")
                self.label_2.show()

            else:
                con.rollback()
                QMessageBox.warning(None, 'Validation Error', 'ID does not exist! Invalid ID')

        except Exception as e:
            print(f"Error this is exception: {e}")
            QMessageBox.warning(None, 'Database Error', 'An error occurred while processing the transaction.')

        finally:
            if con:
                cursor.close()
                con.close()
                print("SQLite connection is closed")
                self.set_text()  # Ensure this method is defined elsewhere