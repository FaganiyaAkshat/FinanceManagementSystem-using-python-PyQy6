import sys
import sqlite3  # Using SQLite for database management

from PyQt6.QtGui import QIcon

from backend import *
from dashboard import *  # Import the dashboard class
from PyQt6 import QtCore, QtGui, QtWidgets
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_image_path(filename):
    """ Get the image path based on the execution context (development or bundled) """
    if hasattr(sys, '_MEIPASS'):
        return resource_path(filename)  # Running as a bundled executable
    else:
        return filename  # Running in development


class Ui_MainWindow(object):
    message = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Firm Management")
        MainWindow.resize(839, 600)
        MainWindow.setMinimumSize(QtCore.QSize(839, 0))
        MainWindow.setStyleSheet("")
        MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        MainWindow.setWindowIcon(QIcon(resource_path("image/icon.ico")))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        image_path = get_image_path("image/add.png")
        print(image_path)
        self.frame.setStyleSheet("#frame{\n"
                                 f"    background-image: url({image_path});\n"
                                 "    background-repeat: no-repeat;\n"

                                 "}\n"
                                 "QFrame {\n"
                                 "    background: transparent;\n"
                                 "    border:none;\n"
                                 "}\n"
                                 "QFrame {\n"
                                 "    border: none;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setStyleSheet("border:0px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 201))
        self.frame_4.setStyleSheet("QFrame {\n"
                                   "    border: none;\n"
                                   "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(410, -20, 406, 580))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setItalic(True)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("border:none;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.frame_5)
        self.widget.setMaximumSize(QtCore.QSize(431, 16777215))
        self.widget.setStyleSheet("QWidget {\n"
                                  "    border: none;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(160, 0, 124, 44))
        self.label.setStyleSheet("font: 28pt \"Bernard MT Condensed\";")
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 111, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 223, 47))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    background-color: #90e0ef;  /* Set background color to black */\n"
                                    "    color: black;  /* Set text color to white for better contrast */\n"
                                    "    border: 2px solid #555;  /* Initial border color */\n"
                                    "   \n"
                                    "    border-radius: 10px;  /* Rounded corners */\n"
                                    "    padding: 10px;  /* Add some padding for better look */\n"
                                    "}\n"
                                    "\n"
                                    "/* Hover effect */\n"
                                    "QLineEdit:hover {\n"
                                    "    border-color: #9A79BA;  /* Change border color on hover to give a visual effect */\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 104, 47))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 140, 221, 47))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    background-color: #90e0ef;  /* Set background color to black */\n"
                                      "    color: black;  /* Set text color to white for better contrast */\n"
                                      "    border: 2px solid #555;  /* Initial border color */\n"
                                      "   \n"
                                      "    border-radius: 10px;  /* Rounded corners */\n"
                                      "    padding: 10px;  /* Add some padding for better look */\n"
                                      "}\n"
                                      "\n"
                                      "/* Hover effect */\n"
                                      "QLineEdit:hover {\n"
                                      "    border-color: #9A79BA;  /* Change border color on hover to give a visual effect */\n"
                                      "}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("/* Base button style */\n"
                                      "QPushButton {\n"
                                      "    background-color: #00b4d8; /* Initial background color */\n"
                                      "    border: none;\n"
                                      "    color: black;\n"
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
                                      "/* Hover effect */\n"
                                      "QPushButton:hover {\n"
                                      "border:2px solid #9A79BA;\n"
                                      "    background-color: #90e0ef; /* Change background color on hover */\n"
                                      "    transform: scale(1.1);  /* Slightly increase size on hover */\n"
                                      "}\n"
                                      "\n"
                                      "/* Click effect */\n"
                                      "QPushButton:pressed {\n"
                                      "    transform: scale(0.9);  /* Slightly decrease size on click */\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_button_clicked)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(110, 190, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Firm Management"))
        self.label.setText(_translate("MainWindow", "     Login"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

    ############################## event####################
    def on_button_clicked(self):

        _translate = QtCore.QCoreApplication.translate
        name = self.lineEdit.text()
        pas = self.lineEdit_2.text()

        try:
            con = sqlite3.connect(resource_path('db/firm_management.db'))
            cursor = con.cursor()
            query = "SELECT * FROM admin WHERE uname = ? AND password = ?"
            cursor.execute(query, (name, pas))
            result = cursor.fetchone()

            if result:
                print("Login successful, loading dashboard...")
                self.window2 = QtWidgets.QMainWindow()
                self.ui = Ui_Dashboard()  # Ensure Ui_Dashboard is defined and imported correctly
                self.ui.setupUi(self.window2)
                self.window2.show()
                MainWindow.close()
            else:
                self.label_4.setText(_translate("MainWindow", "Invalid username and password"))

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.label_4.setText(_translate("MainWindow", "Database connection error"))
        finally:
            if 'con' in locals():
                con.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())