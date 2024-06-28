file=open("Customer_data.csv","r")
lines=file.readlines()

for i in range(len(lines)):
    print(lines[i])