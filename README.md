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

