from session15A import Database
from patient1 import Patient
from tabulate import tabulate  #pip install tabulate

def add_new_patient():
    patient = Patient()
    patient.add_patient_details()
    sql = "INSERT INTO patients (name, phone, email, age, gender, address, diagnosis) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        patient.name, patient.phone, patient.email, patient.age, patient.gender, patient.address, patient.diagnosis)

    # Create an instance of the Database class
    database = Database()
    database.write(sql)

    print("Adding new patient...\n")

def update_existing_patient():
    pid = int(input("Please enter the Patient ID: "))
    
    sql = "select * from patients where pid= {}".format(pid)
    
    database = Database()
    
    rows = database.read(sql)
    patient = Patient(pid=pid, name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4], gender=rows[0][5], address=rows[0][6], diagnosis=rows[0][7], created_on=rows[0][8])

    print("Patient to update: ")
    
    patient.show()
    patient.update_patient_details()
    
    sql = "update patients set name='{name}', phone='{phone}', email='{email}', age={age}, gender='{gender}', address='{address}', diagnosis='{diagnosis}', created_on='{created_on}' where pid = {pid}".format_map(vars(patient))
    
    database.write(sql)
    patient.show()
    
    print("Updating existing patient...\n")

def delete_existing_patient():
    pid = int(input("Enter patient id to be deleted: "))

    sql = "delete from patients where pid= {}".format(pid)
    database = Database()
    ask = input("Are you sure you want to delete? (yes/no)\n")
    
    if ask.lower() == 'yes':
        database.write(sql)
        print("Deleting existing patient...\n")
    else:
        print("Not deleting")
    
def view_patient_by_phone():
    phone_number = input("Please enter the phone number: ")
    sql = "select * from patients where phone= '{}'".format(phone_number)
    
    database = Database()
    
    rows = database.read(sql)
    
    columns = ['pid', 'name', 'phone', 'email', 'age', 'gender', 'address', 'diagnosis', 'created_on']
    if rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing patient...~~~~~~~~~~~~~~~~~~~~\n")
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing patient...~~~~~~~~~~~~~~~~~~~~\n")
        print("Viewing patient by phone...\n")
    else:
        print("No such data exists")
    
def view_patient_by_pid():
    pid = int(input("Please enter the Patient ID: "))
    sql = "select * from patients where pid= {}".format(pid)
    
    database = Database()
    
    rows = database.read(sql)
    
    columns = ['pid', 'name', 'phone', 'email', 'age', 'gender', 'address', 'diagnosis', 'created_on']
    if rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing patient...~~~~~~~~~~~~~~~~~~~~\n")
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing patient...~~~~~~~~~~~~~~~~~~~~\n")
        print("Viewing patient by PID...\n")
    else:
        print("No such data exists")
    
def view_all_patients():
    sql = "select * from patients"
    database = Database()
    rows = database.read(sql)
    columns = ['pid', 'name', 'phone', 'email', 'age', 'gender', 'address', 'diagnosis', 'created_on']
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all patients...~~~~~~~~~~~~~~~~~~~~\n")
    print(tabulate(rows, headers=columns, tablefmt='grid'))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all patients...~~~~~~~~~~~~~~~~~~~~\n")

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~Welcome to PMS APP~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        print("1. Add new Patient")
        print("2. Update Existing Patient")
        print("3. Delete Existing Patient")
        print("4. View Patient By phone")
        print("5. View Patient By PID")
        print("6. View all Patients")
        print("0. To Quit App")

        choice = int(input("Enter Your choice: "))

        if choice == 1:
            add_new_patient()
        elif choice == 2:
            update_existing_patient()
        elif choice == 3:
            delete_existing_patient()
        elif choice == 4:
            view_patient_by_phone()
        elif choice == 5:
            view_patient_by_pid()
        elif choice == 6:
            view_all_patients()
        elif choice == 0:
            print("Quitting the app...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
