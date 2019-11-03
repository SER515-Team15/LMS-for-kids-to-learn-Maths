from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text

app = Flask(__name__)

# Change the credentials to fit your localhost details.
_engine = create_engine("mysql+pymysql://root:Sudhanva@localhost/LoginRegister")
db = scoped_session(sessionmaker(bind = _engine))

EMAIL = ""

app.config['SECRET_KEY'] = 'SER@515@Findler'

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/register", methods = ["GET","POST"])
def register():
	if request.method == "POST":
		name = request.form.get("name")
		email = request.form.get("email")
		password = request.form.get("password")
		confirmpass = request.form.get("confirmPassword")
		role = request.form.get("rolePicker")
		status = "0"
		if password == confirmpass:
			_engine.execute("INSERT INTO Users VALUES (%s, %s, %s, %s, %s)", [name, email, password, role, status])
			db.commit()
			return render_template("login.html")
		else:
			return render_template('register.html')

	return render_template('register.html')

@app.route("/login", methods = ["GET","POST"])
def login():
	if request.method == "POST":


		email = request.form.get("email")
		password = request.form.get("password")

		emailsql = "SELECT email FROM Users WHERE email = '" + email + "'"
		EmailID = _engine.execute(emailsql).fetchone()
		em =  ''.join(EmailID)

		passwordsql = "SELECT password FROM Users WHERE email = '" + em + "'"
		Password = _engine.execute(passwordsql).fetchone()
		Password = ''.join(Password)

		roles = _engine.execute("SELECT Role FROM Users WHERE Email = %s", [em]).fetchone()
		role =  ''.join(roles)

		statuses = _engine.execute("SELECT Status FROM Users WHERE Email = %s", [em]).fetchone()
		status =  ''.join(statuses)

		if password==Password:
			if role == "Admin" and status == "1":
				session["log"] = True
				return redirect(url_for("admin"))

			elif role == "Teacher" and status == "1":
				session["log"] = True
				return redirect(url_for("teacher"))
			
			elif "Student" in role and status == "1":
				session["log"] = True
				return redirect(url_for("student"))
			
			elif status == "0":
				session.clear()
				return "You're not authorized for login!"

	return render_template('login.html')

@app.route("/adminconsole", methods = ["GET","POST"])
def adminconsole():
	data1 = _engine.execute( "SELECT * FROM Users WHERE status = '1'").fetchall()
	data2 = _engine.execute( "SELECT * FROM Users WHERE status = '0'").fetchall()
	return render_template("users.html", acceptedusers = data1, reviewusers = data2)

@app.route("/update/<string:email>", methods = ["GET","POST"])
def update(email):
	_engine.execute("UPDATE Users SET status = '1' WHERE email = %s",[email])
	db.commit()
	return redirect(url_for("adminconsole"))

@app.route("/delete/<string:email>", methods = ["GET","POST"])
def delete(email):
	_engine.execute("DELETE FROM Users WHERE email = %s", [email])
	db.commit()
	return redirect(url_for("adminconsole"))

@app.route("/admin", methods = ["GET","POST"])
def admin():
	return render_template("admin.html")

@app.route("/teacher", methods = ["GET","POST"])
def teacher():
	return render_template("teacher.html")

@app.route("/student", methods = ["GET","POST"])
def student():
	return render_template("student_landing.html")

@app.route("/logout")
def logout():
	session.clear()
	return render_template("login.html")

@app.route("/playground")
def playground():

	#roles = _engine.execute("SELECT Role FROM Users WHERE Email = %s", [EMAIL]).fetchone()
	#role = ''.join(roles)

	#if role == "Student (Elementary School)":
	return render_template('playground.html')
	#else:
	#return render_template('playground_middle.html')

@app.route("/takeQuiz")
def takeQuiz():
	
	return render_template('takeQuiz.html')


@app.route("/reviewGrades")
def reviewGrades():
	return render_template('reviewGrades.html')


@app.route("/createQuiz")
def createQuiz():
	return render_template('createQuiz.html')


@app.route("/gradeQuiz")
def gradeQuiz():
	return render_template('gradeQuiz.html')

if __name__ == '__main__':
	app.debug = True
	app.run()