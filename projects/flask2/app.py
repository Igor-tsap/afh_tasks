from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = "456"

my_list = list(range(1, 11))

my_dict = {
    "dreamlike": "Dale",
    "uncanny": "Laura",
    "ominous": "Betty",
    "disquieting": "Rita",
    "surreal": "Henry",
    "hypnotic": "Jeffrey",
    "shadowed": "Frank",
    "eerie": "Dorothy",
    "fragmented": "Alvin",
    "subconscious": "Gordon"
}

@app.route("/", methods = [ "POST", "GET",])
def index():
    if request.method == "POST":
        new_adj = request.form.get("adj")
        new_name = request.form.get("name")

        new_row = {new_adj: new_name}

        my_dict.update(new_row)

        flash("row was successfully added")
        return redirect(url_for("index"))

    else:
        return render_template("index.html", my_list=my_list, my_dict=my_dict)


@app.route("/numbers/<int:number>")
def number_page(number):
    return render_template("number_page.html", num=number, my_list=my_list)

if __name__ == "__main__":
    app.run(debug=True)