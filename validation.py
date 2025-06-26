import re
from datetime import datetime

def validate_name(name):
    return isinstance(name, str) and len(name.strip()) > 0

def validate_email(email):
    return re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 10

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_balance(balance):
    return isinstance(balance, (int, float)) and balance >= 0
