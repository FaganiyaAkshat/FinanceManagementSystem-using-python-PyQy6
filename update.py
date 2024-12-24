# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import sqlite3  # Importing sqlite3 instead of mysql.connector
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_update(object):
    name = None  # Initialize the 'name' attribute
    age = None

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(845, 592)
        Frame.setStyleSheet("QFrame{\n"
                            " border:none;\n"
                            "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Frame)
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
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
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
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(142, 16777215))
        self.pushButton_2.clicked.connect(self.update2)  # Connect button click to method

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
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_8.setStyleSheet("QLabel {\n"
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
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_7.setMinimumSize(QtCore.QSize(142, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_14.setMinimumSize(QtCore.QSize(142, 0))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.frame_9)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_9.addWidget(self.lineEdit_11)
        self.label_15 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_15.setMinimumSize(QtCore.QSize(142, 0))
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.frame_9)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_9.addWidget(self.lineEdit_12)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_16.setMinimumSize(QtCore.QSize(142, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout.addWidget(self.lineEdit_13)
        self.label_18 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_18.setMinimumSize(QtCore.QSize(142, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout.addWidget(self.lineEdit_15)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_111 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_111.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_111.setStyleSheet("#frame_111\n"
                                     "{\n"
                                     "border:none;\n"
                                     "}")
        self.frame_111.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_111.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_111.setObjectName("frame_111")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_111)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_66 = QtWidgets.QFrame(parent=self.frame_111)
        self.frame_66.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_66)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(parent=self.frame_66)
        self.label_19.setMinimumSize(QtCore.QSize(142, 0))
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.lineEdit_16 = QtWidgets.QLineEdit(parent=self.frame_66)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_5.addWidget(self.lineEdit_16)
        self.horizontalLayout_2.addWidget(self.frame_66)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_111)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_3.setMaximumSize(QtCore.QSize(142, 16777215))
        self.pushButton_3.clicked.connect(self.u_up)  # Connect button click to method

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
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_5.addWidget(self.frame_111)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Update "))
        self.label_5.setText(_translate("Frame", "Enter Client Id"))
        self.pushButton_2.setText(_translate("Frame", "Submit"))
        self.label_6.setText(_translate("Frame", "Aadhar number"))
        self.label_7.setText(_translate("Frame", "Mobile number"))
        self.label_14.setText(_translate("Frame", "Email"))
        self.label_15.setText(_translate("Frame", "Username"))
        self.label_16.setText(_translate("Frame", "City"))
        self.label_18.setText(_translate("Frame", "Nominy name"))
        self.label_19.setText(_translate("Frame", "Nominy Aadhar"))
        self.pushButton_3.setText(_translate("Frame", "Save"))
        self.frame_7.hide()

    def update2(self):
        user_id = self.lineEdit_3.text().strip()
        try:
            # Connect to SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()
            cursor.execute("SELECT * FROM addmember WHERE userid = ?", (user_id,))
            result = cursor.fetchone()
            if result is not None:
                username = result[2]
                aadhar = result[3]
                mobile = result[4]
                email = result[5]
                city = result[6]
                n_name = result[8]
                n_aadhar = result[9]
                self.lineEdit_12.setText(str(username))
                self.lineEdit_4.setText(str(aadhar))
                self.lineEdit_4.setReadOnly(True)

                self.lineEdit_5.setText(str(mobile))
                self.lineEdit_11.setText(str(email))
                self.lineEdit_13.setText(str(city))
                self.lineEdit_15.setText(str(n_name))
                self.lineEdit_16.setText(str(n_aadhar))
                self.frame_7.show()

            else:
                QMessageBox.warning(None, 'Validation Error', 'ID does not exist! Invalid ID')

        except sqlite3.Error as e:
            QMessageBox.critical(None, 'Database Error', str(e))

    def u_up(self):
        try:
            # Connect to SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Change to SQLite connection
            cursor = con.cursor()
            user_id = self.lineEdit_3.text().strip()

            new_username = self.lineEdit_12.text().strip()
            new_aadhar = self.lineEdit_4.text().strip()
            new_mobile = self.lineEdit_5.text().strip()
            new_email = self.lineEdit_11.text().strip()
            new_city = self.lineEdit_13.text().strip()
            new_n_name = self.lineEdit_15.text().strip()
            new_n_aadhar = self.lineEdit_16.text().strip()

            # Update query
            update_query = """
                        UPDATE addmember 
                        SET username = ?, aadhar = ?, mobile = ?, email = ?, city = ?, nominyname = ?, nominyaadhar = ? 
                        WHERE userid = ?
                        """
            cursor.execute(update_query, (
                new_username, new_aadhar, new_mobile, new_email, new_city, new_n_name, new_n_aadhar, user_id))
            con1 = cursor.rowcount
            updt = """update funds set username=? where id=?"""
            cursor.execute(updt, (
                new_username, user_id))
            con2 = cursor.rowcount

            if con2 == 1 and con1 == 1:
                QMessageBox.information(None, 'Success', 'Record updated successfully!')

            con.commit()

            # Clear input fields
            self.lineEdit_3.clear()
            self.lineEdit_12.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_11.clear()
            self.lineEdit_13.clear()
            self.lineEdit_15.clear()
            self.lineEdit_16.clear()
            self.frame_7.hide()
        except sqlite3.Error as e:
            QMessageBox.critical(None, 'Database Error', str(e))

        finally:
            if con:
                con.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_update()
    ui.setupUi(MainWindow)
    MainWindow.show()
