from wsgiref.validate import validator

from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug.utils import secure_filename
import os
from flask_mail import Mail, Message
from flask_wtf import Form, FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField, StringField
from flask_sqlalchemy import  SQLAlchemy

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired, Email
import sqlite3

app = Flask(__name__)
app.secret_key = "123"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"
app.config["SECRET_KEY"] = "123"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "gyourID.dyv@gmail.com"
app.config["MAIL_PASSWORD"] = "sdfhadfh"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column("student_id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

with app.app_context():
    db.create_all()

mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField("Name Of Student", [DataRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices=[("M", "Male"),("F", "Female")])
    Address = TextAreaField("Address")

    email = StringField("Email", [DataRequired("Please enter your email address"),
                                               Email("Please enter your email address")])
    Age = IntegerField("Age")
    language = SelectField("Languages", choices = [("cpp", "C++"),
                                                   ("py", "python")])
    submit = SubmitField("Send")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/2")
def second_index():
    if 'username' in session:
        username = session['username']
        return (
            f'Logged in as {username}<br>'
            "<b><a href='/logout'>Click here to log out</a></b>"
        )

    return (
        "You are not logged in<br>"
        "<a href='/2login'>Click here to log in</a>"
    )


@app.route("/re")
def success_form():
    return f"Form sent successful!"



@app.route("/admin")
def hello_admin():
    # return "Hello Admin!"

    return render_template("admin_page.html", name = "admin" )

# @app.route("/guest/<name>")
# def hello_guest(name):
#     return render_template("blog.html", name = name)

@app.route("/success/<name>")
def success(name, password):
    if name == "admin" and password == "admin":
        flash("You were successfully logged in")
        return redirect(url_for("hello_admin"))

    else:
        error = "Invalid admin username or password"
        return redirect(url_for("hello_guest", name=name))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["pass"]

        if user == "admin" and password == "admin":
            flash("You were successfully logged in")
            return redirect(url_for("hello_admin"))

        else:
            flash("invalid admin username or password")
            return redirect(url_for("index"))

    else:
        return redirect(url_for("index"))

@app.route("/2login", methods = ["GET", "POST"])
def second_login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("second_index"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))



@app.route("/result", methods= ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result = result)

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]

        resp = make_response(render_template("readcookie.html", user = user))
        resp.set_cookie("userID", user)

        return resp

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f"<h1>welcome {name}!</h1>"

@app.route("/upload")
def upload_page():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def uploader_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
        flash("file uploaded successfully")
        return render_template("admin_page.html")

@app.route("/post")
def show_post():
    return render_template("post.html" )


@app.route("/mail")
def mail_page():
    msg = Message("Hello", sender = "yourID@gmail.com", recipients = ["id1@gmai.com"])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required")
            return render_template("contact.html", form = form)
        else:
            return render_template("result.html", form = form)
    elif request.method == "GET":
        return render_template("contact.html", form = form)

with sqlite3.connect("database.db") as con:
    con.execute("DROP TABLE IF EXISTS students")
    con.execute("""
        CREATE TABLE students (
            name TEXT,
            addr TEXT,
            city TEXT,
            pin TEXT
        )
    """)


@app.route("/enternew")
def new_student():
    return render_template("student.html")

@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form["nm"]
            addr = request.form["addr"]
            city = request.form["city"]
            pin = request.form["pin"]

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)",
                            (nm, addr, city, pin))
                msg = "Record successfully added"

        except Exception as e:
            msg = f"Error in insert operation: {e}"

        return render_template("result_sqlite.html", msg = msg)

    return redirect(url_for("new_student"))

@app.route("/list")
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows = rows)

@app.route("/thelist")
def show_all():
    return render_template("thelist.html", students = Student.query.all())

@app.route("/new", methods = ["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["name"] or not request.form["city"] or not request.form["addr"]:
            flash("Please enter all the fields", "error")
        else:
            student = Student(request.form["name"], request.form["city"], request.form["addr"], request.form["pin"])

            db.session.add(student)
            db.session.commit()

            flash("Record was successfully added")
            return redirect(url_for("show_all"))
    return render_template("new.html")

if __name__ == '__main__':
    app.run(debug = True)