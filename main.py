from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

_engine = create_engine("mysql+pymysql://root:Sudhanva@localhost/LoginRegister")
db = scoped_session(sessionmaker(bind = _engine))

app.config['SECRET_KEY'] = 'SER@515@Findler'

@app.route("/")
@app.route("/index", methods = ["GET","POST"])
def index():

	query = "SELECT * FROM Users"
	data = _engine.execute(query).fetchall()
	return render_template("users.html", users = data)

if __name__ == '__main__':
	app.run(debug = True)


@app.route("/delete/<email>", methods = ["GET","POST"])
def delete(email):
	query = "DELETE FROM Users WHERE email = '%s'"
	val = (email,)
	_engine.execute(query,val)
	db.commit()
	return redirect("/")