import hashlib
password=input("Enter your password:- ")
print("Password is:- ",password)
password=password.encode("utf-8")
password_encrypted=hashlib.sha256(password).hexdigest()
print(password_encrypted)