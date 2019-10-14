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
	data1 = _engine.execute( "SELECT * FROM Users WHERE status = 1").fetchall()
	data2 = _engine.execute( "SELECT * FROM Users WHERE status = 0").fetchall()
	return render_template("users.html", acceptedusers = data1, reviewusers = data2)

@app.route("/update/<string:email>", methods = ["GET","POST"])
def update(email):
	_engine.execute("UPDATE Users SET status = 1 WHERE email = %s",[email])
	db.commit()
	return redirect(url_for("index"))

@app.route("/delete/<string:email>", methods = ["GET","POST"])
def delete(email):
	_engine.execute("DELETE FROM Users WHERE email = %s", [email])
	db.commit()
	return redirect(url_for("index"))

if __name__ == '__main__':
	app.run(debug = True)