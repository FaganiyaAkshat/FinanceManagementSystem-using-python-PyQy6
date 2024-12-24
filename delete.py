import os
import smtplib
import sys
import time
import urllib
from email.mime.text import MIMEText
import random
import sqlite3  # Changed from mysql.connector to sqlite3
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


class Ui_delete(object):
    usermail = None
    otp = None
    user_id = None
    def setupUi(self, Ui_delete):
        Ui_delete.setObjectName("Ui_delete")
        Ui_delete.resize(991, 545)
        self.gridLayout_2 = QtWidgets.QGridLayout(Ui_delete)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=Ui_delete)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("QFrame:addmember{\n"
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
"    font-size: 18px;\n"
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
"QPushButton {\n"
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
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(550, 384))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 56))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
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
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_66 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_66.setMaximumSize(QtCore.QSize(16777215, 81))
        self.frame_66.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_66.setObjectName("frame_66")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_66)
        self.gridLayout.setContentsMargins(11, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_66)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 46))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setStyleSheet("padding:0px;")
        self.pushButton.clicked.connect(self.toggle_frames)  # Connect button click to method
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_66)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame_66)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 47))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_66, 1, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 69))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setSpacing(0)
        self.frame_7.hide()

        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_3.setMaximumSize(QtCore.QSize(500, 66))
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_7, 2, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 86))
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setContentsMargins(9, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 47))
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_8)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 46))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setStyleSheet("padding:0px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toggle_delete)  # Connect button click to method

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_8, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_5.setStyleSheet("background:#E6D7FA;\n"
"border-radius:40px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.frame_8.hide()

        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame_5)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 297))
        self.textBrowser.setMaximumSize(QtCore.QSize(573, 16777215))
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    border: none; /* Example: Remove border if needed */\n"
"    overflow: hidden;\n"
"   scrollbar:hideen;\n"
"  background:#E6D7FA;\n"
"}\n"
"\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_5)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.retranslateUi(Ui_delete)
        QtCore.QMetaObject.connectSlotsByName(Ui_delete)

    def retranslateUi(self, Ui_delete):
        _translate = QtCore.QCoreApplication.translate
        Ui_delete.setWindowTitle(_translate("Ui_delete", "Frame"))
        self.label_4.setText(_translate("Ui_delete", "Delete"))
        self.pushButton.setText(_translate("Ui_delete", "Send OTP"))
        self.label.setText(_translate("Ui_delete", "User Id"))
        self.label_3.setText(_translate("Ui_delete", "TextLabel"))
        self.label_5.setText(_translate("Ui_delete", "OTP"))
        self.pushButton_2.setText(_translate("Ui_delete", "Submit "))
        self.textBrowser.setHtml(_translate("Ui_delete", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">CAUTION :</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">1.person who delete his account must be provide one time password otp for his security purpose. whithout otp can not delete account.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">2.it means sender and receiver both are must be cumpolsury to connnected with the internet.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">3. when user fill up id in the userid field then the one time password are received on your registered email.same otp which you have receive provide here.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">4.filling this otp in the otp field submit clicked button and your information will be deleted.</span><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    def toggle_frames(self):
        if self.is_internet_connected():
            _translate = QtCore.QCoreApplication.translate
            user_id = self.lineEdit.text().strip()
            try:
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
                cursor = con.cursor()

                # Check if the email exists in the table
                cursor.execute("SELECT email FROM addmember WHERE userid = ?", (user_id,))
                result = cursor.fetchone()

                if result is not None:
                    useremail = result[0]  # Store the email
                    self.user_id = user_id  # Store the user ID globally

                    print(f"Email found: {useremail}, User ID set to: {self.user_id}")

                    # Toggle frames visibility
                    if self.frame_7.isVisible() and self.frame_8.isVisible():
                        self.frame_7.hide()
                        self.frame_8.hide()
                    else:
                        # Generate and send OTP
                        self.otp = random.randint(10000, 99999)
                        print(self.otp)
                        body = f"""
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <style>
                                body {{
                                    font-family: Arial, sans-serif;
                                    line-height: 1.6;
                                    color: #333;
                                    margin: 0;
                                    padding: 0;
                                    background-color: #F9F9F9;
                                }}
                                .container {{
                                    max-width: 600px;
                                    margin: 20px auto;
                                    padding: 20px;
                                    border: 1px solid #E6D7FA;
                                    border-radius: 10px;
                                    background-color: #FFFFFF;
                                }}
                                .header {{
                                    text-align: center;
                                    font-size: 22px;
                                    font-weight: bold;
                                    color: #653C87;
                                    margin-bottom: 20px;
                                }}
                                .highlight {{
                                    color: #9A79BA;
                                    font-weight: bold;
                                }}
                                .otp {{
                                    font-size: 24px;
                                    color: #9A79BA;
                                    font-weight: bold;
                                    display: inline-block;
                                    margin: 10px 0;
                                }}
                                .footer {{
                                    margin-top: 20px;
                                    text-align: center;
                                    font-size: 12px;
                                    color: #777;
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <div class="header">
                                    Membership Termination Notification
                                </div>
                                <p>Dear User,</p>

                                <p>We hope this email finds you well. We regret to inform you that your membership with <span class="highlight">KuberaFinancialGuardians</span> has been terminated.</p> 

                                <p>This decision was not made lightly and comes after careful consideration. We genuinely value the contributions you've made during your time with us. If you have any questions or need further clarification, please feel free to contact us at 
                                <a href="mailto:support@kuberafirm.com">support@kuberafirm.com</a>.</p>

                                <p>Thank you for being a part of our journey. We wish you all the best in your future endeavors.</p> 

                                <p>Please provide the following OTP to complete the termination process: 
                                <span class="otp">{self.otp}</span></p>

                                <p>Sincerely,</p>  
                                <p>KuberaFinancialGuardians Team</p>

                                <div class="footer">
                                    This is an automated message. Please do not reply to this email.
                                </div>
                            </div>
                        </body>
                        </html>
                        """

                        # Email setup
                        msg = MIMEText(body, "html")
                        from_addr = 'akshatfaganiya152@gmail.com'  # Replace with your verified sender email
                        msg['From'] = from_addr
                        msg['To'] = useremail
                        msg['Subject'] = "Membership Termination Notification"

                        # Send the email
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(from_addr, "yfyaphpishxxdljc")
                        server.send_message(msg)
                        server.quit()
                        self.otp_expiry_time = time.time() + 30  # Set expiry time to 30 seconds from now

                        self.label_3.setText(_translate("Frame", f"OTP sent to {useremail}"))
                        self.frame_7.show()
                        self.frame_8.show()

                else:
                    QMessageBox.warning(None, 'Validation Error', 'ID does not exist! Invalid ID')

            except sqlite3.Error as e:  # Changed to sqlite3.Error
                print(f"Error: {e}")

            finally:
                if con:
                    con.close()
                    print("SQLite connection is closed")

        else:
            QMessageBox.warning(None, 'Validation Error', 'Check internet connection')

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_3.clear()

    def reload_function(self):
        self.frame_7.hide()
        self.frame_8.hide()
        pass

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

    def toggle_delete(self):
        try:
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
            cursor = con.cursor()

            confirm = self.lineEdit_2.text().strip()
            print(f"Confirming OTP: '{confirm}'")
            print(f"Original OTP: '{self.otp}'")

            if confirm:  # Check if the input is not empty
                print(f"Confirming OTP: '{confirm}'")

                if time.time() < self.otp_expiry_time:
                    print(f"Current time: {time.time()}, OTP expiry time: {self.otp_expiry_time}")

                    if confirm == str(self.otp):  # Ensure to compare strings
                        print(f"Expected OTP: '{self.otp}'")

                        # Delete the record using the globally stored user_id
                        cursor.execute("DELETE FROM addmember WHERE userid = ?", (self.user_id,))
                        cursor.execute("DELETE FROM entry WHERE u_id = ?", (self.user_id,))
                        cursor.execute("DELETE FROM funds WHERE id = ?", (self.user_id,))
                        cursor.execute("DELETE FROM entry WHERE u_id = ?", (self.user_id,))
                        con.commit()

                        QMessageBox.information(None, 'Success', 'Record deleted and OTP verified!')

                        # Clear fields after success
                        self.clear_fields()

                        # Reload the function or UI
                        self.reload_function()

                        # Resetting variables
                        self.user_id = None
                        self.otp = None
                        self.usermail = None

                        # Close the connection properly
                        cursor.close()
                        con.close()
                        print("SQLite connection is closed")

                    else:
                        QMessageBox.warning(None, 'Validation Error', 'Invalid OTP!')
                else:
                    QMessageBox.warning(None, 'Validation Error', 'OTP has expired!')
            else:
                QMessageBox.warning(None, 'Validation Error', 'Please enter the OTP!')
                print(f"Email found: {self.usermail}, User ID set to: {self.user_id}")

        except sqlite3.Error as e:  # Changed to sqlite3.Error
            print(f"Error: {e}")
            QMessageBox.critical(None, 'Database Error',
                                 'An error occurred while accessing the database. Please try again later.')

        finally:
            if con:
                con.close()
                print("SQLite connection is closed")

    def get_style_sheet(self):
        return """QFrame:addmember{
        border:none;
        }
        QLabel {
            background-color: #E6D7FA;
            color: #653C87;
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
            font-weight: 600;
            padding: 8px;
            border: 2px solid #653C87;
            border-radius: 10px;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        QLabel:hover {
            background-color: #D4C2EF; 
            border-color: #553075;  
        }
        QLineEdit {
            border: 2px solid #9A79BA;
            border-radius: 10px;
            padding: 8px;
            font-family: 'Segoe UI', sans-serif;
            font-size: 20px;
            color: #653C87;
            background-color: #FFFFFF;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        QLineEdit:hover {
            background-color: #F5F0FA;  
        }
        QLineEdit:focus {
            border: 2px solid #653C87;  
            background-color: #F5F5F5;  
        }
        QPushButton {
            background-color: #653C87; 
            color: #FFFFFF; 
            font-family: 'Segoe UI', sans-serif; 
            font-size: 14px; 
            font-weight: bold; 
            padding: 10px 20px; 
            border: 2px solid #9A79BA; 
            border-radius: 10px; 
            transition: background-color 0.3s ease, border-color 0.3s ease; 
        }
        QPushButton:hover {
            background-color: #9A79BA; 
            border-color: #653C87; 
        }
        QPushButton:pressed {
            background-color: #E6D7FA; 
            border-color: #553075; 
        }"""