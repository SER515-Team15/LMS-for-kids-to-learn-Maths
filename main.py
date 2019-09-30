from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text
from passlib.hash import sha256_crypt

app = Flask(__name__)

_engine = create_engine("mysql+pymysql://root:Sudhanva@localhost/LoginRegister")
db = scoped_session(sessionmaker(bind = _engine))

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/register", methods = ["GET","POST"])
def register():
	if request.method == "POST":

		fName = request.form.get("fName")
		lName = request.form.get("lName")
		password = request.form.get("pass")
		confirmpass = request.form.get("confirmPass")
		email = request.form.get("email")
		secure_password = sha256_crypt.encrypt(str(password))

		if password == confirmpass:
			sql = "INSERT INTO Users(fName, lName, pass, email) VALUES (%s, %s, %s, %s)"
			val = (fName,lName,secure_password,email)
			_engine.execute(sql,val)
			db.commit()

			flash('Registered successfully!','success')
			return redirect(url_for("login"))
		else:
			flash("Passwords do no match","danger")
			# return render_template('register.html')
	
	return render_template("register.html")

@app.route("/login", methods = ["GET","POST"])
def login():
	if request.method == "POST":

		email = request.form.get("email")
		password = request.form.get("pass")

		emailsql = "SELECT email FROM Users WHERE email = '" + email + "'"
		EmailID = _engine.execute(emailsql).fetchone()
		em =  ''.join(EmailID)
		passwordsql = "SELECT pass FROM Users WHERE email = '" + em + "'"
		Password = _engine.execute(passwordsql).fetchone()

		if EmailID == None or Password == None:
			flash("Username or Password is incorrect!", "danger")
			return render_template('login.html')
		else:
			for password_data in Password:
				if sha256_crypt.verify(password,password_data):
					flash("Login successful","success")
					return redirect(url_for("home"))
				else:
					flash("Password is incorrect!", "danger")
					return render_template('login.html')


	return render_template('login.html')

if __name__ == '__main__':
	app.secret_key = '123456789abcdefgh'
	app.run(debug = True)

