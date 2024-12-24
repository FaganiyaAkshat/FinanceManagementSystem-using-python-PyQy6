# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sqlite3  # Changed from mysql.connector to sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
import random
import smtplib
from email.mime.text import MIMEText
from PyQt6.QtWidgets import QMessageBox
import urllib.request

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Database connection details
def get_image_path(filename):
    """ Get the image path based on the execution context (development or bundled) """
    if hasattr(sys, '_MEIPASS'):
        return resource_path(filename)  # Running as a bundled executable
    else:
        return filename  # Running in development
class Ui_member(object):
    def setupUi(self, addmember):
        addmember.setObjectName("addmember")
        addmember.resize(861, 600)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(addmember)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(parent=addmember)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("QFrame:addmember{\n"
                                  "border:none;\n"
                                  "}\n"
                                  "QLabel {\n"
                                  "    \n"
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
                                  "    font-size: 20px;\n"
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
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
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
        self.verticalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(parent=self.widget)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_8.setStyleSheet("QLabel {\n"
                                   "    \n"
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
                                   "    font-size: 20px;\n"
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
        self.label_5 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_6.setMinimumSize(QtCore.QSize(142, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.widget)
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
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.widget)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_16.setMinimumSize(QtCore.QSize(142, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_10.addWidget(self.lineEdit_13)
        self.label_17 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_17.setMinimumSize(QtCore.QSize(142, 0))
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_10.addWidget(self.lineEdit_14)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(parent=self.widget)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_18.setMinimumSize(QtCore.QSize(142, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_11.addWidget(self.lineEdit_15)
        self.label_19 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_19.setMinimumSize(QtCore.QSize(142, 0))
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        self.lineEdit_16 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_11.addWidget(self.lineEdit_16)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(parent=self.widget)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_12)
        self.pushButton_2.setMaximumSize(QtCore.QSize(142, 16777215))
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
        self.pushButton_2.clicked.connect(self.store_detail)
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_12)
        self.verticalLayout_3.addWidget(self.widget)

        self.retranslateUi(addmember)
        QtCore.QMetaObject.connectSlotsByName(addmember)

    def retranslateUi(self, addmember):
        _translate = QtCore.QCoreApplication.translate
        addmember.setWindowTitle(_translate("addmember", "Frame"))
        self.label_4.setText(_translate("addmember", " Add Member"))
        self.label_5.setText(_translate("addmember", "Aadhar number"))
        self.label_6.setText(_translate("addmember", "Mobile number"))
        self.label_14.setText(_translate("addmember", "Email"))
        self.label_15.setText(_translate("addmember", "Username"))
        self.label_16.setText(_translate("addmember", "City"))
        self.label_17.setText(_translate("addmember", "Deposit"))
        self.label_18.setText(_translate("addmember", "Nominee name"))
        self.label_19.setText(_translate("addmember", "Nominee Aadhar"))
        self.pushButton_2.setText(_translate("addmember", "Submit"))

    def store_detail(self):
        global con, cursor
        _translate = QtCore.QCoreApplication.translate

        name = self.lineEdit_12.text().strip()
        mobile = self.lineEdit_4.text().strip()
        aadhar = self.lineEdit_3.text().strip()
        email = self.lineEdit_11.text().strip()
        city = self.lineEdit_13.text().strip()
        n_name = self.lineEdit_15.text().strip()
        n_aadhar = self.lineEdit_16.text().strip()
        dep = self.lineEdit_14.text().strip()
        # Validation
        if not name:
            QMessageBox.warning(None, 'Validation Error', 'Name should not be empty')
            return
        if len(mobile) != 10 or not mobile.isdigit():
            QMessageBox.warning(None, 'Validation Error', 'Mobile number must be 10 digits long')
            return
        if len(aadhar) != 12 or not aadhar.isdigit():
            QMessageBox.warning(None, 'Validation Error', 'Aadhar number must be 12 digits long')
            return
        if "@gmail" not in email or not email.endswith(".com"):
            QMessageBox.warning(None, 'Validation Error', 'Email must a valid email')
            return
        if not n_name:
            QMessageBox.warning(None, 'Validation Error', 'Nominee name should not be empty')
            return
        if len(n_aadhar) != 12 or not n_aadhar.isdigit():
            QMessageBox.warning(None, 'Validation Error', 'Nominee Aadhar number must be 12 digits long')
            return
        try:
            if not dep:
                QMessageBox.warning(None, 'Validation Error', 'fill deposit minimum 1000')
                return

            if int(dep) < 1000:
                QMessageBox.warning(None, 'Validation Error', 'minimum deposit is greater than 1000')
                return
        except Exception as e:
            QMessageBox.warning(None, 'Validation Error', 'invalid amount')
            return
        try:
            # Connect to SQLite database

            con = sqlite3.connect(resource_path("db/firm_management.db"))  # Changed to SQLite connection
            cursor = con.cursor()
            # Email validation
            cursor.execute("SELECT COUNT(*) FROM addmember WHERE email = ?", (email,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error', 'Email already exists in the database')
                return
            if aadhar == n_aadhar:
                QMessageBox.warning(None, 'Validation Error',
                                    'Nominee aadharnumber and account holder aadhar number same ')
                return

            cursor.execute("SELECT COUNT(*) FROM addmember WHERE mobile = ?", (mobile,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'Mobile number already exists in the database')
                return

            cursor.execute("SELECT COUNT(*) FROM addmember WHERE nominyaadhar = ?", (n_aadhar,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'Nominee aadhar exists in database')
                return

            # Check if aadhar already exists in the table
            cursor.execute("SELECT COUNT(*) FROM addmember WHERE aadhar = ?", (aadhar,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'Aadhar number already exists in the database')
                return

            # Check if aadhar is in bankrupt records
            cursor.execute("SELECT COUNT(*) FROM bankrupt WHERE aadhar = ?", (aadhar,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'Aadhar number is listed in the bankrupt records')
                return

            cursor.execute("SELECT COUNT(*) FROM bankrupt WHERE aadhar = ?", (n_aadhar,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'Nominee Aadhar number is already listed in bankrupt records')
                return

            # Check if nominee and user are the same
            cursor.execute("SELECT COUNT(*) FROM addmember WHERE nominyaadhar = ?", (n_aadhar,))
            result = cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, 'Validation Error',
                                    'invalid aadhar number')
                return

            # Generate a unique 5-digit number
            while True:
                five_digit_number = random.randint(10000, 99999)
                cursor.execute("SELECT COUNT(*) FROM addmember WHERE userid = ?", (five_digit_number,))
                result = cursor.fetchone()
                if result[0] == 0:
                    userid = five_digit_number
                    break

            # Insert the record into the addmember table
            in_new = "SELECT interest FROM funds LIMIT 1"
            cursor.execute(in_new)
            r = cursor.fetchone()

            # Default interest value
            d_interest = 0

            # If a row is found, use the existing interest
            if r is not None and r[0] is not None:
                d_interest = r[0]

            # Insert the new customer into the 'funds' table with the determined interest rate
            dep_insert = """INSERT INTO funds(id, username, funds, interest) VALUES (?, ?, ?, ?)"""
            manage_funds = (userid, name, dep, d_interest)
            cursor.execute(dep_insert, manage_funds)

            insert_query = """
            INSERT INTO addmember (userid, username, aadhar, mobile, email, city, nominyname, nominyaadhar)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            record = (userid, name, aadhar, mobile, email, city, n_name, n_aadhar)
            cursor.execute(insert_query, record)
            entry = (userid, dep, 'credit')
            cursor.execute("INSERT INTO entry(u_id, t_amount, t_type) VALUES (?, ?, ?)", entry)

            # Commit the transaction
            con.commit()

            # Clear all QLineEdit fields
            self.lineEdit_12.clear()
            self.lineEdit_14.clear()
            self.lineEdit_4.clear()
            self.lineEdit_3.clear()
            self.lineEdit_11.clear()
            self.lineEdit_13.clear()
            self.lineEdit_15.clear()
            self.lineEdit_16.clear()
            if self.is_internet_connected():
                self.m_s(email, userid)
            QMessageBox.information(None, 'Success', 'Registration successfully')
            con.commit()
        except sqlite3.Error as e:  # Changed to sqlite3.Error
            print(f"Error: {e}")

        finally:
            if con:
                con.rollback()
                cursor.close()
                con.close()
                print("SQLite connection is closed")

    def m_s(self, email, userid):
        # Email body with placeholders for personalization
        body = f"""
        Dear User,

        Congratulations on successfully registering with **Kubera Firm Guardians**!

        We are thrilled to have you on board. Your unique user ID is: **{userid}**.

        Please save this email for your records. If you have any questions or need assistance, feel free to contact us at [support@kuberafirm.com](mailto:support@kuberafirm.com).

        Welcome to the Kubera Firm family!

        Best Regards,  
        Kubera Firm Guardians Team
        """

        # Email setup
        msg = MIMEText(body, "plain")
        fromaddr = 'akshatfaganiya152@gmail.com'  # Replace with your verified sender email
        toaddr = email
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Welcome to Kubera Firm Guardians"

        try:
            # Email server configuration
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "yfyaphpishxxdljc")  # Replace with a secure app-specific password
            server.send_message(msg)
            server.quit()

            print(f"Email successfully sent to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}. Error: {e}")

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
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_member()
    ui.setupUi(MainWindow)
    MainWindow.show()