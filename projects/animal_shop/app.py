from flask import Flask, redirect, render_template, request, url_for, flash
import mysql.connector


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    "port": 8889,
    'database': '1stdb',
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

app = Flask(__name__)
app.secret_key = "68464"



@app.route("/", methods= ["GET", "POST"])
def index():
    if request.method == "POST":
        sql = "INSERT INTO animals (name, price, quantity) VALUES (%s, %s, %s)"
        val = (
            request.form.get("name"),
            request.form.get("price"),
            request.form.get("quantity")
        )

        cursor.execute(sql, val)

        flash("data was successfully added")
        return redirect(url_for("index"))

    else:
        cursor.execute("select * from animals")
        value = cursor.fetchall()

        db.commit()
        return render_template("index.html", data=value)

@app.route("/delete/<int:id>")
def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    val = (id,)

    cursor.execute(sql, val)

    db.commit()
    flash(f"row {id} was successfully deleted")
    return redirect("/")

@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    if request.method == "POST":
        sql = "UPDATE animals SET name = %s, price = %s, quantity = %s WHERE id = %s"
        val = (
               request.form.get("name"),
               request.form.get("price"),
               request.form.get("quantity"),
               id,
               )

        cursor.execute(sql, val)

        db.commit()
        flash(f"row {id} was successfully updated")

        return redirect("/")

    else:
        sql = "SELECT * FROM animals WHERE id = %s"
        val = (id,)

        cursor.execute(sql, val)

        row = cursor.fetchone()
        return render_template("update.html", row=row)

@app.route("/1")
def data1():
    cursor.execute("select * from animals where quantity=1")
    value = cursor.fetchall()
    return render_template("data.html", data=value, quantity=1)

@app.route("/2")
def data2():
    cursor.execute("select * from animals where quantity=2")
    value = cursor.fetchall()
    return render_template("data.html", data=value, quantity=2)

@app.route("/3+")
def data3():
    cursor.execute("select * from animals where quantity>=3")
    value = cursor.fetchall()
    return render_template("data.html", data=value, quantity="3 or more")

if __name__ == "__main__":
    app.run(debug=True)