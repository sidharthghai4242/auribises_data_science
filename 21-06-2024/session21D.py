from session21C import MongoDBHelper
from session21A import User
import datetime
from bson.objectid import ObjectId
from tabulate import tabulate

def print_menu():
    print("MongoDB Helper Test App")
    print("1. Insert User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Fetch Users")
    print("5. Exit")

def main():
    print("Welcome to MongoDB Helper Test App")
    dbhelper = MongoDBHelper()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            user = User()
            user.add_details_to_user()
            document = vars(user)
            dbhelper.insert(document)
            print("User inserted successfully.")

        elif choice == '2':
            object_id = input("Enter the ObjectId of the document to update: ")
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            document_to_update = {
                "name": name,
                "age": age,
                "created_on": datetime.datetime.now()
            }
            query = {'_id': ObjectId(object_id)}
            dbhelper.update(document=document_to_update, query=query)
            print("User updated successfully.")

        elif choice == '3':
            object_id = input("Enter the ObjectId of the document to delete: ")
            query = {'_id': ObjectId(object_id)}
            dbhelper.delete(query)
            print("User deleted successfully.")

        elif choice == '4':
            email = input("Enter email to fetch: ")
            phone = input("Enter phone number to fetch: ")
            # query = {'email': email, 'phone': phone}
            users = dbhelper.fetch()
            # if users:
            #     headers = users[0].keys()
            #     rows = [user.values() for user in users]
            #     print(tabulate(rows, headers=headers))
            # else:
            #     print("No users found.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
