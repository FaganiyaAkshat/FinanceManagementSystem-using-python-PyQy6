import importlib
import os
import sys
import urllib
import sqlite3  # Changed from mysql.connector to sqlite3
import smtplib
import random
import time
from email.mime.text import MIMEText
from PyQt6 import QtCore, QtWidgets

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Database connection details

class Ui_adminFrame(object):
    def setupUi(self, adminFrame):
        adminFrame.setObjectName("adminFrame")
        adminFrame.resize(745, 489)
        self.horizontalLayout = QtWidgets.QHBoxLayout(adminFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(parent=adminFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QtCore.QSize(412, 370))
        self.widget_4.setStyleSheet("#widget_4{\n"
                                     "border:2px solid gray;\n"
                                     "border-radius:50px;\n"
                                     "}\n"
                                     "QLabel{\n"
                                     "background:#9A79BA;\n"
                                     "}\n"
                                     "\n"
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
                                     "    font-family: 'Segoe UI', sans-serif;\n"
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
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(15, 15, 15, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_12 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_12.setMaximumSize(QtCore.QSize(392, 62))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_17.setMinimumSize(QtCore.QSize(142, 0))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.frame_12)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_12.addWidget(self.lineEdit_14)
        self.verticalLayout.addWidget(self.frame_12)
        self.frame_9 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_9.setMaximumSize(QtCore.QSize(392, 62))
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
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_10.setMaximumSize(QtCore.QSize(392, 62))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_15.setMinimumSize(QtCore.QSize(142, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_10.addWidget(self.lineEdit_12)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_11.setMaximumSize(QtCore.QSize(392, 62))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_16.setMinimumSize(QtCore.QSize(142, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_11.addWidget(self.lineEdit_13)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_13 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_13)
        self.pushButton_2.clicked.connect(self.sent_otp)
        self.pushButton_2.setMaximumSize(QtCore.QSize(142, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                         "    background-color: #653C87; /* Dark purple background */\n"
                                         "    color: #FFFFFF; /* White text */\n"
                                         "    font-family: 'Segoe UI', sans-serif; /* Font family */\n"
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
        self.horizontalLayout_14.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_13)
        self.horizontalLayout.addWidget(self.widget_4)

        self.retranslateUi(adminFrame)
        QtCore.QMetaObject.connectSlotsByName(adminFrame)

        # Initialize OTP and its generation time
        self.generated_otp = None
        self.otp_generation_time = None

    def retranslateUi(self, adminFrame):
        _translate = QtCore.QCoreApplication.translate
        adminFrame.setWindowTitle(_translate("adminFrame", "Frame"))
        self.label_17.setText(_translate("adminFrame", "OTP"))
        self.label_14.setText(_translate("adminFrame", "Username"))
        self.label_15.setText(_translate("adminFrame", "Email"))
        self.label_16.setText(_translate("adminFrame", "Password"))
        self.pushButton_2.setText(_translate("adminFrame", "Send OTP"))
        self.frame_9.hide()
        self.frame_10.hide()
        self.frame_12.hide()
        self.frame_11.hide()

    def sent_otp(self):
        if self.is_internet_connected():
            try:
                # Connect to the SQLite database
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite
                cursor = con.cursor()
                query = "SELECT email FROM admin WHERE id=?"
                cursor.execute(query, (1,))
                result = cursor.fetchone()
                email = result[0]

                # Insert user data into the database
                username = self.lineEdit_12.text()

                # Generate a random OTP
                self.generated_otp = random.randint(100000, 999999)
                print(self.generated_otp)
                self.otp_generation_time = time.time()  # Store the current time

                # Email body
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
                        }}
                        .container {{
                            max-width: 600px;
                            margin: 20px auto;
                            padding: 20px;
                            border: 1px solid #E6D7FA;
                            border-radius: 10px;
                            background-color: #F9F9F9;
                        }}
                        .header {{
                            text-align: center;
                            font-size: 20px;
                            font-weight: bold;
                            color: #653C87;
                            margin-bottom: 20px;
                        }}
                        .otp {{
                            font-size: 24px;
                            color: #9A79BA;
                            font-weight: bold;
                            text-align: center;
                            display: block;
                            margin: 20px 0;
                        }}
                        .footer {{
                            margin-top: 20px;
                            text-align: center;
                            font-size: 12px;
                            color: #777;
                        }}
                        .button {{
                            display: inline-block;
                            padding: 10px 20px;
                            font-size: 16px;
                            color: #fff;
                            background-color: #653C87;
                            text-decoration: none;
                            border-radius: 5px;
                            margin-top: 20px;
                        }}
                        .button:hover {{
                            background-color: #9A79BA;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            KuberaFinancialGuardians Account Update Request
                        </div>
                        <p>Dear Admin,</p>

                        <p>We received a request to update your account information. To proceed, please use the following One-Time Password (OTP):</p>

                        <div class="otp">{self.generated_otp}</div>

                        <p>This OTP is valid for the next <strong>1 minute</strong>. If you did not make this request, please contact the support team immediately.</p>

                        <p>Thank you for ensuring the security of your account.</p>

                        <p>Best regards,<br>KuberaFinancialGuardians Support Team</p>

                        <div class="footer">
                            This is an automated message. Please do not reply to this email.
                        </div>
                    </div>
                </body>
                </html>
                """

                # Create email
                msg = MIMEText(body, "html")  # Use "plain" for plain text or "html" for HTML content
                fromaddr = 'akshatfaganiya152@gmail.com'
                toaddr = email
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Action Required: Verify Your Request"

                # Send the email
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(fromaddr, "yfyaphpishxxdljc")  # Use an app password or secure method
                    server.send_message(msg)
                    server.quit()
                    QtWidgets.QMessageBox.information(None, "Success", "OTP sent successfully on your administrator registration email! valid only 1 minute")
                    self.show_otp_input()
                except Exception as e:
                    QtWidgets.QMessageBox.critical(None, "Error", f"Failed to send OTP: {str(e)}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No internet connection.")

    def show_otp_input(self):
        try:
            # Hide the send OTP button and show the OTP input frame
            self.frame_12.show()
            self.pushButton_2.setText("Submit OTP")
            self.pushButton_2.setVisible(False)  # Hide the original Send OTP button

            # Create a new button to submit the OTP
            self.pushButton_submit_otp = QtWidgets.QPushButton("Submit OTP", self.widget_4)
            self.pushButton_submit_otp.setStyleSheet(
                """ 
                QPushButton { 
                    background-color: #653C87; /* Dark purple background */
                    color: #FFFFFF; /* White text */
                    font-family: 'Segoe UI', sans-serif; /* Font family */
                    font-size: 14px; /* Font size */
                    font-weight: bold; /* Bold text */
                    padding: 10px 20px; /* Padding */
                    border: 2px solid #9A79BA; /* Light purple border */
                    border-radius: 10px; /* Rounded corners */
                    transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition */
                } 
                QPushButton:hover { 
                    background-color: #9A79BA; /* Light purple background on hover */
                    border-color: #653C87; /* Dark purple border on hover */
                } 
                QPushButton:pressed { 
                    background-color: #E6D7FA; /* Lightest purple background on press */
                    border-color: #553075; /* Darker purple border on press */
                } 
                """
            )

            # Set the same width, height, and size policy as the original button
            self.pushButton_submit_otp.setSizePolicy(self.pushButton_2.sizePolicy())  # Same size policy
            self.pushButton_submit_otp.setFixedWidth(self.pushButton_2.width())  # Same width
            self.pushButton_submit_otp.setFixedHeight(self.pushButton_2.height())  # Same height

            # Add the new button to the layout
            self.verticalLayout.addWidget(self.pushButton_submit_otp)

            # Center the button inside the layout
            self.verticalLayout.setAlignment(self.pushButton_submit_otp, QtCore.Qt.AlignmentFlag.AlignCenter)

            # Connect the new button to the function to check the OTP
            self.pushButton_submit_otp.clicked.connect(self.check_otp)

        except Exception as e:
            print(f"Error: {e}")

    def check_otp(self):
        entered_otp = self.lineEdit_14.text()
        current_time = time.time()  # Get the current time

        # Check if the OTP is valid (1 minute validity)
        if self.generated_otp is not None and (current_time - self.otp_generation_time) <= 60:
            if entered_otp == str(self.generated_otp):
                self.frame_9.show()
                self.frame_10.show()
                self.frame_11.show()
                self.pushButton_submit_otp.setVisible(False)
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite
                cursor = con.cursor()
                cursor.execute("SELECT * FROM admin WHERE id = ?", (1,))  # Use parameterized query
                result = cursor.fetchone()
                if result is not None:
                    username = result[1]
                    password = result[2]
                    email = result[3]
                    self.lineEdit_11.setText(str(username))
                    self.lineEdit_12.setText(str(email))
                    self.lineEdit_13.setText(str(password))

                    # Create a new button to submit the updated information
                    self.pushbutton_update = QtWidgets.QPushButton("Save", self.widget_4)
                    self.pushbutton_update.setStyleSheet(
                        """ 
                        QPushButton { 
                            background-color: #653C87; /* Dark purple background */
                            color: #FFFFFF; /* White text */
                            font-family: 'Segoe UI', sans-serif; /* Font family */
                            font-size: 14px; /* Font size */
                            font-weight: bold; /* Bold text */
                            padding: 10px 20px; /* Padding */
                            border: 2px solid #9A79BA; /* Light purple border */
                            border-radius: 10px; /* Rounded corners */
                            transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition */
                        } 
                        QPushButton:hover { 
                            background-color: #9A79BA; /* Light purple background on hover */
                            border-color: #653C87; /* Dark purple border on hover */
                        } 
                        QPushButton:pressed { 
                            background-color: #E6D7FA; /* Lightest purple background on press */
                            border-color: #553075; /* Darker purple border on press */
                        } 
                        """
                    )

                    # Set the same width, height, and size policy as the original button
                    self.pushbutton_update.setSizePolicy(self.pushButton_2.sizePolicy())  # Same size policy
                    self.pushbutton_update.setFixedWidth(self.pushButton_2.width())  # Same width
                    self.pushbutton_update.setFixedHeight(self.pushButton_2.height())  # Same height

                    # Add the new button to the layout
                    self.verticalLayout.addWidget(self.pushbutton_update)

                    # Center the button inside the layout
                    self.verticalLayout.setAlignment(self.pushbutton_update, QtCore.Qt.AlignmentFlag.AlignCenter)

                    # Connect the new button to the function to update the information
                    self.pushbutton_update.clicked.connect(self.updt)
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Incorrect OTP!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "OTP has expired!")

    def updt(self):
        try:
            username = self.lineEdit_11.text()
            email = self.lineEdit_12.text()
            password = self.lineEdit_13.text()
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite
            cursor = con.cursor()
            cursor.execute("UPDATE admin SET uname = ?, password = ?, email = ? WHERE id = ?", (username, password, email, 1))
            con.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Record updated successfully!")

        except Exception as e:
            print(f"Error: {e}")

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
            print("No internet connection.")
            return False