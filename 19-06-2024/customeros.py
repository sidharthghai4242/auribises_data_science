file=open("Customer_data.csv",'a')


while True:
    a=int(input("Please enter your command:- "))

    if a==1:
        name=input("Please enter your name:- ")
        phone=input("Please enter your phone:- ")
        email=input("Please enter your email:- ")
        customer_details="{},{},{}\n".format(name,phone,email)
        file.write(customer_details)
        print("Data Written")
    elif a==2:
        print("Thank you")
        file.close()
        break