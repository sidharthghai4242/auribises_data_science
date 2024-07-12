from flask import *
import datetime
import hashlib
from session21C import MongoDBHelper
import os

# Create the Flask application
web_app = Flask(__name__)
db_users = MongoDBHelper(collection="users")
db_patients = MongoDBHelper(collection="patients")  # Initialize a separate instance for patients

@web_app.route("/index")
def index():
    return render_template('index.html')

@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/")
def login():
    return render_template('login.html')

@web_app.route("/view-patients")
def ViewPatients():
    user_data = {
        "doctor": session.get("email"),
    }
    results = db_patients.fetch(query=user_data)
    if results:
        return render_template('viewpatients.html', patients=results)
    else:
        return render_template('viewpatients.html', patients=[])

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
        "doctor": session["email"],
        "name": request.form["name"],
        "age": request.form["age"],
        "phone": request.form["phone"],
        "history": request.form["history"]
    }
    result = db_patients.insert(patient_info)  # Insert into 'patients' collection
    if result.inserted_id:
        message = "Patient inserted successfully."
    else:
        message = "Failed to insert patient data."
    return redirect(url_for('show_patients', message=message))

@web_app.route("/patients")
def show_patients():
    message = request.args.get('message')
    return render_template("patients.html", message=message)

def main():
    port = int(os.environ.get('PORT', 5000))
    web_app.secret_key = "doctors-app-key-v1"
    web_app.run()

if __name__ == "__main__":
    main()
