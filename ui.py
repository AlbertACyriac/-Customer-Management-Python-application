from customer_manager import CustomerManager

manager = CustomerManager()

def display_main_menu():
    while True:
        print("\n=== Customer Management System ===")
        print("1. Display All Customers")
        print("2. Add Customer")
        print("3. Amend Customer")
        print("4. Delete Customer")
        print("5. View Customer by ID")
        print("6. Search by Name")
        print("7. Sort by Balance")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.display_all()
        elif choice == "2":
            manager.add_customer()
        elif choice == "3":
            manager.update_customer()
        elif choice == "4":
            manager.delete_customer()
        elif choice == "5":
            manager.view_customer()
        elif choice == "6":
            manager.search_customer()
        elif choice == "7":
            manager.sort_customers()
        elif choice == "0":
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == "y":
                break
        else:
            print("Invalid option. Please try again.")
