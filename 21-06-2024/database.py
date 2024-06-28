class Customer:
    def __init__(self, name="", phone="", email="", gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
    
    def add_customer_details(self):
        self.name = input("Please enter your name:-")
        self.phone = input("Please enter your phone:-")
        self.email = input("Please enter your email:-")
        self.gender = input("Please enter your gender:-")
    
    def show(self):
        print(f"Customer Details:")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Gender: {self.gender}")


class Address:
    def __init__(self, houseno, addressLine, city, state, zipCode, landmark):
        self.houseno = houseno
        self.addressLine = addressLine
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.landmark = landmark
    
    def show(self):
        print(f"Address Details:")
        print(f"House No: {self.houseno}")
        print(f"Address Line: {self.addressLine}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zipCode}")
        print(f"Landmark: {self.landmark}")
