from customer_data import customers
from validation import *
from datetime import datetime

class CustomerManager:
    def __init__(self):
        self.customers = []
        for c in customers:
            if self.validate_customer(c):
                self.customers.append(c)
            else:
                print(f"Invalid data skipped: {c}")

    def validate_customer(self, customer):
        return (validate_name(customer["name"]) and validate_email(customer["email"])
                and validate_phone(customer["phone"]) and validate_date(customer["join_date"])
                and validate_balance(customer["balance"]))

    def display_all(self):
        for c in self.customers:
            print(f"ID: {c['id']} | Name: {c['name']} | Email: {c['email']}")

    def add_customer(self):
        try:
            new = {
                "id": len(self.customers) + 1,
                "name": input("Name: "),
                "email": input("Email: "),
                "phone": input("Phone: "),
                "address": input("Address: "),
                "membership": input("Membership: "),
                "join_date": input("Join Date (YYYY-MM-DD): "),
                "balance": float(input("Balance: "))
            }
            if self.validate_customer(new):
                self.customers.append(new)
                print("Customer added successfully.")
            else:
                print("Validation failed. Customer not added.")
        except Exception as e:
            print(f"Error: {e}")

    def update_customer(self):
        try:
            cid = int(input("Enter customer ID: "))
            cust = next((c for c in self.customers if c["id"] == cid), None)
            if cust:
                cust["name"] = input("Name: ") or cust["name"]
                cust["email"] = input("Email: ") or cust["email"]
                cust["phone"] = input("Phone: ") or cust["phone"]
                print("Customer updated.")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input.")

    def delete_customer(self):
        try:
            cid = int(input("Enter customer ID to delete: "))
            cust = next((c for c in self.customers if c["id"] == cid), None)
            if cust:
                confirm = input(f"Confirm delete {cust['name']} (y/n): ")
                if confirm.lower() == "y":
                    self.customers.remove(cust)
                    print("Customer deleted.")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input.")

    def view_customer(self):
        try:
            cid = int(input("Enter customer ID to view: "))
            cust = next((c for c in self.customers if c["id"] == cid), None)
            if cust:
                print(cust)
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input.")

    def search_customer(self):
        term = input("Enter name to search: ").lower()
        results = [c for c in self.customers if term in c["name"].lower()]
        for c in results:
            print(f"{c['id']}: {c['name']}")

    def sort_customers(self):
        sorted_list = sorted(self.customers, key=lambda x: x["balance"], reverse=True)
        for c in sorted_list:
            print(f"{c['name']} - Balance: {c['balance']}")
