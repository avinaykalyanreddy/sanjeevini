
from flask import *
from pymongo import  *

client = MongoClient("mongodb://localhost:27017/")

db = client["sanjeevini"]
doctors = db["doctors"]

app = Flask(__name__)
app.secret_key = 'ankenapalli'
@app.route("/login")
def login_page():

    return render_template("login.html")

@app.route("/loging",methods=["POST"])
def loging():

    form  = request.form

    if form["user_type"] == "doctor":

        doc_data = doctors.find_one({"email":form["email"]})

        if doc_data and form["email"] == doc_data["email"] and form["password"] == doc_data["password"]:

            return render_template("doctor.html",doc_data=doc_data)

        else:

            flash("email or password incorrect","authentication")

            return render_template("login.html")





    pass
app.run(debug=True)