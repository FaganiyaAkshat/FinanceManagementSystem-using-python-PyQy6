import os
import random
import smtplib
import sqlite3  # Changed from mysql.connector to sqlite3
import sys
from email.mime.text import MIMEText
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_Frame_voting2(object):
    passkey = None
    subject_of_vote = None
    vote_id_1 = None
    check_aadhar = None  # for voting purpose
    passkey = None  # Class-level attribute to store the generated passkey

    def __init__(self):
        try:
            # Connect to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
            cursor = con.cursor()

            # Clear the 'check_vote' table
            cursor.execute("DELETE FROM check_vote")  # Use DELETE instead of TRUNCATE for SQLite
            con.commit()

            # Generate a random passkey
            Ui_Frame_voting2.passkey = random.randint(10000, 99999)
            print(Ui_Frame_voting2.passkey)

            # Fetch the admin's email from the 'admin' table
            cursor.execute("SELECT email FROM admin WHERE id = 1 LIMIT 1")
            admin_email = cursor.fetchone()

            if admin_email:
                admin_email = admin_email[0]
            else:
                raise Exception("No admin email found in the database.")

            # Create the email body
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
                    .important {{
                        font-weight: bold;
                        color: #9A79BA;
                    }}
                    .passkey {{
                        font-size: 24px;
                        color: #653C87;
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
                        Voting Session Passkey
                    </div>
                    <p>Hello Guardian Manager,</p>

                    <p>This is your one-time passkey for starting the voting session.</p>

                    <p class="important">**DO NOT SHARE THIS PASSKEY WITH ANYONE.**</p>

                    <p>Please insert the passkey below to start and end the session:</p>

                    <p class="passkey">{Ui_Frame_voting2.passkey}</p>

                    <p>Regards,</p>
                    <p>Voting System Team</p>

                    <div class="footer">
                        This is an automated message. Please do not reply to this email.
                    </div>
                </div>
            </body>
            </html>
            """

            # Set up the email
            msg = MIMEText(body,"html")
            fromaddr = 'akshatfaganiya152@gmail.com'
            toaddr = admin_email
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Voting Session Passkey"

            # Send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "yfyaphpishxxdljc")  # App-specific password
            server.send_message(msg)
            server.quit()

            # Display a confirmation message
            QMessageBox.information(None, 'Validation',
                                    'Passkey has been sent to the administrator\'s registered email.')

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the database connection
            if 'con' in locals():
                con.close()

    def setupUi(self, Frame_voting2):
        Frame_voting2.setObjectName("Frame_voting2")
        Frame_voting2.resize(756, 609)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Frame_voting2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Frame_voting2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(118, 16777215))
        self.pushButton_2.clicked.connect(self.verified_pass)
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
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(113, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(118, 16777215))
        self.pushButton_3.clicked.connect(self.vote_id)

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
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 54))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_5)
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
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 85))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_4.setMaximumSize(QtCore.QSize(118, 16777215))
        self.pushButton_4.clicked.connect(self.applied_vote)

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
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 69))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 49))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setStyleSheet("QPushButton {\n"
                                    "    background-color: #757575;  /* Light grey background */\n"
                                    "    color: white;             /* Font color */\n"
                                    "    font-family: \'Segoe UI\', sans-serif; /* Font family */\n"
                                    "    font-size: 30px;            /* Font size */\n"
                                    "    font-weight: bold;          /* Bold font */\n"
                                    "    padding: 10px 20px;         /* Padding */\n"
                                    "    border: 2px solid #757575;  /* Border color */\n"
                                    "    border-radius: 10px;        /* Rounded corners */\n"
                                    "    transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.3s ease;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #e0e0e0;  /* Slightly darker background on hover */\n"
                                    "    border-color: #5a5a5a;      /* Darker border on hover */\n"
                                    "    transform: scale(1.05);     /* Scale up on hover */\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: #d0d0d0;  /* Darkest background on press */\n"
                                    "    border-color: #404040;      /* Darkest border on press */\n"
                                    "    transform: scale(0.95);     /* Scale down on press */\n"
                                    "}\n"
                                    "")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(54)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton_7.clicked.connect(self.yes)

        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.no_vo)

        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton_5.clicked.connect(self.cdn)

        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_3.setContentsMargins(15, 0, 15, 0)
        self.gridLayout_3.setHorizontalSpacing(26)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame_8)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_3.setMaximumSize(QtCore.QSize(200, 100))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Frame_voting2)
        QtCore.QMetaObject.connectSlotsByName(Frame_voting2)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label_text)
        self.timer.start(500)  # Update every 500 milliseconds
        self.dot_count = 0
        self.retranslateUi(Frame_voting2)
        QtCore.QMetaObject.connectSlotsByName(Frame_voting2)

    def retranslateUi(self, Frame_voting2):
        _translate = QtCore.QCoreApplication.translate
        Frame_voting2.setWindowTitle(_translate("Frame_voting2", "Frame"))
        self.label_5.setText(_translate("Frame_voting2", "Enter passkey "))
        self.pushButton_2.setText(_translate("Frame_voting2", "Add voting"))
        self.label_6.setText(_translate("Frame_voting2", "Enter voting id "))
        self.pushButton_3.setText(_translate("Frame_voting2", "submit"))
        self.label_4.setText(_translate("Frame_voting2", "Voting Running..."))
        self.label_8.setText(_translate("Frame_voting2", "Aadhar number"))
        self.pushButton_4.setText(_translate("Frame_voting2", "clicked"))
        self.label_7.setText(_translate("Frame_voting2", "Select your vote yes,no or CDN"))
        self.pushButton_7.setText(_translate("Frame_voting2", "YES"))
        self.pushButton_6.setText(_translate("Frame_voting2", "NO"))
        self.pushButton_5.setText(_translate("Frame_voting2", "CDN"))
        self.label.setText(_translate("Frame_voting2", "Total vote for yes"))
        self.label_2.setText(_translate("Frame_voting2", "Total vote for no"))
        self.label_3.setText(_translate("Frame_voting2", "Total vote for CND(can not be determined)"))
        ####
        self.label_4.hide()
        self.label_8.hide()
        self.lineEdit_5.hide()
        self.pushButton_4.hide()
        ###
        self.label_7.hide()
        self.frame_10.hide()
        self.frame_3.hide()
        ##
        self.frame_8.hide()

    def update_label_text(self):
        dots = "." * self.dot_count
        self.label_4.setText(f"Voting Running{dots}")
        self.dot_count = (self.dot_count + 1) % 4  # Cycle through 0, 1, 2, 3 dots

    def verified_pass(self):
        try:
            key = self.lineEdit_3.text().strip().lower()
            if int(key) == int(Ui_Frame_voting2.passkey):

                # Find the position of the existing button in the grid layout
                layout = self.frame_2.layout()
                for i in range(layout.count()):
                    item = layout.itemAt(i)
                    if item.widget() == self.pushButton_2:
                        position = layout.getItemPosition(i)
                        row, col, row_span, col_span = position
                        break

                # Hide the existing button
                self.pushButton_2.hide()

                # Create a new button at the same grid position
                self.new_button = QtWidgets.QPushButton("End Voting")
                self.new_button.setStyleSheet(
                    """ 
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
                                    } 
                                    """
                )
                layout.addWidget(self.new_button, row, col, row_span, col_span)
                self.new_button.clicked.connect(self.end_voting)

                self.frame_3.show()

                aadhar = self.lineEdit_5.text().strip().lower()

            else:
                QMessageBox.warning(None, 'Validation Error', 'Invalid passkey')
        except Exception as e:
            print("Exception in verified_pass:", e)

    def vote_id(self):
        try:
            v_id = self.lineEdit_4.text().strip()

            con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
            cursor = con.cursor()

            # Check if the voting ID exists in the table
            cursor.execute("SELECT * FROM voting WHERE id = ?", (v_id,))
            result = cursor.fetchone()

            if result is not None:
                Ui_Frame_voting2.vote_id_1 = v_id
                Ui_Frame_voting2.subject_of_vote = str(result[1])
                self.label_4.show()
                self.label_8.show()
                self.lineEdit_5.show()
                self.pushButton_4.show()
                self.lineEdit_3.clear()
                return
            else:
                QMessageBox.warning(None, 'Validation Error', 'No voting schedule available')

        except Exception as e:
            print("Exception in vote_id:", e)

    def applied_vote(self):
            try:
                aadhar = self.lineEdit_5.text().strip()

                if not aadhar:
                    QMessageBox.warning(None, 'Validation Error', 'Aadhar number should not be empty')
                    return
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
                cursor = con.cursor()
                cursor.execute("SELECT * FROM check_vote WHERE aadhar = ?", (aadhar,))
                cek = cursor.fetchone()

                if cek is not None:
                    QMessageBox.warning(None, 'Validation Error', 'You have already voted')
                    return

                cursor.execute("INSERT INTO check_vote(aadhar) VALUES (?)", (aadhar,))
                con.commit()

                # Check if the Aadhar exists in the table
                cursor.execute("SELECT * FROM addmember WHERE aadhar = ?", (aadhar,))
                result = cursor.fetchone()
                Ui_Frame_voting2.check_aadhar = aadhar
                if result is None:
                    QMessageBox.warning(None, 'Validation Error', 'Not a member of the firm')
                    return
                else:
                    nam = str(result[2])
                    self.label_7.setText(f"Welcome {nam}, give your unique vote for {Ui_Frame_voting2.subject_of_vote}")
                    self.label_7.show()
                    self.frame_10.show()

            except Exception as e:
                print("Exception in applied_vote:", e)

    def cdn(self):
            try:
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
                cursor = con.cursor()
                cursor.execute("SELECT * FROM voting WHERE id = ?", (Ui_Frame_voting2.vote_id_1,))
                cek = cursor.fetchone()
                add_cnd = cek[5] + 1

                cursor.execute("UPDATE voting SET cdn = ? WHERE id = ?", (add_cnd, Ui_Frame_voting2.vote_id_1))
                con.commit()
                QMessageBox.warning(None, 'Validation', 'Vote count updated successfully')

            except Exception as e:
                print("Exception in cdn:", e)
            self.label_7.hide()
            self.frame_10.hide()
            self.lineEdit_5.clear()

    def yes(self):
            try:
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
                cursor = con.cursor()
                cursor.execute("SELECT * FROM voting WHERE id = ?", (Ui_Frame_voting2.vote_id_1,))
                cek = cursor.fetchone()
                add_yes = cek[3] + 1

                cursor.execute("UPDATE voting SET yes = ? WHERE id = ?", (add_yes, Ui_Frame_voting2.vote_id_1))
                con.commit()
                QMessageBox.warning(None, 'Validation', 'Vote count updated successfully')

            except Exception as e:
                print("Exception in yes:", e)
            self.label_7.hide()
            self.frame_10.hide()
            self.lineEdit_5.clear()

    def no_vo(self):
            try:
                con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
                cursor = con.cursor()
                cursor.execute("SELECT * FROM voting WHERE id = ?", (Ui_Frame_voting2.vote_id_1,))
                cek = cursor.fetchone()
                add_no = cek[4] + 1

                cursor.execute("UPDATE voting SET no = ? WHERE id = ?", (add_no, Ui_Frame_voting2.vote_id_1))
                con.commit()
                QMessageBox.warning(None, 'Validation', 'Vote count updated successfully')

            except Exception as e:
                print("Exception in no_vo:", e)
            self.label_7.hide()
            self.frame_10.hide()
            self.lineEdit_5.clear()

    def end_voting(self):
            try:
                key = self.lineEdit_3.text().strip().lower()
                if int(key) == int(Ui_Frame_voting2.passkey):
                    self.frame_3.hide()
                    self.frame_5.hide()
                    self.frame_7.hide()
                    self.frame_9.hide()
                    self.frame_10.hide()
                    con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite database connection
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM voting WHERE id = ?", (Ui_Frame_voting2.vote_id_1,))
                    cek = cursor.fetchone()
                    y = cek[3]
                    n = cek[4]
                    c = cek[5]
                    self.label.setText(f"Total votes for YES: {y}")
                    self.label_2.setText(f"Total votes for NO: {n}")
                    self.label_3.setText(f"Total votes for CDN (cannot be determined): {c}")
                    self.frame_8.show()
                    cursor.execute("DELETE FROM check_vote")  # Use DELETE instead of TRUNCATE for SQLite
                    con.commit()
                    QMessageBox.warning(None, 'Validation', 'Your voting session has ended. This is your result.')
            except Exception as e:
                print("Exception in end_voting:", e)

    # Note: Ensure that the SQLite database 'db/db/db/db/firm_management.db' and the required tables are created before running this code.