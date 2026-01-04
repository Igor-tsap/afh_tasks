

from flask import Flask, request, render_template, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.secret_key = "123"
migrate = Migrate(app, db)



PRIORITY_HIGH = 1
PRIORITY_REGULAR = 2
PRIORITY_LOW = 3

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer, db.CheckConstraint("priority IN (1, 2, 3)"), nullable=False, default=2)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        task_priority = int(request.form["priority"])
        task_content = request.form["content"]

        new_task = Todo(content=task_content, priority= task_priority)

        try:
            db.session.add(new_task)
            db.session.commit()

            flash("Task was successfully added")
            return redirect(url_for("index"))

        except:
            return "There was an issue adding your task"

    else:
        tasks = Todo.query.order_by(
            Todo.priority,
            Todo.date_created
        ).all()
        return render_template("index.html", tasks = tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash("Task was successfully deleted")
        return redirect("/")

    except:
        return "There was a problem deleting that task"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]
        task.priority = int(request.form["priority"])

        try:
            db.session.commit()

            flash("Task was successfully updated")
            return redirect("/")

        except:
            return "There was an issue updating your task"

    else:
        return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
