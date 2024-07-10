from flask import *
import datetime
import hashlib
from session21C import MongoDBHelper
import os

# Create the Flask application
web_app = Flask(__name__)
db_users = MongoDBHelper(collection="users")
db_patients = MongoDBHelper(collection="patients")  # Initialize a separate instance for patients

@web_app.route("/")
def index():
    return render_template('index.html')

@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/login")
def login():
    return render_template('login.html')

@web_app.route("/add-user", methods=['POST'])
def add_user_in_db():
    user_data = {
        "name": request.form["name"],
        "phone": request.form["phone"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "age": request.form["age"],
        "gender": request.form["gender"],
        "created_on": datetime.datetime.now(),
    }
    result = db_users.insert(user_data)  # Insert into 'users' collection
    if result:
        session['user_id'] = str(result.inserted_id)
        session['name'] = user_data["name"]
        session['email'] = user_data["email"]
        return render_template("index.html", name=session['name'], email=session['email'])
    else:
        return "Failed to insert user data."

@web_app.route("/fetch-user", methods=['POST'])
def fetch_user_from_db():
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }
    results = db_users.fetch(query=user_data)
    if results:
        # Assuming only one user with this email/password exists
        result = results[0]
        session['user_id'] = str(result["_id"])
        session['name'] = result["name"]
        session['email'] = result["email"]
        return render_template("index.html", name=session['name'], email=session['email'])
    else:
        return "Failed to find user data."

@web_app.route("/patients")
def patients():
    return render_template('patients.html')

@web_app.route("/add-patient", methods=['POST'])
def add_patient_info_in_db():
    patient_info = {
        "name": request.form["name"],
        "age": request.form["age"],
        "history": request.form["history"]
    }
    result = db_patients.insert(patient_info)  # Insert into 'patients' collection
    if result:
        message = "Patient inserted: {}".format(result.inserted_id)
    else:
        message = "Failed to insert patient data."
    return message

def main():
    port = int(os.environ.get('PORT', 5000))
    web_app.secret_key = "doctors-app-key-v1"
    web_app.run()

if __name__ == "__main__":
    main()
