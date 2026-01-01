from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

# @app.route("/success/<name>")
# def success(name):
#     return f"Login successful {name}!"



@app.route("/admin")
def hello_admin():
    return "Hello Admin!"

@app.route("/guest/<name>")
def hello_guest(name):
    return render_template("blog.html", name = name)

@app.route("/success/<name>")
def success(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", name = name))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name = user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name = user))

@app.route("/guest/<name>/<int:post_id>")
def show_blog(name, post_id):
    return render_template("post.html", marks = post_id, name= name)

@app.route("/result", methods= ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result = result)






if __name__ == '__main__':
    app.run(debug = True)