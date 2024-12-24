===================================================================
              KUBERA FINANCIAL GUARDIANS - README
===================================================================

Project Name: Kubera Financial Guardians
Version: 1.0.0
Developer: Akshat Faganiya
Academic Year: 2024-2025
===================================================================

Table of Contents:
1. Overview
2. Features
3. System Requirements
4. Installation Instructions
5. Usage Guide
6. Troubleshooting
7. Contact Information

===================================================================

1. OVERVIEW:
Kubera Financial Guardians is a financial management application designed 
to streamline user account registration, nominee management, and fund 
tracking with a user-friendly interface. The application incorporates 
robust validation and security measures to ensure accurate data handling 
and reliability.

===================================================================

2. FEATURES:
- User registration with detailed validation (name, Aadhar, email, etc.).
- Unique user ID generation.
- Nominee details management.
- Financial transaction tracking (deposits, credits).
- Email confirmation upon successful registration.
- Minimum deposit validation (₹1000 or above).
- Integration with SQLite for efficient database management.

===================================================================

3. SYSTEM REQUIREMENTS:

Hardware Requirements:
- Processor: 1 GHz or faster (dual-core recommended).
- RAM: Minimum 4 GB (8 GB recommended).
- Storage: 500 MB of free space.
- Display: 1024x768 or higher resolution.

Software Requirements:
- Python 3.8 or later (ensure it's added to PATH).
- PyQt6 (for GUI).
- SQLite (default with Python).
- Internet connection for email functionality.

===================================================================

4. INSTALLATION INSTRUCTIONS:

Step 1: Install Python
- Download Python from https://www.python.org/downloads/.
- During installation, ensure the "Add Python to PATH" option is checked.

Step 2: Install Dependencies
- Open a terminal or command prompt.
- Navigate to the project folder.
- Run the following command to install dependencies:

Step 3: Run the Application
- In the terminal or command prompt, navigate to the project folder.
- Execute the following command:

===================================================================

5. USAGE GUIDE:

- Launch the application.
- Fill in the user registration form with the required details:
- Name
- Mobile number
- Aadhar number
- Email address
- City
- Nominee name and Aadhar number
- Deposit amount (minimum ₹1000).
- Click "Submit" to register the user.
- If successful, a confirmation email will be sent to the registered email address.
- All details are securely stored in the SQLite database.

===================================================================

6. TROUBLESHOOTING:

- **Issue**: The application doesn't start.
- Ensure Python 3.8 or later is installed.
- Verify all dependencies are installed using:
  ```
  pip install -r requirements.txt
  ```

- **Issue**: Email confirmation not sent.
- Check your internet connection.
- Verify the email credentials in the application.

- **Issue**: Validation errors during registration.
- Double-check the entered details (e.g., Aadhar, email format, deposit amount).

- **Issue**: Database connection failed.
- Ensure the SQLite database file (`firm_management.db`) is in the correct path.

===================================================================

7. CONTACT INFORMATION:

For any issues, questions, or suggestions, please contact:
- Developer: Akshat Faganiya
- Email: [your_email@example.com]
- College: Kamani Science and Prataprai Arts College

===================================================================
