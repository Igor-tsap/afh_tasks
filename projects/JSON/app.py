from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = "https://6972638632c6bacb12c6c80b.mockapi.io/animals"

@app.route("/")
def index():
    response = requests.get(URL)
    data = response.json()
    
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
