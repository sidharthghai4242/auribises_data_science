from session17B import Consultation
from session17 import Patient
from session17A import Database
from tabulate import tabulate

def main():
    db=Database()
    print("=======================")
    print("Welcome to Doctor's App")
    print("=======================")

    while True:
        print("1. Add new Patient")
        print("2. Update Existing Patient")
        print("3. Delete Existing Patient")
        print("4. View Patient By phone")
        print("5. View Patient By PID")
        print("6. View all Patients")
        print("7. Add new Consultation")
        print("8. View all Consultations")
        print("9. View patient Consultation")
        print("10. View followups")
        print("0. To Quit App")

        choice = int(input("Enter Your choice: "))

        if choice == 1:
            patient=Patient()
            patient.add_patient_details()
            sql="insert into Patient values(null,'{name}','{phone}','{email}','{dob}','{gender}','{created_on}')".format_map(vars(patient))
            db.write(sql)
            print("Patient created....")
        elif choice == 2:
            # update_existing_patient()
            pass
        elif choice == 3:
            # delete_existing_patient()
            pass
        elif choice == 4:
            # view_patient_by_phone()
            pass
        elif choice == 5:
            # view_patient_by_pid()
            pass
        elif choice == 6:
            sql="select * from patient"
            rows=db.read(sql)
            columns=['cid' , 'name' , 'phone' , 'email' , 'dob' , 'gender' , 'created_on']
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == 7:
            consultation=Consultation()
            consultation.add_consultation_details()
            sql="insert into consultation values(null,{pid},'{remarks}','{medicines}','{next_followup}','{created_on}')".format_map(vars(consultation))
            db.write(sql)
            print("Consultation created....")

        elif choice == 8:
            sql="select * from Consultation"
            rows=db.read(sql)
            columns=['cid' , 'pid' , 'remarks' , 'medicines' , 'next_followup' , 'created_on']
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == 9:
            pid =int(input("Enter patient ID:- "))
            sql="select * from Consultation where pid ={}".format(pid)
            rows=db.read(sql)
            columns=['cid' , 'pid' , 'remarks' , 'medicines' , 'next_followup' , 'created_on']
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == 10:
            start_date =input("Enter date (yyyy-mm-dd hh:mm:ss):- ")
            end_date =input("Enter date (yyyy-mm-dd hh:mm:ss):- ")
            sql="select * from Consultation where next_followup>= '{}' and next_followup<='{}'".format(start_date,end_date)
            rows=db.read(sql)
            columns=['cid' , 'pid' , 'remarks' , 'medicines' , 'next_followup' , 'created_on']
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Viewing all customers...~~~~~~~~~~~~~~~~~~~~\n")


        elif choice == 0:
            print("Quitting the app...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()