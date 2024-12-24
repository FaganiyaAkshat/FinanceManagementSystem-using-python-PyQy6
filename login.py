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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        MainWindow.setWindowIcon(QIcon(resource_path("image/icon.ico")))
        # Create central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a QLabel to display the background image
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setObjectName("background_label")
        self.background_label.setGeometry(MainWindow.rect())
        self.background_label.setScaledContents(True)

        # Load the image
        image_path =resource_path( "image/complete.png")  # Adjust the path as needed
        pixmap = QtGui.QPixmap(image_path)

        # Set the image to the label
        self.background_label.setPixmap(pixmap)

        # Adjust size dynamically
        MainWindow.resizeEvent = self.resizeEvent

        # Set the central widget to the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Create login UI elements
        self.create_login_ui()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_login_ui(self):
        """Create the login UI elements within a QFrame."""
        # Create a frame for the login form
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 250, 500, 350))  # Adjusted height of the frame
        self.frame.setStyleSheet("background-color: rgba(); border-radius: 10px;")  # Optional styling

        # Login heading
        self.label_heading = QtWidgets.QLabel(self.frame)
        self.label_heading.setGeometry(QtCore.QRect(150, 20, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        self.label_heading.setFont(font)
        self.label_heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_heading.setText("Login")  # Added login heading

        # Username label
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 85, 204, 47))
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Username input

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 221, 47))
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.lineEdit.setStyleSheet(self.get_line_edit_style())
        self.lineEdit.setObjectName("lineEdit")

        # Password label
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 104, 47))  # Increased vertical gap
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Password input
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 221, 47))  # Increased vertical gap
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.lineEdit_2.setStyleSheet(self.get_line_edit_style())
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Login button
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 240, 101, 51))  # Adjusted position for button
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(self.get_button_style())
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Login")
        self.pushButton.clicked.connect(self.on_button_clicked)

        # Error message label for invalid credentials

        # Additional label for invalid username/password message
        self.label_invalid = QtWidgets.QLabel(self.frame)
        self.label_invalid.setGeometry(QtCore.QRect(130, 210, 341, 21))  # Adjusted position
        self.label_invalid.setFont(font)
        self.label_invalid.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_invalid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_invalid.setObjectName("label_invalid")
        self.label_invalid.setText("Invalid username or password.")  # Show invalid message
        self.label_invalid.hide()
    def get_line_edit_style(self):
        """Return the style for line edits."""
        return (
            "QLineEdit {\n"
            "    background-color: #90e0ef;\n"
            "    color: black;\n"
            "    border: 2px solid #555;\n"
            "    border-radius: 10px;\n"
            "    padding: 10px;\n"
            "    font-size: 15px;\n"
            "    font-weight: 700;\n"
            
            "}\n"
            "QLineEdit:hover {\n"
            "    border-color: #9A79BA;\n"
            "}"
        )

    def get_button_style(self):
        """Return the style for buttons."""
        return (
            "QPushButton {\n"
            "    background-color: #00b4d8;\n"
            "    border: none;\n"
            "    color: black;\n"
            "    text-align: center;\n"
            "    border-radius: 12px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: #90e0ef;\n"
            "    transform: scale(1.1);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    transform: scale(0.9);\n"
            "}"
        )

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
                    self.label_invalid.show()

            except sqlite3.Error as e:
                print(f"Database error: {e}")

            finally:
                if 'con' in locals():
                    con.close()
    def resizeEvent(self, event):
        """Handle resizing of the main window to fit the background image."""
        self.background_label.setGeometry(self.centralwidget.rect())
        event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kubera Financial Management"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())