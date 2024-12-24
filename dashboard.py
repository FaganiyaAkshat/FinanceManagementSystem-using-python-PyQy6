import sys
import os
import sqlite3 as sqlite

from PyQt6.QtGui import QIcon

from calculate_interest import *
from addmember import *
from update import *
from voting import *
from delete import *
from firm_report import *
from bankrupt import *
from managefund import *
from credential import *
from animation import *
from firm_manage import *
from PyQt6 import QtCore, QtGui, QtWidgets


#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Database connection details

class Ui_Dashboard(object):
    def __init__(self):
        self.interest_thread = InterestCalculationThread()
        self.interest_thread.start()  # Start the interest calculation thread automatically

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 659)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QIcon(resource_path("image/icon.ico")))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("QFrame {\n"
                                 "    border: 2px solid #000;  /* Adds a 2px solid black border */\n"
                                 "    border-radius: 0px;     /* Optional: Adds rounded corners */\n"
                                 "    background-color: #653C87;  /* Optional: Adds a background color */\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, 7, -1, 3)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("  border:none;\n"
                                   "\n"
                                   "    background-color: white;  /* Slight color change on press */\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("  border:none;\n"
                                 "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_30.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_30.setMaximumSize(QtCore.QSize(0, 40))
        self.pushButton_30.setStyleSheet("/* Base style */\n"
                                         "QPushButton {\n"
                                         "  \n"
                                         "   \n"
                                         "    color: white;  /* Text color */\n"
                                         "    padding: 10px;\n"
                                         "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                         "}\n"
                                         "\n"
                                         "/* Hover effect */\n"
                                         "QPushButton:hover {\n"
                                         "  border: 2px solid;    /* Default border */\n"
                                         "    border-radius: 12px;  /* Rounded corners */\n"
                                         "    border-color: #ff0000;  /* Change border color on hover */\n"
                                         "    transform: scale(1.05);  /* Slightly increase size on hover */\n"
                                         "}\n"
                                         "\n"
                                         "/* Click effect */\n"
                                         "QPushButton:pressed {\n"
                                         "    transform: scale(0.95);  /* Slightly decrease size on click */\n"
                                         "}\n"
                                         "")
        self.pushButton_30.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("image\\d.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_30.setIcon(icon)
        self.pushButton_30.setIconSize(QtCore.QSize(60, 49))
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_4.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 147))
        self.frame_3.setMinimumSize(QtCore.QSize(16777215, 130))
        self.frame_3.setStyleSheet("border:none;\n"
                                   " border-top: 2px solid black;\n"
                                   "    background-color: white;  /* Slight color change on press */\n"
                                   "\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(-1, 9, -1, 7)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton.clicked.connect(self.load_content)
        self.pushButton.setStyleSheet("/* Base button style */\n"
                                      "QPushButton {\n"
                                      "    background-color: #9A79BA;  /* Green */\n"
                                      "    border: none;\n"
                                      "    color: white;\n"
                                      "    padding: 15px 32px;\n"
                                      "    text-align: center;\n"
                                      "    text-decoration: none;\n"
                                      "    display: inline-block;\n"
                                      "    font-size: 16px;\n"
                                      "    margin: 4px 2px;\n"
                                      "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                      "    cursor: pointer;\n"
                                      "    border-radius: 12px;  /* Rounded corners */\n"
                                      "}\n"
                                      "\n"
                                      "/* Button hover effect */\n"
                                      "QPushButton:hover {\n"
                                      "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                      "}\n"
                                      "\n"
                                      "/* Button click effect */\n"
                                      "QPushButton:pressed {\n"
                                      "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                      "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                      "}\n"
                                      "")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("image\\user.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(80, 75))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_10.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_10.setStyleSheet("/* Base button style */\n"
                                         "QPushButton {\n"
                                         "    background-color: #9A79BA;  /* Green */\n"
                                         "    border: none;\n"
                                         "    color: white;\n"
                                         "    padding: 15px 32px;\n"
                                         "    text-align: center;\n"
                                         "    text-decoration: none;\n"
                                         "    display: inline-block;\n"
                                         "    font-size: 16px;\n"
                                         "    margin: 4px 2px;\n"
                                         "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                         "    cursor: pointer;\n"
                                         "    border-radius: 12px;  /* Rounded corners */\n"
                                         "}\n"
                                         "\n"
                                         "/* Button hover effect */\n"
                                         "QPushButton:hover {\n"
                                         "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                         "}\n"
                                         "\n"
                                         "/* Button click effect */\n"
                                         "QPushButton:pressed {\n"
                                         "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                         "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                         "}\n"
                                         "")
        self.pushButton_10.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("image\\bankruptcy.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.bankrupt)
        self.gridLayout.addWidget(self.pushButton_10, 0, 7, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_3.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("image\\voting-box.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.voting)

        self.gridLayout.addWidget(self.pushButton_3, 0, 8, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_4.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("image\\social-media.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_8.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_8.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "")
        self.pushButton_8.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(resource_path("image\\name.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.credential)
        self.gridLayout.addWidget(self.pushButton_8, 0, 4, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_9.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "")
        self.pushButton_9.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(resource_path("image\\public-relations.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.clicked.connect(self.manage_firm)
        self.pushButton_9.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 5, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_6.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(resource_path("image\\update.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.update)
        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("  border:none;\n"
                                   "")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 8, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 7, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_5.setStyleSheet("/* Base button style */\n"
                                        "QPushButton {\n"
                                        "    background-color: #9A79BA;  /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 15px 32px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                        "    cursor: pointer;\n"
                                        "    border-radius: 12px;  /* Rounded corners */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button hover effect */\n"
                                        "QPushButton:hover {\n"
                                        "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Button click effect */\n"
                                        "QPushButton:pressed {\n"
                                        "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                        "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(resource_path("image\\equity.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.clicked.connect(self.funds)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("  border:none;\n"
                                    "")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("  border:none;\n"
                                    "")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
                                   "    border: none;  /* Removes the border */\n"
                                   "}\n"
                                   "")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_11.setMaximumSize(QtCore.QSize(130, 130))
        self.pushButton_11.setStyleSheet("/* Base button style */\n"
                                         "QPushButton {\n"
                                         "    background-color: #9A79BA;  /* Green */\n"
                                         "    border: none;\n"
                                         "    color: white;\n"
                                         "    padding: 15px 32px;\n"
                                         "    text-align: center;\n"
                                         "    text-decoration: none;\n"
                                         "    display: inline-block;\n"
                                         "    font-size: 16px;\n"
                                         "    margin: 4px 2px;\n"
                                         "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                         "    cursor: pointer;\n"
                                         "    border-radius: 12px;  /* Rounded corners */\n"
                                         "}\n"
                                         "\n"
                                         "/* Button hover effect */\n"
                                         "QPushButton:hover {\n"
                                         "    transform: scale(1.1);  /* Scale effect on hover */\n"
                                         "}\n"
                                         "\n"
                                         "/* Button click effect */\n"
                                         "QPushButton:pressed {\n"
                                         "    transform: scale(0.9);  /* Scale down effect on press */\n"
                                         "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                         "}\n"
                                         "")
        self.pushButton_11.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(resource_path("image\\auditor.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QtCore.QSize(80, 75))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.firm_report)
        self.gridLayout.addWidget(self.pushButton_11, 0, 6, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.frame_4.setStyleSheet("border:none; \n"
                                   "border-top: 2px solid black;\n"
                                   "    border-bottom: 2px solid black;\n"
                                   "\n"
                                   "    background-color: #E6D7FA;  /* Slight color change on press */\n"
                                   "\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(35, 9, 35, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(parent=self.frame_4)
        self.widget.setStyleSheet("border:none;\n"
                                  "background:white;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(parent=self.widget)
        self.frame_6.setStyleSheet("""
                   #frame_6 {
                       border: 3px solid #653C87;  /* Dark purple border */
                       background: white;          /* White background */
                   }
               """)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.widget)
        self.frame_7.setMinimumSize(QtCore.QSize(303, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(354, 16777215))
        self.frame_7.setStyleSheet("QFrame{\n"
                                   "border: 2px solid #000;  /* Adds a 2px solid black border */\n"
                                   "    border-radius: 0px;     /* Optional: Adds rounded corners */\n"
                                   "    background-color: #653C87;  /* Optional: Adds a background color */\n"
                                   "}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.lineEdit.setPlaceholderText("Search")  # Set placeholder text
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
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
                                    "    font-size: 18px; /* Font size */\n"
                                    "    transition: all 0.3s ease; /* Smooth transition */\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "    border-color: gray; /* Darker green border on focus */\n"
                                    "}\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.search_table)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 39))
        self.pushButton_2.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_2.clicked.connect(self.display1)

        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
                                        "        color: white;                /* White text */\n"
                                        "        border: 2px solid black;                /* No border */\n"
                                        "        border-radius: 5px;         /* Rounded corners */\n"
                                        "        font-size: 16px;             /* Font size */\n"
                                        "        cursor: pointer;             /* Pointer cursor on hover */\n"
                                        "    }\n"
                                        "    #pushButton_2:hover {\n"
                                        "        background-color: #45a049;  /* Darker green on hover */\n"
                                        "    }\n"
                                        "    #pushButton_2:pressed {\n"
                                        "        background-color: #397d3a;  /* Even darker green when pressed */\n"
                                        "        padding-left: 12px;         /* Slightly move the button when pressed */\n"
                                        "        padding-top: 12px;          /* Slightly move the button when pressed */\n"
                                        "    }")
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(resource_path("image\\reload.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 19))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_7)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
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
                                       "    margin: 1px; /* Margin between cells */\n"
                                       "    font-family: \'Arial\', sans-serif; /* Font for the table cells */\n"
                                       "    font-size: 18px; /* Font size for the table cells */\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: #A8A2AB; /* Green header background */\n"
                                       "    color: white; /* White text in the header */\n"
                                       "    padding: 4px; /* Padding in header cells */\n"
                                       "    border: 1px solid #dddddd; /* Border for header cells */\n"
                                       "    font-family: \'Verdana\', sans-serif; /* Font for the header */\n"
                                       "    font-size: 18px; /* Font size for the header */\n"
                                       "    font-weight: bold; /* Bold font for the header */\n"
                                       "}\n"
                                       "            QScrollBar:vertical {\n"
                                       "                \n"
                                       "                background: #653C87;\n"
                                       "                \n"
                                       "         \n"
                                       "            }\n"
                                       "\n"
                                       "")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(18)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_5.setStyleSheet("background:white;\n"
                                   "  border:none;\n"
                                   "")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(1)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(178, 18, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_12 = QtWidgets.QLabel(parent=self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("margin-top: 6px;")
        self.horizontalLayout.addWidget(self.label_12)
        spacerItem1 = QtWidgets.QSpacerItem(188, 18, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_29 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_29.setMinimumSize(QtCore.QSize(60, 22))
        self.pushButton_29.setMaximumSize(QtCore.QSize(73, 35))
        self.pushButton_29.clicked.connect(self.close_app)
        self.pushButton_29.setStyleSheet("/* Base style */\n"
                                         "QPushButton#pushButton_29 {\n"
                                         "    background-color: red;  /* Red background */\n"
                                         "    border: 2px solid black;\n"
                                         "    border-radius: 12px;  /* Rounded corners */\n"
                                         "    color: white;\n"
                                         "    text-align: center;\n"
                                         "    font-size: 16px;\n"
                                         "    transition: all 0.3s ease;  /* Smooth transition for all properties */\n"
                                         "}\n"
                                         "\n"
                                         "/* Hover effect */\n"
                                         "QPushButton#pushButton_29:hover {\n"
                                         "    transform: scale(1.1);  /* Slightly increase size on hover */\n"
                                         "}\n"
                                         "\n"
                                         "/* Click effect */\n"
                                         "QPushButton#pushButton_29:pressed {\n"
                                         "    transform: scale(0.95);  /* Slightly decrease size on click */\n"
                                         "    background-color: #3e8e41;  /* Darker green when clicked */\n"
                                         "}\n"
                                         "")
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout.addWidget(self.pushButton_29)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kubera Financial Guardians"))
        self.label.setText(_translate("MainWindow", "Kubera Financial Guardians"))
        self.label_5.setText(_translate("MainWindow", "Manage Firm"))
        self.label_9.setText(_translate("MainWindow", "Update  Detail"))
        self.label_4.setText(_translate("MainWindow", "Voting"))
        self.label_6.setText(_translate("MainWindow", "Firm Report"))
        self.label_2.setText(_translate("MainWindow", "Bankrupt Member"))
        self.label_11.setText(_translate("MainWindow", "Add Member"))
        self.label_10.setText(_translate("MainWindow", "Delete Member"))
        self.label_8.setText(_translate("MainWindow", "Member Funds"))
        self.label_7.setText(_translate("MainWindow", "Member Credential  "))
        self.lineEdit.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "username"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.display1()
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_12.setText(_translate("MainWindow", "© 2024 Kubera Financial Guardians. All rights reserved.\n"
                                                       ""))
        self.pushButton_29.setText(_translate("MainWindow", "CLOSE"))
        self.animation()

    def search_table(self, search_text):
        """ Searches the table for the given search text and displays the matching results. """
        search_text = search_text.lower()
        for row in range(self.tableWidget.rowCount()):
            row_visible = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item_text = item.text().lower()
                    if search_text in item_text:
                        row_visible = True
                        break
            self.tableWidget.setRowHidden(row, not row_visible)

    def display1(self):
        """ Fetches data from the SQLite database and populates the tableWidget. """
        try:
            # Connect to the SQLite database
            con = sqlite.connect(resource_path('db/firm_management.db'))  # Use your database name
            cursor = con.cursor()

            # Execute the SELECT query and fetch the data
            cursor.execute("SELECT userid, username FROM addmember")
            rows = cursor.fetchall()

            # Clear existing rows in the tableWidget
            self.tableWidget.setRowCount(0)

            # Add rows and populate them with data
            for row_data in rows:
                new_row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(new_row_position)
                for column, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget.setItem(new_row_position, column, item)

        except sqlite.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the database connection
            if con:
                con.close()

    def load_content(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_member()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)

    print("Content added to frame_6")  # Debugging print statement

    def update(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_update()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to update")  # Debugging print statement

    def delete(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_delete()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to frame_6")  # Debugging print statement

    def bankrupt(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_bank()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to bank")  # Debugging print statement

    def voting(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_wotingFrame()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statement

    def funds(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_managefund()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statementdadd

    def credential(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_credential()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statementdadd

    def manage_firm(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_Frame()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statementdadd

    def firm_report(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Ui_report()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statementdadd

    def animation(self):
        # Clear existing layout in frame_6
        layout = self.frame_6.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create an instance of Ui_ContentWidget from addmember.py and add it to frame_6
        self.content_widget = QtWidgets.QWidget()
        self.ui_content = Animation()
        self.ui_content.setupUi(self.content_widget)

        # Set layout if not already set
        if not self.frame_6.layout():
            self.frame_6_layout = QtWidgets.QVBoxLayout(self.frame_6)
            self.frame_6.setLayout(self.frame_6_layout)
        self.frame_6.layout().addWidget(self.content_widget)
        print("Content added to voting")  # Debugging print statementdadd

    def close_app(self):
        sys.exit()




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
