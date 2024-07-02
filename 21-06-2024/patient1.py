class Patient:
    def __init__(self, pid=0, name="", phone="", email="", age=0, gender="", address="", diagnosis="", created_on=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address
        self.diagnosis = diagnosis
        self.created_on = created_on

    def add_patient_details(self):
        self.name = input("Please enter your name: ")
        self.phone = input("Please enter your phone: ")
        self.email = input("Please enter your email: ")
        self.age = int(input("Please enter your age: "))
        self.gender = input("Please enter your gender: ")
        self.address = input("Please enter your address: ")
        self.diagnosis = input("Please enter your diagnosis: ")
    
    def update_patient_details(self):
        name = input("Enter patient name (leave blank to keep current): ")
        if name:
            self.name = name

        phone = input("Enter phone number (leave blank to keep current): ")
        if phone:
            self.phone = phone

        email = input("Enter email (leave blank to keep current): ")
        if email:
            self.email = email

        age = input("Enter age (leave blank to keep current): ")
        if age:
            self.age = int(age)

        gender = input("Enter gender (leave blank to keep current): ")
        if gender:
            self.gender = gender

        address = input("Enter address (leave blank to keep current): ")
        if address:
            self.address = address

        diagnosis = input("Enter diagnosis (leave blank to keep current): ")
        if diagnosis:
            self.diagnosis = diagnosis
    
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~Patient~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Patient Id: {}".format(self.pid))
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{} | {} | {}".format(self.age, self.gender, self.created_on))
        print("Address: {}".format(self.address))
        print("Diagnosis: {}".format(self.diagnosis))
        print("~~~~~~~~~~~~~~~~~~~~~~~Patient~~~~~~~~~~~~~~~~~~~~~~~~~")
