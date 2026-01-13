from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = "456"

my_list = list(range(1, 14))

my_dict = {
    "Dale": "Cooper",
    "Laura": "Palmer",
    "Betty": "Elms",
    "Rita": "Hayworth",
    "Henry": "Spencer",
    "Jeffrey": "Beaumont",
    "Frank": "Booth",
    "Dorothy": "Vallens",
    "Alvin": "Straight",
    "Gordon": "Cole"
}

@app.route("/", methods = [ "POST", "GET" ])
def index():
    if request.method == "POST":
        fake_method = request.form.get("fake_method")

        if fake_method is None:
            new_fname = request.form.get("fname")
            new_sname = request.form.get("sname")

            new_row = {new_fname: new_sname}

            my_dict.update(new_row)

            flash("row was successfully added")
            return redirect(url_for("index"))

        elif fake_method == "PUT":
            rep_fname = request.form.get("put_fname")
            rep_sname = request.form.get("put_sname")

            rep_row = {rep_fname: rep_sname}

            my_dict.clear()
            my_dict.update(rep_row)

            flash("table successfully replaced")
            return redirect(url_for("index"))

    else:
        return render_template("index.html", my_list=my_list, my_dict=my_dict)


@app.route("/numbers/<int:number>")
def number_page(number):
    # flash(f"What I can say about number {number}")
    return render_template("number_page.html", num=number, my_list=my_list)

if __name__ == "__main__":
    app.run(debug=True)