from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text
from passlib.hash import sha256_crypt
from functools import wraps


@app.route('/register' , methods=['GET','POST'])
@required_roles('admin')

def required_roles(*roles):
   def wrapper(f):
      @wraps(f)
      def wrapped(*args, **kwargs):
         if get_current_user_role() not in roles:
            flash('Authentication error, please check your details and try again','error')
            return redirect(url_for('index'))
         return f(*args, **kwargs)
      return wrapped
   return wrapper
 
def get_current_user_role():
   return g.user.role


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

			#flash('Registered successfully!','success')
			return render_template("login.html")
		else:
			#flash("Passwords do no match","danger")
			return render_template('register.html')

	return render_template('register.html')
