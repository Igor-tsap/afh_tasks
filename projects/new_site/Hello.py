from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "123"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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


# @app.route("/success/<name>")
# def success(name):
#     return f"Login successful {name}!"



@app.route("/admin")
def hello_admin():
    # return "Hello Admin!"

    return render_template("admin_page.html", name = "admin" )

@app.route("/guest/<name>")
def hello_guest(name):
    return render_template("blog.html", name = name)

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

@app.route("/guest/<name>/<int:post_id>")
def show_blog(name, post_id):
    return render_template("post.html", marks = post_id, name= name)

@app.route("/result", methods= ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result = result)

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]

        resp = make_response(render_template("readcookie.html"))
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





if __name__ == '__main__':
    app.run(debug = True)