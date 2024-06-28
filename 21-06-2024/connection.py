import mysql.connector as db
from session15 import Customer

customer1=Customer()
customer1.add_customer_details()
username="root"
password="Buddy99@ghai"

host="127.0.0.1"
port="3306"

database="customers"

connection= db.connect(user=username,password=password,host=host,database=database)

print("connection created")
print(connection)


sql="insert into customers values(null,'{}','{}','{}','{}','{}')".format(customer1.name,customer1.phone,customer1.email,customer1.age,customer1.gender)


cursor=connection.cursor()
cursor.execute(sql)
connection.commit()

print("SQL command executed....")