import mysql.connector as db

class Database:
    def __init__(self):
        username = "root"
        password = "Buddy99@ghai"
        host = "127.0.0.1"
        port = "3306"
        database = "customers"

        self.connection = db.connect(user=username, password=password, host=host, database=database)
        print("[Database] Connection Created")
        
        self.cursor = self.connection.cursor()
        print("[Database] Cursor Created")

    def write(self, sql):
        print("[Database] SQL statement:- \n",sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("\n[Database] SQL statement executed successfully...\n")

    def read(self, sql):
        print("[Database] SQL statement:- \n",sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print("\n[Database] SQL statement executed successfully...\n")
        return result
