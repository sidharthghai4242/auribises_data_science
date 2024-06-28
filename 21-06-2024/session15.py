"""
create table customers(
    cid int primary key auto_increment,
    name varchar(256),
    phone varchar(15),
    email varchar(256),
    age int,
    gender varchar(256),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


"""


class Customer:
    def __init__(self,cid=0, name="", phone="", email="", age=0, gender="", created_on=""):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.created_on = created_on

    def add_customer_details(self):
        self.name = input("Please enter your name:-")
        self.phone = input("Please enter your phone:-")
        self.email = input("Please enter your email:-")
        self.age = input("Please enter your age:-")
        self.gender = input("Please enter your gender:-")
    
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~Customer~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Customer Id:- {}".format(self.cid))
        print("{} | {} | {}".format(self.name,self.phone,self.email))
        print("{} | {} | {}".format(self.age,self.gender,self.created_on))
        print("~~~~~~~~~~~~~~~~~~~~~~~Customer~~~~~~~~~~~~~~~~~~~~~~~~~")

