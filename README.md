# Customer Management Console Application

## Overview

This is a modular, console-based Python application for managing customer records. It was developed as part of a university assignment to demonstrate skills in structured programming, data validation, modularisation, and test-driven development.

The application allows users to:
- Display all customers
- View detailed information about a specific customer
- Add new customer records
- Edit existing customer records
- Delete customer records

## Features

- **Hard-coded sample data**: Initializes with 10 customer records upon launch.
- **Data Validation**: Input fields such as name, email, phone number, date, and balance are validated using custom logic.
- **User-Friendly Menu**: A clear, consistent interface that allows users to navigate actions with confirmation prompts.
- **Modular Codebase**: Organized into distinct modules for UI, data storage, validation, and operations.
- **Error Handling**: Prevents crashes due to bad input and guides users to correct mistakes.
- **Testing**: Manual test plan and automated tests written using Pytest (see `/tests` folder if applicable).

- ## Testing

This application has been tested using both **manual and automated testing approaches** to ensure reliability and correctness.

### Manual Testing

Manual tests are documented in the provided Excel file:
- `Manual_Test_Plan_CustomerApp.xlsx`

Each test includes:
- Test inputs
- Actions taken
- Expected vs actual results
- Screenshots as evidence

### ⚙Automated Unit Testing (Pytest)

Unit tests for core functionality (e.g., input validation, customer management logic) have been written using **Pytest**.

#### How to Run the Automated Tests

1. Install Pytest if not already installed:
2. Navigate to the root project folder in your terminal:
3. Run the tests with:
4. Pytest will discover and execute all test functions in `test_customer_manager.py` and return a pass/fail report.



## Sample Data Format

Each customer record contains:
- `id`: Unique integer ID
- `name`: Full name (String)
- `email`: Valid email address (String)
- `phone`: 10-digit phone number (String)
- `address`: Postal address (String)
- `membership`: Membership level (Gold, Silver, Bronze)
- `join_date`: Date in format YYYY-MM-DD
- `balance`: Account balance (Float)

## How to Run the Application

1. **Install Python 3.8+**
2. **Clone the Repository** or unzip the provided folder.
3. **Run the Application:**
   ```bash
   python main.py

   
---

### Author

Albert Cyriac


