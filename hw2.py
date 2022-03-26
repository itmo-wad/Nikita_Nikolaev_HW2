from flask import Flask, render_template, redirect, request 
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/general"
mongo = PyMongo(app)


@app.route('/')
@app.route("/auth", methods=["GET","POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user=mongo.db.general.find({"username":username})

        if user and check_password_hash(user["password"],password):
            return redirect("/profile")
        else:
            return "Incorrect!"


@app.route("/profile")
def profile():
    return render_template("profilepage.html")

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
