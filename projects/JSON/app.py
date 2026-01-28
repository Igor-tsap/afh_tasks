from flask import Flask, jsonify, request
import mysql.connector

config = {
    'user': 'root',
    'password': 'aKp1haay2iEs394W',
    'host': 'localhost',
    "port": 8889,
    'database': '2nd',
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)


app = Flask(__name__)
app.secret_key = "68464"


@app.route("/animals", methods=["GET", "POST"])
def index():
    cursor = db.cursor(dictionary=True)

    try:
        if request.method == "POST":
            data = request.get_json(silent=True) or {}
            name = data.get("name")
            price = data.get("price")
            quantity = data.get("quantity")

            sql = "INSERT INTO animals (name, price, quantity) VALUES (%s, %s, %s)"

            cursor.execute(sql, (name, price, quantity))
            db.commit()

            return jsonify({"message": "Animal added"}), 201

        else:
            cursor.execute("SELECT * FROM animals ORDER BY id")
            data = cursor.fetchall()

        return jsonify(data), 200

    finally:
        cursor.close()


@app.route("/animals/<int:id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def the_object(id):
    cursor = db.cursor(dictionary=True)

    try:
        if request.method == "GET":
            cursor.execute("SELECT * FROM animals WHERE id = %s", (id,))

            data = cursor.fetchone()

            return jsonify(data), 200

        if request.method == "PUT":
            data = request.get_json(silent=True) or {}
            name = data.get("name")
            price = data.get("price")
            quantity = data.get("quantity")

            sql = "UPDATE animals SET name = %s, price = %s, quantity = %s WHERE id = %s"

            cursor.execute(sql, (name, price, quantity, id))
            db.commit()

            return jsonify({"message": "data updated"}), 200

        # if request.method == "PATCH": #needs change
        #     data = request.get_json(silent=True) or {}
        #     name = data.get("name")
        #     price = data.get("price")
        #     quantity = data.get("quantity")
        #
        #     sql = "UPDATE animals SET name = %s, price = %s, quantity = %s WHERE id = %s"
        #
        #     cursor.execute(sql, (name, price, quantity, id))
        #     db.commit()
        #
        #     return jsonify({"message": "data updated"}), 200

        if request.method == "DELETE":
            sql = "DELETE FROM animals WHERE id = %s"

            cursor.execute(sql, (id,))
            db.commit()

            return jsonify({"message":"data deleted"}), 200

    finally:
        cursor.close()



if __name__ == "__main__":
    app.run(debug=True)
