from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text

app = Flask(__name__)

_engine = create_engine("mysql+pymysql://root:Sudhanva@localhost/LoginRegister")
db = scoped_session(sessionmaker(bind = _engine))

app.config['SECRET_KEY'] = 'SER@515@Findler'

@app.route("/")
@app.route("/register", methods = ["GET","POST"])
def register():
	if request.method == "POST":
		name = request.form.get("name")
		email = request.form.get("email")
		password = request.form.get("password")
		confirmpass = request.form.get("confirmPassword")
		role = "Admin";
		status = "False"
		if password == confirmpass:
			_engine.execute("INSERT INTO Users VALUES (%s, %s, %s, %s, %r)", [name, password, email, role, status])
			db.commit()
			return render_template("login.html")
		else:
			return render_template('register.html')

	return render_template('register.html')

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
					session["log"] = True
					#flash("Login successful","success")
					return render_template('student_landing.html')
				else:
					#flash("Password is incorrect!", "danger")
					return render_template('login.html')

	return render_template('login.html')

if __name__ == '__main__':
	app.debug = True
	app.run()