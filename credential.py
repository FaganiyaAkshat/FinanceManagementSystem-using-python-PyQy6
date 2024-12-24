from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QPushButton, QHBoxLayout, QWidget, QMessageBox
import sqlite3  # Changed from mysql.connector to sqlite3
import os
from datetime import datetime

from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_credential(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(720, 450)  # Reduced the frame width
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(parent=Frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)  # Added margins for better spacing
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Title label
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 59))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 58))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
                                   "background:none;\n"
                                   "font: 700 20pt \"Verdana\";\n"
                                   "color:#653C87;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3)

        # Table area
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setStyleSheet("QFrame {\n"
                                   "    border: 2px solid #000;\n"
                                   "    border-radius: 5px;\n"
                                   "    background-color: #9A79BA;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)  # Added padding for table
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Search bar
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))  # Adjusted height for a more compact look
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    background-color: #ffffff;\n"
                                    "    border: 2px solid black;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 10px;\n"
                                    "    font-family: 'Arial', sans-serif;\n"
                                    "    font-size: 18px;\n"
                                    "    transition: all 0.3s ease;\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "    border-color: gray;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Search")
        self.verticalLayout_4.addWidget(self.lineEdit)

        # Connect the search bar to the search function
        self.lineEdit.textChanged.connect(self.search_table)

        # Table Widget (Main table to display data)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: 1px solid #888888;
                border-radius: 10px;
                background-color: #f0f0f0;
                font-family: 'Arial', sans-serif;
                font-size: 17px;
                width: 100%;
            }
            QTableWidget::item {
                border: 1px solid #888888;
                padding: 5px;
                font-family: 'Arial', sans-serif;
                font-size: 17px;
            }
            QHeaderView::section {
                background-color: #757575;
                color: white;
                padding: 4px;
                border: 1px solid #dddddd;
                font-family: 'Verdana', sans-serif;
                font-size: 17px;
                font-weight: bold;
            }

            QScrollBar:vertical {
                background-color: #9A79BA;
                border-radius: 5px;
                width: 12px;
            }
            QScrollBar:horizontal {
                background-color: #9A79BA;
                border-radius: 5px;
                height: 12px;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background-color: #4C2A60;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
                background-color: #3B1A44;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;
            }
        """)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Username", "Action"])

        # Stretch columns for proportional sizing
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.display1()  # Populate the table

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Download credential"))

    def display1(self):
        try:
            # Connect to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
            cursor = con.cursor()

            cursor.execute("SELECT id, username FROM funds")  # Only fetching id and username
            rows = cursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_data in rows:
                new_row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(new_row_position)

                for column, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(new_row_position, column, item)

                # Action Widget (where the buttons will be)
                action_widget = QWidget()
                action_layout = QHBoxLayout(action_widget)
                action_layout.setContentsMargins(0, 0, 0, 0)
                action_widget.setStyleSheet("background-color: #f0f0f0;")  # Matching the table background color

                # Create Print Credential button (Green)
                print_button = QPushButton("Print Credential")
                print_button.setFixedWidth(120)
                print_button.setStyleSheet(
                    "QPushButton {\n"
                    "    background-color:  #4CAF50;\n"  # Set button background to green
                    "    color: white;\n"
                    "    border-radius: 5px;\n"
                    "    font-family: 'Arial', sans-serif;\n"
                    "    font-weight: bold;\n"
                    "    font-size: 14px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "    background-color: #45a049;\n"
                    "}")
                print_button.clicked.connect(lambda _, row=row_data: self.on_print_clicked(row))

                # Create Print Entry button (Red)
                print_entry_button = QPushButton("Print Entry")
                print_entry_button.setFixedWidth(120)
                print_entry_button.setStyleSheet(
                    "QPushButton {\n"
                    "    background-color:  #f44336;\n"  # Set button background to red
                    "    color: white;\n"
                    "    border-radius: 5px;\n"
                    "    font-family: 'Arial', sans-serif;\n"
                    "    font-weight: bold;\n"
                    "    font-size: 14px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "    background-color: #e53935;\n"
                    "}")
                # Add a different action for the Print Entry button if needed
                print_entry_button.clicked.connect(lambda _, row=row_data: self.on_print_entry_clicked(row))

                action_layout.addWidget(print_button)
                action_layout.addWidget(print_entry_button)

                self.tableWidget.setCellWidget(new_row_position, 2, action_widget)

            cursor.close()
            con.close()

        except sqlite3.Error as e:  # Changed to sqlite3.Error
            print("SQLite Error:", e)

    def search_table(self):
        """
        Searches the table for the given search text and displays the matching results.
        """
        search_text = self.lineEdit.text().lower()  # Get the search text from the lineEdit

        # Iterate through the table rows and columns
        for row in range(self.tableWidget.rowCount()):
            row_visible = False  # Assume the row should be hidden initially

            for col in range(self.tableWidget.columnCount() - 1):  # Exclude the action column
                item = self.tableWidget.item(row, col)
                if item:
                    item_text = item.text().lower()  # Convert the item text to lowercase for case-insensitive search
                    if search_text in item_text:  # Check if the search text is in the item text
                        row_visible = True  # If found, set row to visible
                        break  # No need to check other cells in this row

            self.tableWidget.setRowHidden(row, not row_visible)  # Set the row visibility based on search result

    def on_print_clicked(self, row_data):
        # Generate PDF when the button is clicked for that row
        id = row_data[0]
        username = row_data[1]
        self.generate_pdf(id, username)

    def on_print_entry_clicked(self, row_data):
        # Print entry-related action
        print(f"Print Entry button clicked for ID: {row_data[0]}, Username: {row_data[1]}")

        try:
            # Establish the connection to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
            cursor = con.cursor()

            # Query for data based on user ID (u_id)
            cursor.execute("SELECT t_amount, t_type, t_time FROM entry WHERE u_id = ?",
                           (row_data[0],))  # Changed to parameterized query

            # Fetch all results, since we expect multiple rows
            results = cursor.fetchall()

            if results:  # Check if there are any results
                for result in results:  # Iterate through all rows
                    t_amount = result[0]
                    t_type = result[1]
                    t_time = result[2]

                    # Print the results (or process further as needed)
                    print(f"Amount: {t_amount}, Type: {t_type}, Time: {t_time}")
            else:
                print("No records found for this user ID.")

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")
        finally:
            # Close the connection to the database
            if con:
                con.close()

    def generate_pdf(self, id, username):
        username = None
        aadhar = None
        mobile = None
        email = None
        city = None
        n_name = None
        n_aadhar = None
        date = None
        loan = None
        fund = None
        try:

            con = sqlite3.connect(resource_path('db/firm_management.db'))  # Changed to SQLite connection
            cursor = con.cursor()
            cursor.execute("SELECT * FROM addmember WHERE userid = ?", (id,))  # Changed to parameterized query
            result = cursor.fetchone()
            if result is not None:
                username = result[2]
                aadhar = result[3]
                mobile = result[4]
                email = result[5]
                city = result[6]
                n_name = result[8]
                n_aadhar = result[9]
                date = result[7]
                # Example data for the user
            cursor.execute("SELECT * FROM funds WHERE id = ?", (id,))  # Changed to parameterized query
            result = cursor.fetchone()
            if result is not None:
                amount = result[3]
                if amount > 0:
                    fund = result[3]
                    loan = 0
                else:
                    fund = 0
                    loan = result[3]
            mobile_number = mobile
            email = email
            amount_due = fund
            amount_loaned = loan
            join_date = date
            city = city
            nominee_name = n_name
            user_aadhar_number = n_aadhar
            nominee_aadhar_number = aadhar

            # Generate the PDF file with user info on the Desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            file_name = f"credential_{id}_{username}.pdf"
            file_path = os.path.join(desktop_path, file_name)

            c = canvas.Canvas(file_path, pagesize=letter)
            back = resource_path('image/d.jpg')
            # Define the path to the logo
            logo_path = resource_path('image/d.png')  # Absolute path to the logo image

            # Check if the logo exists and draw it with transparency
            if os.path.exists(logo_path):
                logo_width = 400  # Width of the logo
                logo_height = 400  # Height of the logo
                # Calculate center of the page
                x_position = (letter[0] - logo_width) / 2  # Center horizontally
                y_position = (letter[1] - logo_height) / 2  # Center vertically

                # Set transparency (alpha)
                c.setFillAlpha(0.3)  # Set transparency level (0.0 to 1.0, where 0 is fully transparent)
                c.setStrokeColor(colors.white)  # White border (optional, no border here)
                c.setLineWidth(0)  # No border thickness
                c.drawImage(logo_path, x_position, y_position, width=logo_width, height=logo_height,
                            mask='auto')  # Draw image with transparency
            else:
                print(f"Error: Logo file not found at {logo_path}")  # Debugging message if logo not found

            # Title at the top of the page (centered and with a large font)
            c.setFont("Helvetica-Bold", 32)
            c.setFillColor(colors.HexColor("#4C2A60"))
            title_width = c.stringWidth("Kubera Financial Guardians", "Helvetica-Bold", 32)
            c.drawString((letter[0] - title_width) / 2, 740, "Kubera Financial Guardians")

            # Subheading (User info)
            c.setFont("Helvetica", 12)
            welcome_text = f"\tWelcome {username}, Guardians of Kubera Financial! We are delighted to have you on board. Unlocking possibilities, together. Transforming the future, today. Excellence is our standard, guardianship is our pride."

            # Set up the styles for the Paragraph
            styles = getSampleStyleSheet()
            style = styles["Normal"]
            style.fontSize = 12
            style.textColor = colors.HexColor("#A9A9A9")

            # Create a Paragraph object with the welcome text and apply the style
            paragraph = Paragraph(welcome_text, style)

            # Position the paragraph and draw it on the canvas
            y_position = 680
            width = letter[0] - 144
            paragraph.wrapOn(c, width, 10000)
            paragraph.drawOn(c, 72, y_position)

            # User details
            y_position = 630
            c.setFont("Helvetica", 18)
            c.setFillColor(colors.black)

            c.drawString(72, y_position, f"Name: {username}")
            y_position -= 50
            c.drawString(72, y_position, f"Mobile Number: {mobile_number}")
            y_position -= 50
            c.drawString(72, y_position, f"Email: {email}")
            y_position -= 50
            c.drawString(72, y_position, f"ID: {id}")
            y_position -= 50
            c.drawString(72, y_position, f"Amount Credit Rs: {amount_due}")
            y_position -= 50
            c.drawString(72, y_position, f"Amount Loaned Rs: {amount_loaned}")
            y_position -= 50
            c.drawString(72, y_position, f"Join Date: {join_date}")
            y_position -= 50
            c.drawString(72, y_position, f"City: {city}")
            y_position -= 50
            c.drawString(72, y_position, f"Nominee Name: {nominee_name}")
            y_position -= 50
            c.drawString(72, y_position, f"User Aadhar Number: {user_aadhar_number}")
            y_position -= 50
            c.drawString(72, y_position, f"Nominee Aadhar Number: {nominee_aadhar_number}")
            y_position -= 50

            # Closing message at the bottom
            closing_text = f"Please any kind of changes are possible in the future then kindly contact the firm +91-8200641807."
            paragraph = Paragraph(closing_text, style)
            y_position = 30
            paragraph.wrapOn(c, width, 10000)
            paragraph.drawOn(c, 72, y_position)

            # Add a page break and terms and conditions
            c.showPage()
            logo_path = resource_path('image/d.png')  # Absolute path to the logo image

            # Check if the logo exists and draw it with transparency
            if os.path.exists(logo_path):
                logo_width = 400  # Width of the logo
                logo_height = 400  # Height of the logo
                # Calculate center of the page
                x_position = (letter[0] - logo_width) / 2  # Center horizontally
                y_position = (letter[1] - logo_height) / 2  # Center vertically

                # Set transparency (alpha)
                c.setFillAlpha(0.3)  # Set transparency level (0.0 to 1.0, where 0 is fully transparent)
                c.setStrokeColor(colors.white)  # White border (optional, no border here)
                c.setLineWidth(0)  # No border thickness
                c.drawImage(logo_path, x_position, y_position, width=logo_width, height=logo_height,
                            mask='auto')  # Draw image with transparency
            else:
                print(f"Error: Logo file not found at {logo_path}")  # Debugging message if logo not found

            # Terms and Conditions Title (centered)
            c.setFont("Helvetica-Bold", 24)
            c.setFillColor(colors.HexColor("#4C2A60"))
            terms_title_width = c.stringWidth("Terms and Conditions", "Helvetica-Bold", 24)
            c.drawString((letter[0] - terms_title_width) / 2, 750, "Terms and Conditions")

            # Terms and conditions content
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.HexColor("#000000"))
            y_position = 710  # Starting Y position for terms text
            c.drawString(72, y_position, "1. The user must ensure all payments are made on time to avoid penalties.")
            y_position -= 18
            c.drawString(72, y_position,
                         "2. The loan is provided with the agreement of paying back the amount within the specified time frame.")
            y_position -= 18
            c.drawString(72, y_position,
                         "3. The nominee’s details must be kept updated in case of any emergency or requirement.")
            y_position -= 18
            c.drawString(72, y_position, "4. The user agrees to provide accurate personal and financial information.")
            y_position -= 18
            c.drawString(72, y_position, "5. The company reserves the right to revise the terms at any point.")
            y_position -= 18
            c.drawString(72, y_position,
                         "6. Any disputes will be resolved as per the company’s guidelines and policies.")
            y_position -= 18
            c.drawString(72, y_position,
                         "7. The user is responsible for safeguarding their Aadhar details and should report any fraud immediately.")
            y_position -= 18

            # Additional privacy policies
            c.drawString(72, y_position, "8. The company ensures that all personal data is kept confidential.")
            y_position -= 18
            c.drawString(72, y_position, "    Data will not be shared with third parties without consent.")
            y_position -= 18

            c.drawString(72, y_position,
                         "9. All users have the right to request deletion of their personal data at any time.")
            y_position -= 18
            c.drawString(72, y_position, "    Requests for data deletion will be processed within 30 days.")
            y_position -= 18

            c.drawString(72, y_position,
                         "10. The company takes all reasonable measures to ensure the security of personal data.")
            y_position -= 18
            c.drawString(72, y_position, "    However, users are advised to take care of their own privacy as well.")
            y_position -= 18

            c.drawString(72, y_position,
                         "11. The company is not responsible for any loss of data caused by third-party actions.")
            y_position -= 18
            c.drawString(72, y_position, "    Users should report any suspicious activity immediately.")
            y_position -= 18

            c.drawString((letter[0] - terms_title_width) / 2, 50,
                         "@2024 Kubera Financial Guardians . All Rights Reserved.")
            # Save the PDF after adding all content
            QMessageBox.warning(None, 'Validation Error', 'Download PDF successfully on location {}'.format(file_path))

            c.save()
        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")
            QMessageBox.warning(None, 'Validation Error', 'Error occurred while creating the PDF')

    def on_print_entry_clicked(self, row_data):
        # Print entry-related action
        print(f"Print Entry button clicked for ID: {row_data[0]}, Username: {row_data[1]}")

        try:
            # Establish the connection to the SQLite database
            con = sqlite3.connect(resource_path('db/firm_management.db'))  # SQLite connection
            cursor = con.cursor()

            # Query for account holder name from addmember table
            cursor.execute("SELECT username FROM addmember WHERE userid = ?", (row_data[0],))
            account_holder = cursor.fetchone()

            if account_holder:
                username = account_holder[0]
                print(f"Account holder's name: {username}")
            else:
                print("No account holder found.")
                return  # Exit if no account holder found

            # Query for transaction details based on user ID (u_id)
            cursor.execute("SELECT t_amount, t_type, t_time FROM entry WHERE u_id = ?", (row_data[0],))
            results = cursor.fetchall()

            # Query for total balance from the funds table
            cursor.execute("SELECT SUM(funds) FROM funds WHERE id = ?", (row_data[0],))
            total_balance = cursor.fetchone()[0] or 0.0  # Default to 0.0 if no funds

            if results:  # Check if there are any results
                # Generate PDF for the results and include account holder name and total balance
                pdf_file_path = self.generate_pdf1(row_data[0], username, results, total_balance)

                # Show success message box
                QMessageBox.warning(None, 'Success', f'Download PDF successfully at: {pdf_file_path}')
            else:
                QMessageBox.warning(None, 'Success', f'No record found.')

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection to the database
            if con:
                con.close()

    def generate_pdf1(self, id, username, results, total_balance):
        try:
            from fpdf import FPDF
            import os

            # Create PDF instance
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()

            # Title of the PDF (Large title at the top of the page)
            pdf.set_font('Arial', 'B', 24)
            pdf.set_text_color(76, 42, 96)  # Title color #4C2A60
            pdf.cell(200, 10, txt="Kubera Financial Guardians", ln=True, align='C')
            pdf.ln(10)

            # Display account holder's name just below the title
            pdf.set_font('Arial', 'I', 16)
            pdf.set_text_color(0, 0, 0)  # Set text color to black for account holder name
            pdf.cell(200, 10, txt=f"Account Holder: {username}", ln=True, align='C')
            pdf.ln(15)
            pdf.set_font('Arial', 'I', 10)
            pdf.cell(200, 10,
                     txt=f"Note : The actually profit/loss does not contain interest provided by the firm because of your consideration.",
                     ln=True, align='C')

            # Add table headers
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(35, 10, 'Credit Amount', 1, 0, 'C')
            pdf.cell(40, 10, 'Credit Time', 1, 0, 'C')
            pdf.cell(35, 10, 'Debit Amount', 1, 0, 'C')
            pdf.cell(40, 10, 'Debit Time', 1, 0, 'C')
            pdf.cell(45, 10, 'Profit/Loss', 1, 1, 'C')  # Header for Profit/Loss

            # Variables to calculate total credit, debit, and profit/loss amounts
            total_credit = 0.0
            total_debit = 0.0
            total_profit_loss = 0.0

            # Add transaction details in tabular format
            pdf.set_font('Arial', '', 12)

            for result in results:
                t_amount = float(result[0])
                t_type = result[1]
                t_time = result[2]

                if t_type.lower() == 'credit':
                    # Credit transactions
                    pdf.cell(35, 10, f"{t_amount:.2f}", 1, 0, 'C')  # Display with 2 decimal places
                    pdf.cell(40, 10, str(t_time), 1, 0, 'C')  # Adjusted width for time
                    pdf.cell(35, 10, '', 1, 0, 'C')  # Empty for Debit Amount
                    pdf.cell(40, 10, '', 1, 0, 'C')  # Empty for Debit Time

                    # Calculate Profit/Loss (Credit - Debit)
                    profit_loss = t_amount  # In this case, Credit is positive, Debit is not yet added
                    pdf.cell(45, 10, f"{profit_loss:+.2f}", 1, 1, 'C')  # Display profit/loss with 2 decimal places

                    # Add the amount to the total credit
                    total_credit += t_amount
                    total_profit_loss += profit_loss

                elif t_type.lower() == 'debit':
                    # Debit transactions
                    pdf.cell(35, 10, '', 1, 0, 'C')  # Empty for Credit Amount
                    pdf.cell(40, 10, '', 1, 0, 'C')  # Empty for Credit Time
                    pdf.cell(35, 10, f"{t_amount:.2f}", 1, 0, 'C')  # Display with 2 decimal places
                    pdf.cell(40, 10, str(t_time), 1, 0, 'C')  # Adjusted width for time

                    # Calculate Profit/Loss (Credit - Debit)
                    profit_loss = -t_amount  # Debit is negative, so subtract it from Credit
                    pdf.cell(45, 10, f"{profit_loss:+.2f}", 1, 1, 'C')  # Display profit/loss with 2 decimal places

                    # Add the amount to the total debit
                    total_debit += t_amount
                    total_profit_loss += profit_loss

            # Add the total row at the bottom (Credit, Debit, Profit/Loss)
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(35, 10, f"Total: {total_credit:.2f}", 1, 0, 'C')  # Total credit with 2 decimal places
            pdf.cell(40, 10, '', 1, 0, 'C')  # Empty for Time
            pdf.cell(35, 10, f"Total: {total_debit:.2f}", 1, 0, 'C')  # Total debit with 2 decimal places
            pdf.cell(40, 10, 'Total Profit/Loss', 1, 0, 'C')  # Empty for Time
            pdf.cell(45, 10, f"{total_profit_loss:+.2f}", 1, 1,
                     'C')  # Total profit/loss with 2 decimal places

            interest = abs(total_profit_loss - total_balance)
            pdf.cell(155, 10, "Interest :", 1, 0, 'C')
            pdf.cell(45, 10, f"{interest:+.2f}", 1, 1, 'C')

            pdf.cell(155, 10, "Total Balance in Firm:", 1, 0, 'C')
            pdf.cell(45, 10, f"{total_balance:.2f}", 1, 1, 'C')

            # Get the desktop path and save the PDF there
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            pdf_file_path = os.path.join(desktop_path, f"Transaction_Entries_{id}.pdf")

            # Output PDF to file
            pdf.output(pdf_file_path)

            return pdf_file_path

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")
            QMessageBox.warning(None, 'Error', 'Error occurred while creating the PDF')


# To run the application
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_credential()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
