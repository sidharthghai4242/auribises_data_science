from session15 import Customer
from session15A import Database
from tabulate import tabulate  #pip install tabulate

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
    cid=int(input("Please enter the Customer ID :- "))
    sql="select * from customers where cid= {}".format(cid)
    
    database=Database()
    
    rows=database.read(sql)
    
    columns=['cid' , 'name' , 'phone' , 'email' , 'age' , 'gender' , 'created_on']
    if rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print(tabulate(rows,headers=columns,tablefmt='grid'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print("Viewing customer by phone...\n")
    else:
        print("No such data exists")
    print("Updating existing customer...\n")
    # Code to update an existing customer goes here

def delete_existing_customer():

    cid=int(input("Enter customer id to be deleted:- "))

    sql="delete from customers where cid= {}".format(cid)
    database = Database()
    ask=input(" Are you sure you want to delete ?(yes/no)\n")
    
    if(ask=='yes'):
        database.write(sql)
        print("Deleting existing customer...\n")
    else:
        print("Not deleting")
    
    # Code to delete an existing customer goes here

def view_customer_by_phone():
    
    phone_number=input("Please enter the phone number:- ")
    sql="select * from customers where phone= '{}'".format(phone_number)
    
    database=Database()
    
    rows=database.read(sql)
    
    columns=['cid' , 'name' , 'phone' , 'email' , 'age' , 'gender' , 'created_on']
    if rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print(tabulate(rows,headers=columns,tablefmt='grid'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print("Viewing customer by phone...\n")
    else:
        print("No such data exists")
    
    # Code to view a customer by phone goes here

def view_customer_by_cid():
    cid=int(input("Please enter the Customer ID :- "))
    sql="select * from customers where cid= {}".format(cid)
    
    database=Database()
    
    rows=database.read(sql)
    
    columns=['cid' , 'name' , 'phone' , 'email' , 'age' , 'gender' , 'created_on']
    if rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print(tabulate(rows,headers=columns,tablefmt='grid'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        print("Viewing customer by phone...\n")
    else:
        print("No such data exists")
    # Code to view a customer by CID goes here

def view_all_customers():
    sql="select * from customers"
    database=Database()
    rows=database.read(sql)
    columns=['cid' , 'name' , 'phone' , 'email' , 'age' , 'gender' , 'created_on']
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
    print(tabulate(rows,headers=columns,tablefmt='grid'))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
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
