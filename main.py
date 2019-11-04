from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text

app = Flask(__name__)

# Change the credentials to fit your localhost details.
_engine = create_engine("mysql+pymysql://root:Sudhanva@localhost/LoginRegister")
db = scoped_session(sessionmaker(bind = _engine))

# Secret Key for secure transaction!
app.config['SECRET_KEY'] = 'SER@515@Findler'

# Home Page route
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

# Register Page Route
@app.route("/register", methods = ["GET","POST"])
def register():

	# Get elements from the database
	if request.method == "POST":
		name = request.form.get("name")
		email = request.form.get("email")
		password = request.form.get("password")
		confirmpass = request.form.get("confirmPassword")
		role = request.form.get("rolePicker")
		status = "0"
		# If both the passwords match, then register
		if password == confirmpass:
			_engine.execute("INSERT INTO Users VALUES (%s, %s, %s, %s, %s)", [name, email, password, role, status])
			db.commit()
			return render_template("login.html")
		else:
			return render_template('register.html')

	return render_template('register.html')

# Login Route
@app.route("/login", methods = ["GET","POST"])
def login():
	if request.method == "POST":

		# Get elements from the database
		email = request.form.get("email")
		session['email'] = request.form.get("email")
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

		# If both the fields match, then register
		if password==Password:
			# If admin
			if role == "Admin" and status == "1":
				session["log"] = True
				return redirect(url_for("admin"))

			# If teacher
			elif role == "Teacher" and status == "1":
				session["log"] = True
				return redirect(url_for("teacher"))
			
			# IF Student
			elif "Student" in role and status == "1":
				session["log"] = True
				return redirect(url_for("student"))
			
			# If Neither
			elif status == "0":
				session.clear()
				return "You're not authorized for login!"

	return render_template('login.html')

# Admin Console Route
@app.route("/adminconsole", methods = ["GET","POST"])
def adminconsole():
	data1 = _engine.execute( "SELECT * FROM Users WHERE status = '1'").fetchall()
	data2 = _engine.execute( "SELECT * FROM Users WHERE status = '0'").fetchall()
	return render_template("users.html", acceptedusers = data1, reviewusers = data2)

# Update the status of a user
@app.route("/update/<string:email>", methods = ["GET","POST"])
def update(email):
	_engine.execute("UPDATE Users SET status = '1' WHERE email = %s",[email])
	db.commit()
	return redirect(url_for("adminconsole"))

# Delete a particular user
@app.route("/delete/<string:email>", methods = ["GET","POST"])
def delete(email):
	_engine.execute("DELETE FROM Users WHERE email = %s", [email])
	db.commit()
	return redirect(url_for("adminconsole"))

# Admin Route
@app.route("/admin", methods = ["GET","POST"])
def admin():
	return render_template("admin.html")

# Teacher Route
@app.route("/teacher", methods = ["GET","POST"])
def teacher():
	return render_template("teacher.html")

# Student Route
@app.route("/student", methods = ["GET","POST"])
def student():
	return render_template("student_landing.html")

# Logout Route
@app.route("/logout")
def logout():
	session.clear()
	return render_template("login.html")

# Playground
@app.route("/playground")
def playground():
	email = session['email']
	roles = _engine.execute("SELECT Role FROM Users WHERE Email = %s", [email]).fetchone()
	role = ''.join(roles)

	# If Elementary Student, else Load Middle School Playground
	if "Elementary" in role:
		return render_template('playground.html')
	else:
		return render_template('playground_middle.html')

# Take Quiz Route
@app.route("/takeQuiz")
def takeQuiz():
	return render_template('takeQuiz.html')

# Review Grades Route
@app.route("/reviewGrades")
def reviewGrades():
	return render_template('reviewGrades.html')

# Create Quiz Route
@app.route("/createQuiz")
def createQuiz():
	return render_template('createQuiz.html')

# Grade Quiz Route
@app.route("/gradeQuiz")
def gradeQuiz():
	return render_template('gradeQuiz.html')

# Run Main in Debug mode
if __name__ == '__main__':
	app.debug = True
	app.run()