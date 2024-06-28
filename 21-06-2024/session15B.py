from session15 import Customer
from session15A import Database

def add_new_customer():
    customer = Customer()
    customer.add_customer_details()
    sql = "INSERT INTO customers (name, phone, email, age, gender) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
        customer.name, customer.phone, customer.email, customer.age, customer.gender)

    # Create an instance of the Database class
    database = Database()
    database.write(sql)

    print("Adding new customer...\n")

def update_existing_customer():
    print("Updating existing customer...\n")
    # Code to update an existing customer goes here

def delete_existing_customer():
    cid=int(input("Enter customer id to be deleted "))

    sql="delete from customers where cid= {}".format(cid)
    database = Database()
    database.write(sql)
    print("Deleting existing customer...\n")
    # Code to delete an existing customer goes here

def view_customer_by_phone():
    print("Viewing customer by phone...\n")
    # Code to view a customer by phone goes here

def view_customer_by_cid():
    print("Viewing customer by CID...\n")
    # Code to view a customer by CID goes here

def view_all_customers():
    print("Viewing all customers...\n")
    # Code to view all customers goes here

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~Welcome to CMS APP~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        print("1. Add new Customer ")
        print("2. Update Existing Customer ")
        print("3. Delete Existing Customer ")
        print("4. View Customer By phone  ")
        print("5. View Customer By cid ")
        print("6. View all Customers ")
        print("0. To Quit App")

        choice = int(input("Enter Your choice: "))

        if choice == 1:
            add_new_customer()
        elif choice == 2:
            update_existing_customer()
        elif choice == 3:
            delete_existing_customer()
        elif choice == 4:
            view_customer_by_phone()
        elif choice == 5:
            view_customer_by_cid()
        elif choice == 6:
            view_all_customers()
        elif choice == 0:
            print("Quitting the app...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
