from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    my_dict = {
        "dreamlike":"Dale",
        "uncanny":"Laura",
        "ominous":"Betty",
        "disquieting":"Rita",
        "surreal":"Henry",
        "hypnotic":"Jeffrey",
        "shadowed":"Frank",
        "eerie":"Dorothy",
        "fragmented":"Alvin",
        "subconscious":"Gordon"
}
    return render_template("index.html", my_list=my_list, my_dict=my_dict)



if __name__ == "__main__":
    app.run(debug=True)