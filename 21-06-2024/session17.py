import datetime
class Patient:
    
    def __init__(self,pid=0,name="",phone="",email="",dob="",gender=""):
        self.pid=pid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()
    
    def add_patient_details(self):
        self.name = input("Please enter your name: ")
        self.phone = input("Please enter your phone: ")
        self.email = input("Please enter your email: ")
        self.dob = input("Please enter your date of birth(yyyy-mm-dd): ")
        self.gender = input("Please enter your gender: ")
    
    def show(self):
        print("===========Patient===========")

        patient="""
        {pid} | {name} | {phone}
        {email} | {dob} 
        {gender} | {created_on}
        """.format_map(vars(self))

        print(patient)

        print("===========Patient===========")

"""
CREATE TABLE Patient (
    pid INT PRIMARY KEY auto_increment,
    name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    dob DATE,
    gender VARCHAR(10),
    created_on datetime
);

"""