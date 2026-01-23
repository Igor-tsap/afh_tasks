from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = "https://6972638632c6bacb12c6c80b.mockapi.io/animals"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        response = requests.get(URL)
        data = response.json()
        return jsonify(data), response.status_code

    if request.method == "POST":
        u_input = request.json
        response = requests.post(URL, json=u_input)
        data = response.json()
        return jsonify(data), response.status_code

@app.route("/posts/<int:id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def the_object(id):
    if request.method == "GET":
        response = requests.get(f"{URL}/{id}")
        data = response.json()
        return jsonify(data), response.status_code

    if request.method == "PUT":
        u_input = request.json
        response = requests.put(f"{URL}/{id}", json=u_input)
        data = response.json()
        return jsonify(data), response.status_code

    if request.method == "PATCH":
        u_input = request.json
        response = requests.patch(f"{URL}/{id}", json=u_input)
        data = response.json()
        return jsonify(data), response.status_code

    if request.method == "DELETE":
        response = requests.delete(f"{URL}/{id}")
        data = {"deleted": True}
        return jsonify(data), response.status_code



if __name__ == "__main__":
    app.run(debug=True)
