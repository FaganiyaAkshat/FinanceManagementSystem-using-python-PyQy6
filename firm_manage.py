import os
import sys
import sqlite3  # Importing sqlite3 instead of mysql

from member_report import *
from loan import *
from developer import *
from how_to_use import *
from voting_reset import *
from interest import *
from admin import *
from PyQt6 import QtCore, QtGui, QtWidgets

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(915, 574)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Frame)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(17)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(244, 16777215))
        self.widget_3.setMinimumSize(QtCore.QSize(244, 0))
        self.widget_3.setStyleSheet("#widget_3{\n"
"border:2px solid #653C87;\n"
"border-radius:30px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.clicked.connect(self.admin_info)

        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/amin_id_pass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 29))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.clicked.connect(self.loan)

        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_7.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/loan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)


        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.clicked.connect(self.change_rate)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("image/change_rate.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_2.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        self.pushButton_2.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_4.clicked.connect(self.report)

        self.pushButton_4.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/user_report.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.clicked.connect(self.reset_vote)

        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_3.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_5.clicked.connect(self.developer)

        self.pushButton_5.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/dev_info.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_6.clicked.connect(self.how_to_use)

        self.pushButton_6.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"border-radius:20px;\n"
"background-color:#9A79BA;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/how_to_use.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 29))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setStyleSheet("#widget_2{\n"
"border:2px solid #653C87;\n"
"border-radius:30px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_4.setMaximumSize(QtCore.QSize(400, 248))
        self.widget_4.setStyleSheet("#widget_4{\n"
"border:2px solid gray;\n"
"border-radius:50px;\n"
"background:#9A79BA;\n"
"}\n"
"QLabel{\n"
"background:#9A79BA;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.label_6.setMinimumSize(QtCore.QSize(142, 0))
        self.label_6.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"font: 900 12pt \"Segoe UI\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(0, 100, 391, 22))
        self.label_7.setMinimumSize(QtCore.QSize(142, 0))
        self.label_7.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"font: 900 12pt \"Segoe UI\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 361, 22))
        self.label_8.setMinimumSize(QtCore.QSize(142, 0))
        self.label_8.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"font: 900 12pt \"Segoe UI\";")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
            try:
                    # Connect to the SQLite database
                    con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite
                    cursor = con.cursor()

                    # Query to check username and password
                    query = "SELECT uname, email FROM admin WHERE id=?"
                    cursor.execute(query, (1,))
                    result = cursor.fetchone()
                    if result is not None:
                            uname = result[0]
                            email = result[1]
                    else:
                            uname = "Admin"
                            email = "Admin"
                    _translate = QtCore.QCoreApplication.translate
                    Frame.setWindowTitle(_translate("Frame", "Frame"))
                    self.pushButton.setText(_translate("Frame", "admin"))
                    self.pushButton_2.setText(_translate("Frame", "interest rate"))
                    self.pushButton_4.setText(_translate("Frame", "member report"))
                    self.pushButton_3.setText(_translate("Frame", "voting reset"))
                    self.pushButton_5.setText(_translate("Frame", "developer"))
                    self.pushButton_6.setText(_translate("Frame", "how to use"))
                    self.pushButton_7.setText(_translate("Frame", "Manage Loans"))
                    self.label_6.setText(_translate("Frame", f"User Name :- {uname}"))
                    self.label_7.setText(_translate("Frame", f"Email :- {email}"))
                    self.label_8.setText(_translate("Frame", "Password :-******************"))
            except Exception as e:
                    print(e)

    def admin_info(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_adminFrame()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")

    def change_rate(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_Framintereste()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement

    def report(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_reportFrame()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement

    def reset_vote(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_votingFrame()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement

    def loan(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_Framloan()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement

    def developer(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_developer()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement

    def how_to_use(self):
            # Clear existing layout in frame_6
            layout = self.widget_2.layout()
            if layout is not None:
                    while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                    child.widget().deleteLater()

            # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
            self.content_widget = QtWidgets.QWidget()
            self.ui_content = Ui_how_to_useFrame()
            self.ui_content.setupUi(self.content_widget)

            # Set layout if not already set
            if not self.widget_2.layout():
                    self.frame_6_layout = QtWidgets.QVBoxLayout(self.widget_2)
                    self.widget_2.setLayout(self.frame_6_layout)
            self.widget_2.layout().addWidget(self.content_widget)
            print("Content added to voting")  # Debugging print statement