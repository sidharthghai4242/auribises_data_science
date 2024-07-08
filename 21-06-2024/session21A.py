import datetime
import hashlib
class User:
    def __init__(self, name="", phone="", email="", password="", age=0, gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()
    
    def add_details_to_user(self):
        self.name = input("Please enter your name: ")
        self.phone = input("Please enter your phone number: ")
        self.email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        password=password.encode("utf-8")
        self.password=hashlib.sha256(password).hexdigest()
        self.age = int(input("Please enter your age: "))
        self.gender = input("Please enter your gender: ")

# Example usage:
# user1 = User()
# user1.add_details_to_user()

# print(f"Name: {user1.name}")
# print(f"Phone: {user1.phone}")
# print(f"Email: {user1.email}")
# print(f"Password: {user1.password}")
# print(f"Age: {user1.age}")
# print(f"Gender: {user1.gender}")
# print(f"Created on: {user1.created_on}")
