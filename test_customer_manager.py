# test_customer_manager.py

from customer_manager import validate_email, validate_phone

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("wrong-email") == False

def test_validate_phone():
    assert validate_phone("0123456789") == True
    assert validate_phone("abc123") == False

from customer_manager import add_customer, customer_list

def test_add_customer():
    add_customer("001", "John Doe", "john@example.com", "0123456789", "123 Street", "1990-01-01", "In Progress", 0.0)
    assert any(c.customer_id == "001" for c in customer_list)
