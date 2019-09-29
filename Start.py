from flask import Flask
from flask import render_template
from flask import request
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.db"

db = SQLAlchemy(app)

class Users(db.Model):
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Users('{self.firstName}','{self.lastName}','{self.email}')"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.form:
        print(request.form)
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.form:
        print(request.form)
    return render_template("register.html")
  
if __name__ == "__main__":
    app.run(debug=True)