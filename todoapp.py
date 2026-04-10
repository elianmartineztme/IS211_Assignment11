from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

todo_items = []


@app.route("/")
def index():
    return render_template("index.html", items=todo_items)


@app.route("/submit", methods=["POST"])
def submit():
    task = request.form.get("task", "").strip()
    email = request.form.get("email", "").strip()
    priority = request.form.get("priority", "").strip()

    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"

    if not task:
        return redirect("/")

    if not re.match(email_pattern, email):
        return redirect("/")

    if priority not in ["Low", "Medium", "High"]:
        return redirect("/")

    todo_items.append({
        "task": task,
        "email": email,
        "priority": priority
    })

    return redirect("/")


@app.route("/clear", methods=["POST"])
def clear():
    todo_items.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run()